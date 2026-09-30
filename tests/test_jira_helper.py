import tempfile
import unittest
from datetime import date
from pathlib import Path

from tools import jira_helper


class JiraHelperTests(unittest.TestCase):
    def test_resolves_query_parameters(self):
        jql = jira_helper.resolve_query(
            "release_scope",
            {"project": "MYM", "fix_version": "OCT-2026"},
        )
        self.assertIn("project = MYM", jql)
        self.assertIn('fixVersion = "OCT-2026"', jql)

    def test_requires_missing_query_parameters(self):
        with self.assertRaises(ValueError):
            jira_helper.resolve_query("release_scope", {"project": "MYM"})

    def test_redacts_possible_password(self):
        issue = {
            "key": "MYM-1",
            "fields": {
                "summary": "Example",
                "issuetype": {"name": "Bug"},
                "status": {"name": "To Do", "statusCategory": {"name": "To Do"}},
                "description": "Steps to reproduce\nlogin pw: SuperSecret123\nExpected: page loads\nActual: error",
            },
        }
        compact = jira_helper.compact_issue(issue)
        self.assertNotIn("SuperSecret123", compact["description"])
        self.assertIn("[REDACTED]", compact["description"])
        codes = {finding["code"] for finding in jira_helper.audit_issue(issue)}
        self.assertIn("possible_secret", codes)

    def test_flags_active_orphan_story(self):
        issue = {
            "key": "MYM-2",
            "fields": {
                "summary": "Standalone story",
                "issuetype": {"name": "Story"},
                "status": {"name": "To Do", "statusCategory": {"name": "To Do"}},
                "description": "Objective\nAcceptance Criteria\n- It works",
            },
        }
        codes = {finding["code"] for finding in jira_helper.audit_issue(issue)}
        self.assertIn("story_without_parent", codes)

    def test_flags_past_due_active_work(self):
        issue = {
            "key": "RAD-1",
            "fields": {
                "summary": "Old task",
                "issuetype": {"name": "Task"},
                "status": {"name": "In Progress", "statusCategory": {"name": "In Progress"}},
                "description": "Objective\nCompletion Criteria\n- Complete",
                "duedate": "2026-08-01",
            },
        }
        codes = {
            finding["code"]
            for finding in jira_helper.audit_issue(issue, today=date(2026, 9, 4))
        }
        self.assertIn("past_due", codes)

    def test_extracts_rovo_nodes_shape(self):
        payload = {"issues": {"nodes": [{"key": "MYM-1", "fields": {"summary": "One"}}]}}
        self.assertEqual("MYM-1", jira_helper.extract_issues(payload)[0]["key"])


GOOD_DESCRIPTION = (
    "Context\nCenters cannot see the capacity of instructors today.\n\n"
    "Acceptance criteria\nAC1: Given a full center, When a CD books, Then a warning is shown.\n"
)
GOOD_SUMMARY = "As a Center Director, I want to see instructor capacity so that I can avoid double booking."
NEW = "2026-10-05T10:00:00.000+0000"
OLD = "2026-08-01T10:00:00.000+0000"


def make_issue(issue_type="Story", summary=GOOD_SUMMARY, description=GOOD_DESCRIPTION, status="To Do", created=NEW, **fields):
    base = {
        "summary": summary,
        "issuetype": {"name": issue_type},
        "status": {"name": status, "statusCategory": {"name": "To Do" if status == "To Do" else "In Progress"}},
        "description": description,
        "created": created,
        "parent": {"key": "MYM-100"},
    }
    base.update(fields)
    return {"key": "MYM-9", "fields": base}


def codes(issue, **kwargs):
    return {finding["code"]: finding["severity"] for finding in jira_helper.audit_issue(issue, **kwargs)}


class StandardV2Tests(unittest.TestCase):
    def test_clean_story_has_no_findings(self):
        self.assertEqual({}, codes(make_issue(customfield_10021=3, customfield_11147=[{"value": "GP API"}])))

    def test_empty_and_near_empty_description(self):
        self.assertEqual("error", codes(make_issue(description=None))["work_description_empty"])
        self.assertEqual("error", codes(make_issue(description="see https://example.com/some/long/path"))["description_near_empty"])

    def test_missing_numbered_ac(self):
        result = codes(make_issue(description="Context\nSomething long enough to count as a real description here."))
        self.assertEqual("error", result["story_no_numbered_ac"])

    def test_summary_format_and_comma(self):
        self.assertEqual("error", codes(make_issue(summary="Improve scheduling"))["summary_format"])
        comma = "As a Center Director, I want to see capacity, so that I can avoid double booking."
        self.assertEqual("error", codes(make_issue(summary=comma))["summary_comma_before_so_that"])

    def test_bracket_must_be_a_code_dependency_value(self):
        self.assertNotIn("summary_bracket_not_allowed", codes(make_issue(summary="[GP API] " + GOOD_SUMMARY)))
        self.assertEqual("error", codes(make_issue(summary="[Calendar 2.0] " + GOOD_SUMMARY))["summary_bracket_not_allowed"])
        self.assertEqual("error", codes(make_issue(summary="[SPIKE] " + GOOD_SUMMARY))["summary_bracket_not_allowed"])
        self.assertEqual("error", codes(make_issue(summary="[GP API] [BE] " + GOOD_SUMMARY))["summary_multiple_brackets"])

    def test_retired_persona(self):
        summary = "As a Center Admin, I want to see capacity so that I can avoid double booking."
        self.assertEqual("error", codes(make_issue(summary=summary))["retired_persona"])
        summary = "As a Radius User, I want to see capacity so that I can avoid double booking."
        self.assertEqual("error", codes(make_issue(summary=summary))["retired_persona"])

    def test_market_adjective(self):
        good = "As a UK Center Director, I want to see capacity so that I can avoid double booking."
        self.assertNotIn("market_adjective_unknown", codes(make_issue(summary=good)))
        bad = "As a Kiwi Center Director, I want to see capacity so that I can avoid double booking."
        self.assertEqual("warning", codes(make_issue(summary=bad))["market_adjective_unknown"])

    def test_points_over_limit_only_when_committed(self):
        over = make_issue(customfield_10021=8, fixVersions=[{"name": "OCT-2026"}])
        self.assertEqual("error", codes(over)["points_over_limit_committed"])
        placeholder = make_issue(customfield_10021=8, fixVersions=[{"name": "N/A"}])
        self.assertNotIn("points_over_limit_committed", codes(placeholder))
        self.assertEqual("suggestion", codes(placeholder)["placeholder_fix_version"])

    def test_unestimated_with_fix_version(self):
        self.assertEqual("warning", codes(make_issue(fixVersions=[{"name": "OCT-2026-SR"}]))["unestimated_with_fix_version"])
        self.assertNotIn("unestimated_with_fix_version", codes(make_issue(fixVersions=[{"name": "FREEZE"}])))

    def test_subtasks_are_not_blanket_rejected(self):
        workflow = make_issue(
            issue_type="Sub-task",
            summary="Automate AC3 regression coverage",
            description="QA automation for the parent Story.",
        )
        self.assertNotIn("subtask_on_new_story", codes(workflow))
        self.assertNotIn("subtask_on_new_story", codes(make_issue(issue_type="Bug of Story")))

    def test_pull_requests_field_required_from_code_review(self):
        self.assertEqual("warning", codes(make_issue(status="CODE REVIEW"))["pull_requests_missing"])
        with_pr = make_issue(status="CODE REVIEW", customfield_11279="https://github.com/mathnasium/Radius/pull/1")
        self.assertNotIn("pull_requests_missing", codes(with_pr))
        self.assertNotIn("pull_requests_missing", codes(make_issue(status="To Do")))

    def test_story_without_epic(self):
        issue = make_issue()
        del issue["fields"]["parent"]
        self.assertEqual("warning", codes(issue)["story_without_parent"])

    def test_code_dependency_multiple_values(self):
        issue = make_issue(customfield_11147=[{"value": "Radius"}, {"value": "GP APP"}])
        self.assertEqual("warning", codes(issue)["code_dependency_multiple"])

    def test_long_description_and_constraint_implementation_detail(self):
        long = GOOD_DESCRIPTION + "x" * 2600
        self.assertEqual("suggestion", codes(make_issue(description=long))["description_long"])
        constraints = GOOD_DESCRIPTION + "\nConstraints\nUse the sp_GetCapacity stored procedure.\n"
        self.assertEqual("suggestion", codes(make_issue(description=constraints))["constraints_implementation_detail"])
        contract = GOOD_DESCRIPTION + "\nConstraints\nnull means inherit the center default, because Scheduling owns it.\n"
        self.assertNotIn("constraints_implementation_detail", codes(make_issue(description=contract)))

    def test_ac_change_after_approval_needs_history(self):
        history = {
            "histories": [
                {"created": "2026-10-06T09:00:00", "items": [{"field": "labels", "fromString": "", "toString": "ac-approved"}]},
                {"created": "2026-10-07T09:00:00", "items": [{"field": "description"}]},
            ]
        }
        issue = make_issue(labels=["ac-approved"])
        self.assertNotIn("ac_changed_without_changelog", codes(issue))  # no history: agent review
        issue["changelog"] = history
        self.assertEqual("warning", codes(issue)["ac_changed_without_changelog"])
        issue["fields"]["description"] = GOOD_DESCRIPTION + "\nChangelog\n- 2026-10-07: AC1 changed.\n"
        self.assertNotIn("ac_changed_without_changelog", codes(issue))
        untouched = make_issue(labels=["ac-approved"])
        untouched["changelog"] = {"histories": history["histories"][:1]}
        self.assertNotIn("ac_changed_without_changelog", codes(untouched))

    def test_legacy_stories_are_informational_until_refined(self):
        old = make_issue(summary="Improve scheduling", created=OLD)
        self.assertEqual("info", codes(old)["summary_format"])
        self.assertEqual("error", codes(old, refined=True)["summary_format"])

    def test_secrets_are_always_errors(self):
        old = make_issue(description="login pw: SuperSecret123", created=OLD)
        self.assertEqual("error", codes(old)["possible_secret"])

    def test_bug_description_checks(self):
        empty = make_issue(issue_type="Bug", description=None, summary="Cancel fails")
        self.assertEqual("error", codes(empty)["bug_description_empty"])
        thin = make_issue(issue_type="Bug", description="It is broken somehow for some users.", summary="Cancel fails")
        self.assertIn("bug_impact_missing", codes(thin))

    def test_watchlist_bug_with_fix_version(self):
        bug = make_issue(
            issue_type="Bug",
            summary="Cancel fails",
            description="Observed: error. Expected: cancel. Steps: click. Environment: prod. Impact: high.",
            customfield_11016={"value": "Watchlist issue"},
            fixVersions=[{"name": "OCT-2026"}],
        )
        self.assertEqual("warning", codes(bug)["watchlist_with_fix_version"])

    def test_task_and_spike(self):
        task = make_issue(issue_type="Task", summary="[Scheduling Microservice] Add OTLP metrics", description="Objective\nAdd metrics to the fanout service for tracing.")
        self.assertEqual("warning", codes(task)["completion_criteria_unclear"])
        spike = make_issue(issue_type="Spike", summary="Evaluate queue options", description="Look at a few queue products and report back to the team.")
        self.assertEqual("warning", codes(spike)["spike_missing_question"])

    def test_committed_queries_resolve(self):
        jql = jira_helper.resolve_query("committed_work", {})
        self.assertIn('fixVersion not in ("N/A", "FREEZE")', jql)
        self.assertIn("cf[10021] > 5", jira_helper.resolve_query("oversized_or_unestimated_committed", {}))
        for name in ("empty_descriptions", "missing_pr_field", "stories_without_epic", "placeholder_fix_versions"):
            self.assertTrue(jira_helper.resolve_query(name, {}))
        with self.assertRaises(KeyError):
            jira_helper.resolve_query("committed_story_bugs", {})


if __name__ == "__main__":
    unittest.main()

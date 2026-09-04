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


if __name__ == "__main__":
    unittest.main()

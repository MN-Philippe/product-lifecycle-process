import json
import re
import shutil
import subprocess
import unittest

from tools import build_plugin

GUARD = build_plugin.PLUGIN_DIR / "hooks" / "guard.sh"


def run_guard(tool_name, **tool_input):
    payload = json.dumps({"hook_event_name": "PreToolUse", "tool_name": tool_name, "tool_input": tool_input})
    return subprocess.run(["bash", str(GUARD)], input=payload, capture_output=True, text=True)


def kind(tool_name, **tool_input):
    result = run_guard(tool_name, **tool_input)
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"] if result.stdout.strip() else None


@unittest.skipUnless(shutil.which("bash"), "bash required")
class GitHubIsReadOnlyTests(unittest.TestCase):
    def test_connector_writes_are_denied(self):
        for tool in (
            "create_issue", "issue_write", "add_issue_comment", "update_pull_request", "create_pull_request",
            "merge_pull_request", "pull_request_review_write", "push_files", "create_or_update_file",
            "sub_issue_write", "actions_run_trigger", "resolve_review_thread",
        ):
            self.assertEqual("deny", kind(f"mcp__github__{tool}"), tool)

    def test_connector_reads_are_allowed(self):
        for tool in ("get_file_contents", "list_pull_requests", "search_code", "pull_request_read", "issue_read", "actions_get"):
            self.assertIsNone(kind(f"mcp__github__{tool}"), tool)

    def test_other_connector_naming_is_still_caught(self):
        self.assertEqual("deny", kind("mcp__claude_ai_GitHub__create_issue"))

    def test_command_line_issue_and_pr_writes_are_denied(self):
        for command in (
            "gh issue create --title x",
            "gh pr comment 6 --body hi",
            "gh pr merge 6",
            "cd repo && gh pr edit 6 --title y",
            "gh api repos/o/r/issues -f title=x",
            "gh api -X POST repos/o/r/issues",
            "gh api --method PATCH repos/o/r/pulls/6",
            'curl -X POST https://api.github.com/repos/o/r/issues -d "{}"',
        ):
            self.assertEqual("deny", kind("Bash", command=command), command)

    def test_reads_and_local_git_are_allowed(self):
        for command in (
            "gh pr view 6", "gh issue list", "gh api repos/o/r/pulls/6", "git status", "git log --oneline",
            "git push origin claude/my-branch", "git push -u origin HEAD", "ls",
        ):
            self.assertIsNone(kind("Bash", command=command), command)

    def test_browser_interaction_on_github_is_denied_but_reading_is_not(self):
        self.assertEqual("deny", kind("mcp__Claude_in_Chrome__form_input", url="https://github.com/o/r/issues/new"))
        self.assertEqual("deny", kind("mcp__chrome__click", page="github.com/o/r/pull/6"))
        self.assertIsNone(kind("mcp__Claude_in_Chrome__navigate", url="https://github.com/o/r/pull/6"))
        self.assertIsNone(kind("mcp__Claude_in_Chrome__read_page", url="https://example.com"))


@unittest.skipUnless(shutil.which("bash"), "bash required")
class JiraWritesAskTests(unittest.TestCase):
    def test_writes_ask(self):
        for tool in ("createJiraIssue", "editJiraIssue", "addCommentToJiraIssue", "transitionJiraIssue", "createIssueLink", "addWorklogToJiraIssue"):
            self.assertEqual("ask", kind(f"mcp__Atlassian__{tool}"), tool)

    def test_reads_do_not_ask(self):
        for tool in ("getJiraIssue", "searchJiraIssuesUsingJql", "getIssueLinkTypes", "getTransitionsForJiraIssue", "lookupJiraAccountId"):
            self.assertIsNone(kind(f"mcp__Atlassian__{tool}"), tool)

    def test_unrelated_tools_are_untouched(self):
        self.assertIsNone(kind("Read", file_path="/tmp/x"))
        self.assertIsNone(kind("Bash", command="ls"))

    def test_prompt_explains_batch_behavior(self):
        out = json.loads(run_guard("mcp__Atlassian__createJiraIssue").stdout)
        self.assertIn("once per Story", out["hookSpecificOutput"]["permissionDecisionReason"])


@unittest.skipUnless(shutil.which("bash"), "bash required")
class HookWiringTests(unittest.TestCase):
    def test_hooks_json_runs_the_bash_guard_without_python(self):
        config = json.loads((GUARD.parent / "hooks.json").read_text(encoding="utf-8"))
        command = config["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
        self.assertEqual('bash "${CLAUDE_PLUGIN_ROOT}/hooks/guard.sh"', command)
        self.assertNotIn("python", GUARD.read_text(encoding="utf-8").lower().replace("no python", ""))

    def test_bad_input_fails_open(self):
        for payload in ("not json", "", "{}"):
            result = subprocess.run(["bash", str(GUARD)], input=payload, capture_output=True, text=True)
            self.assertEqual(0, result.returncode)
            self.assertEqual("", result.stdout)

    def test_hook_changes_require_a_plugin_rebuild(self):
        self.assertTrue(build_plugin.is_current(), "Run: python tools/build_plugin.py")


class WritePolicyTests(unittest.TestCase):
    def test_policy_is_in_one_standard_and_bundled(self):
        source = (build_plugin.ROOT / "standards" / "jira-conventions.md").read_text(encoding="utf-8")
        self.assertIn("## Write policy", source)
        bundled = (build_plugin.REFERENCES_DIR / "jira-conventions.md").read_text(encoding="utf-8")
        self.assertIn("read-only", bundled)

    def test_policy_leaves_local_git_alone_and_states_batch_rule_once(self):
        source = (build_plugin.ROOT / "standards" / "jira-conventions.md").read_text(encoding="utf-8")
        self.assertIn("`git push` to a working branch, is not covered", source)
        self.assertIn("every Story's full draft", source)
        self.assertNotIn("approved as a batch", source)

    def test_skill_points_at_the_policy_instead_of_restating_it(self):
        skill = (build_plugin.SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/jira-conventions.md#write-policy", skill)
        self.assertNotIn("looks good so far", skill)

    def test_no_playbook_tells_the_agent_to_create_github_items(self):
        for path in (build_plugin.ROOT / "playbooks").glob("*.md"):
            text = path.read_text(encoding="utf-8").lower()
            self.assertFalse(re.search(r"create (?:a |an )?github|open (?:a |an )?github issue", text), path.name)


if __name__ == "__main__":
    unittest.main()

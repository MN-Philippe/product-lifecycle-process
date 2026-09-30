import importlib.util
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

from tools import build_plugin

GUARD_PATH = build_plugin.PLUGIN_DIR / "hooks" / "guard.py"
spec = importlib.util.spec_from_file_location("guard", GUARD_PATH)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


def kind(tool_name, **tool_input):
    result = guard.decide({"tool_name": tool_name, "tool_input": tool_input})
    return result["hookSpecificOutput"]["permissionDecision"] if result else None


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

    def test_command_line_writes_are_denied(self):
        for command in (
            "gh issue create --title x",
            "gh pr comment 6 --body hi",
            "gh pr merge 6",
            "gh api repos/o/r/issues -f title=x",
            "gh api -X POST repos/o/r/issues",
            "git push origin main",
            "cd repo && git push --dry-run",
            'curl -X POST https://api.github.com/repos/o/r/issues -d "{}"',
        ):
            self.assertEqual("deny", kind("Bash", command=command), command)

    def test_command_line_reads_are_allowed(self):
        for command in ("gh pr view 6", "gh issue list", "gh api repos/o/r/pulls/6", "git status", "git log --oneline"):
            self.assertIsNone(kind("Bash", command=command), command)

    def test_browser_interaction_on_github_is_denied_but_reading_is_not(self):
        self.assertEqual("deny", kind("mcp__Claude_in_Chrome__form_input", url="https://github.com/o/r/issues/new"))
        self.assertEqual("deny", kind("mcp__chrome__click", page="github.com/o/r/pull/6"))
        self.assertIsNone(kind("mcp__Claude_in_Chrome__navigate", url="https://github.com/o/r/pull/6"))
        self.assertIsNone(kind("mcp__Claude_in_Chrome__read_page", url="https://example.com"))


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


class HookWiringTests(unittest.TestCase):
    def test_hooks_json_points_at_the_guard(self):
        config = json.loads((GUARD_PATH.parent / "hooks.json").read_text(encoding="utf-8"))
        command = config["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
        self.assertIn("${CLAUDE_PLUGIN_ROOT}/hooks/guard.py", command)

    def test_script_emits_a_decision_and_fails_open_on_bad_input(self):
        denied = subprocess.run(
            [sys.executable, str(GUARD_PATH)],
            input=json.dumps({"tool_name": "mcp__github__create_issue", "tool_input": {}}),
            capture_output=True, text=True,
        )
        self.assertEqual(0, denied.returncode)
        self.assertEqual("deny", json.loads(denied.stdout)["hookSpecificOutput"]["permissionDecision"])
        broken = subprocess.run([sys.executable, str(GUARD_PATH)], input="not json", capture_output=True, text=True)
        self.assertEqual(0, broken.returncode)
        self.assertEqual("", broken.stdout)

    def test_hook_changes_require_a_plugin_rebuild(self):
        self.assertTrue(build_plugin.is_current(), "Run: python tools/build_plugin.py")


class WritePolicyTests(unittest.TestCase):
    def test_policy_is_in_one_standard_and_bundled(self):
        source = (build_plugin.ROOT / "standards" / "jira-conventions.md").read_text(encoding="utf-8")
        self.assertIn("## Write policy", source)
        bundled = (build_plugin.REFERENCES_DIR / "jira-conventions.md").read_text(encoding="utf-8")
        self.assertIn("GitHub is read-only", bundled)

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

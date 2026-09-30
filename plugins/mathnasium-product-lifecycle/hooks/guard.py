#!/usr/bin/env python3
"""PreToolUse guard for the mathnasium-product-lifecycle plugin.

Backs up the write policy in standards/jira-conventions.md so it does not depend on the
model following instructions:

* GitHub is read-only: GitHub connector writes, `gh` and `git push` writes, and browser
  interactions on github.com are denied.
* Every Jira write (create, edit, comment, transition, link, worklog) asks the user to
  confirm, even when the connector is set to "always allow".

Reads the hook payload as JSON on stdin and prints a PreToolUse decision. Fails open on
unreadable input so a broken hook never blocks all work. Browser detection is best-effort:
it cannot see what a coordinate click lands on.
"""

from __future__ import annotations

import json
import re
import sys
from typing import Any

GITHUB_READ_TOOLS = re.compile(
    r"^(get_|list_|search_|issue_read$|pull_request_read$|actions_get$|actions_list$|run_secret_scanning$)"
)
JIRA_WRITE_TOOL = re.compile(
    r"(?i)^(create|edit|update|add|transition|delete|assign|link|remove|set)\w*"
)
BASH_GITHUB_WRITE = [
    re.compile(
        r"\bgh\s+(?:issue|pr|release|repo|label|gist|project|discussion|workflow|run|ruleset|secret|variable)\s+"
        r"(?:create|comment|edit|close|reopen|merge|review|delete|transfer|lock|unlock|ready|rerun|cancel|fork|"
        r"archive|rename|sync|run|enable|disable|set|add|remove)\b"
    ),
    re.compile(r"\bgh\s+api\b.*(?:-X\s*(?!GET\b)\w+|--method\s+(?!GET\b)\w+|\s-f\s|\s-F\s|--field|--raw-field|--input)"),
    re.compile(r"\bgit\s+push\b"),
    re.compile(r"api\.github\.com.*(?:-X\s*(?:POST|PATCH|PUT|DELETE)|--request\s+(?:POST|PATCH|PUT|DELETE)|\s-d\s|--data)", re.I),
]
BROWSER_TOOL = re.compile(r"(?i)chrome|browser|playwright|puppeteer|computer")
BROWSER_INTERACTION = re.compile(r"(?i)click|type|fill|form_input|press|submit|key|select|upload|drag|write")

GITHUB_DENY = (
    "GitHub is read-only in this plugin. Reading repos, code and pull requests is fine; creating, commenting on, "
    "editing or closing GitHub issues or pull requests, and pushing, is not. Tell the user you won't do it and stop. "
    "(Jira Stories are the work items here; a repo means a Code Dependency value.)"
)
JIRA_ASK = (
    "Jira write: confirm only if the user approved this exact draft (or before/after) in a later reply. "
    "See standards/jira-conventions.md#write-policy."
)


def _decision(kind: str, reason: str) -> dict[str, Any]:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": kind,
            "permissionDecisionReason": reason,
        }
    }


def _split_tool(name: str) -> tuple[str, str]:
    """(server, tool) for mcp__server__tool names; ("", name) otherwise."""
    if name.startswith("mcp__"):
        parts = name.split("__", 2)
        if len(parts) == 3:
            return parts[1], parts[2]
    return "", name


def decide(payload: dict[str, Any]) -> dict[str, Any] | None:
    """Return a PreToolUse decision, or None to leave the call to normal permissions."""
    name = str(payload.get("tool_name") or "")
    tool_input = payload.get("tool_input") or {}
    server, tool = _split_tool(name)

    if server and "github" in server.lower():
        if not GITHUB_READ_TOOLS.match(tool):
            return _decision("deny", GITHUB_DENY)
        return None

    if name == "Bash":
        command = str(tool_input.get("command") or "")
        if any(pattern.search(command) for pattern in BASH_GITHUB_WRITE):
            return _decision("deny", GITHUB_DENY)
        return None

    if BROWSER_TOOL.search(name):
        blob = json.dumps(tool_input).lower()
        if "github.com" in blob and BROWSER_INTERACTION.search(name + " " + blob):
            return _decision("deny", GITHUB_DENY)

    if server and ("jira" in tool.lower() or "issuelink" in tool.lower()) and JIRA_WRITE_TOOL.match(tool):
        return _decision("ask", JIRA_ASK)

    return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        print("guard.py: unreadable hook input; allowing", file=sys.stderr)
        return 0
    result = decide(payload if isinstance(payload, dict) else {})
    if result:
        print(json.dumps(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Stateless helpers for AI agents working with live Jira data.

This module intentionally does not authenticate to Jira or persist Jira results.
Use the active agent/connector to fetch current Jira data, then use this helper
for shared query resolution, compact context, redaction, and deterministic
quality checks.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any, Iterable

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUERY_FILE = ROOT / "jira" / "queries.yaml"

_SECRET_PATTERNS = [
    re.compile(r"(?i)\b(password|passwd|pwd|pw)\b\s*[:=]\s*([^\s,;]+)"),
    re.compile(r"(?i)\b(api[_ -]?key|access[_ -]?token|secret)\b\s*[:=]\s*([^\s,;]+)"),
    re.compile(r"(?i)\bauthorization\s*:\s*bearer\s+([^\s]+)"),
]


def _flatten_adf(value: Any) -> str:
    """Best-effort extraction of readable text from Jira ADF or plain JSON."""
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n".join(filter(None, (_flatten_adf(item) for item in value)))
    if isinstance(value, dict):
        if isinstance(value.get("text"), str):
            return value["text"]
        if value.get("type") == "hardBreak":
            return "\n"
        if value.get("content") is not None:
            return _flatten_adf(value["content"])
        return "\n".join(filter(None, (_flatten_adf(item) for item in value.values())))
    return str(value)


def contains_possible_secret(text: str) -> bool:
    return any(pattern.search(text or "") for pattern in _SECRET_PATTERNS)


def redact_text(text: str) -> str:
    """Redact likely credential values without echoing them to output."""
    redacted = text or ""
    for pattern in _SECRET_PATTERNS:
        if "authorization" in pattern.pattern.lower():
            redacted = pattern.sub("Authorization: Bearer [REDACTED]", redacted)
        else:
            redacted = pattern.sub(lambda match: f"{match.group(1)}: [REDACTED]", redacted)
    return redacted


def _name(value: Any) -> str | None:
    if isinstance(value, dict):
        return value.get("name") or value.get("key") or value.get("displayName")
    return value if isinstance(value, str) else None


def compact_issue(issue: dict[str, Any]) -> dict[str, Any]:
    """Return a compact, secret-redacted runtime view of a Jira issue."""
    fields = issue.get("fields") if isinstance(issue.get("fields"), dict) else issue
    parent = fields.get("parent") if isinstance(fields.get("parent"), dict) else None
    fix_versions = fields.get("fixVersions") or []
    labels = fields.get("labels") or []
    description = redact_text(_flatten_adf(fields.get("description"))).strip()
    status = fields.get("status") if isinstance(fields.get("status"), dict) else None

    return {
        "key": issue.get("key") or fields.get("key"),
        "summary": fields.get("summary"),
        "issue_type": _name(fields.get("issuetype")),
        "status": _name(fields.get("status")),
        "status_category": _name(status.get("statusCategory")) if status else None,
        "priority": _name(fields.get("priority")),
        "assignee": _name(fields.get("assignee")),
        "parent": parent.get("key") if parent else None,
        "due_date": fields.get("duedate"),
        "fix_versions": [version.get("name") for version in fix_versions if isinstance(version, dict)],
        "labels": labels if isinstance(labels, list) else [],
        "description": description,
    }


def extract_issues(payload: Any) -> list[dict[str, Any]]:
    """Accept common Jira/connector payload shapes and return issue dictionaries."""
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if not isinstance(payload, dict):
        return []
    if payload.get("key") or payload.get("fields"):
        return [payload]

    issues = payload.get("issues")
    if isinstance(issues, list):
        return [item for item in issues if isinstance(item, dict)]
    if isinstance(issues, dict) and isinstance(issues.get("nodes"), list):
        return [item for item in issues["nodes"] if isinstance(item, dict)]
    if isinstance(payload.get("nodes"), list):
        return [item for item in payload["nodes"] if isinstance(item, dict)]
    return []


def _active(issue: dict[str, Any]) -> bool:
    category = (issue.get("status_category") or "").lower()
    return category not in {"done", "complete", "completed"}


def _links_only_or_too_thin(text: str) -> bool:
    without_urls = re.sub(r"https?://\S+", " ", text or "")
    meaningful = re.sub(r"[^A-Za-z0-9]+", "", without_urls)
    return bool(text.strip()) and len(meaningful) < 30


def audit_issue(issue: dict[str, Any], today: date | None = None) -> list[dict[str, str]]:
    """Run lightweight deterministic checks. Findings are guidance, not Jira truth."""
    today = today or date.today()
    compact = compact_issue(issue)
    raw_fields = issue.get("fields") if isinstance(issue.get("fields"), dict) else issue
    raw_description = _flatten_adf(raw_fields.get("description"))
    issue_type = (compact.get("issue_type") or "").lower()
    description = compact.get("description") or ""
    findings: list[dict[str, str]] = []

    def add(severity: str, code: str, message: str) -> None:
        findings.append({"severity": severity, "code": code, "message": message})

    if contains_possible_secret(raw_description):
        add(
            "error",
            "possible_secret",
            "Description may contain a credential or secret. Review and remove/rotate it; the value is not echoed here.",
        )

    if not _active(compact):
        return findings

    if issue_type == "epic":
        if not description:
            add("error", "epic_description_empty", "Active Epic has no description or durable outcome context.")
        elif _links_only_or_too_thin(description):
            add(
                "warning",
                "epic_context_thin",
                "Epic context appears too thin or mostly link-based; verify the outcome can be understood without chasing external context.",
            )

    if issue_type in {"story", "task"}:
        if issue_type == "story" and not compact.get("parent"):
            add(
                "warning",
                "story_without_parent",
                "Active Story has no parent. Confirm whether it is intentional standalone work or should contribute to an initiative.",
            )
        if not description:
            add("error", "work_description_empty", f"Active {compact.get('issue_type') or 'work item'} has no description.")
        elif not re.search(
            r"(?i)acceptance|completion criteria|expected result|done when|definition of done",
            description,
        ):
            add(
                "warning",
                "completion_criteria_unclear",
                "No obvious acceptance/completion criteria signal was found. Confirm the item has a testable definition of complete.",
            )

    if issue_type == "bug":
        if not description:
            add("error", "bug_description_empty", "Active Bug has no diagnostic description.")
        else:
            if not re.search(r"(?i)steps? to reproduce|reproduc|\brepro\b", description):
                add("warning", "bug_reproduction_missing", "No obvious reproduction steps were found.")
            if not re.search(r"(?i)expected|should", description):
                add("warning", "bug_expected_missing", "Expected behavior is not obvious.")
            if not re.search(r"(?i)actual|observed|currently|error|issue", description):
                add("warning", "bug_observed_missing", "Observed/actual behavior is not obvious.")

    due_date = compact.get("due_date")
    if isinstance(due_date, str):
        try:
            if date.fromisoformat(due_date) < today:
                add("warning", "past_due", f"Due date {due_date} has passed while the issue remains active.")
        except ValueError:
            add("warning", "invalid_due_date", "Due date could not be parsed as YYYY-MM-DD.")

    return findings


def audit_collection(issues: Iterable[dict[str, Any]], today: date | None = None) -> list[dict[str, Any]]:
    issue_list = list(issues)
    compact_by_key = {
        compact["key"]: compact
        for compact in (compact_issue(issue) for issue in issue_list)
        if compact.get("key")
    }
    output = []

    for issue in issue_list:
        compact = compact_issue(issue)
        findings = audit_issue(issue, today=today)
        parent_key = compact.get("parent")
        parent = compact_by_key.get(parent_key)
        if parent and _active(compact):
            child_category = (compact.get("status_category") or "").lower()
            parent_status = (parent.get("status") or "").lower()
            if child_category in {"in progress", "indeterminate"} and parent_status in {"to do", "todo", "open"}:
                findings.append(
                    {
                        "severity": "warning",
                        "code": "parent_status_lags_children",
                        "message": f"Child is active/in progress while parent {parent_key} is still {parent.get('status')}. Verify Epic status remains meaningful.",
                    }
                )
        output.append({"issue": compact, "findings": findings})
    return output


def load_queries(path: Path = DEFAULT_QUERY_FILE) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    return data.get("queries") or {}


def resolve_query(name: str, params: dict[str, str], path: Path = DEFAULT_QUERY_FILE) -> str:
    queries = load_queries(path)
    if name not in queries:
        raise KeyError(f"Unknown query preset: {name}")
    spec = queries[name] or {}
    query = spec.get("jql") or spec.get("template")
    if not query:
        raise ValueError(f"Query preset {name} has no jql/template")

    placeholders = set(re.findall(r"{{\s*([A-Za-z0-9_]+)\s*}}", query))
    missing = sorted(placeholders - params.keys())
    if missing:
        raise ValueError(f"Missing parameters for {name}: {', '.join(missing)}")

    for key in placeholders:
        value = params[key].replace("\\", "\\\\").replace('"', '\\"')
        query = re.sub(r"{{\s*" + re.escape(key) + r"\s*}}", value, query)
    return " ".join(query.split())


def _load_json(path: str) -> Any:
    if path == "-":
        return json.load(sys.stdin)
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _parse_params(values: list[str]) -> dict[str, str]:
    params: dict[str, str] = {}
    for value in values:
        if "=" not in value:
            raise ValueError(f"Parameter must use name=value: {value}")
        key, item = value.split("=", 1)
        params[key] = item
    return params


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    list_cmd = sub.add_parser("list", help="List named Jira query presets")
    list_cmd.add_argument("--queries", type=Path, default=DEFAULT_QUERY_FILE)

    query_cmd = sub.add_parser("query", help="Resolve a named query preset into JQL")
    query_cmd.add_argument("name")
    query_cmd.add_argument("--param", action="append", default=[], metavar="NAME=VALUE")
    query_cmd.add_argument("--queries", type=Path, default=DEFAULT_QUERY_FILE)

    context_cmd = sub.add_parser("context", help="Compact and redact live Jira JSON for agent context")
    context_cmd.add_argument("json_file", help="Jira JSON file or - for stdin")

    audit_cmd = sub.add_parser("audit", help="Audit live Jira JSON without writing to Jira")
    audit_cmd.add_argument("json_file", help="Jira JSON file or - for stdin")
    audit_cmd.add_argument("--today", help="Override current date for deterministic runs (YYYY-MM-DD)")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "list":
            for name, spec in load_queries(args.queries).items():
                print(f"{name}\t{(spec or {}).get('description', '')}")
            return 0

        if args.command == "query":
            print(resolve_query(args.name, _parse_params(args.param), args.queries))
            return 0

        issues = extract_issues(_load_json(args.json_file))
        if not issues:
            raise ValueError("No Jira issues found in the supplied JSON payload")

        if args.command == "context":
            print(json.dumps([compact_issue(issue) for issue in issues], indent=2))
            return 0

        if args.command == "audit":
            audit_today = date.fromisoformat(args.today) if args.today else None
            print(json.dumps(audit_collection(issues, today=audit_today), indent=2))
            return 0

    except (KeyError, ValueError, OSError, yaml.YAMLError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

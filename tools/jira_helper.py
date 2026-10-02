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

# Advisory rule implementation; live Confluence standards are authoritative.
# Story: https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2162393089
# Jira: https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2162130987
EFFECTIVE_DATE = date(2026, 10, 1)  # DEFAULT — TBC: standards/story.md#applies-to
MAX_STORY_POINTS = 5
STORY_POINTS_FIELD = "customfield_10021"
PULL_REQUESTS_FIELD = "customfield_11279"
CODE_DEPENDENCY_FIELD = "customfield_11147"
CONFIRMED_ISSUE_FIELD = "customfield_11016"

CODE_DEPENDENCY_OPTIONS = {
    "Radius",
    "Scheduling Microservice",
    "Notifications Microservice",
    "GP APP",
    "GP API",
    "Data Access Layer",
    "Database",
    "Scheduling Fanout",
    "Radius Emails",
}
RETIRED_PERSONAS = {
    "center admin",
    "user",
    "radius user",
    "admin user",
    "center owner",
    "support admin",
    "developer",
}
KNOWN_PERSONAS = [
    "assistant center director",
    "acd",
    "center director",
    "cd",
    "franchise owner",
    "fo",
    "admin",
    "guardian",
    "instructor",
    "education manager",
    "regional manager",
]
MARKET_ADJECTIVES = {
    "canadian",
    "uk",
    "australian",
    "romanian",
    "mexican",
    "saudi",
    "singaporean",
    "international",
}
# Statuses at Code Review or later (lower case); mirrors missing_pr_field in jira/queries.yaml.
CODE_REVIEW_OR_LATER = {
    "code review",
    "in code review",
    "in qa - htd",
    "in qa - mathnasium",
    "in progress - qa",
    "ready for stg",
    "ready for qa in stg",
    "ready for prod",
}
PLACEHOLDER_FIX_VERSIONS = {"n/a", "freeze"}
COMMITTED_VERSION = re.compile(r"^(?:[A-Z]{3}-\d{4}(?:-SR\d*)?|HOTFIX)$")
LONG_DESCRIPTION_CHARS = 2500
IMPLEMENTATION_DETAIL = re.compile(
    r"(?i)stored procedure|\bclass\b|controller|service method|\bsp_\w+|\.cs\b|\bdto\b"
)

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
        return value.get("name") or value.get("value") or value.get("key") or value.get("displayName")
    return value if isinstance(value, str) else None


def _values(value: Any) -> list[str]:
    """Names from a single- or multi-value Jira field."""
    if value is None:
        return []
    items = value if isinstance(value, list) else [value]
    return [name for name in (_name(item) for item in items) if name]


def _number(value: Any) -> float | None:
    try:
        return float(value) if value is not None else None
    except (TypeError, ValueError):
        return None


def _created(fields: dict[str, Any]) -> date | None:
    raw = fields.get("created")
    if isinstance(raw, str):
        try:
            return date.fromisoformat(raw[:10])
        except ValueError:
            return None
    return None


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
        "created": fields.get("created"),
        "story_points": _number(fields.get(STORY_POINTS_FIELD)),
        "pull_requests": bool(_flatten_adf(fields.get(PULL_REQUESTS_FIELD)).strip()) if fields.get(PULL_REQUESTS_FIELD) else False,
        "code_dependency": _values(fields.get(CODE_DEPENDENCY_FIELD)),
        "confirmed_issue": _name(fields.get(CONFIRMED_ISSUE_FIELD)),
        "parent_type": _name(parent["fields"].get("issuetype")) if parent and isinstance(parent.get("fields"), dict) else None,
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


_SUMMARY_FORMAT = re.compile(
    r"^(?:\[[^\]]+\]\s*)?As an? (?P<persona>[^,]+?), I want (?P<want>.+?)(?P<comma>,)? so that (?P<outcome>.+?)\.?$",
    re.IGNORECASE,
)
_AC_PATTERN = re.compile(r"(?i)\bAC\s?\d+\b")
_SECTION_HEADINGS = (
    "context|current behavior|acceptance criteria|constraints|out of scope|open questions|changelog"
)


def _section(description: str, name: str) -> str:
    """Text of a named description section, up to the next standard heading."""
    match = re.search(
        rf"(?ims)^\s*{name}\s*:?\s*$(.*?)(?=^\s*(?:{_SECTION_HEADINGS})\s*:?\s*$|\Z)",
        description or "",
    )
    return match.group(1) if match else ""


def _split_persona(persona: str) -> tuple[str, str]:
    """Return (market/other prefix, known persona core) for a Summary persona."""
    cleaned = re.sub(r"\s*\(.*?\)", "", persona).strip().lower()
    for core in sorted(KNOWN_PERSONAS, key=len, reverse=True):
        if cleaned == core:
            return "", core
        if cleaned.endswith(" " + core):
            return cleaned[: -len(core)].strip(), core
    return cleaned, ""


def _is_committed(fix_versions: list[str]) -> bool:
    return any(COMMITTED_VERSION.match(version or "") for version in fix_versions)


def _ac_edited_after_approval(issue: dict[str, Any]) -> bool | None:
    """True/False from Jira changelog history; None when no history was supplied."""
    changelog = issue.get("changelog")
    histories = changelog.get("histories") if isinstance(changelog, dict) else None
    if not isinstance(histories, list):
        return None
    events = []
    for history in histories:
        for item in history.get("items") or []:
            events.append((history.get("created") or "", item))
    events.sort(key=lambda event: event[0])
    approved_at = None
    for created, item in events:
        if item.get("field") == "labels" and "ac-approved" in (item.get("toString") or "").split():
            if "ac-approved" not in (item.get("fromString") or "").split():
                approved_at = approved_at or created
    if approved_at is None:
        return False
    return any(item.get("field") == "description" and created > approved_at for created, item in events)


def audit_issue(
    issue: dict[str, Any],
    today: date | None = None,
    refined: bool = False,
) -> list[dict[str, str]]:
    """Run deterministic checks. Findings are guidance, not Jira truth.

    Checks for Stories, Tasks and Bugs created before EFFECTIVE_DATE are reported at
    "info" severity unless ``refined`` is set (standards/story.md#applies-to).
    Possible secrets are always errors.
    """
    today = today or date.today()
    compact = compact_issue(issue)
    raw_fields = issue.get("fields") if isinstance(issue.get("fields"), dict) else issue
    raw_description = _flatten_adf(raw_fields.get("description"))
    issue_type = (compact.get("issue_type") or "").lower()
    description = compact.get("description") or ""
    summary = (compact.get("summary") or "").strip()
    status = (compact.get("status") or "").lower()
    fix_versions = compact.get("fix_versions") or []
    points = compact.get("story_points")
    created = _created(raw_fields)
    legacy = created is not None and created < EFFECTIVE_DATE and not refined
    findings: list[dict[str, str]] = []

    def add(severity: str, code: str, message: str, always: bool = False) -> None:
        if legacy and not always and issue_type in {"story", "task", "bug", "spike"}:
            severity = "info"
        findings.append({"severity": severity, "code": code, "message": message})

    if contains_possible_secret(raw_description):
        add(
            "error",
            "possible_secret",
            "Description may contain a credential or secret. Review and remove/rotate it; the value is not echoed here.",
            always=True,
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

    if issue_type in {"story", "task", "spike"}:
        brackets = re.findall(r"\[([^\]]+)\]", summary)
        if len(brackets) > 1:
            add("error", "summary_multiple_brackets", "Summary has more than one bracket; only one repo bracket is allowed.")
        for bracket in brackets[:1]:
            if bracket not in CODE_DEPENDENCY_OPTIONS:
                add(
                    "error",
                    "summary_bracket_not_allowed",
                    f"Bracket [{bracket}] is not exactly a Code Dependency value. Feature names, [SPIKE], [PoC] and status markers are not allowed.",
                )

    if issue_type in {"story", "task"}:
        if points is not None and points > MAX_STORY_POINTS and _is_committed(fix_versions):
            add("error", "points_over_limit_committed", f"{points:g} Story Points with a committed Fix Version; the limit is {MAX_STORY_POINTS}. Split the Story.")
        if points is None and _is_committed(fix_versions):
            add("warning", "unestimated_with_fix_version", "Committed Fix Version but no Story Points.")
        if len(compact.get("code_dependency") or []) > 1:
            add("warning", "code_dependency_multiple", "Code Dependency has more than one value; likely a multi-repo Story that should be split.")

    if issue_type in {"story", "task", "bug"}:
        if {version.lower() for version in fix_versions} & PLACEHOLDER_FIX_VERSIONS:
            add("suggestion", "placeholder_fix_version", "Active item has a placeholder Fix Version (N/A or FREEZE), which is not a delivery commitment.")
        if status in CODE_REVIEW_OR_LATER and not compact.get("pull_requests"):
            add("warning", "pull_requests_missing", "Status is Code Review or later but the Pull Requests field is empty.")

    if issue_type in {"story", "task"}:
        if issue_type == "story" and not compact.get("parent"):
            add(
                "warning",
                "story_without_parent",
                "Active Story has no Epic. Confirm whether it is intentional standalone work or should belong to an Epic.",
            )
        if not description:
            add("error", "work_description_empty", f"Active {compact.get('issue_type') or 'work item'} has no description.")
        elif _links_only_or_too_thin(description):
            add("error", "description_near_empty", f"Active {compact.get('issue_type')} description is near-empty or only links.")
        elif issue_type == "task" and not re.search(
            r"(?i)acceptance|completion criteria|expected result|done when|definition of done",
            description,
        ):
            add(
                "warning",
                "completion_criteria_unclear",
                "No 'Done when' or completion criteria signal was found. Confirm the item has a testable definition of complete.",
            )
        if len(description) > LONG_DESCRIPTION_CHARS:
            add("suggestion", "description_long", f"Description is over about {LONG_DESCRIPTION_CHARS} characters; long Stories average more Bugs of Story. Consider trimming or splitting.")
        if IMPLEMENTATION_DETAIL.search(_section(description, "constraints")):
            add("suggestion", "constraints_implementation_detail", "Constraints appear to name implementation details (classes, stored procedures, controllers). Keep them for the PR unless the solution must obey them.")

    if issue_type == "story":
        match = _SUMMARY_FORMAT.match(summary)
        if not match:
            add("error", "summary_format", "Summary is not in the 'As a <persona>, I want <behavior> so that <outcome>' format.")
        else:
            if match.group("comma"):
                add("error", "summary_comma_before_so_that", "Summary has a comma before 'so that'.")
            prefix, core = _split_persona(match.group("persona"))
            persona_lc = re.sub(r"\s*\(.*?\)", "", match.group("persona")).strip().lower()
            if persona_lc in RETIRED_PERSONAS or any(persona_lc.endswith(" " + name) for name in RETIRED_PERSONAS):
                add("error", "retired_persona", f"Persona '{match.group('persona').strip()}' is retired. Use a persona from standards/story.md.")
            elif core and prefix and prefix not in MARKET_ADJECTIVES:
                add("warning", "market_adjective_unknown", f"'{prefix}' is not in the market list (standards/story.md#international-markets).")
        if description and not _AC_PATTERN.search(description):
            add("error", "story_no_numbered_ac", "No numbered acceptance criteria (AC1, AC2, ...) found.")
        if "ac-approved" in (compact.get("labels") or []):
            edited = _ac_edited_after_approval(issue)
            if edited and not re.search(r"(?is)changelog.*?\d{4}-\d{2}-\d{2}", description):
                add("warning", "ac_changed_without_changelog", "AC text changed after the ac-approved label was added, with no dated Changelog line.")

    if issue_type == "spike":
        if description and not re.search(r"(?i)question|expected output", description):
            add("warning", "spike_missing_question", "Spike has no question to answer or expected output.")

    if issue_type == "bug":
        if not description:
            add("error", "bug_description_empty", "Active Bug has no diagnostic description.")
        else:
            if not re.search(r"(?i)steps? to reproduce|reproduc|\brepro\b|steps?\b", description):
                add("warning", "bug_reproduction_missing", "No obvious reproduction steps were found.")
            if not re.search(r"(?i)expected|should", description):
                add("warning", "bug_expected_missing", "Expected behavior is not obvious.")
            if not re.search(r"(?i)actual|observed|currently|error|issue", description):
                add("warning", "bug_observed_missing", "Observed/actual behavior is not obvious.")
            if not re.search(r"(?i)environment|affected|scope|\bprod|\bstg\b", description):
                add("warning", "bug_environment_missing", "Environment / affected scope is not obvious.")
            if not re.search(r"(?i)impact", description):
                add("warning", "bug_impact_missing", "Impact is not stated.")
        if (compact.get("confirmed_issue") or "").lower() == "watchlist issue" and fix_versions:
            add("warning", "watchlist_with_fix_version", "Bug is still a Watchlist issue but has a Fix Version. Promote it to Confirmed issue or remove the Fix Version.")

    due_date = compact.get("due_date")
    if isinstance(due_date, str):
        try:
            if date.fromisoformat(due_date) < today:
                add("warning", "past_due", f"Due date {due_date} has passed while the issue remains active.")
        except ValueError:
            add("warning", "invalid_due_date", "Due date could not be parsed as YYYY-MM-DD.")

    return findings


def audit_collection(issues: Iterable[dict[str, Any]], today: date | None = None, refined: bool = False) -> list[dict[str, Any]]:
    issue_list = list(issues)
    compact_by_key = {
        compact["key"]: compact
        for compact in (compact_issue(issue) for issue in issue_list)
        if compact.get("key")
    }
    output = []

    for issue in issue_list:
        compact = compact_issue(issue)
        findings = audit_issue(issue, today=today, refined=refined)
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
    audit_cmd.add_argument(
        "--refined",
        action="store_true",
        help="Apply the full rule set to Stories created before the effective date (they are being refined)",
    )

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
            print(json.dumps(audit_collection(issues, today=audit_today, refined=args.refined), indent=2))
            return 0

    except (KeyError, ValueError, OSError, yaml.YAMLError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())


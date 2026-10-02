#!/usr/bin/env python3
"""Keep the Handbook Index page honest without scanning the handbook over and over.

The index is a Confluence page (label ``plugin-index``). Fetch its markdown body to a file, run
this tool on it with ``--index``, then publish the updated body back (with approval).

Stateless, like jira_helper.py: it never calls Confluence. An agent or person fetches the
page tree once through the Atlassian connector (one ``getConfluencePageDescendants`` call
returns every page's id, title and lastModified) and passes the JSON here.

    python tools/handbook_index.py check descendants.json     # drift report; exit 1 if drifted
    python tools/handbook_index.py update profile.json        # refresh Size / Status / Gist

``profile.json`` is a list of {pageId, title, chars, placeholder, gist} objects produced by one
profiling pass. Nothing from the pages is stored beyond a size band, a stub flag and a one-line gist.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

ROW = re.compile(r"^\|\s*(?P<title>[^|]+?)\s*\|\s*(?P<id>\d{10})\s*\|\s*(?P<size>[^|]*?)\s*\|\s*(?P<status>[^|]*?)\s*\|\s*(?P<gist>[^|]*?)\s*\|\s*$")
VERIFIED = re.compile(r"^(?P<prefix>\*\*Verified:\*\*\s*)(?P<date>\d{4}-\d{2}-\d{2}|never)", re.M)
DUPLICATE_TITLE = re.compile(r"\(\d+\)\s*$")


def size_band(chars: int | None) -> str:
    """S under 4K characters, M under 20K, L under 60K, XL above."""
    if chars is None:
        return "?"
    if chars < 4_000:
        return "S"
    if chars < 20_000:
        return "M"
    if chars < 60_000:
        return "L"
    return "XL"


def parse_rows(text: str) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for line in text.splitlines():
        match = ROW.match(line)
        if match:
            rows[match["id"]] = match.groupdict()
    return rows


def verified_date(text: str) -> date | None:
    match = VERIFIED.search(text)
    if not match or match["date"] == "never":
        return None
    return date.fromisoformat(match["date"])


def _results(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, dict):
        payload = payload.get("results") or payload.get("nodes") or []
    return [item for item in payload if isinstance(item, dict) and item.get("id")]


def check(index_text: str, live: Any, root_ids: set[str] | None = None) -> dict[str, list[Any]]:
    """Compare the index with a live page listing. Pure; returns the drift report."""
    indexed = parse_rows(index_text)
    pages = {str(item["id"]): item for item in _results(live)}
    verified = verified_date(index_text)
    report: dict[str, list[Any]] = {
        "missing_from_confluence": [],
        "not_in_index": [],
        "renamed": [],
        "changed_since_verified": [],
        "duplicates_ignored": [],
        "index_never_verified": [] if verified else ["Verified date is not set; run update"],
    }
    for page_id, row in indexed.items():
        page = pages.get(page_id)
        if page is None:
            if not root_ids or page_id not in root_ids:
                report["missing_from_confluence"].append({"pageId": page_id, "title": row["title"]})
            continue
        if page.get("title") and page["title"] != row["title"] and row["title"] not in page["title"]:
            report["renamed"].append({"pageId": page_id, "indexed": row["title"], "live": page["title"]})
        modified = str(page.get("lastModified") or "")[:10]
        if verified and modified and date.fromisoformat(modified) > verified:
            report["changed_since_verified"].append({"pageId": page_id, "title": row["title"], "lastModified": modified})
    for page_id, page in pages.items():
        title = str(page.get("title") or "")
        if page_id in indexed:
            continue
        if DUPLICATE_TITLE.search(title):
            report["duplicates_ignored"].append({"pageId": page_id, "title": title})
        else:
            report["not_in_index"].append({"pageId": page_id, "title": title})
    return report


def has_drift(report: dict[str, list[Any]]) -> bool:
    return any(report[key] for key in ("missing_from_confluence", "not_in_index", "renamed", "changed_since_verified", "index_never_verified"))


def _cell(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("|", "/")).strip()


def update(index_text: str, profile: Any, today: date | None = None) -> str:
    """Refresh Size, Status and Gist for profiled pages and stamp the Verified date."""
    by_id = {str(item["pageId"]): item for item in profile if isinstance(item, dict) and item.get("pageId")}
    today = today or date.today()
    lines = []
    for line in index_text.splitlines():
        match = ROW.match(line)
        if match and match["id"] in by_id:
            item = by_id[match["id"]]
            status = "stub" if item.get("placeholder") else "real"
            gist = "placeholder" if item.get("placeholder") else _cell(str(item.get("gist") or match["gist"]))
            line = f"| {match['title']} | {match['id']} | {size_band(item.get('chars'))} | {status} | {gist} |"
        lines.append(line)
    out = "\n".join(lines) + ("\n" if index_text.endswith("\n") else "")
    return VERIFIED.sub(lambda m: f"{m['prefix']}{today.isoformat()}", out, count=1)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--index", type=Path, required=True, help="File holding the Handbook Index page body (markdown)")
    sub = parser.add_subparsers(dest="command", required=True)
    check_cmd = sub.add_parser("check", help="Report drift between the index and a live page listing")
    check_cmd.add_argument("listing", help="JSON from getConfluencePageDescendants, or - for stdin")
    check_cmd.add_argument("--root", action="append", default=[], help="Page ID that is a root of the listing and so absent from it")
    update_cmd = sub.add_parser("update", help="Write Size, Status and Gist from a profile, and stamp Verified")
    update_cmd.add_argument("profile", help="Profile JSON file")
    update_cmd.add_argument("--today", help="Override the Verified date (YYYY-MM-DD)")
    return parser


def _load(path: str) -> Any:
    if path == "-":
        return json.load(sys.stdin)
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    index_text = args.index.read_text(encoding="utf-8")
    if args.command == "check":
        report = check(index_text, _load(args.listing), set(args.root))
        print(json.dumps(report, indent=2))
        return 1 if has_drift(report) else 0
    today = date.fromisoformat(args.today) if args.today else None
    args.index.write_text(update(index_text, _load(args.profile), today), encoding="utf-8")
    print(f"Updated {args.index}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

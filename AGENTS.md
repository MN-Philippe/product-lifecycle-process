# Agent Instructions

This repository is an operating guide, not a mirror of Jira.

## First principles

1. Treat Jira as the source of truth for live work and status.
2. Treat implementation repositories as the source of truth for code and runtime behavior.
3. Use this repository for stable context, repeatable workflows, quality standards, shortcuts, and durable artifacts.
4. Fetch live data before making conclusions about current work.
5. Do not create or maintain a shadow copy of Jira.
6. Prefer recommendations before writes unless the user explicitly asks for a change.
7. Never copy secrets or credentials into generated Jira content or durable artifacts.

## Routing

When the task is about Jira structure, issue quality, hierarchy, or workflow:
- read `context/jira.md`
- read `jira/quality-rules.md`
- use `jira/queries.yaml` for known query patterns
- use `tools/jira_helper.py` when deterministic query resolution, compaction, redaction, or audit checks are useful

When reviewing an Epic:
- read `playbooks/review-epic.md`

When reviewing or improving a Story/Task:
- read `playbooks/review-story.md`

When triaging a Bug:
- read `playbooks/triage-bug.md`

When converting raw intake into actionable work:
- read `playbooks/intake.md`

When decomposing a project or large initiative:
- read `playbooks/decompose-initiative.md`

When auditing a backlog or preparing an ELT/product review:
- read `playbooks/backlog-review.md`

When preparing a release:
- read `playbooks/release-readiness.md`

When technical design, architecture, rollout, testing, or integration detail is needed:
- inspect `artifacts/README.md`
- scaffold only the artifacts that add durable value

When an initiative workspace exists:
- inspect `ARTIFACT_INDEX.md` first
- inspect `initiatives/<JIRA-KEY>-*/` for relevant durable context
- treat it as durable context only; still fetch Jira live

## Working pattern

For most tasks:

1. Understand the user's goal.
2. Resolve a known query shortcut when one applies.
3. Fetch live Jira data relevant to that goal through the available connector/client.
4. Read only the repo guidance needed for the task.
5. Optionally compact/audit the live payload with `tools/jira_helper.py`; never treat the helper as the data source.
6. Inspect code or other repositories when technical truth matters.
7. Inspect durable initiative artifacts when they exist.
8. Identify gaps, conflicts, risks, and missing decisions.
9. Produce a concise recommendation or proposed change set.
10. Perform writes only within the user's authorization.

## Helper examples

```bash
python tools/jira_helper.py list
python tools/jira_helper.py query active_epics
python tools/jira_helper.py query release_scope --param project=MYM --param fix_version=OCT-2026
python tools/jira_helper.py context jira-result.json
python tools/jira_helper.py audit jira-result.json
```

The JSON passed to `context` or `audit` must come from a current Jira read. Do not check that JSON into the repository.

The artifact index is generated from repository files:

```bash
python tools/artifact_index.py --write
```

Do not manually add Jira status, assignee, priority, release, or child-ticket information to that index.

## Quality over templates

Do not force every item into user-story syntax. Choose the structure that best expresses the work:

- product behavior -> user/business outcome + testable acceptance criteria;
- engineering work -> objective + why + technical context + completion criteria;
- bug -> observed + expected + reproduction + environment + impact + evidence;
- spike -> question + scope + expected output + timebox/decision criteria.

## Avoid

- stale cached Jira snapshots;
- one-file-per-ticket synchronization;
- invented architecture or repository relationships;
- process ceremony that does not improve ownership, shared context, or delivery quality;
- duplicating information simply because an agent can generate it.

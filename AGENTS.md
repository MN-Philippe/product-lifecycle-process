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
- inspect `initiatives/<JIRA-KEY>-*/`
- treat it as durable context only; still fetch Jira live

## Working pattern

For most tasks:

1. Understand the user's goal.
2. Fetch live Jira data relevant to that goal.
3. Read only the repo guidance needed for the task.
4. Inspect code or other repositories when technical truth matters.
5. Identify gaps, conflicts, risks, and missing decisions.
6. Produce a concise recommendation or proposed change set.
7. Perform writes only within the user's authorization.

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

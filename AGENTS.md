# Agent Instructions

This repository is an operating guide, not a mirror of Jira.

## First principles

1. Treat Jira as the source of truth for live work, commitments, and field history.
2. Treat implementation repositories as the source of truth for code and runtime behavior.
3. Use this repository for stable context, lifecycle standards, repeatable workflows, quality rules, shortcuts, and durable artifacts.
4. Fetch live data before making conclusions about current work.
5. Do not create or maintain a shadow copy of Jira.
6. Prefer recommendations before writes unless the user explicitly asks for a change or an approved automation owns specific fields.
7. Never copy secrets or credentials into generated Jira content or durable artifacts.
8. Keep unresolved process questions unresolved; do not silently turn experiments into policy.

## Canonical standards

When reasoning about the product lifecycle, read only the standards relevant to the task:

- `standards/product-lifecycle.md` - intake, Business Requirements Complete, commitment, Product Complete, delivery, release, and exceptions
- `standards/story-quality.md` - Story Summary and acceptance-criteria quality
- `standards/bug-quality.md` - Bug classification, technical assessment, prioritization, and Bug-of-Story rules
- `standards/ai-release-confidence.md` - scheduled AI Release Confidence experiment

These standards are authoritative when older playbook wording conflicts with them.

## Routing

When the task is about Jira structure, issue quality, hierarchy, or workflow:
- read `context/jira.md`
- read `jira/quality-rules.md`
- use `jira/queries.yaml` for known query patterns
- use `tools/jira_helper.py` when deterministic query resolution, compaction, redaction, or audit checks are useful

When reviewing an Epic:
- read `playbooks/review-epic.md`

When reviewing or improving a Story:
- read `standards/story-quality.md`
- read `playbooks/review-story.md`

When triaging a Bug:
- read `standards/bug-quality.md`
- read `playbooks/triage-bug.md`

When converting raw intake into actionable work:
- read `standards/product-lifecycle.md`
- read `playbooks/intake.md`

When decomposing a project or large initiative:
- read `playbooks/decompose-initiative.md`

When auditing a backlog or preparing an ELT/product review:
- read `playbooks/backlog-review.md`

When preparing a release:
- read `standards/product-lifecycle.md`
- read `playbooks/release-readiness.md`

When running the scheduled AI Release Confidence assessment:
- read `standards/ai-release-confidence.md`
- read `playbooks/assess-release-confidence.md`
- use `committed_story_bugs` from `jira/queries.yaml`

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
4. Read only the repo standards/playbooks needed for the task.
5. Optionally compact/audit the live payload with `tools/jira_helper.py`; never treat the helper as the data source.
6. Inspect code or other repositories when technical truth matters.
7. Inspect durable initiative artifacts when they exist.
8. Identify gaps, conflicts, risks, and missing decisions.
9. Produce a concise recommendation or proposed change set.
10. Perform writes only within the user's authorization or an explicitly approved automation write policy.

## Helper examples

```bash
python tools/jira_helper.py list
python tools/jira_helper.py query committed_story_bugs
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

## Story quality rule

For Jira **Stories**, the Summary format is required:

> **As a [specific actor], I want [clear behavior/capability], so that [clear outcome/value].**

The `I want` and `So that` must be clear enough that ELT can understand the Story from the Summary alone. Do not weaken this standard merely because the underlying work is technical; choose the clearest truthful actor, behavior, and outcome.

Tasks, Spikes, and other non-Story issue types can use structures appropriate to their work.

## Scheduled AI Release Confidence boundary

The early-morning scheduled assessment is intentionally narrow:

- assess only **Stories and standalone Bugs with a Fix Version**;
- maintain only **AI Release Confidence** and **AI Release Confidence Reason**;
- read but never edit **AI Release Confidence Feedback**;
- use Jira changelog/history rather than creating a parallel history in Git;
- do not add Epic/release aggregation or dashboard scoring yet.

Broader lifecycle standards do not imply that the scheduled AI job should scan every Jira item.

## Avoid

- stale cached Jira snapshots;
- one-file-per-ticket synchronization;
- invented architecture or repository relationships;
- process ceremony that does not improve ownership, shared context, or delivery quality;
- duplicating information simply because an agent can generate it;
- treating Jira existence as approval or commitment;
- treating a single weak delivery signal as automatic risk.

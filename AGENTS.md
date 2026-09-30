# Agent Instructions

This repository is an operating guide, not a mirror of Jira. This file only routes; every rule lives in exactly one file it links to. Read only what the task needs.

## Principles

- Jira is the source of truth for live work, commitments and history; implementation repos are the source of truth for code. Fetch live data before concluding anything about current work. Do not create a shadow copy of Jira. See [README](README.md#source-of-truth-boundaries).
- GitHub is read-only. Jira writes follow draft, approve, then write. See [write policy](standards/jira-conventions.md#write-policy).
- Every Jira key in output is a link. See [jira-conventions](standards/jira-conventions.md).
- Never copy secrets into Jira content or artifacts. See [jira-conventions](standards/jira-conventions.md#security-hygiene).
- Keep unresolved process questions unresolved. See [lifecycle](standards/lifecycle.md#10-open-questions-not-yet-standardized).
- Standards win over older playbook wording. If a rule is missing from the standards, do not invent it.

## Router

| Task | Read |
| --- | --- |
| Write a Story | [story](standards/story.md), [jira-conventions](standards/jira-conventions.md), [write-story](playbooks/write-story.md), [template](templates/story.md) |
| Refine a Story | [story](standards/story.md), [refine-story](playbooks/refine-story.md) |
| Split a Story | [story](standards/story.md), [split-story](playbooks/split-story.md) |
| Is a Story ready for dev | [lifecycle](standards/lifecycle.md), [ready-check](playbooks/ready-check.md) |
| Review / audit a Story | [story](standards/story.md), [review-story](playbooks/review-story.md) |
| Task or Spike | [task](standards/task.md), [template](templates/task.md) |
| Triage a Bug | [bug](standards/bug.md), [triage-bug](playbooks/triage-bug.md), [template](templates/bug.md) |
| Raw intake | [lifecycle](standards/lifecycle.md), [intake](playbooks/intake.md) |
| Decompose an initiative | [story](standards/story.md), [decompose-initiative](playbooks/decompose-initiative.md) |
| Review an Epic | [review-epic](playbooks/review-epic.md) |
| Backlog / ELT review | [backlog-review](playbooks/backlog-review.md) |
| Prepare a release | [lifecycle](standards/lifecycle.md), [release-readiness](playbooks/release-readiness.md) |
| Monthly release notes and Manual log | [release-docs](playbooks/release-docs.md) |
| Retire replaced tickets | [cleanup](playbooks/cleanup.md) |
| Scheduled AI Release Confidence | [ai-release-confidence](standards/ai-release-confidence.md), [assess-release-confidence](playbooks/assess-release-confidence.md) |
| Vendor (MYM) onboarding | [vendor-guide](templates/vendor-guide.md) |
| Jira fields, Fix Versions, Code Dependency, markets | [jira-conventions](standards/jira-conventions.md) |
| Design, architecture, rollout detail | [artifacts/README](artifacts/README.md) |
| An initiative workspace exists | [ARTIFACT_INDEX](ARTIFACT_INDEX.md), then `initiatives/<JIRA-KEY>-*/` (durable context only; still fetch Jira live) |

## Working pattern

1. Understand the goal. Resolve a known query from `jira/queries.yaml` when one applies.
2. Fetch live Jira data through the connector.
3. Read the routed standard and playbook.
4. Optionally compact or audit the payload with `tools/jira_helper.py` (see [tools/README](tools/README.md)); the helper is never the data source.
5. Inspect code or initiative artifacts when technical truth matters.
6. Recommend or propose a change set; write only within authorization.

## Avoid

Stale Jira snapshots, one-file-per-ticket sync, invented repo relationships, ceremony that does not improve ownership or delivery quality, treating Jira existence as approval, and treating one weak signal as automatic risk.

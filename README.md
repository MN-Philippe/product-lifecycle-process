# Product Lifecycle Process

This repository is the operating layer for AI-assisted product and delivery work across Jira, GitHub, and durable project artifacts.

It is **not a copy of Jira**. Jira remains the live system of record for work, status, assignees, priority, releases, and issue relationships. This repository gives an AI agent the durable context, rules, shortcuts, playbooks, and artifact scaffolding it needs to work with Jira well.

## Core model

- **Jira owns live work.** Fetch current issues, status, hierarchy, ownership, dates, and release data from Jira at runtime.
- **Product and engineering repositories own implementation reality.** Inspect the relevant code when technical context matters.
- **This repo owns durable operating context.** Keep instructions, quality standards, repeatable queries, playbooks, templates, and durable initiative artifacts here.
- **The agent connects them at runtime.** Do not create a synchronization layer unless there is a specific, proven need.

## Start here

AI agents should read [`AGENTS.md`](AGENTS.md) first.

Humans should read [`GUIDE.md`](GUIDE.md) for the repository boundaries, intended operating model, and anti-patterns.

## Repository map

| Area | Purpose |
| --- | --- |
| [`context/`](context/) | Stable product, Jira, and delivery context |
| [`jira/`](jira/) | Jira shortcuts, interpretation rules, and quality standards |
| [`playbooks/`](playbooks/) | Repeatable agent workflows for common PM and delivery tasks |
| [`artifacts/`](artifacts/) | Templates for durable product, architecture, and delivery artifacts |
| [`initiatives/`](initiatives/) | Optional workspaces for initiatives that need durable artifacts beyond Jira |
| [`tools/`](tools/) | Lightweight helpers that reduce repetitive agent work without mirroring Jira |

## Current scope

The initial Jira scope is:

- `RAD` - Radius
- `MYM` - myMathnasium

The first goal is to make an agent consistently useful for:

1. reviewing and improving Epics, Stories, engineering work, and Bugs;
2. turning raw intake into actionable Jira work;
3. decomposing initiatives without losing the business outcome;
4. auditing backlog and release readiness from live Jira data;
5. creating durable technical and delivery artifacts when Jira is not the right home for them.

## Principle

> Keep live state where it already belongs. Put only durable knowledge and reusable operating logic in Git.

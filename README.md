# Product Lifecycle Process

This repository is the operating layer for AI-assisted product and delivery work across Jira, GitHub, and durable project artifacts.

It is **not a copy of Jira**. Jira remains the live system of record for work, status, assignees, priority, releases, and issue relationships. This repository gives an AI agent the durable context, rules, shortcuts, playbooks, and artifact scaffolding it needs to work with Jira well.

## Core model

- **Jira owns live work.** Fetch current issues, status, hierarchy, ownership, dates, release data, and field history from Jira at runtime.
- **Product and engineering repositories own implementation reality.** Inspect the relevant code when technical context matters.
- **This repo owns durable operating context.** Keep lifecycle standards, agent instructions, repeatable queries, playbooks, templates, and durable initiative artifacts here.
- **The agent connects them at runtime.** Do not create a synchronization layer unless there is a specific, proven need.

## Start here

AI agents should read [`AGENTS.md`](AGENTS.md) first.

Humans should read [`GUIDE.md`](GUIDE.md) for the repository boundaries and [`standards/product-lifecycle.md`](standards/product-lifecycle.md) for the current product lifecycle.

## Canonical standards

- [`standards/product-lifecycle.md`](standards/product-lifecycle.md) - intake through release, ownership, readiness, commitments, expedite path, and open questions
- [`standards/story-quality.md`](standards/story-quality.md) - required Story Summary format, acceptance criteria, and Product Complete
- [`standards/bug-quality.md`](standards/bug-quality.md) - Bug classification, triage, technical assessment, prioritization, and Bug-of-Story handling
- [`standards/ai-release-confidence.md`](standards/ai-release-confidence.md) - narrow daily AI Release Confidence experiment for committed Stories and Bugs

## Repository map

| Area | Purpose |
| --- | --- |
| [`standards/`](standards/) | Canonical product-lifecycle and Jira-work quality rules |
| [`context/`](context/) | Stable product, Jira, and delivery context |
| [`jira/`](jira/) | Jira shortcuts, interpretation rules, and supporting quality checks |
| [`playbooks/`](playbooks/) | Repeatable agent workflows for common PM and delivery tasks |
| [`artifacts/`](artifacts/) | Templates for durable product, architecture, and delivery artifacts |
| [`initiatives/`](initiatives/) | Optional workspaces for initiatives that need durable artifacts beyond Jira |
| [`tools/`](tools/) | Lightweight helpers that reduce repetitive agent work without mirroring Jira |

## Current scope

The initial Jira scope is:

- `RAD` - Radius
- `MYM` - myMathnasium

The repository supports broad product-lifecycle guidance, but the first scheduled AI delivery-risk experiment is intentionally narrow:

> **Early each morning, assess only Stories and standalone Bugs with a Fix Version and maintain the AI-owned Release Confidence and Reason fields.**

The human-owned AI Release Confidence Feedback field is read as context and never edited by the agent.

Release/Epic aggregation and the final Google Sheet dashboard remain outside this repository's automation scope for now.

## Principle

> Keep live state where it already belongs. Put only durable knowledge and reusable operating logic in Git.

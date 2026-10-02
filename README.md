# Product Lifecycle Process

The operating layer for AI-assisted product and delivery work across Jira, GitHub and durable project artifacts. Agents start at [`AGENTS.md`](AGENTS.md); people start here.

It is **not a copy of Jira**. Jira stays the live system of record. This repository gives an agent the durable context, rules, shortcuts and playbooks it needs to work with Jira well.

## What this repo is

- canonical lifecycle and Jira-work standards ([`standards/`](standards/));
- repeatable agent playbooks ([`playbooks/`](playbooks/)) and templates ([`templates/`](templates/));
- reusable JQL ([`jira/queries.yaml`](jira/queries.yaml)) and small stateless helpers ([`tools/`](tools/));
- the Mathnasium Claude plugin ([`plugins/`](plugins/)), a lean standalone install that reads the Confluence Technology & Product Handbook live (see [The Claude plugin](#the-claude-plugin));
- durable artifact templates and initiative workspaces for material that Jira is not a good home for ([`artifacts/`](artifacts/), [`initiatives/`](initiatives/)).

## What this repo is not

Do not turn it into a Jira export, one Markdown file per ticket, a cache of status, assignee, sprint, Fix Version, priority, comments or confidence, a second backlog, a synchronization service, a dump of data that can be fetched live, an agent memory dump, or a place to standardize unresolved process questions early.

If information can be fetched reliably from Jira or a code repo and changes often, fetch it at runtime.

## Source-of-truth boundaries

| Owner | Owns |
| --- | --- |
| **Jira** | Issues and hierarchy, status, assignee, priority and due dates, Fix Versions, comments, workflow and field history, current ACs and ticket decisions, AI Release Confidence field values |
| **Implementation repos** | Source code, tests, runtime config, infrastructure-as-code, implementation docs close to the code |
| **This repo** | The agreed lifecycle, how agents interpret live systems, what good Stories/Bugs look like, repeatable reviews, stable cross-repo context, cross-cutting artifacts |

A Fix Version is the current delivery commitment. Use Jira changelog to understand how it changed; do not copy the history here.

## Standards

| Standard | Covers |
| --- | --- |
| [`story.md`](standards/story.md) | The Story: format, size, personas, markets, brackets, ACs and test cases, constraints, sub-tasks, PR field |
| [`task.md`](standards/task.md) | Tasks and Spikes |
| [`bug.md`](standards/bug.md) | Bug classification, categorization, Watchlist, triage, Bug of Story |
| [`lifecycle.md`](standards/lifecycle.md) | Intake to release, Ready for Dev, Fix Version, expedite path, open questions |
| [`jira-conventions.md`](standards/jira-conventions.md) | Site, field IDs, Fix Versions, Code Dependency, statuses |
| [`ai-release-confidence.md`](standards/ai-release-confidence.md) | The scheduled AI Release Confidence experiment |

## Agent write policy

Read-first and propose-first: fetch live state, read the relevant standard, analyze with the playbook, and recommend. The rules for writing (GitHub read-only; Jira draft, approve, then write) are in [`standards/jira-conventions.md`](standards/jira-conventions.md#write-policy).

## Standards vs. scheduled automation

Broad good-practice standards are not automation scope. The scheduled job assesses only committed Stories, Tasks and standalone Bugs; see [`ai-release-confidence.md`](standards/ai-release-confidence.md).

## Initiative workspaces

An initiative does not need a folder because it has a Jira Epic. Create one under [`initiatives/`](initiatives/) only for durable material such as architecture, ADRs, integration contracts, migration plans, dependency maps, test strategy or rollout plans. Reference the Jira key; never copy Jira state.

## The Claude plugin

[`plugins/mathnasium-product-lifecycle/`](plugins/mathnasium-product-lifecycle/) is a **standalone install**, not synced from this repo. It is five small files: two skills, a hook, and a manifest. It holds no handbook content. At runtime it finds the **Handbook Index** page in Confluence by its label (`plugin-index`) or title, reads it, and follows it to the Technology & Product Handbook, using each person's own Confluence access.

So Confluence changes reach everyone immediately: edit the handbook or the index page and nothing else needs to happen. Re-share the plugin only when a skill or the hook changes.

- **Package:** `python tools/package_plugin.py` writes `dist/mathnasium-product-lifecycle-<version>.zip`. Bump `version` in `plugin.json` first; an install only updates when the version increases.
- **Contract:** the index page declares `Plugin contract: 1`. Bump it only for a breaking change to the page's structure; older plugins then tell their users to update.
- **Index page:** maintained in Confluence. The page is "Handbook Index" in the IPD space (label `plugin-index`, page 2162819145). Refresh the page's sizes, statuses and gists with [`playbooks/refresh-handbook-index.md`](playbooks/refresh-handbook-index.md).

`standards/`, `playbooks/` and `templates/` in this repo currently duplicate the handbook's Product Lifecycle pages and feed `tools/jira_helper.py` and `AGENTS.md`. Until one side is declared the source, a change to one must be made in the other.

## Principle

> Keep live state where it already belongs. Put only durable knowledge and reusable operating logic in Git.

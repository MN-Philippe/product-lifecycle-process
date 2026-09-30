# Product Lifecycle Process

The operating layer for AI-assisted product and delivery work across Jira, GitHub and durable project artifacts. Agents start at [`AGENTS.md`](AGENTS.md); people start here.

It is **not a copy of Jira**. Jira stays the live system of record. This repository gives an agent the durable context, rules, shortcuts and playbooks it needs to work with Jira well.

## What this repo is

- canonical lifecycle and Jira-work standards ([`standards/`](standards/));
- repeatable agent playbooks ([`playbooks/`](playbooks/)) and templates ([`templates/`](templates/));
- reusable JQL ([`jira/queries.yaml`](jira/queries.yaml)) and small stateless helpers ([`tools/`](tools/));
- the source of the Mathnasium product lifecycle Claude plugin, generated into [`plugins/`](plugins/);
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

## Updating the standard

1. Edit the file in [`standards/`](standards/) (or the playbook or template). A rule lives in exactly one file; link to it from everywhere else.
2. Run `python tools/build_plugin.py`. It regenerates the plugin's references and bumps its version.
3. Run `python -m unittest discover -s tests -p 'test_*.py'`.
4. Open a PR. CI checks that the plugin is in sync (`python tools/build_plugin.py --check`).
5. On merge to `main`, the GitHub-synced org marketplace updates the plugin automatically.

## Principle

> Keep live state where it already belongs. Put only durable knowledge and reusable operating logic in Git.

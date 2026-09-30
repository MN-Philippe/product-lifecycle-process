# Jira Conventions

Stable facts about Jira for RAD and MYM. Always query Jira live for current issues, field values and history.

- **Site:** `https://mathnasium.atlassian.net`
- **cloudId:** `abd26ef1-c908-455d-8b20-516e025731b2`
- **Projects:** RAD (Radius) and MYM (myMathnasium). MYM spans multiple repos; RAD is mostly Radius, but not only. Never infer a repo from the Jira key alone; check Code Dependency and linked PRs.
- **Hyperlink rule:** every Jira key in user-facing output is a link. Prefer the connector `webUrl`; otherwise `https://mathnasium.atlassian.net/browse/<KEY>` after confirming the key exists. In tables, documents and decks, keep the short key visible and make that text clickable.

## Issue types

Epic, Story, Task, Spike, Bug, Bug of Story, Sub-task.

Hierarchy: `Epic → Story / Task / Bug`, with Bug of Story as the one child type of a Story. Sub-task is legacy; do not create new ones for implementation (`standards/story.md#multi-repo-work-and-sub-tasks`).

The long-term Epic vs. persistent-capability model is still open (`standards/lifecycle.md`). Do not enforce a new Epic taxonomy. Parent status does not reliably roll up from children, so never infer initiative health from Epic status alone.

## Fields

Verified on MYM-565.

| Field | ID | Use |
| --- | --- | --- |
| Story Points | customfield_10021 | The only estimate field |
| Story point estimate | customfield_10909 | Do not use |
| Pull Requests | customfield_11279 | Required once a PR exists |
| Development (GitHub) | customfield_10500 | Read-only PR signal from the GitHub integration |
| Code Dependency | customfield_11147 | Repo(s) touched, multi-value; required by Ready for Dev (see [Code Dependency](#code-dependency)) |
| Test plan | customfield_10956 | Test cases (`DEFAULT — TBC`) |
| Delivery Risk | customfield_11382 | Possibly the AI Release Confidence target (`DEFAULT — TBC`) |
| Business Requirements Finalized | customfield_11383 | Business approval |
| Original Release Target | customfield_11348 | First committed release |
| Confirmed Issue | customfield_11016 | Bug Watchlist state |
| Epic Link | customfield_10016 | Legacy parent link |
| Sprint | customfield_10020 | Sprint |

## Fix Versions

The Fix Version is the delivery commitment once Product and Engineering have planned the work. It is not the business due date. A Fix Version change is meaningful history (moved earlier = expedite; moved later = delay); read it from the Jira changelog, never copy it into Git.

| Pattern | Meaning |
| --- | --- |
| `MON-YYYY` (e.g. `OCT-2026`) | Monthly release. A delivery commitment |
| `MON-YYYY-SR`, `-SR2` | Service release in that month. A delivery commitment |
| `HOTFIX` | Hotfix. A delivery commitment |
| `N/A` | Work that is never released (scripts, research, testing). **Not** a delivery commitment |
| `FREEZE` | `DEFAULT — TBC`: treated as not a delivery commitment until its meaning is confirmed |

"Committed" everywhere in these standards means a Fix Version in the first three rows. Always take release dates from the Jira version record, not from the name.

## Code Dependency

The repo(s) a ticket touches. The field allows several values. Verified options (option IDs in parentheses):

| Option | ID |
| --- | --- |
| Radius | 10971 |
| Scheduling Microservice | 10972 |
| Notifications Microservice | 10973 |
| GP APP | 10974 |
| GP API | 10975 |
| Data Access Layer | 10976 |
| Database | 10977 |
| Scheduling Fanout | 10980 |
| Radius Emails | 11253 |

- **Summary bracket** (`DEFAULT — TBC`): when a bracket is used, its text is **exactly one of these values**, for example `[GP API]` or `[Scheduling Microservice]`. One vocabulary, no mapping table.
- **More than one value** is a multi-repo signal: the Story probably needs splitting (`playbooks/split-story.md`).
- **RAD does not currently use Code Dependency.** All recent tickets with a value were in MYM. Requiring it at Ready for Dev is new practice for RAD.
- **TODO: add to Code Dependency in Jira, or drop.** Radius-API-DataService, AWSToRadius and Parent Reports have no option yet.

## Markets

See `standards/story.md#international-markets`.

## Statuses observed

For interpretation only; read the live workflow.

To Do, In Progress, CODE REVIEW / IN CODE REVIEW, In QA - HTD, IN QA - MATHNASIUM, IN PROGRESS - QA, READY FOR STG, READY FOR QA in STG, READY FOR PROD, Done.

`In QA - HTD` is the vendor's QA; `IN QA - MATHNASIUM` is internal QA.

## Security hygiene

Jira content can contain raw intake, screenshots, payloads and occasionally credential-like data. Never reproduce a secret in Jira content, generated output or a durable artifact. Flag likely credentials, tokens or passwords generically, without echoing the value, and recommend removal or rotation.

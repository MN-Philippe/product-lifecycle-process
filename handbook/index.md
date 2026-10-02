# Technology & Product Handbook: page index

Maps handbook topics to Confluence page IDs so the plugin can fetch exactly the page it needs. It holds no handbook content; the pages are the content.

- **Site:** `https://mathnasium.atlassian.net`, space `IPD`
- **cloudId:** `abd26ef1-c908-455d-8b20-516e025731b2`
- **Root:** [Technology & Product Handbook — Draft](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2162262120) (`2162262120`)
- Page URL: `https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/<pageId>`

## How to read a page

**Verified:** 2026-10-02

Size bands: **S** under 4K characters, **M** under 20K, **L** under 60K, **XL** above. Status: **real** has content; **stub** is a "Draft placeholder".

1. Pick the page from the tables below by title and gist. Do not browse: never fetch the root or a section page to look around.
2. **Skip stubs.** Status `stub` means there is nothing to read yet. Say the topic is not documented in the handbook yet and quote the gist, then stop. Do not answer from memory.
3. **Look up facts before reading pages.** For a single fact (a column, a rule, a name), call `searchConfluenceUsingCql` (`text ~ "<term>" AND space = IPD`) and answer from the excerpts. Fetch the whole page only when the excerpt is not enough.
4. **Size L and XL pages are never fetched in full by default.** Search first; if you must fetch, fetch the one page that answers the question and nothing else from that family.
5. **Read each page at most once per session.** Reuse what you already read instead of fetching it again.
6. To read a page, call `getConfluencePage` with the `cloudId`, the `pageId` and `contentFormat: markdown`. Use the body, not the summary field. Follow numeric page-ID links inside a page only when they point at the next page you need.
7. If an ID fails or the title no longer matches, find the page with `searchConfluenceUsingCql` (`title = "<title>" AND space = IPD`) and tell the user the index is stale.
8. **Freshness.** `Verified` is the date this index's sizes, statuses and gists were last checked. If it is more than 30 days old, or the user says a page has changed, say so. One `getConfluencePageDescendants` call on the root returns every page's lastModified; use it to see what changed instead of re-reading pages.
9. Ignore pages titled `… (2)`: they are duplicates awaiting cleanup.

The handbook is a **draft** and does not yet supersede existing documentation. Where a page carries an owner, status or last-verified date, report it. Current implementation is not automatically an approved standard; keep the page's own legacy-versus-standard labels.

## Jira work: standards, playbooks, templates

Parent: [Product Lifecycle Process](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2162327553) (`2162327553`). Start with the Agent Router.

| Title | pageId | Size | Status | Gist |
| --- | --- | --- | --- | --- |
| Product Lifecycle - Agent Router | 2162065429 | M | real | Routing table mapping each Jira task type to the standards, playbooks and templates to read. |
| Product Lifecycle - Story Standard | 2162393089 | M | real | Story format, size, personas, markets, ACs, decomposition, sub-tasks, PR field and audit checks. |
| Product Lifecycle - Task Standard | 2162425857 | S | real | Task and Spike format, size limits, Done-when rules and audit checks. |
| Product Lifecycle - Bug Standard | 2162458625 | M | real | Bug classification, categorization, Watchlist state, triage, Bug-of-Story rules and checks. |
| Product Lifecycle - Lifecycle Standard | 2162229270 | M | real | Intake to release: Ready for Dev checklist, Fix Version commitment, expedite path, delivery pipeline, open questions. |
| Product Lifecycle - Jira Conventions | 2162130987 | M | real | Jira site facts: field IDs, Fix Version patterns, Code Dependency options, statuses, security hygiene. |
| Product Lifecycle - AI Release Confidence Standard | 2162196502 | M | real | Scope, fields, cadence, evidence signals and evaluation of the daily AI release-confidence experiment. |
| Product Lifecycle Playbook - Write Story | 2162098199 | S | real | Steps for Q&A-driven drafting of a new Story, written to Jira after approval. |
| Product Lifecycle Playbook - Refine Story | 2162196542 | S | real | Steps to fold new answers and comments into an existing Story description. |
| Product Lifecycle Playbook - Split Story | 2162262051 | S | real | Steps to split Stories by behavior seams then repo, keeping each at five points or fewer. |
| Product Lifecycle Playbook - Ready Check | 2162229290 | S | real | Run the Ready for Dev checklist on a Story or Task and report gaps. |
| Product Lifecycle Playbook - Review Story | 2162491413 | S | real | Audit an existing Story against the standard's checks and propose smallest improvements. |
| Product Lifecycle Playbook - Decompose Initiative | 2162524161 | S | real | Break an Epic or initiative into behavior-based, repo-bounded Stories, Tasks and workflow sub-tasks. |
| Product Lifecycle Playbook - Intake | 2162360341 | S | real | Normalize raw intake: classify, dedupe, find underlying need, move toward Business Requirements Complete. |
| Product Lifecycle Playbook - Triage Bug | 2162262071 | S | real | Steps to classify, trace, scope and prioritize a reported Bug. |
| Product Lifecycle Playbook - Cleanup | 2162196522 | S | real | Retire replaced tickets as Won't Do with links; worked example MYM-529. |
| Product Lifecycle Playbook - Release Readiness | 2162327574 | S | real | Assess release scope readiness from live Jira, QA evidence and operational concerns. |
| Product Lifecycle Playbook - Release Docs | 2162032662 | M | real | Monthly Radius release notes, Manual update log and announcement draft procedure with traps. |
| Product Lifecycle Playbook - Review Epic | 2162262031 | S | real | Assess an Epic's context and children without imposing an undecided Epic taxonomy. |
| Product Lifecycle Playbook - Backlog Review | 2162491393 | S | real | Prepare decision-oriented backlog or ELT view of live Jira work. |
| Product Lifecycle Playbook - Assess Release Confidence | 2162098219 | S | real | Daily scheduled steps to set On Track, Watch or At Risk; blocked on write-field TODO. |
| Product Lifecycle Template - Story | 2162032682 | S | real | Copy-paste Story summary, description and field template. |
| Product Lifecycle Template - Task | 2162262091 | S | real | Copy-paste Task and Spike description templates. |
| Product Lifecycle Template - Bug | 2162491433 | S | real | Copy-paste Bug description template with Observed, Expected, Impact and fields. |
| Product Lifecycle Template - Vendor Guide | 2162032702 | S | real | One-page MYM vendor guide: who owns what and working rules. |
| Product Lifecycle Artifact - Technical Design | 2162229310 | S | real | Blank technical design template: problem, constraints, design, risks, rollout. |
| Product Lifecycle Artifact - ADR | 2162425877 | S | real | Blank architecture decision record template. |
| Product Lifecycle Artifact - Implementation Plan | 2162229330 | S | real | Blank implementation plan template: outcome, workstreams, risks, rollout. |
| Product Lifecycle - Initiatives | 2162524181 | S | real | Rules for initiative workspaces, naming, README pointers and artifact index generation. |
| Product Lifecycle - Jira Query Shortcuts | 2162622465 | M | real | Reference copy of reusable JQL queries from jira/queries.yaml. |

## 00 Start Here (`2162720769`)

| Title | pageId | Size | Status | Gist |
| --- | --- | --- | --- | --- |
| Technology at a Glance | 2162688011 | S | stub | placeholder |
| Product & System Map | 2162753557 | S | stub | placeholder |
| Service & Repository Catalog | 2162524247 | S | stub | placeholder |
| Environments | 2162556950 | S | stub | placeholder |
| Glossary | 2162720809 | S | stub | placeholder |
| Onboarding Paths | 2162622525 | S | stub | placeholder |

## 10 Product Handbook (`2162753537`)

| Title | pageId | Size | Status | Gist |
| --- | --- | --- | --- | --- |
| Radius | 2162327640 | S | stub | placeholder |
| myMathnasium | 2162032800 | S | stub | placeholder |
| Scheduling | 2162556970 | S | stub | placeholder |
| Enrollment & Membership | 2162688032 | S | stub | placeholder |
| Billing & Payments | 2162688052 | S | stub | placeholder |
| Leads & CRM | 2162556990 | S | stub | placeholder |
| Attendance | 2162720829 | S | stub | placeholder |
| Curriculum, Assessments & Learning Plans | 2162458672 | S | stub | placeholder |
| Notifications & Communications | 2162819076 | S | stub | placeholder |
| Reporting & Data | 2162327660 | S | stub | placeholder |

## 20 Architecture (`2162360405`)

| Title | pageId | Size | Status | Gist |
| --- | --- | --- | --- | --- |
| System Landscape | 2162688072 | S | stub | placeholder |
| Service Catalog | 2162819096 | S | stub | placeholder |
| Data Architecture | 2162753577 | S | stub | placeholder |
| Identity, Authentication & Authorization | 2162229393 | S | stub | placeholder |
| Events, Messaging & Integration Contracts | 2162622545 | S | stub | placeholder |
| Caching Architecture | 2162688092 | S | stub | placeholder |
| Observability & Operational Architecture | 2162262141 | S | stub | placeholder |
| Architecture Decision Index | 2162458692 | S | stub | placeholder |

## 30 Engineering Standards (`2162786305`)

| Title | pageId | Size | Status | Gist |
| --- | --- | --- | --- | --- |
| Standards Overview | 2162327680 | S | stub | placeholder |
| Radius Engineering Standard | 2162032820 | S | stub | placeholder |
| API & Service Standard | 2162065463 | S | stub | placeholder |
| SQL, DAL & Data Access Standard | 2162098259 | M | real | Normative rules: EF vs stored procedures, isolation, query design, transactions, DB changes. |
| Frontend Engineering Standard | 2162491461 | S | stub | placeholder |
| Microservice Engineering Standard | 2162458712 | S | stub | placeholder |
| Testing & Quality Standard | 2162622565 | S | stub | placeholder |
| Security Standard | 2162032840 | S | stub | placeholder |
| Logging & Observability Standard | 2162491481 | S | stub | placeholder |
| Caching Standard | 2162458732 | S | stub | placeholder |

## 40 Product & Delivery Process (`2162524224`)

| Title | pageId | Size | Status | Gist |
| --- | --- | --- | --- | --- |
| Product Lifecycle | 2162131024 | S | stub | placeholder |
| Work Item Standards | 2162557010 | S | stub | placeholder |
| Product Readiness | 2162524267 | S | stub | placeholder |
| Engineering Delivery Flow | 2162327700 | S | stub | placeholder |
| Release Confidence & Readiness | 2162622585 | S | stub | placeholder |
| Release Management | 2162524287 | S | stub | placeholder |
| Vendor & Team Collaboration | 2162753597 | S | stub | placeholder |

## 50 Operations & Support (`2162720789`)

| Title | pageId | Size | Status | Gist |
| --- | --- | --- | --- | --- |
| Deployment Runbooks | 2162032860 | S | stub | placeholder |
| Database & Data Migration Runbooks | 2162425907 | S | stub | placeholder |
| Production Access | 2162524307 | S | stub | placeholder |
| Troubleshooting Index | 2162262161 | S | stub | placeholder |
| Scheduled Jobs & Recovery | 2162786388 | S | stub | placeholder |
| Data Repair & Reconciliation | 2162491501 | S | stub | placeholder |
| Center & Customer Support Procedures | 2162393141 | S | stub | placeholder |

## 60 History & Decisions (`2162786325`)

| Title | pageId | Size | Status | Gist |
| --- | --- | --- | --- | --- |
| Architecture Decision Records | 2162688112 | S | stub | placeholder |
| Superseded Standards | 2162262181 | S | stub | placeholder |
| Migration History | 2162229413 | S | stub | placeholder |
| Release & Product History | 2162098279 | S | stub | placeholder |

## Radius database reference (SQL)

Hub: Radius Database Reference (`2162622605`), under Data Architecture. Read the hub first (small: gotchas and the map). Overview and Conventions and the domain pages are large; fetch each at most once per session, and search first for single columns or rules.

| Title | pageId | Size | Status | Gist |
| --- | --- | --- | --- | --- |
| Radius Database Reference | 2162622605 | S | real | Hub for Radius SQL guide: provenance, child page map and top cross-domain gotchas. |
| Radius DB Reference - Overview and Conventions | 2162098302 | XL | real | Schema conventions: naming, soft delete, tenancy, time, sensitive columns, query safety, glossary. |
| Radius DB Reference - Lead and Enrollment Funnel | 2162065483 | XL | real | Leads, lead sources, enrollment opportunities, DEE flow, funnel metric definitions and snippets. |
| Radius DB Reference - Billing and Membership | 2162458752 | XL | real | Plans, enrollments, holds, invoices, payments, discounts, credits and billing joins. |
| Radius DB Reference - Scheduling and Attendance | 2162229433 | L | real | Attendance, enrollment types, holds and scheduling tables; no Session table exists. |
| Radius DB Reference - Curriculum and Assessment | 2162098323 | L | real | Assessments, scoring, grouped results, learning plans, assignments, progress checks, notes. |
| Radius DB Reference - People and Organization | 2162688135 | L | real | Centers, role-tree scoping, accounts, guardians, students, employees, time zones. |

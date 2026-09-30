# Playbook: Monthly Radius Release Documentation

Read: [`standards/jira-conventions.md`](../standards/jira-conventions.md), [`standards/story.md`](../standards/story.md#multi-repo-work-and-sub-tasks)

Run monthly, the day after each Radius release (typically mid-month; check the release calendar in Confluence if the date shifts). Output is **three new Confluence pages** in the IT Process Documentation (IPD) space.

| Page | Goes under |
| --- | --- |
| `<MON-YYYY> Release Notes` | [Radius Release Notes - 2026](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2148499457/Radius+Release+Notes+-+2026) |
| `<MON-YYYY> Manual Update Log` | [Radius Manual updates - 2026](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2148433921/Radius+Manual+updates+-+2026) |
| `Radius Release – <Month DD, YYYY>` (draft announcement for team review) | [Radius Release Announcements – 2026](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2147844098/Radius+Release+Announcements+2026) |

Each year has its own container pages. Create the `… - 2027` set alongside them when the year turns.

Read first: [Radius Release Documentation](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2148106241/Radius+Release+Documentation) (queries, tone rules, announcement format, known traps). Then open the most recent month's pages and match their structure.

**Do not open Mathnasium Matters or the Radius Manual.** Both sit behind logins automation cannot reach. Confluence is the system of record: read Jira, the Release Testing sheet and the archived announcements. Do not skip the reconciliation step.

## Steps

### 1. Identify the release

1. Determine the current month's Fix Version for both projects (`MON-YYYY`, see `standards/jira-conventions.md#fix-versions`). Confirm against recent tickets in both projects.
2. Check items outside the monthly version:
   `project in (RAD, MYM) AND fixVersion in ("<MON-YYYY>-SR", "HOTFIX") ORDER BY key ASC`.
   A `-SR` item that shipped this month is a deliberate decision. Flag them.

### 2. Pull every ticket

1. Run `release_scope` from `jira/queries.yaml` **separately** for RAD and MYM. Do not combine, and do not filter by status or type at this stage.
2. Pull summary, description, status, issue type, parent, labels, components and comments.
3. For any ticket unclear from its summary, read the full comment thread before classifying. Deployment comments show what shipped vs. slipped, and **requirements corrected late in the cycle often live only in comments**.

### 3. Classify every ticket

Classification here is specific to release documentation.

- **User-facing Feature:** adds or changes a capability someone would notice, including admin-only changes. `[RADIUS]` tickets in MYM are Radius-side admin work; keep them in the MYM subsection.
- **User-facing Fix:** restores intended behavior that was broken.
- **Backend-only / dev-only:** excluded from the notes but recorded in the excluded table with a reason (infrastructure, logging, stored procedure optimization, internal debug endpoints, SEO tags, backend halves of paired features).

Projects and headings are workstreams, not surfaces. MYM mixes admin-facing Radius work with Guardian Portal work, and a RAD ticket can belong to the myMathnasium/scheduling workstream. Group by what the change *is*.

**Folding:** a Bug of Story folds into its parent Story. An API or enabler item that exists only to serve a user-facing Story folds into it. Legacy `[RADIUS]` + `[Scheduling MS]` pairs for one capability become one entry.

**Backend-only is not automatically unpublishable.** If a backend item has a user-visible consequence (for example an idempotency change centers had been reporting), flag it. Flag anything ambiguous under "Needs human judgment".

### 4. Reconcile

The Mathnasium Matters post is **not** an input. It is curated for franchisees and omits regional fixes, minor cleanup, feature-flagged work and internal tooling. The Release Notes page is the source the post is drafted from.

Before publication, reconcile against internal records:

- **The release announcement** in Slack `#radius-project-updates` states a scope count ("N bug fixes, M features"). Reproduce it exactly. If not, the gap is usually a hotfix excluded from the count, paired sub-tasks double-counted, or a release-independent item with no monthly Fix Version. Explain the difference on the page rather than adjusting numbers.
- **The Release Testing sheet** (Google Drive, `Release Testing - YYYY-MM-DD`, owned by QA) lists every item with its functional **Area** and **APP Category**. Use these for functional-area headers, and note items pulled from the release or hidden behind feature flags.

### 5. Identify affected Radius Manual pages

1. Work from the nav map on [Radius Manual Management](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/1549697026/Radius+Manual+Management) (HelpDocs: `mathnasium-radiusmanual.helpdocsonline.com`).
2. For every user-facing Feature, and any Fix that corrects something the Manual actively describes wrong, identify the page and nav path. Classify as **edit**, **new content** or **verify only**.
3. **Produce a changelog, not drafted copy.** Applications Support writes the wording where the current text is visible. Do not draft paragraphs for pages you cannot read or assert what a page "currently says".
4. Where functionality has no Manual page, say so and propose the section it belongs under.

### 6. Create the three Confluence pages

Every ticket is accounted for on the first two pages. Anything not reported goes in an **excluded** section with a per-ticket reason. State the coverage arithmetic near the top of each page: *N reported, M excluded, total = the release scope.*

**Page 1, Release Notes.** Split into RAD and MYM. Within each, an H3 per functional area from the Release Testing sheet, Features before Fixes, one short plain-language sentence per bullet: matter-of-fact, third person, present tense, no "Fixed:" prefix. Add sub-bullets for caveats (feature flags, country or role restrictions). Cite the ticket key on every bullet, as a link. Include the reconciliation check at the top, an **Excluded from these notes** table with reasons (backend-only, developer-only, folded, never reached production), and a **Needs human judgment** list. Also record what was left out of the announcement and why.

**Page 2, Manual Update Log.** Three tables: **Edits to existing pages**, **New content required**, **Verify only**. Columns: `# | Manual page | Nav path | What changed | Driver ticket(s) | Status`. Link the HelpDocs URL where the slug is known. Status starts at "Not started" and is updated by Applications Support. Also include structural gaps, open drafts from the Radius Manual Tracker that overlap, and a **draft Change Log entry** (a month heading, one linked bullet per page in the Change Log's phrasing, for example *Updated screenshot and language for [Page]*). End with **Excluded from the Manual**, grouped by reason: Guardian Portal changes, fixes that restore already-documented behavior, and backend, developer-only and non-production items.

**Page 3, draft announcement.** Franchisee-facing, clearly marked as a draft for team review before it is published to Mathnasium Matters. Cut down from Page 1 and match the house format exactly:

- Fixed preamble: *"The Radius Team is hard at work to enhance and improve the Radius Experience. Find out what changes may be important to you! Please review our Radius Release Highlights below. These updates will be implemented and available on **\<Day, Month DD, YYYY\>.**"* followed by the 5:00–8:00 a.m. US PT maintenance-window paragraph.
- Features then Fixes, each with an H3 per functional area. **No RAD / MYM split**: all scheduling and Guardian Portal work sits under one "myMathnasium" heading in each section, wherever the ticket lives (a workstream label, not a surface).
- One short sentence per bullet, third person, no "Fixed:" prefix, **no ticket keys**.
- Leave out regional fixes, minor cleanup, feature-flagged work off by default, and internal tooling, and record the cuts on Page 1.
- Flag anything held back that a center would plausibly notice; a new capability or guardian-visible change needs a deliberate decision.

### 7. Verify before finishing

- Every ticket pulled in step 2 appears in the notes, the excluded table or the no-impact list.
- No bullet cites a key that was not in the pull.
- Counts reconcile with the Slack announcement, or the difference is explained.
- Every announcement bullet traces to a ticket.

## Traps

- Role lists drift from ticket titles. A ticket titled "allow administrators to…" may have shipped to ACD/CD/FO/Admin after a mid-cycle decision. Trust QA evidence in the comments.
- Feature-flagged work needs a publish decision, not an assumption.
- A fix "released" in a prior month that regressed should be verified in production before it is claimed again.
- Separately deployed microservices (parent-reports, scheduling fanout, notifications) can land after the main window; check the deployment thread in `#radiusrelease`.
- Not every release gets a post (April 2026 had none; special and hotfix releases go out by email). Posts can also be wrong: May 2026 republished March's content under a March date.
- If the Manual nav changes, update the map on Radius Manual Management. It is the only thing standing between this playbook and guesswork.

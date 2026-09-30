# Monthly Radius Release Documentation Task (v2)

**Suggested cadence:** Monthly, the day after each Radius release (typically mid-month — check the release calendar in Confluence if the date shifts).

**Paste the instructions below into Cowork when creating the scheduled task.**

**What changed from v1:** the task no longer tries to open Mathnasium Matters or the Radius Manual — both sit behind logins automation can't reach, and v1 silently produced unverified work as a result. Confluence is now the system of record. The task reads Jira, the release-testing sheet, and the archived announcements, and writes two Confluence pages.

---

## Task Instructions (paste into Cowork)

You are producing the monthly Radius release documentation. The output is **three new Confluence pages** in the IT Process Documentation (IPD) space:

| Page | Goes under |
| --- | --- |
| `<MON-YYYY> Release Notes` | [Radius Release Notes - 2026](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2148499457/Radius+Release+Notes+-+2026) |
| `<MON-YYYY> Manual Update Log` | [Radius Manual updates - 2026](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2148433921/Radius+Manual+updates+-+2026) |
| `Radius Release – <Month DD, YYYY>` — draft announcement for team review | [Radius Release Announcements – 2026](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2147844098/Radius+Release+Announcements+2026) |

Each year has its own set of container pages, so the structure archives itself. Create `… - 2027` alongside them when the year turns.

**Read this first:** [Radius Release Documentation](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2148106241/Radius+Release+Documentation). It carries the queries, classification rules, tone rules, announcement format, and known traps. Then open the most recent month's pages and match their structure.

Work through these steps in order. Don't skip the reconciliation step — it's the part most likely to be incomplete if rushed.

### Step 1: Identify the release

Determine the current month's fix version for both Jira projects (format `MON-YYYY`, e.g. `SEP-2026`). Confirm by checking recent tickets in both projects before assuming the pattern holds.

Also check for items sitting outside the monthly version — service releases and hotfixes:

```
project in (RAD, MYM) AND fixVersion in ("<MON-YYYY>-SR", "HOTFIX") ORDER BY key ASC
```

These are not automatically in scope, but a `-SR` item that shipped this month is a deliberate decision, not a query boundary. Flag them.

### Step 2: Pull every ticket in both projects

Run separately for each project — do not combine into one query, and do not filter by status or issue type at this stage (pull everything, then classify):

```
project = RAD AND fixVersion = "<CURRENT-MONTH>" ORDER BY key ASC
project = MYM AND fixVersion = "<CURRENT-MONTH>" ORDER BY key ASC
```

Pull `summary`, `description`, `status`, `issuetype`, `parent`, `labels`, `components`, and `comment` for each. For any ticket whose purpose isn't clear from the summary alone, read the full comment thread before classifying it — deployment comments confirm what actually shipped vs. what slipped, and **requirements corrected late in the cycle often live only in comments while the description stays wrong**.

### Step 3: Classify every ticket

For each ticket, decide:

- **User-facing Feature** — adds or changes a capability someone would notice, including *admin-only* capability changes (tickets tagged `[RADIUS]` in the MYM project are admin-facing Radius work even though the project is myMathnasium — label them as Radius-side, but keep them in the MYM subsection since the split is by project).

**Projects and headings describe workstreams, not surfaces.** The MYM project mixes admin-facing Radius work in with Guardian Portal work — and the reverse holds too: a RAD ticket can belong to the myMathnasium/scheduling workstream. Group by what the change *is*, not by which project tracked it.
- **User-facing Fix** — restores intended behavior that was broken.
- **Backend-only / dev-only** — exclude from the notes but record in the excluded table with a reason: infrastructure, logging, stored procedure optimization, internal debug endpoints, SEO tags, backend halves of paired admin features.

**Folding rules:** a `[RADIUS]` + `[Scheduling MS]` pair for one capability becomes one entry. A story bug folds into its parent story. An API/enabler story that exists only to serve a user-facing story folds into that story.

**Backend-only isn't automatically unpublishable.** September published RAD-7601 — an idempotency change with no UI at all — because it fixed a problem centers had been reporting. If a backend item has a user-visible *consequence*, flag it rather than burying it.

Flag anything genuinely ambiguous rather than guessing — list it under "Needs human judgment" at the end of the page.

### Step 4: Reconcile

**The Mathnasium Matters post is not an input.** It sits behind Radius SSO, it's curated for franchisees, and it deliberately omits regional fixes, minor cleanup, feature-flagged work, and internal admin tooling. The Confluence Release Notes page you're writing is the **source the post is drafted from**. For scale: September published roughly 30 bullets against 55 tickets.

**Before publication**, reconcile against internal records:

- **The release announcement** in Slack `#radius-project-updates` states a scope count ("N bug fixes, M features"). Your classification should reproduce it exactly. If it doesn't, the gap is usually a hotfix excluded from the count, paired sub-tasks double-counted, or a release-independent item with no monthly fix version. Explain the difference on the page rather than quietly adjusting your numbers to match.
- **The Release Testing sheet** for the release date (Google Drive, `Release Testing - YYYY-MM-DD`, owned by QA). It lists every item with its functional **Area** and **APP Category** — use these for the functional-area headers rather than inventing groupings. It also flags items pulled from the release and items hidden behind feature flags.

The announcement itself is **drafted in Step 6** and cut down from the Release Notes page, so there is nothing to reverse-engineer. The archive of past announcements is the format template — see [Radius Release Announcements – 2026](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2147844098/Radius+Release+Announcements+2026) for a year of real examples.

### Step 5: Identify affected Radius Manual pages

The Manual is on **HelpDocs** at `mathnasium-radiusmanual.helpdocsonline.com`. Work from the **nav map** on [Radius Manual Management](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/1549697026/Radius+Manual+Management) — it carries the section tree, known page slugs, and the writing conventions. Do not attempt to open the Manual.

For every user-facing Feature — and any Fix that corrects something the manual actively describes wrong — identify the affected page and its nav path. Classify each as **edit**, **new content**, or **verify only**.

**Produce a changelog, not drafted copy.** Applications Support writes the wording directly in the Manual where the current text is visible. Your job is to say what changed and where it lands. Do not draft replacement paragraphs for pages you cannot read, and do not assert what a page "currently says."

Where affected functionality has no manual page at all, say so explicitly and propose which section it belongs under.

### Step 6: Create the three Confluence pages

**Every ticket must be accounted for on the first two pages.** Whatever isn't reported goes in an **excluded** section with a per-ticket reason, so a reader never has to wonder whether something was considered and dropped or simply missed. State the coverage arithmetic near the top of each page — *N reported, M excluded, total = the release scope.*

**Page 1 — `<MON-YYYY> Release Notes`**

Split into **RAD** and **MYM**. Within each, organize by functional area (H3 per area, taken from the Release Testing sheet), Features before Fixes, one short plain-language sentence per bullet. Match the house tone: matter-of-fact, third person, present tense, no "Fixed:" prefixes — e.g. *"Double clicking on the event will open the edit event window."* Add a sub-bullet for scope caveats (feature flags, country restrictions, role restrictions). Cite the ticket key on every bullet.

Include: the reconciliation check at the top, every user-facing item, an **Excluded from these notes** table giving each unreported ticket and why (backend-only, developer-only, folded into another bullet, never reached production), and a **Needs human judgment** list.

*Note the structural difference from the published post — it has no RAD/MYM split and groups everything under Features then Fixes. Don't copy that into the internal page.*

**Page 2 — `<MON-YYYY> Manual Update Log`**

A changelog with three tables — **Edits to existing pages**, **New content required**, **Verify only** — each with columns: `# | Manual page | Nav path | What changed | Driver ticket(s) | Status`. Link the page to its HelpDocs URL where the slug is known. Status starts at "Not started" and is updated by Applications Support.

Also include: any structural gaps (functionality with no manual page), open drafts from the Radius Manual Tracker that overlap this month's work, and a **draft Change Log entry** — a month heading with one linked bullet per page in the Change Log's own phrasing (*Updated screenshot and language for [Page]*), ready to trim and paste.

End with an **Excluded from the Manual** section accounting for every remaining ticket, grouped by reason. The recurring categories are: *Guardian Portal changes* (the Manual documents Radius for franchise users and has no myMathnasium section), *fixes that restore already-documented behaviour* (the Manual was right and the application was wrong), and *backend, developer-only and non-production* items.

**Page 3 — `Radius Release – <Month DD, YYYY>` (draft announcement)**

The franchisee-facing announcement, drafted for the team to review and approve before it's published to Mathnasium Matters. Mark it clearly as a draft. Cut down from Page 1 and match the house format exactly:

- **Fixed preamble:** *"The Radius Team is hard at work to enhance and improve the Radius Experience. Find out what changes may be important to you! Please review our Radius Release Highlights below. These updates will be implemented and available on **\<Day, Month DD, YYYY\>.**"* followed by the 5:00–8:00 a.m. US PT maintenance-window paragraph.
- **Features** then **Fixes**, each grouped by functional area with an H3 per area. **No RAD / MYM split** — all scheduling and Guardian Portal work sits under a single "myMathnasium" heading in each section, wherever the ticket lives. That heading is a workstream label, not a surface: September's post correctly carried "Updates to Appointment Management page *in Radius*" and a Scheduling Calendar fix under it.
- One short sentence per bullet, third person, no "Fixed:" prefixes, **no ticket keys**.
- Leave out regional fixes, minor cleanup, feature-flagged work that's off by default, and internal tooling — and record on Page 1 what you left out and why.
- Flag anything held back that a center would plausibly notice. A new capability or a guardian-visible change deserves a deliberate decision, not a silent omission.

### Step 7: Verify before finishing

Confirm every ticket pulled in Step 2 appears somewhere — in the notes, the excluded table, or the no-impact list. Confirm no bullet cites a ticket key that wasn't in the pull. Confirm the counts reconcile against the Slack announcement, or that the difference is explained. Confirm every bullet in the draft announcement traces to a ticket.

---

## Notes for next time this task runs

- **Don't try to open Mathnasium Matters or the HelpDocs Manual.** Both require interactive logins. v1 of this task assumed a Claude in Chrome handoff that never happened, and the result was manual edits drafted against pages nobody had read. The announcement archive and the nav map exist so the task doesn't need either login.
- **The announcement is drafted, not transcribed.** The team reviews and approves it before publication. Write it to be publishable as-is, and make the cuts visible on the Release Notes page so reviewers can see what was left out rather than having to spot it.
- The MYM project contains admin-facing Radius functionality mixed in with Guardian Portal work — always check ticket tags/summaries for "Radius," "[RADIUS]," or "Center Admin" rather than assuming MYM = Guardian-only.
- Paired subtasks (`[RADIUS]` + `[Scheduling MS]` for the same capability) become one release-notes bullet, not two.
- Role lists drift from ticket titles. A ticket titled "allow administrators to…" may have shipped to ACD/CD/FO/Admin after a mid-cycle decision. Trust the QA evidence in the comments.
- Feature-flagged work needs a publish decision, not an assumption. Items behind a flag that's off by default may not belong in a post that reaches every franchisee.
- A fix that was already "released" in a prior month and regressed should be verified in production before it's claimed again.
- Separately deployed microservices (parent-reports, scheduling fanout, notifications) can land after the main release window — check the deployment thread in `#radiusrelease`.
- Not every release gets a post — April 2026 had none, and special/hotfix releases go out by email instead. Posts can also be wrong: May 2026 republished March's content under a March date.
- If the Manual nav changes, update the map on Radius Manual Management. The map is the only thing standing between this task and guesswork.

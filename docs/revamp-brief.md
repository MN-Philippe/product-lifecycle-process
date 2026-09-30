# Product Lifecycle Repo — Revamp Brief (Standard v2)

**For:** Claude Code, working in `product-lifecycle-process`.
**Author of decisions:** Philippe Cavé, 9/30/2026.
**Status:** Decisions in "Decided" sections are final. Items marked `DEFAULT — TBC` use a recommended default. Implement them as written and list them in the PR description so they can be confirmed.

---

## How to work

1. Work on a branch named `standard-v2`. Do not commit to `main`.
2. Implement the phases in order. Commit at the end of each phase with a message `Phase N: <summary>`.
3. **Stop and ask for review after Phase 2** (the Story standard) before continuing. It drives everything else.
4. **Do not read from or write to Jira.** All Jira facts you need are in this brief.
5. One rule lives in exactly one file. Playbooks, AGENTS.md, and the plugin **link** to standards and never restate rules. If you find yourself copying a rule, link instead.
6. When finished, delete this brief (`docs/revamp-brief.md`) in the final commit so it doesn't become another copy of the rules. Then open a PR summarizing the changes and listing every `DEFAULT — TBC` item.

---

## Why this revamp

- The same Story rules are restated in about 7 files. One rule change took about 20 commits in PR #5.
- The plugin `mathnasium-product-lifecycle` ships hand-copied versions of 9 repo files that will drift.
- A review of 456 RAD/MYM Stories showed the real problems are personas, Story size, weak or missing acceptance criteria, requirements settled in comments, and PRs tracked only in comments. Formatting compliance is not the problem: 74% already follow the Summary format.
- MYM Stories are mostly written by a third-party vendor. The standard must be simple enough for them to follow.
- Guiding principle: **consistency and clarity win over preserving legacy practice.**

---

## Phase 0 — Read before changing anything

Read every file in the repo. Note which rules appear in more than one place. You will collapse them.

---

## Phase 1 — Restructure

Target tree:

```text
README.md                    What the repo is and how to use it (absorb GUIDE.md)
AGENTS.md                    Router only: task → standard/playbook. ≤ 60 lines. No rules.
standards/
  story.md                   (Phase 2) replaces story-quality.md + personas.md
  task.md                    Technical work and Spikes
  bug.md                     from bug-quality.md
  lifecycle.md               from product-lifecycle.md, plus the new gates
  jira-conventions.md        Field IDs, Fix Versions, issue types, repos, markets (absorb context/jira.md)
  ai-release-confidence.md   updated
playbooks/
  write-story.md             rewritten (PM Q&A flow)
  refine-story.md            new
  split-story.md             new
  ready-check.md             new
  review-story.md            slimmed: audit an existing Story against standards/story.md
  decompose-initiative.md    slimmed
  triage-bug.md              slimmed
  intake.md                  slimmed
  release-readiness.md       slimmed
  assess-release-confidence.md  updated
  release-docs.md            new (monthly release notes + Manual update log)
  cleanup.md                 new (retiring replaced tickets)
templates/
  story.md
  task.md
  bug.md
  vendor-guide.md
jira/queries.yaml            updated
tools/
  jira_helper.py             audit rules updated to match the standards
  build_plugin.py            new: generates the plugin from standards/ + playbooks/
  artifact_index.py          unchanged
tests/                       updated + new tests
artifacts/                   keep; fix README (see Phase 9)
initiatives/                 keep
.claude-plugin/marketplace.json   new (Phase 8)
plugins/mathnasium-product-lifecycle/   generated (Phase 8)
.github/workflows/validate.yml    updated
```

Delete after their content is merged:

- `GUIDE.md`
- `context/jira.md`
- `standards/story-quality.md`
- `standards/personas.md`
- `standards/product-lifecycle.md` (renamed to `lifecycle.md`)
- `standards/bug-quality.md` (renamed to `bug.md`)
- `jira/quality-rules.md`. Its checks move into `tools/jira_helper.py`, and each standard gets a short **Checks** table (rule, severity) at the end.

Update every internal link.

---

## Phase 2 — `standards/story.md` (stop for review after this phase)

Write it as the single source for Stories. Keep it tight: rules, one example each, no essays. Content:

### 2.1 The Story on one screen (template)

```text
Summary:  [Repo] As a <Persona>, I want <behavior> so that <outcome>.
          ([Repo] is optional)

Description
  Context             1–3 sentences: the problem and who it affects.
  Current behavior    Only when existing behavior changes.
  Acceptance criteria Numbered AC1, AC2… in Given / When / Then.
  Constraints         Only non-negotiable technical rules, each with its reason.
  Out of scope        Optional.
  Open questions      Each tagged [Business], [Engineering] or [QA]. Must be empty before AC approval.
  Changelog           Dated one-liners for any change after AC approval.

Fields:   Story Points (≤ 5) · Code Dependency (repo) · Pull Requests · Epic · Fix Version
```

- **Empty description is an Error.** The minimum at creation is Context plus at least one AC.
- No comma before "so that".
- The Summary must be understandable by ELT on its own.

### 2.2 Size

- **Maximum 5 Story Points.** A Story over 5 is split before it enters a sprint.
- An unestimated Story cannot receive a Fix Version.
- Use the **Story Points** field only (`customfield_10021`). Do not use "Story point estimate" (`customfield_10909`).
- Split along seams that keep each piece independently testable: a group of ACs, one persona, one repo, or backend rule vs. UI.
- Evidence to cite in one line: Stories over 2,500 characters averaged 0.95 Bugs of Story, against 0.16 for short ones.

### 2.3 Personas (Decided)

| Persona | Use for |
| --- | --- |
| Center Director (CD) | **Default** for any center-facing Radius work |
| Admin | **Default** for HQ users and HQ-only functions |
| Guardian | **Default** for myMathnasium and the Guardian Portal |
| Franchise Owner (FO) | Only when owner-only permissions or finances matter |
| Assistant Center Director (ACD) | Only when ACD access differs from CD |
| Instructor | Instructional workflows |

`DEFAULT — TBC`: keep **Education Manager** as a persona for curriculum work. Fold **Regional Manager** into Admin.

**Retired, never use:** Center Admin, User, Radius User, Admin User, Center Owner, Support Admin (use Admin), Developer (technical work is a Task — see `standards/task.md`).

**Role access goes in an AC, not the persona.** When several roles get a capability, the Summary uses the default persona, and one AC states exactly who has access and who doesn't. Example:

> AC5: Given a user with the ACD, CD, FO or Admin profile, the button is visible; given an Instructor, it is hidden.

### 2.4 International markets (Decided: market-specific personas matter)

Format: the market is an adjective on the persona.

> As a UK Center Director… / As a Canadian Guardian…

- US is the default and is never stated.
- Fixed market list (`DEFAULT — TBC`): Canadian, UK, Australian, Romanian, Mexican, Saudi, Singaporean. Use **International** when the Story applies to every non-US market.
- Also apply one label per market from a fixed list (`DEFAULT — TBC`): `market-CA`, `market-UK`, `market-AU`, `market-RO`, `market-MX`, `market-SA`, `market-SG`, `market-INTL`. These replace the legacy labels Romania, Australia, SaudiArabia and Mexico.
- Market differences in behavior get their own AC ("Given a Canadian center…").

### 2.5 Brackets (Decided: repo allowed but not required)

- A repo bracket is **optional** in both projects. When used, it is the **only** bracket and comes from the repo list in `standards/jira-conventions.md`.
- The repo is always recorded in the **Code Dependency** field (`customfield_11147`), required by Ready for Dev. A bracket, when present, must match it.
- Not allowed in the Summary:
    - Feature names such as [Calendar 2.0]. The feature is the Epic.
    - [SPIKE] or [PoC]. Use the Spike issue type.
    - [Absorbed…], [Consolidated…] or [Duplicate]. Use a resolution plus an "is replaced by" link.
    - [BE] or [FE]. Use the repo name.

### 2.6 Acceptance criteria → test cases (Decided: ACs central and must lead to TCs; TCs upstream)

Lifecycle of a Story's definition:

1. **PM drafts ACs**: numbered AC1, AC2…, in Given / When / Then.
2. **AC approval**: PM, engineering lead (vendor lead for MYM) and QA review in refinement. Requires open questions empty and Story Points set. `DEFAULT — TBC`: recorded by adding the label `ac-approved`.
3. **QA writes test cases within 2 business days**, each mapped to an AC number (TC 3.1 tests AC3). `DEFAULT — TBC`: stored in the Jira **Test plan** field (`customfield_10956`).
4. **Ready for Dev**: see the checklist in `standards/lifecycle.md`.
5. QA in DEV and QA in STG execute those test cases. Results may be posted in comments.

AC writing rules:

- One behavior per AC, with an observable result in the Then.
- Role access and market differences stated explicitly.
- Existing behavior that must not change is written as regression ACs ("Then the existing cancellation window still applies").
- A mockup supports an AC but doesn't replace it. "Matches the mockup" is never an AC; name the elements that matter.
- If QA can't write a test case for an AC, the AC goes back to the PM.

### 2.7 Requirements vs. constraints vs. implementation ideas

This replaces the old "no code-design checklist" wording.

| Tier | What it is | Where it lives |
| --- | --- | --- |
| Acceptance criteria | Behavior anyone can observe: UI, API response, data outcome, email | Description (required) |
| Constraint | A rule the solution must obey, stated with its reason: security, contract between repos, compatibility or migration, performance target, data retention, compliance | Description → Constraints |
| Implementation idea | A suggestion for how to build it | A comment marked "non-binding", the PR, or a technical design doc. **Never the description.** |

**The test:** if engineering built it differently and every AC passed, would we reject it? Yes → it's a constraint; write it with the reason. No → it's an implementation idea and stays out of the description.

Good constraint: a cross-repo contract. For example, *"Scheduling accepts max_daily_appointments and max_weekly_appointments; null means inherit the center default."* It defines the interface, not the internals.

Not a constraint: naming which service class or stored procedure to use. That belongs in the PR or the implementing repo's coding standards.

### 2.8 Multi-repo work and sub-tasks (Decided: sub-tasks aren't in the standard; find a better way)

- A multi-repo feature is **an Epic with one Story per repo**, each 5 points or less, linked with "blocks" where order matters.
- **Do not use sub-tasks for implementation steps or per-repo splits.** Reasons to state in one line each:
    - Sub-tasks share the parent's sprint and Fix Version, so they can't be committed separately.
    - Sub-task points don't roll into velocity by default.
    - Release notes have to fold them back together by hand.
- **Keep Bug of Story.** It is the one child type, and it rides the parent Story's release path.
- A step list that engineering or the vendor wants to track goes in the description as a checklist, or in the PR.
- Every Story belongs to an Epic.

### 2.9 Description vs. comments (Decided: comments are fine but mustn't leave the description inconsistent)

- The description is the **only** source of truth for scope and ACs.
- Comments are for questions, discussion and QA evidence.
- When a comment answers a question that changes scope or an AC, the PM updates the description **the same day**, adds a Changelog line after AC approval, and replies "Description updated (AC4)".
- After a Fix Version is set, an AC change also triggers a release-confidence recheck.

### 2.10 Pull requests (Decided)

- Every PR is recorded in the **Pull Requests** field (`customfield_11279`), whoever opens it. Comments may add context, but can never be the only record.
- A Story in Code Review or later with an empty Pull Requests field is a Warning.

### 2.11 The vendor

- The standard applies to every ticket, whoever writes it.
- For MYM, Mathnasium's PM owns the Summary, the ACs and AC approval.
- The vendor owns Tasks, estimates and the Pull Requests field.
- See `templates/vendor-guide.md`.

### 2.12 Checks (end of file)

A table of every rule with severity, used by `tools/jira_helper.py` (see Phase 7).

---

## Phase 3 — Other standards

### `standards/task.md`

Technical work with no product-observable behavior is a **Task**, never a Story with a Developer persona.

- **Summary:** `[Repo] Verb + object`. Example: *[Scheduling] Add OTLP metrics to the Fanout service*. The repo bracket is optional, as for Stories.
- **Description:** Objective / Why / Done when.
- **Size:** 5 points maximum.
- **Fields:** the same PR field and Code Dependency rules as Stories.

Spike:

- Uses the Spike issue type, never a [SPIKE] bracket.
- **Description:** question to answer / scope / expected output / timebox.

### `standards/bug.md`

Carry over `bug-quality.md` content and trim duplication. Keep:

- classify before committing to a fix;
- categorize under the impacted feature (no generic Bug Fixing Epic);
- Watchlist rules;
- functional triage and technical assessment;
- Bug of Story vs. standalone.

Add: a standalone Bug also needs a non-empty description (Observed / Expected / Steps / Environment / Impact).

### `standards/lifecycle.md`

Carry over `product-lifecycle.md`, trimmed. Add the gates:

**AC approval.** Defined in `standards/story.md` §2.6. Link to it; don't restate it.

**Ready for Dev checklist.** A Story is Ready for Dev when all are true:

- Summary in format, with the correct persona (and repo bracket if used);
- Epic set;
- description non-empty;
- ACs approved;
- open questions empty;
- Story Points 5 or less;
- Code Dependency set;
- test cases attached and mapped to ACs.

**Fix Version.** Assigned by Product + Engineering once the Story is estimated at 5 points or less, normally at Ready for Dev. The Fix Version is the delivery commitment.

Keep the existing delivery pipeline, the expedite path, and the "open questions not yet standardized" list, updated to remove items this brief decides.

### `standards/jira-conventions.md`

Absorb `context/jira.md`. It should state the site, cloudId and hyperlink rule, followed by the sections below.

- **Site:** `https://mathnasium.atlassian.net`
- **cloudId:** `abd26ef1-c908-455d-8b20-516e025731b2`
- **Projects:** RAD (Radius), MYM (myMathnasium). MYM spans multiple repos; RAD is mostly Radius, but not only.
- **Hyperlink rule:** keep the existing rule. Every Jira key in output is a link.

**Issue types:** Epic, Story, Task, Spike, Bug, Bug of Story, Sub-task. Sub-task is legacy; don't create new ones for implementation.

**Fields** (verified on MYM-565):

| Field | ID | Use |
| --- | --- | --- |
| Story Points | customfield_10021 | The only estimate field |
| Story point estimate | customfield_10909 | Do not use |
| Pull Requests | customfield_11279 | Required once a PR exists |
| Development (GitHub) | customfield_10500 | Read-only PR signal from the GitHub integration |
| Code Dependency | customfield_11147 | Repo(s) touched; required by Ready for Dev |
| Test plan | customfield_10956 | Test cases (`DEFAULT — TBC`) |
| Delivery Risk | customfield_11382 | Possibly the AI Release Confidence target (`DEFAULT — TBC`) |
| Business Requirements Finalized | customfield_11383 | Business approval |
| Original Release Target | customfield_11348 | First committed release |
| Confirmed Issue | customfield_11016 | Bug Watchlist state |
| Epic Link | customfield_10016 | Legacy parent link |
| Sprint | customfield_10020 | Sprint |

**Fix Versions:**

| Pattern | Meaning |
| --- | --- |
| `MON-YYYY` (e.g. `OCT-2026`) | Monthly release — a delivery commitment |
| `MON-YYYY-SR`, `-SR2` | Service release in that month — a delivery commitment |
| `HOTFIX` | Hotfix — a delivery commitment |
| `N/A` | Work that is never released (scripts, research, testing). **Not** a delivery commitment. |
| `FREEZE` | `DEFAULT — TBC`: treated as not a delivery commitment until its meaning is confirmed |

Always take release dates from the Jira version record, not from the name.

**Repo list** (`DEFAULT — TBC`; bracket name → GitHub repo):

- [Radius] → mathnasium/Radius
- [Radius API DataService] → mathnasium/Radius-API-DataService
- [AWSToRadius] → mathnasium/AWSToRadius
- [Scheduling] → mathnasium/Scheduling-Microservice
- [Guardian Portal] → the Guardian Portal front end
- [Guardian Portal API] → mathnasium/guardian-portal-api
- [Notifications] → the Notifications microservice
- [Fanout] → the Fanout service
- [DAL] → the Data Access Layer
- [Parent Reports] → the parent-reports microservice
- [Database] → schema-only changes

Record the Code Dependency option name for each where known (e.g. "Scheduling Microservice").

**Market list:** reference `standards/story.md` §2.4. Don't restate it.

**Statuses observed** (for interpretation only): To Do, In Progress, CODE REVIEW / IN CODE REVIEW, In QA - HTD, IN QA - MATHNASIUM, IN PROGRESS - QA, READY FOR STG, READY FOR QA in STG, READY FOR PROD, Done. `In QA - HTD` is the vendor's QA; `IN QA - MATHNASIUM` is internal QA.

### `standards/ai-release-confidence.md` (Decided: must be more aware)

Keep the experiment framing (On Track / Watch / At Risk; AI owns Confidence and Reason; humans own Feedback; daily cadence; don't rewrite unchanged values). Change the following.

**Scope.** Stories, Tasks and standalone Bugs whose Fix Version is a delivery commitment. Exclude `N/A` and `FREEZE`: today these two alone pull 54 uncommitted items into scope.

**New signals:**

| Signal | Source | What it catches |
| --- | --- | --- |
| PR state vs. Jira status | Pull Requests + Development fields | Work further along or behind than its status says |
| Open Bugs of Story | Child items | Defects found close to release |
| Size | Story Points | Over 5 or unestimated, with a Fix Version |
| AC changes after commitment | Changelog section + description history | Late scope change |
| Blocked siblings | "blocks" links within the Epic | A repo Story waiting on another repo |
| Vendor vs. Mathnasium QA | Statuses | Work stuck at the handoff |
| Release milestones | Release calendar: code freeze, branch cut | Time left measured to the real cutoff |
| Readiness | `ac-approved` label + test cases present | Committed work that was never Ready for Dev |

**Write targets.** `DEFAULT — TBC`: the field names "AI Release Confidence / Reason / Feedback" were not found on MYM-565, but "Delivery Risk" (customfield_11382) exists. Add a clearly marked TODO to confirm the write fields before the job's scope changes.

**Evaluation.** After each release, measure the lead time of the first warning on items that slipped, and the false-alarm rate on items that shipped normally.

---

## Phase 4 — Playbooks

Every playbook contains **steps only**. It starts with "Read: <links to standards>" and never restates a rule.

### `playbooks/write-story.md` (rewrite)

The PM gives a plain request ("write a story for…"). The agent runs a short Q&A, drafts, and writes only after approval.

1. **Look things up first.** Search Jira for the Epic, related Stories and duplicates. If a duplicate exists, offer to rewrite it instead of creating a new Story. Never ask the PM something Jira can answer.
2. **Ask one round of 3–5 questions**, only about gaps that change what gets built, tested or split. Offer options and a default for each question. Use tap-to-answer input when the client supports it.
   The agent works from this fixed checklist and asks only about what it couldn't fill:
    - persona and role access;
    - market;
    - current behavior (if changing);
    - desired happy path;
    - the 1–2 key rules or edge cases;
    - what must not change;
    - out of scope;
    - Epic;
    - business priority and due date (may stay open).
3. **Sort the answers into three buckets.**
    - Answered → AC.
    - Default accepted → AC.
    - Unknown or skipped → an Open question tagged [Business], [Engineering] or [QA].
4. **Flag a likely split** early if the scope looks over 5 points, as an [Engineering] open question.
5. **Show the full draft** (Summary, Context, ACs, Constraints if any, Open questions) and wait for "create it".
6. **Create it** in To Do, with no Fix Version and no points unless provided.
7. **Fast path:** if the PM says "just draft it", ask nothing and put every gap into Open questions.

### `playbooks/refine-story.md` (new)

Fold new answers (from the PM, comments or the vendor) into the description.

1. Answered questions move from Open questions into ACs or Constraints.
2. Change only what changed.
3. Flag any comment that contradicts the description.
4. After AC approval, add a Changelog line for every AC change.
5. Show a diff before writing.

### `playbooks/split-story.md` (new)

Used when an estimate is over 5 points or the scope spans repos.

1. Propose the split along the seams in `standards/story.md` §2.2.
2. Give one Story per repo for multi-repo work, linked with "blocks".
3. Move each AC to the Story it belongs to.
4. Show the proposed Stories before creating them.
5. Retire the original per `playbooks/cleanup.md`.

### `playbooks/ready-check.md` (new)

1. Run the Ready for Dev checklist from `standards/lifecycle.md`.
2. Output pass/fail per item and exactly what's missing. Example: *"No test cases attached; AC4 has an open question."*

### Other playbooks

- **Update** `review-story.md`, `decompose-initiative.md`, `triage-bug.md`, `intake.md`, `release-readiness.md` and `assess-release-confidence.md`: cut restated rules, link to standards, and align with this brief. `decompose-initiative.md` must produce one Story per repo under the Epic, with no implementation sub-tasks.
- **Create** `release-docs.md` from `docs/radius-monthly-release-task-v2.md` if that file is present in the repo. Replace its classification rules with links to the standards. If the file is absent, create a stub with a TODO.
- **Create** `cleanup.md` for retiring replaced tickets:
    1. resolve as Won't Do;
    2. add an "is replaced by" link;
    3. strip the Fix Version, sprint and assignee;
    4. remove bracket status markers from the Summary.

  Include the MYM-529 cleanup as a worked example:
    - Retire Stories MYM-552 to MYM-555.
    - Retire sub-tasks MYM-547, MYM-583 and MYM-585 to MYM-589, plus the other "Consolidated into…" items under MYM-591.
    - Archive Epic MYM-609.
    - Rename MYM-593 to MYM-597 into the Story format.
    - Keep MYM-551 and MYM-556 to MYM-559.

---

## Phase 5 — Templates

- `templates/story.md`: the §2.1 template with placeholder text.
- `templates/task.md`, `templates/bug.md`: the matching templates.
- `templates/vendor-guide.md`: one page for the MYM vendor. It covers:
    - what the vendor owns (Tasks, estimates, the PR field) and what Mathnasium's PM owns (Summary, ACs, AC approval);
    - how to ask questions (numbered, in comments; the PM folds answers into the description);
    - the 5-point limit;
    - one Story per repo and no implementation sub-tasks;
    - the three-tier rule (implementation ideas go in the PR, not the description).

---

## Phase 6 — `jira/queries.yaml`

Replace `committed_story_bugs` with `committed_work`:

```text
project in (RAD, MYM)
AND issuetype in (Story, Task, Bug)
AND fixVersion is not EMPTY
AND fixVersion not in ("N/A", "FREEZE")
AND statusCategory != Done
ORDER BY fixVersion ASC, priority DESC, key ASC
```

Add:

- `oversized_or_unestimated_committed`: `committed_work` AND (cf[10021] > 5 OR cf[10021] is EMPTY)
- `empty_descriptions`: active Stories, Tasks and Bugs where `description is EMPTY`
- `missing_pr_field`: statuses at Code Review or later AND cf[11279] is EMPTY
- `stories_without_epic`: rename of `orphan_stories`
- `placeholder_fix_versions`: active items with fixVersion in ("N/A", "FREEZE")

Update every reference to the old query name.

---

## Phase 7 — Tools and tests

Update `tools/jira_helper.py`'s audit so it implements the **Checks** tables from the standards:

**Error:**

- empty or near-empty description;
- no numbered AC (Stories);
- Summary not in format (Stories);
- bracket present but not in the repo list, or more than one bracket;
- retired persona;
- Story Points over 5 with a committed Fix Version;
- implementation sub-task on a new Story.

**Warning:**

- market adjective not in the list;
- Pull Requests field empty at Code Review or later;
- AC edit after approval without a Changelog line (detect heuristically: `ac-approved` label present and no Changelog section);
- Story with no Epic;
- unestimated with a Fix Version.

**Suggestion:**

- description over about 2,500 characters;
- implementation detail inside Constraints (a heuristic keyword list: stored procedure, class, controller, service method names).

Keep the existing secret redaction and never echo secrets.

Add tests for each new check. All tests must pass: `python -m unittest discover -s tests -p 'test_*.py'`.

---

## Phase 8 — Plugin and marketplace

Goal: merging to `main` updates the org plugin automatically through Claude's GitHub marketplace sync.

1. **Keep the plugin name `mathnasium-product-lifecycle`** and its skill `write-jira-story`, so it replaces the existing one cleanly.
2. **Layout.** Verify it against the current Claude Code plugin docs before writing:

   ```text
   .claude-plugin/marketplace.json
   plugins/mathnasium-product-lifecycle/
     .claude-plugin/plugin.json
     skills/write-jira-story/
       SKILL.md
       references/   (generated copies of standards/*.md and the story playbooks)
   ```

3. **`tools/build_plugin.py`:**
    - copies the referenced standards and playbooks into `references/`;
    - rewrites repo-relative links to the reference file names;
    - bumps the plugin version in `plugin.json` when content changed;
    - supports `--check`, which exits non-zero if the generated folder is stale.
4. **`SKILL.md`** is hand-written but short. It contains:
    - a description that triggers on "write a story for…", "draft a story", "refine MYM-123", "split this story", "is MYM-123 ready for dev", "review this story";
    - four modes, **write, refine, split and ready check**, each pointing to its playbook in `references/`;
    - ground rules: Jira is live truth, propose before writing, link every Jira key, never copy secrets;
    - one line: "The rules live in `references/story.md`; follow it wherever this file is less specific."

   Do not restate rules in SKILL.md.
5. **Validate** the plugin with `claude plugin validate --strict .` (or the current equivalent command).

---

## Phase 9 — Entry points and cleanup

- **`AGENTS.md`:** a router table of task → files to read. Keep the first principles, the write policy and the hyperlink rule as one-liners that link to their standards. No more than 60 lines.
- **`README.md`:** absorbs `GUIDE.md`, including the repo boundaries (what this repo is and isn't). Add a section **"Updating the standard"**: edit `standards/`, run `python tools/build_plugin.py`, open a PR, and CI checks that the plugin is in sync.
- **`artifacts/README.md`:** it lists templates that don't exist (`integration-contract.md`, `test-strategy.md`, `rollout-plan.md`, `product/problem-definition.md`). Remove those entries; don't invent templates.
- **`ARTIFACT_INDEX.md`:** run `python tools/artifact_index.py --write`.
- **`.github/workflows/validate.yml`:** add `python tools/build_plugin.py --check`.

---

## Phase 10 — Verify and open the PR

1. Confirm all tests pass, `artifact_index.py --check` passes, `build_plugin.py --check` passes, and the plugin validates.
2. Search for leftover old rules and fix every hit outside the "Retired" list and the Checks tables:
    - "Center Admin", "Support Admin" and "Developer" used as allowed personas;
    - "must start with the owning repository";
    - `committed_story_bugs`.
3. Confirm no rule text appears in more than one file. Spot-check the playbooks and AGENTS.md.
4. Delete `docs/revamp-brief.md`.
5. Open the PR titled **"Standard v2: consolidated standards, PM Q&A story writing, self-syncing plugin"**. The body contains:
    - a summary per phase;
    - the list of every `DEFAULT — TBC` item;
    - the post-merge admin steps below.

**Post-merge admin steps** (for the PR body):

1. An org admin opens Organization settings > Plugins & skills > Marketplaces and adds a marketplace synced from this GitHub repo, with automatic sync on.
2. Install the Claude GitHub App on this repository.
3. Remove the old manually installed `mathnasium-product-lifecycle` plugin.
4. Optional but recommended: transfer the repo from `MN-Philippe` to the `mathnasium` GitHub organization.

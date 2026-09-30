# Story Standard

The single source of truth for Jira Stories in RAD and MYM. It applies to every Story, whoever writes it. Playbooks, templates and the plugin link here and never restate these rules.

Items marked `DEFAULT — TBC` are recommended defaults awaiting confirmation.

## Applies to

`DEFAULT — TBC`: effective date **2026-10-01**.

- Stories created **on or after the effective date**.
- Existing active Stories, **the next time they are refined**.
- **Done tickets are never rewritten** to match this standard. Do not mechanically rename or edit historical tickets.

Audit checks honor the effective date: they apply the full rule set to Stories created on or after it, and report older active Stories as informational until refined.

## The Story on one screen

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

The copy-paste version is `templates/story.md`.

- **An empty description is an Error.** The minimum at creation is Context plus at least one AC.
- No comma before "so that".
- ELT must be able to understand the Story from the Summary alone: who, what, why. Avoid vague behaviors ("improve scheduling") and filler outcomes ("so that it works better").

Weak: *As a user, I want better scheduling so that scheduling is easier.*
Strong: *As a Center Director, I want to be warned before an appointment exceeds available instructor capacity so that I can resolve the conflict before confirming the booking.*

## Size

- **Maximum 5 Story Points.** A Story over 5 is split before it enters a sprint (`playbooks/split-story.md`).
- An unestimated Story cannot receive a Fix Version.
- Use the **Story Points** field only. Do not use "Story point estimate". Field IDs are in `standards/jira-conventions.md`.
- Split along seams that keep each piece independently testable: a group of ACs, one persona, one repo, or backend rule vs. UI.
- Why: Stories over 2,500 characters averaged 0.95 Bugs of Story, against 0.16 for short ones.

## Personas

| Persona | Use for |
| --- | --- |
| Center Director (CD) | **Default** for any center-facing Radius work |
| Admin | **Default** for HQ users and HQ-only functions |
| Guardian | **Default** for myMathnasium and the Guardian Portal |
| Franchise Owner (FO) | Only when owner-only permissions or finances matter |
| Assistant Center Director (ACD) | Only when ACD access differs from CD |
| Instructor | Instructional workflows |
| Education Manager | Curriculum work. `DEFAULT — TBC`: kept as a persona |

`DEFAULT — TBC`: Regional Manager is folded into Admin.

FO, CD and ACD may be abbreviated. Pick the full name or the abbreviation and stay consistent within related work.

**Retired, never use:** Center Admin, User, Radius User, Admin User, Center Owner, Support Admin (use Admin), Developer (technical work is a Task; see `standards/task.md`).

**Role access goes in an AC, not the persona.** When several roles get a capability, the Summary uses the default persona and one AC states exactly who has access and who doesn't:

> AC5: Given a user with the ACD, CD, FO or Admin profile, the button is visible; given an Instructor, it is hidden.

Do not write combined personas ("As a Guardian or CD"). If two personas do materially different things, split the Story.

If no real actor can be identified, that is a requirements gap. Raise it as an Open question rather than inventing a persona.

## International markets

The market is an adjective on the persona:

> As a UK Center Director… / As a Canadian Guardian…

- US is the default and is never stated.
- Market list (`DEFAULT — TBC`): Canadian, UK, Australian, Romanian, Mexican, Saudi, Singaporean. Use **International** when the Story applies to every non-US market.
- Also apply one label per market (`DEFAULT — TBC`): `market-CA`, `market-UK`, `market-AU`, `market-RO`, `market-MX`, `market-SA`, `market-SG`, `market-INTL`. These replace the legacy labels Romania, Australia, SaudiArabia and Mexico.
- A market difference in behavior gets its own AC ("Given a Canadian center…").

## Brackets

- A repo bracket is **optional** in both projects. When used, it is the **only** bracket and comes from the repo list in `standards/jira-conventions.md`.
- The repo is always recorded in **Code Dependency** (required by Ready for Dev). A bracket, when present, must match it.
- Not allowed in the Summary:
    - Feature names such as [Calendar 2.0]. The feature is the Epic.
    - [SPIKE] or [PoC]. Use the Spike issue type.
    - [Absorbed…], [Consolidated…] or [Duplicate]. Use a resolution plus an "is replaced by" link (`playbooks/cleanup.md`).
    - [BE] or [FE]. Use the repo name.

## Acceptance criteria and test cases

Lifecycle of a Story's definition:

1. **PM drafts ACs**: numbered AC1, AC2…, in Given / When / Then.
2. **AC approval**: PM, engineering lead (vendor lead for MYM) and QA review in refinement. Requires open questions empty and Story Points set. `DEFAULT — TBC`: recorded by adding the label `ac-approved`.
3. **QA writes test cases within 2 business days**, each mapped to an AC number (TC 3.1 tests AC3). `DEFAULT — TBC`: stored in the Jira **Test plan** field.
4. **Ready for Dev**: the checklist is in `standards/lifecycle.md`.
5. QA in DEV and QA in STG execute those test cases. Results may be posted in comments.

AC writing rules:

- One behavior per AC, with an observable result in the Then.
- Role access and market differences are stated explicitly.
- Existing behavior that must not change is written as a regression AC ("Then the existing cancellation window still applies").
- A mockup supports an AC but doesn't replace it. "Matches the mockup" is never an AC; name the elements that matter.
- If QA can't write a test case for an AC, the AC goes back to the PM.

Example:

```text
AC3: Given a center has no remaining instructor capacity for the selected time,
     When a Center Director attempts to confirm another appointment,
     Then a warning explaining the capacity conflict appears before the appointment is saved.
```

## Requirements, constraints and implementation ideas

| Tier | What it is | Where it lives |
| --- | --- | --- |
| Acceptance criteria | Behavior anyone can observe: UI, API response, data outcome, email | Description (required) |
| Constraint | A rule the solution must obey, stated with its reason: security, contract between repos, compatibility or migration, performance target, data retention, compliance | Description → Constraints |
| Implementation idea | A suggestion for how to build it | A comment marked "non-binding", the PR, or a technical design doc. **Never the description.** |

**The test:** if engineering built it differently and every AC passed, would we reject it? Yes → it's a constraint; write it with the reason. No → it's an implementation idea and stays out of the description.

Good constraint, a cross-repo contract: *"Scheduling accepts max_daily_appointments and max_weekly_appointments; null means inherit the center default."* It defines the interface, not the internals.

Not a constraint: naming which service class or stored procedure to use. That belongs in the PR or the implementing repo's coding standards.

Keep the description to the minimum that changes what must be built, tested, sequenced or decided. State a rule once, at the highest useful level (the Epic), use one term per concept, and leave out stale discussion and PR or progress status.

## Multi-repo work and sub-tasks

- A multi-repo feature is **an Epic with one Story per repo**, each 5 points or less, linked with "blocks" where order matters.
- **Do not use sub-tasks for implementation steps or per-repo splits.**
    - Sub-tasks share the parent's sprint and Fix Version, so they can't be committed separately.
    - Sub-task points don't roll into velocity by default.
    - Release notes have to fold them back together by hand.
- **Bug of Story stays.** It is the one child type, and it rides the parent Story's release path (`standards/bug.md`).
- A step list that engineering or the vendor wants to track goes in the description as a checklist, or in the PR.
- Every Story belongs to an Epic.

## Description vs. comments

- The description is the **only** source of truth for scope and ACs.
- Comments are for questions, discussion and QA evidence.
- When a comment answers a question that changes scope or an AC, the PM updates the description **the same day**, adds a Changelog line if ACs are already approved, and replies "Description updated (AC4)".
- After a Fix Version is set, an AC change also triggers a release-confidence recheck (`standards/ai-release-confidence.md`).

## Pull requests

- Every PR is recorded in the **Pull Requests** field, whoever opens it. Comments may add context but can never be the only record.
- A Story in Code Review or later with an empty Pull Requests field is a Warning.

## The vendor

- This standard applies to every ticket, whoever writes it.
- For MYM, Mathnasium's PM owns the Summary, the ACs and AC approval.
- The vendor owns Tasks, estimates and the Pull Requests field.
- See `templates/vendor-guide.md`.

## Checks

Used by `tools/jira_helper.py`. "Auto" means the helper detects it; other rules are for agent review. All rules respect the effective date in [Applies to](#applies-to).

| Rule | Severity | Auto |
| --- | --- | --- |
| Description empty or near-empty | Error | Yes |
| No numbered AC | Error | Yes |
| Summary not in `As a … I want … so that …` format | Error | Yes |
| Bracket present but not in the repo list, or more than one bracket | Error | Yes |
| Retired persona in the Summary | Error | Yes |
| Story Points over 5 with a committed Fix Version ([committed](jira-conventions.md#fix-versions); `N/A` and `FREEZE` do not count) | Error | Yes |
| Sub-task created on a Story on or after the effective date (Bug of Story is exempt) | Error | Yes |
| Market adjective not in the market list | Warning | Yes |
| Pull Requests field empty at Code Review or later | Warning | Yes |
| AC text changed after the `ac-approved` label was added, with no Changelog line | Warning | Only when the helper receives issue changelog history; otherwise agent review |
| Story with no Epic | Warning | Yes |
| Unestimated with a Fix Version | Warning | Yes |
| Open questions non-empty at AC approval | Warning | No |
| Comment changes scope or an AC but the description was not updated | Warning | No |
| Multi-role access stated in the persona instead of an AC | Warning | No |
| Description over about 2,500 characters | Suggestion | Yes |
| Implementation detail inside Constraints | Suggestion | Yes |

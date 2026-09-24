# Story Quality Standard

This standard defines what a good Jira Story should look like for RAD and MYM.

## Summary format is required

The Jira Story Summary should use the full user-story format:

> **As a [specific actor], I want [clear behavior/capability] so that [clear outcome/value].**

Do not place a comma before `so that`.

### Choose the right Jira level before writing the Story

A repository, pull request, schema change, API contract, migration, cache change, or service-layer change is **not automatically a Story**.

Use a **Story** when the item represents a coherent user/business behavior with observable product acceptance. Use a **Task or Sub-task** when the work is implementation-only and exists to enable a Story, for example schema changes, service plumbing, contract propagation, migrations, caching, refactors, or repository-specific engineering work.

Do not invent a persona simply to keep technical work classified as a Story.

### Multi-repository Epics and projects

A Jira project or Epic may represent one product capability while implementation spans multiple code repositories. **myMathnasium (MYM) is a common example:** a single capability may require coordinated changes in Radius, Scheduling, Guardian Portal, or another implementation repository.

For these multi-repository initiatives:

- keep the Epic/capability centered on the end-to-end business outcome;
- first identify coherent product behaviors, then identify the technical/repository work needed to implement them;
- keep one Story focused on one coherent product behavior;
- use repository-bounded Tasks/Sub-tasks for implementation slices when several repositories contribute to the same Story;
- create separate repository-bounded Stories only when each repository owns a distinct product behavior with its own meaningful acceptance criteria and lifecycle;
- do not combine unrelated repository work merely because it contributes to the same capability;
- when a Story itself is genuinely repository-owned, start its Summary with the owning repository in square brackets, followed by the normal user-story Summary.

Required pattern:

> **[Repo] As a [specific actor], I want [clear behavior/capability] so that [clear outcome/value].**

Examples:

> **[Radius] As a Center Director, I want to configure enrollment booking-limit overrides so that guardian scheduling follows the center's approved limits.**

> **[Scheduling] As a Guardian, I want scheduling eligibility to honor enrollment booking limits so that I cannot create appointments beyond the allowed limits.**

> **[Guardian Portal] As a Guardian, I want unavailable scheduling actions to be blocked in the portal so that the UI matches the scheduling rules enforced by the backend.**

Use the actual implementation repository name represented by the Story. If one product Story spans repositories, keep the Story centered on the behavior and make repository ownership explicit in its child Tasks/Sub-tasks and dependencies rather than forcing one Story per PR.

This is not just formatting. The Summary should be good enough that an ELT member can read it by itself and understand what the Story is about.

### `As a`

Use the real actor who benefits from or performs the behavior when possible.

Follow `standards/personas.md` for the canonical persona vocabulary. Preserve the actual center role when known—for example **Franchise Owner (FO)**, **Center Director (CD)**, or **Assistant Center Director (ACD)**. Common business abbreviations such as FO, CD, and ACD are valid. Do not replace a known role with vague labels such as Center Admin, Radius User, Admin User, Admin, or generic User.

Avoid vague actors such as `user` when a more specific role is known. Market, product surface, and center configuration are normally qualifiers rather than separate personas.

### `I want`

This is the most important clarity test. It must make the actual behavior/capability changing immediately obvious.

Avoid vague phrases such as:

- improve scheduling;
- update reporting;
- support billing changes;
- fix workflow.

State what the person/system should actually be able to do or experience.

### `So that`

State the real outcome or business/user value.

Avoid filler such as:

- so that it works better;
- so that the experience is improved;
- so that the system functions correctly.

If the `I want` and `So that` do not clearly explain the Story to someone outside the delivery team, improve the Summary before treating the Story as ready.

## Example

Weak:

> As a user, I want better scheduling so that scheduling is easier.

Stronger:

> As a Center Director, I want to be warned before an appointment exceeds available instructor capacity so that I can resolve the conflict before confirming the booking.

## Description

Keep the description as the durable product definition, not a dated implementation-status report. PR state, current assignee, temporary progress, and other live delivery state should stay in Jira fields, development links, or comments.

Use the description for the detail that does not belong in the Summary, such as:

- business context;
- current behavior;
- desired behavior;
- business rules;
- important scenarios and exceptions;
- references/evidence;
- implementation constraints when they are truly requirements;
- authority/source-of-truth boundaries;
- cross-system contract semantics such as required inputs, null/default/inheritance behavior, validation ownership, and logic that must not be duplicated;
- important existing behavior that must be preserved;
- explicit out-of-scope behavior and unresolved decisions.

Do not bury the core purpose of the Story in the description. The Summary should already make the Story understandable.

## Acceptance criteria

Acceptance criteria are required for Product Complete.

They should be:

- specific;
- observable;
- testable;
- complete enough that QA and Engineering do not have to guess intended behavior;
- consistent with the approved business requirement.

Prefer **Given / When / Then** when it makes the behavior clearer, especially for rules, branching behavior, permissions, state transitions, and edge cases.

Example:

```text
Given a center has no remaining instructor capacity for the selected time
When a Center Director attempts to confirm another appointment
Then the user is warned before the appointment is saved
And the warning clearly explains the capacity conflict
```

Clear bullet-point acceptance criteria are acceptable when Given / When / Then would add ceremony without clarity.

Acceptance criteria should describe product-observable behavior. Do not turn them into a code-design checklist unless the technical constraint is required for correctness, security, compatibility, or operations.

For Tasks/Sub-tasks, prefer **Done when** or **Completion criteria** rather than manufacturing user-facing acceptance criteria.

## Product Complete

A Story is Product Complete when:

- the approved business requirement is represented accurately;
- the Summary clearly communicates who / what / why;
- acceptance criteria define the intended product behavior;
- QA test cases / validation coverage are defined;
- Product and QA agree the Story is sufficiently precise and testable.

If detailed acceptance criteria expose a material change to the previously approved business requirement, route that change back to the business for approval.

## Engineering review

Engineering review is conditional, not a default gate.

Flag the Story for Engineering review when architecture, permissions, integrations, data, security, performance, deployment, feasibility, or another technical concern deserves explicit review before development.

## Scope changes after commitment

If requirements or acceptance criteria materially change after a Fix Version has been assigned, make the change visible and reassess delivery impact.

Do not assume every scope change increases release risk. Scope change is evidence to evaluate in context, not an automatic downgrade.

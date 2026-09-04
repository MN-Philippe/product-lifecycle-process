# Story Quality Standard

This standard defines what a good Jira Story should look like for RAD and MYM.

## Summary format is required

The Jira Story Summary should use the full user-story format:

> **As a [specific actor], I want [clear behavior/capability], so that [clear outcome/value].**

This is not just formatting. The Summary should be good enough that an ELT member can read it by itself and understand what the Story is about.

### `As a`

Use the real actor who benefits from or performs the behavior when possible.

Avoid vague actors such as `user` when a more specific role is known.

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

> As a user, I want better scheduling, so that scheduling is easier.

Stronger:

> As a Center Director, I want to be warned before an appointment exceeds available instructor capacity, so that I can resolve the conflict before confirming the booking.

## Description

Use the description for the detail that does not belong in the Summary, such as:

- business context;
- current behavior;
- desired behavior;
- business rules;
- important scenarios and exceptions;
- references/evidence;
- implementation constraints when they are truly requirements.

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

# Persona Standard

This standard defines the canonical actor vocabulary for Jira Stories across RAD and MYM.

The goal is consistency without erasing meaningful role differences. Use the smallest stable set of personas that accurately represents who performs or benefits from the behavior.

## Core product personas

### Guardian

Use **Guardian** for a parent/guardian using myMathnasium, Guardian Portal, or other guardian self-service experiences.

Do not create separate personas such as `Canadian Guardian` or `Australian Guardian` merely for localization. Market/country is normally a qualifier of the behavior, not a different persona.

Example:

> As a Guardian, I want Canadian address labels to use the correct terminology so that my profile reflects my local format.

### Center Director

Use **Center Director** for normal center-level operational and administrative work in Radius or related center tools.

This is the canonical replacement for overlapping labels such as:

- Center Admin;
- Radius User;
- Admin User;
- Admin;
- CD;
- generic User, when the real actor is center staff performing center operations.

Use another persona instead when the requirement genuinely depends on a different role's permissions, responsibilities, or goals.

### Center Owner

Use **Center Owner** when ownership-specific concerns materially matter, such as owner-level permissions, financial responsibility, organization access, or owner-only controls.

Do not collapse Center Owner into Center Director when the distinction affects behavior or authorization.

### Instructor

Use **Instructor** for instructional-session workflows, DWP/session execution, instructional notes, or other behavior performed specifically by instructional staff.

### Education Manager

Use **Education Manager** when curriculum/education-management responsibilities materially distinguish the actor from a Center Director.

### Support Admin

Use **Support Admin** for internal support-only capabilities or elevated support permissions.

If a more specific corporate/support role is required because its permissions or outcome materially differ, use that named role rather than forcing it into Support Admin.

### Regional Manager

Use **Regional Manager** for region-level workflows or permissions that span multiple centers and are specifically tied to regional responsibility.

## Technical and operational actors

### Developer

Use **Developer** only when the developer is genuinely the user/beneficiary of the capability, such as developer tooling, diagnostics, CI/CD, migration tooling, or engineering support workflows.

Do not use Developer merely because Engineering is implementing the Story. If the change exists to deliver user/business behavior, use the actual product persona.

If the work is purely technical with no meaningful user-facing actor or outcome, consider whether the Jira item should be a Task rather than forcing it into a Story.

### Release Engineer / operational roles

Use a specific operational role such as **Release Engineer** only when that person directly performs the behavior being delivered.

### System/service actors

A system or service is not a product persona.

Prefer a Task for pure system-internal implementation. If an existing Story genuinely describes autonomous system behavior and retaining it as a Story is useful, identify the concrete service explicitly rather than using a vague actor such as `system`.

## Qualifiers are not personas

Do not create separate personas just because the same actor is in a different market, product surface, or center configuration.

Common qualifiers include:

- country/market: Canadian, Australian, UK, US, international;
- product surface: Radius, myMathnasium, Guardian Portal;
- center configuration: Drop-In, Hybrid, Virtual Center, centralized/non-centralized;
- implementation repository.

Put qualifiers in the behavior, description, acceptance criteria, or repository prefix as appropriate.

Examples:

Instead of:

> As a Canadian User, I want...

Prefer:

> As a Center Director, I want Canadian tax behavior...

or:

> As a Guardian, I want Canadian address labels...

Instead of:

> As a Radius User, I want...

Prefer the actual role:

> As a Center Director, I want...

## Avoid combined personas

Avoid summaries such as:

> As a Guardian or Center Director...

If the two personas perform materially different actions or have different permissions, split the work or choose the correct persona for each Story.

If the same underlying behavior serves both personas identically and splitting adds no delivery value, use the persona most directly affected by the Story and cover the other actor in the description/acceptance criteria.

## Generic actor rule

Avoid:

- User;
- Admin;
- Admin User;
- Radius User;
- CD;
- vague role abbreviations.

When reviewing an existing Story, infer the real actor from the behavior, permissions, UI surface, and acceptance criteria before rewriting the Summary.

Do not invent a persona merely to satisfy formatting. If the actor is genuinely unclear, treat that as a requirements gap.

## Applying this standard

Apply this standard to:

- new Stories;
- active Stories being materially revised;
- Stories being decomposed from Epics/initiatives;
- Stories whose persona is being reviewed for clarity.

Do not create noise by mechanically rewriting completed historical tickets solely to normalize terminology.

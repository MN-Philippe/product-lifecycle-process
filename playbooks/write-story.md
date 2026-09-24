# Playbook: Write a Story

## Goal

Create Jira work at the right level of abstraction so Product, Engineering, QA, and ELT can understand the outcome without forcing technical implementation work into fake user Stories.

Read:

- `standards/story-quality.md`
- `standards/personas.md`
- the parent Epic/capability and relevant related work live from Jira

## Steps

1. **Start with the product behavior, not the repository.**
   - State the user/business behavior or outcome that must change.
   - Identify the real persona who performs or benefits from that behavior.
   - Confirm the Story can be tested as product behavior rather than merely as code completion.

2. **Choose the Jira issue type before writing the Summary.**
   - Use a **Story** for a coherent user/business behavior with observable product acceptance.
   - Use a **Task** or **Sub-task** for implementation-only work such as schema changes, service plumbing, contract propagation, migrations, caching, refactors, or repository-specific engineering work that exists only to enable a Story.
   - Do not invent a persona to keep technical work classified as a Story.
   - A repository or PR boundary is not automatically a Story boundary.

3. **Choose the boundary.**
   - Keep one Story focused on one coherent product behavior.
   - If several repositories implement that behavior, keep the product behavior at the Story level and split repository-specific execution into Tasks/Sub-tasks when practical.
   - Create separate repository-bounded Stories only when each repository owns a distinct product behavior that has its own meaningful acceptance criteria and lifecycle.
   - If a technical enabler supports several Stories, consider a Task under the Epic rather than duplicating it under each Story.

4. **Write the Summary.**
   For a Story:

   > **As a [specific actor], I want [clear behavior/capability] so that [clear outcome/value].**

   Do not place a comma before `so that`.

   If the Story itself is genuinely repository-owned in a multi-repository initiative, prefix it:

   > **[Repo] As a [specific actor], I want [clear behavior/capability] so that [clear outcome/value].**

   For a Task/Sub-task, use an action-oriented implementation Summary such as:

   > **[Scheduling] Persist Pod identity on appointments and validate center ownership.**

5. **Write only the durable definition in the description.**
   Prefer these sections when useful:

   - **Context / Goal**
   - **Scope**
   - **Business rules / invariants**
   - **Acceptance criteria**
   - **Out of scope**
   - **Dependencies**
   - **Open decisions**
   - **Technical constraints**, only when they are real requirements

   Do not turn the description into a dated status report. PR state, current assignee, temporary implementation progress, and other live delivery state belong in Jira fields, development links, or comments.

6. **Make authority and contracts explicit for cross-system work.**
   Identify, when relevant:

   - which system owns the rule or source of truth;
   - which system is the trust/validation boundary;
   - the minimum inputs and outputs that cross repositories;
   - null/default/inheritance semantics;
   - what downstream systems must validate rather than trust;
   - what logic must not be duplicated;
   - backward/mixed-deployment expectations.

   Put end-to-end rules at the highest useful level, then give each implementation item only the local contract it needs.

7. **Write acceptance criteria at the product boundary.**
   - Make them observable and testable.
   - Cover happy path, important branches, permissions, edge cases, and regression behavior.
   - Prefer Given / When / Then when branching or state transitions benefit from it.
   - Do not use acceptance criteria as a code-design checklist unless the technical constraint is itself required for correctness, security, compatibility, or operations.

   For Tasks/Sub-tasks, use **Done when** or **Completion criteria** instead of fake user-facing acceptance criteria.

8. **Make dependencies real.**
   - Link actual blockers in Jira at the level where Engineering experiences them.
   - Distinguish a true blocker from an integration gate. Work that can proceed against a frozen contract should not be marked blocked merely because another implementation is not merged yet.
   - If a hard deadline exists, derive a small number of execution waves from the dependency graph after the work is decomposed.

9. **Keep decomposition lean.**
   - Split work when it creates a useful ownership, review, testing, or sequencing boundary.
   - Do not create tickets merely to make every item tiny.
   - For implementation Tasks/Sub-tasks, roughly 3-5 points is often a useful execution size, but this is a heuristic, not a rule.
   - Combine coherent same-owner work when splitting it would create 1-point ticket noise without reducing delivery risk.

10. **Resolve requirement decisions into the description.**
    - Comments may contain investigation, discussion, or implementation guidance.
    - When a comment establishes a requirement or contract, fold the durable decision into the description.
    - Mark obsolete guidance as superseded so developers do not have to reconstruct which comment is authoritative.

11. **Clean up replaced work.**
    - When an oversized Story is replaced by an Epic/decomposition, keep the old issue only as historical/source context.
    - Do not leave it as an active execution child with release/sprint/assignee metadata if it is no longer meant to be delivered.
    - Link it to the replacement/decomposition rather than duplicating both definitions.

## Final self-check

Before calling a Story ready, verify:

- Is this actually a Story rather than technical work?
- Can ELT understand who / what / why from the Summary alone?
- Is the real persona used?
- Is the Story boundary a product boundary rather than just a repo/PR boundary?
- Are authority, trust, and cross-repository contracts clear where relevant?
- Are acceptance criteria observable and testable?
- Are important existing behaviors explicitly preserved?
- Are material open decisions resolved or clearly visible?
- Are blockers linked at the actual execution level?
- Is transient implementation status kept out of the durable definition?

# Playbook: Write a Story

## Goal

Create Jira Stories that are cohesive, reviewable delivery units with clear repository ownership, while adding lower-level sequencing only when it materially helps execution.

Read:

- `standards/story-quality.md`
- `standards/personas.md`
- the parent Epic/capability and relevant related work live from Jira

## Steps

1. **Start with the outcome and implementation ownership.**
   - State the user/business behavior or outcome that must change.
   - Identify the real persona who performs or benefits from that behavior.
   - Identify the implementation repository that owns the unit of work.

2. **Choose a cohesive Story boundary.**
   - A Story should generally stay within one implementation repository.
   - Keep together work that forms one understandable, implementable, reviewable, testable unit.
   - Split a repository's work into multiple Stories when there are multiple coherent units that would be easier to implement or review independently.
   - A pull request may map naturally to a Story, but do not force the boundary solely because a PR exists.
   - A cross-repository Story should be exceptional; prefer separate Stories with explicit dependencies.

3. **Do not add lower-level hierarchy by default.**
   - A cohesive Story should normally be enough to drive implementation.
   - Do not create Tasks/Sub-tasks merely to enumerate implementation steps.
   - Add Tasks/Sub-tasks when they have a clear execution purpose: sequencing, parallel ownership, or separately tracked work needed to meet a compressed or otherwise constrained plan.
   - When there is no meaningful parallelism or sequencing benefit, keep the work in the Story.

4. **Write the Summary.**
   For a Story:

   > **As a [specific actor], I want [clear behavior/capability] so that [clear outcome/value].**

   Do not place a comma before `so that`.

   For implementation Stories in a multi-repository initiative, prefix it with the owning repository:

   > **[Repo] As a [specific actor], I want [clear behavior/capability] so that [clear outcome/value].**

   When a Task/Sub-task is justified by execution sequencing, use an action-oriented implementation Summary such as:

   > **[Scheduling] Persist Pod identity on appointments and validate center ownership.**

5. **Write the minimum sufficient durable definition.**
   Include enough detail to remove meaningful ambiguity, but no more. Prefer these sections when useful:

   - **Context / Goal**
   - **Scope**
   - **Business rules / invariants**
   - **Acceptance criteria**
   - **Out of scope**
   - **Dependencies**
   - **Open decisions**
   - **Technical constraints**, only when they are real requirements

   Do not turn the description into a dated status report. PR state, current assignee, temporary implementation progress, and other live delivery state belong in Jira fields, development links, or comments.

   Then do a simplification pass:
   - remove duplicated rules already stated at the Epic or another authoritative parent;
   - remove examples that do not clarify a genuine edge case;
   - remove speculative implementation suggestions that are not requirements;
   - replace multiple terms for the same concept with one canonical term;
   - remove prose that merely restates the Summary, Scope, or acceptance criteria;
   - preserve only details that change what must be built, tested, sequenced, or decided.

6. **Make authority and contracts explicit for cross-system work.**
   Identify, when relevant:

   - which system owns the rule or source of truth;
   - which system is the trust/validation boundary;
   - the minimum inputs and outputs that cross repositories;
   - null/default/inheritance semantics;
   - what downstream systems must validate rather than trust;
   - what logic must not be duplicated;
   - backward/mixed-deployment expectations.

   Put end-to-end rules at the highest useful level, then give each repository-bounded Story only the local contract it needs.

7. **Write acceptance criteria at the product boundary.**
   - Make them observable and testable.
   - Cover the happy path and only the important branches, permissions, edge cases, and regression behavior needed to remove ambiguity.
   - Do not enumerate every logically implied variation once a broader rule makes the expected behavior clear.
   - Prefer Given / When / Then when branching or state transitions benefit from it.
   - Do not use acceptance criteria as a code-design checklist unless the technical constraint is itself required for correctness, security, compatibility, or operations.

   For Tasks/Sub-tasks, use **Done when** or **Completion criteria** instead of fake user-facing acceptance criteria.

8. **Make dependencies real.**
   - Link actual blockers between Stories where Engineering experiences them.
   - Distinguish a true blocker from an integration gate. Work that can proceed against a frozen contract should not be marked blocked merely because another implementation is not merged yet.
   - Introduce Tasks/Sub-tasks and execution waves only when the plan genuinely benefits from parallel tracks or explicit sequencing.

9. **Keep decomposition lean.**
   - Prefer smaller cohesive Stories over large repository Stories that contain several independently reviewable changes.
   - Do not create tickets merely to make every item tiny.
   - Do not create Tasks/Sub-tasks merely because a Story contains several implementation steps.
   - Use lower-level items when they unlock meaningful parallel work or clarify critical sequencing.

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

- Is this one cohesive unit of work?
- Is it generally limited to one implementation repository?
- Would splitting it further materially improve implementation or review?
- Can ELT understand who / what / why from the Summary alone?
- Is the real persona used?
- Are Tasks/Sub-tasks present only because sequencing or parallel execution genuinely benefits from them?
- Are authority, trust, and cross-repository contracts clear where relevant?
- Are acceptance criteria observable and testable?
- Are important existing behaviors explicitly preserved?
- Are material open decisions resolved or clearly visible?
- Are blockers linked at the actual execution level?
- Is transient implementation status kept out of the durable definition?
- Can anything be removed without changing what must be built, tested, sequenced, or decided?
- Is each domain concept described with one clear, consistent term?

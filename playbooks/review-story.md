# Playbook: Review a Story

## Goal

Make the Story understandable at an ELT glance, aligned to the approved business intent, testable by QA, and ready to move through the normal product lifecycle.

Read `standards/story-quality.md` first.

## Steps

1. Fetch the Story live.
2. Fetch its parent/related context when useful to understand the intended outcome.
3. Check that the Story is one cohesive, generally single-repository unit of work. If it spans repositories or contains multiple independently reviewable units, recommend splitting it into Stories.
4. Check the Summary against the required format:
   - `As a [specific actor], I want [clear behavior/capability] so that [clear outcome/value]`
   - do not place a comma before `so that`.
5. Apply the ELT test: can someone understand who / what / why from the Summary alone?
6. Check whether the Story is small enough to implement and review coherently without unnecessary internal decomposition.
7. Check whether the description captures durable business context/rules/scenarios, authority/source-of-truth boundaries, important invariants, out-of-scope behavior, and cross-system contract semantics when relevant. Flag transient PR/progress status embedded in the durable definition.
8. Evaluate acceptance criteria for specificity, observability, and testability. Prefer Given / When / Then when it improves clarity. Flag code-design checklists masquerading as product acceptance criteria.
9. Check whether comments contain requirement decisions that should be folded into the description and whether obsolete guidance is clearly superseded.
10. If the Story has Tasks/Sub-tasks, verify they exist for a real sequencing or parallel-execution need rather than simply restating implementation steps.
11. Check real blockers between Stories and distinguish them from integration gates.
12. Determine whether Product Complete is supportable: Product definition is precise and QA test coverage is defined.
13. Flag Engineering review only when technical uncertainty/complexity warrants it; do not invent a universal technical gate.
14. Look for duplicate work, hidden dependencies, or material scope changes after commitment.
15. If a Fix Version exists, treat it as the delivery commitment. Material scope changes are risk evidence to assess, not automatic confidence downgrades.
16. Inspect code or durable artifacts when technical truth matters.
17. Recommend the smallest useful improvement.

## Output

- **Summary quality / ELT readability**
- **Business intent clarity**
- **Acceptance criteria**
- **Product Complete gaps**
- **Engineering review needed?**
- **Dependencies / scope-change concerns**
- **Proposed Jira wording/changes**, if needed

Do not weaken the required Story Summary format. Do not add ceremony that does not improve clarity or delivery quality.

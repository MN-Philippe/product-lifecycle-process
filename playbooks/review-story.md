# Playbook: Review a Story

## Goal

Make the Story understandable at an ELT glance, aligned to the approved business intent, testable by QA, and ready to move through the normal product lifecycle.

Read `standards/story-quality.md` first.

## Steps

1. Fetch the Story live.
2. Fetch its parent/related context when useful to understand the intended outcome.
3. First verify that the issue is actually a Story. If it is implementation-only work with no independent product behavior, recommend Task/Sub-task rather than inventing a persona.
4. Check the Summary against the required format:
   - `As a [specific actor], I want [clear behavior/capability] so that [clear outcome/value]`
   - do not place a comma before `so that`.
5. Apply the ELT test: can someone understand who / what / why from the Summary alone?
6. Check whether the Story boundary represents coherent product behavior rather than merely a repository, PR, schema, or service boundary.
7. Check whether the description captures durable business context/rules/scenarios, authority/source-of-truth boundaries, important invariants, out-of-scope behavior, and cross-system contract semantics when relevant. Flag transient PR/progress status embedded in the durable definition.
8. Evaluate acceptance criteria for specificity, observability, and testability. Prefer Given / When / Then when it improves clarity. Flag code-design checklists masquerading as product acceptance criteria.
9. Check whether comments contain requirement decisions that should be folded into the description and whether obsolete guidance is clearly superseded.
10. Check real blockers at the implementation level and distinguish them from integration gates.
11. Determine whether Product Complete is supportable: Product definition is precise and QA test coverage is defined.
12. Flag Engineering review only when technical uncertainty/complexity warrants it; do not invent a universal technical gate.
13. Look for duplicate work, hidden dependencies, or material scope changes after commitment.
14. If a Fix Version exists, treat it as the delivery commitment. Material scope changes are risk evidence to assess, not automatic confidence downgrades.
15. Inspect code or durable artifacts when technical truth matters.
16. Recommend the smallest useful improvement.

## Output

- **Summary quality / ELT readability**
- **Business intent clarity**
- **Acceptance criteria**
- **Product Complete gaps**
- **Engineering review needed?**
- **Dependencies / scope-change concerns**
- **Proposed Jira wording/changes**, if needed

Do not weaken the required Story Summary format. Do not add ceremony that does not improve clarity or delivery quality.

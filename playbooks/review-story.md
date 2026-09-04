# Playbook: Review a Story

## Goal

Make the Story understandable at an ELT glance, aligned to the approved business intent, testable by QA, and ready to move through the normal product lifecycle.

Read `standards/story-quality.md` first.

## Steps

1. Fetch the Story live.
2. Fetch its parent/related context when useful to understand the intended outcome.
3. Check the Summary against the required format:
   - `As a [specific actor]`
   - `I want [clear behavior/capability]`
   - `so that [clear outcome/value]`
4. Apply the ELT test: can someone understand who / what / why from the Summary alone?
5. Check whether the description captures the business context/rules/scenarios that do not fit in the Summary.
6. Evaluate acceptance criteria for specificity, observability, and testability. Prefer Given / When / Then when it improves clarity.
7. Determine whether Product Complete is supportable: Product definition is precise and QA test coverage is defined.
8. Flag Engineering review only when technical uncertainty/complexity warrants it; do not invent a universal technical gate.
9. Look for duplicate work, hidden dependencies, or material scope changes after commitment.
10. If a Fix Version exists, treat it as the delivery commitment. Material scope changes are risk evidence to assess, not automatic confidence downgrades.
11. Inspect code or durable artifacts when technical truth matters.
12. Recommend the smallest useful improvement.

## Output

- **Summary quality / ELT readability**
- **Business intent clarity**
- **Acceptance criteria**
- **Product Complete gaps**
- **Engineering review needed?**
- **Dependencies / scope-change concerns**
- **Proposed Jira wording/changes**, if needed

Do not weaken the required Story Summary format. Do not add ceremony that does not improve clarity or delivery quality.

# Playbook: Review a Story or Task

## Goal

Make the work understandable, appropriately scoped, testable, and connected to the right outcome without forcing unnecessary template language.

## Steps

1. Fetch the issue live.
2. Fetch its parent when present and enough sibling context to understand the intended outcome.
3. Decide whether the work is primarily product behavior, engineering work, or a Spike-like investigation.
4. Evaluate it using the corresponding rules in `jira/quality-rules.md`.
5. Check whether acceptance/completion criteria are observable and sufficient for QA/engineering.
6. Look for accidental duplication, hidden dependencies, or an obviously wrong/missing parent.
7. Inspect code or durable artifacts when the issue cannot be evaluated accurately from Jira alone.
8. Recommend the smallest useful improvement.

## Output

- **Work type**
- **Clarity**
- **Completion criteria**
- **Parent/context fit**
- **Risks or missing information**
- **Proposed Jira wording/changes**, if needed

Do not rewrite clear tickets just to make them conform to a stylistic template.

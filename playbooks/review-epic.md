# Playbook: Review an Epic

## Goal

Determine whether an Epic is a useful representation of a bounded outcome, whether its child work supports that outcome, and what should be improved.

## Steps

1. Fetch the Epic live from Jira.
2. Fetch its direct children live.
3. Classify the Epic as finite initiative, persistent capability/work bucket, or unclear/misclassified.
4. For finite initiatives, evaluate problem, outcome, scope, success, ownership, dependencies, and decomposition using `jira/quality-rules.md`.
5. Inspect child Stories/Tasks/Bugs for coverage, overlap, missing work, and inconsistent lifecycle state.
6. Inspect relevant code/artifacts only when technical truth is needed.
7. Check for an initiative workspace in `initiatives/`; if one exists, use its durable decisions but do not trust it for live Jira state.
8. Report errors, warnings, suggestions, missing decisions, and a concise proposed improvement plan.

## Output

Prefer:

- **Classification**
- **Outcome / intent**
- **What is strong**
- **Gaps**
- **Hierarchy / decomposition concerns**
- **Risks / missing decisions**
- **Recommended Jira changes**
- **Recommended durable artifacts**, only if genuinely useful

Do not write changes unless authorized.

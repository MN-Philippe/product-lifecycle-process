# Playbook: Triage a Bug

Read: [`standards/bug.md`](../standards/bug.md)

## Steps

1. Fetch the report live, with comments, parent Story, prior requirements and related work.
2. Classify it (`standards/bug.md`, section 2) before prescribing a fix.
3. Trace a true defect to the Story, requirement or release it violates.
4. Fill the required description content (`standards/bug.md`, section 5). Ask for what is missing.
5. Search Jira for duplicates. Inspect implementation repos when technical context materially helps.
6. With Dev + QA + PM, assess fix scope and regression risk (`standards/bug.md`, section 6).
7. If found during a Story, decide Bug of Story vs. standalone.
8. For a standalone Bug, identify the impacted product area and associate it there. Recommend moving any Bug found under a generic Bug Fixing Epic when the area is clear.
9. Recommend prioritization treatment (`standards/bug.md`, section 7). If a Fix Version is assigned, it is a delivery commitment.
10. Flag secret-like content without repeating it.

## Output

- Classification and traceability
- Observed vs. expected; repro confidence
- Impact and affected scope
- Product area / feature categorization
- Fix scope and regression concerns; QA verification
- Bug of Story vs. standalone
- Prioritization recommendation and Jira changes

# Playbook: Assess AI Release Confidence

Read: [`standards/ai-release-confidence.md`](../standards/ai-release-confidence.md), [`standards/jira-conventions.md`](../standards/jira-conventions.md)

Blocked until the write-field TODO in the standard is resolved.

## Steps

1. Fetch scope with `committed_work` from `jira/queries.yaml`.
2. For each item, fetch current context: status, Story Points, Pull Requests and Development fields, child Bugs, "blocks" links, labels, and description.
3. Read the Jira changelog for Fix Version, AC and AI-field changes, and the current Feedback field.
4. Gather the signals in the standard, weighted by time remaining to the real cutoff on the release calendar.
5. Decide On Track, Watch or At Risk using the definitions in the standard.
6. Draft a short Reason naming only the strongest signals.
7. Compare with current Jira values. Write only when Confidence or the material Reason changed. Never edit Feedback.

## Output / write set

Only the AI-owned fields named in the standard. Nothing else is owned by this automation.

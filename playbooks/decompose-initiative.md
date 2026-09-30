# Playbook: Decompose an Initiative

Read: [`standards/story.md`](../standards/story.md), [`standards/task.md`](../standards/task.md), [`standards/jira-conventions.md`](../standards/jira-conventions.md)

Break a bounded outcome into delivery work without losing business intent.

## Steps

1. Fetch the Epic live and inspect current children.
2. Confirm problem, outcome, scope, constraints, non-scope, business priority and due date when available.
3. Identify every implementation repo touched. Do not infer repos from the Jira key.
4. Produce **one Story per repo under the Epic**, each 5 points or less, linked with "blocks" where order matters. Split further where `standards/story.md#size` applies. **Do not propose implementation sub-tasks.**
5. Use a Task (`standards/task.md`) for technical work with no observable behavior.
6. State cross-repo contracts, source of truth and trust boundaries at the Epic level; give each Story only the local contract it needs (`standards/story.md#requirements-constraints-and-implementation-ideas`).
7. Separate real blockers from integration gates. Work that can proceed against a frozen contract is not blocked.
8. Run a simplification pass: shared rules at the Epic, one term per concept, no duplicated detail in children.
9. Recommend conditional Engineering review (`standards/lifecycle.md`) and durable artifacts (`artifacts/README.md`) only where warranted.

## Output

- Outcome and scope recap
- Proposed Epic → Story breakdown, with Summaries in the standard format
- Dependencies and sequencing
- Engineering-review candidates
- Open decisions
- Recommended Jira changes and artifacts, if any

Do not create Jira work unless authorized.

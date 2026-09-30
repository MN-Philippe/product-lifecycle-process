# Playbook: Decompose an Initiative

Read: [`standards/story.md`](../standards/story.md), [`standards/task.md`](../standards/task.md), [`standards/jira-conventions.md`](../standards/jira-conventions.md)

Break a bounded outcome into delivery work without losing business intent.

## Steps

1. Fetch the Epic live and inspect current children.
2. Confirm problem, outcome, scope, constraints, non-scope, business priority and due date when available.
3. Inventory the **independently testable behaviors** before deciding ticket boundaries. Look for meaningful user actions/inputs and system responses/outcomes: buttons or menu actions, tabs with distinct behavior, sorting/filtering, form submission, create/edit/delete actions, validations, authorization results, API/data outcomes and asynchronous responses.
4. Treat each independent behavior as a Story candidate, but do not fragment mechanically. Keep closely coupled behavior together when it serves one coherent outcome and has no useful independent acceptance, ownership, sequencing or release value. Decomposition is a refinement tool, not a reason to block an otherwise coherent Story.
5. Identify every implementation repo touched. Do not infer repos from the Jira key. Map each proposed Story to one repo, recorded in the Code Dependency field; when a behavior spans repos, propose the necessary repo-specific **Jira** Stories. A repo may have multiple Stories for the initiative. A "repo" here never means acting on GitHub.
6. Keep each Story at 5 points or less. Never move production implementation into sub-tasks to make a Story look smaller.
7. Use delivery-workflow sub-tasks only where separate tracking adds value: QA automation, test setup/data, pre/post-deployment steps, release/runbook work or coordination. QA automation code is allowed; production implementation code is not.
8. Use a Task (`standards/task.md`) for standalone technical/operational work that does not introduce product/system behavior and is not merely workflow for a specific Story.
9. State cross-repo contracts, source of truth and trust boundaries at the Epic level; give each Story only the local contract it needs (`standards/story.md#requirements-constraints-and-implementation-ideas`).
10. Separate real blockers from integration gates. Work that can proceed against a frozen contract is not blocked.
11. Run a simplification pass: shared rules at the Epic, one term per concept, no duplicated detail in children.
12. Recommend conditional Engineering review (`standards/lifecycle.md`) and durable artifacts (`artifacts/README.md`) only where warranted.

## Output

- Outcome and scope recap
- Proposed Epic → Story breakdown, with the behavior boundary and Summary for each Story
- Dependencies and sequencing
- Engineering-review candidates
- Open decisions
- Recommended Jira changes and artifacts, if any

Propose only. Jira writes follow the write policy in `standards/jira-conventions.md#write-policy`; GitHub is read-only.

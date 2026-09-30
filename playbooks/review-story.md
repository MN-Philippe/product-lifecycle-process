# Playbook: Review a Story

Read: [`standards/story.md`](../standards/story.md)

Audit an existing Story against the standard. To fix a Story rather than audit it, use `playbooks/refine-story.md`; to check readiness only, use `playbooks/ready-check.md`.

## Steps

1. Fetch the Story live, with its parent and related context.
2. Check the effective date in `standards/story.md#applies-to`. For Stories created before it, review for information only.
3. Walk the Checks table in `standards/story.md`, plus the ELT test on the Summary.
4. Check the description for stale content: comments that contradict it, superseded guidance, duplicated rules, implementation ideas outside a comment or PR.
5. Check the behavior boundary, size and repo scope. Recommend `playbooks/split-story.md` when the Story bundles independently testable actions/responses, crosses repos or exceeds 5 points. Do not fail a coherent Story merely because a screen contains several tightly coupled controls; decomposition requires judgment.
6. Recommend the smallest useful improvement.

## Output

- Summary quality / ELT readability
- Acceptance criteria and test-case coverage
- Findings by severity (Error / Warning / Suggestion)
- Proposed wording or Jira changes, if needed

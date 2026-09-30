# Playbook: Release Readiness

Read: [`standards/lifecycle.md`](../standards/lifecycle.md), [`standards/jira-conventions.md`](../standards/jira-conventions.md)

## Steps

1. Fetch the release scope live with `release_scope` from `jira/queries.yaml`. Take the release date from the Jira version record.
2. Read changelog history when commitment changes matter. Do not rely on Epic status.
3. Inspect statuses, blockers, open Bugs of Story, overdue work, late AC changes, and remaining pipeline stages.
4. Inspect PRs and repos when deployment readiness matters.
5. Check QA in DEV evidence, then STG evidence (regression, integration, targeted validation).
6. Check rollout, migration/data, monitoring, rollback and business-readiness concerns when relevant.
7. Separate must-resolve blockers from acceptable risks and follow-ups.
8. Confirm QA has declared Ready for Release. Surface the Business + PM release decision still required.

## Output

- Scope summary
- Ready / Watch / At risk / Blocked
- QA readiness; operational concerns
- Business/PM decisions required; recommended actions

Item-level confidence is defined in `standards/ai-release-confidence.md`; do not invent release rollups.

# Playbook: Release Readiness

## Goal

Evaluate whether a planned release is ready to ship by combining live Jira scope with delivery, QA, dependency, and operational context.

## Steps

1. Fetch the live release scope from Jira by project/fix version.
2. Group work by initiative/outcome and identify standalone items.
3. Inspect current statuses, blockers, unresolved Bugs, overdue work, and scope that lacks clear ownership or context.
4. Check whether parent initiatives meaningfully represent the release work; do not rely on Epic status alone.
5. Inspect relevant PRs/code/repositories when implementation or deployment readiness matters.
6. Check test/QA evidence, rollout concerns, migration/data concerns, observability/monitoring, and rollback/operational readiness where applicable.
7. Separate must-resolve blockers from acceptable risks and post-release follow-ups.
8. Produce a concise go/no-go view with explicit decisions needed.

## Output

- **Release scope summary**
- **Ready**
- **At risk**
- **Blocked**
- **Operational / rollout concerns**
- **Decisions required**
- **Recommended actions and owners**

Do not equate ticket status with readiness. Readiness is an evidence-based assessment across the actual delivery path.

# Playbook: Release Readiness

## Goal

Evaluate whether a planned release is ready to ship by combining live Jira scope with delivery, QA, dependency, and operational context while respecting the agreed ownership model.

Read `standards/product-lifecycle.md` first.

## Normal pipeline

**Development -> Code Review -> QA in DEV -> Release Branch -> STG -> QA in STG -> Ready for Release -> Release**

QA owns the **Ready for Release** gate. Business + PM own the decision to release after QA readiness. Engineering executes deployment.

## Steps

1. Fetch the live release scope from Jira by project/Fix Version.
2. Treat the Fix Version as the current delivery commitment and inspect changelog/history when commitment changes matter.
3. Group work by initiative/outcome where useful, but do not depend on Epic status as the sole project signal.
4. Inspect current statuses, blockers, unresolved Bugs, overdue work, late scope changes, and remaining delivery stages.
5. Inspect relevant PRs/code/repositories when implementation or deployment readiness matters.
6. Check QA in DEV evidence for individual-change validation.
7. Check STG evidence including automated regression, integration testing, and targeted validation as appropriate.
8. Check rollout, migration/data, observability/monitoring, rollback, training/business-readiness, or other operational concerns when relevant.
9. Separate must-resolve blockers from acceptable risks and post-release follow-ups.
10. Confirm QA has declared the release Ready for Release before treating it as ready to ship.
11. Surface any business/PM decision still required for actual release timing.

## Delivery-risk principle

Raise risk early enough to act, but do not warn on everything all the time. Consider the full delivery path and the amount of time remaining rather than treating one status/field as decisive.

The scheduled item-level AI experiment is defined separately in `standards/ai-release-confidence.md`; do not invent Epic/release rollup logic here yet.

## Output

- **Release scope summary**
- **Ready**
- **Watch / At risk**
- **Blocked**
- **QA readiness**
- **Operational / rollout concerns**
- **Business/PM decisions required**
- **Recommended actions**

Do not equate ticket status with readiness. Do not equate QA readiness with the business decision to release.

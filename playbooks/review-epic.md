# Playbook: Review an Epic

## Goal

Assess whether an Epic provides useful context for its current work without imposing an Epic/capability taxonomy that has not yet been decided.

## Important boundary

The long-term model for finite initiatives vs persistent capability/product-area buckets is **still an open design question**.

Do not treat an existing persistent/bucket Epic as invalid merely because it is not a finite initiative. Do not recommend a new hierarchy model as though it were already policy.

## Steps

1. Fetch the Epic live from Jira.
2. Fetch its direct children live when relevant.
3. Understand what the Epic currently appears to represent: a bounded initiative, persistent grouping/capability, catch-all bucket, or unclear context.
4. Evaluate whether the Epic provides enough useful context for the work it currently contains.
5. For a clearly finite initiative, assess problem, outcome, scope, success, dependencies, and decomposition where useful.
6. Inspect child Stories/Tasks/Bugs for coverage, overlap, missing work, and inconsistent lifecycle state.
7. Inspect relevant code/artifacts only when technical truth is needed.
8. Check for an initiative workspace in `initiatives/`; if one exists, use its durable decisions but do not trust it for live Jira state.
9. Report concrete quality/context gaps without turning the review into an unapproved hierarchy redesign.

## Output

Prefer:

- **What the Epic appears to represent**
- **Useful context / strengths**
- **Gaps**
- **Child-work / decomposition concerns**
- **Risks / missing decisions**
- **Recommended Jira improvements that do not depend on an unresolved taxonomy**
- **Recommended durable artifacts**, only if genuinely useful

Do not write changes unless authorized. Keep the Epic/capability model open until it is explicitly decided.

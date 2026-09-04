# Playbook: Assess AI Release Confidence

## Goal

Produce a concise, evidence-based delivery-confidence assessment for every committed Story and standalone Bug without turning the automation into a broad Jira hygiene bot.

Read `standards/ai-release-confidence.md` before running this playbook.

## Scope gate

Only assess Jira items that meet both conditions:

1. issue type is **Story** or standalone **Bug**;
2. a **Fix Version** is assigned.

Do not expand the scheduled scan based on ownership, business visibility, parent hierarchy, completeness fields, or other prerequisites.

## Daily flow

1. Resolve/fetch `committed_story_bugs` from live Jira.
2. For each eligible item, fetch enough current Jira context to understand its delivery state and current Fix Version.
3. Read Jira changelog/history for critical changes, especially:
   - Fix Version;
   - AI Release Confidence;
   - AI Release Confidence Reason;
   - AI Release Confidence Feedback.
4. Read the current human-owned Feedback field.
5. Gather other available delivery evidence when it materially improves assessment, including GitHub/PR, QA, blockers/dependencies, estimates, scope changes, technical review, and team context.
6. Weight the evidence against **time remaining to the committed release**.
7. Decide `On Track`, `Watch`, or `At Risk` using the definitions in the standard.
8. Draft a short Reason naming only the strongest signals.
9. Compare the proposed values with current Jira values.
10. Write only when Confidence or the material Reason has changed. Never edit the Feedback field.

## Reason quality

A useful Reason answers:

> What is the strongest evidence that makes this confidence level appropriate today?

Prefer a small number of concrete signals over a diagnostic dump.

Good:

> Watch: 9 days to release, development has not started, and the dependent API work is still in code review.

Weak:

> Watch: item may be delayed.

Also weak:

> Watch: status=To Do, estimate=5, sprint=42, assignee=X, labels=Y, parent=Z...

## Fix Version changes

When changelog shows a Fix Version change, explicitly assess the change:

- moved earlier -> expedite / compressed window;
- moved later -> delay / revised commitment.

Do not automatically downgrade solely because the date changed. Explain why the revised commitment is or is not credible now.

## Scope changes

Material requirement/acceptance-criteria changes after commitment should be considered and may be noted in the Reason. They are not automatic risk downgrades.

## Human Feedback

Treat Feedback as important evidence, but not a guaranteed override. If other evidence still supports a different conclusion, keep the evidence-based assessment and explain the material reason without arguing with the human.

Never clear, append to, or rewrite the Feedback field.

## Guardrails

- Do not scan uncommitted work in the scheduled job.
- Do not create release/Epic rollup scores yet.
- Do not maintain a parallel history in Git.
- Do not rewrite equivalent fields every day.
- Do not expose secrets or credentials in Reasons.
- Do not make priority or release-tradeoff decisions for the business.

## Output / write set

For each eligible Story/Bug:

- **AI Release Confidence**: `On Track | Watch | At Risk`
- **AI Release Confidence Reason**: concise rationale

Nothing else is owned by this automation during the experiment.

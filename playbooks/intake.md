# Playbook: Normalize Intake

## Goal

Capture legitimate requests early, then turn raw intake into clear business requirements without confusing Jira existence with approval or commitment.

Read `standards/product-lifecycle.md` first.

## Operating rule

Anyone may create a Jira request, including through a request form. **Capture first.**

A Jira item at intake is not automatically approved, prioritized, ready, or committed.

## Steps

1. Understand the request and preserve useful source evidence.
2. Search Jira for duplicates, related work, prior requirements, and known context.
3. Determine what the request actually represents: Bug, Story, Task, Spike, Epic/initiative, reporting need, process issue, configuration/data issue, or something else.
4. Identify the underlying business/user need.
5. Preserve the requester's proposed solution as meaningful input.
6. Challenge the proposed solution when it is not optimal and recommend a better approach when possible.
7. Normalize raw forms, Slack/email threads, screenshots, and payloads into an actionable description rather than leaving source material as the final definition.
8. Work toward Business Requirements Complete by clarifying problem, affected users, current/desired behavior, rules, scope, scenarios, dependencies, and expected outcome.
9. Confirm the business supplies **priority** and **business due date** before normal commitment.
10. PM assesses Business Requirements Complete; business approves it.
11. Create/update Jira only within the user's authorization or approved workflow.

## Guardrails

- Do not treat Jira existence as commitment.
- Do not duplicate work that already exists.
- Do not expose credentials, tokens, or other secrets from source material.
- Do not confuse a requested implementation with the underlying requirement.
- Do not confuse a reporting/data need with a product behavior change.
- Do not manufacture a delivery commitment from the business due date. Product + Engineering set the Fix Version later.

## Output

- **Underlying need**
- **Requested solution**
- **Recommended solution**, when different
- **Classification**
- **Related Jira work**
- **Business Requirements Complete gaps**
- **Recommended action**
- **Draft Jira content**, when useful

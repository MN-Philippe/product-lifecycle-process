# Playbook: Normalize Intake

## Goal

Turn raw requests from Slack, email, meetings, support, or pasted forms into the right actionable work without blindly creating a Jira ticket.

## Steps

1. Understand the request and its source evidence.
2. Search Jira for duplicates, related Epics, Stories, Bugs, and known capability areas.
3. Determine whether the need is best represented as a Bug, product Story, engineering Task, Spike, Epic, reporting request, process change, or no software work at all.
4. Identify the business/user problem before prescribing implementation.
5. Preserve useful evidence but synthesize the Jira description instead of dumping raw source material.
6. Recommend parent/link relationships and relevant release/ownership context when evident from live Jira.
7. If durable technical work is likely, identify which artifact scaffold may be useful.
8. Draft the proposed Jira item(s). Create or update only when authorized.

## Guardrails

- Do not assume every request deserves a new ticket.
- Do not duplicate work that already exists.
- Do not expose credentials, tokens, or other secrets from source material.
- Do not force user-story syntax onto engineering work.
- Do not confuse a reporting/data need with a product behavior change.

## Output

- **What the request is actually asking for**
- **Classification**
- **Related Jira work**
- **Recommended action**
- **Draft Jira content**, when useful

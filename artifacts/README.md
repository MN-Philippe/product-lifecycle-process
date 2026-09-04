# Durable Artifact Scaffolding

Use these templates only when the work needs durable information that does not belong in a Jira ticket.

Do not create artifacts by default. Prefer Jira for ticket-level context and implementation repositories for code-local documentation.

## Architecture / technical design

Useful when an initiative needs durable cross-cutting design or decisions:

- `architecture/technical-design.md`
- `architecture/adr.md`
- `architecture/integration-contract.md`

## Delivery

Useful when execution has meaningful sequencing, risk, or operational complexity:

- `delivery/implementation-plan.md`
- `delivery/test-strategy.md`
- `delivery/rollout-plan.md`

## Product

Useful when discovery/problem framing is larger than a Jira description:

- `product/problem-definition.md`

## Rules

- Link the artifact to its Jira initiative; do not copy live Jira state into it.
- Record durable decisions, constraints, interfaces, and rationale.
- Avoid restating information already available in code or Jira unless the artifact needs it for comprehension.
- Keep artifacts close to the initiative that uses them when initiative-specific.

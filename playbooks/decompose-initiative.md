# Playbook: Decompose an Initiative

## Goal

Break a bounded outcome into coherent delivery work without losing the business intent or prematurely over-specifying implementation.

## Steps

1. Fetch the initiative/Epic live and inspect current children.
2. Confirm the problem, desired outcome, scope, constraints, important non-scope, business priority, and due date when available.
3. Identify major user/business capabilities and technical enablers required to reach the outcome.
4. Separate product Stories from Tasks/Spikes/other technical work.
5. For every proposed Jira **Story**, follow `standards/story-quality.md` and use a Summary that clearly states `As a / I want / So that` at ELT-readable quality.
6. Identify dependencies, sequencing constraints, migration needs, observability/testing needs, and rollout concerns.
7. Propose work that is independently understandable and can later become Product Complete with clear acceptance criteria and QA coverage.
8. Avoid decomposition that merely mirrors components or teams unless that is genuinely how value must be delivered.
9. Recommend conditional Engineering review where architecture, permissions, integrations, data, security, performance, deployment, or feasibility warrants it.
10. Recommend durable artifacts only where the initiative needs design/decision material beyond Jira.

## Output

- **Outcome and scope recap**
- **Proposed work breakdown**
- **Proposed Story Summaries in required format**
- **Dependencies / sequencing**
- **Engineering-review candidates**
- **Open decisions**
- **Recommended Jira changes**
- **Recommended artifacts**, if any

Do not create all proposed Jira work unless authorized. Do not assume a new Epic/capability taxonomy while that design question remains open.

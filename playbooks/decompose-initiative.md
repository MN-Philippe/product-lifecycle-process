# Playbook: Decompose an Initiative

## Goal

Break a bounded outcome into coherent delivery work without losing the business intent or prematurely over-specifying implementation.

## Steps

1. Fetch the initiative/Epic live and inspect current children.
2. Confirm the problem, desired outcome, scope, constraints, important non-scope, business priority, and due date when available.
3. Identify major user/business capabilities and technical enablers required to reach the outcome.
4. Identify every implementation repository touched by the initiative. Do not assume the Jira project key maps to one repository; MYM commonly spans Radius, Scheduling, Guardian Portal, and related repositories.
5. Separate product Stories from Tasks/Spikes/other technical work. A PR/repository boundary alone does not justify a Story.
6. Decompose first by coherent product behavior. Then identify repository-specific execution needed to implement each behavior.
7. When several repositories contribute to the same product behavior, prefer one product Story with repository-bounded Tasks/Sub-tasks when practical. Create separate repository-bounded Stories only when each repository owns distinct product behavior with its own meaningful acceptance criteria and lifecycle.
8. For every proposed Jira **Story**, follow `standards/story-quality.md`. Prefix `[Repo]` only when the Story itself is genuinely repository-owned. Use action-oriented `[Repo]` summaries for Tasks/Sub-tasks.
9. Identify source-of-truth, trust/validation boundaries, minimum cross-repository contracts, null/default semantics, compatibility expectations, and logic that must not be duplicated.
10. Identify real blockers separately from integration gates. If work can proceed against a frozen contract, do not model it as blocked merely because the upstream implementation is not merged.
11. Build the dependency graph at the implementation-work level, then collapse it into a small number of useful execution waves when timing warrants it.
12. Propose work that is independently understandable and can later become Product Complete with clear acceptance criteria and QA coverage.
13. Keep decomposition lean. Split work when it creates useful ownership, review, testing, or sequencing boundaries; combine coherent same-owner work when splitting creates tiny-ticket noise without reducing delivery risk.
14. As an execution heuristic, implementation Tasks/Sub-tasks in the 3-5 point range are often easier to plan than many 1-point fragments, but do not treat this as a hard rule.
15. Recommend conditional Engineering review where architecture, permissions, integrations, data, security, performance, deployment, or feasibility warrants it.
16. Recommend durable artifacts only where the initiative needs design/decision material beyond Jira.

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

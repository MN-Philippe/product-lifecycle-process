# Playbook: Decompose an Initiative

## Goal

Break a bounded outcome into coherent delivery work without losing the business intent or prematurely over-specifying implementation.

## Steps

1. Fetch the initiative/Epic live and inspect current children.
2. Confirm the problem, desired outcome, scope, constraints, important non-scope, business priority, and due date when available.
3. Identify major user/business capabilities and technical enablers required to reach the outcome.
4. Identify every implementation repository touched by the initiative. Do not assume the Jira project key maps to one repository; MYM commonly spans Radius, Scheduling, Guardian Portal, and related repositories.
5. Separate product Stories from Tasks/Spikes/other technical work.
6. When implementation spans repositories, split Stories by repository whenever the work can be developed, reviewed, tested, and merged independently. Preserve the common business outcome at the Epic/capability level and express cross-repository dependencies explicitly.
7. For every proposed Jira **Story**, follow `standards/story-quality.md`. In multi-repository work, start the Summary with `[Repo]`, then use the required `As a / I want / so that` format at ELT-readable quality.
8. Identify dependencies, sequencing constraints, migration needs, observability/testing needs, and rollout concerns.
9. Propose work that is independently understandable and can later become Product Complete with clear acceptance criteria and QA coverage.
10. Avoid decomposition that merely mirrors teams. Repository boundaries are a valid decomposition boundary when they correspond to independently implemented/reviewed code, but do not split a coherent same-repository behavior into artificial fragments without delivery value.
11. Recommend conditional Engineering review where architecture, permissions, integrations, data, security, performance, deployment, or feasibility warrants it.
12. Recommend durable artifacts only where the initiative needs design/decision material beyond Jira.

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

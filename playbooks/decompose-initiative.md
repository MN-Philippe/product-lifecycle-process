# Playbook: Decompose an Initiative

## Goal

Break a bounded outcome into coherent delivery work without losing the business intent or prematurely over-specifying implementation.

## Steps

1. Fetch the initiative/Epic live and inspect current children.
2. Confirm the problem, desired outcome, scope, constraints, important non-scope, business priority, and due date when available.
3. Identify major user/business capabilities and technical enablers required to reach the outcome.
4. Identify every implementation repository touched by the initiative. Do not assume the Jira project key maps to one repository; MYM commonly spans Radius, Scheduling, Guardian Portal, and related repositories.
5. Decompose implementation into **cohesive, generally single-repository Stories**.
6. Within a repository, split further when separate units would be easier to understand, implement, review, test, or merge independently. Do not keep a large Story together merely because all changes live in one repo.
7. For every proposed Jira **Story**, follow `standards/story-quality.md` and prefix the owning repository with `[Repo]` for multi-repository initiatives.
8. Use explicit Story-to-Story dependencies for cross-repository sequencing. A cross-repository Story should be exceptional.
9. Do **not** create Tasks/Sub-tasks by default. Add them only when they materially support sequencing, parallel ownership, or separately tracked execution needed by the delivery plan.
10. Identify source-of-truth, trust/validation boundaries, minimum cross-repository contracts, null/default semantics, compatibility expectations, and logic that must not be duplicated.
11. Identify real blockers separately from integration gates. If work can proceed against a frozen contract, do not model it as blocked merely because the upstream implementation is not merged.
12. When a hard deadline creates a genuine need for parallel tracks, introduce the minimum useful Tasks/Sub-tasks and collapse dependencies into a small number of execution waves.
13. Propose work that is independently understandable and can later become Product Complete with clear acceptance criteria and QA coverage.
14. Keep decomposition lean: prefer smaller cohesive Stories over both oversized Stories and lower-level ticket noise.
15. Run a simplification pass across the Epic and proposed Stories:
    - keep shared rules at the highest useful level;
    - remove duplicated or implied detail from children;
    - use one term consistently for each domain concept;
    - remove examples and implementation notes that do not resolve real ambiguity;
    - make each child readable without forcing developers to sort signal from generated noise.
16. Recommend conditional Engineering review where architecture, permissions, integrations, data, security, performance, deployment, or feasibility warrants it.
17. Recommend durable artifacts only where the initiative needs design/decision material beyond Jira.

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

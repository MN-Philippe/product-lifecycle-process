# Initiative Workspaces

An initiative does not need a folder here simply because it has a Jira Epic.

Create a workspace only when the initiative needs durable material that Jira is not a good home for, such as architecture, ADRs, integration contracts, implementation plans, test strategy, or rollout/migration detail.

## Suggested naming

`<JIRA-KEY>-<short-name>/`

Example:

```text
MYM-421-observability/
├── README.md
├── architecture.md
├── decisions/
├── implementation-plan.md
├── test-strategy.md
└── rollout.md
```

## Workspace README

Keep the README lightweight:

```yaml
jira: MYM-421
product: myMathnasium
systems:
  - <system>
repos:
  - <repo>
```

Then provide a short artifact index.

Do not copy status, assignee, priority, fix version, child Stories, comments, or other live Jira state into the workspace.

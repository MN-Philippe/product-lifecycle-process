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

Keep the README lightweight. It may include stable pointers such as:

```yaml
jira: MYM-421
product: myMathnasium
systems:
  - <system>
repos:
  - <repo>
```

Do not copy status, assignee, priority, fix version, child Stories, comments, or other live Jira state into the workspace.

## Repository-level index

`ARTIFACT_INDEX.md` is generated from the actual workspace files. It is a navigation aid, not another source of project status.

After adding, renaming, or removing an initiative artifact, regenerate it with:

```bash
python tools/artifact_index.py --write
```

CI runs `python tools/artifact_index.py --check` so the index cannot quietly drift into a manually maintained project tracker.

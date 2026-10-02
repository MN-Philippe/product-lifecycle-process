# Product Lifecycle Tooling

Confluence is the authoritative home for Mathnasium product lifecycle standards, playbooks, templates and durable handbook content.

- [Technology & Product Handbook](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2162262120)
- [Product Lifecycle Process](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2162327553)
- [Agent Router](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2162065429)
- [Handbook Index](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2162819145)

The handbook is still under collective review. Confluence authority does not make a proposed rule approved: preserve each page's status, evidence, scope and unresolved decisions.

## What remains here

This repository maintains executable tooling, reusable JQL, tests and the Claude plugin package. Former policy paths contain links only, so old bookmarks continue to work without maintaining a competing copy. Git history preserves prior content.

Jira owns live work and commitments. Implementation repositories own code/tests/runtime configuration. Confluence owns durable business definitions and process rules.

## Plugin

The plugin's references contain Confluence pointers. The agent fetches live page bodies through the Atlassian connector and follows the relevant standards. An unavailable page is an evidence gap, not permission to fall back to outdated policy.

Editing Confluence text does not require rebuilding the plugin. Changes to routing pointers or the skill bootstrap require `python tools/build_plugin.py`; this refreshes pointers and bumps the plugin version. It does not download or bundle page bodies.

## Tooling changes

1. Read AGENTS.md and the relevant live Confluence standard.
2. Change tools, queries or routing as needed.
3. Run `python -m unittest discover -s tests -p 'test_*.py'` and `python tools/build_plugin.py --check`.
4. Open a PR using the normal repository workflow.

The Jira helper is advisory. Its deterministic checks implement a versioned subset of the standard; read current Confluence before treating a result as a policy finding. Unconfirmed defaults must not become release blockers just because a helper emits a warning/error.

The artifact-index helper remains available for existing repo-local technical artifacts. New cross-system initiative documentation belongs in Confluence; the local index is not the handbook index and does not list Confluence pages.

# Agent Instructions

Read the live [Agent Router](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2162065429) and the task-specific standards it links before doing product/Jira work. Read the [Handbook Index](https://mathnasium.atlassian.net/wiki/spaces/IPD/pages/2162819145) for other handbook topics.

Confluence is authoritative for durable policy. Local standards, playbooks and templates are navigation pointers only. Respect draft/proposed labels; do not treat an unapproved engineering PR as policy. If live guidance is inaccessible, report the limitation and do not silently substitute old Git content.

Jira remains live truth for tickets. Fetch live state before conclusions and use the user's existing authorization for writes. Preserve unresolved decisions. Never copy secrets. Link Jira keys in output.

For tooling changes, preserve the stateless/read-only data boundary, run the existing unit tests, regenerate the plugin when routing/bootstrap changes, and verify build_plugin.py --check. Repository tooling does not override Confluence policy.

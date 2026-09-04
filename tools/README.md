# Helper Tooling

This directory is for small helpers that make agent workflows faster and more consistent without persisting a shadow copy of Jira.

Good candidates:

- resolve a named Jira shortcut from `jira/queries.yaml`;
- fetch an Epic plus its live children into agent context;
- run read-only quality checks against live issues;
- build an index of durable initiative artifacts from repository metadata;
- detect likely credentials/secrets before proposed Jira content is written;
- produce release-readiness input from live Jira plus explicitly linked artifacts.

Avoid tooling that:

- exports Jira into Git;
- syncs status/assignee/comments/fix versions;
- requires a local database of Jira issues;
- makes stale cached issue data the default source;
- writes broad Jira changes without an explicit approval policy.

The first useful implementation target is a **read-only Jira context/audit helper**, followed by an **artifact index generator**. Keep both stateless where practical.

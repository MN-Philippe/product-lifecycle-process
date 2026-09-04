# Helper Tooling

This directory contains small, stateless helpers that make agent workflows faster and more consistent without persisting a shadow copy of Jira.

## Jira helper

`jira_helper.py` deliberately does **not** authenticate to Jira. The active AI agent or connector should fetch live Jira data. This helper supplies shared query shortcuts and deterministic normalization/audit logic without becoming another Jira client or data store.

Install the small local dependency:

```bash
python -m pip install -r requirements.txt
```

List known Jira shortcuts:

```bash
python tools/jira_helper.py list
```

Resolve a shortcut into JQL:

```bash
python tools/jira_helper.py query active_epics
python tools/jira_helper.py query release_scope \
  --param project=MYM \
  --param fix_version=OCT-2026
```

Typical agent flow:

1. resolve a named query from `jira/queries.yaml`;
2. fetch the results live through the available Jira connector/client;
3. pass the returned JSON into the helper when deterministic compaction/auditing is useful;
4. reason from the live result plus repo guidance;
5. write to Jira only when authorized.

Compact and redact a live Jira payload:

```bash
python tools/jira_helper.py context jira-result.json
# or
cat jira-result.json | python tools/jira_helper.py context -
```

Run deterministic quality checks:

```bash
python tools/jira_helper.py audit jira-result.json
```

The audit is intentionally advisory. It flags obvious structural/quality concerns such as empty Epic context, unparented active Stories, unclear completion criteria, weak Bug reproduction detail, past-due active work, hierarchy/status inconsistencies when the parent is present in the payload, and possible credentials/secrets. It does not decide business priority or replace human/product judgment.

Secret-like values are redacted from compact output and are never echoed in audit findings.

## Artifact index

`artifact_index.py` builds a table of contents from the durable files that actually exist under `initiatives/`. It does not query Jira and does not add live Jira state to the index.

Preview:

```bash
python tools/artifact_index.py
```

Regenerate the checked-in index:

```bash
python tools/artifact_index.py --write
```

CI verifies that `ARTIFACT_INDEX.md` stays generated rather than becoming another manually maintained document:

```bash
python tools/artifact_index.py --check
```

## Keep the boundary

Good helper-tool candidates:

- resolve named Jira shortcuts;
- compact live Jira results for agent context;
- run read-only quality checks against live issues;
- build indexes of durable initiative artifacts;
- detect likely credentials/secrets before proposed Jira content is written;
- produce release-readiness input from live Jira plus explicitly linked artifacts.

Avoid tooling that:

- exports Jira into Git;
- syncs status, assignee, comments, priority, or fix versions;
- requires a local database of Jira issues;
- makes stale cached issue data the default source;
- writes broad Jira changes without an explicit approval policy.

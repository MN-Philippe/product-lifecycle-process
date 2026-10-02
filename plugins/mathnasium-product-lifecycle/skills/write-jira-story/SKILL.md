---
name: write-jira-story
description: Write, refine, split, decompose and ready-check Jira Stories for the RAD and MYM projects. Use when asked to "write a story for…", "draft a story", "refine MYM-123", "improve the acceptance criteria", "split this story", "decompose this epic", "write stories for this BRD", "turn this into Jira stories", "is MYM-123 ready for dev", "is this story ready", or "review this story", or when given a raw request form, email or Slack thread to turn into work.
---

# Write Jira Stories

The playbooks, standards and templates live in the Technology & Product Handbook in Confluence. Read them live; do not rely on memory. Page IDs and reading rules are in [handbook-index.md](handbook-index.md).

Pick the mode from the request, read its playbook page, then the standards it names, and follow the steps.

| Mode | When | Playbook page |
| --- | --- | --- |
| Write | "write a story for…", "draft a story" | Playbook - Write Story |
| Refine | "refine MYM-123", "improve the acceptance criteria", new answers to fold in | Playbook - Refine Story |
| Split | "split this story", estimate over 5 points, several repos | Playbook - Split Story |
| Decompose | "decompose this epic", "write stories for this BRD", "turn this into Jira stories" | Playbook - Decompose Initiative |
| Intake | raw request forms, emails, Slack threads | Playbook - Intake |
| Ready check | "is MYM-123 ready for dev", "is this story ready" | Playbook - Ready Check |
| Review | "review this story" | Playbook - Review Story |
| Bug | "triage this bug" | Playbook - Triage Bug |

The Story Standard page is the authority for Stories; follow it wherever this file is less specific.

## Ground rules

- Jira is the live truth. Fetch before concluding; never rely on memory of a ticket.
- **GitHub issues and PRs are read-only, and Jira writes follow draft, approve, then write.** Show the full draft (or a before/after), wait for an explicit "create it" or "approved" in a later reply, then write only what was approved. A hook in this plugin enforces this and asks before every Jira write, once per Story. The full rule is the Write policy section of the Jira Conventions page; if that section is missing there, the rule in this paragraph still applies.
- If a handbook page is still a "Draft placeholder", say so instead of guessing.
- Link every Jira key to `https://mathnasium.atlassian.net/browse/<KEY>`.
- Never copy secrets or credentials into Jira content.
- Jira site, cloudId and field IDs: the Jira Conventions page.
- The handbook is read-only here; do not edit Confluence.

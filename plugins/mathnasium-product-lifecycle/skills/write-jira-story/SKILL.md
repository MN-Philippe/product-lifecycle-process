---
name: write-jira-story
description: Write, refine, split, decompose, triage and ready-check Jira work items for the RAD and MYM projects. Use for "write a story for…", "draft a story", "refine MYM-123", "improve the acceptance criteria", "split this story", "decompose this epic", "write stories for this BRD", "turn this into Jira stories", "is MYM-123 ready for dev", "is this story ready", "review this story", "triage this bug", or when given a raw request form, email or Slack thread to turn into work.
---

# Jira work items

The standards, playbooks and templates live in the Technology & Product Handbook in Confluence. Read them live; never rely on memory.

## Start here

1. Find the index with the Atlassian connector: `searchConfluenceUsingCql` with `(label = "plugin-index" OR title = "Handbook Index") AND space = "IPD" AND type = page` (cloudId `abd26ef1-c908-455d-8b20-516e025731b2`, site `https://mathnasium.atlassian.net`). Read that page once per session with `getConfluencePage`, `contentFormat: markdown`.
2. Check its **Plugin contract** line. This plugin supports contract **1**. If the page says a higher number, tell the user to update the plugin and stop.
3. Use the index's **Intent router** to pick the playbook for the request. Read that playbook, then the standards it names, and follow its steps. The Story Standard is the authority for Stories.

If there is no Atlassian connector or index page, say so plainly and stop. If a page is a "Draft placeholder", say so instead of guessing.

## Ground rules

- Jira is the live truth. Fetch before concluding; never rely on memory of a ticket.
- **GitHub issues and PRs are read-only, and Jira writes follow draft, approve, then write.** Show the full draft (or a before/after), wait for an explicit "create it" or "approved" in a later reply, then write only what was approved. A hook in this plugin asks before every Jira write, once per Story.
- Link every Jira key to `https://mathnasium.atlassian.net/browse/<KEY>`.
- Never copy secrets or credentials into Jira content.
- The handbook is read-only here; do not edit Confluence.

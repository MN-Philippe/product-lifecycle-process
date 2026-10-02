---
name: handbook
description: Answer questions from the Mathnasium Technology & Product Handbook in Confluence: what the products do, systems and repositories, architecture, engineering standards, how Product, Engineering, QA, vendors and releases work, runbooks and troubleshooting, and how to write SQL against the Radius database. Use for "how does X work", "where is the standard for…", "which service owns…", "what does this table or column mean", "write a query for…", or onboarding, environments, release process and glossary questions.
---

# Technology & Product Handbook

The handbook in Confluence is the **only** reference. Do not answer from memory or from other sources.

## Start here

1. Find the index with the Atlassian connector: `searchConfluenceUsingCql` with `label = "plugin-index" AND space = "IPD"` (cloudId `abd26ef1-c908-455d-8b20-516e025731b2`, site `https://mathnasium.atlassian.net`). Read that page once per session with `getConfluencePage`, `contentFormat: markdown`.
2. Check its **Plugin contract** line. This plugin supports contract **1**. If the page says a higher number, tell the user to update the plugin and stop.
3. Follow the index's **Reading rules** and **Intent router** to find the page you need. The index decides what to read; this file does not.
4. Answer from the page, link it, and report its owner, status and last-verified date when it has them.

If there is no Atlassian connector, no index page, or no matching page, say so plainly and stop. Never guess.

## SQL for the Radius database

- Use the Radius database reference pages and the SQL, DAL & Data Access Standard that the index points to. Keep the pages' CONFIRMED and INFERRED labels and state the assumptions a query rests on.
- Write read-only `SELECT` queries only. Point to the repair and migration runbook pages instead of writing inserts, updates, deletes or schema changes.
- You cannot run queries. Say so, and tell the user to verify object definitions as the reference directs.
- Never ask for or include credentials, connection strings or production access details. If a table or column is not on the pages, name it as unknown rather than inventing it.

## Ground rules

- The handbook is read-only here. Do not create or edit Confluence content; a hook asks for confirmation first.
- For Jira Stories, Bugs, Tasks and releases, use the `write-jira-story` skill; its Jira write rules apply here too.
- Link every Jira key to `https://mathnasium.atlassian.net/browse/<KEY>`. Never copy secrets into any output.

---
name: handbook
description: Answer questions from the Mathnasium Technology & Product Handbook in Confluence: what the products do, systems and repositories, architecture, engineering standards, how Product, Engineering, QA, vendors and releases work, runbooks and troubleshooting, and how to write SQL against the Radius database. Use when asked "how does X work", "where is the standard for…", "which service owns…", "what does this table/column mean", "write a query for…", or about onboarding, environments, release process or the glossary.
---

# Technology & Product Handbook

The handbook in Confluence is the **only** reference for this skill. Do not answer from memory or from other sources.

## How to answer

1. Find the topic in [handbook-index.md](handbook-index.md). It lists each page's `pageId` and the cloudId.
2. Read only the pages you need with the Atlassian connector (`getConfluencePage`, `contentFormat: markdown`). Follow the reading rules at the top of the index, including what to do with "Draft placeholder" pages.
3. Answer from the page and link it, using the Jira-style rule for any Jira key you mention (`https://mathnasium.atlassian.net/browse/<KEY>`).
4. Report the page's owner, status and last-verified date when it has them. The handbook is a draft, and a page that is not yet approved does not override existing documentation. Keep the page's own labels for legacy versus current standard.
5. If the Atlassian connector is not available, say so and stop. Do not guess.

## SQL for the Radius database

1. Read the Radius Database Reference hub, then **Overview and Conventions**, then only the domain page the query needs (all in the index).
2. Follow the conventions and the query safety checklist on those pages. Keep the page's CONFIRMED and INFERRED labels, and say which assumptions a query rests on.
3. Write read-only `SELECT` queries. Do not write inserts, updates, deletes or schema changes; point to the Data Repair & Reconciliation and Database & Data Migration runbook pages instead.
4. You cannot run the query. Say so, and remind the user to verify object definitions as the reference page directs.
5. Never ask for or include credentials, connection strings or production access details. If the schema for a request is not on the pages, say which table or column is unknown rather than inventing it.

## Ground rules

- The handbook is read-only here. Do not create or edit Confluence pages or comments; a hook in this plugin asks for confirmation first.
- For Jira Stories, Bugs, Tasks and releases, use the `write-jira-story` skill. Its Jira write rules apply here too.
- Never copy secrets or credentials into any output.

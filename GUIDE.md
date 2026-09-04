# Repository Operating Guide

## What this repo is

This repository is a helper layer for AI-assisted product and delivery work. Its job is to reduce rediscovery, encode stable operating knowledge, and give agents reliable shortcuts and playbooks for working with live systems.

Use it for:

- durable instructions and standards;
- stable descriptions of products, boards, workflows, and terminology;
- reusable JQL/query patterns;
- agent playbooks;
- templates and scaffolding for architecture, delivery, and product artifacts;
- durable initiative-specific decisions and designs when Jira is not the right home.

## What this repo is not

Do **not** turn this repository into:

- a Jira export;
- one Markdown file per Jira ticket;
- a cache of issue status, assignee, sprint, fix version, priority, or comments;
- a replacement project-management database;
- a synchronization service between Jira and Git;
- a second backlog;
- a place to paste large amounts of source data that can be fetched live;
- an agent memory dump containing transient observations.

If information can be fetched reliably from Jira or the implementation repository and changes frequently, fetch it at runtime instead of persisting it here.

## Source-of-truth boundaries

### Jira

Jira owns live delivery state:

- issues and hierarchy;
- status;
- assignee;
- priority;
- due dates;
- fix versions/releases;
- comments and workflow history;
- current acceptance criteria and ticket-level decisions.

### Product / engineering repositories

Implementation repositories own:

- source code;
- tests;
- runtime configuration;
- infrastructure-as-code;
- implementation-specific documentation close to the code.

### This repository

This repository owns:

- how agents should interpret the systems above;
- what good product/delivery work looks like;
- how to execute repeatable reviews and audits;
- stable cross-repository context;
- durable cross-cutting artifacts that do not naturally belong in a single implementation repository.

## Initiative workspaces

An initiative does **not** need a folder here simply because it has a Jira Epic.

Create an initiative workspace only when there is durable information worth keeping outside Jira, such as:

- architecture/design;
- ADRs;
- integration contracts;
- migration plans;
- dependency maps;
- test strategy;
- rollout/operational-readiness plans;
- important decisions that need a durable technical record.

An initiative folder should reference the Jira key and relevant systems/repos, but it should not copy Jira state.

## Agent write policy

Default behavior is read-first and propose-first.

1. Fetch live state.
2. Inspect relevant durable context.
3. Analyze against the appropriate playbook and standards.
4. Recommend changes.
5. Write to Jira/GitHub only when explicitly authorized or when the surrounding automation has a clearly approved write policy.

## Design principle

Prefer small, composable guidance over a giant process manual. If a rule matters only to one workflow, keep it in that playbook. If it is broadly reusable, promote it into shared context or Jira quality rules.

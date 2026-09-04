# Repository Operating Guide

## What this repo is

This repository is a helper layer for AI-assisted product and delivery work. Its job is to reduce rediscovery, encode stable operating knowledge, and give agents reliable standards, shortcuts, and playbooks for working with live systems.

Use it for:

- canonical product-lifecycle and Jira-work standards;
- durable agent instructions;
- stable descriptions of products, boards, workflows, and terminology;
- reusable JQL/query patterns;
- agent playbooks;
- templates and scaffolding for architecture, delivery, and product artifacts;
- durable initiative-specific decisions and designs when Jira is not the right home.

The canonical lifecycle standards live under `standards/`.

## What this repo is not

Do **not** turn this repository into:

- a Jira export;
- one Markdown file per Jira ticket;
- a cache of issue status, assignee, sprint, Fix Version, priority, comments, confidence, or field history;
- a replacement project-management database;
- a synchronization service between Jira and Git;
- a second backlog;
- a place to paste large amounts of source data that can be fetched live;
- an agent memory dump containing transient observations;
- a place to prematurely standardize unresolved process questions.

If information can be fetched reliably from Jira or an implementation repository and changes frequently, fetch it at runtime instead of persisting it here.

## Source-of-truth boundaries

### Jira

Jira owns live delivery state:

- issues and hierarchy;
- status;
- assignee;
- business priority and due dates;
- Fix Versions/releases;
- comments and workflow history;
- field changelog/history;
- current acceptance criteria and ticket-level decisions;
- AI Release Confidence / Reason / Feedback field values.

A Fix Version is the current delivery commitment. Use Jira changelog/history to understand how that commitment or the AI fields changed over time; do not copy the history into this repo.

### Product / engineering repositories

Implementation repositories own:

- source code;
- tests;
- runtime configuration;
- infrastructure-as-code;
- implementation-specific documentation close to the code.

### This repository

This repository owns:

- the agreed product lifecycle;
- how agents should interpret live systems;
- what good Stories/Bugs/product definition look like;
- how to execute repeatable reviews and audits;
- stable cross-repository context;
- durable cross-cutting artifacts that do not naturally belong in a single implementation repository.

## Standards vs scheduled automation

Do not confuse broad good-practice standards with automation scope.

The current scheduled AI Release Confidence experiment is intentionally narrow:

- only Stories and standalone Bugs;
- only when a Fix Version is present;
- early-morning daily cadence;
- AI owns Release Confidence and Reason;
- humans own Feedback;
- no Epic/release aggregation or dashboard scoring yet.

See `standards/ai-release-confidence.md`.

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
2. Inspect relevant durable context and standards.
3. Analyze against the appropriate playbook.
4. Recommend changes.
5. Write to Jira/GitHub only when explicitly authorized or when an approved automation has a clearly bounded write policy.

The AI Release Confidence experiment is an example of a bounded write policy: it owns only the AI Confidence and Reason fields and never edits human Feedback.

## Design principle

Prefer small, composable guidance over a giant process manual. Promote decisions to canonical standards when they apply broadly. Keep unresolved areas explicitly open rather than filling the gap with generic process doctrine.

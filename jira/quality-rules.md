# Jira Quality Rules

These rules guide agent reviews. They are not all hard gates.

Use three severities:

- **Error** - missing information makes the work unsafe or not actionable.
- **Warning** - likely quality or lifecycle problem that deserves review.
- **Suggestion** - improvement that may make the ticket clearer or easier to deliver.

## Epic

For a finite initiative, look for:

- clear problem or opportunity;
- desired outcome;
- scope and important non-scope;
- measurable or otherwise observable success criteria;
- accountable business/product owner when relevant;
- key dependencies and constraints;
- enough context to decompose the work without losing intent.

Flag when:

- description is empty or links-only;
- the Epic appears to be only a persistent capability/work bucket;
- child work is active while the Epic conveys no useful initiative context;
- the Epic cannot answer what success looks like.

## Product Story

A Story should make clear:

- what behavior/outcome changes;
- who or what system benefits;
- why the change matters when not obvious;
- what observable conditions make it complete.

User-story syntax is optional. Do not rewrite a clear ticket merely to force `As a ... I want ... so that ...`.

Flag missing or ambiguous acceptance criteria when the work cannot be tested confidently.

## Engineering work

Prefer:

- **Objective**
- **Why**
- **Technical Context**
- **Completion Criteria**

Do not invent a fake end-user persona for infrastructure, observability, refactoring, security, migration, or platform work.

## Bug

Look for:

- **Observed behavior**
- **Expected behavior**
- **Reproduction / trigger**
- **Environment / scope**
- **Impact / severity**
- **Evidence** when useful

A screenshot alone is not sufficient if the problem cannot be understood without it.

## Spike

A Spike should state:

- question/decision to resolve;
- scope;
- expected output;
- completion or decision criteria;
- timebox when useful.

## Hierarchy and lifecycle

Warnings may include:

- active Story with no meaningful parent/context;
- child work in QA/review while parent initiative remains semantically untouched;
- due date already passed while work remains active;
- release scope without clear initiative grouping;
- parent is a generic catch-all bucket rather than the actual outcome being delivered.

## Intake normalization

Raw request forms, Slack transcripts, large payloads, copied email chains, and external-ticket dumps should be treated as source material, not automatically as the final Jira description.

Preserve evidence, but synthesize the actionable problem and expected outcome.

## Security

**Error:** likely plaintext credential, access token, API key, secret, or other sensitive authentication material is present in Jira content.

Do not echo the secret in the review. State the location generically and recommend removing/rotating as appropriate.

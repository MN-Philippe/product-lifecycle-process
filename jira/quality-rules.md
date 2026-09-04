# Jira Quality Rules

These rules guide agent reviews. They are not all hard gates, and they do not expand the scope of the scheduled AI Release Confidence job.

Use three severities:

- **Error** - missing information makes the work unsafe or not actionable.
- **Warning** - likely quality or lifecycle problem that deserves review.
- **Suggestion** - improvement that may make the ticket clearer or easier to deliver.

Read the canonical standards in `standards/` when reviewing Stories, Bugs, or lifecycle state.

## Epic

The organization's long-term Epic/capability model is still an open design question. Do not impose a new hierarchy policy yet.

For a finite initiative, it is still useful to look for:

- clear problem or opportunity;
- desired outcome;
- scope and important non-scope;
- measurable or otherwise observable success criteria;
- key dependencies and constraints;
- enough context to decompose the work without losing intent.

Flag obvious quality gaps such as an empty/links-only Epic or an initiative that cannot explain what success looks like, but do not automatically classify persistent capability/bucket Epics as invalid until the Epic model is formally decided.

## Story

The Jira Story Summary **must** use:

> **As a [specific actor], I want [clear behavior/capability], so that [clear outcome/value].**

Quality test:

> Can an ELT member understand who/what/why by reading the Summary alone?

Flag when:

- the Summary is not in the required format;
- `As a` is unnecessarily vague;
- `I want` does not make the actual behavior/capability clear;
- `So that` is generic filler rather than real user/business value;
- acceptance criteria are missing or too ambiguous to test confidently.

Acceptance criteria are required for Product Complete. Prefer Given / When / Then when it improves clarity, while allowing clear testable bullets when that is simpler.

See `standards/story-quality.md`.

## Business Requirements Complete

For work being prepared for commitment, PM should be able to assess the business requirement as complete and the business should approve it.

Look for, as applicable:

- problem / need;
- affected user/business group;
- current and desired behavior;
- business rules / constraints;
- scope and important exclusions;
- important scenarios/edge cases;
- dependencies / unresolved business decisions;
- observable success;
- business priority;
- business due date.

The business due date is not itself the delivery commitment. The Fix Version is the initial delivery commitment once Product + Engineering plan the work.

## Product Complete

Product Complete requires:

- clear acceptance criteria owned by Product/PM;
- QA test cases / validation coverage owned by QA;
- Product + QA agreement that the Story is sufficiently precise and testable.

If detailed definition materially changes the approved business requirement, route it back to the business rather than silently changing scope.

## Engineering review

Do not require a universal Technical Ready gate.

Suggest/flag Engineering review when architecture, permissions/security, integrations, data, deployment/migration, performance, feasibility, or another technical concern warrants explicit review.

## Engineering work / Task

For non-Story technical work, prefer a structure appropriate to the work, such as:

- **Objective**
- **Why**
- **Technical Context**
- **Completion Criteria**

The mandatory `As a / I want / So that` rule applies to Jira **Stories**, not every issue type.

## Bug

A reported problem must first be classified. It may be a true defect, feature request, missed requirement, configuration/data issue, reporting issue, misunderstanding, known issue, or still unclear.

For a standalone Bug, look for:

- **Observed behavior**;
- **Expected behavior**;
- **Reproduction / trigger** when possible;
- **Environment / affected scope**;
- **Impact**;
- **Evidence** when useful;
- relevant prior Story/requirement context when traceable;
- enough technical assessment to understand the intended fix scope and regression risk;
- QA verification approach.

A screenshot alone is not sufficient if the problem cannot be understood without guessing.

Dev + QA + PM jointly decide whether a defect found during Story delivery stays a Bug of Story or becomes a standalone Bug.

See `standards/bug-quality.md`.

## Spike

A Spike should state:

- question/decision to resolve;
- scope;
- expected output;
- completion or decision criteria;
- timebox when useful.

## Commitment and lifecycle

The normal delivery path is:

**Development -> Code Review -> QA in DEV -> Release Branch -> STG -> QA in STG -> Ready for Release -> Release**

QA owns Ready for Release. Business + PM own the release decision.

Sprint planning is the default entry into development, but expedited work may bypass normal gates when urgency warrants it. Treat skipped definition/validation as consciously accepted risk, not as the new standard.

A Fix Version is the delivery commitment. Moving it earlier is an expedite signal; moving it later is a delay/revised-commitment signal.

Material scope change after commitment is a signal to reassess, not an automatic release-risk downgrade.

## Intake normalization

Raw request forms, Slack transcripts, large payloads, copied email chains, and external-ticket dumps are source material, not automatically the final Jira description.

Capture legitimate requests early. Anyone may submit. Jira existence does not mean approval, priority, readiness, or commitment.

Preserve the requester's proposed solution as input, but identify the underlying need and challenge the solution when a better approach exists.

## Scheduled AI Release Confidence

The scheduled experiment has a strict scope boundary:

- **Story or standalone Bug**;
- **Fix Version is present**.

The scheduled agent owns only:

- **AI Release Confidence** (`On Track | Watch | At Risk`);
- **AI Release Confidence Reason**.

It reads but never edits **AI Release Confidence Feedback**.

Do not use these broader Jira quality rules as a reason to expand the daily scheduled scan to uncommitted items.

See `standards/ai-release-confidence.md`.

## Security

**Error:** likely plaintext credential, access token, API key, secret, or other sensitive authentication material is present in Jira content.

Do not echo the secret in the review. State the location generically and recommend removing/rotating as appropriate.

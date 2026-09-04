# Jira Context

## Primary projects

- `RAD` - Radius
- `MYM` - myMathnasium

Always query Jira live for current issues, field values, and history.

## Working interpretation

The boards currently contain a mix of finite initiatives, persistent capability buckets, product Stories, engineering work, Bugs, and Spikes. Do not assume that an existing issue type or parent relationship proves the semantic role of an item.

A recurring agent responsibility is to understand what an item is intended to represent from its live context without inventing a hierarchy redesign that has not been agreed.

## Core hierarchy

The common practical hierarchy is:

`Epic -> Story / Task / Bug -> Sub-task`

Some existing work does not follow this consistently. Evaluate hierarchy/context gaps when relevant, but the long-term Epic vs persistent-capability model is still an open design question.

Do not enforce a new Epic taxonomy yet.

## Workflow interpretation

Issue status must be read live. Parent status is not currently guaranteed to roll up coherently from children, so never infer initiative health from Epic status alone. Inspect child work and release metadata when evaluating progress.

## Release metadata

**Fix Version is the delivery commitment** once Product + Engineering have planned the work.

Distinguish it from the business due date:

- **business due date** = when the business wants/needs the outcome;
- **Fix Version** = the delivery team's current release commitment.

A Fix Version change is meaningful history:

- moved earlier -> expedite / compressed delivery window;
- moved later -> delay / revised commitment.

Use Jira field changelog/history to preserve and interpret commitment changes rather than copying them into Git.

## AI Release Confidence fields

The initial experiment uses three Jira fields:

- **AI Release Confidence** - AI-owned: `On Track | Watch | At Risk`;
- **AI Release Confidence Reason** - AI-owned concise rationale;
- **AI Release Confidence Feedback** - human-owned persistent context, read but never edited by the agent.

The scheduled early-morning scan assesses only Stories and standalone Bugs that have a Fix Version.

See `standards/ai-release-confidence.md`.

## Security hygiene

Jira descriptions can contain raw intake, screenshots, payloads, environment details, and occasionally credential-like data. Agents must avoid reproducing secrets and should flag likely credentials/tokens/passwords for remediation.

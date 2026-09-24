# Jira Context

## Primary projects

- `RAD` - Radius
- `MYM` - myMathnasium

Jira site: `https://mathnasium.atlassian.net`

Always query Jira live for current issues, field values, and history.

Whenever a Jira item is mentioned in user-facing output, make its visible Jira key a hyperlink to the live issue. Prefer the connector-provided `webUrl`; otherwise use `https://mathnasium.atlassian.net/browse/<JIRA-KEY>` after confirming the key is valid. In tables, documents, and slide decks, keep the short key visible and make it clickable instead of showing the long URL.

## Working interpretation

The boards currently contain a mix of finite initiatives, persistent capability buckets, product Stories, engineering work, Bugs, and Spikes. Do not assume that an existing issue type or parent relationship proves the semantic role of an item.

A recurring agent responsibility is to understand what an item is intended to represent from its live context without inventing a hierarchy redesign that has not been agreed.

## Core hierarchy

The common practical hierarchy is:

`Epic -> Story / Task / Bug -> Sub-task`

Some existing work does not follow this consistently. Evaluate hierarchy/context gaps when relevant, but the long-term Epic vs persistent-capability model is still an open design question.

Do not enforce a new Epic taxonomy yet.

One specific Bug rule is already decided: standalone Bugs should be categorized under the product area, feature, or initiative they impact rather than under a generic **Bug Fixing** Epic. This rule does not otherwise settle the broader Epic/capability taxonomy.

## Multi-repository product work

Jira project boundaries do not necessarily match implementation-repository boundaries.

In particular, **MYM is a product/project grouping, not a single code repository**. One MYM Epic or capability may require coordinated work in Radius, Scheduling, Guardian Portal, or another repository.

Working rule:

- keep the parent Epic/capability focused on the end-to-end product outcome;
- identify coherent product behaviors before repository implementation slices;
- keep shared product behavior at the Story level and use repository-bounded Tasks/Sub-tasks for implementation-only work when practical;
- create separate repository-bounded Stories only when each repository owns distinct product behavior with meaningful acceptance criteria;
- when a Story itself is repository-owned, begin its Summary with the owning repository in square brackets, for example `[Radius]`, `[Scheduling]`, or `[Guardian Portal]`;
- do not infer implementation ownership from the Jira project key alone;
- inspect linked PRs/code when the repository is unclear.

See `standards/story-quality.md`.

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

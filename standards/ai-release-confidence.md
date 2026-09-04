# AI Release Confidence Standard

This document defines the initial AI delivery-risk experiment. Keep it deliberately narrow so the signal can be evaluated before expanding the automation.

## Scope

The daily AI assessment scans **only Jira Stories and standalone Bugs that have a Fix Version**.

- Story + Fix Version -> assess.
- Standalone Bug + Fix Version -> assess.
- No Fix Version -> do not assess; leave AI release-confidence fields blank.
- Bug of Story -> rides with the parent Story unless Dev + QA + PM promote it to a standalone Bug.

The Fix Version is the delivery commitment, so it is the boundary that makes release-confidence assessment meaningful.

Do not turn this experiment into a general Jira hygiene scanner. Broader quality standards can exist in this repository, but the scheduled release-confidence automation remains limited to committed Stories and Bugs.

## Jira fields

### AI Release Confidence

AI-owned field with exactly three states:

- **On Track** - current evidence supports that the committed release is reasonably achievable.
- **Watch** - meaningful evidence has weakened confidence, but there is still a credible path to hit the commitment without major intervention.
- **At Risk** - hitting the commitment appears unlikely without intervention, scope change, reprioritization, or an unusually favorable outcome.

Humans should not manually maintain this field during the experiment.

### AI Release Confidence Reason

AI-owned short text field explaining the few strongest signals behind the current assessment.

The Reason should:

- be concise;
- be evidence-based;
- explain why the current confidence level makes sense;
- mention meaningful recent changes when they materially affect interpretation;
- avoid dumping every metric or weak signal;
- never expose credentials/secrets.

Example:

> Watch: 9 days to release, development has not started, and the dependent API work is still in code review.

Humans should not manually maintain this field during the experiment.

### AI Release Confidence Feedback

Human-owned persistent context for the AI.

Use it when a human believes the AI assessment is wrong, incomplete, or missing important context.

The agent:

- reads this field on every daily assessment;
- treats it as evidence rather than an automatic override;
- **never edits or clears it**.

The feedback remains until a human changes or removes it.

## Cadence

Run the assessment on a **fixed daily cadence, early morning**.

Do not add event-driven or intraday reassessment yet. The goal is a stable, understandable experiment with a fresh signal available at the start of each workday.

## Evidence model

Release Confidence is a synthesis, not a formula based on one Jira field.

Use all relevant available evidence, including when accessible:

- time remaining until the committed release;
- sprint assignment and sprint progress;
- Jira workflow/status;
- estimate / size;
- remaining scope;
- milestones and planned dates;
- PR and code-review state;
- QA in DEV progress/results;
- release-branch / STG progress;
- QA in STG, regression, and integration results;
- blockers and dependencies;
- Product Complete/readiness context;
- engineering-review flags and technical uncertainty;
- recent scope/acceptance-criteria changes;
- Fix Version changes;
- historical throughput/cycle-time patterns when available;
- team/engineering judgment or relevant current discussion when available;
- AI Release Confidence Feedback.

**Proximity to release is a major weighting factor.** The same status or remaining work can be healthy far from release and concerning close to release.

Do not create warnings merely because a single weak signal exists. The objective is to surface meaningful risk early enough to act without warning on everything all the time.

## Confidence changes

The agent must be able to move confidence both down and back up as evidence changes.

Examples:

- On Track -> Watch when confidence materially weakens but recovery remains credible.
- Watch -> At Risk when the current commitment becomes unlikely without intervention.
- At Risk -> Watch or On Track when blockers clear, work progresses, scope changes, or the commitment is revised and the new evidence supports recovery.

## Fix Version changes

A Fix Version change is a first-class signal because it changes the delivery commitment.

### Moved earlier

Treat this as an **expedite / compressed delivery window**. Reassess whether the earlier commitment remains credible and note the change in the Reason when material.

### Moved later

Treat this as a **delay / revised commitment**. Where evidence allows, distinguish whether the delay appears driven by:

- the item itself not being ready;
- another higher-priority item displacing it;
- capacity;
- dependencies;
- another legitimate delivery tradeoff.

Do not automatically keep the item At Risk forever after a delay. Confidence is always against the **current** Fix Version. Preserve the prior commitment change through Jira history and mention it in the current Reason when useful.

Example:

> On Track: moved from September to October after higher-priority work displaced capacity; current progress supports the revised October commitment.

## Scope and requirement changes

A material change after commitment is a signal, not an automatic confidence downgrade.

Consider:

- size of the change;
- time remaining;
- whether development has started;
- whether completed work must be redone;
- whether dependencies or estimates changed;
- whether the team still has a credible path to the current Fix Version.

A notable change may be mentioned in the Reason even while confidence remains On Track.

## History / changelog

Use Jira's issue field changelog/history as the source for critical change history, including at minimum:

- Fix Version changes;
- AI Release Confidence changes;
- AI Release Confidence Reason changes;
- AI Release Confidence Feedback changes.

Do **not** maintain a parallel append-only history in Git.

Do not add another Jira change-log field unless the actual Jira integration proves the changelog API insufficient for this use case.

Avoid polluting the changelog: the agent should not rewrite semantically equivalent Confidence/Reason values every morning simply to prove that the job ran. Write only when the assessment or material rationale changes.

## Experiment evaluation

After releases, use the history to evaluate whether the AI is useful. Useful measures include:

- whether missed items were flagged at all;
- how many days before release the first meaningful warning appeared;
- whether Watch and At Risk transitions were appropriately timed;
- false-alarm rate for items that delivered normally;
- whether the stated Reason identified the signal that actually drove the miss or recovery;
- whether human Feedback improved subsequent assessment quality.

Use these results to tune the assessment before expanding its scope.

## Explicitly out of scope

For this project/experiment, do not yet implement:

- automatic Epic-level confidence;
- automatic release-level confidence;
- a worst-item rollup rule;
- the final Google Sheet release dashboard;
- release aggregation/scoring logic;
- a broad automated Jira hygiene scan.

The dashboard can pull granular Jira fields and be designed separately. Revisit aggregation/automation after seeing which item-level signals prove useful.

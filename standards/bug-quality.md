# Bug Quality and Triage Standard

Bugs are a major product-quality input, but a reported problem should not automatically be accepted as a Bug without triage.

## 1. Bugs can come from anywhere

Potential Bugs may be surfaced through:

- Support escalations;
- Engineering;
- QA;
- Product/PM;
- business users;
- franchisees/customers;
- monitoring or other operational signals.

The source does not determine whether the item is actually a Bug.

## 2. Classify before committing to the fix

First determine what the report actually represents.

It may be:

- a true defect/regression;
- a feature request;
- a missed or incomplete requirement;
- expected behavior that is misunderstood;
- a configuration/data issue;
- a reporting issue;
- another previously known issue;
- still unclear and requiring investigation.

Search prior Jira work and requirements when useful. Where possible, trace a true defect back to the Story, requirement, release, or behavior it violates.

## 3. Watchlist Bugs

A **Watchlist Bug** is an active triage state for a reported defect that is worth tracking, but is not yet ready for a delivery commitment. This is commonly appropriate when the evidence is credible but reproduction, scope, trigger conditions, or technical understanding are still incomplete.

The Jira source of truth is:

- **Confirmed Issue = Watchlist issue**;
- **Fix Version is normally empty**.

A Watchlist Bug is not merely a parking lot. Keep enough current evidence on the issue to make the next review useful, including as applicable:

- known production examples / support cases;
- observed and expected behavior;
- logs, screenshots, or data evidence;
- current hypothesis or suspected trigger;
- what is still missing or unknown;
- a workaround, if one exists;
- the evidence or event that should cause the issue to be reviewed again.

When the evidence is sufficient to treat the item as an actionable defect, change **Confirmed Issue** from **Watchlist issue** to **Confirmed issue** and prioritize it normally. Add a Fix Version only when delivery is actually committed.

A Bug that is still marked **Watchlist issue** but has a Fix Version should be treated as an inconsistent state unless it is intentionally in transition. Once a Fix Version is assigned, it is a delivery commitment and should leave the Watchlist state.

Do not confuse Jira's **Watchlist issue** state with **AI Release Confidence = Watch**. They are different concepts:

- **Watchlist issue** = pre-commitment Bug triage / observation;
- **AI Release Confidence = Watch** = delivery risk on an already committed Story or standalone Bug with a Fix Version.

## 4. Functional triage

A useful Bug should make the issue understandable and investigable.

Capture as applicable:

- **Observed behavior**;
- **Expected behavior**;
- **Steps to reproduce / trigger**, when reproducible;
- **Environment and affected scope**;
- **Impact**;
- **Evidence**, such as logs/screenshots/data examples, when useful;
- relevant prior work or requirement context.

A screenshot by itself is not a complete Bug if the issue cannot be understood without guessing.

## 5. Technical assessment

Before treating a standalone Bug as ready, Dev + QA + PM should understand enough of the technical scope to avoid making a narrow patch that breaks something else.

Assess as appropriate:

- likely affected system/component;
- exact scope of the intended fix;
- adjacent behavior that must not regress;
- underlying cause versus visible symptom;
- relevant architecture/integration/data implications;
- how the fix will be verified;
- whether a broader/correct fix is preferable to a local workaround.

The goal is not to require perfect root-cause analysis before work starts. The goal is to **fix the right problem in the right way with a conscious understanding of regression risk**.

## 6. Prioritization

Once ready:

- routine Bugs may be prioritized directly by the delivery team;
- important Bugs should increasingly be brought into sprint planning alongside Stories;
- urgent Bugs may use the expedite path;
- Bugs with meaningful business/customer impact or leadership visibility may need the same business prioritization treatment as Stories, including business priority and due date when meaningful.

A standalone Bug with a Fix Version is a delivery commitment and follows the same release-confidence and delivery rules as a committed Story.

## 7. Bug of Story

A defect discovered while a Story is still being developed or validated will normally remain a **Bug of Story**, tied to the parent Story and riding the parent Story's delivery path.

Dev + QA + PM jointly decide when it should instead become a standalone Bug.

Promote it when, for example, it is:

- materially broader than the parent Story;
- significantly larger than reasonably completing the Story;
- architecturally distinct;
- affecting existing functionality beyond the Story;
- not reasonable to complete within the Story's current release path.

Do not split defects away merely to make the parent Story appear complete while known Story-related defects remain unresolved.

## 8. Delivery pipeline

Standalone Bugs use the same normal delivery pipeline as Stories:

**Development -> Code Review -> QA in DEV -> Release Branch -> STG -> QA in STG -> Ready for Release -> Release**

QA owns Ready for Release. Business + PM own the release decision.

## 9. Secrets and sensitive content

Do not place passwords, tokens, API keys, or other authentication secrets in Bug descriptions, comments, or evidence.

If detected, do not echo the value. Flag it generically and recommend removal/rotation as appropriate.

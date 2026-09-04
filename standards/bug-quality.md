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

## 3. Functional triage

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

## 4. Technical assessment

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

## 5. Prioritization

Once ready:

- routine Bugs may be prioritized directly by the delivery team;
- important Bugs should increasingly be brought into sprint planning alongside Stories;
- urgent Bugs may use the expedite path;
- Bugs with meaningful business/customer impact or leadership visibility may need the same business prioritization treatment as Stories, including business priority and due date when meaningful.

A standalone Bug with a Fix Version is a delivery commitment and follows the same release-confidence and delivery rules as a committed Story.

## 6. Bug of Story

A defect discovered while a Story is still being developed or validated will normally remain a **Bug of Story**, tied to the parent Story and riding the parent Story's delivery path.

Dev + QA + PM jointly decide when it should instead become a standalone Bug.

Promote it when, for example, it is:

- materially broader than the parent Story;
- significantly larger than reasonably completing the Story;
- architecturally distinct;
- affecting existing functionality beyond the Story;
- not reasonable to complete within the Story's current release path.

Do not split defects away merely to make the parent Story appear complete while known Story-related defects remain unresolved.

## 7. Delivery pipeline

Standalone Bugs use the same normal delivery pipeline as Stories:

**Development -> Code Review -> QA in DEV -> Release Branch -> STG -> QA in STG -> Ready for Release -> Release**

QA owns Ready for Release. Business + PM own the release decision.

## 8. Secrets and sensitive content

Do not place passwords, tokens, API keys, or other authentication secrets in Bug descriptions, comments, or evidence.

If detected, do not echo the value. Flag it generically and recommend removal/rotation as appropriate.

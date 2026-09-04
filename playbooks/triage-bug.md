# Playbook: Triage a Bug

## Goal

Turn a reported symptom into the correct work item, understand the safest fix scope, and avoid treating every report as a standalone Bug by default.

Read `standards/bug-quality.md` first.

## Steps

1. Fetch the report/Bug live and inspect relevant comments, parent Story, prior requirements, and related work when useful.
2. Classify the report before prescribing a fix. Determine whether it is:
   - a true defect/regression;
   - a feature request;
   - a missed/incomplete requirement;
   - expected behavior / misunderstanding;
   - configuration/data/reporting issue;
   - duplicate/known issue;
   - still unclear.
3. Trace a true defect back to prior Story/requirement/release context when possible.
4. Identify observed behavior, expected behavior, reproduction/trigger, environment, impact, and evidence.
5. Search Jira for related/duplicate work.
6. Inspect relevant implementation repositories when technical context materially improves triage.
7. With Dev + QA + PM, assess the likely fix scope and adjacent regression risk:
   - what should change;
   - what should not change;
   - underlying cause vs visible symptom;
   - broader architecture/integration/data implications;
   - how QA will verify the fix.
8. If the defect was found while delivering a Story, decide jointly whether it should remain a Bug of Story or become a standalone Bug.
9. For a ready standalone Bug, recommend prioritization treatment:
   - routine team prioritization;
   - sprint-planning visibility;
   - business prioritization when impact/visibility warrants it;
   - expedite when urgency warrants it.
10. If a Fix Version is assigned, treat it as a delivery commitment and apply the same delivery/release-confidence rules as a committed Story.
11. Flag credential/secret-like content without repeating it.

## Output

- **Classification**
- **Traceability to prior work/requirement**
- **Observed vs expected**
- **Repro confidence**
- **Impact / affected scope**
- **Technical fix-scope / regression concerns**
- **QA verification needs**
- **Bug of Story vs standalone recommendation**
- **Prioritization recommendation**
- **Recommended Jira changes**

Do not turn implementation guesses into facts. Do not split a Story-related defect into future work merely to make the parent Story appear complete.

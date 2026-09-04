# Product Lifecycle Standard

This document captures the current operating standard for product work across the RAD and MYM Jira boards. It is intentionally practical: define the normal path, keep room for judgment, and make exceptions explicit rather than pretending they do not happen.

## Governing principles

1. **Capture freely.** Jira is an intake system as well as a delivery system. Anyone may submit a legitimate request, including through automated/request-form intake.
2. **Existence is not commitment.** A Jira item is not approved, prioritized, or committed simply because it exists.
3. **Clarify before committing.** Business intent should be complete and approved before Product + Engineering make a normal delivery commitment.
4. **Respect the request, challenge the solution.** Preserve what the requester asked for, understand the underlying need, and recommend a better solution when the proposed one is not optimal.
5. **Keep ownership clear.** PM owns requirement quality and process facilitation. Business owns business approval, priority, and requested due date. Product + Engineering jointly own the initial delivery commitment. QA owns release readiness. Business + PM own the release decision.
6. **Stay flexible without lowering the bar silently.** The normal process can be expedited or adapted when urgency warrants it, but skipped gates and accepted risk must be conscious and visible.
7. **Use AI to absorb repetitive synthesis, not business judgment.** AI can continuously assess delivery evidence; humans retain prioritization, approval, tradeoff, and release decisions.

## 1. Intake

Anyone may create a Jira request. Intake can come from business teams, Support, Engineering, QA, leadership, franchisees, forms, or other legitimate channels.

At intake:

- capture the request early;
- do not assume the submitted classification or proposed solution is correct;
- search for duplicate, related, or prior work;
- identify the underlying problem and intended outcome;
- preserve useful source evidence, but normalize it into actionable Jira content rather than leaving raw forms, email chains, screenshots, or payloads as the final definition.

## 2. Business Requirements Complete

**Business Requirements Complete** means the business need is understood well enough that Product and Engineering should not have to guess what the business wants.

PM assesses completeness. The business approves it.

The requirement package should cover, as applicable:

- problem / need;
- who is affected;
- current behavior;
- desired behavior / outcome;
- requested solution, when one was proposed;
- Product recommendation when a better solution exists;
- business rules and constraints;
- scope;
- meaningful exclusions;
- important happy-path, sad-path, and edge scenarios;
- dependencies or unresolved business decisions;
- observable success / expected outcome.

Before normal commitment, the business must also provide:

- **business priority**;
- **business due date**.

The business due date is when the business wants or needs the outcome. It is not, by itself, an Engineering delivery commitment.

## 3. Prioritization and delivery commitment

Once Business Requirements are Complete, the work can be properly prioritized and planned.

Product + Engineering jointly assign the **Target Release / Fix Version** based on:

- business priority;
- business due date;
- scope and complexity;
- actual team capacity and delivery reality;
- competing commitments and dependencies.

**The Fix Version is the initial delivery commitment.**

If Product + Engineering cannot resolve competing priorities or the required tradeoff crosses business functions, escalate to ELT.

## 4. Product Complete

After business requirements are approved and the work is planned, the work must become **Product Complete** before normal development.

Product Complete means the approved business requirement has been translated into precise, testable product behavior.

Ownership:

- PM/Product owns acceptance criteria and detailed product behavior;
- QA owns QA test cases / validation coverage;
- Product + QA together determine Product Complete.

The business does not need to approve every detailed acceptance criterion. If the detailed work materially changes the previously approved business requirement, route the change back to the business for approval.

## 5. Conditional Engineering review

There is no universal additional "Technical Ready" gate.

A Story may be flagged for Engineering review when technical assessment is warranted, such as:

- architecture/design uncertainty;
- permissions or security implications;
- integration or data concerns;
- migration/deployment complexity;
- performance/scale risk;
- technical feasibility uncertainty;
- important cross-system dependencies.

If Engineering review materially changes product behavior or business scope, route the impact back through Product and, when needed, the business.

## 6. Planning and expedite path

Sprint planning is the default entry point into development.

Anyone may initiate an expedite after giving the delivery team a heads up. Expedited work may bypass normal readiness gates when urgency genuinely warrants it.

When bypassing normal gates, be deliberate about:

- what definition or validation is missing;
- what risk is being accepted;
- what planned work may be displaced;
- what follow-up is required to close the gap.

**Expedite bypasses normal scheduling; it does not make quality concerns disappear.**

## 7. Normal delivery pipeline

The normal delivery path is:

**Development -> Code Review -> QA in DEV -> Release Branch -> STG -> QA in STG -> Ready for Release -> Release**

### QA in DEV

Validate the individual change against its acceptance criteria and intended behavior.

### QA in STG

Validate the integrated release, including as appropriate:

- automated regression;
- integration testing;
- targeted validation of changed behavior.

### Ready for Release

QA owns the **Ready for Release** gate.

QA determines whether the release has passed the expected validation and is fit to move forward.

### Release decision

Once QA has declared the release ready, **Business + PM own the decision to release**. Engineering executes the deployment.

## 8. Post-release validation

Current post-release validation is relatively light and relies heavily on business testing and users surfacing defects.

The desired principle is stronger:

> Released is not automatically equivalent to fully validated. Production verification should be proportionate to risk.

There is not yet a formal risk-classification framework. PM, Engineering, and QA should use judgment. Do not invent a mandatory risk matrix until the organization has agreed on one.

## 9. Commitment changes and delivery risk

Delivery risk should be surfaced early enough to act, without creating constant low-value warnings.

Product and Engineering should work hand in hand with the business when a commitment is weakening and escalate to ELT when the required tradeoff cannot be resolved within the team.

A Fix Version change is a first-class delivery signal:

- **moved earlier** = expedite / compressed delivery window;
- **moved later** = delay / revised commitment.

A delay may be caused by the item itself, another higher-priority item, capacity, dependencies, or another legitimate tradeoff. The history should preserve the fact that the commitment changed even if the item is now On Track against the revised commitment.

Material scope changes after commitment are also meaningful signals, but **scope change is a signal, not an automatic risk increase**. Assess the size, timing, rework, dependencies, and remaining delivery window in context.

## 10. Open questions not yet standardized

The following areas are intentionally unresolved and should not be turned into hard rules yet:

- whether persistent capability/product-area buckets should continue to be modeled as Epics;
- how Story/Bug confidence should aggregate into Epic- or release-level confidence;
- the final Google Sheet / release-dashboard model;
- a formal delivery-risk classification framework;
- stronger automated post-release verification.

Document experiments and observations, but do not prematurely codify these as policy.

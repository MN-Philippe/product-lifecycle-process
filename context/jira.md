# Jira Context

## Primary projects

- `RAD` - Radius
- `MYM` - myMathnasium

Always query Jira live for current issues and metadata.

## Working interpretation

The boards currently contain a mix of finite initiatives, persistent capability buckets, product Stories, engineering work, Bugs, and Spikes. Do not assume that an existing issue type or parent relationship proves the semantic role of an item.

A recurring agent responsibility is to distinguish what an item *is intended to represent* from how Jira happens to classify it today.

## Core hierarchy

The common practical hierarchy is:

`Epic -> Story / Task / Bug -> Sub-task`

Some existing work does not follow this consistently. Treat hierarchy gaps as something to evaluate, not automatically as an error: standalone work can be legitimate, but meaningful delivery work should still have enough context to explain what outcome it contributes to.

## Epic interpretation

Before reviewing an Epic, classify it as one of:

1. **Finite initiative** - a bounded outcome that can eventually be completed.
2. **Persistent capability/work bucket** - an ongoing area such as a product capability, system-hardening stream, generic bug bucket, or other non-finite grouping.
3. **Unclear/misclassified** - insufficient information to determine the intended role.

Do not require a persistent capability bucket to satisfy every finite-initiative rule. Instead, flag the semantic mismatch and recommend a cleaner classification/model when useful.

## Workflow interpretation

Issue status must be read live. Parent status is not currently guaranteed to roll up coherently from children, so never infer initiative health from Epic status alone. Inspect child work and release metadata when evaluating progress.

## Release metadata

Fix versions are meaningful delivery signals, especially at Story/Bug level. Use them when reviewing release scope, but do not assume that an Epic's metadata is complete or authoritative without examining its children.

## Security hygiene

Jira descriptions can contain raw intake, screenshots, payloads, environment details, and occasionally credential-like data. Agents must avoid reproducing secrets and should flag likely credentials/tokens/passwords for remediation.

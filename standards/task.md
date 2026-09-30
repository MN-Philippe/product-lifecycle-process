# Task and Spike Standard

Technical work with no product-observable behavior is a **Task**, never a Story with a Developer persona. Work with observable behavior is a Story (`standards/story.md`).

## Task

- **Summary:** `[Repo] Verb + object`. Example: *[Scheduling] Add OTLP metrics to the Fanout service*. The repo bracket is optional, as for Stories, and comes from the repo list in `standards/jira-conventions.md`.
- **Description:** Objective / Why / Done when.
- **Size:** 5 points maximum.
- **Fields:** the same Pull Requests and Code Dependency rules as Stories. Ownership of Tasks in MYM sits with the vendor (`templates/vendor-guide.md`).
- A Task belongs to an Epic. It does not need acceptance criteria; "Done when" replaces them.

The copy-paste version is `templates/task.md`.

## Spike

- Uses the **Spike** issue type, never a `[SPIKE]` bracket.
- **Description:** question to answer / scope / expected output / timebox.
- A Spike ends with a written answer or decision, not code to ship.

## Checks

Used by `tools/jira_helper.py`. Both rules respect the effective date in `standards/story.md#applies-to`.

| Rule | Severity | Auto |
| --- | --- | --- |
| Description empty or near-empty | Error | Yes |
| No "Done when" (Task) or no question/expected output (Spike) | Warning | Yes |
| More than one bracket, or bracket not in the repo list | Error | Yes |
| `[SPIKE]` or `[PoC]` bracket on any issue type | Error | Yes |
| Story Points over 5 with a committed Fix Version | Error | Yes |

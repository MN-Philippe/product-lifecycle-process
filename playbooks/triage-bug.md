# Playbook: Triage a Bug

## Goal

Turn a reported symptom into a useful, investigable Jira Bug without losing evidence or prematurely prescribing a solution.

## Steps

1. Fetch the Bug live and inspect relevant comments/parent context when needed.
2. Identify observed behavior, expected behavior, reproduction/trigger, environment, impact, and evidence.
3. Separate source material from the synthesized problem statement.
4. Determine whether the item is actually a defect, a feature request, a reporting issue, a business-process misunderstanding, or still unclear.
5. Search Jira for related/duplicate work when useful.
6. Inspect relevant implementation repositories when technical context materially improves triage.
7. Flag credential/secret-like content without repeating it.
8. Recommend missing information, classification, priority considerations, and parent/link relationships.

## Output

- **Classification**
- **Observed vs expected**
- **Repro confidence**
- **Impact**
- **Related work**
- **Missing investigation context**
- **Recommended Jira changes**

Do not turn implementation guesses into acceptance criteria unless supported by evidence.

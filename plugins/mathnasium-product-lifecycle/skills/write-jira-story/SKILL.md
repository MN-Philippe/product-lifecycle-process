---
name: write-jira-story
description: Write, refine, split and ready-check Jira Stories for the RAD and MYM projects. Use when asked to "write a story for…", "draft a story", "refine MYM-123", "split this story", "is MYM-123 ready for dev", or "review this story".
---

# Write Jira Stories

Pick the mode from the request, then follow its playbook step by step.

| Mode | When | Playbook |
| --- | --- | --- |
| Write | "write a story for…", "draft a story" | [references/write-story.md](references/write-story.md) |
| Refine | "refine MYM-123", new answers to fold in | [references/refine-story.md](references/refine-story.md) |
| Split | "split this story", estimate over 5 points, several repos | [references/split-story.md](references/split-story.md) |
| Ready check | "is MYM-123 ready for dev" | [references/ready-check.md](references/ready-check.md) |

"Review this story" audits an existing Story: [references/review-story.md](references/review-story.md).

## Ground rules

- Jira is the live truth. Fetch before concluding; never rely on memory of a ticket.
- Propose before writing. Change Jira only after the user approves the draft.
- Link every Jira key to `https://mathnasium.atlassian.net/browse/<KEY>`.
- Never copy secrets or credentials into Jira content.

The rules live in [references/story.md](references/story.md); follow it wherever this file is less specific.

---
name: write-jira-story
description: Write, refine, split, decompose and ready-check Jira Stories for the RAD and MYM projects. Use when asked to "write a story for…", "draft a story", "refine MYM-123", "improve the acceptance criteria", "split this story", "decompose this epic", "write stories for this BRD", "turn this into Jira stories", "is MYM-123 ready for dev", "is this story ready", or "review this story", or when given a raw request form, email or Slack thread to turn into work.
---

# Write Jira Stories

Pick the mode from the request, then follow its playbook step by step.

| Mode | When | Playbook |
| --- | --- | --- |
| Write | "write a story for…", "draft a story" | [references/write-story.md](references/write-story.md) |
| Refine | "refine MYM-123", "improve the acceptance criteria", new answers to fold in | [references/refine-story.md](references/refine-story.md) |
| Split | "split this story", estimate over 5 points, several repos | [references/split-story.md](references/split-story.md) |
| Decompose | "decompose this epic", "write stories for this BRD", "turn this into Jira stories" | [references/decompose-initiative.md](references/decompose-initiative.md) |
| Intake | raw request forms, emails, Slack threads | [references/intake.md](references/intake.md) |
| Ready check | "is MYM-123 ready for dev", "is this story ready" | [references/ready-check.md](references/ready-check.md) |

"Review this story" audits an existing Story: [references/review-story.md](references/review-story.md).

## Ground rules

- Jira is the live truth. Fetch before concluding; never rely on memory of a ticket.
- **GitHub issues and PRs are read-only, and Jira writes follow draft, approve, then write.** Full rule: [references/jira-conventions.md](references/jira-conventions.md#write-policy). A hook in this plugin enforces it.
- Link every Jira key to `https://mathnasium.atlassian.net/browse/<KEY>`.
- Never copy secrets or credentials into Jira content.
- Jira site, cloudId and field IDs: [references/jira-conventions.md](references/jira-conventions.md).

The rules live in [references/story.md](references/story.md); follow it wherever this file is less specific.

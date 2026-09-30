# Vendor Guide (MYM)

One page for the MYM vendor team. The full rules are in [`standards/story.md`](../standards/story.md); this page says who does what.

## Who owns what

| Mathnasium PM | Vendor |
| --- | --- |
| Story Summary | Tasks and delivery-workflow sub-tasks |
| Acceptance criteria (ACs) | Estimates (Story Points) |
| AC approval | Pull Requests field |

The standard applies to every ticket, whoever writes it.

## Working rules

1. **Questions go in a comment, numbered** (Q1, Q2…). The PM folds the answer into the description and replies "Description updated (AC4)". Don't rely on a comment as the requirement.
2. **A Story is 5 points or less.** If your estimate is higher, say so in a comment; the PM splits it.
3. **Decompose Stories by behavior first, then repo.** Meaningful user actions/inputs and distinct system responses are normally separate Story candidates; a repo may have several Stories for one feature. Do not fragment tightly coupled behavior just to increase ticket count. Production implementation never belongs in a sub-task. Workflow sub-tasks are appropriate for QA automation, test setup/data, pre/post-deployment steps, release/runbook work or coordination when separate tracking helps.
4. **Record every PR in the Pull Requests field**, not only in a comment.
5. **Implementation ideas go in the PR or a comment marked "non-binding", not in the description.** The description holds behavior (ACs) and non-negotiable constraints with their reason.
6. **Set Code Dependency** to every repo the ticket touches. More than one value means the Story probably needs splitting.

## Before you start work

The Story must be Ready for Dev: [`standards/lifecycle.md`](../standards/lifecycle.md#ready-for-dev-checklist). If something is missing, ask; don't guess.

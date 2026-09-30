# Vendor Guide (MYM)

One page for the MYM vendor team. The full rules are in [`standards/story.md`](../standards/story.md); this page says who does what.

## Who owns what

| Mathnasium PM | Vendor |
| --- | --- |
| Story Summary | Tasks |
| Acceptance criteria (ACs) | Estimates (Story Points) |
| AC approval | Pull Requests field |

The standard applies to every ticket, whoever writes it.

## Working rules

1. **Questions go in a comment, numbered** (Q1, Q2…). The PM folds the answer into the description and replies "Description updated (AC4)". Don't rely on a comment as the requirement.
2. **A Story is 5 points or less.** If your estimate is higher, say so in a comment; the PM splits it.
3. **One Story per repo, and no sub-tasks for implementation steps.** A step list you want to track goes in the description as a checklist, or in the PR.
4. **Record every PR in the Pull Requests field**, not only in a comment.
5. **Implementation ideas go in the PR or a comment marked "non-binding", not in the description.** The description holds behavior (ACs) and non-negotiable constraints with their reason.
6. **Set Code Dependency** to every repo the ticket touches. More than one value means the Story probably needs splitting.

## Before you start work

The Story must be Ready for Dev: [`standards/lifecycle.md`](../standards/lifecycle.md#ready-for-dev-checklist). If something is missing, ask; don't guess.

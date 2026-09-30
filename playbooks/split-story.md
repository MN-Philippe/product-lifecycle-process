# Playbook: Split a Story

Read: [`standards/story.md`](../standards/story.md), [`standards/jira-conventions.md`](../standards/jira-conventions.md)

Use when an estimate is over 5 points or the scope spans repos.

## Steps

1. Propose the split along the seams in `standards/story.md#size`.
2. Give one Story per repo for multi-repo work, linked with "blocks" where order matters.
3. Move each AC to the Story it belongs to.
4. Show the proposed Stories before creating them.
5. If the original Story has comments, PRs or history, **keep its key for the first piece** and create new Stories only for the rest.
6. Retire the original per `playbooks/cleanup.md` only if no piece remains.

# Playbook: Refine a Story

Read: [`standards/story.md`](../standards/story.md)

Fold new answers (from the PM, comments or the vendor) into the description.

## Steps

1. Fetch the Story live, including comments, and the current description.
2. Move answered Open questions into ACs or Constraints.
3. Change only what changed.
4. Flag any comment that contradicts the description.
5. After AC approval, add a Changelog line for every AC change.
6. Show a before/after and wait for approval (`standards/jira-conventions.md#write-policy`).
7. After writing, and with the PM's approval, post a reply comment "Description updated (ACn)" so the person who asked sees their question was folded in.
8. Re-run `playbooks/ready-check.md`.
9. If an answer pushes the estimate over 5 points, hand off to `playbooks/split-story.md`.
10. If a Fix Version is set and an AC changed, note that a release-confidence recheck applies.

# Playbook: Write a Story

Read: [`standards/story.md`](../standards/story.md), [`standards/jira-conventions.md`](../standards/jira-conventions.md), [`templates/story.md`](../templates/story.md)

The PM gives a plain request ("write a story for…"). Run a short Q&A, draft, and write to Jira only after approval.

## Principle

**Never invent behavior.** Anything the PM did not state and Jira does not show becomes an Open question, not an AC.

## Steps

1. **Look things up first.** Search Jira live for the Epic, related Stories and duplicates. If a duplicate exists, offer to rewrite it (`playbooks/refine-story.md`) instead of creating a new Story. Never ask the PM something Jira can answer. If no suitable Epic exists, add an Open question proposing one. If the request clearly spans several repos, draft **one Story per repo under the Epic from the start** (`playbooks/split-story.md`), rather than flagging a split later.
2. **Ask one round of 3–5 questions**, only about gaps that change what gets built, tested or split. Offer options and a default for each question. Use tap-to-answer input when the client supports it. Allow **at most one follow-up round**; any gap still open after that goes to Open questions.

   Work from this fixed checklist and ask only about what you could not fill:
    - persona and role access;
    - market;
    - current behavior (if changing);
    - desired happy path;
    - the 1–2 key rules or edge cases;
    - what must not change;
    - out of scope;
    - Epic;
    - business priority and due date (may stay open).
3. **Sort the answers into three buckets.**
    - Answered → AC.
    - Default accepted → AC, marked **(default)** in the draft so the PM can see which behaviors they never stated.
    - Unknown or skipped → an Open question tagged `[Business]`, `[Engineering]` or `[QA]`.
4. **Flag a likely split** early if the scope looks over 5 points, as an `[Engineering]` open question.
5. **Show the full draft** (Summary, Context, ACs, Constraints if any, Open questions) and wait for "create it".
6. **Create it** in To Do with the description, the Epic, Code Dependency (if known) and the market label (`standards/story.md#international-markets`). No Fix Version and no points unless provided.
7. **Fast path:** if the PM says "just draft it", ask nothing and put every gap into Open questions.

Then hand off: AC approval and test cases follow the lifecycle in `standards/story.md`; check readiness with `playbooks/ready-check.md`.

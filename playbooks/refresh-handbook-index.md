# Playbook: Refresh the Handbook Index

Read: [`tools/handbook_index.py`](../tools/handbook_index.py)

The Handbook Index is a Confluence page (label `plugin-index`). Keeping it accurate costs one listing call, not a re-read of the handbook. Run this when the handbook structure changes, when the page's **Verified** date is more than 60 days old, or when a page the plugin cites has moved.

## Steps

1. Fetch the index page body (`getConfluencePage`, markdown) and save it to a file outside the repo.
2. Fetch the live tree once: `getConfluencePageDescendants` on the root (`2162262120`), depth 4, and again on any parent that sits outside the root (Product Lifecycle Process, Radius Database Reference). Save the JSON.
3. Run `python tools/handbook_index.py --index <index.md> check <listing.json> --root 2162262120`. It reports pages missing from Confluence, pages not in the index, renames, **retired** pages (`ZZ — Retired — …`), pages changed since **Verified** (compared to the minute, so keep Verified as a UTC datetime), and `(2)` duplicates. Use `--since <datetime>` to override the stamp.
   Save the index body and the listing exactly as the connector returned them. Never regenerate either one: a check against a rebuilt index proves nothing.
4. Read **only** the pages it flags. Record for each: character count, whether it is still a "Draft placeholder", and a one-line gist.
5. Give every page a specific gist, never generic text such as "populated page": the plugin routes by gist. Put the values in a profile JSON (`pageId`, `title`, `chars`, `placeholder`, `gist`) and run `python tools/handbook_index.py --index <index.md> update <profile.json>`. Add rows by hand for new pages and remove rows for deleted ones.
6. Show the result and, once approved, update the Confluence page. Do not edit Confluence without approval.

Do not store page content in this repo. The index keeps a size band, a stub flag and a one-line gist only. Plugin changes are never needed for any of this.

# Playbook: Refresh the Handbook Index

Read: [`handbook/index.md`](../handbook/index.md), [`tools/handbook_index.py`](../tools/handbook_index.py)

Keeps the plugin's page map accurate with one listing call instead of re-reading pages. Run it when the handbook structure changes, when the index `Verified` date is more than 30 days old, or when a page the plugin cites has moved.

## Steps

1. Fetch the live tree once: `getConfluencePageDescendants` on the root (`2162262120`) with depth 4, and again on the Product Lifecycle Process and Radius Database Reference pages if they are not under the root. Save the JSON outside the repo.
2. Run `python tools/handbook_index.py check <listing.json> --root 2162262120`. It reports pages missing from Confluence, pages not in the index, renames, pages changed since `Verified`, and `(2)` duplicates it ignores.
3. Read **only** the pages it lists as changed or new (not the whole handbook). Record for each: character count, whether it is still a "Draft placeholder", and a one-line gist.
4. Put those values in a profile JSON (`pageId`, `title`, `chars`, `placeholder`, `gist`) and run `python tools/handbook_index.py update <profile.json>`. Add rows by hand for new pages and remove rows for deleted ones.
5. Run `python tools/build_plugin.py` to copy the index into the skills and bump the plugin version, then the tests, then open a PR.

Do not store page content in this repo. The index keeps a size band, a stub flag and a one-line gist only.

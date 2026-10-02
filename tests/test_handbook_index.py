import json
import unittest
from datetime import date

from tools import handbook_index

INDEX = """# Index

**Verified:** 2026-09-01

| Title | pageId | Size | Status | Gist |
| --- | --- | --- | --- | --- |
| Story Standard | 2162393089 | M | real | Story rules |
| Glossary | 2162720809 | ? | ? | ? |
| Old Name | 2162000001 | S | real | gone page |
"""

LIVE = {
    "results": [
        {"id": "2162393089", "title": "Story Standard", "lastModified": "2026-09-20T10:00:00.000Z"},
        {"id": "2162720809", "title": "Glossary of Terms", "lastModified": "2026-08-01T10:00:00.000Z"},
        {"id": "2162999999", "title": "Brand New Page", "lastModified": "2026-09-25T10:00:00.000Z"},
        {"id": "2162888888", "title": "Identity (2)", "lastModified": "2026-09-25T10:00:00.000Z"},
    ]
}


class SizeBandTests(unittest.TestCase):
    def test_bands(self):
        self.assertEqual("S", handbook_index.size_band(300))
        self.assertEqual("M", handbook_index.size_band(5000))
        self.assertEqual("L", handbook_index.size_band(30000))
        self.assertEqual("XL", handbook_index.size_band(81000))
        self.assertEqual("?", handbook_index.size_band(None))


class CheckTests(unittest.TestCase):
    def setUp(self):
        self.report = handbook_index.check(INDEX, LIVE)

    def test_reports_each_kind_of_drift(self):
        self.assertEqual(["2162000001"], [r["pageId"] for r in self.report["missing_from_confluence"]])
        self.assertEqual(["2162999999"], [r["pageId"] for r in self.report["not_in_index"]])
        self.assertEqual(["2162393089"], [r["pageId"] for r in self.report["changed_since_verified"]])
        self.assertEqual(["2162888888"], [r["pageId"] for r in self.report["duplicates_ignored"]])
        self.assertEqual([], self.report["renamed"])  # "Glossary" within "Glossary of Terms" is not a rename
        self.assertTrue(handbook_index.has_drift(self.report))

    def test_real_rename_is_reported(self):
        live = {"results": [{"id": "2162393089", "title": "Totally Different Title", "lastModified": "2026-08-01T00:00:00Z"}]}
        report = handbook_index.check(INDEX, live)
        self.assertEqual("2162393089", report["renamed"][0]["pageId"])

    def test_root_pages_are_not_reported_missing(self):
        report = handbook_index.check(INDEX, LIVE, root_ids={"2162000001"})
        self.assertEqual([], report["missing_from_confluence"])

    def test_clean_index_has_no_drift(self):
        clean = INDEX.replace("| Old Name | 2162000001 | S | real | gone page |\n", "").replace("Glossary |", "Glossary of Terms |")
        live = {"results": [LIVE["results"][0], LIVE["results"][1]]}
        report = handbook_index.check(clean.replace("2026-09-01", "2026-10-01"), live)
        self.assertFalse(handbook_index.has_drift(report), report)

    def test_unverified_index_is_drift(self):
        report = handbook_index.check(INDEX.replace("2026-09-01", "never"), LIVE)
        self.assertTrue(report["index_never_verified"])


class UpdateTests(unittest.TestCase):
    def test_update_writes_size_status_gist_and_verified_date(self):
        profile = [
            {"pageId": "2162720809", "title": "Glossary", "chars": 350, "placeholder": True, "gist": "ignored"},
            {"pageId": "2162393089", "title": "Story Standard", "chars": 14000, "placeholder": False, "gist": "Story rules | with a pipe"},
        ]
        out = handbook_index.update(INDEX, profile, today=date(2026, 10, 2))
        rows = handbook_index.parse_rows(out)
        self.assertEqual(("S", "stub", "placeholder"), (rows["2162720809"]["size"], rows["2162720809"]["status"], rows["2162720809"]["gist"]))
        self.assertEqual(("M", "real"), (rows["2162393089"]["size"], rows["2162393089"]["status"]))
        self.assertNotIn("|  with", rows["2162393089"]["gist"])
        self.assertEqual(date(2026, 10, 2), handbook_index.verified_date(out))
        self.assertEqual("gone page", rows["2162000001"]["gist"])  # unprofiled rows untouched

    def test_update_is_idempotent(self):
        profile = [{"pageId": "2162393089", "title": "Story Standard", "chars": 14000, "placeholder": False, "gist": "Story rules"}]
        once = handbook_index.update(INDEX, profile, today=date(2026, 10, 2))
        self.assertEqual(once, handbook_index.update(once, profile, today=date(2026, 10, 2)))


class RealIndexTests(unittest.TestCase):
    def test_repo_index_parses_and_has_unique_ids(self):
        text = handbook_index.DEFAULT_INDEX.read_text(encoding="utf-8")
        rows = handbook_index.parse_rows(text)
        self.assertGreater(len(rows), 60)
        ids = [line for line in text.splitlines() if handbook_index.ROW.match(line)]
        self.assertEqual(len(ids), len(rows), "duplicate page IDs in handbook/index.md")

    def test_cli_check_reads_a_listing_file(self):
        import tempfile, pathlib
        with tempfile.TemporaryDirectory() as temp:
            listing = pathlib.Path(temp) / "listing.json"
            listing.write_text(json.dumps(LIVE), encoding="utf-8")
            index = pathlib.Path(temp) / "index.md"
            index.write_text(INDEX, encoding="utf-8")
            self.assertEqual(1, handbook_index.main(["--index", str(index), "check", str(listing)]))


if __name__ == "__main__":
    unittest.main()

import re
import unittest

from tools import build_plugin

REQUIRED_TOPICS = (
    "Product Lifecycle - Agent Router",
    "Product Lifecycle - Story Standard",
    "Product Lifecycle - Jira Conventions",
    "Product Lifecycle Playbook - Write Story",
    "Radius Database Reference",
    "Radius DB Reference - Overview and Conventions",
    "SQL, DAL & Data Access Standard",
)


class IndexTests(unittest.TestCase):
    def setUp(self):
        self.source = build_plugin.INDEX_SOURCE.read_text(encoding="utf-8")

    def test_index_states_site_and_cloud_id(self):
        self.assertIn("abd26ef1-c908-455d-8b20-516e025731b2", self.source)
        self.assertIn("https://mathnasium.atlassian.net", self.source)

    def test_required_topics_are_mapped_to_numeric_page_ids(self):
        for title in REQUIRED_TOPICS:
            row = next((line for line in self.source.splitlines() if title in line and "|" in line), None)
            self.assertIsNotNone(row, title)
            self.assertRegex(row, r"\b\d{10}\b", title)

    def test_page_ids_are_unique_per_topic_row(self):
        ids = re.findall(r"\|\s*(\d{10})\s*\|?\s*$", self.source, flags=re.M)
        self.assertEqual(len(ids), len(set(ids)), "duplicate page IDs in the index")

    def test_index_contains_no_secrets_or_jira_state(self):
        lowered = self.source.lower()
        for word in ("password", "api key", "token", "fixversion", "assignee"):
            self.assertNotIn(word, lowered)


class PluginInSyncTests(unittest.TestCase):
    def test_generated_copies_and_version_are_current(self):
        self.assertTrue(build_plugin.is_current(), "Run: python tools/build_plugin.py")

    def test_every_skill_has_an_index_copy_and_resolves_its_links(self):
        for skill in build_plugin.SKILLS_WITH_INDEX:
            folder = build_plugin.SKILLS_DIR / skill
            self.assertTrue((folder / build_plugin.INDEX_NAME).exists(), skill)
            text = (folder / "SKILL.md").read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)#\s]+)", text):
                if target.startswith("http"):
                    continue
                self.assertTrue((folder / target).exists(), f"{skill} links to {target}")

    def test_plugin_no_longer_bundles_standards(self):
        self.assertEqual([], list(build_plugin.SKILLS_DIR.rglob("references")))

    def test_skills_describe_confluence_as_the_only_source(self):
        handbook = (build_plugin.SKILLS_DIR / "handbook" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("only** reference", handbook)
        self.assertIn("SELECT", handbook)
        self.assertIn("Draft placeholder", (build_plugin.SKILLS_DIR / "write-jira-story" / "SKILL.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()

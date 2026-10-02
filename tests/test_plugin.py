import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from tools import package_plugin

PLUGIN = package_plugin.PLUGIN_DIR
SKILLS = PLUGIN / "skills"
CLOUD_ID = "abd26ef1-c908-455d-8b20-516e025731b2"


class LeanPluginTests(unittest.TestCase):
    def test_plugin_is_exactly_the_small_standalone_set(self):
        files = sorted(path.relative_to(PLUGIN).as_posix() for path in package_plugin.plugin_files())
        self.assertEqual(
            [
                ".claude-plugin/plugin.json",
                "hooks/guard.sh",
                "hooks/hooks.json",
                "skills/handbook/SKILL.md",
                "skills/write-jira-story/SKILL.md",
            ],
            files,
        )

    def test_no_handbook_content_or_index_copy_is_bundled(self):
        self.assertEqual([], list(SKILLS.rglob("references")))
        self.assertEqual([], list(PLUGIN.rglob("*index*.md")))

    def test_manifest_is_valid_and_versioned(self):
        manifest = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual("mathnasium-product-lifecycle", manifest["name"])
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")

    def test_skills_find_the_index_by_label_not_by_page_id(self):
        for skill in ("handbook", "write-jira-story"):
            text = (SKILLS / skill / "SKILL.md").read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\nname: " + skill + "\n"), skill)
            self.assertIn('label = "plugin-index" AND space = "IPD"', text)
            self.assertIn(CLOUD_ID, text)
            self.assertIn("contract **1**", text)
            self.assertNotRegex(text, r"\b\d{10}\b", f"{skill} hard-codes a page ID")

    def test_skills_stay_small_so_confluence_carries_the_content(self):
        for skill in ("handbook", "write-jira-story"):
            size = len((SKILLS / skill / "SKILL.md").read_text(encoding="utf-8"))
            self.assertLess(size, 4000, skill)

    def test_skills_stop_instead_of_guessing(self):
        for skill in ("handbook", "write-jira-story"):
            text = (SKILLS / skill / "SKILL.md").read_text(encoding="utf-8").lower()
            self.assertIn("say so plainly and stop", text, skill)


class PackagingTests(unittest.TestCase):
    def test_zip_has_the_plugin_at_its_root_and_nothing_else(self):
        with tempfile.TemporaryDirectory() as temp:
            target = package_plugin.package(Path(temp))
            self.assertRegex(target.name, r"^mathnasium-product-lifecycle-\d+\.\d+\.\d+\.zip$")
            with zipfile.ZipFile(target) as archive:
                names = sorted(archive.namelist())
        self.assertIn(".claude-plugin/plugin.json", names)
        self.assertIn("skills/handbook/SKILL.md", names)
        self.assertFalse([name for name in names if "__pycache__" in name or name.endswith(".pyc")])

    def test_cli_writes_the_archive(self):
        with tempfile.TemporaryDirectory() as temp:
            result = subprocess.run(
                [sys.executable, str(package_plugin.ROOT / "tools" / "package_plugin.py"), "--out", temp],
                capture_output=True, text=True, cwd=package_plugin.ROOT,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertTrue(list(Path(temp).glob("*.zip")))


if __name__ == "__main__":
    unittest.main()

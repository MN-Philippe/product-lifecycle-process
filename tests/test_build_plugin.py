import re
import unittest

from tools import build_plugin


class RewriteLinksTests(unittest.TestCase):
    def test_links_between_mapped_files_point_at_siblings(self):
        text = "See [story](../standards/story.md#size) and `standards/lifecycle.md#ready-for-dev-checklist`."
        result = build_plugin.rewrite_links(text, "playbooks/split-story.md")
        self.assertIn("[story](story.md#size)", result)
        self.assertIn("`lifecycle.md#ready-for-dev-checklist`", result)

    def test_sibling_links_inside_standards_resolve(self):
        result = build_plugin.rewrite_links("[c](jira-conventions.md#code-dependency)", "standards/story.md")
        self.assertEqual("[c](jira-conventions.md#code-dependency)", result)

    def test_template_gets_a_distinct_name(self):
        result = build_plugin.rewrite_links("[t](../templates/story.md)", "playbooks/write-story.md")
        self.assertEqual("[t](story-template.md)", result)

    def test_links_that_leave_the_plugin_are_unwrapped(self):
        result = build_plugin.rewrite_links("[guide](../templates/vendor-guide.md)", "standards/story.md")
        self.assertEqual("guide", result)

    def test_external_and_in_page_links_are_kept(self):
        text = "[x](https://example.com/a) and [y](#size)"
        self.assertEqual(text, build_plugin.rewrite_links(text, "standards/story.md"))


class PluginInSyncTests(unittest.TestCase):
    def test_generated_plugin_is_current(self):
        self.assertTrue(build_plugin.is_current(), "Run: python tools/build_plugin.py")

    def test_no_reference_links_escape_the_folder(self):
        for name, content in build_plugin.generate().items():
            for target in re.findall(r"\]\(([^)\s]+)\)", content):
                if target.startswith(("http", "#")):
                    continue
                path = target.split("#")[0]
                self.assertIn(path, build_plugin.SOURCES.values(), f"{name} links to {target}")

    def test_skill_links_resolve_to_references(self):
        skill = (build_plugin.SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        for target in re.findall(r"\]\(references/([^)#\s]+)", skill):
            self.assertTrue((build_plugin.REFERENCES_DIR / target).exists(), target)


if __name__ == "__main__":
    unittest.main()

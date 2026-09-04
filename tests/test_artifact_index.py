import tempfile
import unittest
from pathlib import Path

from tools import artifact_index


class ArtifactIndexTests(unittest.TestCase):
    def test_empty_index(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            initiatives = root / "initiatives"
            initiatives.mkdir()
            rendered = artifact_index.render(initiatives, root)
            self.assertIn("No initiative workspaces", rendered)

    def test_indexes_durable_files_by_jira_workspace(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            workspace = root / "initiatives" / "MYM-421-observability"
            decisions = workspace / "decisions"
            decisions.mkdir(parents=True)
            (workspace / "README.md").write_text("# Observability", encoding="utf-8")
            (workspace / "architecture.md").write_text("# Architecture", encoding="utf-8")
            (decisions / "ADR-001-logging.md").write_text("# ADR", encoding="utf-8")

            rendered = artifact_index.render(root / "initiatives", root)

            self.assertIn("## MYM-421 - Observability", rendered)
            self.assertIn("initiatives/MYM-421-observability/README.md", rendered)
            self.assertIn("initiatives/MYM-421-observability/architecture.md", rendered)
            self.assertIn("initiatives/MYM-421-observability/decisions/ADR-001-logging.md", rendered)
            self.assertNotIn("John Doe", rendered)
            self.assertNotIn("OCT-2026", rendered)


if __name__ == "__main__":
    unittest.main()

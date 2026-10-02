#!/usr/bin/env python3
"""Zip the Mathnasium plugin for a standalone install.

    python tools/package_plugin.py            # writes dist/mathnasium-product-lifecycle-<version>.zip

The plugin carries no handbook content: it finds its index page in Confluence at runtime, so
sharing it once is enough. Re-package only when the skills or the hook change, and bump the
version in plugin.json first (an install only updates when the version increases).
"""

from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_DIR = ROOT / "plugins" / "mathnasium-product-lifecycle"
DIST_DIR = ROOT / "dist"
EXCLUDED_PARTS = {"__pycache__", ".DS_Store"}


def plugin_files() -> list[Path]:
    return sorted(
        path
        for path in PLUGIN_DIR.rglob("*")
        if path.is_file() and not (set(path.relative_to(PLUGIN_DIR).parts) & EXCLUDED_PARTS) and path.suffix != ".pyc"
    )


def version() -> str:
    return json.loads((PLUGIN_DIR / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]


def package(out_dir: Path = DIST_DIR) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"mathnasium-product-lifecycle-{version()}.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in plugin_files():
            archive.write(path, path.relative_to(PLUGIN_DIR).as_posix())
    return target


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, default=DIST_DIR)
    args = parser.parse_args(argv)
    print(f"Wrote {package(args.out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Migrate a schema-v1 Lexsis page workspace to the single-source v2 layout."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def migrate(directory: Path) -> dict[str, Any]:
    manifest_path = directory / "page-manifest.json"
    if not manifest_path.is_file():
        raise ValueError("page-manifest.json is missing")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schemaVersion") == 2:
        return {"changed": False, "status": "already-v2"}
    if manifest.get("schemaVersion") != 1:
        raise ValueError("Only schemaVersion 1 workspaces can be migrated")

    visual_path = directory / "visual-source.html"
    source_path = directory / "lexsis-source.html"
    visual_source = visual_path.read_text(encoding="utf-8") if visual_path.is_file() else ""
    production_source = source_path.read_text(encoding="utf-8") if source_path.is_file() else ""
    if visual_source and production_source and visual_source != production_source:
        raise ValueError(
            "visual-source.html and lexsis-source.html differ; choose the canonical "
            "version and obtain renewed visual approval before migration"
        )
    canonical_source = production_source or visual_source

    page_config = manifest.setdefault("pageConfig", {})
    embedded_theme_css = page_config.get("themeCss", "")
    page_theme_path = directory / "page-theme.css"
    existing_page_theme = (
        page_theme_path.read_text(encoding="utf-8")
        if page_theme_path.is_file()
        else ""
    )
    if (
        existing_page_theme
        and embedded_theme_css
        and existing_page_theme != embedded_theme_css
    ):
        raise ValueError(
            "page-theme.css and pageConfig.themeCss differ; choose the canonical "
            "theme before migration"
        )
    canonical_theme = existing_page_theme or embedded_theme_css
    if not canonical_theme:
        setup_theme_path = Path(str(manifest.get("themeCssPath", "")))
        if not setup_theme_path.is_absolute():
            setup_theme_path = directory / setup_theme_path
        if not setup_theme_path.is_file():
            raise ValueError(
                "Cannot create page-theme.css: pageConfig.themeCss and the "
                "saved setup theme file are both unavailable"
            )
        canonical_theme = setup_theme_path.read_text(encoding="utf-8")
    if not canonical_theme.strip():
        raise ValueError("Canonical page theme cannot be empty")

    old_visual = manifest.get("visual", {})
    old_status = old_visual.get("status", "pending")
    if old_status == "approved":
        old_status = "changes-pending-approval"
    manifest["schemaVersion"] = 2
    manifest["pageThemeCssPath"] = "page-theme.css"
    manifest["compileInputs"] = manifest.get("compileInputs", {})
    page_config.pop("themeCss", None)
    manifest["visual"] = {
        "status": old_status,
        "sourcePath": "lexsis-source.html",
        "themeCssPath": "page-theme.css",
        "previewPath": "visual-preview.html",
        "compileArtifactPath": "compile-artifact.json",
        "approvedSourceHash": None,
        "approvedThemeCssHash": None,
        "approvedConfigHash": None,
        "approvedStructureHash": None,
        "approvedBundleHash": None,
        "approvedCompileBundleHash": None,
        "hydrationStatus": "pending",
        "hydrationEvidence": None,
    }
    manifest["fidelity"] = {
        "status": "pending",
        "productionBundleHash": None,
        "remoteSourceHash": None,
        "remoteBundleHash": None,
        "changedBindingPaths": [],
        "approvedExceptions": [],
    }

    if canonical_source and production_source != canonical_source:
        source_path.write_text(canonical_source, encoding="utf-8")
    if existing_page_theme != canonical_theme:
        page_theme_path.write_text(canonical_theme, encoding="utf-8")
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if visual_path.is_file():
        visual_path.unlink()
    return {
        "changed": True,
        "status": "migrated",
        "visualStatus": old_status,
        "requiresVisualApproval": old_status == "changes-pending-approval",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("working_directory", type=Path)
    args = parser.parse_args()
    try:
        result = migrate(args.working_directory.resolve())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 1
    print(json.dumps({"ok": True, **result}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Migrate a legacy Lexsis page workspace to the compact schema-v3 manifest."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def compact_asset(asset: dict[str, Any]) -> dict[str, Any]:
    result = {
        key: asset[key]
        for key in (
            "role",
            "sectionId",
            "sourceType",
            "assetId",
            "productId",
            "mediaId",
            "url",
        )
        if asset.get(key) is not None
    }
    result["status"] = asset.get("status") or asset.get("verificationStatus") or "pending"
    return result


def compact_island(island: dict[str, Any]) -> dict[str, Any]:
    schema = island.get("schema") if isinstance(island.get("schema"), dict) else {}
    return {
        "sectionId": island.get("sectionId"),
        "name": island.get("name"),
        "schemaVersion": island.get("schemaVersion") or schema.get("version"),
        "lifecycleStatus": island.get("lifecycleStatus")
        or schema.get("lifecycleStatus"),
        "mode": island.get("mode") or island.get("productionMode"),
        "previewMode": island.get("previewMode"),
    }


def rename_preview(directory: Path) -> None:
    old_path = directory / "visual-preview.html"
    new_path = directory / "page-preview.html"
    if not old_path.is_file():
        return
    if new_path.is_file():
        if old_path.read_bytes() != new_path.read_bytes():
            raise ValueError(
                "visual-preview.html and page-preview.html differ; choose the "
                "approved preview before migration"
            )
        old_path.unlink()
        return
    old_path.rename(new_path)


def canonicalize_v1_source(directory: Path, manifest: dict[str, Any]) -> None:
    visual_path = directory / "visual-source.html"
    source_path = directory / "lexsis-source.html"
    visual_source = visual_path.read_text(encoding="utf-8") if visual_path.is_file() else ""
    production_source = source_path.read_text(encoding="utf-8") if source_path.is_file() else ""
    if visual_source and production_source and visual_source != production_source:
        raise ValueError(
            "visual-source.html and lexsis-source.html differ; choose the canonical "
            "version before migration"
        )
    if visual_source and not production_source:
        source_path.write_text(visual_source, encoding="utf-8")
    if visual_path.is_file():
        visual_path.unlink()

    page_config = manifest.get("pageConfig", {})
    embedded_theme = page_config.get("themeCss", "") if isinstance(page_config, dict) else ""
    theme_path = directory / "page-theme.css"
    existing_theme = theme_path.read_text(encoding="utf-8") if theme_path.is_file() else ""
    if existing_theme and embedded_theme and existing_theme != embedded_theme:
        raise ValueError(
            "page-theme.css and pageConfig.themeCss differ; choose the canonical "
            "theme before migration"
        )
    if not existing_theme and embedded_theme:
        theme_path.write_text(embedded_theme, encoding="utf-8")


def migrate(directory: Path) -> dict[str, Any]:
    manifest_path = directory / "page-manifest.json"
    if not manifest_path.is_file():
        raise ValueError("page-manifest.json is missing")

    old = json.loads(manifest_path.read_text(encoding="utf-8"))
    version = old.get("schemaVersion")
    if version == 3:
        return {"changed": False, "status": "already-v3"}
    if version not in {1, 2}:
        raise ValueError("Only schemaVersion 1 or 2 workspaces can be migrated")

    if version == 1:
        canonicalize_v1_source(directory, old)
    rename_preview(directory)

    skipped = [
        "design-page" if item == "visual-page" else item
        for item in old.get("workflow", {}).get("skippedSkills", [])
    ]
    template = old.get("template", {}) if isinstance(old.get("template"), dict) else {}
    new: dict[str, Any] = {
        "schemaVersion": 3,
        "status": old.get("status", "planned"),
        "workflow": {"skippedSkills": skipped},
        "page": old.get("page", {}),
        "workspaceId": old.get("workspaceId"),
        "storeId": old.get("storeId"),
        "themeId": old.get("themeId"),
        "setupPath": old.get("setupPath", "work/storefront/setup/setup.json"),
        "template": {
            "mode": template.get("mode", "custom"),
            "pageKitId": template.get("pageKitId"),
            "sectionTemplateIds": template.get("sectionTemplateIds", []),
        },
        "sections": old.get("sections", []),
        "products": [
            {
                "productId": item.get("productId") or item.get("shopifyProductId"),
                "variantIds": item.get("variantIds", []),
            }
            for item in old.get("productBindings", old.get("products", []))
            if isinstance(item, dict)
            and (item.get("productId") or item.get("shopifyProductId"))
        ],
    }

    page_config = old.get("pageConfig", {}) if isinstance(old.get("pageConfig"), dict) else {}
    compile_inputs = (
        old.get("compileInputs", {})
        if isinstance(old.get("compileInputs"), dict)
        else {}
    )
    if (directory / "lexsis-source.html").is_file() or page_config or compile_inputs:
        new["config"] = {
            "head": page_config.get("head", {}),
            "scripts": page_config.get("scripts", []),
            "productBinding": compile_inputs.get("productBinding", {}),
            "commerceConfig": compile_inputs.get("commerceConfig", {}),
        }

    assets = [
        compact_asset(item)
        for item in old.get("assets", [])
        if isinstance(item, dict)
    ]
    islands = [
        compact_island(item)
        for item in old.get("islands", [])
        if isinstance(item, dict)
    ]
    if assets or (directory / "lexsis-source.html").is_file():
        new["assets"] = assets
    if islands or (directory / "lexsis-source.html").is_file():
        new["islands"] = islands

    old_visual = old.get("visual", {}) if isinstance(old.get("visual"), dict) else {}
    old_design = old.get("design", {}) if isinstance(old.get("design"), dict) else {}
    old_status = old_visual.get("status", old_design.get("status", "pending"))
    if old_status == "approved":
        old_status = "changes-pending-approval"
    if (directory / "lexsis-source.html").is_file() or old_visual or old_design:
        hydration = old_visual.get("hydrationEvidence")
        if isinstance(hydration, dict):
            hydration = {
                "status": old_visual.get("hydrationStatus", "pending"),
                **hydration,
            }
        new["design"] = {
            "status": old_status,
            "stylePack": old_design.get("stylePack"),
            "compiledStyleManifest": old_design.get("compiledStyleManifest"),
            "sourceHash": old_visual.get("approvedSourceHash"),
            "themeCssHash": old_visual.get("approvedThemeCssHash"),
            "configHash": old_visual.get("approvedConfigHash"),
            "structureHash": old_visual.get("approvedStructureHash"),
            "bundleHash": old_visual.get("approvedBundleHash"),
            "compiledBundleHash": old_visual.get("approvedCompileBundleHash"),
            "hydration": hydration,
        }

    old_sync = old.get("sourceSync", {}) if isinstance(old.get("sourceSync"), dict) else {}
    old_fidelity = old.get("fidelity", {}) if isinstance(old.get("fidelity"), dict) else {}
    if old_sync or old_fidelity:
        new["sync"] = {
            "lastCompiledBundleHash": old_sync.get("lastCompiledBundleHash"),
            "lastSyncedBundleHash": old_sync.get("lastSyncedBundleHash"),
            "lastSyncedSectionHashes": old_sync.get("lastSyncedSectionHashes", {}),
            "lastChangedSections": old_sync.get("lastChangedSections", []),
            "remoteSourceHash": old_fidelity.get("remoteSourceHash"),
            "remoteBundleHash": old_fidelity.get("remoteBundleHash"),
        }
    if isinstance(old.get("remote"), dict) and old["remote"]:
        new["remote"] = old["remote"]
    old_qa = old.get("qa", {}) if isinstance(old.get("qa"), dict) else {}
    if old_qa:
        new["qa"] = {
            "status": old_qa.get("status", "pending"),
            "version": old_qa.get("version", old_qa.get("checkedVersion")),
            "bundleHash": old_qa.get("bundleHash", old_qa.get("checkedBundleHash")),
            "checks": {
                key: old_qa.get(key, False)
                for key in (
                    "responsive",
                    "visualRegression",
                    "commerce",
                    "copy",
                    "claims",
                    "assets",
                    "integrity",
                )
            },
        }

    manifest_path.write_text(
        json.dumps(new, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return {
        "changed": True,
        "status": "migrated",
        "fromSchemaVersion": version,
        "requiresDesignApproval": new.get("design", {}).get("status")
        == "changes-pending-approval",
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

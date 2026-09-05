#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VALIDATOR = load_module(
    "validate_page_workspace",
    ROOT / "skills/generate/scripts/validate_page_workspace.py",
)
MIGRATOR = load_module(
    "migrate_page_workspace_v2",
    ROOT / "skills/generate/scripts/migrate_page_workspace_v2.py",
)

SOURCE = """<!-- section: hero -->
<section id="hero">
  <lx-island name="BuyBox">
    <script type="application/json">
      {"product": {"title": "Creatine", "price": "₹299", "variants": []}}
    </script>
    <div data-lx-island-fallback>
      <p>Creatine</p>
      <button type="button">Add to cart</button>
    </div>
  </lx-island>
</section>

<style>
  #hero { color: var(--lx-text-color); }
</style>
"""
THEME_CSS = ":root { --lx-accent-color: #111111; --lx-text-color: #222222; }\n"
PREVIEW = """<!doctype html>
<html>
  <body data-lx-visual-preview data-lx-hydration-status="pending">
    <div data-island="BuyBox" data-props="{}"></div>
    <link rel="stylesheet" href="https://storefront.trylexsis.com/islands/storefront.css">
    <script src="https://storefront.trylexsis.com/islands/islands.js"></script>
    <script>
      window.__LEXSIS_PREVIEW_STATUS__ = {state: "passed"};
      window.LexsisIslands.hydrateIslands([]);
    </script>
  </body>
</html>
"""


class WorkspaceValidatorTests(unittest.TestCase):
    def make_workspace(self, visual_status: str = "approved") -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "assets").mkdir()
        setup_dir = root / "saved-setup"
        brand_dir = setup_dir / "stores" / "store"
        theme_dir = brand_dir / "themes"
        theme_dir.mkdir(parents=True)
        brand_path = brand_dir / "brand-design.md"
        setup_theme_path = theme_dir / "theme.css"
        setup_path = setup_dir / "setup.json"
        brand_path.write_text("# Brand\n", encoding="utf-8")
        setup_theme_path.write_text(THEME_CSS, encoding="utf-8")
        setup_path.write_text(
            json.dumps(
                {
                    "schemaVersion": 1,
                    "workspaceId": "workspace",
                    "defaultStoreId": "store",
                    "defaultThemeId": "theme",
                    "stores": [
                        {
                            "storeId": "store",
                            "brandDesignPath": str(brand_path),
                            "themes": [
                                {
                                    "themeId": "theme",
                                    "themeCssPath": str(setup_theme_path),
                                }
                            ],
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        (root / "page-plan.md").write_text("# Plan\n", encoding="utf-8")
        (root / "qa-report.md").write_text("# QA\nAll checks passed.\n", encoding="utf-8")
        (root / "lexsis-source.html").write_text(SOURCE, encoding="utf-8")
        (root / "page-theme.css").write_text(THEME_CSS, encoding="utf-8")

        page_config = {"head": {"title": "Creatine"}, "scripts": []}
        compile_inputs = {
            "productBinding": {"productId": "product", "variantIds": ["variant"]}
        }
        source_hash = VALIDATOR.sha256(SOURCE)
        theme_hash = VALIDATOR.sha256(THEME_CSS)
        config_hash = VALIDATOR.config_hash(page_config, compile_inputs)
        structure_hash = VALIDATOR.structure_hash(SOURCE)
        current_bundle_hash = VALIDATOR.bundle_hash(
            SOURCE, page_config, THEME_CSS, compile_inputs
        )
        hashes = VALIDATOR.section_hashes(SOURCE)
        compile_response = {
            "page": {
                "sections": [
                    {
                        "id": "hero",
                        "html": '<section id="hero"><div data-island="BuyBox" data-props="{}"></div></section>',
                        "css": "",
                        "js": "",
                    }
                ]
            }
        }
        compiled_bundle_hash = VALIDATOR.compiled_response_hash(compile_response)

        if visual_status == "approved":
            (root / "visual-preview.html").write_text(PREVIEW, encoding="utf-8")
            (root / "compile-artifact.json").write_text(
                json.dumps(
                    {
                        "schemaVersion": 1,
                        "sourceHash": source_hash,
                        "themeCssHash": theme_hash,
                        "configHash": config_hash,
                        "structureHash": structure_hash,
                        "bundleHash": current_bundle_hash,
                        "compiledBundleHash": compiled_bundle_hash,
                        "compiledAt": "2026-09-05T12:00:00Z",
                        "response": compile_response,
                    }
                ),
                encoding="utf-8",
            )

        skipped = ["visual-page"] if visual_status == "skipped" else []
        visual = {
            "status": visual_status,
            "sourcePath": "lexsis-source.html",
            "themeCssPath": "page-theme.css",
            "previewPath": "visual-preview.html",
            "compileArtifactPath": "compile-artifact.json",
            "approvedSourceHash": source_hash if visual_status == "approved" else None,
            "approvedThemeCssHash": theme_hash if visual_status == "approved" else None,
            "approvedConfigHash": config_hash if visual_status == "approved" else None,
            "approvedStructureHash": structure_hash if visual_status == "approved" else None,
            "approvedBundleHash": current_bundle_hash if visual_status == "approved" else None,
            "approvedCompileBundleHash": compiled_bundle_hash if visual_status == "approved" else None,
            "hydrationStatus": "passed" if visual_status == "approved" else "pending",
            "hydrationEvidence": (
                {
                    "bundleHash": current_bundle_hash,
                    "expectedIslands": ["0:BuyBox"],
                    "hydratedIslands": ["0:BuyBox"],
                    "checkedAt": "2026-09-05T12:01:00Z",
                }
                if visual_status == "approved"
                else None
            ),
        }
        manifest = {
            "schemaVersion": 2,
            "status": "qa_passed",
            "workflow": {"skippedSkills": skipped},
            "mcp": {
                "status": "connected",
                "checkedAt": "2026-09-05T12:00:00Z",
                "surfaceVersion": "3.0",
                "capabilities": [{"router": "lexsis_pages", "actions": ["compile"]}],
            },
            "page": {"title": "Creatine", "handle": "creatine", "archetype": "landing"},
            "workspaceId": "workspace",
            "storeId": "store",
            "themeId": "theme",
            "template": {
                "mode": "custom",
                "evaluatedTemplates": [],
                "selectionReason": "No suitable template matched the test fixture",
                "selectedAt": "2026-09-05T12:00:00Z",
            },
            "design": {
                "themeId": "theme",
                "themeSource": "saved-and-verified",
                "stylePack": "minimal",
                "compiledStyleManifest": {
                    "engine": "tailwindcss",
                    "compiler_version": "4.3.0",
                },
            },
            "setupPath": str(setup_path),
            "brandDesignPath": str(brand_path),
            "themeCssPath": str(setup_theme_path),
            "pageThemeCssPath": "page-theme.css",
            "pageConfig": page_config,
            "compileInputs": compile_inputs,
            "productBindings": [{"productId": "product", "variantIds": ["variant"]}],
            "assets": [],
            "sections": ["hero"],
            "islands": [
                {
                    "sectionId": "hero",
                    "name": "BuyBox",
                    "schema": {
                        "version": "5.0.0",
                        "lifecycleStatus": "active",
                        "resolvedAt": "2026-09-05T12:00:00Z",
                    },
                    "productionMode": "native",
                    "previewMode": "hydrated",
                    "previewData": True,
                }
            ],
            "visual": visual,
            "fidelity": {
                "status": "passed",
                "productionBundleHash": current_bundle_hash,
                "remoteSourceHash": source_hash,
                "remoteBundleHash": current_bundle_hash,
                "changedBindingPaths": [],
                "approvedExceptions": [],
            },
            "sourceSync": {
                "lastCompiledBundleHash": current_bundle_hash,
                "lastSyncedBundleHash": current_bundle_hash,
                "lastSyncedSectionHashes": hashes,
                "lastChangedSections": ["hero"],
            },
            "qa": {
                "status": "passed",
                "checkedVersion": 2,
                "checkedBundleHash": current_bundle_hash,
                "responsive": True,
                "visualRegression": True,
                "commerce": True,
                "copy": True,
                "claims": True,
                "assets": True,
                "integrity": True,
            },
            "remote": {
                "pageId": "page",
                "lastKnownVersion": 2,
                "previewUrl": "https://preview.example",
            },
        }
        (root / "page-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return root

    def manifest(self, root: Path) -> dict:
        return json.loads((root / "page-manifest.json").read_text(encoding="utf-8"))

    def write_manifest(self, root: Path, manifest: dict) -> None:
        (root / "page-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    def codes(self, root: Path, phase: str) -> set[str]:
        return {item["code"] for item in VALIDATOR.validate_workspace(root, phase)["errors"]}

    def test_valid_workspace_passes_draft_and_publish_gates(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        evidence = {
            "remote_source_hash": manifest["fidelity"]["remoteSourceHash"],
            "remote_bundle_hash": manifest["fidelity"]["remoteBundleHash"],
        }
        self.assertTrue(
            VALIDATOR.validate_workspace(root, "draft", **evidence)["ok"]
        )
        self.assertTrue(
            VALIDATOR.validate_workspace(root, "publish", **evidence)["ok"]
        )

    def test_single_source_visual_passes(self) -> None:
        result = VALIDATOR.validate_workspace(self.make_workspace(), "visual")
        self.assertTrue(result["ok"], result)
        self.assertEqual(VALIDATOR.sha256(SOURCE), result["sourceHash"])

    def test_explicit_visual_skip_passes_precompile(self) -> None:
        result = VALIDATOR.validate_workspace(self.make_workspace("skipped"), "precompile")
        self.assertTrue(result["ok"], result)

    def test_adopted_page_does_not_require_visual_artifacts(self) -> None:
        result = VALIDATOR.validate_workspace(self.make_workspace("not-used"), "adopted")
        self.assertTrue(result["ok"], result)

    def test_approved_visual_requires_generated_files(self) -> None:
        root = self.make_workspace()
        (root / "visual-preview.html").unlink()
        (root / "compile-artifact.json").unlink()
        self.assertIn("missing_visual_artifact", self.codes(root, "visual"))

    def test_compiled_island_markup_is_rejected_in_source(self) -> None:
        root = self.make_workspace("skipped")
        (root / "lexsis-source.html").write_text(
            '<!-- section: hero --><section id="hero">'
            '<div data-island="BuyBox" data-props="{}"></div></section>',
            encoding="utf-8",
        )
        self.assertIn("compiled_source_island", self.codes(root, "precompile"))

    def test_preview_requires_runtime_status_markers(self) -> None:
        root = self.make_workspace()
        (root / "visual-preview.html").write_text(
            '<body data-lx-visual-preview><script src="https://storefront.trylexsis.com/islands/islands.js"></script>'
            "<script>window.LexsisIslands.hydrateIslands([])</script></body>",
            encoding="utf-8",
        )
        codes = self.codes(root, "visual")
        self.assertIn("preview_hydration_state", codes)
        self.assertIn("preview_status_object", codes)

    def test_source_theme_and_config_drift_are_blocking(self) -> None:
        root = self.make_workspace()
        (root / "lexsis-source.html").write_text(SOURCE.replace("Creatine", "Changed", 1), encoding="utf-8")
        self.assertIn("visual_source_drift", self.codes(root, "precompile"))

        root = self.make_workspace()
        (root / "page-theme.css").write_text(THEME_CSS + "body { margin: 0; }\n", encoding="utf-8")
        self.assertIn("visual_theme_drift", self.codes(root, "precompile"))

        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["pageConfig"]["head"]["title"] = "Changed"
        self.write_manifest(root, manifest)
        self.assertIn("visual_config_drift", self.codes(root, "precompile"))

        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["compileInputs"]["productBinding"]["productId"] = "other-product"
        self.write_manifest(root, manifest)
        self.assertIn("visual_config_drift", self.codes(root, "precompile"))

    def test_compile_artifact_drift_is_blocking(self) -> None:
        root = self.make_workspace()
        artifact_path = root / "compile-artifact.json"
        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        artifact["bundleHash"] = "wrong"
        artifact_path.write_text(json.dumps(artifact), encoding="utf-8")
        self.assertIn("compile_artifact_drift", self.codes(root, "visual"))

    def test_compile_response_hash_must_match_artifact(self) -> None:
        root = self.make_workspace()
        artifact_path = root / "compile-artifact.json"
        artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        artifact["response"]["page"]["sections"][0]["html"] = "<section>Different</section>"
        artifact_path.write_text(json.dumps(artifact), encoding="utf-8")
        self.assertIn("compile_bundle_drift", self.codes(root, "visual"))

    def test_hydration_and_fallback_are_blocking(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["visual"]["hydrationStatus"] = "failed"
        manifest["islands"][0]["previewMode"] = "fallback"
        self.write_manifest(root, manifest)
        codes = self.codes(root, "visual")
        self.assertIn("visual_hydration", codes)
        self.assertIn("visual_island_fallback", codes)

    def test_hydration_evidence_must_cover_approved_bundle(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["visual"]["hydrationEvidence"]["hydratedIslands"] = []
        self.write_manifest(root, manifest)
        self.assertIn("visual_hydration_evidence", self.codes(root, "visual"))

    def test_not_used_cannot_hide_old_approval(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["visual"]["status"] = "not-used"
        self.write_manifest(root, manifest)
        self.assertIn("visual_approval_bypass", self.codes(root, "adopted"))

    def test_skipped_cannot_hide_old_approval(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["visual"]["status"] = "skipped"
        manifest["workflow"]["skippedSkills"] = ["visual-page"]
        self.write_manifest(root, manifest)
        self.assertIn("visual_approval_bypass", self.codes(root, "precompile"))

    def test_manifest_requires_schema_v2_and_external_page_theme(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["schemaVersion"] = 1
        manifest["pageConfig"]["themeCss"] = THEME_CSS
        self.write_manifest(root, manifest)
        codes = self.codes(root, "precompile")
        self.assertIn("manifest_schema", codes)
        self.assertIn("embedded_theme_css", codes)

    def test_page_theme_path_cannot_redirect_to_another_file(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["pageThemeCssPath"] = "other.css"
        self.write_manifest(root, manifest)
        self.assertIn("page_theme_path", self.codes(root, "precompile"))

    def test_preview_placeholder_is_visual_only(self) -> None:
        root = self.make_workspace()
        source = SOURCE.replace(
            "<p>Creatine</p>",
            '<p>Creatine</p><img src="assets/placeholders/hero-landscape.svg" alt="Hero">',
        )
        (root / "lexsis-source.html").write_text(source, encoding="utf-8")
        manifest = self.manifest(root)
        manifest["visual"]["status"] = "skipped"
        manifest["workflow"]["skippedSkills"] = ["visual-page"]
        manifest["assets"] = [
            {
                "role": "hero",
                "sectionId": "hero",
                "sourceType": "preview-placeholder",
                "url": "assets/placeholders/hero-landscape.svg",
                "width": 1600,
                "height": 900,
                "desktopCrop": "center",
                "mobileCrop": "center",
                "altTextIntent": "Temporary hero composition",
                "verificationStatus": "preview-only",
            }
        ]
        self.write_manifest(root, manifest)
        self.assertNotIn("preview_asset_in_production", self.codes(root, "visual"))
        self.assertIn("preview_asset_in_production", self.codes(root, "precompile"))
        self.assertIn("relative_media_url", self.codes(root, "precompile"))

    def test_remote_hash_mismatch_blocks_draft(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["fidelity"]["remoteBundleHash"] = "wrong"
        self.write_manifest(root, manifest)
        result = VALIDATOR.validate_workspace(
            root,
            "draft",
            remote_source_hash=manifest["fidelity"]["remoteSourceHash"],
            remote_bundle_hash="live-wrong",
        )
        codes = {item["code"] for item in result["errors"]}
        self.assertIn("fidelity_failed", codes)
        self.assertIn("remote_evidence_mismatch", codes)

    def test_draft_requires_live_remote_hash_evidence(self) -> None:
        root = self.make_workspace()
        self.assertIn("remote_evidence_missing", self.codes(root, "draft"))

    def test_remote_version_mismatch_is_blocking(self) -> None:
        root = self.make_workspace()
        result = VALIDATOR.validate_workspace(root, "precompile", current_remote_version=3)
        self.assertIn(
            "remote_version_mismatch",
            {item["code"] for item in result["errors"]},
        )

    def test_changed_sections_reports_only_modified_hero(self) -> None:
        root = self.make_workspace("skipped")
        baseline = """<!-- section: hero -->
<section id="hero"><h1>Original</h1></section>
<!-- section: faq -->
<section id="faq"><details><summary>Question</summary><p>Answer</p></details></section>
"""
        changed = baseline.replace("Original", "Improved")
        (root / "lexsis-source.html").write_text(changed, encoding="utf-8")
        manifest = self.manifest(root)
        manifest["sections"] = ["hero", "faq"]
        manifest["islands"] = []
        manifest["sourceSync"]["lastSyncedSectionHashes"] = VALIDATOR.section_hashes(baseline)
        self.write_manifest(root, manifest)
        result = VALIDATOR.validate_workspace(root, "precompile")
        self.assertEqual(["hero"], result["changedSections"])

    def test_v1_migration_promotes_identical_source_and_requires_reapproval(self) -> None:
        root = self.make_workspace("skipped")
        manifest = self.manifest(root)
        manifest["schemaVersion"] = 1
        manifest["pageConfig"]["themeCss"] = THEME_CSS
        manifest.pop("pageThemeCssPath")
        manifest.pop("fidelity")
        manifest["visual"] = {
            "status": "approved",
            "sourcePath": "visual-source.html",
            "previewPath": "visual-preview.html",
        }
        self.write_manifest(root, manifest)
        (root / "visual-source.html").write_text(SOURCE, encoding="utf-8")
        (root / "page-theme.css").unlink()

        result = MIGRATOR.migrate(root)

        self.assertTrue(result["changed"])
        migrated = self.manifest(root)
        self.assertEqual(2, migrated["schemaVersion"])
        self.assertEqual("changes-pending-approval", migrated["visual"]["status"])
        self.assertFalse((root / "visual-source.html").exists())
        self.assertEqual(THEME_CSS, (root / "page-theme.css").read_text(encoding="utf-8"))

    def test_v1_migration_stops_on_source_conflict(self) -> None:
        root = self.make_workspace("skipped")
        manifest = self.manifest(root)
        manifest["schemaVersion"] = 1
        self.write_manifest(root, manifest)
        (root / "visual-source.html").write_text(SOURCE.replace("Creatine", "Other", 1), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "differ"):
            MIGRATOR.migrate(root)

    def test_v1_migration_recovers_visual_source_when_production_is_empty(self) -> None:
        root = self.make_workspace("skipped")
        manifest = self.manifest(root)
        manifest["schemaVersion"] = 1
        manifest["pageConfig"]["themeCss"] = THEME_CSS
        self.write_manifest(root, manifest)
        (root / "lexsis-source.html").write_text("", encoding="utf-8")
        (root / "visual-source.html").write_text(SOURCE, encoding="utf-8")

        MIGRATOR.migrate(root)

        self.assertEqual(
            SOURCE,
            (root / "lexsis-source.html").read_text(encoding="utf-8"),
        )

    def test_v1_migration_stops_on_theme_conflict(self) -> None:
        root = self.make_workspace("skipped")
        manifest = self.manifest(root)
        manifest["schemaVersion"] = 1
        manifest["pageConfig"]["themeCss"] = "body { color: red; }"
        self.write_manifest(root, manifest)
        with self.assertRaisesRegex(ValueError, "differ"):
            MIGRATOR.migrate(root)


if __name__ == "__main__":
    unittest.main()

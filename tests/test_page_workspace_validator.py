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
    "migrate_page_workspace_v3",
    ROOT / "skills/generate/scripts/migrate_page_workspace_v3.py",
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
    def make_workspace(self, design_status: str = "approved") -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "assets").mkdir()
        setup_dir = root / "saved-setup"
        store_dir = setup_dir / "stores" / "store"
        theme_dir = store_dir / "themes"
        theme_dir.mkdir(parents=True)
        brand_path = store_dir / "brand-design.md"
        theme_path = theme_dir / "theme.css"
        setup_path = setup_dir / "setup.json"
        brand_path.write_text("# Brand\n", encoding="utf-8")
        theme_path.write_text(THEME_CSS, encoding="utf-8")
        setup_path.write_text(
            json.dumps(
                {
                    "schemaVersion": 1,
                    "workspaceId": "workspace",
                    "stores": [
                        {
                            "storeId": "store",
                            "brandDesignPath": str(brand_path),
                            "themes": [
                                {
                                    "themeId": "theme",
                                    "themeCssPath": str(theme_path),
                                }
                            ],
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        (root / "page-plan.md").write_text("# Plan\n", encoding="utf-8")
        (root / "lexsis-source.html").write_text(SOURCE, encoding="utf-8")
        (root / "page-theme.css").write_text(THEME_CSS, encoding="utf-8")

        config = {
            "head": {"title": "Creatine"},
            "scripts": [],
            "productBinding": {"productId": "product", "variantIds": ["variant"]},
            "commerceConfig": {},
        }
        page_config = {"head": config["head"], "scripts": config["scripts"]}
        compile_inputs = {
            "productBinding": config["productBinding"],
            "commerceConfig": config["commerceConfig"],
        }
        source_hash = VALIDATOR.sha256(SOURCE)
        theme_hash = VALIDATOR.sha256(THEME_CSS)
        config_hash = VALIDATOR.config_hash(page_config, compile_inputs)
        structure_hash = VALIDATOR.structure_hash(SOURCE)
        bundle_hash = VALIDATOR.bundle_hash(
            SOURCE, page_config, THEME_CSS, compile_inputs
        )
        section_hashes = VALIDATOR.section_hashes(SOURCE)
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
        compiled_hash = VALIDATOR.compiled_response_hash(compile_response)

        if design_status == "approved":
            (root / "page-preview.html").write_text(PREVIEW, encoding="utf-8")
            (root / "compile-artifact.json").write_text(
                json.dumps(
                    {
                        "schemaVersion": 1,
                        "sourceHash": source_hash,
                        "themeCssHash": theme_hash,
                        "configHash": config_hash,
                        "structureHash": structure_hash,
                        "bundleHash": bundle_hash,
                        "compiledBundleHash": compiled_hash,
                        "compiledAt": "2026-09-05T12:00:00Z",
                        "response": compile_response,
                    }
                ),
                encoding="utf-8",
            )

        skipped = ["design-page"] if design_status == "skipped" else []
        manifest = {
            "schemaVersion": 3,
            "status": "qa_passed",
            "workflow": {"skippedSkills": skipped},
            "page": {"title": "Creatine", "handle": "creatine", "archetype": "landing"},
            "workspaceId": "workspace",
            "storeId": "store",
            "themeId": "theme",
            "setupPath": str(setup_path),
            "template": {
                "mode": "custom",
                "pageKitId": None,
                "sectionTemplateIds": [],
            },
            "sections": ["hero"],
            "products": [{"productId": "product", "variantIds": ["variant"]}],
            "config": config,
            "assets": [],
            "islands": [
                {
                    "sectionId": "hero",
                    "name": "BuyBox",
                    "schemaVersion": "5.0.0",
                    "lifecycleStatus": "active",
                    "mode": "native",
                    "previewMode": "hydrated",
                }
            ],
            "design": {
                "status": design_status,
                "stylePack": "minimal",
                "compiledStyleManifest": {
                    "engine": "tailwindcss",
                    "compilerVersion": "4.3.0",
                },
                "sourceHash": source_hash if design_status == "approved" else None,
                "themeCssHash": theme_hash if design_status == "approved" else None,
                "configHash": config_hash if design_status == "approved" else None,
                "structureHash": structure_hash if design_status == "approved" else None,
                "bundleHash": bundle_hash if design_status == "approved" else None,
                "compiledBundleHash": compiled_hash if design_status == "approved" else None,
                "hydration": (
                    {
                        "status": "passed",
                        "bundleHash": bundle_hash,
                        "expectedIslands": ["0:BuyBox"],
                        "hydratedIslands": ["0:BuyBox"],
                        "checkedAt": "2026-09-05T12:01:00Z",
                    }
                    if design_status == "approved"
                    else None
                ),
            },
            "sync": {
                "lastCompiledBundleHash": bundle_hash,
                "lastSyncedBundleHash": bundle_hash,
                "lastSyncedSectionHashes": section_hashes,
                "lastChangedSections": ["hero"],
                "remoteSourceHash": source_hash,
                "remoteBundleHash": bundle_hash,
            },
            "qa": {
                "status": "passed",
                "version": 2,
                "bundleHash": bundle_hash,
                "checks": {
                    "responsive": True,
                    "visualRegression": True,
                    "commerce": True,
                    "copy": True,
                    "claims": True,
                    "assets": True,
                    "integrity": True,
                },
            },
            "remote": {
                "pageId": "page",
                "lastKnownVersion": 2,
                "previewUrl": "https://preview.example",
            },
        }
        (root / "page-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        (root / "qa-report.md").write_text("# QA\nAll checks passed.\n", encoding="utf-8")
        return root

    def manifest(self, root: Path) -> dict:
        return json.loads((root / "page-manifest.json").read_text(encoding="utf-8"))

    def write_manifest(self, root: Path, manifest: dict) -> None:
        (root / "page-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    def codes(self, root: Path, phase: str) -> set[str]:
        return {item["code"] for item in VALIDATOR.validate_workspace(root, phase)["errors"]}

    def test_valid_workspace_passes_draft_and_publish(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        evidence = {
            "remote_source_hash": manifest["sync"]["remoteSourceHash"],
            "remote_bundle_hash": manifest["sync"]["remoteBundleHash"],
        }
        self.assertTrue(VALIDATOR.validate_workspace(root, "draft", **evidence)["ok"])
        self.assertTrue(VALIDATOR.validate_workspace(root, "publish", **evidence)["ok"])

    def test_progressive_plan_manifest_needs_no_design_state(self) -> None:
        root = self.make_workspace()
        for name in (
            "lexsis-source.html",
            "page-theme.css",
            "page-preview.html",
            "compile-artifact.json",
            "qa-report.md",
        ):
            (root / name).unlink(missing_ok=True)
        manifest = self.manifest(root)
        for key in ("config", "assets", "islands", "design", "sync", "qa", "remote"):
            manifest.pop(key, None)
        manifest["status"] = "planned"
        self.assertLess(len(json.dumps(manifest)), 1500)
        self.write_manifest(root, manifest)
        self.assertTrue(VALIDATOR.validate_workspace(root, "plan")["ok"])

    def test_design_passes_and_requires_generated_files(self) -> None:
        root = self.make_workspace()
        self.assertTrue(VALIDATOR.validate_workspace(root, "design")["ok"])
        (root / "page-preview.html").unlink()
        self.assertIn("missing_design_artifact", self.codes(root, "design"))

    def test_legacy_visual_skip_is_accepted(self) -> None:
        root = self.make_workspace("skipped")
        manifest = self.manifest(root)
        manifest["workflow"]["skippedSkills"] = ["visual-page"]
        self.write_manifest(root, manifest)
        self.assertTrue(VALIDATOR.validate_workspace(root, "precompile")["ok"])

    def test_source_and_config_drift_are_blocking(self) -> None:
        root = self.make_workspace()
        (root / "lexsis-source.html").write_text(
            SOURCE.replace("Creatine", "Changed", 1),
            encoding="utf-8",
        )
        self.assertIn("design_source_drift", self.codes(root, "precompile"))

        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["config"]["head"]["title"] = "Changed"
        self.write_manifest(root, manifest)
        self.assertIn("design_config_drift", self.codes(root, "precompile"))

    def test_compiled_runtime_markup_is_rejected_in_source(self) -> None:
        root = self.make_workspace("skipped")
        (root / "lexsis-source.html").write_text(
            '<!-- section: hero --><section id="hero">'
            '<div data-island="BuyBox" data-props="{}"></div></section>',
            encoding="utf-8",
        )
        self.assertIn("compiled_source_island", self.codes(root, "precompile"))

    def test_preview_placeholder_is_design_only(self) -> None:
        root = self.make_workspace("skipped")
        source = SOURCE.replace(
            "<p>Creatine</p>",
            '<p>Creatine</p><img src="assets/placeholders/hero-landscape.svg" alt="Hero">',
        )
        (root / "lexsis-source.html").write_text(source, encoding="utf-8")
        manifest = self.manifest(root)
        manifest["assets"] = [
            {
                "role": "hero",
                "sectionId": "hero",
                "sourceType": "preview-placeholder",
                "url": "assets/placeholders/hero-landscape.svg",
                "status": "preview-only",
            }
        ]
        self.write_manifest(root, manifest)
        self.assertNotIn("preview_asset_in_production", self.codes(root, "design"))
        self.assertIn("preview_asset_in_production", self.codes(root, "precompile"))

    def test_remote_hash_mismatch_blocks_draft(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["sync"]["remoteBundleHash"] = "wrong"
        self.write_manifest(root, manifest)
        result = VALIDATOR.validate_workspace(
            root,
            "draft",
            remote_source_hash=manifest["sync"]["remoteSourceHash"],
            remote_bundle_hash="live-wrong",
        )
        codes = {item["code"] for item in result["errors"]}
        self.assertIn("fidelity_failed", codes)
        self.assertIn("remote_evidence_mismatch", codes)

    def test_changed_sections_reports_only_modified_hero(self) -> None:
        root = self.make_workspace("skipped")
        baseline = """<!-- section: hero -->
<section id="hero"><h1>Original</h1></section>
<!-- section: faq -->
<section id="faq"><details><summary>Question</summary><p>Answer</p></details></section>
"""
        (root / "lexsis-source.html").write_text(
            baseline.replace("Original", "Improved"),
            encoding="utf-8",
        )
        manifest = self.manifest(root)
        manifest["sections"] = ["hero", "faq"]
        manifest["islands"] = []
        manifest["sync"]["lastSyncedSectionHashes"] = VALIDATOR.section_hashes(baseline)
        self.write_manifest(root, manifest)
        result = VALIDATOR.validate_workspace(root, "precompile")
        self.assertEqual(["hero"], result["changedSections"])

    def test_v2_migration_compacts_manifest_and_renames_preview(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["schemaVersion"] = 2
        manifest["pageConfig"] = {
            "head": manifest["config"]["head"],
            "scripts": [],
        }
        manifest["compileInputs"] = {
            "productBinding": manifest["config"]["productBinding"],
            "commerceConfig": {},
        }
        manifest["productBindings"] = manifest.pop("products")
        manifest["visual"] = {
            "status": "approved",
            "approvedSourceHash": manifest["design"]["sourceHash"],
            "approvedThemeCssHash": manifest["design"]["themeCssHash"],
            "approvedConfigHash": manifest["design"]["configHash"],
            "approvedStructureHash": manifest["design"]["structureHash"],
            "approvedBundleHash": manifest["design"]["bundleHash"],
            "approvedCompileBundleHash": manifest["design"]["compiledBundleHash"],
            "hydrationStatus": "passed",
            "hydrationEvidence": manifest["design"]["hydration"],
        }
        manifest["sourceSync"] = manifest.pop("sync")
        manifest["fidelity"] = {
            "remoteSourceHash": manifest["sourceSync"]["remoteSourceHash"],
            "remoteBundleHash": manifest["sourceSync"]["remoteBundleHash"],
        }
        manifest.pop("config")
        manifest.pop("design")
        manifest["workflow"]["skippedSkills"] = ["visual-page"]
        self.write_manifest(root, manifest)
        (root / "page-preview.html").rename(root / "visual-preview.html")

        result = MIGRATOR.migrate(root)

        self.assertTrue(result["changed"])
        migrated = self.manifest(root)
        self.assertEqual(3, migrated["schemaVersion"])
        self.assertEqual(["design-page"], migrated["workflow"]["skippedSkills"])
        self.assertNotIn("mcp", migrated)
        self.assertNotIn("fidelity", migrated)
        self.assertTrue((root / "page-preview.html").is_file())


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "skills/generate/scripts/validate_page_workspace.py"
SPEC = importlib.util.spec_from_file_location("validate_page_workspace", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


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
"""

PREVIEW = """<!doctype html>
<html>
  <body data-lx-visual-preview>
    <div data-island="BuyBox" data-props="{}"></div>
    <link rel="stylesheet" href="https://storefront.trylexsis.com/islands/storefront.css">
    <script src="https://storefront.trylexsis.com/islands/islands.js"></script>
    <script>window.LexsisIslands.hydrateIslands([]);</script>
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
        theme_path = theme_dir / "theme.css"
        setup_path = setup_dir / "setup.json"
        brand_path.write_text("# Brand\n", encoding="utf-8")
        theme_path.write_text(":root { --lx-accent-color: #111111; }\n", encoding="utf-8")
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
        (root / "qa-report.md").write_text("# QA\nAll checks passed.\n", encoding="utf-8")
        if visual_status == "approved":
            (root / "visual-source.html").write_text(SOURCE, encoding="utf-8")
            (root / "visual-preview.html").write_text(PREVIEW, encoding="utf-8")
        (root / "lexsis-source.html").write_text(SOURCE, encoding="utf-8")

        page_config = {
            "head": {"title": "Creatine"},
            "themeCss": ":root { --lx-accent-color: #111111; }",
            "scripts": [],
        }
        current_bundle_hash = MODULE.bundle_hash(SOURCE, page_config)
        hashes = MODULE.section_hashes(SOURCE)
        skipped = ["visual-page"] if visual_status == "skipped" else []
        manifest = {
            "schemaVersion": 1,
            "status": "qa_passed",
            "workflow": {"skippedSkills": skipped},
            "mcp": {
                "status": "connected",
                "checkedAt": "2026-09-04T12:00:00Z",
                "surfaceVersion": "3.0",
                "capabilities": [
                    {"router": "lexsis_pages", "actions": ["compile"]}
                ],
            },
            "page": {"title": "Creatine", "handle": "creatine", "archetype": "landing"},
            "workspaceId": "workspace",
            "storeId": "store",
            "themeId": "theme",
            "template": {
                "mode": "custom",
                "evaluatedTemplates": [],
                "selectionReason": "No suitable template matched the test fixture",
                "selectedAt": "2026-09-04T12:00:00Z",
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
            "themeCssPath": str(theme_path),
            "pageConfig": page_config,
            "productBindings": [{"productId": "product", "variantIds": ["variant"]}],
            "assets": [],
            "sections": ["hero"],
            "islands": [{
                "sectionId": "hero",
                "name": "BuyBox",
                "schema": {
                    "version": "5.0.0",
                    "lifecycleStatus": "active",
                    "resolvedAt": "2026-09-04T12:00:00Z",
                },
                "productionMode": "native",
                "previewMode": "hydrated",
                "previewData": True,
            }],
            "visual": {
                "status": visual_status,
                "sourcePath": "visual-source.html" if visual_status == "approved" else None,
                "previewPath": "visual-preview.html" if visual_status == "approved" else None,
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
                "commerce": True,
                "copy": True,
                "claims": True,
                "assets": True,
                "integrity": True,
            },
            "remote": {"pageId": "page", "lastKnownVersion": 2, "previewUrl": "https://preview.example"},
        }
        (root / "page-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return root

    def manifest(self, root: Path) -> dict:
        return json.loads((root / "page-manifest.json").read_text(encoding="utf-8"))

    def write_manifest(self, root: Path, manifest: dict) -> None:
        (root / "page-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    def codes(self, root: Path, phase: str) -> set[str]:
        return {item["code"] for item in MODULE.validate_workspace(root, phase)["errors"]}

    def test_valid_workspace_passes_publish_gate(self) -> None:
        result = MODULE.validate_workspace(self.make_workspace(), "publish")
        self.assertTrue(result["ok"], result)

    def test_interactive_visual_source_passes_visual_gate(self) -> None:
        result = MODULE.validate_workspace(self.make_workspace(), "visual")
        self.assertTrue(result["ok"], result)

    def test_explicit_visual_skip_passes_precompile(self) -> None:
        result = MODULE.validate_workspace(self.make_workspace("skipped"), "precompile")
        self.assertTrue(result["ok"], result)

    def test_adopted_page_does_not_require_visual_files(self) -> None:
        result = MODULE.validate_workspace(self.make_workspace("not-used"), "adopted")
        self.assertTrue(result["ok"], result)

    def test_approved_visual_requires_source_and_preview(self) -> None:
        root = self.make_workspace()
        (root / "visual-preview.html").unlink()
        self.assertIn("missing_visual_artifact", self.codes(root, "visual"))

    def test_visual_source_rejects_compiled_markup_and_custom_script(self) -> None:
        root = self.make_workspace()
        (root / "visual-source.html").write_text(
            '<!-- section: hero --><section id="hero">'
            '<div data-island="BuyBox" data-props="{}"></div>'
            '<script>console.log("no")</script></section>',
            encoding="utf-8",
        )
        codes = self.codes(root, "visual")
        self.assertIn("compiled_visual_island", codes)
        self.assertIn("visual_script", codes)

    def test_visual_preview_requires_runtime_and_no_template_tokens(self) -> None:
        root = self.make_workspace()
        (root / "visual-preview.html").write_text(
            "<body data-lx-visual-preview>{{SECTIONS_JSON}}</body>",
            encoding="utf-8",
        )
        codes = self.codes(root, "visual")
        self.assertIn("preview_runtime", codes)
        self.assertIn("preview_hydration", codes)
        self.assertIn("preview_template_token", codes)

    def test_empty_source_fails_precompile_and_publish(self) -> None:
        root = self.make_workspace()
        (root / "lexsis-source.html").write_text("", encoding="utf-8")
        for phase in ("precompile", "publish"):
            self.assertIn("empty_source", self.codes(root, phase))

    def test_manifest_requires_selected_store_theme_paths(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        del manifest["themeCssPath"]
        self.write_manifest(root, manifest)
        self.assertIn("manifest_binding", self.codes(root, "precompile"))

    def test_manifest_requires_successful_mcp_preflight(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["mcp"]["status"] = "blocked"
        self.write_manifest(root, manifest)
        self.assertIn("mcp_status", self.codes(root, "precompile"))

    def test_template_selection_requires_evidence(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["template"] = {"mode": "page-kit", "evaluatedTemplates": []}
        self.write_manifest(root, manifest)
        codes = self.codes(root, "precompile")
        self.assertIn("template_evidence", codes)
        self.assertIn("template_page_kit", codes)
        self.assertIn("template_sections", codes)

    def test_design_theme_must_match_page_theme(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["design"]["themeId"] = "other-theme"
        self.write_manifest(root, manifest)
        self.assertIn("design_theme", self.codes(root, "visual"))

    def test_island_requires_active_schema_evidence(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["islands"][0]["schema"]["lifecycleStatus"] = "deprecated"
        self.write_manifest(root, manifest)
        self.assertIn("island_schema_evidence", self.codes(root, "precompile"))

    def test_publish_requires_compiler_style_manifest(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["design"]["compiledStyleManifest"] = None
        self.write_manifest(root, manifest)
        self.assertIn("design_compile", self.codes(root, "publish"))

    def test_missing_setup_and_theme_files_fail(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        Path(manifest["setupPath"]).unlink()
        Path(manifest["themeCssPath"]).unlink()
        codes = self.codes(root, "precompile")
        self.assertIn("setup_missing", codes)
        self.assertIn("theme_css_missing", codes)

    def test_source_rejects_content_before_sections_and_duplicate_ids(self) -> None:
        root = self.make_workspace()
        (root / "lexsis-source.html").write_text(
            '<p>Outside</p><!-- section: hero --><section id="hero"><div id="hero"></div></section>',
            encoding="utf-8",
        )
        codes = self.codes(root, "precompile")
        self.assertIn("content_before_section", codes)
        self.assertIn("duplicate_html_id", codes)

    def test_head_change_invalidates_publish_bundle(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["pageConfig"]["head"]["title"] = "Changed"
        self.write_manifest(root, manifest)
        codes = self.codes(root, "publish")
        self.assertIn("compile_stale", codes)
        self.assertIn("source_not_synced", codes)

    def test_publish_requires_passing_current_qa(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["qa"]["commerce"] = False
        manifest["qa"]["checkedVersion"] = 1
        self.write_manifest(root, manifest)
        codes = self.codes(root, "publish")
        self.assertIn("qa_failed", codes)
        self.assertIn("qa_version", codes)

    def test_source_rejects_complete_page_image(self) -> None:
        root = self.make_workspace()
        (root / "lexsis-source.html").write_text(
            '<!-- section: hero --><section id="hero"><img src="https://cdn.trylexsis.com/page.png" alt="Page"></section>',
            encoding="utf-8",
        )
        self.assertIn("complete_page_image", self.codes(root, "precompile"))

    def test_source_rejects_renamed_local_media(self) -> None:
        root = self.make_workspace()
        source = SOURCE.replace(
            "<p>Creatine</p>",
            '<p>Creatine</p><img src="assets/hero-landscape.svg" alt="Hero">',
        )
        (root / "lexsis-source.html").write_text(source, encoding="utf-8")
        self.assertIn("relative_media_url", self.codes(root, "precompile"))

    def test_source_rejects_local_media_inside_island_json_and_css(self) -> None:
        root = self.make_workspace()
        source = SOURCE.replace(
            '"variants": []',
            '"variants": [], "image": "assets/product.svg"',
        ).replace(
            "</section>",
            "<style>#hero { background-image: url('assets/background.jpg'); }</style></section>",
        )
        (root / "lexsis-source.html").write_text(source, encoding="utf-8")
        self.assertIn("relative_media_url", self.codes(root, "precompile"))

    def test_remote_version_mismatch_is_blocking(self) -> None:
        root = self.make_workspace()
        result = MODULE.validate_workspace(
            root,
            "precompile",
            current_remote_version=3,
        )
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
        manifest["sourceSync"]["lastSyncedSectionHashes"] = MODULE.section_hashes(baseline)
        self.write_manifest(root, manifest)
        result = MODULE.validate_workspace(root, "precompile")
        self.assertEqual(["hero"], result["changedSections"])

    def test_preview_asset_is_allowed_visually_but_blocked_from_production(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["assets"] = [{
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
        }]
        self.write_manifest(root, manifest)
        self.assertNotIn("preview_asset_in_production", self.codes(root, "visual"))
        self.assertIn("preview_asset_in_production", self.codes(root, "precompile"))

    def test_shopify_asset_does_not_require_lexsis_asset_id(self) -> None:
        root = self.make_workspace()
        manifest = self.manifest(root)
        manifest["assets"] = [{
            "role": "product-gallery",
            "sectionId": "hero",
            "sourceType": "shopify",
            "productId": "gid://shopify/Product/1",
            "mediaId": "gid://shopify/MediaImage/1",
            "url": "https://cdn.shopify.com/image.jpg",
            "width": 1200,
            "height": 1200,
            "desktopCrop": "center",
            "mobileCrop": "center",
            "altTextIntent": "Product image",
            "verificationStatus": "verified",
        }]
        self.write_manifest(root, manifest)
        self.assertNotIn("asset_identity", self.codes(root, "precompile"))


if __name__ == "__main__":
    unittest.main()

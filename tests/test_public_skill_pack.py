#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

EXPECTED_PUBLIC_SKILLS = {
    "setup",
    "plan-page",
    "visual-page",
    "asset-prep",
    "generate",
    "publish",
    "analyze-page",
    "optimize",
    "experiment",
    "cart",
}


class PublicSkillPackTests(unittest.TestCase):
    def test_public_command_set_is_exact(self) -> None:
        actual = {
            path.parent.name
            for path in SKILLS.glob("*/SKILL.md")
        }
        self.assertEqual(EXPECTED_PUBLIC_SKILLS, actual)
        self.assertFalse((SKILLS / "storefront-engine" / "SKILL.md").exists())

    def test_each_public_skill_has_consistent_openai_metadata(self) -> None:
        for name in EXPECTED_PUBLIC_SKILLS:
            metadata = SKILLS / name / "agents" / "openai.yaml"
            self.assertTrue(metadata.is_file(), name)
            text = metadata.read_text(encoding="utf-8")
            self.assertIn(f"${name}", text, name)
            self.assertIn("https://mcp.trylexsis.com/mcp", text, name)

    def test_visual_preview_assets_are_complete(self) -> None:
        visual_assets = SKILLS / "visual-page" / "assets"
        shell = (visual_assets / "preview-shell.html").read_text(encoding="utf-8")
        for token in (
            "{{THEME_CSS}}",
            "{{COMPILED_SECTION_CSS}}",
            "{{COMPILED_SECTION_MARKUP}}",
            "{{SECTIONS_JSON}}",
            "{{TEST_CART_DATA_JSON}}",
            "{{COMMERCE_CONFIG_JSON}}",
            "{{PRODUCT_BINDING_JSON}}",
        ):
            self.assertIn(token, shell)
        self.assertIn("LexsisIslands.hydrateIslands", shell)
        self.assertNotIn("Content-Security-Policy", shell)
        self.assertNotIn("window.fetch =", shell)
        self.assertNotIn("XMLHttpRequest.prototype.open", shell)
        self.assertNotIn("navigator.sendBeacon =", shell)
        self.assertNotIn("window.open =", shell)

        placeholders = visual_assets / "placeholders"
        expected = {
            "hero-landscape.svg",
            "product-square.svg",
            "lifestyle-portrait.svg",
            "video-poster.svg",
            "avatar.svg",
        }
        self.assertEqual(expected, {path.name for path in placeholders.glob("*.svg")})

    def test_visual_preview_builder_assembles_compiled_island_output(self) -> None:
        script_path = (
            SKILLS / "visual-page" / "scripts" / "build_visual_preview.py"
        )
        spec = importlib.util.spec_from_file_location(
            "build_visual_preview",
            script_path,
        )
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        preview = module.build_preview(
            {
                "page": {
                    "sections": [
                        {
                            "id": "video",
                            "html": (
                                '<section id="video">'
                                '<div data-island="ShoppableVideoFeed" '
                                'data-props="{}"></div></section>'
                            ),
                            "css": "#video { min-height: 80vh; }",
                            "js": "",
                        }
                    ]
                }
            },
            theme_css=":root { --lx-accent-color: #111; }",
        )
        self.assertIn('data-section-id="video"', preview)
        self.assertIn('data-island="ShoppableVideoFeed"', preview)
        self.assertIn("LexsisIslands.hydrateIslands", preview)
        self.assertNotIn("{{SECTIONS_JSON}}", preview)

    def test_full_pack_discovery_includes_shared_resources(self) -> None:
        for root in (
            ROOT / ".agents" / "skills",
            ROOT / "plugins" / "lexsis-storefront-skills" / "skills",
        ):
            self.assertTrue(
                (
                    root
                    / "storefront-engine"
                    / "references"
                    / "source-artifact-workflow.md"
                ).is_file()
            )


if __name__ == "__main__":
    unittest.main()

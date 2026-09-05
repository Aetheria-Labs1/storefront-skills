#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
PLUGIN_AGENTS = ROOT / "plugins" / "lexsis-storefront-skills" / "agents"

EXPECTED_PUBLIC_SKILLS = {
    "setup",
    "plan-page",
    "design-page",
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
        design_assets = SKILLS / "design-page" / "assets"
        shell = (design_assets / "preview-shell.html").read_text(encoding="utf-8")
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
        self.assertIn("__LEXSIS_PREVIEW_STATUS__", shell)
        self.assertIn("data-lx-hydration-status", shell)
        self.assertIn('"pending-triggers"', shell)
        self.assertIn("Immediate islands did not hydrate", shell)
        self.assertNotIn("Islands did not hydrate:", shell)
        self.assertNotIn("Content-Security-Policy", shell)
        self.assertNotIn("window.fetch =", shell)
        self.assertNotIn("XMLHttpRequest.prototype.open", shell)
        self.assertNotIn("navigator.sendBeacon =", shell)
        self.assertNotIn("window.open =", shell)

        placeholders = design_assets / "placeholders"
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
            SKILLS / "design-page" / "scripts" / "build_page_preview.py"
        )
        spec = importlib.util.spec_from_file_location(
            "build_page_preview",
            script_path,
        )
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        preview = module.build_preview(
            {
                "response": {
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

    def test_claude_plugin_contains_materialized_skills(self) -> None:
        plugin_skills = (
            ROOT / "plugins" / "lexsis-storefront-skills" / "skills"
        )
        self.assertTrue(plugin_skills.is_dir())
        self.assertFalse(plugin_skills.is_symlink())
        self.assertEqual(
            EXPECTED_PUBLIC_SKILLS,
            {
                path.parent.name
                for path in plugin_skills.glob("*/SKILL.md")
            },
        )
        for source in SKILLS.rglob("*"):
            if (
                not source.is_file()
                or "__pycache__" in source.parts
                or source.suffix == ".pyc"
            ):
                continue
            packaged = plugin_skills / source.relative_to(SKILLS)
            self.assertTrue(packaged.is_file(), source)
            self.assertEqual(source.read_bytes(), packaged.read_bytes(), source)

    def test_active_skill_docs_use_one_html_source(self) -> None:
        for path in SKILLS.rglob("*.md"):
            self.assertNotIn("visual-source.html", path.read_text(encoding="utf-8"), path)

    def test_design_lint_fixture_exit_codes(self) -> None:
        script = SKILLS / "design-page" / "scripts" / "design_lint.py"
        fixtures = ROOT / "tests" / "fixtures" / "design-lint"
        rejected = subprocess.run(
            [sys.executable, str(script), str(fixtures / "rejected")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(rejected.returncode, 1, rejected.stdout)
        self.assertRegex(rejected.stdout, r"N1 emoji\s+1[0-9]\s+FAIL")
        corrected = subprocess.run(
            [sys.executable, str(script), str(fixtures / "corrected")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(corrected.returncode, 0, corrected.stdout)
        with tempfile.TemporaryDirectory() as tmp:
            allowed = Path(tmp)
            for name in ("lexsis-source.html", "page-theme.css"):
                (allowed / name).write_bytes((fixtures / "rejected" / name).read_bytes())
            (allowed / "page-plan.md").write_text(
                '**Emoji in copy.** allowed: "please keep the emoji in the ticker copy"\n',
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(script), str(allowed)], capture_output=True, text=True
            )
        self.assertRegex(result.stdout, r"N1 emoji \(plan allows in copy\)\s+1[0-9]\s+PASS")
        self.assertEqual(result.returncode, 1, "other rules still fail on the rejected fixture")

    def test_house_rules_are_wired(self) -> None:
        references = SKILLS / "storefront-engine" / "references"
        self.assertTrue((references / "design-rules.md").is_file())
        self.assertTrue((references / "island-presets.md").is_file())
        rules = (references / "design-rules.md").read_text(encoding="utf-8")
        self.assertEqual(rules.count("\n```") % 2, 0, "unclosed code fence in design-rules.md")
        wired = [
            path
            for path in [*SKILLS.rglob("SKILL.md"), *PLUGIN_AGENTS.glob("*.md"), *references.glob("*.md")]
            if "design-rules.md" in path.read_text(encoding="utf-8")
        ]
        self.assertGreaterEqual(len(wired), 10, [p.name for p in wired])
        for name in (
            "storefront-craft",
            "conversion-psychology",
            "animation-system",
            "visual-craft",
            "premium-patterns",
            "plan-page",
            "generation-protocol",
        ):
            text = (references / f"{name}.md").read_text(encoding="utf-8")
            self.assertIn("House rules in `storefront-engine/references/design-rules.md`", text, name)
            self.assertNotIn("hover:scale", text, name)
        self.assertNotIn(
            "Color Temperature Flow",
            (references / "plan-page.md").read_text(encoding="utf-8"),
        )
        plan = (SKILLS / "plan-page" / "SKILL.md").read_text(encoding="utf-8")
        for block in ("## Design direction", "### Imagery and background plan", "### Asset slots", "## Parallel Planning"):
            self.assertIn(block, plan)
        design = (SKILLS / "design-page" / "SKILL.md").read_text(encoding="utf-8")
        for block in ("## Design Direction Gate", "## Self-Critique Gate", "## Asset Gap Confirmation", "design-critique.md"):
            self.assertIn(block, design)

    def test_plan_page_does_not_choose_islands(self) -> None:
        text = (SKILLS / "plan-page" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("must not define islands", text)
        self.assertNotIn("required islands", text.lower())
        self.assertNotIn("island_schema", text)
        self.assertIn("occasion dates", text)
        self.assertIn("shelf is empty", text)
        self.assertIn("### Proof sources", text)
        self.assertIn("Design template selection", text)
        self.assertIn("Design asset selection", text)
        self.assertNotIn("reviewsEndpoint", text)

    def test_design_page_compiles_early_and_allows_lazy_hydration(self) -> None:
        text = (SKILLS / "design-page" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Compile the rough complete source", text)
        self.assertIn("validation_errors", text)
        self.assertIn("ROUGH_PREVIEW", text)
        self.assertIn("pending until their trigger", text)
        self.assertIn("DESIGN_PREVIEW_READY_QA_PENDING", text)

    def test_visual_page_was_replaced(self) -> None:
        self.assertFalse((SKILLS / "visual-page").exists())
        self.assertTrue((SKILLS / "design-page" / "SKILL.md").is_file())

    def test_discovery_is_not_a_global_blocker(self) -> None:
        checked = [
            *SKILLS.rglob("*.md"),
            ROOT / "scripts" / "build-distributions.py",
            *(
                ROOT / "plugins" / "lexsis-storefront-skills" / "agents"
            ).glob("*.md"),
        ]
        for path in checked:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("BLOCKED_LEXSIS_MCP", text, path)

        contract = (
            SKILLS
            / "storefront-engine"
            / "references"
            / "lexsis-mcp-contract.md"
        ).read_text(encoding="utf-8")
        self.assertIn("A response with `ok: true` and `count: 0` is a", contract)
        self.assertIn('"router": "lexsis_catalog"', contract)
        self.assertIn('"action": "list"', contract)


if __name__ == "__main__":
    unittest.main()

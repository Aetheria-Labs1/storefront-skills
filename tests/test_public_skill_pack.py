#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
PLUGIN_AGENTS = ROOT / "agents"

EXPECTED_PUBLIC_SKILLS = {
    "setup",
    "plan-page",
    "design-page",
    "asset-prep",
    "generate",
    "publish",
    "analyze-page",
    "optimize",
    "ab-test",
    "cart",
    "build",
    "build-with-template",
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

    def test_local_preview_renderer_is_removed(self) -> None:
        design = SKILLS / "design-page"
        self.assertFalse((design / "assets" / "preview-shell.html").exists())
        self.assertFalse((design / "assets" / "placeholders").exists())
        self.assertFalse((design / "scripts" / "build_page_preview.py").exists())
        self.assertFalse((design / "references" / "island-preview.md").exists())
        for path in [
            *SKILLS.rglob("*.md"),
            *SKILLS.rglob("*.py"),
            ROOT / "README.md",
            *PLUGIN_AGENTS.glob("*.md"),
        ]:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("page-preview.html", text, path)
            self.assertNotIn("build_page_preview.py", text, path)

    def test_full_pack_discovery_includes_shared_resources(self) -> None:
        for root in (
            ROOT / ".agents" / "skills",
            ROOT / "skills",
        ):
            self.assertTrue(
                (
                    root
                    / "storefront-engine"
                    / "references"
                    / "source-artifact-workflow.md"
                ).is_file()
            )

    def test_each_public_skill_is_self_contained_for_skills_cli(self) -> None:
        reference_re = re.compile(r"`(references/[A-Za-z0-9_./-]+\.md)`")
        for name in EXPECTED_PUBLIC_SKILLS:
            skill_dir = SKILLS / name
            text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            self.assertNotIn("storefront-engine/references/", text, name)
            for reference in reference_re.findall(text):
                self.assertTrue((skill_dir / reference).is_file(), (name, reference))

            for packaged_reference in (skill_dir / "references").glob("*.md"):
                packaged_text = packaged_reference.read_text(encoding="utf-8")
                self.assertNotIn(
                    "storefront-engine/references/",
                    packaged_text,
                    packaged_reference,
                )
                for referenced_name in re.findall(
                    r"(?:`|\()(?:(?:references/)?)([A-Za-z0-9_-]+\.md)(?:`|\))",
                    packaged_text,
                ):
                    if (SKILLS / "storefront-engine" / "references" / referenced_name).is_file():
                        self.assertTrue(
                            (skill_dir / "references" / referenced_name).is_file(),
                            (name, packaged_reference.name, referenced_name),
                        )

    def test_claude_plugin_uses_the_canonical_skill_tree(self) -> None:
        self.assertTrue((ROOT / ".claude-plugin" / "plugin.json").is_file())
        self.assertTrue((ROOT / ".mcp.json").is_file())
        self.assertTrue((ROOT / "agents" / "page-builder.md").is_file())
        self.assertTrue((ROOT / "agents" / "cro-analyzer.md").is_file())
        self.assertFalse((ROOT / "plugins" / "lexsis-storefront-skills").exists())
        marketplace = json.loads(
            (ROOT / ".claude-plugin" / "marketplace.json").read_text()
        )
        self.assertEqual("./", marketplace["plugins"][0]["source"])

    def test_active_skill_docs_use_one_html_source(self) -> None:
        for path in SKILLS.rglob("*.md"):
            self.assertNotIn("visual-source.html", path.read_text(encoding="utf-8"), path)

    def test_design_lint_fixture_exit_codes(self) -> None:
        script = ROOT / "tests/support/design_lint.py"
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
            "visual-craft",
            "premium-patterns",
            "plan-page",
            "generation-protocol",
        ):
            text = (references / f"{name}.md").read_text(encoding="utf-8")
            self.assertIn("design-rules.md", text, name)
            self.assertNotIn("hover:scale", text, name)
        motion = (references / "animation-system.md").read_text(encoding="utf-8")
        self.assertIn("references/design-rules.md", motion)
        self.assertNotIn("override every example below", motion)
        self.assertNotIn(
            "Color Temperature Flow",
            (references / "plan-page.md").read_text(encoding="utf-8"),
        )
        plan = (SKILLS / "plan-page" / "SKILL.md").read_text(encoding="utf-8")
        for block in ("## Design direction", "### Imagery and background plan", "### Asset slots", "## Parallel Planning"):
            self.assertIn(block, plan)
        self.assertIn("Consumer decision model", plan)
        design = (SKILLS / "design-page" / "SKILL.md").read_text(encoding="utf-8")
        for block in (
            "## Design Direction Gate",
            "## Hosted Design Review",
            "## Asset Gap Confirmation",
            "hosted URL and tested version",
        ):
            self.assertIn(block, design)

    def test_consumer_behavior_framework_is_wired_to_page_decisions(self) -> None:
        reference = (
            SKILLS
            / "storefront-engine"
            / "references"
            / "consumer-behavior-cro.md"
        )
        text = reference.read_text(encoding="utf-8")
        for phrase in (
            "Classify the visitor's likely primary mode",
            "Select at most three behavioral patterns",
            "Gallery Job Coverage",
            "two or three relevant products",
            "Do not add a carousel",
            'Never ask "Do you want custom images?"',
            "## Consumer decision model",
        ):
            self.assertIn(phrase, text)

        for skill_name in (
            "plan-page",
            "design-page",
            "build",
            "build-with-template",
            "generate",
            "optimize",
            "ab-test",
        ):
            skill = (SKILLS / skill_name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("references/consumer-behavior-cro.md", skill, skill_name)
            self.assertTrue(
                (
                    SKILLS
                    / skill_name
                    / "references"
                    / "consumer-behavior-cro.md"
                ).is_file(),
                skill_name,
            )

    def test_plan_page_does_not_choose_islands(self) -> None:
        text = (SKILLS / "plan-page" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("must not define islands", text)
        self.assertNotIn("required islands", text.lower())
        self.assertNotIn("island_schema", text)
        self.assertIn("occasion dates", text)
        self.assertIn("shelf is empty", text)
        self.assertIn("### Proof ledger", text)
        self.assertIn("### Offer ledger", text)
        self.assertIn("## Identify the Page Type", text)
        self.assertIn("Review the checklist", text)
        self.assertIn("lexsis_assets.view", text)
        self.assertIn("section-asset-workflow.md", text)
        self.assertIn("Design template selection", text)
        self.assertIn("Design asset selection", text)
        self.assertNotIn("reviewsEndpoint", text)

    def test_design_page_compiles_and_creates_the_hosted_draft(self) -> None:
        text = (SKILLS / "design-page" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Compile the rough complete source", text)
        self.assertIn("validation_errors", text)
        self.assertIn("lexsis_page_create.create", text)
        self.assertIn("publish:false", text)
        self.assertIn("design.status: pending-approval", text)
        self.assertIn("Return the hosted preview immediately as `DRAFT_CREATED`", text)
        self.assertIn("## Page-Type Workflow", text)
        self.assertIn("generation-policy.md", text)
        self.assertIn("lexsis_assets.view", text)
        self.assertNotIn("page-preview.html", text)

    def test_generate_routes_intent_and_creates_before_ready_qa(self) -> None:
        text = (SKILLS / "generate" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Infer intent from the whole request and conversation", text)
        self.assertIn("fast-draft", text)
        self.assertIn("production-ready", text)
        self.assertLess(
            text.index("lexsis_page_create.create"),
            text.index("Production-Ready Follow-Through"),
        )
        self.assertIn("DRAFT_CREATED", text)
        self.assertIn("DRAFT_READY", text)
        self.assertIn("No workspace adapter", text)
        self.assertIn("Do not call\n`lexsis_page_create.create` again", text)

    def test_design_page_supports_optional_existing_tool_concepts(self) -> None:
        text = (SKILLS / "design-page" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("## Choose the Visual Route", text)
        self.assertIn("CONCEPT_READY", text)
        self.assertIn("references/design-concepts.md", text)
        reference = (
            SKILLS / "storefront-engine" / "references" / "design-concepts.md"
        ).read_text(encoding="utf-8")
        self.assertIn("lexsis_drafts` action `asset_generate", reference)
        self.assertIn("lexsis_assets` action `view", reference)
        self.assertIn("never page media", reference)

    def test_fast_build_commands_are_bounded_draft_only_workflows(self) -> None:
        for name in ("build", "build-with-template"):
            text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("publish:false", text)
            self.assertIn("DRAFT_CREATED", text)
            self.assertIn("one targeted repair", text)
            self.assertIn("references/fast-build.md", text)

        reference = (
            SKILLS / "storefront-engine" / "references" / "fast-build.md"
        ).read_text(encoding="utf-8")
        self.assertLess(
            reference.index("lexsis_page_create"),
            reference.index("## After the First Draft"),
        )
        self.assertIn("workflow.skippedSkills", reference)
        self.assertIn("Do not run repeated repair loops", reference)

    def test_ab_test_is_url_first_local_first_and_draft_only(self) -> None:
        text = (SKILLS / "ab-test" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("supplied URL", text)
        self.assertIn("page_duplicate", text)
        self.assertIn("experiment_create", text)
        self.assertIn("Do not use `page_variation`", text)
        reference = (
            SKILLS / "storefront-engine" / "references" / "ab-testing.md"
        ).read_text(encoding="utf-8")
        self.assertIn("AB_TEST_PLAN_READY", reference)
        self.assertIn("AB_VARIANTS_READY", reference)
        self.assertIn("AB_TEST_DRAFT_CREATED", reference)
        self.assertIn("Sub-agents never spend credits", reference)
        self.assertFalse((SKILLS / "experiment").exists())

    def test_public_skills_ship_no_local_page_qa_tooling(self) -> None:
        for skill in ("generate", "design-page", "plan-page"):
            self.assertEqual(list((SKILLS / skill / "scripts").glob("*.py")), [])
        for path in [*SKILLS.glob("*/SKILL.md"), *PLUGIN_AGENTS.glob("*.md")]:
            content = path.read_text()
            for retired in ("lexsis-source.html", "page-theme.css", "plan_lint.py", "design_lint.py", "prepare_workspace_compile", "validate_page_workspace"):
                self.assertNotIn(retired, content, path)
        source = (SKILLS / "storefront-engine/references/source-artifact-workflow.md").read_text()
        self.assertIn("Never combine the two input modes", source)
        self.assertIn("expected_version", source)
        self.assertIn("only preview", source)

    def test_visual_page_was_replaced(self) -> None:
        self.assertFalse((SKILLS / "visual-page").exists())
        self.assertTrue((SKILLS / "design-page" / "SKILL.md").is_file())

    def test_release_version_is_7_9_0(self) -> None:
        for path in (
            ROOT / ".claude-plugin" / "plugin.json",
            ROOT / "codex" / ".codex-plugin" / "plugin.json",
        ):
            self.assertEqual("7.9.0", json.loads(path.read_text())["version"])

    def test_discovery_is_not_a_global_blocker(self) -> None:
        checked = [
            *SKILLS.rglob("*.md"),
            ROOT / "scripts" / "build-distributions.py",
            *PLUGIN_AGENTS.glob("*.md"),
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

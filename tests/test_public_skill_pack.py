#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
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
    "visualize-page",
    "plan-assets",
    "design-page",
    "optimize",
    "publish",
    "cart",
    "ab-test",
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
        for block in (
            "## 1. Establish the Brief",
            "## 3. Identify One Page Type",
            "## 5. Finalize Copy, Proof, and Layout",
            "## 6. Define Production Asset Requirements",
            "## 7. Choose Template Direction",
            "## 8. Produce and Approve the Plan",
        ):
            self.assertIn(block, plan)
        contract = (references / "plan-page.md").read_text(encoding="utf-8")
        for block in (
            "## Consumer decision model",
            "## Section specification",
            "## Claim gate",
            "## Asset requirements",
            "## Plan status",
        ):
            self.assertIn(block, contract)
        design = (SKILLS / "design-page" / "SKILL.md").read_text(encoding="utf-8")
        for block in (
            "## 1. Enforce the Handoff",
            "## 3. Resolve the Implementation",
            "## 4. Compile Early",
            "## 5. Create or Update One Draft",
            "## 6. Run Hosted Review",
            "PLAN_APPROVED",
            "ASSETS_READY",
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

        for skill_name in ("optimize", "ab-test"):
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
        planning_rules = (
            SKILLS
            / "storefront-engine"
            / "references"
            / "planning-rules.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Classify the primary visitor mode",
            "three to five questions",
            "Use at most three behavioural patterns",
            "Do not add carousels",
        ):
            self.assertIn(phrase, planning_rules)

    def test_plan_page_does_not_choose_islands(self) -> None:
        text = (SKILLS / "plan-page" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Do not choose\nislands", text)
        self.assertNotIn("island_schema", text)
        self.assertIn("There is no fixed question limit", text)
        self.assertIn("Sections are decided before templates", text)
        self.assertIn("shelf is empty", text)
        self.assertIn("Review the checklist", text)
        self.assertIn("lexsis_template_library.search_page_kits", text)
        self.assertIn("lexsis_capture.funnel_templates", text)
        self.assertIn("PLAN_READY_FOR_APPROVAL", text)
        self.assertIn("PLAN_APPROVED", text)
        self.assertNotIn("reviewsEndpoint", text)
        for action in (
            "lexsis_asset_library.search",
            "lexsis_assets.view",
            "lexsis_asset_import.import",
            "lexsis_asset_upload.upload",
            "lexsis_workspace.credits",
            "lexsis_drafts.asset_generate",
        ):
            self.assertNotIn(action, text, action)
        for retired in ("fast-draft", "fast-build", "`/build`", "DRAFT_READY"):
            self.assertNotIn(retired, text, retired)

    def test_visualize_page_is_optional_and_concept_only(self) -> None:
        text = (SKILLS / "visualize-page" / "SKILL.md").read_text(encoding="utf-8")
        for phrase in (
            "PLAN_APPROVED",
            "concept-only",
            "VISUAL_DIRECTION_IN_REVIEW",
            "VISUAL_DIRECTION_APPROVED",
            "VISUAL_DIRECTION_SKIPPED",
            "Regenerate only rejected frames",
            "Do not assume a particular external tool exists",
            "Generate the 390 mobile concept first for every frame",
            "Mobile is the canonical",
            "infer the 768/1280 treatment",
            "generate a larger-screen concept image only when the user asks",
            "## Responsive asset implications",
            "Mobile aspect and target",
            "Larger-screen aspect and target",
        ):
            self.assertIn(phrase, text, phrase)
        self.assertIn("URLs are never placed in the page", text)
        self.assertNotIn("Generate desktop concepts first", text)

    def test_plan_assets_owns_asset_execution(self) -> None:
        text = (SKILLS / "plan-assets" / "SKILL.md").read_text(encoding="utf-8")
        for phrase in (
            "lexsis_catalog.get",
            "lexsis_asset_library.search",
            "lexsis_assets.view",
            "lexsis_assets.capabilities",
            "lexsis_asset_import.import",
            "lexsis_asset_upload.upload",
            "lexsis_workspace.credits",
            "lexsis_drafts.asset_generate",
            "Search and visual inspection always precede generation",
            "ASSETS_READY",
            "ASSETS_PENDING_USER",
            "ASSETS_BLOCKED",
            "verified official source or merchant upload",
            "## 2. Resolve Mobile Before Larger Screens",
            "mobile asset first",
            "Full-width mobile imagery",
            "target at least 1600px wide and prefer 1920px",
            "Design Library link",
            "do not treat opening the dashboard as a completed selection",
        ):
            self.assertIn(phrase, text, phrase)
        self.assertIn(
            "https://app.trylexsis.com/workspaces/<workspace-id>/storefront/design-library?theme=<theme-id>&tab=assets",
            text,
        )
        for example_id in (
            "829550b2-bd37-411b-9949-ff57a4fce18b",
            "831f51ce-481b-492b-923e-2d6e361cf7f5",
        ):
            self.assertNotIn(example_id, text)

    def test_asset_requirements_are_mobile_first_and_size_specific(self) -> None:
        plan = (
            SKILLS
            / "storefront-engine"
            / "references"
            / "plan-page.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Mobile aspect/crop/pixels",
            "Larger-screen aspect/crop/pixels",
            "1080x1350",
            "1800x1200",
            "1080x1920",
            "1920x1080",
            "same master, art-directed crops",
        ):
            self.assertIn(phrase, plan, phrase)

    def test_new_asset_workflow_is_provider_neutral(self) -> None:
        paths = (
            SKILLS / "visualize-page" / "SKILL.md",
            SKILLS / "plan-assets" / "SKILL.md",
            SKILLS / "storefront-engine" / "references" / "asset-prep.md",
            ROOT / "README.md",
        )
        for path in paths:
            text = path.read_text(encoding="utf-8").lower()
            for provider in ("higgsfield", "openart"):
                self.assertNotIn(provider, text, path)

    def test_setup_builds_structured_store_context(self) -> None:
        text = (SKILLS / "setup" / "SKILL.md").read_text(encoding="utf-8")
        for phrase in (
            "work/storefront/",
            "setup.md",
            "brand.md",
            "design.md",
            "products.md",
            "persona.md",
            "rules.md",
            "themes/<theme-id>.css",
            "Page through `lexsis_catalog.list` until no next cursor remains",
            "Preserve stable persona ids",
            "evidence-supported inference",
            "Always write\n`setup.md` last",
            "design.md` always binds to the store's default working theme",
            "Use available web search or browser research",
            "ask the user",
            "source URL or source action and the access/refresh date",
            "record the item as an open question",
        ):
            self.assertIn(phrase, text, phrase)
        for removed_action in (
            "lexsis_campaigns.creatives",
            "lexsis_campaigns.personas",
            "get_ad_creatives",
            "list_personas",
        ):
            self.assertNotIn(removed_action, text, removed_action)

    def test_design_page_compiles_and_creates_the_hosted_draft(self) -> None:
        text = (SKILLS / "design-page" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Compile the complete rough source", text)
        self.assertIn("validation_errors", text)
        self.assertIn("lexsis_page_create.create", text)
        self.assertIn("publish:false", text)
        self.assertIn("design.status: pending-approval", text)
        self.assertIn("Return the hosted preview immediately", text)
        self.assertIn("references/design-authoring.md", text)
        self.assertIn("references/hosted-design-review.md", text)
        self.assertNotIn("page-preview.html", text)
        for phrase in (
            "PLAN_APPROVED",
            "ASSETS_READY",
            "DESIGN_APPROVED",
            "768",
            "lexsis_drafts.page_record_qa",
            "expected_version",
        ):
            self.assertIn(phrase, text, phrase)
        for retired in (
            "DRAFT_READY",
            "`/generate`",
            "fast-draft",
            "lexsis_asset_library.search",
            "lexsis_asset_import.import",
            "lexsis_asset_upload.upload",
            "lexsis_drafts.asset_generate",
            "CONCEPT_READY",
            "PLAN_READY_FOR_DESIGN",
            "PLAN_COMPLETE - asset tasks pending",
        ):
            self.assertNotIn(retired, text, retired)

    def test_optimize_scores_plans_and_applies(self) -> None:
        text = (SKILLS / "optimize" / "SKILL.md").read_text(encoding="utf-8")
        for phrase in (
            "## Scorecard",
            "## Findings by section",
            "## Asset slots",
            "## Claim gate",
            "## Work queue",
            "OPTIMIZATION_PLAN_READY",
            "DESIGN_APPROVED",
            "expected_version",
            "lexsis_assets.view",
            "references/plan-page.md",
            "lexsis_analytics.page",
        ):
            self.assertIn(phrase, text, phrase)

    def test_publish_gates_on_design_approved(self) -> None:
        publish = (SKILLS / "publish" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("DESIGN_APPROVED", publish)
        for path in [
            *SKILLS.glob("*/SKILL.md"),
            *PLUGIN_AGENTS.glob("*.md"),
            ROOT / "README.md",
            ROOT / "AGENTS.md",
        ]:
            text = path.read_text(encoding="utf-8")
            for retired in (
                "DRAFT_READY",
                "`/generate`",
                "`/build`",
                "`/build-with-template`",
                "`/analyze-page`",
                "`/asset-prep`",
                "fast-build",
            ):
                self.assertNotIn(retired, text, (path, retired))

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
        for skill in (
            "design-page",
            "plan-page",
            "visualize-page",
            "plan-assets",
            "optimize",
        ):
            self.assertEqual(list((SKILLS / skill / "scripts").glob("*.py")), [])
        for path in [*SKILLS.glob("*/SKILL.md"), *PLUGIN_AGENTS.glob("*.md")]:
            content = path.read_text()
            for retired in ("lexsis-source.html", "page-theme.css", "plan_lint.py", "design_lint.py", "prepare_workspace_compile", "validate_page_workspace"):
                self.assertNotIn(retired, content, path)
        source = (SKILLS / "storefront-engine/references/source-artifact-workflow.md").read_text()
        self.assertIn("Never combine the two input modes", source)
        self.assertIn("expected_version", source)
        self.assertIn("only preview", source)

    def test_visualize_page_replaces_the_old_visual_page_name(self) -> None:
        self.assertFalse((SKILLS / "visual-page").exists())
        self.assertTrue((SKILLS / "visualize-page" / "SKILL.md").is_file())

    def test_skill_frontmatter_survives_a_strict_yaml_parser(self) -> None:
        """The skills CLI drops any SKILL.md whose frontmatter fails YAML parsing."""
        hazard = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*): (\S.*)$")
        for path in [*SKILLS.glob("*/SKILL.md"), *PLUGIN_AGENTS.glob("*.md")]:
            front = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
            self.assertIsNotNone(front, path)
            for line in front.group(1).split("\n"):
                found = hazard.match(line)
                if not found or found.group(2)[0] in "\"'|>[{&*!":
                    continue
                for unsafe in (": ", " #"):
                    self.assertNotIn(unsafe, found.group(2), (path, found.group(1)))
        if importlib.util.find_spec("yaml"):
            import yaml

            for path in [*SKILLS.glob("*/SKILL.md"), *PLUGIN_AGENTS.glob("*.md")]:
                front = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
                yaml.safe_load(front.group(1))

    def test_release_version_is_8_0_2(self) -> None:
        for path in (
            ROOT / ".claude-plugin" / "plugin.json",
            ROOT / "codex" / ".codex-plugin" / "plugin.json",
        ):
            self.assertEqual("8.0.2", json.loads(path.read_text())["version"])

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

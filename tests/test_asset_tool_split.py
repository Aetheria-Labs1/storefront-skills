from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REFERENCES = SKILLS / "storefront-engine" / "references"


class AssetToolSplitTests(unittest.TestCase):
    def test_documentation_does_not_route_import_through_upload(self) -> None:
        obsolete_action = re.compile(
            r"lexsis_asset_upload(?:\.import|`?\s+(?:→|action)\s+`?import"
            r"|\(\{\s*action:\s*[\"']import[\"'])|lexsis_asset_import\.upload"
        )
        documents = [
            *SKILLS.rglob("*.md"),
            *(ROOT / "gpt").glob("*.md"),
            *(ROOT / "agents").glob("*.md"),
        ]
        stale = [
            str(path.relative_to(ROOT))
            for path in documents
            if obsolete_action.search(path.read_text(encoding="utf-8"))
        ]
        self.assertFalse(stale, f"{len(stale)} stale documents: {stale[:10]}")

    def test_asset_workflows_expose_import_and_upload_separately(self) -> None:
        documents = [
            SKILLS / name / "SKILL.md"
            for name in ("plan-page", "design-page", "optimize")
        ]
        documents.extend(
            REFERENCES / name
            for name in (
                "asset-prep.md",
                "lexsis-mcp-contract.md",
                "assets/asset-sourcing-sequence.md",
                "workflows/section-asset-workflow.md",
                "mcp-playbooks/tool-sequence-by-stage.md",
            )
        )
        for path in documents:
            with self.subTest(path=path.relative_to(ROOT)):
                text = path.read_text(encoding="utf-8")
                self.assertIn("lexsis_asset_import", text)
                self.assertIn("lexsis_asset_upload", text)

    def test_import_and_upload_contract_is_explicit(self) -> None:
        text = (REFERENCES / "lexsis-mcp-contract.md").read_text(encoding="utf-8")
        for phrase in (
            "lexsis_asset_import.import",
            "requires exactly one source",
            "`url`",
            "`data` + `mime_type`",
            "`attachments`",
            "never opens the upload UI",
            "lexsis_asset_upload.upload",
            "wait for the user's uploaded-asset message",
            "URL or conversation attachment",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_page_type_upload_offers_use_the_shared_asset_workflow(self) -> None:
        page_types = REFERENCES / "page-types"
        for path in page_types.glob("*.md"):
            if path.name.startswith("_"):
                continue
            with self.subTest(page_type=path.stem):
                self.assertIn(
                    "references/workflows/_how-to-read.md", path.read_text(encoding="utf-8")
                )
        workflow = (REFERENCES / "workflows" / "_how-to-read.md").read_text(encoding="utf-8")
        self.assertIn("references/workflows/section-asset-workflow.md", workflow)
        assets = (REFERENCES / "workflows" / "section-asset-workflow.md").read_text(encoding="utf-8")
        self.assertIn("lexsis_asset_upload.upload", assets)
        self.assertIn("lexsis_asset_import.import", assets)


if __name__ == "__main__":
    unittest.main()

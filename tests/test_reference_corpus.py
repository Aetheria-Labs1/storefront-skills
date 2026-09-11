from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "skills" / "storefront-engine" / "references"
BASELINE = json.loads((ROOT / "tests/fixtures/corpus-baseline.json").read_text())
SPEC = importlib.util.spec_from_file_location("corpus_builder", ROOT / "scripts/build-distributions.py")
assert SPEC and SPEC.loader
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)
URL_RE = re.compile(r'https?://[^\s<>`"\\]+')
LINK_RE = re.compile(r"(?<![A-Za-z0-9_/-])(?:storefront-engine/)?references/([A-Za-z0-9_./-]+\.md)")
ANNOTATIONS = {"usage_hint", "when_to_use", "when_not_to_use", "combine_with"}


def normalized_url(value: str) -> str:
    return quote(value.rstrip(".,;:!?)]}"), safe="/:@-._~!$&'()*+,;=%?#[]")


def ascii_clause(value: str) -> str:
    replacements = str.maketrans({
        "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
        "\u2013": "-", "\u2014": " - ", "\u2192": "U+2192", "\u00bb": "U+00BB",
        "\u203a": ">", "\u00b7": ";", "\u2265": ">=", "\u2264": "<=",
        "\u00a0": " ",
    })
    return value.translate(replacements).replace("page-plan.md", "page plan").replace("page-theme.css", "theme_css")


class ReferenceCorpusTests(unittest.TestCase):
    def test_no_local_page_workflow_remains_in_distributions(self) -> None:
        forbidden = re.compile(
            r"lexsis-source\.html|page-theme\.css|page-manifest\.json|qa-report\.md"
            r"|compile-artifact\.json|plan_lint\.py|design_lint\.py"
            r"|validate_page_workspace|prepare_workspace_compile|migrate_page_workspace"
            r"|\$W(?:\b|/)|```(?:bash|shell|python)\n"
        )
        for path in [*REFERENCES.rglob("*.md"), *(ROOT / "skills").glob("*/SKILL.md")]:
            self.assertIsNone(forbidden.search(path.read_text()), path)

    def test_authored_island_mentions_are_active(self) -> None:
        schemas = {
            data["name"]: data
            for path in (REFERENCES / "islands").glob("*/schema.json")
            for data in [json.loads(path.read_text())]
        }
        for path in REFERENCES.rglob("*.md"):
            for name in re.findall(r'<lx-island\b[^>]*name=["\']([A-Za-z][A-Za-z0-9]*)["\']', path.read_text()):
                if name in {"Name", "IslandName"}:
                    continue
                self.assertIn(name, schemas, (path, name))
                self.assertFalse(schemas[name].get("deprecated"), (path, name))

    def test_island_validator_scans_new_nested_references(self) -> None:
        spec = importlib.util.spec_from_file_location(
            "corpus_island_validator", ROOT / "scripts/validate-island-contracts.py"
        )
        assert spec and spec.loader
        validator = importlib.util.module_from_spec(spec)
        with patch.dict(sys.modules, {spec.name: validator}):
            spec.loader.exec_module(validator)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            references = root / "references"
            nested = references / "new"
            nested.mkdir(parents=True)
            document = nested / "recipe.md"
            document.write_text(
                '<lx-island name="UnknownFixtureIsland">'
                '<script type="application/json">{}</script></lx-island>'
            )
            with (
                patch.object(validator, "SKILLS", root / "skills"),
                patch.object(validator, "REFERENCES", references),
                patch.object(validator, "ISLANDS", references / "islands"),
            ):
                examples = list(validator.collect_examples())
            self.assertEqual([example.island for example in examples], ["UnknownFixtureIsland"])
            self.assertEqual(examples[0].path, document)

    def test_generator_prunes_only_obsolete_packaged_references(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            skills = root / "skills"
            references = skills / "storefront-engine" / "references"
            packaged = skills / "build" / "references"
            references.mkdir(parents=True)
            packaged.mkdir(parents=True)
            (skills / "build" / "SKILL.md").write_text("Read `references/current.md`.\n")
            (references / "current.md").write_text("Current canonical reference.\n")
            (references / "old.md").write_text("Retained canonical entry point.\n")
            (packaged / "old.md").write_text("Obsolete packaged copy.\n")
            with (
                patch.object(BUILDER, "ROOT", root),
                patch.object(BUILDER, "SKILLS", skills),
                patch.object(BUILDER, "REFERENCES", references),
                patch.object(BUILDER, "SKILL_SHARED_REFERENCES", {}),
            ):
                self.assertTrue(BUILDER.sync_skill_shared_references(check=True))
                self.assertTrue((packaged / "old.md").exists())
                self.assertFalse((packaged / "current.md").exists())
                BUILDER.sync_skill_shared_references(check=False)
                self.assertFalse((packaged / "old.md").exists())
                self.assertEqual((packaged / "current.md").read_text(), (references / "current.md").read_text())
                self.assertEqual((references / "old.md").read_text(), "Retained canonical entry point.\n")
                self.assertFalse(BUILDER.sync_skill_shared_references(check=True))

    def test_all_original_checklists_and_workflow_sections_survive(self) -> None:
        for name, expected in BASELINE["checklists"].items():
            with self.subTest(page_type=name):
                text = (REFERENCES / "page-types" / name).read_text()
                match = re.search(r"## Checklist\s*```json\s*(\{.*?\})\s*```", text, re.S)
                self.assertIsNotNone(match)
                self.assertEqual(json.loads(match[1]), expected)
                workflow = text.split("### Section by section", 1)[1].split("### Asset budget", 1)[0]
                actual = re.findall(r"^\| `([^`]+)`", workflow, re.M)
                self.assertEqual(actual, BASELINE["workflow_sections"][name])

    def test_all_original_source_addresses_survive(self) -> None:
        actual = {
            normalized_url(address)
            for path in REFERENCES.rglob("*.md")
            for address in URL_RE.findall(path.read_text())
        }
        expected = {normalized_url(address) for address in BASELINE["source_urls"]}
        self.assertFalse(expected - actual, sorted(expected - actual))

    def test_house_rule_clauses_are_not_weakened(self) -> None:
        text = (REFERENCES / "design-rules.md").read_text()
        actual = {
            clause.split(".", 1)[0]: clause
            for clause in re.findall(r"^(?:N\d+|A\d+)\. .+$", text, re.M)
        }
        expected = {name: ascii_clause(clause) for name, clause in BASELINE["house_rule_clauses"].items()}
        self.assertEqual(actual, expected)
        self.assertIn("U+2192", text)
        self.assertIn("U+00BB", text)

    def test_schema_structure_is_unchanged(self) -> None:
        for name, expected in BASELINE["island_contract_hashes"].items():
            with self.subTest(island=name):
                data = json.loads((REFERENCES / name).read_text())
                contract = {key: value for key, value in data.items() if key not in ANNOTATIONS}
                self.assertNotIn("example", contract.get("authoring", {}))
                self.assertNotIn("examples", contract.get("authoring", {}))
                actual = hashlib.sha256(json.dumps(contract, sort_keys=True).encode()).hexdigest()
                self.assertEqual(actual, expected)

    def test_reference_links_and_generated_copies_resolve(self) -> None:
        roots = [REFERENCES]
        for skill in (ROOT / "skills").iterdir():
            if not (skill / "SKILL.md").is_file():
                continue
            packaged = skill / "references"
            roots.append(packaged)
            expected = BUILDER.shared_reference_closure(BUILDER.skill_reference_roots(skill.name))
            actual = {str(path.relative_to(packaged)) for path in packaged.rglob("*.md")}
            self.assertEqual(actual, expected, skill.name)
            for name in expected:
                self.assertEqual(
                    (packaged / name).read_text(),
                    BUILDER.packaged_reference_content(REFERENCES / name),
                    (skill.name, name),
                )
            for name in LINK_RE.findall((skill / "SKILL.md").read_text()):
                self.assertTrue((packaged / name).is_file(), (skill.name, name))
        for root in roots:
            for path in root.rglob("*.md"):
                for name in LINK_RE.findall(path.read_text()):
                    self.assertTrue((root / name).is_file(), (path, name))

    def test_repeated_procedures_have_one_home(self) -> None:
        for phrase in ("sight unseen", "one shoot", "closest existing asset"):
            owners = {
                str(path.relative_to(REFERENCES))
                for path in REFERENCES.rglob("*.md")
                if phrase in path.read_text()
            }
            self.assertEqual(owners, {"workflows/section-asset-workflow.md"}, phrase)
        for path in (REFERENCES / "page-types").glob("*.md"):
            self.assertNotIn("tell the merchant", path.read_text(), path)
            self.assertNotIn("section fit review", path.read_text(), path)

    def test_no_band_aids_or_compiled_authoring_examples(self) -> None:
        banned = re.compile(
            r"Not real islands|Superseded|ignore what follows|override every example below"
            r"|Examples show structure and copy intent|<[^>]+data-island=|data-props=['\"]"
            r"|no variant sync|no plan sync",
            re.I,
        )
        for path in REFERENCES.rglob("*.md"):
            self.assertIsNone(banned.search(path.read_text()), path)
        forbidden = re.compile(
            r"\b(?:TrustBadgeBar|CompareTable|ComparisonTable|PDPInfoCards|ProductGrid|"
            r"FilterBar|NewsletterSignup|SectionHeading|CartDrawer|FAQ|StatCards|Marquee|Tabs|"
            r"EditorialProductGrid|ProductImage|AddToCart|ExitIntent|BackToTop|Carousel|Countdown)\b"
        )
        for path in (REFERENCES / "islands").glob("*/schema.json"):
            data = json.loads(path.read_text())
            self.assertIsNone(forbidden.search(json.dumps(data.get("combine_with", []))), path)

    def test_documentation_and_live_mcp_source_agree(self) -> None:
        expected = {
            router + "." + action
            for router, actions in BASELINE["mcp_surface"].items()
            for action in actions
        }
        actual = {
            action
            for path in [*REFERENCES.rglob("*.md"), *(ROOT / "skills").glob("*/SKILL.md")]
            for action in re.findall(r"\blexsis_[a-z_]+\.[a-z][a-z_]+", path.read_text())
        }
        self.assertEqual(actual, expected)
        source = ROOT.parent / "services/storefront-blueprint-mcp/src/tools/consolidated.ts"
        if source.is_file():
            declaration = source.read_text().split("export const CONSOLIDATED_ROUTERS", 1)[1].split("\n];", 1)[0]
            surface = {
                match[1]: re.findall(r'operation\("([^"]+)"', match[2])
                for match in re.finditer(r'name: "(lexsis_[a-z_]+)"(.*?)(?=\n  \{\n    name:|\Z)', declaration, re.S)
            }
            self.assertEqual(surface, BASELINE["mcp_surface"])

    def test_reference_prose_is_ascii_except_currency(self) -> None:
        for path in REFERENCES.rglob("*.md"):
            bad = {char for char in path.read_text() if ord(char) > 127 and unicodedata.category(char) != "Sc"}
            self.assertFalse(bad, (path, bad))

    def test_copy_warnings_and_proof_offer_failures_keep_their_severity(self) -> None:
        fixture = ROOT / "tests/fixtures/design-lint/corrected"
        script = ROOT / "tests/support/design_lint.py"
        for content, expected in (("seamless", 0), ("people are viewing", 1), ("Hurry", 1)):
            with self.subTest(content=content), tempfile.TemporaryDirectory() as temporary:
                workspace = Path(temporary)
                for name in ("lexsis-source.html", "page-theme.css"):
                    (workspace / name).write_bytes((fixture / name).read_bytes())
                source = workspace / "lexsis-source.html"
                source.write_text(source.read_text() + f"\n<p>{content}</p>\n")
                result = subprocess.run([sys.executable, str(script), str(workspace)], capture_output=True, text=True)
                self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
                self.assertIn("WARN" if expected == 0 else "FAIL", result.stdout)


if __name__ == "__main__":
    unittest.main()

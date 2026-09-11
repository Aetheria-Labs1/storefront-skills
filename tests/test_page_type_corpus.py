#!/usr/bin/env python3
"""The page-type corpus is machine-readable and plan_lint enforces it."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "skills" / "storefront-engine" / "references"
PAGE_TYPES = REFS / "page-types"
FORMAT = (PAGE_TYPES / "_checklist-format.md").read_text(encoding="utf-8")
LINT = ROOT / "tests/support/plan_lint.py"

REQUIRED_HEADINGS = [
    "## Identify it", "## Anatomy", "## Workflow", "### Context reads",
    "### Section by section", "### Asset budget",
    "## Above the fold (390px)", "## Proof",
    "## Offer and CTA", "## Imagery", "## Copy", "## Never", "## Examples",
    "## Checklist", "## Sources",
]
REQUIRED_KEYS = {
    "page_type", "funnel_stage", "awareness", "traffic", "sections",
    "mandatory_sections", "forbidden_sections", "nav", "price_above_fold",
    "cta", "proof", "imagery", "copy_framework", "offer_compat", "urgency",
}


def vocabulary(table_group_header: str) -> set[str]:
    """Collect backticked ids from the vocabulary tables in _checklist-format.md."""
    section = FORMAT.split(table_group_header, 1)[1]
    section = section.split("\n## ", 1)[0]
    return set(re.findall(r"`([a-z][a-z0-9-]*)`", section))


SECTION_IDS = vocabulary("## Canonical section id vocabulary")
PROOF_KINDS = vocabulary("## Proof kind vocabulary")
IMAGE_JOBS = vocabulary("## Image job vocabulary")


def type_files() -> list[Path]:
    return sorted(p for p in PAGE_TYPES.glob("*.md") if not p.name.startswith("_"))


def checklist(path: Path) -> dict:
    m = re.search(r"## Checklist\s*```json\s*(\{.*?\})\s*```", path.read_text(encoding="utf-8"), re.S)
    assert m, f"{path.name}: no ## Checklist json block"
    return json.loads(m.group(1))


class PageTypeCorpusTests(unittest.TestCase):
    def test_corpus_is_large_enough(self) -> None:
        self.assertGreaterEqual(len(type_files()), 25)

    def test_every_type_file_has_required_headings_and_checklist(self) -> None:
        for path in type_files():
            text = path.read_text(encoding="utf-8")
            for heading in REQUIRED_HEADINGS:
                self.assertIn(heading, text, (path.name, heading))
            self.assertIn("references/workflows/_how-to-read.md", text, path.name)
            self.assertIn(
                "| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |",
                text,
                path.name,
            )
            data = checklist(path)
            self.assertEqual(data["page_type"], path.stem, path.name)
            self.assertTrue(REQUIRED_KEYS <= set(data), (path.name, REQUIRED_KEYS - set(data)))
            self.assertLessEqual(data["sections"]["min"], data["sections"]["max"], path.name)

    def test_checklist_ids_use_the_shared_vocabulary(self) -> None:
        for path in type_files():
            data = checklist(path)
            for key in ("mandatory_sections", "recommended_sections", "forbidden_sections"):
                for entry in data.get(key, []):
                    for sid in (entry if isinstance(entry, list) else [entry]):
                        self.assertIn(sid, SECTION_IDS, (path.name, key, sid))
            for key in ("required_kinds", "forbidden_kinds"):
                for kind in data["proof"].get(key, []):
                    self.assertIn(kind, PROOF_KINDS, (path.name, key, kind))
            for job in data["imagery"].get("required_jobs", []):
                self.assertIn(job, IMAGE_JOBS, (path.name, job))
            overlap = set(map(str, data["mandatory_sections"])) & set(data["forbidden_sections"])
            self.assertFalse(overlap, (path.name, overlap))

    def test_index_lists_every_type(self) -> None:
        index = (PAGE_TYPES / "_index.md").read_text(encoding="utf-8")
        for path in type_files():
            self.assertIn(f"`{path.stem}`", index, path.stem)

    def test_plan_lint_passes_and_fails_correctly(self) -> None:
        data = checklist(PAGE_TYPES / "ad-landing-page.md")
        first = [e[0] if isinstance(e, list) else e for e in data["mandatory_sections"]]
        forbidden = set(data["forbidden_sections"])
        fillers = [
            e[0] if isinstance(e, list) else e for e in data.get("recommended_sections", [])
        ] + ["faq", "trust-bar", "guarantee", "shipping-returns", "stats", "story"]
        for sid in fillers:
            if len(first) >= data["sections"]["min"]:
                break
            if sid not in first and sid not in forbidden and sid not in {"header", "sticky-cta", "countdown", "stock-indicator"}:
                first.append(sid)
        with tempfile.TemporaryDirectory() as tmp:
            w = Path(tmp)
            plan = "\n".join(
                [
                    "# Plan", "## Page type", "**Type.** ad-landing-page",
                    "**Mandatory sections omitted.** none",
                    "## Design direction", "## Consumer decision model",
                    "## Proof ledger", "## Offer ledger", "## Asset slots",
                ]
            )
            (w / "page-plan.md").write_text(plan, encoding="utf-8")
            manifest = {
                "page": {"pageType": "ad-landing-page"},
                "sections": first,
                "offer": {"type": "first-order"},
                "reviews": {"source": "collection", "available": 12},
                "assets": [{"slotId": "A1", "role": "hero_bg", "generated": True}],
            }
            (w / "page-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            ok = subprocess.run([sys.executable, str(LINT), str(w)], capture_output=True, text=True)
            self.assertEqual(ok.returncode, 0, ok.stdout)

            manifest["sections"] = first[1:] + list(data["forbidden_sections"][:1])
            manifest["assets"][0]["role"] = "product_media"
            (w / "page-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            advisory = subprocess.run([sys.executable, str(LINT), str(w)], capture_output=True, text=True)
            self.assertEqual(advisory.returncode, 0, "advisory mode never blocks")
            self.assertIn("WARN", advisory.stdout)
            bad = subprocess.run([sys.executable, str(LINT), "--strict", str(w)], capture_output=True, text=True)
            self.assertEqual(bad.returncode, 1, bad.stdout)
            self.assertIn("T2 mandatory sections", bad.stdout)


if __name__ == "__main__":
    unittest.main()

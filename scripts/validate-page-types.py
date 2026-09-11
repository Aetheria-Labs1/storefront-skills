#!/usr/bin/env python3
"""Validate page-type reference files against _checklist-format.md.

Usage: validate-page-types.py [file.md ...]   (default: every type file)
Checks required headings, the JSON checklist block, required keys, and that
every section id, proof kind and image job comes from the shared vocabulary.
Exit 1 on any problem.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE_TYPES = ROOT / "skills/storefront-engine/references/page-types"
FORMAT = (PAGE_TYPES / "_checklist-format.md").read_text(encoding="utf-8")

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
ENUMS = {
    "nav": {"none", "minimal", "full"},
    "price_above_fold": {"required", "optional", "forbidden"},
    "urgency": {"none", "verified-only", "encouraged"},
}
CTA_STICKY = {"required", "optional", "forbidden"}
CTA_COPY = {"add-to-cart", "claim-offer", "next-step", "start-quiz", "join-waitlist", "subscribe", "shop-collection", "read-results"}
HERO = {"packshot", "product-in-hand", "product-in-context", "editorial-lifestyle", "video-poster", "typographic", "grid", "ugc-screenshot"}
VIDEO = {"required", "optional", "forbidden"}
FRAMEWORKS = {"pas", "aida", "bab", "4ps", "fab", "story-lead", "listicle", "comparison", "hook-story-offer", "answer-first", "qualifier-lead"}
AWARENESS = {"unaware", "problem-aware", "solution-aware", "product-aware", "most-aware"}
STAGES = {"tof", "mof", "bof", "retention"}


def vocabulary(header: str) -> set[str]:
    section = FORMAT.split(header, 1)[1].split("\n## ", 1)[0]
    return set(re.findall(r"`([a-z][a-z0-9-]*)`", section))


SECTION_IDS = vocabulary("## Canonical section id vocabulary")
PROOF_KINDS = vocabulary("## Proof kind vocabulary")
IMAGE_JOBS = vocabulary("## Image job vocabulary")


def check(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for h in REQUIRED_HEADINGS:
        if h not in text:
            errors.append(f"missing heading {h!r}")
    if "references/workflows/_how-to-read.md" not in text:
        errors.append("workflow must reference the shared procedures")
    workflow_header = "| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |"
    if workflow_header not in text:
        errors.append("missing type-specific workflow decision table")
    m = re.search(r"## Checklist\s*```json\s*(\{.*?\})\s*```", text, re.S)
    if not m:
        return errors + ["no ## Checklist ```json block"]
    try:
        d = json.loads(m.group(1))
    except json.JSONDecodeError as exc:
        return errors + [f"checklist JSON invalid: {exc}"]
    missing = REQUIRED_KEYS - set(d)
    if missing:
        errors.append(f"checklist missing keys {sorted(missing)}")
    if d.get("page_type") != path.stem:
        errors.append(f"page_type {d.get('page_type')!r} != file stem {path.stem!r}")
    for key, allowed in ENUMS.items():
        if d.get(key) not in allowed:
            errors.append(f"{key}={d.get(key)!r} not in {sorted(allowed)}")
    for key in ("mandatory_sections", "recommended_sections", "forbidden_sections"):
        for entry in d.get(key, []):
            for sid in (entry if isinstance(entry, list) else [entry]):
                if sid not in SECTION_IDS:
                    errors.append(f"{key}: unknown section id {sid!r}")
    flat_mand = {s for e in d.get("mandatory_sections", []) for s in (e if isinstance(e, list) else [e])}
    overlap = flat_mand & set(d.get("forbidden_sections", []))
    if overlap:
        errors.append(f"mandatory and forbidden overlap: {sorted(overlap)}")
    sec = d.get("sections", {})
    if not (isinstance(sec, dict) and 0 < sec.get("min", 0) <= sec.get("max", 0)):
        errors.append(f"sections min/max invalid: {sec}")
    cta = d.get("cta", {})
    if cta.get("sticky") not in CTA_STICKY:
        errors.append(f"cta.sticky={cta.get('sticky')!r}")
    if cta.get("copy_pattern") not in CTA_COPY:
        errors.append(f"cta.copy_pattern={cta.get('copy_pattern')!r}")
    if not (isinstance(cta.get("min"), int) and isinstance(cta.get("max"), int) and 0 <= cta["min"] <= cta["max"]):
        errors.append(f"cta.min/max invalid: {cta}")
    if not isinstance(cta.get("first_after_section"), int):
        errors.append("cta.first_after_section must be an int")
    proof = d.get("proof", {})
    for key in ("required_kinds", "forbidden_kinds"):
        for kind in proof.get(key, []):
            if kind not in PROOF_KINDS:
                errors.append(f"proof.{key}: unknown kind {kind!r}")
    if not (isinstance(proof.get("min_modules"), int) and isinstance(proof.get("max_modules"), int) and proof["min_modules"] <= proof["max_modules"]):
        errors.append(f"proof.min/max_modules invalid: {proof}")
    img = d.get("imagery", {})
    for job in img.get("required_jobs", []):
        if job not in IMAGE_JOBS:
            errors.append(f"imagery.required_jobs: unknown job {job!r}")
    if img.get("hero") not in HERO:
        errors.append(f"imagery.hero={img.get('hero')!r}")
    if img.get("video") not in VIDEO:
        errors.append(f"imagery.video={img.get('video')!r}")
    for fw in d.get("copy_framework", []):
        if fw not in FRAMEWORKS:
            errors.append(f"copy_framework: unknown {fw!r}")
    for a in d.get("awareness", []):
        if a not in AWARENESS:
            errors.append(f"awareness: unknown {a!r}")
    for st in d.get("funnel_stage", []):
        if st not in STAGES:
            errors.append(f"funnel_stage: unknown {st!r}")
    oc = d.get("offer_compat", {})
    if not (isinstance(oc, dict) and "allowed" in oc and "forbidden" in oc):
        errors.append("offer_compat needs allowed[] and forbidden[]")
    if re.search(r"[\U0001F000-\U0001FAFF]", text):
        errors.append("emoji present")
    return errors


def main() -> int:
    files = [Path(a) for a in sys.argv[1:]] or sorted(p for p in PAGE_TYPES.glob("*.md") if not p.name.startswith("_"))
    bad = 0
    for path in files:
        errors = check(path)
        status = "OK " if not errors else "BAD"
        bad += bool(errors)
        print(f"{status} {path.name}")
        for e in errors:
            print(f"     - {e}")
    print(f"\n{len(files) - bad}/{len(files)} page-type files valid")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

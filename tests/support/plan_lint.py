#!/usr/bin/env python3
"""Repository-only regression checks for page-type checklist fixtures.

Usage: plan_lint.py <workspace> [--references <dir>]
       plan_lint.py --input-json - [--strict]
The stdin object contains manifest and optional plan Markdown.

Reads page-manifest.json (page.pageType, sections[], assets[], offer, reviews)
and page-plan.md, loads references/page-types/<pageType>.md, and checks the
mechanical rules from _checklist-format.md:

  T1 page type recorded and a checklist file exists
  T2 every mandatory section present or listed under "Mandatory sections omitted"
  T3 no forbidden section present
  T4 section count within min..max
  T5 nav rule (header present only when nav != none)
  T6 sticky-cta present when cta.sticky == required, absent when forbidden
  T7 plan has the required blocks: Page type, Design direction, Consumer
     decision model, Proof ledger, Asset slots; Offer ledger when an offer exists
  T8 every generated asset slot uses an ALLOW purpose, or an ASK purpose with askApproved: true
  T9 reviews section planned only when manifest.reviews.available > 0
  T10 countdown / stock-indicator sections only when the offer ledger verifies them

Advisory by default: prints WARN rows and exits 0 so the plan owner decides.
Pass --strict to exit 1 on any WARN. References default to the plan-page
skill's own references/ directory (self-contained install) and fall back to
the shared storefront-engine corpus.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ALLOW_PURPOSES = {
    "hero_bg", "section_bg", "card_bg", "texture_fill", "pattern_tile",
    "decorative_element", "product_composite", "icon_set",
}
ASK_PURPOSES = {"product_lifestyle"}  # allowed only with "askApproved": true
REQUIRED_BLOCKS = [
    "## Page type",
    "## Design direction",
    "## Consumer decision model",
    "## Proof ledger",
    "## Asset slots",
]


def references_dir(cli: str | None) -> pathlib.Path:
    candidates = [pathlib.Path(cli)] if cli else []
    candidates += [
        HERE.parents[1] / "skills" / "storefront-engine" / "references",
    ]
    for c in candidates:
        if (c / "page-types").is_dir():
            return c
    sys.exit("plan_lint: cannot find references/page-types")


def load_checklist(refs: pathlib.Path, page_type: str) -> dict:
    path = refs / "page-types" / f"{page_type}.md"
    if not path.is_file():
        return {}
    m = re.search(r"## Checklist\s*```json\s*(\{.*?\})\s*```", path.read_text(encoding="utf-8"), re.S)
    return json.loads(m.group(1)) if m else {}


def matches(section_id: str, canonical: str) -> bool:
    return section_id == canonical or section_id.startswith(canonical + "-")


def any_present(entry, sections: list[str]) -> bool:
    options = entry if isinstance(entry, list) else [entry]
    return any(matches(s, o) for s in sections for o in options)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", nargs="?", type=pathlib.Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--references")
    parser.add_argument("--input-json", choices=["-"], help="Read plan and manifest from stdin")
    arguments = parser.parse_args()
    if arguments.input_json and arguments.workspace:
        parser.error("choose a workspace or --input-json -, not both")
    strict = arguments.strict
    refs = references_dir(arguments.references)
    if arguments.input_json:
        try:
            payload = json.load(sys.stdin)
        except json.JSONDecodeError as error:
            parser.error(f"invalid input JSON: {error}")
        if not isinstance(payload, dict) or not isinstance(payload.get("manifest"), dict):
            parser.error("input must be a JSON object with a manifest object")
        manifest = payload["manifest"]
        plan = payload.get("plan", "")
        if not isinstance(plan, str):
            parser.error("plan must be a string")
    else:
        workspace = arguments.workspace or pathlib.Path(".")
        manifest = json.loads((workspace / "page-manifest.json").read_text(encoding="utf-8"))
        plan_path = workspace / "page-plan.md"
        plan = plan_path.read_text(encoding="utf-8") if plan_path.exists() else ""
    page = manifest.get("page", {})
    page_type = page.get("pageType") or ""
    sections = list(manifest.get("sections", []))
    offer = manifest.get("offer") or {}
    reviews = manifest.get("reviews") or {}
    checklist = load_checklist(refs, page_type) if page_type else {}

    omitted_block = re.search(r"\*\*Mandatory sections omitted\.\*\*\s*(.+)", plan)
    omitted = set()
    if omitted_block and omitted_block.group(1).strip().lower() != "none":
        omitted = {
            m.strip("`* ") for m in re.findall(r"`?([a-z][a-z0-9-]+)`?\s*:", omitted_block.group(1))
        }

    results: list[tuple[str, bool, str]] = []

    results.append(("T1 page type + checklist file", bool(page_type and checklist),
                    page_type or "page.pageType missing"))

    missing = [
        e for e in checklist.get("mandatory_sections", [])
        if not any_present(e, sections)
        and not any(o in omitted for o in (e if isinstance(e, list) else [e]))
    ]
    results.append(("T2 mandatory sections", not missing, ", ".join(map(str, missing)) or "all present"))

    present_forbidden = [
        e for e in checklist.get("forbidden_sections", []) if any_present(e, sections)
    ]
    results.append(("T3 forbidden sections", not present_forbidden, ", ".join(present_forbidden) or "none"))

    lo = checklist.get("sections", {}).get("min", 0)
    hi = checklist.get("sections", {}).get("max", 999)
    n = len([s for s in sections if not matches(s, "announcement") and not matches(s, "footer") and not matches(s, "header")])
    results.append((f"T4 section count {lo}..{hi}", lo <= n <= hi, str(n)))

    nav = checklist.get("nav")
    has_header = any(matches(s, "header") for s in sections)
    nav_ok = True if nav is None else (has_header if nav != "none" else not has_header)
    results.append(("T5 nav rule", nav_ok, f"nav={nav} header={'yes' if has_header else 'no'}"))

    sticky = checklist.get("cta", {}).get("sticky")
    has_sticky = any(matches(s, "sticky-cta") for s in sections)
    sticky_ok = True
    if sticky == "required":
        sticky_ok = has_sticky
    elif sticky == "forbidden":
        sticky_ok = not has_sticky
    results.append(("T6 sticky cta rule", sticky_ok, f"sticky={sticky} present={'yes' if has_sticky else 'no'}"))

    missing_blocks = [b for b in REQUIRED_BLOCKS if b not in plan]
    if offer and offer.get("type", "none") != "none" and "## Offer ledger" not in plan:
        missing_blocks.append("## Offer ledger")
    results.append(("T7 plan blocks", not missing_blocks, ", ".join(missing_blocks) or "all present"))

    def is_generated(a: dict) -> bool:
        return bool(a.get("generated")) or "provider" in a or a.get("sourceType") == "generated"

    def purpose_ok(a: dict) -> bool:
        role = a.get("role")
        return role in ALLOW_PURPOSES or (role in ASK_PURPOSES and a.get("askApproved") is True)

    bad_purposes = [
        f"{a.get('slotId')}:{a.get('role')}"
        for a in manifest.get("assets", [])
        if is_generated(a) and not purpose_ok(a)
    ]
    results.append(("T8 generated slots use ALLOW/approved-ASK purposes", not bad_purposes, ", ".join(bad_purposes) or "ok"))

    has_reviews_section = any(any_present(k, sections) for k in ["reviews", "review-summary", "testimonial-spotlight", "review-list"])
    reviews_ok = (not has_reviews_section) or (reviews.get("source") in {"collection", "products", "external-verified"} and int(reviews.get("available") or 0) > 0)
    results.append(("T9 reviews backed by data", reviews_ok, f"available={reviews.get('available')}"))

    urgency_sections = [s for s in sections if matches(s, "countdown") or matches(s, "stock-indicator")]
    urgency_ok = not urgency_sections or bool(offer.get("endsAt") or offer.get("stockVerified"))
    results.append(("T10 urgency verified", urgency_ok, ", ".join(urgency_sections) or "none"))

    warns = 0
    print(f"{'check':42} result  detail")
    for name, ok, detail in results:
        warns += not ok
        print(f"{name:42} {'OK' if ok else 'WARN':6}  {detail}")
    if warns:
        print(f"\n{warns} deviation(s) from the type default. Note each under "
              "'Deviations from the type default' in page-plan.md, or change the plan.")
    return 1 if (warns and strict) else 0


if __name__ == "__main__":
    sys.exit(main())

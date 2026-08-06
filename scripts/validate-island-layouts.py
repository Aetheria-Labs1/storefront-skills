#!/usr/bin/env python3
"""Validate every layout's data-props against the island's real Props interface.

A layout that passes a prop the island doesn't declare is silently dropped by
React. When the dropped prop is *required*, the island throws during hydration
and is swallowed by the hydrator's try/catch — the page still returns 200 with a
dead mount. This check makes that failure loud at CI time instead.

Ground truth is reference/islands/{island}/schema.json, generated from the
TypeScript `interface Props` by packages/storefront-components/scripts/
generate-schemas.ts (see scripts/sync-island-schemas.py).

Usage:
    python3 scripts/validate-island-layouts.py           # report + exit 1 on error
    python3 scripts/validate-island-layouts.py --json    # machine-readable
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ISLANDS_DIR = Path("reference/islands")

# Islands whose `productId` is expanded into real props at hydration time by
# services/storefront-renderer/app/lib/islands/product-resolver.client.ts.
# Keep in sync with PRODUCT_RESOLVE_ISLANDS in
# services/storefront-renderer/app/lib/islands/hydrator.client.tsx.
PRODUCT_RESOLVE_ISLANDS = {
    "BuyBox",
    "StickyBar",
    "QuickAdd",
    "ProductCarousel",
    "ProductGallery",
    "ProductHero",
    "OptionResolver",
    "SubscriptionToggle",
    "InventoryIndicator",
    "CartCrossSell",
}

# Props every island accepts via React/our conventions but which don't appear in
# the generated schema.
UNIVERSAL_PROPS = {"className", "children", "key", "id", "style"}

ISLAND_RE = re.compile(
    r"""data-island=["'](?P<name>[A-Za-z0-9_]+)["'][^>]*?"""
    r"""data-props='(?P<props>[^']*)'""",
    re.DOTALL,
)
PLACEHOLDER_RE = re.compile(r"\{\{[A-Z0-9_]+\}\}")


def load_schemas() -> dict[str, dict]:
    schemas: dict[str, dict] = {}
    for path in sorted(ISLANDS_DIR.glob("*/schema.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        name = data.get("name")
        if name:
            schemas[name] = data
    return schemas


def parse_props(raw: str) -> dict | None:
    """Parse a data-props blob, neutralising {{TEMPLATE_VARS}} first.

    Placeholders sit in value position (`"x":{{FOO}}` or `"x":"{{FOO}}"`), so
    substituting a bare `null` yields valid JSON either way once the quoted form
    collapses to `"null"`.
    """
    text = raw.replace("&quot;", '"').replace("&#39;", "'").replace("&amp;", "&")
    text = PLACEHOLDER_RE.sub("null", text)
    text = text.replace('"null"', "null")
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def check_layout(
    island: str, props: dict, schema: dict | None
) -> tuple[list[str], list[str]]:
    """Return (errors, warnings) for one mount."""
    if schema is None:
        return ([f"island '{island}' does not exist"], [])

    declared = schema.get("props", {}) or {}
    known = set(declared) | UNIVERSAL_PROPS
    resolves_product = island in PRODUCT_RESOLVE_ISLANDS
    if resolves_product:
        known.add("productId")

    errors: list[str] = []
    warnings: list[str] = []

    unknown = sorted(k for k in props if k not in known)
    for key in unknown:
        # `productId` on a non-resolving island is the crash signature: the
        # author expected runtime expansion that never happens.
        if key == "productId":
            errors.append(
                f"'productId' passed but {island} is not in PRODUCT_RESOLVE_ISLANDS "
                f"— it will never be expanded into real props"
            )
        else:
            warnings.append(f"unknown prop '{key}' (silently ignored by React)")

    # A required prop is only satisfiable statically unless the resolver fills it.
    for name, spec in declared.items():
        if not spec.get("required"):
            continue
        if name in props:
            continue
        if resolves_product and "productId" in props:
            continue
        errors.append(f"required prop '{name}' missing")

    # Enum values must be members of the declared union.
    for name, value in props.items():
        spec = declared.get(name)
        if not spec or spec.get("type") != "enum":
            continue
        allowed = spec.get("values") or []
        if isinstance(value, str) and allowed and value not in allowed:
            errors.append(
                f"'{name}' = {value!r} is not one of {allowed}"
            )

    # Nested required keys. An object prop that is present but missing a
    # non-optional field of its shape still crashes — e.g. QuickAdd's
    # `product` without `variants` dies on product.variants.find().
    for name, spec in declared.items():
        shape = spec.get("shape")
        if not shape or spec.get("type") != "object":
            continue
        value = props.get(name)
        if not isinstance(value, dict):
            continue
        for field, ftype in shape.items():
            # '?string' marks the field optional in the generated schema.
            if isinstance(ftype, str) and ftype.startswith("?"):
                continue
            if field not in value:
                errors.append(
                    f"'{name}.{field}' missing (required by shape, type {ftype})"
                )

    return errors, warnings


def main() -> int:
    as_json = "--json" in sys.argv

    if not ISLANDS_DIR.is_dir():
        print(f"::error::{ISLANDS_DIR} not found — run from the repo root")
        return 1

    schemas = load_schemas()
    if not schemas:
        print(f"::error::no schema.json files under {ISLANDS_DIR}")
        return 1

    results: list[dict] = []
    layout_count = 0

    for layout_path in sorted(ISLANDS_DIR.glob("*/layouts/*.json")):
        layout_count += 1
        rel = layout_path.as_posix()
        try:
            layout = json.loads(layout_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            results.append({"file": rel, "errors": [f"invalid JSON: {exc}"], "warnings": []})
            continue

        html = layout.get("html", "") or ""
        errors: list[str] = []
        warnings: list[str] = []

        mounts = list(ISLAND_RE.finditer(html))
        # A layout with no mount is fine (pure-CSS/JS section), but a
        # data-island with an unparseable data-props is not.
        for match in mounts:
            island = match.group("name")
            props = parse_props(match.group("props"))
            if props is None:
                errors.append(f"{island}: data-props is not valid JSON")
                continue
            errs, warns = check_layout(island, props, schemas.get(island))
            errors.extend(f"{island}: {e}" for e in errs)
            warnings.extend(f"{island}: {w}" for w in warns)

        # Catch mounts whose data-props we failed to pair up at all.
        bare = len(re.findall(r"data-island=", html)) - len(mounts)
        if bare > 0:
            errors.append(f"{bare} data-island mount(s) with unmatched/missing data-props")

        if errors or warnings:
            results.append({"file": rel, "errors": errors, "warnings": warnings})

    if as_json:
        print(json.dumps(results, indent=2))
        return 1 if any(r["errors"] for r in results) else 0

    failing = [r for r in results if r["errors"]]
    warning_only = [r for r in results if not r["errors"] and r["warnings"]]

    for result in failing:
        for err in result["errors"]:
            print(f"::error file={result['file']}::{err}")
        for warn in result["warnings"]:
            print(f"::warning file={result['file']}::{warn}")

    for result in warning_only:
        for warn in result["warnings"]:
            print(f"::warning file={result['file']}::{warn}")

    print()
    print(f"Checked {layout_count} layouts across {len(schemas)} islands")
    print(f"  {len(failing)} with errors (island renders dead or crashes)")
    print(f"  {len(warning_only)} with warnings only (renders, intent dropped)")

    if failing:
        print()
        print("Errors are blocking: a layout that drops a required prop hydrates")
        print("into a dead mount, and the hydrator swallows the exception.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

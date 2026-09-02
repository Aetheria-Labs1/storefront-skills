#!/usr/bin/env python3
"""Validate explicit island examples against the bundled island contracts.

The storefront skill pack intentionally keeps deprecated schemas so older pages
can still be explained. Deprecated mounts therefore warn, while unknown island
names, unknown props, and invalid literal enum values fail validation.

Only explicit JSON objects are checked. Examples containing ellipses or other
pseudocode are ignored until they become concrete enough to validate.
"""

from __future__ import annotations

import html
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
ISLANDS = SKILLS / "storefront-engine" / "references" / "islands"
REFERENCES = SKILLS / "storefront-engine" / "references"

UNIVERSAL_PROPS = {"children", "className", "id", "key", "style"}

# These authoring conveniences are expanded by the storefront renderer before
# the React island receives its generated-schema props.
RESOLVER_PROPS: dict[str, set[str]] = {
    "BuyBox": {"productId"},
    "FeaturedCollectionStage": {"productIds"},
    "InventoryIndicator": {"productId"},
    "OptionResolver": {"productId"},
    "PlanSelector": {"productId"},
    "ProductCarousel": {"productIds"},
    "ProductGallery": {"productId"},
    "ProductHero": {"productId"},
    "QuantityBreaks": {"productId", "tierQuantities"},
    "QuickAdd": {"productId"},
    "StickyBar": {"productId"},
    "SubscriptionToggle": {"productId"},
}

DATA_ISLAND_TAG_RE = re.compile(
    r"<[^>]*\bdata-island=(?P<quote>[\"'])(?P<name>[A-Za-z0-9_]+)"
    r"(?P=quote)[^>]*>",
    re.DOTALL,
)
DATA_PROPS_RE = re.compile(
    r"\bdata-props=(?P<quote>[\"'])(?P<props>.*?)(?P=quote)(?:\s|/?>)",
    re.DOTALL,
)
LX_ISLAND_RE = re.compile(
    r"<lx-island\b[^>]*\bname=(?P<quote>[\"'])"
    r"(?P<name>[A-Za-z0-9_]+)(?P=quote)[^>]*>"
    r"(?P<body>.*?)</lx-island>",
    re.DOTALL,
)
JSON_SCRIPT_RE = re.compile(
    r"<script\b[^>]*\btype=(?P<quote>[\"'])application/json(?P=quote)"
    r"[^>]*>(?P<props>.*?)</script>",
    re.DOTALL,
)
QUOTED_PLACEHOLDER_RE = re.compile(r'"\{\{[^{}]+\}\}"')
PLACEHOLDER_RE = re.compile(r"\{\{[^{}]+\}\}")
PSEUDOCODE_RE = re.compile(r"\.\.\.|<[^>]+>")
PLACEHOLDER = "__LEXIS_PLACEHOLDER__"
GENERIC_EXAMPLE_NAMES = {"IslandName", "Name"}
REFERENCE_EXAMPLE_FILES = {
    "generate-collection.md",
    "generate-editorial.md",
    "generate-landing-page.md",
    "generate-pdp.md",
    "generation-protocol.md",
    "island-patterns.md",
    "product-grid.md",
    "section-library.md",
    "source-format.md",
}


@dataclass(frozen=True)
class Example:
    path: Path
    location: str
    island: str
    raw_props: str | None


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_schemas() -> dict[str, dict]:
    schemas: dict[str, dict] = {}
    for path in sorted(ISLANDS.glob("*/schema.json")):
        schema = json.loads(path.read_text(encoding="utf-8"))
        name = schema.get("name")
        if isinstance(name, str):
            schemas[name] = schema
    return schemas


def examples_from_text(path: Path, text: str, location: str = "") -> Iterator[Example]:
    for match in DATA_ISLAND_TAG_RE.finditer(text):
        tag = match.group(0)
        props_match = DATA_PROPS_RE.search(tag)
        yield Example(
            path=path,
            location=location,
            island=match.group("name"),
            raw_props=props_match.group("props") if props_match else None,
        )

    for match in LX_ISLAND_RE.finditer(text):
        script_match = JSON_SCRIPT_RE.search(match.group("body"))
        yield Example(
            path=path,
            location=location,
            island=match.group("name"),
            raw_props=script_match.group("props") if script_match else None,
        )


def string_values(value: object, pointer: str = "") -> Iterator[tuple[str, str]]:
    if isinstance(value, str):
        yield pointer, value
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from string_values(item, f"{pointer}/{index}")
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from string_values(item, f"{pointer}/{key}")


def collect_examples() -> Iterator[Example]:
    markdown_paths = set(SKILLS.glob("*/SKILL.md"))
    markdown_paths.update(REFERENCES / name for name in REFERENCE_EXAMPLE_FILES)
    for path in sorted(markdown_paths):
        yield from examples_from_text(path, path.read_text(encoding="utf-8"))

    for path in sorted(ISLANDS.rglob("*.json")):
        document = json.loads(path.read_text(encoding="utf-8"))
        for pointer, value in string_values(document):
            yield from examples_from_text(path, value, pointer)


def parse_explicit_props(raw: str) -> tuple[dict | None, str | None]:
    decoded = html.unescape(raw).strip()
    if not decoded:
        return {}, None
    if PSEUDOCODE_RE.search(decoded):
        return None, None

    decoded = QUOTED_PLACEHOLDER_RE.sub(json.dumps(PLACEHOLDER), decoded)
    decoded = PLACEHOLDER_RE.sub("null", decoded)
    try:
        value = json.loads(decoded)
    except json.JSONDecodeError as exc:
        return None, f"invalid explicit JSON props: {exc.msg}"
    if not isinstance(value, dict):
        return None, "island props must be a JSON object"
    return value, None


def annotation(kind: str, example: Example, message: str) -> str:
    location = f" {example.location}" if example.location else ""
    return f"::{kind} file={relative(example.path)}::{example.island}{location}: {message}"


def main() -> int:
    if not ISLANDS.is_dir():
        print(f"::error::{relative(ISLANDS)} is missing")
        return 1

    schemas = load_schemas()
    errors: list[str] = []
    warnings: list[str] = []
    checked_names = 0
    checked_props = 0

    for example in collect_examples():
        if example.island in GENERIC_EXAMPLE_NAMES:
            continue
        checked_names += 1
        schema = schemas.get(example.island)
        if schema is None:
            errors.append(annotation("error", example, "unknown island"))
            continue

        if schema.get("deprecated"):
            replacement = schema.get("replacement")
            suffix = f"; use {replacement}" if replacement else ""
            warnings.append(annotation("warning", example, f"deprecated island{suffix}"))

        if example.raw_props is None:
            continue
        props, parse_error = parse_explicit_props(example.raw_props)
        if parse_error:
            errors.append(annotation("error", example, parse_error))
            continue
        if props is None:
            continue

        checked_props += 1
        declared = set((schema.get("props") or {}).keys())
        allowed = declared | UNIVERSAL_PROPS | RESOLVER_PROPS.get(example.island, set())
        for prop in sorted(set(props) - allowed):
            errors.append(annotation("error", example, f"unknown prop {prop!r}"))

        for prop, value in props.items():
            spec = (schema.get("props") or {}).get(prop)
            if (
                not isinstance(spec, dict)
                or spec.get("type") != "enum"
                or not isinstance(value, str)
                or value == PLACEHOLDER
            ):
                continue
            allowed_values = spec.get("values") or []
            if allowed_values and value not in allowed_values:
                errors.append(
                    annotation(
                        "error",
                        example,
                        f"{prop!r} literal {value!r} is not one of {allowed_values}",
                    )
                )

    for warning in sorted(set(warnings)):
        print(warning)
    for error in sorted(set(errors)):
        print(error)

    print(
        f"Checked {checked_names} island names and {checked_props} explicit prop objects "
        f"against {len(schemas)} contracts."
    )
    print(f"Warnings: {len(set(warnings))}; errors: {len(set(errors))}.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

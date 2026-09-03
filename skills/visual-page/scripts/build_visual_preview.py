#!/usr/bin/env python3
"""Build a safe local visual preview from a Lexsis compile response."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_SHELL = SKILL_DIR / "assets" / "preview-shell.html"


def script_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False).replace("<", "\\u003c")


def compiled_sections(payload: dict[str, Any]) -> list[dict[str, Any]]:
    candidates = [
        payload.get("sections"),
        payload.get("page", {}).get("sections")
        if isinstance(payload.get("page"), dict)
        else None,
        payload.get("compiled_page", {}).get("sections")
        if isinstance(payload.get("compiled_page"), dict)
        else None,
        payload.get("result", {}).get("page", {}).get("sections")
        if isinstance(payload.get("result"), dict)
        and isinstance(payload.get("result", {}).get("page"), dict)
        else None,
    ]
    sections = next((item for item in candidates if isinstance(item, list)), None)
    if sections is None:
        raise ValueError("Compile response does not contain a sections array")

    normalized: list[dict[str, Any]] = []
    for item in sections:
        if not isinstance(item, dict) or not item.get("id") or not item.get("html"):
            raise ValueError("Every compiled section requires id and html")
        normalized.append(
            {
                "id": str(item["id"]),
                "html": str(item["html"]),
                "css": str(item.get("css", "")),
                "js": str(item.get("js", "")),
            }
        )
    return normalized


def build_preview(
    compile_payload: dict[str, Any],
    *,
    theme_css: str = "",
    test_cart_data: list[dict[str, Any]] | None = None,
    commerce_config: dict[str, Any] | None = None,
    product_binding: dict[str, Any] | None = None,
    shell_path: Path = DEFAULT_SHELL,
) -> str:
    sections = compiled_sections(compile_payload)
    shell = shell_path.read_text(encoding="utf-8")

    markup = "\n".join(
        (
            f'<div data-section-id="{section["id"]}">'
            f'<div data-lx-preview-section>{section["html"]}</div>'
            "</div>"
        )
        for section in sections
    )
    section_css = "\n".join(
        section["css"] for section in sections if section["css"].strip()
    )

    replacements = {
        "{{THEME_CSS}}": theme_css,
        "{{COMPILED_SECTION_CSS}}": section_css,
        "{{COMPILED_SECTION_MARKUP}}": markup,
        "{{SECTIONS_JSON}}": script_json(sections),
        "{{TEST_CART_DATA_JSON}}": script_json(test_cart_data or []),
        "{{COMMERCE_CONFIG_JSON}}": script_json(commerce_config or {}),
        "{{PRODUCT_BINDING_JSON}}": script_json(product_binding or {}),
    }
    for token, value in replacements.items():
        shell = shell.replace(token, value)

    unresolved = [token for token in replacements if token in shell]
    if unresolved:
        raise ValueError(f"Preview shell still contains tokens: {unresolved}")
    return shell


def read_json(path: Path | None, default: Any) -> Any:
    if path is None:
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("compile_response", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--theme-css", type=Path)
    parser.add_argument("--test-cart-data", type=Path)
    parser.add_argument("--commerce-config", type=Path)
    parser.add_argument("--product-binding", type=Path)
    parser.add_argument("--shell", type=Path, default=DEFAULT_SHELL)
    args = parser.parse_args()

    preview = build_preview(
        read_json(args.compile_response, {}),
        theme_css=(
            args.theme_css.read_text(encoding="utf-8")
            if args.theme_css
            else ""
        ),
        test_cart_data=read_json(args.test_cart_data, []),
        commerce_config=read_json(args.commerce_config, {}),
        product_binding=read_json(args.product_binding, {}),
        shell_path=args.shell,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(preview, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

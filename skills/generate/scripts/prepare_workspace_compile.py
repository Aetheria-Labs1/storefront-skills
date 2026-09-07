#!/usr/bin/env python3
"""Prepare exact Lexsis MCP compile/create inputs from a page workspace."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path.name} must contain a JSON object")
    return value


def prepare(directory: Path) -> dict[str, Any]:
    manifest_path = directory / "page-manifest.json"
    source_path = directory / "lexsis-source.html"
    theme_path = directory / "page-theme.css"
    for path in (manifest_path, source_path, theme_path):
        if not path.is_file():
            raise ValueError(f"{path.name} is missing")

    manifest = load_json(manifest_path)
    config = manifest.get("config")
    if not isinstance(config, dict):
        raise ValueError("page-manifest.json config must be an object")

    head = config.get("head")
    scripts = config.get("scripts", [])
    product_binding = config.get("productBinding", {})
    commerce_config = config.get("commerceConfig", {})
    if not isinstance(head, dict) or not str(head.get("title", "")).strip():
        raise ValueError("config.head.title is required")
    if not isinstance(scripts, list):
        raise ValueError("config.scripts must be an array")
    if not isinstance(product_binding, dict):
        raise ValueError("config.productBinding must be an object")
    if not isinstance(commerce_config, dict):
        raise ValueError("config.commerceConfig must be an object")

    source = source_path.read_text(encoding="utf-8")
    theme_css = theme_path.read_text(encoding="utf-8")
    if not source.strip():
        raise ValueError("lexsis-source.html cannot be empty")
    if not theme_css.strip():
        raise ValueError("page-theme.css cannot be empty")

    compile_args = {
        "source": source,
        "head": head,
        "theme_css": theme_css,
        "scripts": scripts,
        "mode": "summary",
    }
    create_args = {
        "slug": manifest.get("page", {}).get("handle"),
        "title": manifest.get("page", {}).get("title") or head.get("title"),
        "archetype": manifest.get("page", {}).get("archetype", "landing"),
        "publish": False,
        "theme_id": manifest.get("themeId"),
        "product_binding": product_binding,
        "workspace_id": manifest.get("workspaceId"),
        "store_id": manifest.get("storeId"),
    }
    if not create_args["slug"]:
        raise ValueError("page.handle is required")

    return {
        "schemaVersion": 1,
        "workingDirectory": str(directory),
        "compile": compile_args,
        "create": create_args,
        "commerceConfig": commerce_config,
        "hashes": {
            "source": sha256(source),
            "themeCss": sha256(theme_css),
            "compileInput": sha256(
                json.dumps(
                    {
                        "source": source,
                        "head": head,
                        "theme_css": theme_css,
                        "scripts": scripts,
                        "product_binding": product_binding,
                        "commerce_config": commerce_config,
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                )
            ),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("working_directory", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        help="Write the request envelope to this file instead of stdout",
    )
    args = parser.parse_args()
    try:
        payload = prepare(args.working_directory.resolve())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 1

    encoded = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
        print(
            json.dumps(
                {
                    "ok": True,
                    "output": str(args.output.resolve()),
                    "hashes": payload["hashes"],
                },
                sort_keys=True,
            )
        )
    else:
        sys.stdout.write(encoded)
    return 0


if __name__ == "__main__":
    sys.exit(main())

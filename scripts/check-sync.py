#!/usr/bin/env python3
"""Require reference parity across all distribution packages."""
import filecmp
import sys
from pathlib import Path

errors = []

# --- Guard 1: cursor/rules/reference/ must NOT exist ---
cursor_ref = Path("cursor/rules/reference")
if cursor_ref.exists():
    errors.append("cursor/rules/reference/ still exists — delete it, cursor uses ../../reference/ paths")

# --- Guard 1b: mcp-skills/ must NOT exist ---
mcp_skills = Path("mcp-skills")
if mcp_skills.exists():
    errors.append("mcp-skills/ still exists — it was removed in Phase 2 (redundant with plugins/commands/)")

# --- Guard 2: Codex ↔ Plugin parity (existing check) ---
ref_dir = Path("plugins/lexsis-storefront-skills/skills/storefront-engine/reference")
codex_dir = Path("codex/skills/storefront-engine/reference")

if not ref_dir.exists() or not codex_dir.exists():
    errors.append("Missing Claude or Codex reference directory")
else:
    ref_files = sorted(
        path.relative_to(ref_dir)
        for path in ref_dir.rglob("*")
        if path.is_file() and path.name != ".DO-NOT-EDIT"
    )
    codex_files = sorted(
        path.relative_to(codex_dir)
        for path in codex_dir.rglob("*")
        if path.is_file() and path.name != ".DO-NOT-EDIT"
    )
    missing = [p for p in ref_files if p not in codex_files]
    extra = [p for p in codex_files if p not in ref_files]
    mismatched = [
        p for p in ref_files
        if p in codex_files and not filecmp.cmp(ref_dir / p, codex_dir / p, shallow=False)
    ]

    for label, paths in (("missing", missing), ("extra", extra), ("content mismatch", mismatched)):
        if paths:
            errors.append(f"Codex reference {label}: {len(paths)} files")
            for p in paths[:5]:
                errors.append(f"  - {p}")

    if not (missing or extra or mismatched):
        print(f"Codex: all {len(ref_files)} reference files match plugin")

# --- Report ---
if errors:
    for e in errors:
        print(f"::error::{e}")
    sys.exit(1)

print("All checks passed.")

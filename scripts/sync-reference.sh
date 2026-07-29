#!/usr/bin/env bash
set -euo pipefail

# Sync canonical reference/ → distribution packages that need real copies.
# Run after editing any file in reference/.

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ROOT_REF="$REPO_ROOT/reference"
CODEX_REF="$REPO_ROOT/codex/skills/storefront-engine/reference"

if [ ! -d "$ROOT_REF" ]; then
  echo "Error: reference/ directory not found at $ROOT_REF"
  exit 1
fi

# --- Codex: mirror top-level .md files (real copies for distribution) ---
echo "Syncing top-level .md files to codex..."
count=0
for src in "$ROOT_REF"/*.md; do
  [ -f "$src" ] || continue
  cp "$src" "$CODEX_REF/$(basename "$src")"
  count=$((count + 1))
done
echo "  $count files synced"

# --- Codex islands: update only files that already exist (don't add new ones) ---
echo "Syncing island files to codex..."
island_count=0
while IFS= read -r -d '' existing; do
  rel="${existing#"$CODEX_REF/"}"
  src="$ROOT_REF/$rel"
  if [ -f "$src" ]; then
    cp "$src" "$existing"
    island_count=$((island_count + 1))
  fi
done < <(find "$CODEX_REF/islands" -type f -print0 2>/dev/null)
echo "  $island_count island files synced"

echo "Sync complete."

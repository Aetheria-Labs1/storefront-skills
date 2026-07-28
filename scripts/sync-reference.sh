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

# --- Vertical plugins: copy with rename ---
echo "Syncing vertical plugins..."
declare -A VERTICALS=(
  [beauty]="plugins/lexsis-beauty-skills/skills/storefront-engine/reference/beauty-expertise.md"
  [fashion]="plugins/lexsis-fashion-skills/skills/storefront-engine/reference/fashion-expertise.md"
  [food]="plugins/lexsis-food-skills/skills/storefront-engine/reference/food-expertise.md"
  [home]="plugins/lexsis-home-skills/skills/storefront-engine/reference/home-expertise.md"
  [luxury]="plugins/lexsis-luxury-skills/skills/storefront-engine/reference/luxury-expertise.md"
  [supplements]="plugins/lexsis-supplements-skills/skills/storefront-engine/reference/supplements-expertise.md"
)

vert_count=0
for vertical in "${!VERTICALS[@]}"; do
  src="$ROOT_REF/vertical-${vertical}.md"
  dst="$REPO_ROOT/${VERTICALS[$vertical]}"
  if [ -f "$src" ] && [ -d "$(dirname "$dst")" ]; then
    cp "$src" "$dst"
    vert_count=$((vert_count + 1))
  fi
done
echo "  $vert_count vertical files synced"

echo "Sync complete."

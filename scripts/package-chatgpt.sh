#!/usr/bin/env bash
# Zip chatgpt/ (symlinks resolved) for ChatGPT workspace upload:
# Admin console -> Plugins -> Add -> Upload plugin.
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
version="$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["version"])' "$root/.claude-plugin/plugin.json")"
out="$root/dist/lexsis-storefront-chatgpt-$version.zip"
stage="$(mktemp -d)"; trap 'rm -rf "$stage"' EXIT
cp -RL "$root/chatgpt" "$stage/lexsis-storefront-skills"
mkdir -p "$root/dist"; rm -f "$out"
(cd "$stage/lexsis-storefront-skills" && zip -qr "$out" . -x '*/__pycache__/*' '*.DS_Store')
echo "$out"

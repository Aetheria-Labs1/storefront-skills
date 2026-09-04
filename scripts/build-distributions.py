#!/usr/bin/env python3
"""Build generated distributions from the canonical skills/ tree.

Canonical source of truth: skills/<name>/SKILL.md (Agent Skills spec,
agentskills.io) with shared resources at
skills/storefront-engine/references/.

Everything else is DERIVED:
  gpt/knowledge.md      — concatenation of skill bodies + curated references
  gpt/instructions.md   — persona template with version injected

Claude Code, Codex, and Cursor need no generation step — they discover the
canonical tree directly (.claude plugin via plugins/*/skills symlink, Codex and
Cursor via .agents/skills symlink).

Also validates:
  - spec frontmatter on every skill (name == dirname, <=64 chars, description
    non-empty <=500 chars — the Codex cap, stricter than the spec's 1024)
  - all symlinks resolve
  - no retired tool names anywhere
  - phase numbering is the contiguous Phase 1-5 scheme

Usage:
  python3 scripts/build-distributions.py           # regenerate
  python3 scripts/build-distributions.py --check   # CI: fail if anything would change
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
REFERENCES = SKILLS / "storefront-engine" / "references"
SHARED_RESOURCE_DIRS = {"storefront-engine"}

RETIRED_TOOLS = [
    "write_vibe_page",
    "preview_vibe_page",
    "get_cart_config",
    "update_cart_config",
    "validate_cart_rules",
    "validate_vibe_page",
    "publish_vibe_page",
    "update_page_section",
    "preview_section_update",
    "edit_asset",
]

STALE_GUIDANCE = {
    "CDN included in renderer": "Tailwind is compiled page-wide; there is no runtime Tailwind CDN",
    "score > 0.7": "template search does not expose a stable score threshold",
}

REFERENCE_PATH_RE = re.compile(
    r"((?:storefront-engine/)?references/[A-Za-z0-9_./-]+\.md)"
)

# References worth shipping to a custom GPT (knowledge budget is finite;
# schemas and vertical deep-dives stay out — the GPT can't call tools to
# follow up anyway, so operational docs matter more than raw data).
GPT_REFERENCE_ALLOWLIST = [
    "storefront-craft",
    "generation-protocol",
    "source-format",
    "workflow-orchestration",
    "conversion-psychology",
    "island-patterns",
    "style-packs",
    "asset-prep",
    "qa-recipe",
    "publishing",
    "page-generation",
    "page-editing",
    "source-artifact-workflow",
    "island-preview",
    "visual-layout-workflow",
    "workflow-handoffs",
    "lexsis-mcp-contract",
    "lexsis-design-capabilities",
]

def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError(f"{path}: missing frontmatter")
    fm: dict[str, str] = {}
    for line in m.group(1).split("\n"):
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, m.group(2)


def plugin_version() -> str:
    pj = json.loads((ROOT / "plugins/lexsis-storefront-skills/.claude-plugin/plugin.json").read_text())
    return pj["version"]


def validate() -> list[str]:
    errors: list[str] = []

    codex_version = json.loads(
        (ROOT / "codex/.codex-plugin/plugin.json").read_text()
    ).get("version")
    if codex_version != plugin_version():
        errors.append(
            f"plugin version drift: Claude={plugin_version()!r}, "
            f"Codex={codex_version!r}"
        )

    for skill_dir in sorted(SKILLS.iterdir()):
        if not skill_dir.is_dir():
            continue
        sk = skill_dir / "SKILL.md"
        if not sk.exists():
            if skill_dir.name in SHARED_RESOURCE_DIRS:
                continue
            errors.append(f"{skill_dir.name}: no SKILL.md")
            continue
        try:
            fm, body = parse_frontmatter(sk)
        except ValueError as e:
            errors.append(str(e))
            continue
        name = fm.get("name", "")
        desc = fm.get("description", "")
        if name != skill_dir.name:
            errors.append(f"{skill_dir.name}: frontmatter name {name!r} != directory name (spec requires match)")
        if len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name or "x"):
            errors.append(f"{skill_dir.name}: name violates spec (<=64 chars, lowercase/digits/hyphens)")
        if not desc:
            errors.append(f"{skill_dir.name}: empty description")
        elif len(desc) > 500:
            errors.append(f"{skill_dir.name}: description {len(desc)} chars > 500 (Codex cap)")
        for tool in RETIRED_TOOLS:
            if tool in body:
                errors.append(f"{skill_dir.name}: references retired tool {tool}")
        for reference in REFERENCE_PATH_RE.findall(body):
            if reference.startswith("storefront-engine/"):
                candidates = [
                    ROOT / "skills" / reference,
                ]
            else:
                candidates = [
                    skill_dir / reference,
                    REFERENCES / reference.removeprefix("references/"),
                ]
            if not any(path.is_file() for path in candidates):
                errors.append(
                    f"{skill_dir.name}: references missing document {reference}"
                )
        if re.search(r"<[^>]+data-island=|data-props=['\"]", body):
            errors.append(
                f"{skill_dir.name}: raw compiled island markup in an authoring skill; "
                "use <lx-island> source format instead"
            )

    # Phase scheme: nothing outside Phase 1-5 / 4a / 4b
    bad_phase = re.compile(r"Phase (-1|0|2A|2B|A\b|B\b)")
    for md in SKILLS.rglob("*.md"):
        text = md.read_text()
        for stale, replacement in STALE_GUIDANCE.items():
            if stale in text:
                errors.append(
                    f"{md.relative_to(ROOT)}: stale guidance {stale!r}; {replacement}"
                )
        for i, line in enumerate(text.split("\n"), 1):
            if bad_phase.search(line):
                errors.append(f"{md.relative_to(ROOT)}:{i}: stale phase numbering: {line.strip()[:80]}")

    # Reference docs may illustrate compiled renderer markup, but must label it
    # so an agent does not copy it into source-authoring tools.
    for reference in REFERENCES.rglob("*.md"):
        text = reference.read_text()
        if reference.name == "source-format.md":
            continue
        if re.search(r"<[^>]+data-island=|data-props=['\"]", text) and "Compiled runtime reference:" not in text:
            errors.append(
                f"{reference.relative_to(ROOT)}: compiled island markup is missing the source-format notice"
            )

    # Symlinks resolve
    for link in [ROOT / ".agents/skills", ROOT / "plugins/lexsis-storefront-skills/skills"]:
        if not link.is_symlink():
            errors.append(f"{link.relative_to(ROOT)}: expected symlink")
        elif not link.resolve().exists():
            errors.append(f"{link.relative_to(ROOT)}: broken symlink")

    return errors


def derived_counts() -> dict[str, int]:
    islands_dir = REFERENCES / "islands"
    schemas = [
        json.loads(path.read_text())
        for path in islands_dir.glob("*/schema.json")
    ]
    return {
        "skills": len([d for d in SKILLS.iterdir() if d.is_dir() and (d / "SKILL.md").exists()]),
        "references": len(list(REFERENCES.glob("*.md"))),
        "island_schemas": len(schemas),
        "active_islands": sum(
            not schema.get("deprecated", False) for schema in schemas
        ),
    }


def build_gpt() -> dict[str, str]:
    version = plugin_version()
    counts = derived_counts()
    banner = (
        f"<!-- GENERATED from skills/ by scripts/build-distributions.py — DO NOT EDIT.\n"
        f"     storefront-skills v{version} · {counts['skills']} skills · "
        f"{counts['active_islands']} active islands -->\n\n"
    )

    parts: list[str] = [banner, "# Lexsis Storefront Skills — Knowledge Base\n"]

    parts.append("\n## Workflows\n")
    for skill_dir in sorted(SKILLS.iterdir()):
        sk = skill_dir / "SKILL.md"
        if not skill_dir.is_dir() or not sk.exists():
            continue
        fm, body = parse_frontmatter(sk)
        if fm.get("disable-model-invocation") == "true":
            continue  # maintainer tools stay out of the GPT
        parts.append(f"\n---\n\n# Skill: {fm['name']}\n\n> {fm['description']}\n\n{body.strip()}\n")
        local_references = skill_dir / "references"
        if local_references.is_dir():
            for reference in sorted(local_references.glob("*.md")):
                parts.append(
                    f"\n### {fm['name']} reference: {reference.stem}\n\n"
                    f"{reference.read_text().strip()}\n"
                )

    parts.append("\n---\n\n## Reference Knowledge\n")
    for name in GPT_REFERENCE_ALLOWLIST:
        ref = REFERENCES / f"{name}.md"
        if ref.exists():
            parts.append(f"\n---\n\n{ref.read_text().strip()}\n")

    knowledge = "".join(parts)

    instructions = f"""{banner}You are the Lexsis Storefront assistant. You help merchants plan, generate,
edit, and optimize AI-built Shopify storefront pages using the Lexsis AI MCP
(https://mcp.trylexsis.com/mcp).

Use the normal workflow when building a page:
setup → plan-page → visual-page → asset-prep → generate → publish.
Each command remains independently invokable, and explicit skips are recorded.
Run the mandatory MCP preflight before Lexsis-dependent work. Configuration is
not proof of availability. If discovery fails, return BLOCKED_LEXSIS_MCP and
do not substitute static HTML unless the user explicitly requests an offline
prototype.
Search page kits and section templates before custom composition. Load the
selected LX theme, use --lx-* tokens and compile-time Tailwind utilities, and
resolve every selected island schema before authoring it.
Author pages in source format, never hand-written data-island/data-props JSON.
Never invent island names or props; resolve the current schema first. Never use
retired tools.
"""
    return {"gpt/knowledge.md": knowledge, "gpt/instructions.md": instructions}


def main() -> int:
    check = "--check" in sys.argv

    errors = validate()
    if errors:
        print(f"VALIDATION FAILED ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
        return 1

    outputs = build_gpt()
    # Generated output must never carry retired tools — if it does, a canonical
    # skill re-introduced one and the allowlist above needs pruning.
    for rel, content in outputs.items():
        for tool in RETIRED_TOOLS:
            if tool in content:
                print(f"FATAL: generated {rel} would contain retired tool {tool}")
                return 1
    changed = []
    for rel, content in outputs.items():
        path = ROOT / rel
        if not path.exists() or path.read_text() != content:
            changed.append(rel)
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)

    counts = derived_counts()
    print(f"skills={counts['skills']} references={counts['references']} island_schemas={counts['island_schemas']}")
    if check:
        if changed:
            print(f"DRIFT: {len(changed)} generated file(s) out of date: {', '.join(changed)}")
            print("Run: python3 scripts/build-distributions.py")
            return 1
        print("All generated distributions up to date.")
    else:
        print(f"Regenerated: {', '.join(changed) if changed else 'nothing (already current)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

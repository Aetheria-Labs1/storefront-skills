#!/usr/bin/env python3
"""Build generated distributions from the canonical skills/ tree.

Canonical source of truth: skills/<name>/SKILL.md (Agent Skills spec,
agentskills.io) with shared resources at
skills/storefront-engine/references/.

Everything else is DERIVED:
  gpt/knowledge.md      — concatenation of skill bodies + curated references
  gpt/instructions.md   — persona template with version injected

The repository root is the Claude plugin package, so Claude, Codex, Cursor,
and skills.sh all consume the same canonical `skills/` tree. Codex and Cursor
also discover it through `.agents/skills`.

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
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
REFERENCES = SKILLS / "storefront-engine" / "references"
LEGACY_CLAUDE_PLUGIN_ROOT = ROOT / "plugins" / "lexsis-storefront-skills"
SHARED_RESOURCE_DIRS = {"storefront-engine"}
SKILL_SHARED_REFERENCES = {
    "plan-page": {
        "animation-system.md",
        "page-files.md",
        "consumer-behavior-cro.md",
        "design-rules.md",
        "island-presets.md",
        "workflow-intent.md",
        "page-types/",
        "workflows/",
        "authoring/",
        "proof/",
        "offers/",
        "assets/",
        "copy/",
        "mcp-playbooks/",
    },
    "design-page": {
        "page-layout.md",
        "animation-system.md",
        "page-files.md",
        "consumer-behavior-cro.md",
        "design-concepts.md",
        "design-rules.md",
        "island-presets.md",
        "merchant-templates.md",
        "workflow-intent.md",
        "page-types/",
        "workflows/",
        "authoring/",
        "proof/",
        "offers/",
        "assets/",
        "anti-patterns/",
        "copy/",
        "mcp-playbooks/",
        "qa-recipe.md",
        "page-editing.md",
    },
    "ab-test": {
        "animation-system.md",
        "ab-testing.md",
        "consumer-behavior-cro.md",
    },
    "optimize": {
        "industry-cro.md",
        "evidence-led-cro.md",
        "animation-system.md",
        "consumer-behavior-cro.md",
        "design-rules.md",
        "lexsis-design-capabilities.md",
        "page-types/",
        "workflows/",
        "authoring/",
        "anti-patterns/",
        "plan-page.md",
        "page-editing.md",
        "qa-recipe.md",
        "offers/offer-ledger.md",
        "assets/generation-policy.md",
        "copy/",
        "proof/",
    },
    "publish": {
        "workflow-intent.md",
    },
}

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
SHARED_REFERENCE_DEP_RE = re.compile(
    r"(?:`|\()(?:(?:skills/)?storefront-engine/references/|references/)?"
    r"((?:[a-z0-9_-]+/)*[A-Za-z0-9_-]+\.md)(?:`|\))"
)

CORPUS_REFERENCE_BRIDGES = {
    "ab-testing.md", "ad-to-page.md", "animation-system.md", "asset-prep.md",
    "blob-shapes.md", "cart-composition.md", "cart-profile-management.md",
    "consumer-behavior-cro.md", "conversion-psychology.md", "cro-research.md",
    "design-assets.md", "design-enrichment.md", "design-rules.md",
    "generate-bundle-page.md", "generate-collection.md", "generate-editorial.md",
    "generate-homepage.md", "generate-landing-page.md", "generate-listicle.md",
    "generate-pdp.md", "generation-protocol.md", "island-patterns.md",
    "island-presets.md", "lexsis-mcp-contract.md", "page-files.md", "plan-page.md",
    "product-grid.md", "qa-recipe.md", "source-artifact-workflow.md",
    "source-format.md", "traffic-source-google.md", "traffic-source-meta.md",
    "traffic-source-tiktok.md", "vertical-beauty.md", "vertical-fashion.md",
    "vertical-food.md", "vertical-home.md", "vertical-luxury.md",
    "vertical-supplements.md", "visual-craft.md", "workflow-intent.md",
}

# References worth shipping to a custom GPT (knowledge budget is finite;
# schemas and vertical deep-dives stay out — the GPT can't call tools to
# follow up anyway, so operational docs matter more than raw data).
GPT_REFERENCE_ALLOWLIST = [
    "storefront-craft",
    "animation-system",
    "design-rules",
    "island-presets",
    "generation-protocol",
    "source-format",
    "workflow-orchestration",
    "conversion-psychology",
    "consumer-behavior-cro",
    "island-patterns",
    "style-packs",
    "asset-prep",
    "qa-recipe",
    "publishing",
    "page-generation",
    "page-editing",
    "source-artifact-workflow",
    "visual-layout-workflow",
    "workflow-handoffs",
    "lexsis-mcp-contract",
    "merchant-templates",
    "lexsis-design-capabilities",
    "page-types/_index",
    "page-types/_checklist-format",
    "proof/reviews-sourcing",
    "proof/proof-ledger",
    "assets/generation-policy",
    "offers/offer-types",
    "anti-patterns/dark-patterns",
    "anti-patterns/copy-anti-patterns",
    "mcp-playbooks/tool-sequence-by-stage",
    "mcp-playbooks/router-actions",
    "workflows/_how-to-read",
    "workflows/section-asset-workflow",
    "workflows/island-selection-workflow",
    "workflows/copy-workflow",
    "authoring/source-authoring",
    "authoring/css-and-styling",
]

PLAIN_SCALAR_HAZARD = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*): (\S.*)$")


def unsafe_frontmatter_scalars(path: Path) -> list[str]:
    """Frontmatter values a strict YAML parser rejects.

    The skills CLI parses SKILL.md frontmatter with a real YAML parser. An
    unquoted plain scalar may not contain ": " or " #": the parser raises
    "Nested mappings are not allowed in compact mappings" and the skill is
    dropped from discovery, so the published skill silently disappears.
    Quote the value or rephrase it.
    """
    match = re.match(r"^---\n(.*?)\n---\n", path.read_text(), re.S)
    if not match:
        return []
    problems = []
    for line in match.group(1).split("\n"):
        found = PLAIN_SCALAR_HAZARD.match(line)
        if not found:
            continue
        key, value = found.groups()
        if value[0] in "\"'|>[{&*!":  # quoted, block or flow scalar: parser-safe
            continue
        for hazard in (": ", " #"):
            if hazard in value:
                problems.append(
                    f"{path.parent.name}: frontmatter {key!r} is an unquoted scalar "
                    f"containing {hazard!r}; strict YAML parsers reject it and the "
                    "skills CLI drops the skill. Quote the value or rephrase."
                )
    return problems


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
    pj = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    return pj["version"]


def remove_legacy_claude_plugin(*, check: bool) -> list[str]:
    """Remove the old duplicate Claude package that confused skills update."""
    if not LEGACY_CLAUDE_PLUGIN_ROOT.exists():
        return []
    changed = [str(LEGACY_CLAUDE_PLUGIN_ROOT.relative_to(ROOT))]
    if not check:
        if LEGACY_CLAUDE_PLUGIN_ROOT.is_dir():
            shutil.rmtree(LEGACY_CLAUDE_PLUGIN_ROOT)
        else:
            LEGACY_CLAUDE_PLUGIN_ROOT.unlink()
        plugins_dir = LEGACY_CLAUDE_PLUGIN_ROOT.parent
        if plugins_dir.is_dir() and not any(plugins_dir.iterdir()):
            plugins_dir.rmdir()
    return changed


def expand_reference_dirs(names: set[str]) -> set[str]:
    """`page-types/` in SKILL_SHARED_REFERENCES means every .md in that directory."""
    expanded: set[str] = set()
    for name in names:
        if name.endswith("/") and (REFERENCES / name).is_dir():
            expanded.update(
                str(path.relative_to(REFERENCES))
                for path in sorted((REFERENCES / name).glob("*.md"))
            )
        else:
            expanded.add(name)
    return expanded


def shared_reference_closure(names: set[str]) -> set[str]:
    names = expand_reference_dirs(names)
    pending = list(names)
    resolved = set(names)
    while pending:
        name = pending.pop()
        source = REFERENCES / name
        if not source.is_file():
            continue
        for dependency in SHARED_REFERENCE_DEP_RE.findall(source.read_text()):
            if dependency == name or not (REFERENCES / dependency).is_file():
                continue
            if "/" in name and "/" not in dependency and dependency not in CORPUS_REFERENCE_BRIDGES:
                continue
            if dependency not in resolved:
                resolved.add(dependency)
                pending.append(dependency)
    return resolved


def packaged_reference_content(source: Path) -> str:
    return (
        source.read_text()
        .replace("skills/storefront-engine/references/", "references/")
        .replace("storefront-engine/references/", "references/")
    )


def skill_reference_roots(skill_name: str) -> set[str]:
    roots = set(SKILL_SHARED_REFERENCES.get(skill_name, set()))
    skill = SKILLS / skill_name / "SKILL.md"
    for reference in REFERENCE_PATH_RE.findall(skill.read_text()):
        roots.add(reference.split("references/", 1)[1])
    return roots


def sync_skill_shared_references(*, check: bool) -> list[str]:
    """Materialize shared docs inside public skills for per-skill installers."""
    changed: list[str] = []
    for skill in sorted(SKILLS.iterdir()):
        if not (skill / "SKILL.md").is_file():
            continue
        skill_name = skill.name
        names = skill_reference_roots(skill_name)
        target_dir = SKILLS / skill_name / "references"
        resolved = shared_reference_closure(names)
        for target in sorted(target_dir.rglob("*.md")):
            name = str(target.relative_to(target_dir))
            if name not in resolved:
                changed.append(f"{target.relative_to(ROOT)} (obsolete generated reference)")
                if not check:
                    target.unlink()
        for name in sorted(resolved):
            source = REFERENCES / name
            target = target_dir / name
            if not source.is_file():
                changed.append(
                    f"{target.relative_to(ROOT)} (missing source {source.relative_to(ROOT)})"
                )
                continue
            expected = packaged_reference_content(source)
            if not target.is_file() or target.read_text() != expected:
                changed.append(str(target.relative_to(ROOT)))
                if not check:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text(expected)
    return changed


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
        errors.extend(unsafe_frontmatter_scalars(sk))
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

    for reference in REFERENCES.rglob("*.md"):
        text = reference.read_text()
        if re.search(r"<[^>]+data-island=|data-props=['\"]", text):
            errors.append(
                f"{reference.relative_to(ROOT)}: use source-format markup, not compiled island examples"
            )

    # Local agent discovery remains a symlink to the canonical tree.
    for link in [ROOT / ".agents/skills"]:
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
        "references": len(
            [p for p in REFERENCES.rglob("*.md") if "islands" not in p.parts]
        ),
        "island_schemas": len(schemas),
        "active_islands": sum(
            not schema.get("deprecated", False) for schema in schemas
        ),
    }


def build_gpt() -> dict[str, str]:
    version = plugin_version()
    counts = derived_counts()
    banner = (
        f"<!-- GENERATED from skills/ by scripts/build-distributions.py - DO NOT EDIT.\n"
        f"     storefront-skills v{version}; {counts['skills']} skills; "
        f"{counts['active_islands']} active islands -->\n\n"
    )

    parts: list[str] = [banner, "# Lexsis Storefront Skills - Knowledge Base\n"]

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
            generated_shared = shared_reference_closure(
                skill_reference_roots(skill_dir.name)
            )
            for reference in sorted(local_references.glob("*.md")):
                if reference.name in generated_shared:
                    continue
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

Use the normal workflow when building a reviewed page:
setup -> plan-page -> design-page -> publish.
plan-page returns a complete specification (final section copy, an asset
decision for every section, claim gate, work queue, plan status) and waits for
explicit approval. design-page builds it, creates one unpublished hosted draft,
runs hosted QA at 390, 768 and 1280 with commerce checks, applies later edits
with expected_version, and returns DESIGN_APPROVED. optimize scores an existing
page against the same rules, proposes a plan with the same blocks, and applies
approved changes. design-page may generate a mobile-first visual concept before
source when the user wants to approve the look.
Each command remains independently invokable, and explicit skips are recorded.
Infer only question depth and publish-versus-draft intent from the request;
plan approval before design and live publishing always require explicit
approval for the named page and version.
Use the exact router/action pairs declared by each skill. Call
lexsis_discover only for an unfamiliar argument schema, using its structured
router and action fields. A zero-result discovery lookup is not an MCP outage;
the actual domain call determines availability. Report its concrete error and
do not substitute static HTML unless the user explicitly requests an offline
prototype.
Search page kits and section templates before custom composition. Load the
selected LX theme, use --lx-* tokens and compile-time Tailwind utilities, and
resolve every selected island schema before authoring it.
Author pages in source format, never hand-written data-island/data-props JSON.
Send source and optional theme_css directly through MCP. Do not create local
page files, preview builds or local QA gates; review the hosted draft.
Never invent island names or props; resolve the current schema first. Never use
retired tools.
"""
    return {"gpt/knowledge.md": knowledge, "gpt/instructions.md": instructions}


def main() -> int:
    check = "--check" in sys.argv

    shared_reference_changes = sync_skill_shared_references(check=check)
    legacy_plugin_changes = remove_legacy_claude_plugin(check=check)
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
    changed = [*shared_reference_changes, *legacy_plugin_changes]
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

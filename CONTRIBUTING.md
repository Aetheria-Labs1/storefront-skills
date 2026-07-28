# Contributing to Lexsis Storefront Skills

Thanks for your interest in contributing! This repo contains AI skill packs that teach coding agents (Claude Code, OpenAI Codex, Cursor, GPTs) how to build high-converting Shopify landing pages.

## Types of Contributions

| Type | What it is | Example |
|------|-----------|---------|
| **Vertical plugin** | Industry-specific expertise | `lexsis-pets-skills` |
| **Core skill** | Reference knowledge for page generation | `animation-system.md` |
| **Command** | Slash command workflow | `/generate-quiz` |
| **Bug fix** | Fix incorrect instructions or broken skills | Typo in island props |

## Skill File Structure

All skills are markdown files with YAML frontmatter:

```markdown
---
description: One-line description of what this skill does
allowed-tools: mcp__lexsis-ai__*
---

# Skill Title

Content goes here...
```

### Required frontmatter fields

| Field | Purpose |
|-------|---------|
| `description` | Shown in skill listings and used for auto-triggering |
| `allowed-tools` | MCP tools this skill can invoke (usually `mcp__lexsis-ai__*`) |

## Directory Structure

```
plugins/lexsis-storefront-skills/
├── .claude-plugin/
│   └── plugin.json          ← Plugin metadata (name, version, author)
├── commands/                ← Slash commands (/generate, /optimize, etc.)
│   ├── generate.md
│   ├── optimize.md
│   └── ...
├── skills/
│   └── storefront-engine/
│       ├── SKILL.md         ← Main orchestrator (auto-loaded)
│       └── reference/       ← Knowledge skills (loaded on demand)
│           ├── craft-guide.md
│           ├── island-patterns.md
│           ├── islands/     ← Island-specific docs + layout JSONs
│           └── ...
└── agents/                  ← Agent definitions
```

## Adding a Vertical Plugin

1. Create directory: `plugins/lexsis-{name}-skills/`
2. Add plugin config:

```
plugins/lexsis-{name}-skills/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── storefront-engine/
        ├── SKILL.md
        └── reference/
            └── {name}-expertise.md
```

3. Create `plugin.json`:

```json
{
  "name": "lexsis-{name}-skills",
  "description": "Your description here",
  "version": "1.0.0",
  "author": { "name": "Your Name" },
  "license": "MIT"
}
```

4. Register in `.claude-plugin/marketplace.json` at repo root
5. Submit PR

## Adding a Command

1. Create `plugins/lexsis-storefront-skills/commands/{name}.md`
2. Structure:

```markdown
---
description: What the command does in one line
allowed-tools: mcp__lexsis-ai__*
---

# /{name}

## When to Use
- Trigger conditions...

## Workflow
1. Step one...
2. Step two...

## Tool Usage
\`\`\`json
{ "name": "tool_name", "arguments": { ... } }
\`\`\`
```

3. Register in `manifest.json` under `commands[]`

## Adding a Knowledge Skill

1. Create `plugins/lexsis-storefront-skills/skills/storefront-engine/reference/{name}.md`
2. Add frontmatter with `description`
3. Write the knowledge content (patterns, techniques, examples)
4. Reference it from `SKILL.md` if it should auto-load

## PR Process

1. **Fork** this repo
2. **Branch** from `main` — use `feat/`, `fix/`, or `docs/` prefix
3. **Commit** with conventional commits: `feat: add pets vertical`, `fix: correct BuyBox props`
4. **Push** and open a PR
5. CI validates your JSON and frontmatter automatically
6. A maintainer will review — we aim for 48hr turnaround

## Local Testing

```bash
# Validate JSON
python3 -c "import json; json.load(open('plugins/lexsis-storefront-skills/.claude-plugin/plugin.json'))"

# Run validation scripts
python3 scripts/validate-plugins.py
python3 scripts/validate-frontmatter.py

# Install locally in Claude Code (test your changes)
/plugin install ./plugins/lexsis-storefront-skills

# Test a command
/your-new-command
```

## Reference Files (Single Source of Truth)

All reference `.md` files live in `reference/` at the repo root. Distribution packages (codex, vertical plugins) contain copies for standalone installation.

**Editing reference content:**
1. Edit in `reference/` only
2. Run `scripts/sync-reference.sh`
3. Commit both the source and synced copies

**CI enforces this**: `scripts/check-sync.py` fails the build if copies diverge.

**Do NOT:**
- Create `cursor/rules/reference/` (cursor reads root directly via relative paths)
- Edit files in `codex/skills/storefront-engine/reference/` directly
- Edit vertical plugin `*-expertise.md` files directly

## Style Guide

- Use ATX headings (`#`, `##`, not underlines)
- End files with a newline
- Use fenced code blocks with language identifiers
- Keep lines readable (no strict wrap limit for prose)
- Use tables for structured data (props, options, variants)
- Prefer concrete examples over abstract descriptions

## Questions?

Open a [Discussion](https://github.com/Aetheria-Labs1/storefront-skills/discussions) or file an issue using the templates.

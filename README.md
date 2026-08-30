# Lexsis AI — Storefront Skills

> Native AI workflows for building high-converting Shopify storefronts. One canonical skill set ([Agent Skills standard](https://agentskills.io)), consumable from Claude Code, OpenAI Codex, Cursor, and custom GPTs.

## The one-line install

```bash
npx skills add Aetheria-Labs1/storefront-skills
```

[skills.sh](https://skills.sh) symlinks the canonical `skills/` into whichever agents you use. Or install per-platform:

## Install the Lexsis MCP

This installer adds the full Lexsis storefront skill pack for the selected
clients, configures the credential-free remote MCP, and opens OAuth on first
use:

```bash
curl -fsSL https://mcp.trylexsis.com/install.sh -o /tmp/lexsis-mcp-install.sh
sh /tmp/lexsis-mcp-install.sh
```

Choose one or more supported clients interactively, or pass a target directly:

```bash
sh /tmp/lexsis-mcp-install.sh codex
sh /tmp/lexsis-mcp-install.sh claude-project
sh /tmp/lexsis-mcp-install.sh cursor-global
sh /tmp/lexsis-mcp-install.sh --dry-run auto
```

The installer never stores a user credential. Restart the client and complete
the Lexsis OAuth prompt when it first connects. Select the workspaces and
minimum Read, Build, or Publish access needed for the task. Use `--skip-skills`
for an MCP-only setup.

## Install (Claude Code)

```bash
# 1. Register marketplace (one-time)
/plugin marketplace add lexsis https://github.com/Aetheria-Labs1/storefront-skills

# 2. Install
/plugin install lexsis-storefront-skills@lexsis
```

Skills auto-load, the MCP auto-configures, and every skill is invocable as `/skill-name`.

## Install (OpenAI Codex)

```bash
codex plugin marketplace add Aetheria-Labs1/storefront-skills --ref main
codex plugin add lexsis-storefront-skills@lexsis-storefront
```

Or zero-install: clone the repo anywhere inside your project — Codex discovers `.agents/skills/` automatically. Invoke with `$skill-name` (`$generate`, `$cart`) or let Codex select from your request. Complete the `lexsis-ai` OAuth prompt when Codex requests MCP access.

## Install (Cursor)

Nothing to copy. Cursor reads the Agent Skills standard from `.agents/skills/` natively — clone the repo (or use `npx skills add`) and the skills appear. The old `cursor/rules/*.mdc` file is gone as of v5.0.0.

## Install (Custom GPT)

1. Copy `gpt/instructions.md` → paste into GPT Instructions
2. Upload `gpt/knowledge.md` as a Knowledge file

Both files are **generated** from the canonical skills by `scripts/build-distributions.py` — never edit them by hand.

## What's Included

- **14 independently runnable skills** — one directory per workflow under `skills/`, spec-compliant SKILL.md each
- **2 agents** (cro-analyzer, page-builder) for Claude Code
- **54 reference docs** (CRO patterns, verticals, traffic sources, workflows) under `skills/storefront-engine/references/`
- **54 island schemas** with layouts under `references/islands/`
- Vertical expertise: beauty, supplements, fashion, food, luxury, home
- Traffic-source patterns: Meta, Google, TikTok

## Skills

Invoke as `/name` (Claude Code) or `$name` (Codex); most also trigger automatically from a matching request.

| Skill | What it does |
|-------|--------------|
| `plan-page` | Discover requirements, design section layout, get plan approval |
| `asset-prep` | Source images/video — brand library first, then generation, import, external MCPs |
| `generate` | Generate a Shopify page — auto-detects type (PDP, landing, collection, homepage, editorial, listicle, bundle) |
| `optimize` | CRO-optimize an existing page — CTAs, trust signals, mobile UX |
| `remix` | Rebuild a competitor page or ad creative adapted to your brand |
| `experiment` | A/B tests, personalization variants, results monitoring |
| `cart` | Cart profiles — upsells, progress bars, conditional rules |
| `publish` | QA, draft preview, and go-live (only after explicit approval) |
| `analyze-page` | Turn a reference URL into a reproducible design + CRO brief |
| `browser-analyze` | Deep URL analysis via a browser tool when available |
| `search-docs` | Search Lexsis docs — islands, workflows, troubleshooting |
| `storefront-engine` | Orchestrator for broad multi-step requests; owns the reference corpus |
| `extract-island` | Maintainer tool — convert a live component into a reusable island layout (explicit invocation only) |

## Workflow Sequence

Every page moves through one contiguous sequence — **Phase 1 Plan → Phase 2 Context → Phase 3 Assets → Phase 4 Build → Phase 5 Ship**:

```
/plan-page → /asset-prep → /generate → /optimize
```

| Step | Output |
|------|--------|
| `/plan-page` | Approved page plan (Phase 1 — mandatory gate) |
| `/asset-prep` | Asset manifest |
| `/generate` | Draft page + preview URL (Phases 2-5) |
| `/optimize` | CRO fixes applied section-by-section |

Each step is independent — start anywhere. `/plan-page` → `/generate` skips asset-prep when the brand library has everything.

## MCP Server

- **Codex and Claude Code:** connect the hosted `lexsis-ai` HTTP server and
  complete browser OAuth when prompted. User API keys and manually configured
  `Authorization` headers are not supported.

## External MCPs (Optional)

`asset-prep` detects and uses these when installed — none required:

| MCP | Adds |
|-----|------|
| **Playwright** | Visual QA, screenshots, CRO audit |
| **Exa** | Image research, mood boards, competitor screenshots |
| **HiggsField** | AI video generation for hero sections |
| **OpenArt** | Specialized AI illustration |

## Repo Structure

```
storefront-skills/
├── skills/                          ← CANONICAL — one dir per skill (Agent Skills spec)
│   └── storefront-engine/
│       └── references/              ← shared reference corpus + island schemas
├── .agents/skills → skills/         ← Codex + Cursor native discovery (symlink)
├── plugins/lexsis-storefront-skills/← Claude Code plugin (skills → symlink, agents, MCP config)
├── codex/                           ← Codex plugin manifest + MCP config
├── gpt/                             ← GENERATED — custom GPT instructions + knowledge
├── cursor/                          ← pointer README (Cursor needs no copies)
└── scripts/build-distributions.py   ← regenerates gpt/, validates everything (CI gate)
```

One source of truth: edit `skills/`, run `python3 scripts/build-distributions.py`, commit. CI fails on drift.

> **Windows note:** the fan-out uses symlinks — clone with `git config core.symlinks true`.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). Short version: edit canonical `skills/` only; the build script and CI keep every distribution in sync. Skill frontmatter must pass the [Agent Skills spec](https://agentskills.io/specification) (name = directory name, ≤64 chars; description ≤500 chars).

## License

MIT — [LICENSE](./LICENSE)

---

Built with [Lexsis AI](https://trylexsis.com)

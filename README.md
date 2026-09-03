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

- **10 focused storefront commands** — six core workflow commands and four optional operations
- **2 agents** (cro-analyzer, page-builder) for Claude Code
- Shared CRO, vertical, traffic-source, workflow, and island references under `skills/storefront-engine/references/`
- **47 active islands** plus 7 deprecated compatibility contracts under
  `skills/storefront-engine/references/islands/`
- Vertical expertise: beauty, supplements, fashion, food, luxury, home
- Traffic-source patterns: Meta, Google, TikTok

## Skills

Invoke as `/name` (Claude Code) or `$name` (Codex); most also trigger automatically from a matching request.

| Skill | What it does |
|-------|--------------|
| `setup` | Save reusable brand and theme context for one or more stores |
| `plan-page` | Turn campaign requirements into an approved page plan |
| `visual-page` | Build a responsive mockup with interactive Lexsis island previews |
| `asset-prep` | Replace temporary media with verified production assets |
| `generate` | Write readable source, compile, create a draft, and run hosted QA |
| `publish` | Release a synchronized draft only after explicit approval |
| `analyze-page` | Analyze a URL, screenshot, ad, or existing page |
| `optimize` | Improve an existing page for a chosen business outcome |
| `experiment` | Create and evaluate focused storefront experiments |
| `cart` | Inspect, assign, and edit cart profiles |

## Workflow Sequence

Run setup once for the stores and themes you use:

```text
/setup
```

The normal page workflow is:

```text
/setup
  → /plan-page
  → /visual-page
  → /asset-prep
  → /generate
  → /publish (separate approval)
```

| Step | Output |
|------|--------|
| `/setup` | Saved store brand reference and theme CSS, indexed by store and theme |
| `/plan-page` | Approved campaign, content, and section plan |
| `/visual-page` | Readable visual source plus an interactive local preview |
| `/asset-prep` | Verified final asset manifest and updated mockup |
| `/generate` | Readable source, synchronized draft, preview URL, and QA report |
| `/publish` | Explicit release of the reviewed page version |

When several saved stores or themes are available, every page records the
selected `storeId` and `themeId`; it never silently switches themes. Commands
remain independently invokable, and explicitly skipped steps are recorded in
the page manifest.

`visual-page` authors readable `<lx-island>` source, dry-run compiles it, and
loads Lexsis's exported island runtime in a safe local preview. Complex
components such as shoppable video can therefore be reviewed before draft
creation. Cart and checkout writes remain disabled locally and are certified
on the hosted draft created by `generate`.

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
├── skills/                          ← CANONICAL public Agent Skills
│   ├── visual-page/assets/          ← preview shell + neutral placeholders
│   └── storefront-engine/           ← shared resources, not a public command
│       └── references/              ← workflow guidance + island schemas
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

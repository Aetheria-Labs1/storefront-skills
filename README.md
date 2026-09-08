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

- **12 focused storefront commands** — five reviewed-workflow commands and seven optional or fast-path operations
- **2 agents** (cro-analyzer, page-builder) for Claude Code
- Shared CRO, vertical, traffic-source, workflow, and island references under `skills/storefront-engine/references/`, including the house `design-rules.md` and `island-presets.md`
- A consumer-behavior CRO framework that turns shopper uncertainty, gallery
  gaps, compatibility, solution completion, trust, and mobile context into
  page-specific hypotheses instead of generic conversion modules
- **47 active islands** plus 7 deprecated compatibility contracts under
  `skills/storefront-engine/references/islands/`
- Vertical expertise: beauty, supplements, fashion, food, luxury, home
- Traffic-source patterns: Meta, Google, TikTok

## Skills

Invoke as `/name` (Claude Code) or `$name` (Codex); most also trigger automatically from a matching request.

| Skill | What it does |
|-------|--------------|
| `setup` | Save reusable brand and theme context for one or more stores |
| `plan-page` | Produce a one-page plan at the depth implied by the user's intent |
| `design-page` | Build source, compile it, and create one unpublished hosted draft |
| `build` | Create the fastest unpublished draft from a prompt or automatically selected template |
| `build-with-template` | Create an unpublished draft directly from a supplied template URL |
| `asset-prep` | Independently search, generate, import, or replace media |
| `generate` | Create an unpublished draft early, then synchronize and QA it to production readiness |
| `publish` | Release a synchronized draft only after explicit approval |
| `analyze-page` | Analyze a URL, screenshot, ad, or existing page |
| `optimize` | Improve an existing page for a chosen business outcome |
| `ab-test` | Analyze a Lexsis page URL, build verified challengers, and create or evaluate a draft A/B test |
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
  → /design-page
  → /generate
  → /publish (separate approval)
```

The fast unpublished-draft routes are:

```text
/build <prompt or optional template URL>
/build-with-template <template URL> <prompt>
```

| Step | Output |
|------|--------|
| `/setup` | Saved store brand reference and theme CSS, indexed by store and theme |
| `/plan-page` | Intent-aware plan with design direction, wireframe, imagery plan, and asset slots |
| `/design-page` | Canonical source, islands, and `DRAFT_CREATED` hosted preview |
| `/build` | `DRAFT_CREATED` with planning and visual approval recorded as skipped |
| `/build-with-template` | `DRAFT_CREATED` from the supplied template direction |
| `/generate` | `DRAFT_CREATED` preview first; `DRAFT_READY` after synchronization and hosted QA |
| `/publish` | Explicit release of the reviewed page version |

When several saved stores or themes are available, every page records the
selected `storeId` and `themeId`; it never silently switches themes. Commands
remain independently invokable, and explicitly skipped steps are recorded in
the page manifest.

`design-page` can first generate a mobile-first visual concept with the
existing Lexsis image tools when the user wants to approve the look. Concept
images remain non-production evidence. It then inventories existing assets,
asks once before generating missing media, authors readable `<lx-island>`
source, compiles it, and creates one unpublished hosted draft. The hosted
renderer is the only interactive preview. `/generate` reuses that draft for
tablet, synchronization, and commerce QA.

The workflow infers `fast-draft` versus `production-ready` from the complete
request and conversation rather than requiring a trigger phrase. Reversible
ambiguity defaults to an early unpublished draft. Publishing, paid generation,
deletion, and destructive changes retain explicit authorization boundaries.
Fast build limits compilation to one initial attempt and one targeted repair;
full QA and synchronization remain an explicit `/generate` upgrade.

## MCP Server

- **Codex and Claude Code:** connect the hosted `lexsis-ai` HTTP server and
  complete browser OAuth when prompted. User API keys and manually configured
  `Authorization` headers are not supported.

## External MCPs (Optional)

`design-page` or standalone `asset-prep` can use these when installed — none required:

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
│   ├── design-page/                 ← source composition + hosted draft workflow
│   └── storefront-engine/           ← shared resources, not a public command
│       └── references/              ← workflow guidance + island schemas
├── .claude-plugin/                  ← marketplace + Claude plugin manifests
├── agents/                          ← Claude page-builder and CRO agents
├── .mcp.json                        ← Claude plugin MCP configuration
├── .agents/skills → skills/         ← Codex + Cursor native discovery (symlink)
├── codex/                           ← Codex plugin manifest + MCP config
├── gpt/                             ← GENERATED — custom GPT instructions + knowledge
├── cursor/                          ← pointer README (Cursor needs no copies)
└── scripts/build-distributions.py   ← regenerates Claude/GPT outputs and validates everything
```

One source of truth: edit `skills/`, run `python3 scripts/build-distributions.py`,
commit. The repository root is also the Claude plugin package, preventing
duplicate skill paths during `npx skills update`. CI fails on drift.

The Claude and Codex plugins plus the GPT distribution package the shared
`storefront-engine/references/` corpus. Public skill entrypoints remain
self-contained: the build copies each consumed shared reference into that
skill's own `references/` directory. Clients that install individual skills
therefore do not depend on a missing sibling `storefront-engine` directory.

> **Windows note:** `.agents/skills` is a convenience symlink for local agent
> discovery. The published Claude plugin uses real copied files and does not
> depend on symlink support.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). Short version: edit canonical `skills/` only; the build script and CI keep every distribution in sync. Skill frontmatter must pass the [Agent Skills spec](https://agentskills.io/specification) (name = directory name, ≤64 chars; description ≤500 chars).

## License

MIT — [LICENSE](./LICENSE)

---

Built with [Lexsis AI](https://trylexsis.com)

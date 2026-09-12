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

Or zero-install: clone the repo anywhere inside your project — Codex discovers `.agents/skills/` automatically. Invoke with `$skill-name` (`$design-page`, `$cart`) or let Codex select from your request. Complete the `lexsis-ai` OAuth prompt when Codex requests MCP access.

## Install (Cursor)

Nothing to copy. Cursor reads the Agent Skills standard from `.agents/skills/` natively — clone the repo (or use `npx skills add`) and the skills appear. The old `cursor/rules/*.mdc` file is gone as of v5.0.0.

## Install (Custom GPT)

1. Copy `gpt/instructions.md` → paste into GPT Instructions
2. Upload `gpt/knowledge.md` as a Knowledge file

Both files are **generated** from the canonical skills by `scripts/build-distributions.py` — never edit them by hand.

## What's Included

- **7 focused storefront commands** — four reviewed-workflow commands and three optional operations
- **2 agents** (cro-analyzer, page-builder) for Claude Code
- Shared CRO, vertical, traffic-source, workflow, and island references under `skills/storefront-engine/references/`, including the house `design-rules.md` and `island-presets.md`
- **Page-type contracts** (`references/page-types/`): 30 ecommerce page types
  (ad landing, PDP, advertorial, listicle, quiz funnel, bundle, offer, sale,
  gifting, launch, subscription, UGC, homepage, collection and more), each with
  mandatory and forbidden sections, an above-the-fold recipe, proof density,
  CTA and price rules, imagery jobs, a step-by-step `## Workflow` (context reads, then per section:
  media, island, copy) and a machine-readable default checklist shared by
  hosted review and repository regression tests
- **Proof, offer, asset, anti-pattern and copy rule corpora**
  (`references/proof/`, `offers/`, `assets/`, `anti-patterns/`, `copy/`):
  review sourcing with a zero-review playbook, press and badge verification,
  UGC rights, compare-at legality by jurisdiction, urgency rules, campaign
  calendar, funnel stages, an ALLOW / ASK / NEVER image-generation policy,
  slot specs, a dark-pattern catalogue with regulator text, a lintable AI-slop
  copy blacklist, copy frameworks and a message-match scorecard
- **Workflows** (`references/workflows/`): the assets-first per-section loop
  (catalog media, library by tag, merchant sources, generation, then tell the
  merchant and offer upload or generation) and how to pick and configure
  islands live through `lexsis_design.islands` and `island_schema`
- **MCP playbooks** (`references/mcp-playbooks/`): the exact `router.action`
  sequence per stage and per page type
- A consumer-behavior CRO framework that turns shopper uncertainty, gallery
  gaps, compatibility, solution completion, trust, and mobile context into
  page-specific hypotheses instead of generic conversion modules
- **50 active islands** plus 8 deprecated compatibility contracts under
  `skills/storefront-engine/references/islands/`
- Vertical expertise: beauty, supplements, fashion, food, luxury, home
- Traffic-source patterns: Meta, Google, TikTok

## Skills

Invoke as `/name` (Claude Code) or `$name` (Codex); most also trigger automatically from a matching request.

| Skill | What it does |
|-------|--------------|
| `setup` | Save reusable brand and theme context for one or more stores |
| `plan-page` | Produce the complete page specification: copy, asset decisions, claim gate, work queue, status; waits for approval |
| `design-page` | Build the approved plan, create one unpublished hosted draft, run hosted QA at 390/768/1280, apply edits, return `DESIGN_APPROVED` |
| `publish` | Release a `DESIGN_APPROVED` draft version only after explicit approval |
| `optimize` | Score an existing page, propose a strict optimization plan, apply approved changes |
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
  → /publish (separate approval)
```

| Step | Output |
|------|--------|
| `/setup` | Saved store brand reference and theme CSS, indexed by store and theme |
| `/plan-page` | Complete page specification (`PLAN_READY_FOR_DESIGN`, `PLAN_COMPLETE - asset tasks pending` or `BLOCKED - evidence required`); `PLAN_APPROVED` after explicit approval |
| `/design-page` | Canonical source, islands and `DRAFT_CREATED` hosted preview; `DESIGN_APPROVED` after hosted QA at 390/768/1280 |
| `/publish` | Explicit release of the `DESIGN_APPROVED` page version |

When several saved stores or themes are available, every page records the
selected `storeId` and `themeId`; it never silently switches themes. Commands
remain independently invokable, and explicitly skipped steps are recorded in
the task handoff.

`plan-page` returns the whole specification of the page: final section copy,
an asset decision for every section, a claim gate, a work queue with owners and
a plan status. It spends no credits and always waits for explicit approval.
`design-page` runs a Plan Gate on that status, can first generate a
mobile-first visual concept when the user wants to approve the look (concept
images remain non-production evidence), resolves each asset slot by its
decision, places the plan's copy, authors readable `<lx-island>` source,
compiles it, and creates one unpublished hosted draft. Source and optional
theme CSS go directly to MCP; there are no per-page source files, compile
artifacts, local preview builds or local QA steps. The hosted renderer is the
only interactive preview. `design-page` then runs hosted QA at 390, 768 and
1280 with commerce checks, applies later edits with `expected_version`, and
returns `DESIGN_APPROVED`.

The workflow infers only question depth and publish-versus-draft intent from
the request; plan approval before design and publishing approval are never
inferred. Publishing, paid generation, deletion, and destructive changes retain
explicit authorization boundaries.

## MCP Server

- **Codex and Claude Code:** connect the hosted `lexsis-ai` HTTP server and
  complete browser OAuth when prompted. User API keys and manually configured
  `Authorization` headers are not supported.

## External MCPs (Optional)

`design-page` can use these when installed — none required:

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

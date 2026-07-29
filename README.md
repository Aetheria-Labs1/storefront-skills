# Lexsis AI — Storefront Skills

> Native AI workflows for building high-converting Shopify storefronts with Claude Code and OpenAI Codex.

## Install (Claude Code)

```bash
# 1. Register marketplace (one-time)
/plugin marketplace add lexsis https://github.com/Aetheria-Labs1/storefront-skills

# 2. Install (includes all verticals, workflows, and MCP config)
/plugin install lexsis-storefront-skills@lexsis
```

Done. Skills auto-load, MCP auto-configures, commands available immediately.

## Install (OpenAI Codex)

Run these commands in your terminal:

```bash
# 1. Register the Lexsis marketplace (one-time)
codex plugin marketplace add Aetheria-Labs1/storefront-skills --ref main

# 2. Install the storefront plugin
codex plugin add lexsis-storefront-skills@lexsis-storefront
```

Start a new Codex task after installation. Complete the `lexsis-ai` OAuth prompt when Codex requests access to the bundled MCP server.

Codex selects skills automatically from your request. You can also invoke any workflow directly with `$skill-name`, for example `$generate`, `$browser-analyze`, or `$cart`. Plugin-defined slash commands such as `/generate` are Claude-only.

Verify or update the installation:

```bash
# Show installed plugin and version
codex plugin list

# Fetch marketplace updates, then reinstall the latest plugin version
codex plugin marketplace upgrade lexsis-storefront
codex plugin add lexsis-storefront-skills@lexsis-storefront
```

Codex Browser is optional. URL analysis and draft QA use it when available; otherwise skills fall back to Lexsis server-side design extraction.

## Install (Other Platforms)

<details>
<summary><strong>Cursor</strong></summary>

```bash
git clone https://github.com/Aetheria-Labs1/storefront-skills.git
mkdir -p .cursor/rules
cp -r storefront-skills/cursor/rules/* .cursor/rules/
```
</details>

<details>
<summary><strong>Custom GPT</strong></summary>

1. Copy `gpt/instructions.md` → paste into GPT Instructions
2. Upload `gpt/knowledge.md` as Knowledge file
</details>

## What's Included

One plugin — everything included:
- 10 Claude commands + 12 Codex skills + 2 agents
- 49 reference docs (CRO patterns, verticals, workflows)
- 47 island schemas
- Vertical expertise built-in: beauty, supplements, fashion, food, luxury, home
- Traffic source patterns: Meta, Google, TikTok

## Codex Skills

Codex supports skills rather than plugin-defined slash commands. Use natural language for automatic skill selection, or select one directly with `$skill-name`.

| Skill | What It Does |
|-------|--------------|
| `$storefront-engine` | Route broad, multi-step storefront requests to the right workflow |
| `$browser-analyze` | Audit a storefront URL using Codex Browser when available |
| `$analyze-page` | Turn page evidence into a reproducible design and CRO brief |
| `$cart` | Configure Cart V2 composition, upsells, and behavior |
| `$experiment` | Set up A/B tests and personalization variants |
| `$extract-island` | Convert a page component into a reusable island layout |
| `$generate` | Generate a Shopify page with planning, validation, and draft-first publishing |
| `$optimize` | Improve an existing page for conversion |
| `$plan-page` | Create a page blueprint before generation |
| `$publish` | Validate, preview, and publish with explicit live approval |
| `$remix` | Adapt competitor or ad patterns to a brand |
| `$search-docs` | Search Lexsis workflows, island schemas, and reference material |

Page-type and specialist workflows such as `generate-pdp.md`, `generate-homepage.md`, `ab-test-variant.md`, and `cart-v2-management.md` remain shared references used by these skills. They are not duplicated as standalone Codex skills.

## Workflow Sequence

The 5-step pipeline — each command feeds into the next:

```
/plan-page → /asset-prep → /generate → /audit-cro → /optimize
```

| Step | What it does | Output |
|------|-------------|--------|
| `/plan-page` | Discover requirements, design section layout | Approved page plan |
| `/asset-prep` | Source images/video (library + AI + external MCPs) | Asset manifest |
| `/generate` | Generate HTML + wire islands + publish draft | Preview URL |
| `/audit-cro` | 12-point CRO scoring via Playwright | CRO blueprint |
| `/optimize` | Apply CRO fixes section-by-section | Updated page |

Each step is independent — start anywhere. `/plan-page` → `/generate` skips asset-prep if the brand library has everything. `/audit-cro` works on any existing page without prior steps.

## Claude Code Commands (after installing core)

### Core Pipeline

| Command | What It Does |
|---------|-------------|
| `/plan-page` | Plan a page — gather requirements, design section layout, get approval |
| `/asset-prep` | Source assets — library search + AI generation + external MCPs (video, research) |
| `/generate` | Generate a Shopify page — auto-detects type (PDP, landing, collection, homepage, editorial, listicle, bundle) |
| `/optimize` | CRO-optimize an existing page — fix CTAs, trust signals, mobile UX |

### Specialist

| Command | What It Does |
|---------|-------------|
| `/remix` | Rebuild a competitor page or ad creative adapted to your brand |
| `/experiment` | Set up A/B tests, personalization variants, monitor results |
| `/cart` | Configure Cart V2 drawer — upsells, progress bars, conditional rules |
| `/publish` | QA check and publish a page to Shopify |
| `/analyze-page` | Screenshot a URL and extract design tokens + CRO patterns |
| `/search-docs` | Search documentation — islands, skills, conversion patterns, workflows |

## MCP Server

Core plugin auto-configures the Lexsis AI MCP server.

- **Codex:** complete OAuth when prompted. No manual MCP configuration is required.
- **Claude Code:** get an API key at [app.trylexsis.com/settings/api-key](https://app.trylexsis.com/settings/api-key), then add it to the `lexsis-ai` MCP server's `Authorization` header in Claude Code settings.

## Visual Verification

Skills instruct Claude to screenshot pages after generation. Install [Playwright MCP](https://playwright.dev/docs/getting-started-mcp) for automatic visual QA:

```bash
/plugin install playwright@claude-plugins-official
```

Codex workflows use Codex Browser when enabled. Browser is optional; URL analysis falls back to Lexsis server-side extraction when it is unavailable.

## How It Works

```
Skills (this repo)              → teaches AI how to build pages
MCP Server (mcp.trylexsis.com) → provides tools (generate, publish, analyze, assets)
Playwright (optional)          → visual verification via screenshots
External MCPs (optional)       → video generation, image research, stock photography
```

## External MCPs (Optional)

The `/asset-prep` workflow detects and uses these MCPs when installed:

| MCP | What it adds | Install |
|-----|-------------|---------|
| **Playwright** | Visual QA, page screenshots, CRO audit | `/plugin install playwright@claude-plugins-official` |
| **Exa** | Image research, mood boards, competitor screenshots | Exa MCP plugin |
| **HiggsField** | AI video generation for hero sections | HiggsField MCP |
| **OpenArt** | Specialized AI illustration beyond built-in styles | OpenArt MCP |

None are required. The core workflow (plan → generate → publish) works with just the Lexsis AI MCP. External MCPs add richer asset sourcing for `/asset-prep`.

## Repo Structure

```
storefront-skills/
├── plugins/                         ← Claude Code marketplace plugins
│   ├── lexsis-storefront-skills/    ← Core (required)
│   ├── lexsis-beauty-skills/        ← Vertical add-ons
│   ├── lexsis-supplements-skills/
│   ├── lexsis-fashion-skills/
│   ├── lexsis-food-skills/
│   ├── lexsis-home-skills/
│   └── lexsis-luxury-skills/
├── codex/                           ← OpenAI Codex format
├── cursor/                          ← Cursor rules
└── gpt/                             ← Custom GPT knowledge
```

## Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for:
- How to add a new vertical plugin
- How to add a core skill or command
- Skill file structure and conventions
- PR process and local testing

## License

MIT — [LICENSE](./LICENSE)

---

Built with [Lexsis AI](https://trylexsis.com)

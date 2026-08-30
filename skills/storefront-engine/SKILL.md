---
name: storefront-engine
description: Route a storefront request to the one Lexsis workflow that owns it. Use for broad or ambiguous requests spanning visual page creation, reference analysis, assets, generation, optimization, experiments, cart configuration, or publishing.
---

# Storefront Engine

This is the router. It does not build pages, generate assets, edit pages, or
publish. Select one owning skill and pass it only the context it needs.

Read `references/workflow-handoffs.md` for optional workflow connections.

Reference files use compact `router.action(...)` notation. Execute that as the
named consolidated MCP router with `{"action": "action", "args": {...}}`.
Never call a former one-tool-per-operation name directly.

## Routing

| User intent | Owning skill |
|---|---|
| New page from a brief, product, ad, screenshot, URL, or mixed input | `visual-page` |
| Text-only section and conversion plan, without visual concept generation | `plan-page` |
| Analyze a reference URL into a safe structural brief | `analyze-page` |
| Capture a URL with Browser before analysis | `browser-analyze` |
| Prepare final page assets | `asset-prep` |
| Build an approved plan and asset manifest into a draft | `generate` |
| Improve an existing page using performance evidence | `optimize` |
| Create or monitor a controlled experiment | `experiment` |
| Configure cart profiles | `cart` |
| QA a ready draft and release it live | `publish` |
| Search a schema, workflow, or troubleshooting answer | `search-docs` |
| Extract a reusable island layout for maintainers | `extract-island` |

## Routing Rules

1. Use `visual-page` for every new page request unless the user explicitly
   asks for planning only.
2. Send a reference URL through `browser-analyze` or `analyze-page` before
   `visual-page`; do not make `visual-page` rediscover the same evidence.
3. Do not call `generate` until the plan is approved and `asset-prep` returns
   the final asset manifest.
4. Do not call `publish` until a draft has passed visual QA and the user
   explicitly asks to go live.
5. Do not use `remix` to build a page. It produces a brand-safe reference
   brief for `visual-page`.

## Completion

This router is complete after selecting a workflow. The selected skill can run
independently; do not require a chain merely because a related workflow exists.

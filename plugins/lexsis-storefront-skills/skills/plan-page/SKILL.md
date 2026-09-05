---
name: plan-page
description: Turn campaign and product requirements into an approved storefront page plan. Use before visual design; this skill does not generate mockups, assets, or page source.
---

# Plan a Page

Create the strategy and section blueprint for one storefront page.

Read:

- `references/page-files.md`

Before creating or changing the page workspace, confirm `lexsis_discover` is
available and discover the exact catalogue and template actions required by
this run. Configuration alone is not proof of connection. If discovery fails,
return `BLOCKED_LEXSIS_MCP` without changing page artifacts.

When the full Lexsis skill pack is installed, the optional detailed contracts
are under `storefront-engine/references/lexsis-mcp-contract.md` and
`storefront-engine/references/lexsis-design-capabilities.md`.

Read `work/storefront/setup/setup.json`, select one saved store/theme pair, and
read its brand design and theme CSS. Prefer an explicit selection, then an
existing page binding, then an unambiguous default. If the selection is not
saved, stop with `Run /setup for this store and theme first.`

## Ask Only What Is Missing

Collect:

1. Page or campaign type.
2. Product or collection.
3. Audience and customer problem.
4. Traffic source.
5. Primary conversion goal and CTA.
6. Required proof, claims, offers, or sections.

Ask no more than four questions at once. Read current products, variants,
prices, and availability from `lexsis_catalog`; do not rely on setup for them.
If a URL, screenshot, or ad is important, use the compact output from
`/analyze-page`.

## Select a Template Direction

Discover the current template actions, then search page kits using the page
type, archetype, objective, industry, and mood. A kit is a coherent list of
section-template IDs, not a page-instantiation action.

If no suitable kit exists, search individual sections. In a host with an
interactive template picker, wait for the user's selection. Record evaluated
results, the selected kit/sections, or the reason for a custom composition.

## Produce `page-plan.md`

Include:

- objective, buyer, traffic source, and primary CTA
- selected workspace, store, theme, product, and collection
- ordered section map with copy intent
- visual rhythm and desktop/mobile behavior
- asset roles
- required islands
- claims requiring evidence
- selected template direction and adaptation intent

Start `page-manifest.json` using `references/page-files.md`, including the MCP,
template, and design records. Create the page working directory and `assets/`,
but do not write visual or production HTML.

## Approval

Present a compact summary:

```text
Page: [type]
Goal: [conversion goal]
Audience: [buyer]
Sections: [ordered list]
Islands: [list]
Assets needed: [list]
Claims to verify: [list]
```

Wait for approval and update the plan when requested.

## Return

Return `working_directory`, `page_plan_path`, `page_manifest_path`, and
`PLAN_APPROVED`, plus the required MCP and template evidence. The next normal
command is `/visual-page`, but this skill is complete after the plan is
approved.

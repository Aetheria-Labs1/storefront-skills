---
name: visual-page
description: Turn a storefront brief, product, ad, screenshot, reference URL, or mixed input into an approved visual layout brief and a draft Shopify page. Use when a user wants a new page designed visually before it is built.
---

# Visual Page Builder

Use this workflow for new page generation when the user wants a visual layout
before source HTML is written. It orchestrates `plan-page`, `asset-prep`, and
`generate`; do not duplicate their detailed rules.

Read `storefront-engine/references/visual-layout-workflow.md` before starting.

## Inputs

Accept any combination of:

- a plain-language brief, target audience, traffic source, or conversion goal
- a product or collection
- a brand direction or existing design assets
- an ad creative, screenshot, or reference URL

Route inputs before creating a layout:

| Input | First action |
|---|---|
| Reference URL or screenshot | Load `browser-analyze` or `analyze-page` |
| Ad creative | `analyze_ad_creative`, then `match_persona_to_ad` |
| Product or collection | `lexsis_catalog` action `list` and use real Shopify imagery |
| Brief only | Run the embedded `plan-page` assessment |
| Existing page edit | Use the edit flow, not this skill |

Never reuse competitor copy, logos, product images, or brand marks. Reference
inputs are for composition, hierarchy, and interaction patterns only.

## Phase 1: Draft Plan and Layout

1. Gather the minimum missing requirements with the `plan-page` assessment.
2. Gather brand context through `lexsis_brand`, `lexsis_design`,
   `lexsis_catalog`, and `lexsis_asset_library`.
3. Create an internal `PLAN_DRAFT`: section order, conversion goal, visual
   rhythm, asset needs, and required islands.
4. Call `lexsis_workspace` action `credits` and `lexsis_assets` action
   `capabilities`.
5. Generate a layout reference with `lexsis_drafts` action `asset_generate`.
6. Call `lexsis_assets` action `view` to inspect it. Translate the concept into a layout brief:
   desktop composition, mobile stacking, section proportions, CTA positions,
   image placement, and island mapping.
7. Present the layout concept and the plan together. Wait for approval before
   producing final assets or page source.

Use only `lexsis_drafts` action `asset_generate` for layout-reference creation.
Do not assume a provider or model. Call `lexsis_assets` action `capabilities` when
the brief requires a specific quality, cost, reference-image, size, or output
format decision.

The concept prompt must say it is a storefront composition study, not a final
page. Use generic placeholder copy where text treatment matters. The concept
is not a production page image and must not be embedded in the final page.

## Approval Format

Present one decision point:

```text
Visual Page Plan: [page type]

Goal: [conversion goal]
Layout: [concept asset URL]
Sections: [ordered section list]
Visual rhythm: [composition, palette, spacing]
Commerce: [islands]
Production assets needed: [list]

Proceed to prepare final assets and create a draft preview?
```

## Phase 2: Build the Draft

After approval:

1. Hand the approved plan and layout brief to `asset-prep`.
2. Hand the final asset manifest, plan, and layout brief to `generate`.
3. `generate` compiles source-format HTML and creates a draft preview only.
4. Inspect desktop and mobile screenshots against the approved layout.
5. Fix material composition, overflow, asset, or island failures before
   returning the preview.

Never call `lexsis_live_ops` action `publish` unless the user separately
approves a live publish.

## Optional Follow-Up

After approval, this workflow may use `asset-prep` and `generate` to create a
draft. It may also end after returning the approved plan and layout brief when
the user wants to continue later.

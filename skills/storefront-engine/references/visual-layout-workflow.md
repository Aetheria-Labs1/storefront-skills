# Visual Layout Workflow

Use this reference with the `visual-page` skill. It converts mixed page inputs
into a visual concept, an approved page plan, and a valid source-format draft.

## Layout Concept Contract

The concept is an internal visual brief. It communicates:

- section order and relative heights
- hero composition and focal point
- grid, split, and card proportions
- image placement and treatment
- color temperature and whitespace rhythm
- CTA hierarchy and likely island placement
- desktop composition and mobile stacking intent

It does not provide final copy, production imagery, product facts, or valid
island props. Use brand data, Shopify product data, and the island schemas for
those.

## Generate the Layout Reference

Call `lexsis_drafts` action `asset_generate` to create the visual reference. The workflow is
provider-neutral: do not hardcode a provider or model here.

Call `lexsis_assets.capabilities` only when the request needs a deliberate
quality, cost, reference-image, size, output-format, or transparency choice.
Record the returned asset ID in the working brief, but do not use the layout
reference as final page media.

## Prompt Template

```text
Create a desktop ecommerce [PAGE TYPE] composition study for [AUDIENCE].

Goal: [CONVERSION GOAL].
Brand direction: [BRAND TONE, PALETTE, TYPOGRAPHY].
Section order: [SECTION PLAN].
Use [PRODUCT / EXISTING ASSET] only as visual reference.
Show clear hierarchy, whitespace, CTA placement, image zones, card/grid
proportions, and mobile-friendly stacking intent.
This is a layout concept, not a final website. Use generic placeholder copy;
do not reproduce competitor branding, logos, copy, or imagery.
```

Use `16:9`, `2K`, and PNG by default. Use reference images only when they are
tenant-owned assets, user-supplied assets, or safe visual references.

## Concept to Source Mapping

After `lexsis_assets.view`, write a concise layout brief before running `asset-prep`:

| Concept signal | Source-format implementation |
|---|---|
| Full-bleed hero | Semantic `<section>` with responsive image and overlay |
| Split hero | Grid that stacks below `lg` |
| Product purchase area | `BuyBox` with real product data |
| Repeated cards | CSS grid with stable media aspect ratios |
| Reviews / FAQs / tabs | Valid matching island with schema-derived props |
| Pinned conversion action | `StickyBar` only when the page type and product support it |

Do not copy pixels literally. Preserve visual intent while obeying the brand
kit, accessibility rules, content hierarchy, source format, and island
contracts.

## Approval and QA

Show the concept and plan in one approval response. After approval, compare the
draft preview at desktop and 375px mobile widths:

- hero headline and CTA are visible above the fold
- layouts stack without horizontal overflow
- real product data and final assets replaced placeholders
- no concept image is embedded in the page
- islands hydrate and page compilation has zero errors
- composition still matches the approved visual rhythm

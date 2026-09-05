---
name: plan-page
description: Turn campaign and product requirements into a concise one-page storefront plan with a design direction, wireframe, imagery plan and resolved asset slots. Use before page design; this skill does not choose islands or implementation details.
---

# Plan a Page

Produce a concise strategy, design direction and section blueprint that can be
reviewed quickly. The plan owns every visual decision that `/design-page` will
execute: hierarchy, wireframe, palette, type, the one bold moment, the imagery
and background plan, and every asset slot on the page.

Read:

- `references/page-files.md`
- `storefront-engine/references/design-rules.md`
- `storefront-engine/references/island-presets.md`

Use `lexsis_catalog.list`, `lexsis_catalog.get`,
`lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`, `lexsis_asset_library.search`,
`lexsis_assets.view`, `lexsis_asset_upload.import`,
`lexsis_drafts.asset_generate`, and `lexsis_workspace.credits`. Resolve an
unfamiliar schema with exact router/action discovery.

Read `work/storefront/setup/setup.json`, select one saved store/theme pair, and
read its brand design. If the selection is not saved, stop with
`Run /setup for this store and theme first.`

## Ask Only What Is Missing

Collect:

1. Page or campaign type.
2. Product or collection.
3. Audience and customer problem.
4. Traffic source.
5. Primary conversion goal and CTA.
6. Required proof, offer, claim, or section constraints.

Ask no more than four questions at once. Read current products, variants,
prices, and availability from Lexsis.

## Choose a Direction

Search page kits using the page type, objective, industry, and mood. If no kit
fits, inspect the returned status before deciding why:

- A successful catalog response with zero results means that shelf is empty.
  Continue with section search or a custom direction; do not make an unrelated
  control call merely to prove the service works.
- A failed request is a tool error, not an empty shelf. Report it and use only
  an explicitly documented fallback.

Search sections for useful structural references when no page kit fits. Record
only the selected kit or section IDs in the manifest; put the short selection
rationale in the plan.

Template selection at this stage is directional. `/design-page` owns fetching
source, adapting layouts, selecting islands, and resolving schemas.
The plan must not define islands.

A preset id from `storefront-engine/references/island-presets.md` is a
design-intent token, not implementation, and may be named per section as
`Preset: <island>/<intent>-<tone>`. At most one preset per island role; every
preset's tone must match the tone named in the Design direction block or be
listed as an explicit exception. Header and footer presets are chosen in the
Design direction block, not per section.

## Parallel Planning

If the runtime can spawn sub-agents, fan out three read-only lanes and merge
their output; otherwise run the same three blocks sequentially in this order.

1. Hierarchy and wireframe: section order, buy-box position, media share, the
   ASCII wireframe at 1280 and 390 with a slot id on every media box.
2. Imagery, background plan and asset slots: search the asset library and
   catalog media for every slot; propose the treatment per imagery section.
3. Palette, type, motion and icon decisions from the saved brand design and
   theme tokens, with the overrides list.

Each lane returns only its block. The parent merges them into `page-plan.md`,
runs the generic-default check, resolves conflicts by the house rules, and asks
the single asset question below. Lanes never write files or spend credits.

## Write a One-Page Plan

Keep `page-plan.md` concise enough to scan in one view. Include:

- objective, audience, traffic source, product, and primary CTA
- selected template direction
- ordered section list
- one sentence describing each section's purpose
- the Design direction, Imagery and background plan, and Asset slots blocks
  defined below
- offers and claims that require confirmation

### Design direction (required block in page-plan.md)

Write this block before the section list. Read the saved brand design, the
theme tokens and `storefront-engine/references/design-rules.md` first. Fill
every field; "none" is an answer, "TBD" is not. Then run the generic-default
check at the end and revise anything it catches.

Template to copy into `page-plan.md`:

````markdown
## Design direction

**Palette (4 to 6, named, with roles)**
| Role | Name | Hex | Used for |
|---|---|---|---|
| page | | | the only section background |
| ink | | | text, primary button |
| muted | | | captions, compare-at, metadata |
| rule | | | 1px hairlines, input borders |
| accent | | | price, links, focus ring; one accent per screen |
| bar (optional) | | | announcement bar only |

**Type roles and scale.** Heading family and weight; body family and weights; script family via `[lang]` if any. One ratio (1.2 to 1.333) from 16px, listed as steps. Body line-height; heading line-height. Measure 60 to 70ch.

**Layout concept.** One sentence. Then the alignment rule (left-aligned throughout unless stated).

**Wireframe.** ASCII at 1280 and at 390, one box per section, showing media share, buy-box position and the bold moment. Every box that shows media carries its asset slot id in brackets, so the wireframe enumerates every asset slot on the page.

1280                                   390
+------------------+----------------+  +------------------+
| gallery 55% [A1] | title          |  | gallery [A1]     |
|                  | price  variants|  | title / price    |
|                  | add to cart    |  | variants / cart  |
+------------------+----------------+  +------------------+
| trust line (hairline above/below)  |  | trust line       |
+-----------------------------------+  +------------------+
| lifestyle photo [A2] | copy       |  | lifestyle [A2]   |
+-----------------------------------+  +------------------+

**Icons.** `none` or `one inline SVG set: <name>, <stroke>px, <size>px, currentColor`. Never emoji.

**Background rule.** One page background `<hex>` from navbar to footer. Full-bleed exception: `none` or `<section id>` (this must be the bold moment).

**The one bold moment.** Which element, why it is the memorable thing for this brand and product, and what stays quiet because of it.

**Motion.** `none` or `one moment: <what, when, duration>`. Everything else is static; hover states change colour or underline only.

**Generic-default check.** Write two lines: "A generic <page type> for <vertical> would have: ..." then "This plan differs by: ..." with at least three concrete, visible differences (layout, type, moment, media treatment). If you cannot name three, the plan is the default; change it.

**Overrides of brand design.md.** List each design.md or brand-kit line you are ignoring, with the house rule id (N1 to N14, A1 to A12). Example: "design.md 'Always include emoji icons in ticker bar' → N1. 'Trust strip in --lx-secondary-color' → N2."
````

### Imagery and background plan

The page has one background from navbar to footer. Visual richness comes from
imagery, the way every strong commerce page is built: a full-bleed hero photo
or banner, inset product media, lifestyle photography, proof artefacts,
editorial image grids. Never from tinted section bands.

Write one line per imagery section:

```text
<section> → <slot ids> → <treatment: full-bleed | inset | grid | background image with legibility overlay>
```

Every imagery section maps to at least one slot. The single full-bleed
exception is the bold moment named above. Sections without imagery are
separated by spacing and a hairline, not colour.

### Asset slots

List every slot the wireframe names, for any page type:

```markdown
| Slot | Section | Role/purpose | Aspect | Source decision | Id / URL | Status |
|---|---|---|---|---|---|---|
| A1 | gallery | product_media | 4:5 | shopify media | gid://…/ProductImage/… | verified |
| A2 | proof | product_lifestyle | 3:2 | generate | | planned |
```

`Role/purpose` uses the generation purposes where they apply (`hero_bg`,
`product_lifestyle`, `section_bg`, `product_composite`, `texture_fill`,
`decorative_element`) plus `product_media`, `logo`, and `proof`. `Status` is
`verified` or `planned`. Interface icons are never slots.

Resolve every slot before approval:

1. For each slot, search `lexsis_asset_library.search` (semantic, then tags)
   and the product's Shopify media through `lexsis_catalog.get`.
2. Present the table with the best candidate per slot, then ask once:
   - **You pick.** Use the asset picker if one appeared in this host; otherwise
     name asset ids or filenames from the web asset library (Storefront →
     Design library → Assets) and the skill searches by filename.
   - **I pick.** Use the best library or catalog match for every slot.
   - **Generate the gaps.** Check `lexsis_workspace.credits`, then
     `lexsis_drafts.asset_generate` per unresolved slot with the slot's
     purpose and aspect, and import externally supplied files with
     `lexsis_asset_upload.import`.
3. Apply the answer to all slots. Verify identity-sensitive picks with
   `lexsis_assets.view`. Record the provider and asset id for generated slots.
4. Write the final table into the plan and one `assets[]` entry per slot into
   the manifest. A slot the user postpones stays `planned`; `/design-page`
   confirms only those.

Verify facts that control the page's urgency or trust before treating them as
copy. This includes occasion dates, delivery cutoffs, prices, availability,
medical or performance claims, certifications, endorsements, and legal or
safety language. Use an authoritative current source where one exists. Mark an
unverified item as unresolved in the plan instead of guessing it.

Do not include:

- island names or schemas
- island props or hydration modes
- HTML, CSS, Tailwind classes, or implementation notes
- asset search transcripts or rejected candidates
- gradients, hover effects, or motion beyond the Motion line
- template search transcripts
- QA, compilation, synchronization, or publishing state

Create the page directory, `assets/`, and a compact schema-v3
`page-manifest.json` using `references/page-files.md`, including one
`assets[]` entry per slot. Do not create source, preview, compile, or QA files.

## Approval

Present:

```text
Page:
Goal:
Audience:
Template direction:
Design direction:
Bold moment:
Overrides:
Sections:
Asset slots: <n verified / m planned>
Planned slots (unresolved):
Claims to confirm:
```

Wait for approval.

## Return

Return the working directory, plan path, manifest path, the asset slot
summary, and `PLAN_APPROVED`. The next normal command is `/design-page`.

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
`lexsis_template_library.search_sections`, `lexsis_template_library.get_kit`,
`lexsis_asset_library.search`, `lexsis_assets.view`,
`lexsis_asset_upload.import`, `lexsis_drafts.asset_generate`,
`lexsis_workspace.credits`, `lexsis_catalog.reviews_status`,
`lexsis_catalog.review_collections`, `lexsis_catalog.reviews`, and
`lexsis_catalog.reviews_search`. Resolve an unfamiliar schema with exact
router/action discovery.

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

When the first answers arrive, ask a second round of three questions together.
The user picks first; the skill searches only where the user declines:

7. Templates: pick a page kit or sections yourself, or should I search and
   propose?
8. Assets: pick from your library (banners, lifestyle photos, proof, logo), or
   should I search and propose?
9. Reviews: which review collection should the page use (list the active ones
   with their counts), product reviews, or none?

## Choose a Direction

Ask first, search second. The catalog is small (about 30 page kits, about 200
section templates, only a few kits per page type); a person scans it faster
than a query ranks it.

**User picks (question 7).** Call `lexsis_template_library.search_page_kits`
with `query: ""`, the `page_type`, `industry` and `mood` filters, and
`limit: 20`. When the host shows the Template Gallery, wait for the
`Design template selection:` message and record its `kind` and `slug` or `id`.
If no kit fits, browse `search_sections` with `query: ""` for the section that
matters most. Without a picker, give the public gallery
`https://storefront.trylexsis.com/templates?view=kits&page_type=<type>&industry=<vertical>&mood=<mood>`
and accept a pasted kit URL, template URL, slug, or id. Resolve kit slugs and
URLs with `lexsis_template_library.get_kit`; pass template URLs on unchanged,
`/design-page` resolves them.

**Skill searches (user declined).** Search page kits using the page type,
objective, industry, and mood. If no kit fits, inspect the returned status
before deciding why:

- A successful catalog response with zero results means that shelf is empty.
  Continue with section search or a custom direction; do not make an unrelated
  control call merely to prove the service works.
- A failed request is a tool error, not an empty shelf. Report it and use only
  an explicitly documented fallback.

Search sections for useful structural references when no page kit fits.
Present at most three candidates, one line each, and ask the user to confirm
one or decline all.

Record only the selected kit or section IDs in the manifest (`template.mode`
is `page-kit`, `sections`, or `custom`); put the short selection rationale in
the plan. Custom composition names the evaluated ids and why none fit.

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
2. Imagery, background plan, asset slots and proof sources: search the asset
   library and catalog media only for slots the user did not pick; read
   `lexsis_catalog.reviews_status` and `lexsis_catalog.review_collections`;
   propose the treatment per imagery section.
3. Palette, type, motion and icon decisions from the saved brand design and
   theme tokens, with the overrides list.

Each lane returns only its block. The parent merges them into `page-plan.md`,
runs the generic-default check, resolves conflicts by the house rules, and asks
the second-round questions. Lanes never write files or spend credits.

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

**Icons.** `none` or `one inline SVG set: <name>, <stroke>px, <size>px, currentColor`. Never emoji as icons; if no set fits, generate a monochrome SVG icon set.

**Emoji in copy.** `none` (default) or `allowed: "<the user's exact request>"`. Only when the user explicitly insists, only inside running text, never as an icon or separator.

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
`decorative_element`) plus `product_media`, `logo`, `proof`, and `icon_set` (only
when the Icons decision says a set must be generated). `Status` is `verified`
or `planned`. Ordinary interface icons come from one inline SVG set and are
not slots; emoji are never an icon fallback.

Resolve every slot before approval. The user picks first (question 8); the
skill searches only for what the user did not pick.

1. **User picks.** Call `lexsis_asset_library.search` once per slot group
   (`query: ""`, `kind: "image"` or `"svg"` for the logo, `mode: "tags"` with
   `banner`, `lifestyle`, `social-proof`, `logo`, `product-shot` or `hero` when
   the group is clear, `theme_id` from `setup.json` (required), `limit: 48`).
   The asset picker multi-selects across pages; wait for the
   `Design asset selection:` message and map its `assets[]` to slot ids in
   `selection_order` (A1, A2, …). Confirm the mapping in one line or take a
   one-line remap. Without a picker: Storefront → Design library → Assets;
   accept filenames or URLs and look them up with `mode: "filename"`. Files
   not yet in the library go through `lexsis_asset_upload.import` with no
   source; the upload panel's message carries the new asset id.
2. **Skill fills the gaps.** For every slot still unresolved, search
   `lexsis_asset_library.search` (semantic, then tags) and the product's
   Shopify media through `lexsis_catalog.get`. Present the table with the best
   candidate per slot, then ask once: **I pick** (use the best match for every
   remaining slot) or **Generate the gaps** (check `lexsis_workspace.credits`,
   then `lexsis_drafts.asset_generate` per slot with its purpose and aspect).
3. Verify identity-sensitive picks with `lexsis_assets.view`. Record the
   provider and asset id for generated slots.
4. Write the final table into the plan and one `assets[]` entry per slot into
   the manifest. A slot the user postpones stays `planned`; `/design-page`
   confirms only those.

### Proof sources

Before planning any reviews or testimonials section, call
`lexsis_catalog.reviews_status` and `lexsis_catalog.review_collections` with
`collection_status: "active"`. Ask question 9 with the active collections and
their `item_count`. Write one line in the plan:

```text
reviews → collection:<id> "<name>" (<n> items)
        | products:<gid, …> (min rating <r>, <n> available via lexsis_catalog.reviews)
        | none → guarantees, certifications, product evidence instead
```

`connected: false` with an empty library means `none`; do not plan the
section. Every count comes from the API and is listed under "Claims to
confirm". The plan never activates a collection. To propose a shortlist, run
`lexsis_catalog.reviews_search` and, only when the user asks,
`lexsis_drafts.review_collection_create` (draft); the merchant activates it in
Storefront → Reviews → Collections. If the host returns `UNKNOWN_ACTION` for
these actions, ask the user to pick a collection there and paste its id.

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
`assets[]` entry per slot and the `reviews` block. Do not create source,
preview, compile, or QA files.

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
Proof sources:
Claims to confirm:
```

Wait for approval.

## Return

Return the working directory, plan path, manifest path, the asset slot
summary, and `PLAN_APPROVED`. The next normal command is `/design-page`.

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
- `references/page-types/_index.md`, then only the matching
  `references/page-types/<type>.md` (its `## Workflow` is the procedure to
  follow)
- `references/workflows/section-asset-workflow.md` (the per-section media
  loop) and `references/workflows/island-selection-workflow.md`
- `references/mcp-playbooks/tool-sequence-by-stage.md` and the matching row of
  `references/mcp-playbooks/tool-sequence-by-page-type.md`
- `references/animation-system.md` when the page may use motion
- `references/consumer-behavior-cro.md`
- `references/design-rules.md`
- `references/island-presets.md`
- `references/workflow-intent.md`
- `references/offers/funnel-stages.md`, `references/offers/offer-ledger.md`,
  and the matching entries of `references/offers/offer-types.md` and
  `references/offers/campaign-calendar.md`
- `references/proof/proof-ledger.md` and `references/proof/reviews-sourcing.md`;
  `references/proof/press-and-media-mentions.md`,
  `references/proof/trust-badges-certifications.md`,
  `references/proof/ugc-rights-and-display.md`,
  `references/proof/before-after-and-claims.md` when the page plans that kind
  of proof
- `references/assets/image-jobs-by-page-type.md`,
  `references/assets/asset-sourcing-sequence.md`,
  `references/assets/generation-policy.md`
- `references/copy/copy-frameworks.md` and `references/copy/message-match.md`

Use `lexsis_catalog.list`, `lexsis_catalog.get`,
`lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`, `lexsis_template_library.get_kit`,
`lexsis_asset_library.search`, `lexsis_assets.view`,
`lexsis_asset_import.import`, `lexsis_asset_upload.upload`,
`lexsis_drafts.asset_generate`,
`lexsis_workspace.credits`, `lexsis_catalog.reviews_status`,
`lexsis_catalog.review_collections`, `lexsis_catalog.reviews`,
`lexsis_catalog.reviews_search`, and, for ad-driven or persona-led pages,
`lexsis_campaigns.creatives`, `lexsis_campaigns.analyze`,
`lexsis_campaigns.personas`, `lexsis_campaigns.match_persona`; for quiz and
lead-capture types, `lexsis_capture.funnel_templates` and
`lexsis_capture.funnel_template`. Resolve an unfamiliar schema with exact
router/action discovery.

## Bind the Workspace and Campaign

Reuse the confirmed workspace, store and theme from saved setup or current
MCP context. Resolve an ambiguous selection before proceeding and state the
chosen binding in one line. Never mix stores or themes on one page.

Group this page with its campaign purpose, confirmed dates, offer and
audience. Reuse the existing campaign evidence for variants and edits.
Keep the plan and compact decision record in the task handoff according to
`references/page-files.md`; do not create campaign folders or page files.

## Infer the Planning Mode

Use `references/workflow-intent.md` to infer `fast-draft` or
`production-ready` from the whole request and conversation. Record compact
intent evidence in `workflow`.

For `fast-draft`, fill reasonable campaign, template, asset, and review
specifics from the saved brand, live catalog, and user context. Ask only when a
missing choice would materially change the campaign or spend credits. Do not
require plan approval before handing the reversible first version to
`/design-page` or `/generate`.

For `production-ready`, collect and confirm the choices that affect final
handoff quality.

Choose the next route from intent:

- `concept-first` when the user wants to see or approve a mockup before source;
- `direct-design` for the normal source and hosted-draft review;
- `fast-build` when the user supplies a template direction and asks for the
  fastest first draft.

Record the route in `page plan`. Do not force every user to choose among all
three. Paid visual-concept generation is confirmed in `/design-page`;
`fast-build` hands off to `/build` or `/build-with-template`.

If a packaged design or preset reference is unavailable, warn once and
continue from the saved brand, theme, and live catalog. A missing optional
reference must not prevent a reversible plan.

## Identify the Page Type

Do this before any template, asset, or proof call. Walk the decision tree in
`references/page-types/_index.md` from the brief: traffic source, funnel stage,
awareness level, offer shape, product count, campaign trigger, desired action.
Choose exactly one `pageType`. When two fit, the index names the tie-break;
when the brief is silent, choose the type that assumes less of the visitor and
say so. Then load only `references/page-types/<type>.md`.

Write this block at the top of `page plan` and mirror it in the page record
(`page.pageType`, `page.funnelStage`, `page.awareness`, `page.trafficSource`,
`offer`, `campaign`):

```markdown
## Page type

**Type.** <file name without .md>
**Funnel stage.** tof | mof | bof | retention
**Awareness.** unaware | problem-aware | solution-aware | product-aware | most-aware
**Traffic.** <source>
**Offer.** <offer-types id> or none
**Campaign.** <campaign-calendar id> or evergreen
**Copy framework.** <copy-frameworks id>
**Mandatory sections omitted.** none | `<id>`: <reason>
**Deviations from the type default.** none | <field>: <value>, <reason>
```

Then follow the type file's `## Workflow` in order:

1. **Context reads.** Run its numbered tool calls first and note what they
   return: how many catalog images exist and which image jobs they cover,
   the variant axes and whether colour variants have their own images, price
   and compare-at, selling plans, inventory, the review count band, theme
   tokens and voice, what the asset library holds under each tag, and the ad
   creative when traffic is paid. Every later decision cites one of these.
2. **Section by section.** For each section in the type's Anatomy order,
   decide three things and write them into the plan: the media (which image
   job, where it comes from, or generate when the policy allows; when nothing
   fits, tell the merchant exactly what is missing and offer upload or MCP
   generation, and skip the section only if they choose:
   `references/workflows/section-asset-workflow.md`), the interactive
   component if any (name the island role and the decision inputs from the
   context reads; the plan never resolves a schema or names props, and
   `/design-page` reads the live catalog and schema for the variant and props:
   `references/workflows/island-selection-workflow.md`; record the inputs and
   a `Preset:` or one-line note), and the copy pattern and ceiling. A section that would end up as
   a colour band, emoji row, icon tiles or a wall of text is rebuilt around
   imagery or put to the merchant.
3. **Asset budget.** Fill the type's asset-budget table for this product:
   what the catalog and library supply, which jobs are missing, and per gap
   whether to reuse, generate (with the purpose), or ask the merchant to
   upload or approve generation. Every missing asset is listed for the
   merchant; in fast-draft, proceed with the shared fallback or a
   `planned` slot and still list it. Assets carry the page; plain colour
   does not.

The `## Checklist` JSON is the default this workflow lands on. When the
context argues for something else (a PDP with two images, a store with no
reviews, a brand whose voice bans a section), deviate and record it under
"Deviations from the type default". Review the checklist before presenting
the plan; explain every deviation without treating it as an automatic failure.

## Ask Only What Is Missing

Collect:

1. Page type, only when the brief leaves the identified type ambiguous.
2. Product or collection.
3. Audience and customer problem.
4. Traffic source.
5. Primary conversion goal and CTA.
6. Required proof, offer, claim, or section constraints.

Ask no more than three questions at once. Read current products, variants,
prices, availability, media, and reviews from Lexsis. Questions are
conditional, not a fixed stage gate. Use
`references/consumer-behavior-cro.md` to inspect likely shopper uncertainty
before asking. Do not ask about custom imagery until the existing gallery has
been mapped to its relevant decision jobs and a specific gap is visible.

In `production-ready` mode, or when the user clearly wants to choose the
creative direction, offer these together. In `fast-draft`, choose them unless
the user already expressed a preference:

7. Templates: user-selected kit/sections or skill-selected direction.
8. Assets: user-selected library assets or skill-selected existing assets.
9. Reviews: which review collection should the page use (list the active ones
   with their counts), product reviews, or none?

## Choose a Direction

For `production-ready`, ask first and search second. The catalog is small
(about 30 page kits, about 200 section templates, only a few kits per page
type); a person scans it faster than a query ranks it. For `fast-draft`, search
and choose a coherent direction unless the user already selected one.

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

Record only the selected kit or section IDs in the page record (`template.mode`
is `page-kit`, `sections`, or `custom`); put the short selection rationale in
the plan. Custom composition names the evaluated ids and why none fit.

Template selection at this stage is directional. `/design-page` owns fetching
source, adapting layouts, selecting islands, and resolving schemas.
The plan must not define islands.

A preset id from `references/island-presets.md` is a
design-intent token, not implementation, and may be named per section as
`Preset: <island>/<intent>-<tone>`. At most one preset per island role; every
preset's tone must match the tone named in the Design direction block or be
listed as an explicit exception. Header and footer presets are chosen in the
Design direction block, not per section.

## Parallel Planning

If the runtime can spawn sub-agents, fan out three read-only lanes and merge
their output; otherwise run the same three blocks sequentially in this order.

1. Consumer decision model, hierarchy and wireframe: primary visitor mode,
   top decision questions, at most three behavioral patterns, section order,
   buy-box position, media share, and the ASCII wireframe at 1280 and 390 with
   a slot id on every media box.
2. Imagery, background plan, asset slots and proof sources: search the asset
   library and catalog media only for slots the user did not pick; read
   `lexsis_catalog.reviews_status` and `lexsis_catalog.review_collections`;
   propose the treatment per imagery section.
3. Palette, type, motion and icon decisions from the saved brand design and
   theme tokens, with the overrides list.

Each lane returns only its block. The parent merges them into `page plan`,
runs the generic-default check, resolves conflicts by the house rules, and asks
only unresolved questions required by the inferred mode. Lanes never write
files or spend credits.

## Write a One-Page Plan

Keep `page plan` concise enough to scan in one view. Include:

- objective, audience, traffic source, product, and primary CTA
- selected template direction
- ordered section list
- one sentence describing each section's purpose
- the Page type block defined above
- the Consumer decision model block from
  `references/consumer-behavior-cro.md`
- the Design direction, Imagery and background plan, and Asset slots blocks
  defined below
- the Proof ledger and, when an offer exists, the Offer ledger
- the copy framework and headline pattern from
  `references/copy/copy-frameworks.md`, and the message-match line from
  `references/copy/message-match.md` for ad-driven traffic
- offers and claims that require confirmation

### Design direction (required block in page plan)

Write this block before the section list. Read the saved brand design, the
theme tokens and `references/design-rules.md` first. Fill
every field; "none" is an answer, "TBD" is not. Then run the generic-default
check at the end and revise anything it catches.

Template to copy into `page plan`:

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

**Overrides of brand design.md.** List each design.md or brand-kit line you are ignoring, with the house rule id (N1 to N14, A1 to A12). Example: "design.md 'Always include emoji icons in ticker bar' U+2192 N1. 'Trust strip in --lx-secondary-color' U+2192 N2."
````

### Imagery and background plan

The page has one background from navbar to footer. Visual richness comes from
imagery, the way every strong commerce page is built: a full-bleed hero photo
or banner, inset product media, lifestyle photography, proof artefacts,
editorial image grids. Never from tinted section bands.

Write one line per imagery section:

```text
<section> U+2192 <slot ids> U+2192 <treatment: full-bleed | inset | grid | background image with legibility overlay>
```

Every imagery section maps to at least one slot. The single full-bleed
exception is the bold moment named above. Sections without imagery are
separated by spacing and a hairline, not colour.

Before finalizing the imagery plan, map the existing gallery to the relevant
jobs in `references/consumer-behavior-cro.md` and to the page type's
`imagery.required_jobs` in `references/assets/image-jobs-by-page-type.md`:
identity, detail, scale/fit, texture/finish, context, variation,
setup/sequence, and sourced proof. Create slots for every required job the
gallery does not cover and for decision-critical gaps. Resolve each slot with
the ordered sequence in `references/assets/asset-sourcing-sequence.md`
(Shopify media, asset library, merchant-supplied or brand-site capture,
licensed stock where the policy allows, then generation). A slot may be
planned for generation only when its purpose is on the ALLOW list in
`references/assets/generation-policy.md`; NEVER-list jobs (the product
itself, people shown as customers, results, logos, badges, text in images)
stay `planned` until the merchant supplies media. If paid generation would
fill allowed gaps, ask once with the exact jobs, count, aspects, and
placements.

### Asset slots

List every slot the wireframe names, for any page type:

```markdown
| Slot | Section | Role/purpose | Aspect | Source decision | Id / URL | Status |
|---|---|---|---|---|---|---|
| A1 | gallery | product_media | 4:5 | shopify media | gid://.../ProductImage/... | verified |
| A2 | story | context | 3:2 | library | asset 7f2e... | verified |
| A3 | closing-cta | hero_bg | 3:2 | generated (after credit confirmation) | | planned |
| A4 | benefits | in-use | 3:2 | pending: merchant to upload, or approve a `product_composite` scene | | planned |
```

`Role/purpose` uses the image job for real media (`product_media`, `context`,
`in-use`, `logo`, `proof`, ...) and the generation purpose for generated
media: ALLOW purposes `hero_bg`, `section_bg`, `card_bg`, `texture_fill`,
`pattern_tile`, `decorative_element`, `product_composite`; `product_lifestyle`
only as an ASK slot with the merchant's yes recorded; `icon_set` when the
Icons decision says a monochrome inline SVG set must be authored
(`references/assets/generation-policy.md`). `Status` is `verified`
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
   `selection_order` (A1, A2, ...). Confirm the mapping in one line or take a
   one-line remap. Without a picker: Storefront U+2192 Design library U+2192 Assets;
   accept filenames or URLs and look them up with `mode: "filename"`. Files
   not yet in the library go through `lexsis_asset_upload.upload` with the
   selected `workspace_id` and `theme_id`; wait for the user's uploaded-asset
   message with the new asset id. Import supplied URLs, image base64 plus
   `mime_type`, or conversation attachments through `lexsis_asset_import.import`
   instead, using exactly one source. Without inline UI, ask for a URL or
   conversation attachment and import it; never call import with no source.
2. **Skill fills the gaps.** For every slot still unresolved, search the
   product's Shopify media through `lexsis_catalog.get`, then
   `lexsis_asset_library.search` (tags first, then semantic, then filename).
   Present the table with the best candidate per slot and, for every slot
   with no candidate, say exactly what is missing (section, job, aspect,
   count). Then ask once: **I pick** (use the best match for every remaining
   slot), **Upload** (the merchant supplies files through
   `lexsis_asset_upload.upload`, or URLs/attachments through
   `lexsis_asset_import.import`), or **Generate the gaps**
   (only ALLOW purposes, or ASK purposes with the merchant's yes recorded;
   check `lexsis_workspace.credits`, then `lexsis_drafts.asset_generate` per
   slot with its purpose and aspect). Skipping a section is the merchant's
   choice, offered alongside.
3. View every asset before it fills a slot. `lexsis_assets.view` returns the
   image itself; judge it against the section with the fit review in
   `references/workflows/section-asset-workflow.md` (subject does the job,
   crops without losing the subject, leaves a quiet area for the copy,
   matches the neighbouring slots' lighting and styling, colours sit inside
   the palette, no baked-in text or watermark). A filename, tag or alt text
   is never evidence. View the candidates for one section together so the set
   reads as one shoot. Record the provider and asset id for generated slots
   and view those too.
4. Write the final table into the plan and one `assets[]` entry per slot into
   the page record. A slot the user postpones stays `planned`; `/design-page`
   confirms only those.

### Proof ledger

Every proof element on the page is a row in the `## Proof ledger` block
defined in `references/proof/proof-ledger.md`: kind, claim it supports,
source, evidence id or URL, verification status, and the section that shows
it. Nothing renders that is not in the ledger. Fill it with the tiered
procedure in `references/proof/reviews-sourcing.md`:

1. `lexsis_catalog.reviews_status`, then `lexsis_catalog.review_collections`
   with `collection_status: "active"`, then `lexsis_catalog.reviews`
   (`rating_min`, `has_media`, `product_id`) for counts and distribution.
2. `lexsis_catalog.reviews_search` once per top decision question to place
   proof beside the claim it answers.
3. Only when tiers 1 and 2 return nothing usable: the zero-review playbook
   (public reviews on marketplaces, Google, Trustpilot, Reddit, YouTube,
   creator content) via the host's web search and `lexsis_assets.view`. An
   external quote enters the ledger as `external-verified` only with its
   source URL, the merchant's written approval, verbatim text, and
   attribution the platform's terms permit. Marketplace review text that the
   platform forbids reusing is evidence for the merchant, never page copy.
4. Still nothing: plan guarantees, policy facts, certifications with issuer
   ids, test data, a founder note, or verified press instead. Never a review
   section, never invented counts, never `SocialProofPopup`.

Ask question 9 with the active collections and their `item_count`. Every
number in the ledger comes from the API or a linked source and is repeated
under "Claims to confirm". The plan never activates a collection; to propose
a shortlist, run `lexsis_catalog.reviews_search` and, only when the user asks,
`lexsis_drafts.review_collection_create` (draft). If the host returns
`UNKNOWN_ACTION`, ask the user to pick a collection in Storefront U+2192 Reviews U+2192
Collections and paste its id.

Press logos, "as seen in" marquees, badges, certifications, UGC, before/after
media, expert quotes, and counts follow their own files in
`references/proof/`. A press logo without a linked article, a badge without
an issuer, UGC without rights, or a count without a source does not enter the
ledger and does not appear on the page.

### Offer ledger

When the page carries any offer, discount, bundle price, urgency, or
delivery promise, write the `## Offer ledger` block from
`references/offers/offer-ledger.md`: offer type, exact terms, math shown on
the page, compare-at basis, start and end, stock basis, exclusions, regions,
code, stacking, and who confirmed each item. Use
`references/offers/offer-types.md` for the anatomy changes the offer type
requires and `references/offers/price-presentation.md` and
`references/offers/urgency-scarcity.md` for what may be shown. A countdown or
stock indicator is planned only when the ledger has a confirmed end date or
live inventory read. Mirror the summary in the page record `offer` block.

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

Record the confirmed binding, ordered sections, asset decisions, reviews,
offer evidence and unresolved questions in the task handoff. No per-page
manifest, source, theme, compile or QA files are created.

## Approval

Present:

```text
Page:
Campaign: <campaign-slug> (<campaign type>)
Binding: <workspace> / <store> / <theme>
Page type: <type> ; <funnel stage> ; <awareness> ; <traffic>
Deviations from the type default: <none | list>
Mandatory sections omitted:
Goal:
Audience:
Offer: <type and terms | none>
Campaign:
Copy framework:
Template direction:
Design direction:
Bold moment:
Overrides:
Sections:
Asset slots: <n verified / m planned / k blocked by generation policy>
Planned slots (unresolved):
Proof ledger: <n verified / m pending / k dropped>
Consumer decision model:
Behavioral hypothesis:
Claims to confirm:
Next route: <concept-first | direct-design | fast-build>
```

For `production-ready`, wait for approval. For `fast-draft`, present the
summary and continue to the inferred reversible route unless the user asked to
review the plan first or the route requires paid generation.

## Return

Return the plan and campaign summary, workspace/store/theme binding, asset
slot summary, the
missing-asset list, the inferred next route, and `PLAN_APPROVED`. Name the
route with the command it maps to:

| Route | Next command | When |
|---|---|---|
| `direct-design` | `/design-page` | the normal source and hosted-draft review |
| `concept-first` | `/design-page` (concept path) | the user wants to approve a mockup first |
| `fast-build` | `/build` | fastest draft, no template supplied |
| `fast-build` | `/build-with-template` | the user supplied a page-kit or section-template URL |

Every route builds the page the same way: the type's `## Workflow`, media
decided per section before copy, every asset viewed before use, and missing
slots reported rather than filled with colour or copy. `fast-build` asks fewer
questions and skips the design-approval stage; it does not skip the assets.

---
name: plan-page
description: Produce the complete, execution-ready specification for one storefront page: strategy, final section copy, a resolved asset decision for every section, claim and proof gates, an ordered work queue with owners, and a plan status. Waits for explicit approval before design. Does not choose islands or implementation.
---

# Plan a Page

The plan is the entire blueprint of the page. `/design-page` builds from it
without reopening strategy, writing copy, or deciding what image goes where.
A plan that says "explain benefits", "show product imagery" or "TBD" is not a
plan; write the customer-facing copy and name the exact asset instead.

One speed: every plan is complete, every plan waits for explicit approval.
This skill spends no credits; it reads `lexsis_workspace.credits` only to
estimate a generation brief. The plan must not define islands, schemas or
props; it records the behaviour a section needs and the decision inputs, and
`/design-page` resolves the current island against the live catalog.

## References

Read a row only when its trigger applies. Everything else you need is in this
file.

| Reference | Read when |
|---|---|
| `references/page-types/_index.md`, then only the matching `references/page-types/<type>.md` | always; the type file's `## Workflow` supplies the context reads, the per-section inputs and the asset budget |
| `references/consumer-behavior-cro.md` | writing the Consumer decision model |
| `references/copy/copy-frameworks.md`, `references/copy/headline-and-cta-rules.md` | choosing the framework and writing section copy |
| `references/copy/message-match.md` | ad or paid-search traffic |
| `references/anti-patterns/copy-anti-patterns.md` | checking the finished copy |
| `references/design-rules.md` | the Design direction block (A1 fields, N2 background, N7 overlays) |
| `references/assets/generation-policy.md` sections 1, 3 and 4 | any slot that may be generated or composited (ALLOW / ASK / NEVER) |
| `references/workflows/section-asset-workflow.md` section 2 | the fit review before an asset enters a slot |
| `references/proof/proof-ledger.md`, `references/proof/reviews-sourcing.md` | the Proof ledger |
| `references/proof/press-and-media-mentions.md`, `references/proof/trust-badges-certifications.md`, `references/proof/ugc-rights-and-display.md`, `references/proof/before-after-and-claims.md` | only when the page plans that kind of proof |
| `references/offers/offer-ledger.md` | any discount, bundle price, urgency or delivery promise |
| `references/workflow-intent.md` | deciding how many optional questions to ask; it never skips approval |

Use `lexsis_catalog.list`, `lexsis_catalog.get`, `lexsis_brand.context`,
`lexsis_brand.brand_kit`, `lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`, `lexsis_template_library.get_kit`,
`lexsis_asset_library.search`, `lexsis_assets.view`,
`lexsis_asset_import.import`, `lexsis_asset_upload.upload`,
`lexsis_workspace.credits`, `lexsis_catalog.reviews_status`,
`lexsis_catalog.review_collections`, `lexsis_catalog.reviews`,
`lexsis_catalog.reviews_search`, and, for ad-driven or persona-led pages,
`lexsis_campaigns.creatives`, `lexsis_campaigns.analyze`,
`lexsis_campaigns.frames`, `lexsis_campaigns.personas`,
`lexsis_campaigns.match_persona`; for quiz and lead-capture types,
`lexsis_capture.funnel_templates` and `lexsis_capture.funnel_template`.
Resolve an unfamiliar schema with exact router/action discovery.

## Bind the Workspace and Campaign

Reuse the confirmed workspace, store and theme from saved setup or current
MCP context. Resolve an ambiguous selection before proceeding and state the
chosen binding in one line. Never mix stores or themes on one page.

Group this page with its campaign purpose, confirmed dates, offer and
audience. Reuse existing campaign evidence for variants and edits. Keep the
plan and the compact page record in the task handoff; do not create campaign
folders or page files.

## Identify the Page Type

Do this before any template, asset, or proof call. Walk the decision tree in
`references/page-types/_index.md` from the brief: traffic source, funnel stage,
awareness level, offer shape, product count, campaign trigger, desired action.
Choose exactly one `pageType`. When two fit, the index names the tie-break;
when the brief is silent, choose the type that assumes less of the visitor and
say so. Then load only `references/page-types/<type>.md`.

Write this block at the top of the plan and mirror it in the page record
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
   its row in `### Section by section` gives the media job, the interaction
   decision inputs and the copy constraints. Those rows feed the Section
   specification and the Asset slots below; the plan writes the actual copy
   and the actual asset decision, not the row.
3. **Asset budget.** Fill the type's asset-budget table for this product:
   what the catalog and library supply, which jobs are missing, and per gap
   which decision state applies. Assets carry the page; plain colour does
   not.

The `## Checklist` JSON is the default this workflow lands on. When the
context argues for something else (a PDP with two images, a store with no
reviews, a brand whose voice bans a section), deviate and record it under
"Deviations from the type default". Review the checklist before presenting
the plan; explain every deviation without treating it as an automatic failure.

## Ask Only What Is Missing

Collect, only when the brief and the live store do not already answer:

1. Page type, when the identified type is ambiguous.
2. Product or collection, and the default variant.
3. Audience and customer problem.
4. Traffic source and the creative, when paid.
5. Primary conversion goal and CTA destination.
6. Required proof, offer, claim, or section constraints.

Ask no more than three questions at once. Read current products, variants,
prices, availability, media, and reviews from Lexsis before asking. Use
`references/consumer-behavior-cro.md` to inspect likely shopper uncertainty
before asking. Do not ask about custom imagery until the existing gallery and
library have been mapped to their jobs and a specific gap is visible.

`references/workflow-intent.md` decides only how many of the optional
questions below to ask: a user who delegates specifics gets the skill's
choice for 7 and 9; a user preparing a campaign hand-off is offered all three.
Neither reading skips the approval at the end.

7. Template: user-selected kit or sections, or skill-selected direction.
8. Assets: the role-by-role choice in `## User selection` (always offered
   when a role has more than one fit candidate).
9. Reviews: which active review collection the page uses, product reviews,
   or none.

## Choose a Direction

The catalog is small (about 30 page kits, about 200 section templates, a few
kits per page type); a person scans it faster than a query ranks it.

**User picks (question 7).** Call `lexsis_template_library.search_page_kits`
with `query: ""`, the `page_type`, `industry` and `mood` filters, and
`limit: 20`. When the host shows the Template Gallery, wait for the
`Design template selection:` message and record its `kind` and `slug` or `id`.
If no kit fits, browse `search_sections` with `query: ""` for the section that
matters most. Without a picker, give the public gallery
`https://storefront.trylexsis.com/templates?view=kits&page_type=<type>&industry=<vertical>&mood=<mood>`
and accept a pasted kit URL, template URL, slug, or id. Resolve kit slugs and
URLs with `lexsis_template_library.get_kit`; pass template URLs on unchanged.

**Skill picks (user declined).** Search page kits using the page type,
objective, industry, and mood. If no kit fits, inspect the returned status
before deciding why: a successful response with zero results means that
shelf is empty, so continue with section search or a custom direction; a
failed request is a tool error, so report it. Present at most three
candidates, one line each, and ask the user to confirm one or decline all.

Record only the selected kit or section ids in the page record
(`template.mode` is `page-kit`, `sections`, or `custom`) and the one-line
rationale in the plan. Template selection is directional: `/design-page` owns
fetching source, adapting layouts, selecting islands, and resolving schemas.

## Parallel Planning

If the runtime can spawn sub-agents, fan out three read-only lanes and merge
their output; otherwise run the same three blocks sequentially in this order.

1. Strategy, Consumer decision model, Design direction and wireframe.
2. Section specification (final copy per section) and the Claim gate.
3. Asset slots, User selection candidates, Generation briefs, Proof ledger and
   Offer ledger.

Each lane returns only its blocks. The parent merges them, runs the
generic-default check, resolves conflicts by the house rules, computes the Work
queue and Plan status, and asks only the questions still open. Lanes never
write files or spend credits.

## The Plan

Write these blocks, in this order, every time:

1. `## Page type` (above)
2. `## Page strategy`
3. `## Consumer decision model`
4. `## Design direction` (includes the Imagery and background plan)
5. `## Section specification`
6. `## Asset slots`
7. `## User selection` (only when a role has more than one fit candidate)
8. `## Generation briefs` (only when a slot is generate-required or composite-required)
9. `## Generation record` (header only; `/design-page` fills it after generation)
10. `## Proof ledger`
11. `## Offer ledger` (only when an offer exists)
12. `## Message match` (only for ad or paid-search traffic)
13. `## Claim gate`
14. `## Work queue`
15. `## Plan status`

Every block is present; `none` is an answer, `TBD` is not. A plan missing a
block, or carrying a placeholder where copy or an asset decision belongs, is
not presented for approval.

### Page strategy

```markdown
## Page strategy

**Landing-page type.** <pageType>
**Funnel stage / awareness.** <tof | mof | bof | retention> / <unaware | problem-aware | solution-aware | product-aware | most-aware>
**Traffic / ad source.** <meta | google | tiktok | email | organic | ...>; creative <id or none>
**Campaign goal.** <one measurable action: add to cart | purchase | lead | waitlist | quiz start>
**Offer and purchase model.** <offer-types id or none>; <one-time | subscription | pre-order | bundle>; terms in the Offer ledger
**Product and default variant.** <title> gid://shopify/Product/<id>; default variant gid://shopify/ProductVariant/<id> (<option values>); price <currency amount>
**Visual direction.** One sentence: the mood, the bold moment, the media treatment (detail in Design direction).
**Copy framework.** <copy-frameworks id>; secondaries: <section: id, ...> or none
**Headline pattern.** <the headline formula for this awareness level>; 4U score <useful>/<urgent>/<unique>/<ultra-specific> = <total>
**Message match.** <one line: ad promise, ad noun phrase, CTA verb the page repeats> or `not ad traffic`
**Section order.** 1 <id> ; 2 <id> ; 3 <id> ; ... (canonical ids; header, announcement, footer and sticky-cta listed where they sit)
```

Rules: one primary framework from the type checklist's `copy_framework` list,
matched to the awareness level (`references/copy/copy-frameworks.md` CF1 and
CF2); the headline formula and the 4U score come from
`references/copy/headline-and-cta-rules.md` (ship at 12 or more, rewrite under
8); for ad traffic the message-match line follows
`references/copy/message-match.md`. Section ids come from the canonical
vocabulary in the type file; the order is the type's Anatomy order unless a
recorded deviation says otherwise.

### Consumer decision model

Copy the block from `references/consumer-behavior-cro.md` into the plan and
fill every line:

```markdown
## Consumer decision model

**Primary visitor mode.** confirm | compare | explore | complete | replenish
**Top decision questions.** Three shopper questions this page must answer.
**Selected behavioral patterns.** At most three, each with observed evidence.
**First decision area.** Facts, proof, and action visible before deeper detail.
**Gallery jobs.** covered; missing; asset slots created for missing jobs.
**Guided merchandising.** relationship name, reason, 2-3 products or none.
**Risk and trust.** sourced proof/policy placed beside the relevant decision.
**Mobile context.** what remains visible or is repeated during long scroll.
**Hypothesis and metric.** one primary behavior change and measurement.
```

### Design direction

Read the saved brand design, the theme tokens and `references/design-rules.md`
first. Fill every field; "none" is an answer, "TBD" is not. Then run the
generic-default check and revise anything it catches.

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

Write one line per imagery section at the end of the Design direction block:

```text
<section> U+2192 <slot ids> U+2192 <treatment: full-bleed | inset | grid | background image with legibility overlay>
```

Every imagery section maps to at least one slot. The single full-bleed
exception is the bold moment named above. Sections without imagery are
separated by spacing and a hairline, not colour. Map the existing gallery to
the type's required image jobs (identity, detail, scale, texture, in-use,
context, variation, sequence, sourced proof) and create a slot for every
required job the gallery does not cover; the decision for each slot is made in
Asset slots below.

### Section specification

One entry per section, in Section order. The copy is the final customer-facing
text `/design-page` will place; it is not a brief for someone else to write.

```markdown
## Section specification

### S1. hero - <purpose in one line>

**Copy.**
- Eyebrow: <text or none>
- Headline: <text, at most 10 words, sentence case>
- Subhead: <text, at most 20 words, or none>
- Body: <paragraph(s), at most 45 words each>
- Labels / bullets: <exact strings, or none>
- CTA: "<verb + object [+ outcome or price]>" -> <#buy-box | URL | cart action>
- FAQ (faq sections only): Q: <question> / A: <answer whose first sentence is the answer>
**Claims in this section.** <C# ids from the Claim gate> or none
**Layout.** 1280: <media share, column order, buy-box position> | 390: <stack order, what stays above the fold>
**Interaction.** none | <behaviour the shopper needs and the decision inputs: variant count, review band, page length>; no island names, schemas or props
**Asset.** <slot id: decision state> | none-required: <why this section carries no image>
```

Rules for the copy:

- Final text only. A bracket, "TBD", "lorem", or an instruction such as
  "explain benefits" fails the plan.
- Ceilings: h1 at most 10 words, subhead at most 20, paragraph at most 45,
  FAQ answer at most 60 (`references/copy/copy-frameworks.md` CF5 and the
  type file's tighter ceilings where given). Sentence case throughout; the
  CTA names the action and its destination; the first sentence of every FAQ
  answer is the answer.
- Every number, quote, count, price, badge or timeframe in the copy is a
  Claim gate row backed by a `P#` or `O#` ledger row. An unresolved number is
  deleted with its sentence, never estimated.
- For ad traffic the h1 keeps at least 60 percent token overlap with the ad
  headline and the CTA verb equals the ad's (`references/copy/message-match.md`).
- Check the finished copy against `references/anti-patterns/copy-anti-patterns.md`;
  nothing from that list ships.
- A section that would end up as a colour band, an emoji row, icon tiles or a
  wall of text is rebuilt around imagery or put to the merchant.

### Asset slots

List every slot the wireframe names. Every section has exactly one asset
decision: a slot row here, or `none-required` with its reason on the
section's `Asset` line.

```markdown
## Asset slots

| Slot | Section | Role/purpose | Aspect | Decision | Source decision | Id / URL | Status |
|---|---|---|---|---|---|---|---|
| A1 | buy-box | product_media (identity) | 1:1 | shopify-product-media | shopify media, viewed | gid://shopify/Product/1 / gid://shopify/MediaImage/123 | verified |
| A2 | story | context | 3:2 | reuse-selected | library, viewed; crop: centre-right; placement: inset left; alt intent: kitchen counter with the jar | asset 7f2e... | verified |
| A3 | hero | hero_bg | 16:9 + 4:5 | generate-required | generated (hero_bg, library: none); brief G1 | | planned |
| A4 | benefits | context | 1:1 + 4:5 | composite-required | generated (product_composite over A1, library: none); brief G2 | | planned |
| A5 | reviews | proof (ugc, ledger P5) | 1:1 | user-selection-required | 4 library candidates in User selection, role 3 | | planned |
| A6 | how-it-works | sequence | 3:2 | user-upload-required | merchant-upload: three step photos of the routine, same light, product legible | | planned |

Reference-only creatives: <asset or creative id> - <why it cannot be placed: baked-in headline / badge / price / claim> -> replaced by slot <A#>.
```

Decision states, exactly one per section:

| Decision | Meaning | Status | Page record `assets[]` |
|---|---|---|---|
| `none-required` | The section carries no image; say why (native disclosure, factual table, text-only per the type). Appears on the section's `Asset` line only, never as a slot row. | n/a | none |
| `reuse-selected` | An existing library asset, viewed and fit-reviewed; crop, placement and alt-text intent written in Source decision. | `verified` | `decision`, `sourceType: lexsis`, `assetId`, `url` |
| `shopify-product-media` | The exact product or variant media item; placement written. | `verified` | `decision`, `sourceType: shopify`, `productId`, `mediaId`, `url` |
| `user-selection-required` | Two or more fit-reviewed library candidates suit this role; they are listed under `## User selection` and the plan waits for the choice. | `planned` | `decision`, `sourceType: pending` |
| `user-upload-required` | No suitable media exists and the job may not be generated (the product itself, people as customers, results, logos, badges, text in images); name the exact source file needed. | `planned` | `decision`, `sourceType: pending` |
| `generate-required` | An ALLOW purpose, or an ASK purpose with the merchant's yes quoted; brief `G#` written below. | `planned` until `/design-page` generates | `decision`, `sourceType: pending`, `role` = purpose, `askApproved: true` for ASK |
| `composite-required` | A `product_composite`: the real product media (named slot) plus a generated or editorial layer, each defined in brief `G#`. | `planned` | as above plus `referenceSlot` |
| `reference-only` | A baked ad creative or any image carrying copy, badges, claims or product text that cannot be safely cropped. Never a slot source; listed under the table with the slot that replaces it. | none | not in `assets[]` |

`Status` stays `verified` or `planned`: `verified` only with `reuse-selected`
or `shopify-product-media`; `planned` only with the four pending states.
`Role/purpose` is the image job for real media (`product_media`, `context`,
`in-use`, `proof`, ...) and the generation purpose for generated media
(`hero_bg`, `section_bg`, `card_bg`, `texture_fill`, `pattern_tile`,
`decorative_element`, `product_composite`; `product_lifestyle` only as ASK).
`Source decision` uses one of: `shopify media`, `library <asset id>`,
`merchant-upload (owner: merchant, <date>)`, `supplier (licence: <ref>)`,
`stock (licence: <id>)`, `generated (<purpose>, library: none)`; append
`viewed` once the asset has been seen. Ordinary interface icons come from one
inline SVG set and are not slots; emoji are never an icon fallback.

Resolve every slot to a decision before approval, in this order:

1. **Inventory.** Map the catalog media from `lexsis_catalog.get` and the
   library (`lexsis_asset_library.search` with `theme_id`, `mode: "tags"`
   using `hero`, `lifestyle`, `product-shot`, `social-proof`, `logo`, then a
   semantic query per missing job) to the jobs the type requires. Run a
   `mode: "ocr"` search to flag candidates with baked-in text before viewing
   them.
2. **View.** Nothing enters a slot from a filename, tag or search rank.
   `lexsis_assets.view` returns the image itself; judge it in its section
   with the fit review in `references/workflows/section-asset-workflow.md`
   section 2: the subject does the job, it crops to the slot aspect without
   losing the subject, it leaves a quiet area where the headline and body
   sit, it matches the neighbouring slots' lighting and styling, its colours
   sit inside the palette, and it carries no baked-in text or watermark. View
   a section's candidates together so the set reads as one set of photographs.
   A creative that fails only on baked-in copy is `reference-only`.
3. **Decide.** One fit candidate: `reuse-selected` or `shopify-product-media`.
   Two or more: `user-selection-required`, listed by role below. None, and
   the job is on the generation NEVER list: `user-upload-required` with the
   exact file described. None, and the purpose is ALLOW (or ASK with a yes):
   `generate-required` or `composite-required` with a brief. No image needed:
   `none-required` with the reason.
4. **Offer the choice by role.** Present `## User selection` and wait. Never
   make the user choose among irrelevant assets; never assume a selection
   when the visual decision materially affects the page (the hero, the
   formula or detail visual, the proof visual, the closing visual).

```markdown
## User selection

Choose one asset per role. Only roles with more than one fit-reviewed candidate are listed; a single fit is already reuse-selected.

| Role | Section / slot | Candidates (asset id - one-line description - fit note) | Why the choice matters |
|---|---|---|---|
| 1 hero editorial visual | hero / A3 | 8c1f... - jar on linen, quiet left third - crops to 4:5 ; 2d9a... - overhead flat lay - no quiet area at 390 | sets the bold moment and the message match with the ad |
| 2 formula / detail visual | ingredients / A4 | ... | shows the mechanism the copy claims |
| 3 social-proof / results visual | reviews / A5 | ... | must carry a proof-ledger row |
| 4 closing CTA visual | closing-cta / A7 | ... | reuse of A1 is the default if none |

Reply with the role number and asset id, or "agent picks" per role.
```

Picker mechanics: one `lexsis_asset_library.search` per role group
(`query: ""`, `kind: "image"` or `"svg"` for the logo, `mode: "tags"`,
`theme_id` from setup, `limit: 48`). When the host shows the asset picker,
wait for the `Design asset selection:` message and map its `assets[]` to the
roles in `selection_order`; confirm the mapping in one line. Without a
picker, accept asset ids, filenames (`mode: "filename"`) or URLs. Files not
yet in the library go through `lexsis_asset_upload.upload` with the selected
`workspace_id` and `theme_id` (wait for the user's uploaded-asset message) or,
for a URL, image base64 with `mime_type`, or a conversation attachment,
through `lexsis_asset_import.import` with exactly one source. View every
uploaded or imported asset before it fills a slot.

Every `generate-required` or `composite-required` slot has a brief:

```markdown
## Generation briefs

### G1 - slot A3, hero, hero_bg (ALLOW)
**Aspect and crops.** landscape 1536x1024 for 1280; portrait 1024x1536 for 390; focal point centre-left, quiet right third for the h1
**Subject and composition.** unbleached linen surface, one ceramic bowl at the left edge, empty right two thirds
**Wardrobe.** none (no people)
**Palette.** brand hexes #F5F0E6 #1F1D24 #B8654A; nothing outside the Design direction palette
**Lighting and mood.** soft north window light, late morning, calm
**Exclusions.** text, letters, logos, badges, prices, packaging, fake product, UI, hands, people, watermarks
**Composite.** none | real product media <A1 mediaId> composited untouched on top (product_composite)
**Alt-text intent.** decorative: alt="" aria-hidden | composite: "<product> on a linen surface (generated scene)"
**Estimated credits.** <n> per image x <images> (balance <b> from lexsis_workspace.credits)
**Approval.** ALLOW - credits confirmed in /design-page before the call | ASK - "<merchant's words>" <name> <date> | pending merchant yes (Work queue T#)
```

Brief rules: purposes, aspects and the ALLOW / ASK / NEVER lists come from
`references/assets/generation-policy.md`; a NEVER job (the product itself,
people presented as customers or staff, results, logos, badges, text in
images) is never briefed and becomes `user-upload-required`; at most four
generated slots per page; an ASK approval quotes the merchant's words and
date, and plan approval alone never counts as ASK approval. After generation
`/design-page` writes the `## Generation record` row (prompt, negatives,
provider, asset id, metadata, label) and flips the slot to `verified`.

### Proof ledger

Every proof element on the page is a row in the `## Proof ledger` block
defined in `references/proof/proof-ledger.md`: kind, the exact claim it
supports, source, evidence id or URL, how and when verified, the section that
shows it, and `verified | pending | dropped`. Nothing renders that is not in
the ledger. Fill it with the tiered procedure in
`references/proof/reviews-sourcing.md`:

1. `lexsis_catalog.reviews_status`, then `lexsis_catalog.review_collections`
   with `collection_status: "active"`, then `lexsis_catalog.reviews`
   (`rating_min`, `has_media`, `product_id`) for counts and distribution.
2. `lexsis_catalog.reviews_search` once per top decision question to place
   proof beside the claim it answers.
3. Only when tiers 1 and 2 return nothing usable: the zero-review playbook
   (public reviews, Google, Trustpilot, Reddit, YouTube, creator content) via
   the host's web search and `lexsis_assets.view`. An external quote enters
   the ledger as `external-verified` only with its source URL, the merchant's
   written approval, verbatim text, and attribution the platform permits.
4. Still nothing: guarantees, policy facts, certifications with issuer ids,
   test data, a founder note, or verified press instead. Never a review
   section, never invented counts, never a social-proof popup.

Ask question 9 with the active collections and their `item_count`. Every
number in the ledger comes from the API or a linked source and appears as a
Claim gate row. The plan never activates a collection; to propose a shortlist,
run `lexsis_catalog.reviews_search` and, only when the user asks,
`lexsis_drafts.review_collection_create` (draft). If the host returns
`UNKNOWN_ACTION`, ask the user to pick a collection in Storefront > Reviews >
Collections and paste its id.

Press logos, "as seen in" marquees, badges, certifications, UGC, before/after
media, expert quotes, and counts follow their own files in
`references/proof/`. A press logo without a linked article, a badge without
an issuer, UGC without rights, or a count without a source does not enter the
ledger and does not appear on the page.

### Offer ledger

When the page carries any offer, discount, bundle price, urgency, or delivery
promise, write the `## Offer ledger` block from
`references/offers/offer-ledger.md`: offer type, exact terms, the math shown
on the page, compare-at basis, start and end, stock basis, exclusions,
regions, code, stacking, and who confirmed each item. A countdown or stock
indicator is planned only when the ledger has a confirmed end date or a live
inventory read. Mirror the summary in the page record `offer` block. Each
item the ledger file lists under "Claims to confirm before design" becomes an
Offer ledger row or a Claim gate row; do not keep a separate list.

Verify facts that control the page's urgency or trust before treating them as
copy: occasion dates, delivery cutoffs, prices, availability, medical or
performance claims, certifications, endorsements, and legal or safety
language. Use an authoritative current source where one exists. An unverified
item is a `merchant evidence required` Claim gate row, not a guess.

### Claim gate

One row per claim in the ad creative and per claim in the proposed copy.

```markdown
## Claim gate

| # | Claim (verbatim) | Where | Gate | Evidence | V1 copy if not approved |
|---|---|---|---|---|---|
| C1 | "4.8 stars from 212 reviews" | ad + hero | approved evidence available | P1 (verified) | - |
| C2 | "Dermatologist tested" | ad + trust-bar | merchant evidence required | test report with lab, date, n -> P8 pending | "Fragrance-free, patch-test recommended" |
| C3 | "Visible results in 14 days" | ad | remove from V1 | no study, no customer data | not on the page; the ad needs a rewrite |
```

Gates:

- `approved evidence available`: a `verified` `P#` or `O#` row whose Section
  column is this section. The claim ships.
- `merchant evidence required`: the evidence exists somewhere the agent
  cannot reach. Write the V1 copy that ships without the claim, and add a
  `merchant`-owned Work queue task naming the document.
- `remove from V1`: no evidence and no path to it. Delete the sentence, never
  soften it.

Clinical badges, before/after imagery, ratings, review counts, result
timelines and efficacy claims never appear without an evidence source
assigned to that exact section. An ad claim the page cannot carry is reported
as a message-match risk, not quietly dropped.

### Work queue

End every plan with the ordered checklist the next workflow executes.

```markdown
## Work queue

| # | Task | Owner | Section / slot | Unblocks | Status |
|---|---|---|---|---|---|
| T1 | Supply the dermatologist test report (lab, date, n) | merchant | trust-bar / C2 | C2 -> approved | open |
| T2 | Choose the hero editorial visual (User selection role 1) | user | hero / A3 | A3 -> reuse-selected | open |
| T3 | Upload three routine step photos, same light, product legible | user | how-it-works / A6 | A6 -> verified | open |
| T4 | Generate G1 at 16:9 and 4:5 after credit confirmation | agent | hero / A3 | A3 -> verified | open |
| T5 | Bind Shopify media gid://.../123 to the purchase section | agent | buy-box / A1 | - | done |
| T6 | Confirm shipping and returns copy against the policy page | merchant | shipping-returns / O7, O13 | O7, O13 -> verified | open |
| T7 | Build the page from the approved copy and selected assets | agent | all | DRAFT_CREATED | open |
| T8 | Verify 1280 and 390 crops for every slot | agent | all slots | hosted review | open |
| T9 | Run claim, asset and CTA QA at 390, 768 and 1280 | agent | all | DESIGN_APPROVED | open |
```

Owners:

- `user`: the person in this conversation (a choice, an upload, an answer).
- `agent`: `/design-page` executes it without asking.
- `merchant`: someone outside the conversation supplies a document, an
  approval or a fact.
- `blocked-by-evidence`: no owner can act until evidence exists; the page has
  no V1 without it.

Every plan carries at least: build the page, verify the crops, run claim,
asset and CTA QA; plus one task per open claim, per pending slot, and per
unconfirmed offer item.

### Plan status

```markdown
## Plan status

**Plan status.** PLAN_READY_FOR_DESIGN | PLAN_COMPLETE - asset tasks pending | BLOCKED - evidence required
**Blocking items.** none | <C#, A#, O#, S# with one line each>
**Approval.** pending | PLAN_APPROVED <who> <date>
```

Compute it from the Work queue: `BLOCKED - evidence required` when any open
task is `blocked-by-evidence`; otherwise `PLAN_COMPLETE - asset tasks pending`
when any open task is owned by `user` or `merchant`; otherwise
`PLAN_READY_FOR_DESIGN`.

The plan is not ready while any section has missing final copy, an
unresolved `Asset` line, a `planned` slot without a decision state, a Claim
gate row without a gate, a CTA without a destination, or an unchosen product
or variant. `PLAN_APPROVED` is written only after the user's explicit
approval in this conversation, and never while the status is
`BLOCKED - evidence required`.

## Do Not Include

- island names or schemas
- island props or hydration modes
- HTML, CSS, Tailwind classes, or implementation notes
- asset search transcripts or rejected candidates
- gradients, hover effects, or motion beyond the Motion line
- template search transcripts
- QA, compilation, synchronization, or publishing state

Record the confirmed binding, section order, asset decisions, reviews, offer
evidence, claim gates and open tasks in the task handoff. No per-page
manifest, source, theme, compile or QA files are created.

## Approval

Present the plan, then this summary:

```text
Page:
Campaign: <campaign-slug> (<campaign type>)
Binding: <workspace> / <store> / <theme>
Page type: <type> ; <funnel stage> ; <awareness> ; <traffic>
Deviations from the type default: <none | list>
Mandatory sections omitted:
Goal:
Audience:
Product / default variant:
Offer: <type and terms | none>
Copy framework / headline pattern:
Template direction:
Design direction:
Bold moment:
Overrides:
Sections: <n, in order>
Asset slots: <n verified / m planned> ; decisions: <counts per state>
User selection: <roles awaiting a choice | none>
Generation briefs: <G# ids and estimated credits | none>
Proof ledger: <n verified / m pending / k dropped>
Claim gate: <n approved / m merchant evidence required / k removed>
Work queue: <n open: u user / a agent / m merchant / b blocked>
Plan status: <PLAN_READY_FOR_DESIGN | PLAN_COMPLETE - asset tasks pending | BLOCKED - evidence required>
```

Wait for explicit approval. Answer questions, take remaps and edits, and
re-present. Record `PLAN_APPROVED <who> <date>` in the Plan status block only
when the user approves and the status is not `BLOCKED - evidence required`.
A blocked plan is returned with its blocking items; the user decides whether
to obtain the evidence or remove the dependent sections.

## Return

Return the plan, the binding, the status label, the Work queue, and
`PLAN_APPROVED` when it was granted. The next command is always
`/design-page`; it reads the Plan status and the Work queue first, executes
the agent-owned tasks, asks for the user- and merchant-owned ones, and builds
the page from the approved copy and the selected assets.

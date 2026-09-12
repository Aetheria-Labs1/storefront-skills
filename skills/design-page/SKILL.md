---
name: design-page
description: Turn an approved page plan into canonical Lexsis source and one unpublished hosted draft, run the hosted review at 390, 768 and 1280 with commerce checks, apply later edits with version protection, and return DESIGN_APPROVED. Never publishes.
---

# Design the Page

Build the page the plan specifies, compile it, create one unpublished hosted
draft, review it on the real renderer, fix it in place, and return
`DESIGN_APPROVED` once the user approves the reviewed version. Never publish.

Read:

- `references/plan-page.md` for the plan blocks, asset decision states,
  claim gates, work-queue owners and status labels this skill consumes
- `references/design-rules.md`
- the plan's `references/page-types/<type>.md` (its `## Workflow` names the
  island and asset decision inputs per section) and
  `references/page-types/_checklist-format.md` for the vocabulary
- `references/workflows/island-selection-workflow.md` (live schema
  resolution) and `references/workflows/section-asset-workflow.md`
- `references/authoring/css-and-styling.md` and
  `references/authoring/source-authoring.md` before writing any class or
  section CSS
- `references/mcp-playbooks/tool-sequence-by-stage.md` (Stages 2 and 3) and
  the matching row of `references/mcp-playbooks/tool-sequence-by-page-type.md`
- `references/animation-system.md` when the plan names a motion moment
- `references/consumer-behavior-cro.md`
- `references/island-presets.md`
- `references/merchant-templates.md`
- `references/design-concepts.md` only when the user wants a visual concept
  before source authoring
- `references/page-layout.md`
- `references/proof/proof-ledger.md` (display rules) and the proof files the
  ledger uses
- `references/offers/price-presentation.md` and
  `references/offers/urgency-scarcity.md` when the plan has an Offer ledger
- `references/assets/generation-policy.md` and `references/assets/slot-spec.md`;
  `references/assets/video-rules.md` when any slot is video
- `references/copy/headline-and-cta-rules.md`,
  `references/anti-patterns/copy-anti-patterns.md`,
  `references/anti-patterns/dark-patterns.md`,
  `references/anti-patterns/cro-anti-patterns.md`,
  `references/anti-patterns/mobile-anti-patterns.md`
- `references/qa-recipe.md` for the hosted review and
  `references/page-editing.md` for edits to an existing page
- `references/source-artifact-workflow.md` for direct MCP authoring

Use `lexsis_brand.context`, `lexsis_brand.get_theme`,
`lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`, `lexsis_design.guide`,
`lexsis_design.islands`, `lexsis_design.island_schema`,
`lexsis_design.get_section`, `lexsis_template_library.get_kit`,
`lexsis_asset_library.search`, `lexsis_catalog.get`, `lexsis_catalog.reviews`,
`lexsis_catalog.review_collection_items`, `lexsis_brand.navigation` (full-nav
types only), `lexsis_assets.capabilities`, `lexsis_assets.view`,
`lexsis_workspace.credits`, `lexsis_drafts.asset_generate`,
`lexsis_asset_import.import`, `lexsis_asset_upload.upload`,
`lexsis_pages.compile`, `lexsis_page_create.create`,
`lexsis_pages.edit_context`, `lexsis_pages.source`,
`lexsis_pages.section_source`, `lexsis_pages.integrity`, `lexsis_pages.qa`,
`lexsis_pages.diff`, `lexsis_drafts.page_update_section`,
`lexsis_drafts.page_patch`, `lexsis_drafts.page_update_head`, and
`lexsis_drafts.page_record_qa`.

When the user wants one of their saved reusable sections, use
`lexsis_template_library.list_mine` and `get_mine`. Treat its source as a
starting section in the page, not as an inherited renderer shell. Resolve
only unfamiliar argument schemas through exact router/action discovery.

## Inputs

Use the approved plan and its confirmed workspace, store and theme binding.
Follow `references/source-artifact-workflow.md` for direct MCP authoring.
The plan defines strategy, the Design direction, the Section specification
(the copy), the Asset slots (every media decision), the Proof and Offer
ledgers, the Claim gate and the Work queue; it must not define islands or
implementation details, and this skill does not reopen its decisions.

Implement the plan's Consumer decision model without adding generic CRO
modules. Preserve its visitor mode, top decision questions, selected patterns,
gallery jobs, merchandising relationship, risk treatment, mobile context, and
metric. Reopen a decision only when live catalog, asset, or policy evidence
contradicts the plan, and record the reopening.

If the user explicitly skips `/plan-page`, write the full plan with the same
blocks (Page type, Page strategy, Consumer decision model, Design direction,
Section specification, Asset slots, Proof ledger, Offer ledger when an offer
exists, Claim gate, Work queue, Plan status), obtain approval, and record the
skip. Never run `/setup` or `/plan-page` automatically.

An explicit `/design-page` request authorizes one page-creation credit for the
named page and nothing else: not paid asset generation, not a duplicate page,
not publishing. The hosted review below always runs before `DESIGN_APPROVED`.

## Plan Gate

Read `## Plan status` and `## Work queue` before anything else.

1. `BLOCKED - evidence required`, or `Approval: pending`: stop. Return the
   blocking items and the open tasks; do not compose.
2. `PLAN_COMPLETE - asset tasks pending` with `PLAN_APPROVED`: execute every
   open `agent` task that precedes composition (bind Shopify media, generate
   briefed slots after credit confirmation, author the icon set). Put every
   open `user` and `merchant` task into one message and wait. Compose only
   when no pending decision affects a section's copy or its asset.
3. `PLAN_READY_FOR_DESIGN` with `PLAN_APPROVED`: proceed.
4. Mark each task `done` as it completes and keep the Work queue current in
   the task handoff.

## Page-Type Workflow

Before any template fetch or HTML, read `page.pageType` from the page record
and the matching `references/page-types/<type>.md`. Its `## Workflow` names,
per section, the media job and the interactive decision inputs; the plan has
already turned those into a Section specification entry and an asset
decision. Compare the checklist with the plan's "Deviations from the type
default": a deviation the plan explains is a decision, a deviation it does not
mention is a question for the plan owner. A review section with no review data
or urgency with no verified basis is the one case to stop and ask.

For each section, in order:

1. Resolve its asset decision through Asset Gap Confirmation below.
2. Resolve the planned interaction through
   `references/workflows/island-selection-workflow.md`; the plan names the
   behaviour and the decision inputs, design selects the current island and
   schema-valid props.
3. Place the plan's copy through Copy Placement below.

Carry these type defaults into composition:

- **Above the fold (390px).** Build the type's first screen exactly as listed;
  nothing else enters it.
- **CTA.** Count, first position, sticky behaviour and copy from the plan's
  Section specification. Every CTA on a single-goal type performs the same
  action.
- **Nav.** `none` means logo only, not a link; `minimal` means logo plus one
  utility link; `full` means the store navigation from `lexsis_brand.navigation`.
- **Price.** `price_above_fold` is obeyed at 390 and 1280.
- **Proof density.** Module count inside the checklist range; kinds only from
  the ledger.

## Choose the Visual Route

Infer this from the request rather than always presenting a gate:

- Use the concept-first path when the user asks for a mockup, wants to approve
  the appearance before implementation, or explicitly chooses visual
  exploration.
- Otherwise continue directly to source and the hosted draft.
- If the user genuinely has not indicated whether they want visual approval,
  offer two choices in one line: generate a mobile-first concept, or continue
  directly to the hosted draft.

For concept-first work, follow `references/design-concepts.md`. Use the
existing Lexsis image generator, show mobile first, and return
`CONCEPT_READY`. Generate the desktop adaptation after the mobile direction is
approved unless the user requested both together. The concept is design
evidence only: keep it out of production `assets[]` and never use its URL in
page source.

After concept approval, return to the plan's Asset slots, confirm any
remaining paid generation batch, resolve those slots, and continue with the
ordinary Design Direction, Compose, Compile, Hosted Draft, and Approval stages.

## Design Direction Gate

Before writing any HTML, read the "Design direction" block in the plan and
`references/design-rules.md`. If the plan has no design direction, write one
now (palette of four to six named hex values, type roles and scale, layout
concept, wireframe with slot ids, icon decision, the one bold moment) and
record it in the plan before continuing.

Precedence, in order: house rules (`design-rules.md`) > merchant-stated brand
rules (`voice_md`, owner notes) > brand-kit token values > generated design.md
guidance > brand-kit preview blueprint and presets. A lower layer may narrow a
higher one, never widen it. Token values win over prose for values; if a token
value fails WCAG AA against its documented pairing, return
`THEME_CONTEXT_CONFLICT` with both values. Style guidance never raises a
conflict; it is overridden and recorded in the plan under "Overrides of
brand design.md".

## Copy Placement

The plan's Section specification is the copy. Place every eyebrow, headline,
subhead, body paragraph, label, CTA and FAQ answer verbatim, in its section.

- Edit only for layout fit: a line break, one word to avoid an orphan, a
  label that overflows at 390. Record every edit in a `## Copy edits` table
  appended to the plan: `| Section | Field | Plan text | Placed text | Reason |`.
- Never introduce a claim, number, price, count, quote or CTA the plan does
  not carry. A gap in the plan's copy is a question for the plan owner, not a
  sentence to invent.
- Sentence case, the CTA names its action and destination, the first
  sentence of every FAQ answer answers (`references/copy/headline-and-cta-rules.md`);
  nothing from `references/anti-patterns/copy-anti-patterns.md`.

## Claim Rendering

Render only Claim gate rows gated `approved evidence available`. A row gated
`merchant evidence required` renders its "V1 copy if not approved" text; a row
gated `remove from V1` renders nothing. Every numeral inside a proof, trust,
stats or press section traces to a `verified` Proof ledger or Offer ledger row.
A claim that appears in the copy without a Claim gate row stops composition
until the plan owner gates it.

## Asset Gap Confirmation

The plan made every asset decision. Read the `## Asset slots` table and
`assets[]` from the page record and act per decision:

| Decision | Action |
|---|---|
| `reuse-selected`, `shopify-product-media` (`verified`) | Final. Use the recorded ids, URLs, crop, placement and alt intent as-is. |
| `user-selection-required` | Show the plan's `## User selection` candidates for that role (view them again with `lexsis_assets.view`), wait for the choice, set the slot `verified`. |
| `user-upload-required` | Ask for the named file: `lexsis_asset_upload.upload` for the local-file UI (wait for the user's uploaded-asset message) or `lexsis_asset_import.import` for a URL, base64 image with `mime_type`, or attachment (exactly one source). View it, run the fit review, set `verified`. |
| `generate-required`, `composite-required` | Read `lexsis_workspace.credits`, confirm the batch (count, purposes, cost) with the user, then call `lexsis_drafts.asset_generate` exactly per the brief `G#`: purpose, aspect, style, negatives, brand hexes, `reference_images` holding the real cut-out for a composite. View the result, run the fit review, write the `## Generation record` row (prompt, negatives, provider, asset id, metadata, visible label, approver), set `verified`. A rejected result gets one bounded repair; then the slot is reported, not filled with colour. |
| `reference-only` | Never placed. Its replacement slot carries the section. |
| `none-required` | The section is built without media, as the plan says. |

View every asset with `lexsis_assets.view` before it enters the source and
run the fit review in `references/workflows/section-asset-workflow.md`
against the section it belongs to: subject, crop at the slot aspect, a quiet
area where the headline and body sit, consistency with the neighbouring
slots, palette, no baked-in text or watermark. Never place an asset from its
filename, tag or search rank alone.

Use Lexsis icons, supported SVG, or CSS for ordinary interface icons. When the
plan's Icons decision names a set to author, author one monochrome inline SVG
set (one stroke, one size) and import it. Never fall back to emoji as icons;
emoji appear only where the plan's "Emoji in copy" line allows them, inside
running text.

Generation obeys `references/assets/generation-policy.md`. ALLOW purposes
(`hero_bg`, `section_bg`, `card_bg`, `texture_fill`, `pattern_tile`,
`decorative_element`, `product_composite` over a real cut-out) are generated
after credit confirmation; `icon_set` means "author one monochrome inline SVG
set", never a raster generation; ASK purposes need the merchant's quoted yes
in the brief. NEVER purposes are not generated under any instruction short of
the merchant supplying the media: the product itself when Shopify media exists
or could exist, a person presented as a customer, reviewer, creator or staff,
before/after or result imagery, press logos, badges, certifications or awards,
text or prices inside images, and competitor products. Such a slot stays
`planned` as `user-upload-required` and the section is built without it or
removed with a note.

Do not use local or temporary placeholder assets. When a store has no usable
logo image, use an accessible text wordmark or plain HTML header. Do not
substitute a product image or generic logo placeholder.

## Compose

1. Read the saved brand design and selected theme CSS.
2. Use the template direction from the plan. For a user-picked kit recorded
   only as a slug or URL, call `lexsis_template_library.get_kit`, then fetch
   section source with `lexsis_design.get_section`, one to three ids per call,
   in kit order. Search again only when the plan has no usable template
   direction.
3. Convert each Section specification entry into responsive layout following
   its Layout line, the wireframe, the Imagery and background plan, and the
   slot ids. Header, Announcement, Navigation, and Footer are included here in
   their intended source order when required.
4. Read the compact island catalog and select only the interactive
   components the plan's Interaction lines call for. Do not fetch every full
   schema in advance. A `Preset:` label, if the plan carries one, records
   visual intent, not a frozen prop bundle. Follow
   `references/workflows/island-selection-workflow.md` to resolve that intent
   against the current schema. Record the actual props, hydration and scoped
   styling, with any intentional departure in `islands[].presetOverrides`.
5. Proof renders only from the plan's Proof ledger and the Claim Rendering
   rule. Review islands use the ledger's `collectionId` or `productIds`,
   `minRating`, `pageSize` of 12 or fewer. Omit the reviews endpoint prop; the
   page supplies it at runtime. `averageRating` and `totalReviews` only from
   the `lexsis_catalog.reviews` total. `none` means no review island. Never a
   social-proof popup, never a live viewer or purchase count. Star glyphs
   appear only next to a real average and count. Every press logo is an `<a>`
   to the ledger's article URL, monochrome, one height; a logo with no URL is
   not rendered. Badges and certifications carry the ledger's issuer text.
   Quotes are verbatim with the ledger's attribution.
6. Offers render from the Offer ledger following
   `references/offers/price-presentation.md`: current price first, compare-at
   struck through only with a recorded basis and a `data-source` attribute
   naming it, savings in the merchant's currency, unit or per-day price only
   when accurate, shipping and tax language from the store. Countdown and
   stock islands are bound to the ledger's confirmed end date or live
   inventory, never a fixed number or a timer that resets. Nothing in
   `references/anti-patterns/dark-patterns.md` ships.
7. Prepare a rough but complete source string with stable section
   delimiters from the canonical vocabulary, minimal island props, and the
   documented examples as a starting point.
8. Place the copy per Copy Placement.
9. Put page-wide rules in `theme_css`; keep section-specific CSS beside its
   section. `references/authoring/css-and-styling.md` decides which layer a
   rule belongs to.
10. Use LX tokens for brand values and compile-time Tailwind utilities for
    layout, mobile-first. There is no runtime Tailwind CDN, and a class the
    compiler cannot generate is a blocking error, so never invent class names.
    Author the source itself as `references/authoring/source-authoring.md`
    describes.
11. Compare explicit `NEVER`, `must`, and `non-negotiable` rules in the saved
    brand design with matching theme tokens. On a direct value contradiction,
    return `THEME_CONTEXT_CONFLICT` with both values. Do not silently choose one.
12. Use ordinary HTML for static content and `<lx-island>` source for supported
    interactions. Use headless mode only with complete required hooks.
13. Keep island props schema-valid and use current product bindings. Real
    commerce is tested on the hosted draft.
14. For guided merchandising, show two or three relevant choices by default,
    name the relationship, show why each item belongs, and preserve the primary
    product decision. Never use an unlabeled generic recommendation carousel.
15. Media follows `references/assets/slot-spec.md`: every `<img>` has the
    slot's aspect, minimum resolution, descriptive alt text from the plan's
    alt intent (empty alt for decorative), `loading="lazy"` below the fold
    and the hero preloaded; video is click-to-play or muted loop with a poster
    and captions (`references/assets/video-rules.md`).

## Parallel Section Generation

If the runtime can spawn sub-agents, each may write one section's markup and
scoped CSS from its Section specification entry, wireframe box, resolved slot
and interaction decision. The parent assembles source in plan order, owns
page-wide `theme_css`, compiles once, and creates the draft. Sub-agents never
compile, never edit shared CSS, never change copy, and never spend credits.
Without sub-agents, write the sections sequentially.

## Compile and Create the Draft

Compile the rough complete source, CSS, head, scripts, and bindings early. The
compiler is the authoritative compatibility check.

1. Use `validation_errors` as the work list.
2. Fetch a full island schema only for an island named by an error or when a
   required behavior remains unclear.
3. Fix the source while preserving the planned composition and the copy.
4. Recompile until blocking errors are clear.
5. Retain the exact clean response and input hashes as compile evidence.

Create with the exact clean compile ID and creation metadata using
`lexsis_page_create.create` with `publish:false`. Record page ID, version,
preview URL, input hashes, compile bundle hash, `status: draft_created`,
`design.status: pending-approval`, and `qa.status: pending`.
Do not send source, head, CSS or scripts alongside `compile_id`; the
mutually exclusive input modes are in `references/source-artifact-workflow.md`.

If the compile ID expires, recompile the same unchanged inputs once. If the
page record already contains a page ID, do not spend another creation credit:
fetch its current version and edit it under Existing Page Edits.

Return the hosted preview immediately as `DRAFT_CREATED`. A failed later
review never erases or conceals the working draft.

## Hosted Design Review

Always required before `DESIGN_APPROVED`. Use the hosted preview at 390px,
768px and 1280px. Review the persisted source against the house, copy, proof
and offer rules, then check real renderer output for fonts, media, hydration,
overflow, clipping, hierarchy, usable responsive layout and working commerce
(`references/qa-recipe.md`).

Design questions, one line each from the 390 and 1280 screenshots:

- Where does the eye land first? Is it the plan's bold moment? If not, what
  is stealing attention?
- How many visually distinct horizontal bands are there between navbar and
  footer? Must be 1, plus the named exception.
- Which elements would appear on any generic page of this type in this
  vertical? Name them. Change or remove at least one.
- Which accessory can be removed with no loss? Remove it.
- Do any of the tells apply: cream page + serif + terracotta accent as the
  only idea; identical cards; eyebrow caps; pills; arrows in CTAs; icon
  tiles; uniform radius; scattered motion?
- At 390: is anything clipped, is the price above 1.5 screens, are tap
  targets 48px?
- Does the 390 first screen match the type file's "Above the fold" list,
  nothing more? Is `price_above_fold` obeyed? Is there exactly one
  conversion goal on single-goal types?
- Does every proof element on screen trace to a Proof ledger row and an
  approved Claim gate row (open the press links, count the stars against the
  ledger total)?
- Does the placed copy match the Section specification, with every fit edit
  in the `## Copy edits` table?
- Is any item from `references/anti-patterns/mobile-anti-patterns.md`
  visible: stacked sticky bars over 15% of the viewport, hover-only
  controls, text under 16px, side-by-side buttons under 48px?

Commerce checks at all three viewports:

- No horizontal overflow; every image loads; the hero is a real `<img>` in
  the initial HTML.
- Native disclosures and interactive islands respond; the expected Shopify
  variant enters the cart; the cart opens as a right drawer on desktop and a
  bottom sheet on mobile; quantity and subtotal update.
- Quick Add is anchored to media top-right; sold-out variants are disabled;
  product grids keep titles, prices, media and availability after hydration
  and do not blank, flicker or shift.
- The authored header and footer appear exactly once, in source order; no
  renderer-injected shell or duplicate navigation; no console errors.

Evidence: run `lexsis_pages.integrity`, read `lexsis_pages.qa`, and save the
supported fields with `lexsis_drafts.page_record_qa`. Record results with the
hosted URL and tested version. Fix source under Existing Page Edits, then
rerun only the failed checks. Never create a replacement draft for a visual
fix.

If browser automation is unavailable, return the hosted preview URL with
`DRAFT_CREATED` and state that the hosted review remains pending. Never mark
design approval or hydration as passed without hosted evidence.

## Existing Page Edits

For a page that already has an id (a review fix, a later change request, or an
approved `/optimize` plan):

1. Read `lexsis_pages.edit_context`, then `lexsis_pages.source` or
   `lexsis_pages.section_source`. Confirm the target and current version;
   stop on unexpected version drift and reconcile from current MCP source.
2. Edit the source value MCP returned, keeping stable section ids. Compile
   the changed inputs once.
3. Write with `expected_version`: `lexsis_drafts.page_update_section` for one
   section, `lexsis_drafts.page_patch` for several; `lexsis_drafts.page_update_head`
   for title, description or fonts.
4. Read back, run `lexsis_pages.diff` and `lexsis_pages.integrity`, update
   the recorded version and hashes only after success.
5. Rerun only the failed hosted checks. Any visible change returns the design
   to `changes-pending-approval` until the review passes again.

Details and the argument shapes are in `references/page-editing.md`. Never
patch compiled output in place of editable source.

## Approval

Show:

```text
Hosted preview: [url]
Draft: [page id] version [version]
Page type: [type] ; deviations [none | list]
Plan status consumed: [PLAN_READY_FOR_DESIGN | PLAN_COMPLETE - asset tasks pending] ; PLAN_APPROVED [who, date]
Work queue: [open tasks by owner | all done]
Hosted review: 390/768/1280 [pending | passed | findings]
Commerce: [passed | findings]
Sections: [ordered list]
Interactive components: [islands]
Copy edits: [n, table appended | none]
Claims rendered: [C# ids] ; V1 substitutes: [C# ids] ; removed: [C# ids]
Proof rendered: [n ledger rows] ; dropped: [rows and why]
Offer rendered: [terms | none]
Assets: [n verified] ; generated: [slots with purposes] ; awaiting user or merchant: [slots]
Concept: [not requested | asset ids and approval]
```

On approval, set `design.status: approved`. Record only final IDs, compact
island schema evidence, presets and overrides, and source, theme,
configuration, structure, and bundle hashes in the page record. Do not store
creative explanations or tool transcripts there.

Any later visible source, CSS, copy, layout, island, or asset change returns
the design to `changes-pending-approval`.

## Return

Return the page ID, version, compile evidence, hosted preview URL, sections,
selected islands, the asset summary, and `DRAFT_CREATED`. After the hosted
review passes and the user approves the reviewed version, return
`DESIGN_APPROVED` with the page id and version; `/publish` gates on that same
version.

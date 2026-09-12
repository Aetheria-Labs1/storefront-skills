<!-- GENERATED from skills/ by scripts/build-distributions.py - DO NOT EDIT.
     storefront-skills v8.0.1; 7 skills; 50 active islands -->

# Lexsis Storefront Skills - Knowledge Base

## Workflows

---

# Skill: ab-test

> Analyze an editable Lexsis landing-page URL, plan one controlled change, build verified challenger pages, and create or evaluate a draft A/B test. Use for URL-first storefront experimentation, not ordinary page editing.

# Create or Evaluate an A/B Test

Read `references/ab-testing.md` and
`references/consumer-behavior-cro.md`.

Use the host's available browser capability to inspect the supplied URL at
desktop and mobile widths. For Lexsis state, use
`lexsis_pages.find`, `lexsis_pages.get`, `lexsis_pages.edit_context`,
`lexsis_pages.source`, `lexsis_pages.compile`, `lexsis_pages.integrity`,
`lexsis_analytics.page`, `lexsis_analytics.experiment`,
`lexsis_workspace.credits`, `lexsis_drafts.page_duplicate`,
`lexsis_drafts.page_replace`, `lexsis_drafts.page_update_section`, and
`lexsis_drafts.experiment_create`.

Use `lexsis_live_ops.publish` and `lexsis_live_ops.scale_winner` only after
explicit approval. Resolve unfamiliar or newly available start/pause arguments
through exact router/action discovery.

Follow `references/ab-testing.md`:

1. Open and visually inspect the supplied Lexsis or custom-domain URL.
2. Resolve it to an editable Lexsis page and current source.
3. Present evidence-based candidates tied to one shopper uncertainty or
   behavioral pattern, then ask what the user wants to test.
4. Write and approve one focused `ab-test-plan.md`.
5. Confirm duplicate credits.
6. Build challengers locally, using isolated sub-agents when available.
7. Compile, duplicate, apply, and verify every challenger.
8. Create the draft experiment only after variant approval.

Default to one control and one challenger. Do not use `page_variation`, do not
let sub-agents perform paid or remote writes, and do not publish or start live
traffic merely because the user approved the test plan.

Return the control URL and page id, plan path, variant source and preview
paths, remote page and blueprint ids, experiment id, current state, and
remaining activation or evaluation steps.

---

# Skill: cart

> Inspect, assign, or edit Lexsis cart profiles for a storefront page. Covers offers, shipping goals, subscriptions, responsive behavior, and scoped cart styling.

# Configure a Cart

Cart profiles are managed separately from page section HTML.

Use `lexsis_cart.get` and, when requested,
`lexsis_drafts.cart_set` and `lexsis_drafts.cart_edit`. Resolve unfamiliar
argument schemas with exact router/action discovery. An empty discovery result
is not a cart outage; the actual cart call determines availability. Do not
infer the effective cart profile from page HTML.

Resolve the target store from a page binding, an explicit saved choice, or the
unambiguous default in `work/storefront/setup/setup.json`. If it is not saved,
stop and ask the user to run `/setup`; never invoke setup automatically.

## Rules

- A page enables the cart through its supported page configuration; do not add
  DrawerShell or cart-line markup to page sections.
- Effective profile order is page assignment, campaign assignment, store
  default, then legacy fallback.
- Draft profile edits are not live until published in the Lexsis app.
- Do not invent products, prices, currencies, offers, or selling plans.

## Workflow

1. Call `lexsis_cart.get`.
   - Use `page_id` to inspect the effective profile and resolution source.
   - Use `cart_profile_id` to inspect an editable profile.
   - Use `store_id` to list profiles.
2. When requested, assign a published profile with
   `lexsis_drafts` action `cart_set`. Passing a null profile removes the page
   assignment.
3. Edit a draft with `lexsis_drafts` action `cart_edit` and a partial patch.
   Supported areas include mode, layout, rules, commerce settings, offers,
   responsive presentation, and scoped custom CSS.
4. Re-read the page with `lexsis_cart.get`.
5. Preview add-to-cart and header cart triggers on desktop and mobile.

Use Shopify product GIDs for offers. Show subscriptions only when real selling
plans exist. Cart triggers dispatch `cart:open`; they do not need a profile ID.

Custom CSS must remain scoped to the cart. External imports, remote URLs,
script escapes, and unbalanced rules are not allowed.

## Return

Report the effective profile, resolution source, draft changes, page
assignment, MCP evidence, and which actions still require review or
publication in Lexsis.

---

# Skill: design-page

> Turn an approved page plan into canonical Lexsis source and one unpublished hosted draft, run the hosted review at 390, 768 and 1280 with commerce checks, apply later edits with version protection, and return DESIGN_APPROVED. Never publishes.

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

---

# Skill: optimize

> Score an existing Lexsis page against the same page-type, design, proof, offer, asset and copy rules used to build pages, propose improvements as a strict optimization plan with real replacement copy and asset decisions, wait for approval, then apply the approved changes with version protection and hosted QA.

# Optimize a Page

`/plan-page` and `/design-page` for a page that already exists. Read the live
page, score it against the rules a new page is built to, write the same plan
blocks a new page gets (final copy, an asset decision per section, a claim
gate, a work queue), wait for approval, then apply the approved changes to the
persisted source and review the hosted draft. Never publish.

## References

| Reference | Read when |
|---|---|
| `references/plan-page.md` | always; the shared block vocabulary (Asset slots decisions, Claim gate, Work queue owners, status labels) this skill reuses |
| `references/evidence-led-cro.md`, `references/consumer-behavior-cro.md` | ordering evidence and forming one behavioural hypothesis |
| the matching section of `references/industry-cro.md` | when the vertical is known |
| `references/page-types/_index.md`, then the type file | scoring the page against its type contract (Above the fold, Proof, Offer and CTA, Imagery, Copy, Never, Checklist) |
| `references/design-rules.md` | scoring N1 to N14 and A1 to A12 |
| `references/proof/proof-ledger.md`, `references/offers/offer-ledger.md` | reconstructing the ledgers from what the page shows |
| `references/workflows/section-asset-workflow.md` section 2 | the fit review of every image on the page |
| `references/copy/headline-and-cta-rules.md`, `references/anti-patterns/copy-anti-patterns.md` | scoring copy |
| `references/anti-patterns/mobile-anti-patterns.md`, `references/anti-patterns/cro-anti-patterns.md` | scoring mobile and CRO tells |
| `references/assets/generation-policy.md` | before proposing any generated or composited asset |
| `references/page-editing.md`, `references/qa-recipe.md`, `references/source-artifact-workflow.md` | applying approved changes and reviewing the hosted draft |
| `references/authoring/css-and-styling.md`, `references/animation-system.md` | before any CSS, class or motion change |
| `references/lexsis-design-capabilities.md` | optional deeper design guidance |

Use `lexsis_pages.edit_context`, `lexsis_pages.get`, `lexsis_pages.inspect`,
`lexsis_pages.source`, `lexsis_pages.section_source`, `lexsis_pages.compile`,
`lexsis_pages.integrity`, `lexsis_pages.diff`, `lexsis_pages.qa`,
`lexsis_analytics.page`, `lexsis_analytics.timeseries`,
`lexsis_analytics.attribution`, `lexsis_catalog.get`, `lexsis_catalog.reviews`,
`lexsis_assets.view`, `lexsis_asset_library.search`,
`lexsis_asset_import.import`, `lexsis_asset_upload.upload`,
`lexsis_workspace.credits`, `lexsis_drafts.asset_generate`,
`lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`,
`lexsis_drafts.page_update_section`, `lexsis_drafts.page_patch`, and
`lexsis_drafts.page_record_qa`. Resolve only unfamiliar schemas through exact
router/action discovery. A zero-result directory lookup does not make page or
analytics data unavailable. If the actual live read fails, state that
limitation; generic CRO guidance is not a substitute for live evidence.

## Confirm the Objective

Start by confirming:

1. Target outcome: conversion, add-to-cart, AOV, bounce, trust, mobile UX,
   speed, or SEO.
2. Target page, audience, and traffic source.
3. Diagnosis only, or permission to edit after approval.
4. Copy, sections, SEO fields, or offers that must remain unchanged.

Do not edit until the objective and scope are clear. Confirm the page's
workspace, store and theme binding from saved setup or current MCP context;
if it is missing, stop with `Run /setup for this store and theme first.` Never
run setup automatically.

## Read the Live Page

1. `lexsis_pages.edit_context`, then `lexsis_pages.get`, `lexsis_pages.inspect`
   and `lexsis_pages.source`: current version, section order, islands, copy,
   media, head.
2. `lexsis_analytics.page`, `.timeseries`, `.attribution` for the outcome
   window: conversion, bounce, device split, drop-off by section, traffic
   source. Analytics and observed behaviour outrank generic patterns.
3. The host browser at 390, 768 and 1280: screenshots, first screen, sticky
   elements, hydration, console.
4. `lexsis_assets.view` on every image the page shows: identity, job, crop,
   baked-in text or watermark, set consistency. A filename is never evidence.
5. `lexsis_catalog.get` and `lexsis_catalog.reviews` for the products and
   proof the page claims.
6. Identify the page type from the live structure and the brief with
   `references/page-types/_index.md`; load only that type file.

## Score

Write the scorecard first. Every row cites the rule source and the finding.

```markdown
## Scorecard

| Area | Rule source | Result | Blocking findings | Notes |
|---|---|---|---|---|
| Page type contract | <type>.md checklist, Above the fold | 7/10 | price below 1.5 screens at 390 (A8) | |
| House rules | design-rules N1-N14, A1-A12 | 11/14 | N2 band in benefits, N1 emoji in trust strip | |
| Proof | proof-ledger per-kind table | 2 verified / 3 unledgered | "50,000 customers" has no source | |
| Offer | offer-ledger rules 1-6 | ... | compare-at without basis (O2) | |
| Assets | section-asset-workflow section 2 | 5 pass / 2 fail | hero carries a baked-in ad headline -> reference-only | |
| Copy | copy-frameworks CF5, headline HC rules, copy blacklist | ... | h1 14 words; "seamless" x3 | |
| Mobile | mobile-anti-patterns | ... | sticky bars 22% of viewport | |
| CRO anti-patterns | cro-anti-patterns | ... | | |
| Analytics | evidence-led-cro | CVR, bounce, device split, drop-off section | | |
```

Proof and offer findings block; type deviations and copy findings are review
notes unless the page's own plan recorded them. Use
`references/consumer-behavior-cro.md` to name the visitor mode, the top
unanswered decision question, and the smallest behavioural hypothesis.

## Findings by Section

One entry per section, in page order, with the same copy fields
`/plan-page` uses so the replacement text is final, not a brief.

```markdown
## Findings by section

### S3. benefits - keep | improve | replace | remove | test

**Finding.** three icon tiles on a tinted band; no image of the product in use
**Evidence.** screenshot 390 and 1280; N2, N3; drop-off 38% at this section (analytics)
**Rule.** design-rules N2, N3; <type>.md Imagery
**Proposed change.** rebuild around one in-use image per benefit
**Copy.** (only when copy changes)
- Eyebrow: <text or none>
- Headline: <text, at most 10 words, sentence case>
- Subhead: <text, at most 20 words, or none>
- Body: <paragraph(s), at most 45 words each>
- Labels / bullets: <exact strings, or none>
- CTA: "<verb + object>" -> <destination>
**Claims in this section.** <C# ids> or none
**Layout.** 1280: ... | 390: ...
**Interaction.** none | <behaviour and decision inputs>; no island names or props
**Asset.** <slot id: decision state> | none-required: <why>
```

Protect the primary-product decision and any element the user listed as
unchanged. Do not force template comparison for copy-only, offer-only,
metadata or minor visual changes; for a structural redesign, compare the
current structure with relevant page kits and sections
(`lexsis_template_library.search_page_kits`, `search_sections`).

## Asset Plan

Write the `## Asset slots` table exactly as `/plan-page` defines it
(`references/plan-page.md`): one row per media slot on the proposed page with
a decision from `reuse-selected`, `shopify-product-media`,
`user-selection-required`, `user-upload-required`, `generate-required`,
`composite-required`; `none-required` on a section's `Asset` line; a current
image that fails the fit review or carries baked-in copy is `reference-only`
with its replacement slot named.

```markdown
## Asset slots

| Slot | Section | Role/purpose | Aspect | Decision | Source decision | Id / URL | Status |
```

An existing image that passes the fit review is `reuse-selected` with its
current id. Add `## User selection` when a role has more than one fit
candidate and `## Generation briefs` for every generate-required or
composite-required slot, in the shapes `/plan-page` defines. Generation obeys
`references/assets/generation-policy.md`; this skill spends no credits before
approval.

## Claim Gate

Write the `## Claim gate` table exactly as `/plan-page` defines it: one row per
claim currently on the page and per proposed claim, gated
`approved evidence available`, `merchant evidence required` or
`remove from V1`, with the ledger row or the V1 copy that ships without it.

```markdown
## Claim gate

| # | Claim (verbatim) | Where | Gate | Evidence | V1 copy if not approved |
```

A claim on the live page with no evidence is a blocking finding: it is
gated `remove from V1` or `merchant evidence required`, never left as is.

## Work Queue

Write the `## Work queue` table with the owners `/plan-page` defines (`user`,
`agent`, `merchant`, `blocked-by-evidence`). Tasks include every approved
change, every pending asset, every open claim, the apply step, the hosted
review, and any `/ab-test` hand-off.

```markdown
## Work queue

| # | Task | Owner | Section / slot | Unblocks | Status |
```

## Approval

Present the Scorecard, Findings by section, Asset slots, Claim gate, Work
queue, the protected elements, and the measurement:

```text
Outcome:
Evidence:
Main friction:
Visitor mode:
Behavioral hypothesis:
Scorecard: <blocking findings n / notes m>
Changes: <keep k / improve i / replace r / remove d / test t>
Asset slots: <n verified / m planned> ; decisions: <counts per state>
Claim gate: <n approved / m merchant evidence required / k removed>
Work queue: <n open: u user / a agent / m merchant / b blocked>
Protected elements:
Expected measurement:
Experiment recommended: yes/no
Status: OPTIMIZATION_PLAN_READY | BLOCKED - evidence required
```

Return `OPTIMIZATION_PLAN_READY`, or `BLOCKED - evidence required` when any
open task is `blocked-by-evidence`. Wait for explicit approval; record
`PLAN_APPROVED <who> <date>` when granted. Nothing is edited before that.

## Apply Approved Changes

Run `/design-page`'s Existing Page Edits and Hosted Design Review procedures:

1. `lexsis_pages.edit_context`, then `lexsis_pages.source` or
   `lexsis_pages.section_source`; stop on unexpected version drift.
2. Resolve the approved asset decisions first: `lexsis_asset_library.search`
   and `lexsis_assets.view` for reuse, `lexsis_asset_upload.upload` or
   `lexsis_asset_import.import` for supplied files, `lexsis_workspace.credits`
   then `lexsis_drafts.asset_generate` per brief after the user confirms the
   batch. View every asset before it enters the source.
3. Edit the source MCP returned, place the approved copy verbatim, compile
   the changed inputs once with any page-wide `theme_css`.
4. Write with `expected_version`: `lexsis_drafts.page_update_section` for one
   section, `lexsis_drafts.page_patch` for several.
5. `lexsis_pages.diff` and `lexsis_pages.integrity`; update recorded version
   and hashes only after success.
6. Hosted review at 390, 768 and 1280 with the commerce checks in
   `references/qa-recipe.md`; save evidence with `lexsis_drafts.page_record_qa`.
   Fix in place with another versioned patch; never a replacement page.

Preserve the URL and SEO fields unless the user approved changing them. Never
edit compiled output in place of source. Return `DESIGN_APPROVED` for the new
version once the hosted review passes and the user approves it; `/publish`
gates on that version.

## Experiment Handoff

When the value of a change is uncertain and traffic supports measurement,
return a focused hypothesis for `/ab-test` instead of presenting the change
as proven.

## Return

Return the approved objective, the scorecard totals, changed sections, page
version, verification results, MCP evidence, whether an experiment is
recommended, and the state: `OPTIMIZATION_PLAN_READY` or `DESIGN_APPROVED`.

---

# Skill: plan-page

> Produce the complete, execution-ready specification for one storefront page, covering strategy, final section copy, a resolved asset decision for every section, claim and proof gates, an ordered work queue with owners, and a plan status. Waits for explicit approval before design. Does not choose islands or implementation.

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

---

# Skill: publish

> Publish a Lexsis storefront draft version that carries DESIGN_APPROVED from /design-page or /optimize. Use only when the user explicitly asks to release a specific page version.

# Publish a Page

Publishing is a separate, explicit action. Do not rebuild the page here.

Read `references/workflow-intent.md`. Intent inference may distinguish a draft
request from a live-release request, but it never substitutes for explicit
approval naming the page and version. A request to preview, create, finish,
review, or approve a design is not publication approval.

Use `lexsis_pages.edit_context`, `lexsis_pages.integrity`,
`lexsis_pages.source`, `lexsis_workspace.get`, and
`lexsis_live_ops.publish`. Resolve unfamiliar argument schemas with exact
router/action discovery. Do not use a prose query for these known actions. An
empty discovery result is not a publishing outage; the actual context,
entitlement, or publish call determines availability. A local QA report cannot
authorize or substitute for a successful live publish.

## Gate

1. Read the page's operation record and hosted QA evidence under
   `references/source-artifact-workflow.md`.
2. Confirm the saved store/theme binding still exists.
3. Confirm reviewed source, bundle and section hashes match the persisted
   draft and recorded baseline.
4. Read `lexsis_pages` action `edit_context`.
5. Confirm the remote version equals `remote.lastKnownVersion`.
6. Confirm `DESIGN_APPROVED` was recorded by `/design-page` or `/optimize` for
   this same page version and reviewed bundle, with hosted QA at 390, 768 and
   1280 and commerce, copy, claims, assets and integrity checks passed.
7. Re-read integrity and source/bundle evidence through MCP. Missing or stale
   evidence blocks release; no local file or validator substitutes for it.
8. Confirm the store has the required entitlement.
9. Ask for explicit approval naming the page and version.

Only then call:

```text
lexsis_live_ops({ action: "publish", args: { page_id } })
```

Do not treat draft creation or a preview request as publishing approval.

## Other Lifecycle Actions

Use `lexsis_live_ops` for unpublish or rollback only when the user explicitly
requests that action and the target page/version is clear.

## Return

Report the published page, version, public URL, and whether the previous live
version remains available for rollback. Include the MCP capability and action
evidence.

---

# Skill: setup

> Connect one or more Lexsis storefront workspaces and save reusable brand and theme design context per workspace, store and theme. Run once initially, then to add, switch or refresh a workspace, store or theme.

# Set Up Lexsis

Run this once after installing the Lexsis MCP and skills. It saves the
slow-changing context that page skills reuse; it does not create or edit pages.

Use exact action slots for setup: `lexsis_workspace.list`,
`lexsis_workspace.stores`, `lexsis_brand.context`,
`lexsis_brand.brand_kit`, `lexsis_brand.list_themes`,
`lexsis_brand.get_theme`, `lexsis_brand.navigation`, and
`lexsis_design.guide`. When an input schema is unfamiliar, call
`lexsis_discover` with its exact `router` and `action`. Never use a prose query
for these known actions. An empty discovery result is not a connection
failure; the real domain call determines whether the operation is available.

## What to Save

1. Resolve only unfamiliar schemas through exact router/action discovery.
2. Call `lexsis_workspace.list` for every authorized workspace, then
   `lexsis_workspace.stores` per workspace for its connected stores, then
   `lexsis_brand.list_themes` per store. An agency or multi-brand account
   commonly has several workspaces, each with its own stores and themes.
3. Show the tree by name, never raw ids, and ask which workspaces, stores and
   themes to save and which of each should be the default. Saving one
   workspace now does not prevent adding another later. When only one
   workspace, store or theme exists, save it and say so instead of asking.
4. For each selected store, read the brand kit, design guide, voice, and
   navigation. For each selected theme, read its exact theme CSS.
5. Write one file per saved artefact, namespaced by workspace so two
   workspaces can hold a store with the same name:

```text
work/storefront/setup/
+-- setup.json
+-- workspaces/
    +-- <workspace-id>/
        +-- stores/
            +-- <store-id>/
                +-- brand-design.md
                +-- themes/
                    +-- <theme-id>.css
```

`setup.json` indexes every saved workspace, store and theme, and names one
default at each level:

```json
{
  "schemaVersion": 2,
  "defaultWorkspaceId": "...",
  "workspaces": [
    {
      "workspaceId": "...",
      "workspaceName": "Acme Brands",
      "defaultStoreId": "...",
      "defaultThemeId": "...",
      "stores": [
        {
          "storeId": "...",
          "storeName": "Main Store",
          "storeDomain": "acme.myshopify.com",
          "brandDesignPath": "workspaces/<workspace-id>/stores/<store-id>/brand-design.md",
          "themes": [
            {
              "themeId": "...",
              "themeName": "Light",
              "themeCssPath": "workspaces/<workspace-id>/stores/<store-id>/themes/<theme-id>.css"
            }
          ]
        }
      ]
    }
  ]
}
```

Rules for the index:

- `defaultWorkspaceId` names a saved workspace; each workspace's
  `defaultStoreId` names one of its own stores and `defaultThemeId` one of
  that store's themes. A default never points across workspaces.
- Paths are relative to `setup.json` and unique per workspace, store and
  theme. Adding a theme never overwrites another theme's CSS, another store's
  design file, or another workspace's tree.
- Schema 1 (a single flat `workspaceId` with `stores[]` at the root) is still
  readable. When a schema-1 file is found and the user adds a second
  workspace, migrate it: move `stores/` under
  `workspaces/<workspace-id>/stores/`, wrap the existing entry in
  `workspaces[]`, set `schemaVersion: 2` and `defaultWorkspaceId`, and update
  every `brandDesignPath` and `themeCssPath`. Say that the migration happened.

## Switching Workspace, Store or Theme

A page binds exactly one workspace, store and theme, recorded in its manifest
as `workspaceId`, `storeId` and `themeId`, and it never silently changes.

- When the user names a workspace, store or theme, resolve it by name from
  `setup.json` and use it. An ambiguous name (the same store name in two
  workspaces) is disambiguated by asking, showing the workspace for each.
- When the user names nothing, use the defaults, and state which workspace,
  store and theme are in effect in one line so a wrong default is visible
  immediately.
- Switching mid-campaign is a new binding, not an edit: a page already bound
  to one store keeps that binding, and a page for the other store belongs to
  its own campaign/page decision record. Never combine design
  files or theme CSS from two themes, stores or workspaces on one page.
- `/setup` can be re-run to add a workspace, store or theme, or to change a
  default, without touching what is already saved.

## Reuse

If a requested workspace, store or theme is already saved, reuse it. Refresh
only when the user asks, adds one, or Lexsis reports that the saved binding is
no longer valid.

Do not cache changing commerce or operational data. Page skills still read
current products, variants, prices, assets, island schemas, permissions,
credits, analytics, and remote page versions from Lexsis.

Never save credentials, cookies, authorization headers, or tokens.

## Return

Return the setup path, the saved tree as workspace then store then theme names,
the default at each level, MCP status, discovered capabilities, actions called,
fallbacks, and blockers. Say whether a schema-1 file was migrated. Other skills
read this setup independently and never invoke `/setup` automatically.

---

## Reference Knowledge

---

# Storefront craft

Start with `references/workflows/_how-to-read.md`, then `references/authoring/source-authoring.md` and `references/authoring/css-and-styling.md`. House rules in `storefront-engine/references/design-rules.md` govern every design decision. `references/source-artifact-workflow.md` owns artifact synchronization; the compiler owns acceptance of source.

---

# Managed Motion  -  Storefront Agent Reference

House motion requirements are defined in `references/design-rules.md` N10.
Choose at most the plan-named moment or a response to a shopper action;
this reference owns the managed runtime APIs, not another motion budget.

Lexsis supports open-ended custom animation without requiring a named scene or
a custom island for every visual idea. Agents author the composition; the MCP
compiler and renderer own capability validation, resource loading, lifecycle,
cleanup, reduced motion, and performance limits.

## Choose the lightest valid approach

| Need | Use |
|---|---|
| Hover or focus feedback | CSS color or border transition |
| The approved single motion moment | A managed module with explicit capabilities |
| Custom timeline or interaction | Managed motion with WAAPI or GSAP |
| Procedural drawing | Managed Canvas 2D |
| Custom shaders | Managed WebGL |
| Interactive 3D product or environment | Managed Three.js |
| Supplied vector/state-machine animation | Managed Lottie or Rive |
| Reusable stateful commerce/UI behavior | An island |

Do not create an island solely to hold a one-off timeline, shader, particle
field, 3D object, or scroll composition.

## Source contract

Place the motion block in the same source section as its markup:

```html
<!-- section: product-hero-object -->
<section id="product-hero-object" class="product-object">
  <canvas class="product-canvas" aria-label="Interactive product view"></canvas>
  <img
    class="product-fallback"
    src="https://cdn.example.com/product-static.webp"
    alt="Product front view"
  >
</section>

<script
  type="application/lexsis-motion"
  data-motion-id="product-hero-object"
  data-capabilities="three resize"
  data-mode="interaction"
  data-importance="decorative"
  data-reduced-motion="static"
>
async ({ dom, three, resize, scheduler, quality }) => {
  // Agent-authored motion.
}
</script>
```

The script body must be one function expression. The MCP compiler extracts it
into `section.motion[]`; never hand-write that compiled representation.

### Module attributes

| Attribute | Values | Meaning |
|---|---|---|
| `data-motion-id` | Unique identifier | Runtime diagnostics and source round-trip |
| `data-capabilities` | Space/comma-separated capabilities | APIs granted to the module |
| `data-mode` | `entrance`, `interaction`, `scroll`, `continuous` | Execution pattern |
| `data-importance` | `essential`, `decorative` | Whether motion carries required meaning |
| `data-reduced-motion` | `static`, `simplified` | Reduced-motion behavior |

Defaults are `entrance`, `decorative`, and `static`. Capabilities are never
inferred as permission: declare every capability the code uses.

## Runtime APIs

Always available:

- `root`
- `dom.query()`, `dom.queryAll()`, `dom.on()`, `dom.create()`, `dom.append()`
- `scheduler.frame()`, `scheduler.loop()`, `scheduler.timeout()`,
  `scheduler.interval()`, `scheduler.addCleanup()`
- `quality.tier`, `quality.dpr`, `quality.fps`
- `preferences.reducedMotion`, `saveData`, `colorScheme`, `contrast`
- `assets.url()`, `assets.json()`, `assets.image()`

Declared capabilities:

| Capability | Runtime API |
|---|---|
| `waapi` | `waapi.animate()` |
| `svg` | `svg.create()`, `svg.set()` |
| `gsap` | `gsap.load()`, `gsap.withContext()` |
| `scroll` | `scroll.on()`, `scroll.progress()` |
| `pointer` | `pointer.onMove()`, `onEnter()`, `onLeave()` |
| `resize` | `resize.observe()` |
| `visibility` | `visibility.observe()` |
| `canvas` | `canvas.context2d()`, `canvas.fit()` |
| `webgl` | `webgl.context()` |
| `three` | `three.load()` |
| `lottie` | `assets.lottie.mount()` |
| `rive` | `assets.rive.mount()` |
| `video` | `media.source()` |
| `events` | `events.on()`, `events.emit()` |

Undeclared capability APIs are removed from the runtime context.

## Scroll reveal with WAAPI

Content stays visible by default. The running animation supplies the temporary
starting state, preventing a failed module from leaving a blank section.

```html
<script
  type="application/lexsis-motion"
  data-motion-id="material-reveal"
  data-capabilities="visibility waapi"
  data-mode="scroll"
  data-reduced-motion="static"
>
({ dom, visibility, waapi }) => {
  const cards = dom.queryAll(".material-card");
  const observer = visibility.observe(cards, (entries, instance) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      waapi.animate(entry.target, [
        { opacity: 0.25, transform: "translateY(28px)" },
        { opacity: 1, transform: "translateY(0)" }
      ], {
        duration: 650,
        easing: "cubic-bezier(.16,1,.3,1)",
        fill: "both"
      });
      instance.unobserve(entry.target);
    });
  }, { threshold: 0.2 });

  return () => observer.disconnect();
}
</script>
```

## Three.js

Do not add Three.js through `scripts[]` or a CDN. `three.load()` lazy-loads the
renderer-owned package and reserves one managed WebGL context.

```html
<script
  type="application/lexsis-motion"
  data-motion-id="faceted-product"
  data-capabilities="three resize"
  data-mode="interaction"
  data-importance="decorative"
  data-reduced-motion="static"
>
async ({ dom, three, resize, scheduler, quality }) => {
  const THREE = await three.load();
  const canvas = dom.query(".product-canvas");
  if (!canvas) return;

  const renderer = new THREE.WebGLRenderer({
    canvas,
    alpha: true,
    antialias: quality.tier !== "low"
  });
  renderer.setPixelRatio(quality.dpr);

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(32, 1, 0.1, 100);
  camera.position.z = 7;

  const geometry = new THREE.IcosahedronGeometry(1.4, 2);
  const material = new THREE.MeshPhysicalMaterial({
    color: 0x111111,
    roughness: 0.18,
    clearcoat: 1
  });
  const object = new THREE.Mesh(geometry, material);
  scene.add(object);
  scene.add(new THREE.HemisphereLight(0xffffff, 0x222222, 3));

  const fit = () => {
    const rect = canvas.getBoundingClientRect();
    renderer.setSize(Math.max(1, rect.width), Math.max(1, rect.height), false);
    camera.aspect = rect.width / Math.max(1, rect.height);
    camera.updateProjectionMatrix();
  };
  fit();
  resize.observe(canvas, fit);

  const stopLoop = scheduler.loop(() => {
    object.rotation.y += 0.004;
    renderer.render(scene, camera);
  }, { fps: quality.fps });

  return () => {
    stopLoop();
    renderer.forceContextLoss();
    renderer.dispose();
    geometry.dispose();
    material.dispose();
  };
}
</script>
```

For drag rotation, use `dom.on()` for `pointerdown`, `pointermove`,
`pointerup`, and `pointercancel` on the canvas. Use pointer capture. Keep
vertical tilt bounded and let horizontal rotation wrap when a full revolve is
appropriate.

## Raw WebGL

Use raw WebGL when the design needs a custom shader rather than a Three.js
scene:

```html
<script
  type="application/lexsis-motion"
  data-motion-id="custom-shader"
  data-capabilities="webgl resize"
  data-mode="continuous"
  data-reduced-motion="simplified"
>
({ webgl, resize, scheduler, quality }) => {
  const surface = webgl.context(".shader-canvas", { version: 2, alpha: true });
  resize.observe(surface.canvas, surface.fit);

  const stopLoop = scheduler.loop((time) => {
    const { context } = surface;
    surface.fit();
    context.clearColor(0.08, 0.03, 0.06 + Math.sin(time * 0.001) * 0.02, 1);
    context.clear(context.COLOR_BUFFER_BIT);
  }, { fps: quality.fps });

  return () => stopLoop();
}
</script>
```

Agent-authored shader compilation, buffers, uniforms, textures, and drawing
remain inside the module. The runtime owns context limits, pause/resume, and
context loss during cleanup.

## GSAP

Do not add GSAP through page scripts. The managed loader uses pinned
first-party assets with a bounded fallback.

```html
<script
  type="application/lexsis-motion"
  data-motion-id="hero-timeline"
  data-capabilities="gsap"
  data-mode="entrance"
  data-reduced-motion="simplified"
>
async ({ gsap }) => {
  return gsap.withContext((runtime) => {
    const timeline = runtime.timeline();
    timeline
      .from(".hero-title", { opacity: 0, y: 34, duration: 0.8 })
      .from(".hero-copy", { opacity: 0, y: 16, duration: 0.5 }, "-=0.35");
    return () => timeline.kill();
  });
}
</script>
```

`gsap.withContext()` scopes selectors, reverts the timeline on cleanup, and
pauses managed animations while the section is offscreen.

## Canvas 2D

Use `canvas.context2d()` and `surface.fit()` so the renderer applies the
device-quality DPR cap. Put related drawing in one `scheduler.loop()` rather
than starting one loop per particle or object.

## Motion assets

Declare every remote resource on section markup with an absolute HTTPS URL:

```html
<div
  data-motion-asset="gift-reveal"
  data-src="https://cdn.example.com/gift-reveal.json"
  hidden
></div>
```

Then load only by declared name:

```javascript
({ assets }) => assets.json("gift-reveal")
```

Use `assets.image`, `assets.lottie.mount`, `assets.rive.mount`, or
`media.source` as appropriate. Arbitrary `fetch()` is rejected.

## Progressive enhancement

- Keep meaningful copy, images, SVG, and controls present in static HTML.
- Keep content visible by default.
- Do not make an empty fixed-height canvas the only representation of
  essential content.
- Hide a static visual fallback only after the module reports ready.
- Use `data-reduced-motion="static"` when the fallback communicates the same
  information.
- Never delay pricing, variants, CTA availability, cart state, or trust
  evidence behind animation.

If a module fails or exceeds a boundary, Lexsis disables that module and keeps
the static section usable.

## Compiler and runtime boundaries

- Motion source: at most 100 KiB per page.
- Managed loops: at most 2 per section and 4 per page.
- WebGL/Three modules: at most 2 per page.
- Device tiers cap DPR at 1, 1.5, or 2 and fps at 30, 45, or 60.
- Offscreen and hidden sections pause managed work.
- Repeated callbacks over 50 ms disable only the offending module.
- Mutation storms, excessive DOM growth, and event-loop stalls disable only
  the offending module.
- Section replacement and page exit clean up listeners, observers, timers,
  loops, engine contexts, and loaded media.

The compiler rejects:

- `window`, `document`, and global browser escape hatches
- `fetch`, WebSockets, workers, and browser storage
- raw timers, animation frames, and observers
- dynamic imports and dynamic code execution
- programmatic `.click()`
- island-internal access
- unbounded loops
- use of undeclared capabilities

Use the managed context equivalents.

## MCP compile workflow

1. Author the source section and motion block in `MCP source`.
2. Call `lexsis_pages` action `compile` with complete source, head, theme CSS,
   and approved page scripts.
3. Fix every `motion_*`, `unmanaged_*`, or capability error.
4. Confirm the returned animation manifest reflects the expected engines,
   capabilities, continuous motion, and performance tier.
5. Create or update the unpublished draft only after compilation is clean.
6. Verify the hosted draft at desktop and mobile widths. A successful compile
   proves contract safety, not visual quality.

The MCP round-trips managed motion through source reads, section patches, page
bundles, and versioned drafts.

---

# Design Rules

House rules for every generated page. They override generated brand `design.md`
guidance and brand-kit preview blueprints. Record every override in
`page plan` under "Overrides of brand design.md".

Loaded by `/plan-page` (Design direction block), `/design-page` (Design Direction
Gate and hosted review) and `/optimize` (Scorecard).
Review the persisted MCP source and hosted draft. No local QA script or
page-file workflow is required.

## Precedence

```text
house rules (storefront-engine/references/design-rules.md)
  > merchant-stated brand rules (voice_md, banned_phrases, explicit owner notes in brand-design.md)
    > brand-kit token VALUES (colours, fonts, radii, spacing)
      > generated design.md guidance (intent, component patterns, do/don't)
        > brand-kit preview blueprint and island presets (illustrative only)
```

Rules for applying it:

1. A lower layer may narrow a higher layer (pick one of the allowed icon sets) but never widen it (re-enable emoji).
2. Token values win over design.md prose for values, except where the value fails WCAG AA against its documented pairing; then return `THEME_CONTEXT_CONFLICT` with both values. Conflicts are raised for values only, never for style guidance.
3. "Mandated by the brand guide" (the ALL-CAPS exception in N5) means merchant-stated only. Anything the generator inferred from screenshots is tagged `[observed]` and cannot unlock an exception.

## 2. Design rules for generated storefront pages

Format per rule: imperative sentence, rationale and hosted/MCP acceptance
check. Inspect the persisted source through MCP and the actual hosted DOM,
styles and interactions; never inject diagnostic code into section source.

### 2.1 NEVER

N1. Never use emoji by default, and never as icons: not in tickers, trust strips, badges, buttons, alt text, island JSON props or CSS `content`. Emoji may appear in copy only when the user explicitly insists; record it in `page plan` under "Design direction > Emoji in copy" with the merchant's wording, and keep every occurrence inside running text. When the page needs icons and no inline SVG set fits, generate a monochrome SVG icon set (one stroke, one size); never substitute emoji.
Rationale: glyphs render differently per OS vendor, ignore `currentColor` and stroke weight, are announced by Unicode name to screen readers, and are the most recognised marker of AI-generated pages (Miller et al. 2018; uxskill).
Check (hosted/MCP): Inspect visible copy, alt text, props and CSS content for emoji. None may be icons; any copy-only exception must match the merchant's recorded wording.

N2. Never change the background from section to section. The page has one background, `--lx-bg-color`, from below the navbar to above the footer. Allowed exceptions, exhaustively: the announcement bar, the navbar, the footer, and at most one full-bleed moment that `page plan` names under "Design direction > Bold moment". A `<section>` or any full-width wrapper painted `--lx-bg-surface`, `--lx-surface-alt` or `--lx-secondary-color` is a band and fails, even if it is white.
Rationale: bands are a template's way of faking structure; separation belongs to spacing, type scale and hairlines (NN/g grouping; Stellae). Alternating fills are also the reason the rejected page read as five stacked templates.
Check (hosted/MCP): At each viewport, inspect full-width backgrounds. Only chrome and the single plan-named full-bleed exception may differ from the page background.

N3. Never use emoji, images or mixed libraries as icons. Icons are one inline SVG set, one stroke weight, `stroke="currentColor"`, `fill="none"`, one size per context, `aria-hidden="true"` with a visible text label. Or no icons.
Rationale: two stroke languages on one screen is a tell; icons that garnish headings are skipped by readers (uxskill icons).
Check (hosted/MCP): Inspect rendered icons and persisted markup: one SVG set, one stroke weight, currentColor, no image icons, hidden decorative SVGs and visible labels.

N4. Never use more than two type families. A non-Latin script gets one matching family declared with `[lang]`; it does not count.
Rationale: one display face plus one workhorse is the ceiling for coherence (frontend-design; Shopify Theme Store "Consistent typography").
Check (hosted/MCP): Inspect computed font families and loaded font stylesheets. At most two families plus the declared non-Latin family.

N5. Never set eyebrow labels in ALL-CAPS unless a merchant-stated brand rule (not a generator-observed one) requires it, and then at most one per three sections.
Rationale: the tracked-out caps eyebrow above every heading is the highest-frequency AI tell (designer-skill avoid-ai-slop; frontend-design).
Check (hosted/MCP): Inspect eyebrow labels. No uppercase without a merchant-stated rule; an authorized exception appears at most once per three sections.

N6. Never accent a single word or phrase inside a headline with colour, italic, weight or underline.
Rationale: the one-word accent is a default treatment, not a decision (frontend-design).
Check (hosted/MCP): Inspect each headline's child spans and computed styles. No word-level accent treatment.

N7. Never use gradient washes, glow shadows, shimmer, pulse, float, animated backgrounds, or `hover:scale` / `hover:-translate` / `hover:scale-1xx` on cards, buttons or images. The only permitted gradient is a black-to-transparent overlay on a photograph for text legibility inside the plan-named bold moment.
Rationale: gradient + hover-lift is the SaaS-card kit that reads as generated regardless of brand (Sailop; frontend-design).
Check (hosted/MCP): Inspect source and rendered effects at rest and on hover. No banned effects; only the plan-named photographic legibility overlay may use a gradient.

N8. Never wrap plain text in a card. A card (`--lx-bg-surface`, border, or shadow with radius) surrounds a distinct object only: a product, a proof artefact with an image, a table, a form, a quoted review. Paragraphs, lists and FAQs sit on the page background.
Rationale: identical rounded cards chop content into interchangeable units and signal that nothing is more important than anything else (uxskill tells; NN/g common region "use sparingly").
Check (hosted/MCP): At desktop and mobile, count cards containing only paragraphs/lists/FAQs: zero. Every card surrounds a permitted distinct object.

N9. Never render discount or status pills in ALL-CAPS or with percentages ("31% OFF", "BEST VALUE", "MOST POPULAR", "NEW ARRIVALS") unless the merchant runs a named sale recorded in the plan's confirmed claims. Compare-at price is struck-through text only.
Rationale: the OFF pill and the highlighted middle tier are stock conversion-template chrome; Baymard's guidance is to show the price and compare-at clearly, not to shout.
Check (hosted/MCP): Inspect offer/status treatments. No prohibited pills; any named-sale exception is evidenced in confirmed claims and prices follow the offer ledger.

N10. Never add motion that is not answering a user action, except one orchestrated moment named in the plan. No fade-up per section, no stagger, no counters, no parallax, no marquee ticker unless the announcement bar's own island provides it. Custom motion must follow `animation-system.md` and use `application/lexsis-motion`, not raw observers, timers, or global DOM access.
Rationale: scattered entrance effects are the generic default; one moment lands, ten do not (frontend-design; Sailop).
Check (hosted/MCP): Inspect motion blocks and hosted behavior with reduced motion enabled and disabled. Non-interaction motion is limited to the single plan-named moment; no raw observers, timers or global DOM recipes are authored.

N11. Never show proof you cannot source: star glyphs, review counts, customer counts, "Only N left", countdowns, "as seen in" logos. Every number in a proof section traces to "Claims confirmed" in the plan.
Rationale: fabricated proof destroys trust and is itself a tell (five gold stars + round avatar + italic quote). `references/proof/reviews-sourcing.md` owns reviewer and quotation evidence.
Check (hosted/MCP): List every visible proof numeral, count, logo and testimonial. Match each to confirmed evidence and its proof-ledger row.

N12. Never append `U+2192` or `U+00BB` to link and button text, join meta strings with middle dots, or place an icon in a rounded tile above a heading (icon-tile-stack).
Rationale: template chrome that appears whatever the subject (frontend-design; designer-skill).
Check (hosted/MCP): Inspect link/button labels and heading ornaments. No U+2192 or U+00BB suffixes, middle-dot meta chains or icon-tile headings.

N13. Never mix radii on the same object type or use one radius on everything. Declare a radius scale by object type and use only those tokens.
Rationale: uniform `rounded-2xl` on cards, buttons, inputs and images is the absence of a system (Sailop "rounded-2xl on everything").
Check (hosted/MCP): Compare computed radii by object type to the declared radius tokens; no stray values or universal radius.

N14. Never hardcode off-brand hex or Tailwind default colours. Colours come from `--lx-*` tokens or the plan's named palette.
Rationale: default colours such as `#667eea`, `#764ba2`, `#8b5cf6`, `#f9fafb`, and `text-yellow-400` mark a page as templated rather than merchant-specific (uxskill tells).
Check (hosted/MCP): Compare computed colors and source values to the selected theme and plan palette; no off-brand defaults.

### 2.2 ALWAYS

A1. Always write the Design direction block in `page plan` before any HTML: palette of 4 to 6 named hex with roles; type roles, families and one modular ratio; layout concept in one sentence plus an ASCII wireframe at 1280 and 390; alignment rule; icon decision; the one bold moment; the background rule with its single named exception or "none"; motion decision; the generic-default check with at least three concrete differences; the list of brand-design.md lines being overridden.
Rationale: the plan-review-build-critique loop is what stops the model averaging toward the centre of its training data (frontend-design).
Check (hosted/MCP): The plan contains all ten Design direction fields, with no empty or TBD value, before source authoring.

A2. Always separate sections with a spacing scale and, where a break is needed, one 1px hairline in `--lx-border-color`. Use one 8-point scale; section padding comes from at most two pairs (e.g. 64/96 and 40/56 mobile/desktop).
Rationale: proximity and whitespace carry grouping; a line is a subtle, universally understood divider; colour is emotional and should be spent on pacing, not plumbing (NN/g; Stellae; Tubik).
Check (hosted/MCP): Measure section spacing at mobile and desktop: one 8-point scale, at most two padding pairs and only the specified hairline where needed.

A3. Always build hierarchy with a single modular type scale (one ratio, 1.2 to 1.333 for commerce), no more than three sizes visible on one screen, one `<h1>`, one `<h2>` per section, headings 1.1 to 1.2 line-height, body 1.5 to 1.7.
Rationale: three sizes give hierarchy without noise; NN/g and accessibility.build converge on this.
Check (hosted/MCP): Inspect heading count, computed sizes and line heights against the declared ratio. One h1, one h2 per section and no more than three sizes per screen.

A4. Always keep body measure between 45 and 80 characters at every viewport; give serif body 0.05 more line-height than sans. Constrain text containers with `max-width` in `ch` (60 to 70ch), not px.
Rationale: WCAG 1.4.8 caps body at 80 characters; legibility research centres on 45 to 75 (Butterick 45 to 90).
Check (hosted/MCP): Inspect body measure at each viewport: 45 to 80 characters, 60 to 70ch containers, and the required serif line-height adjustment.

A5. Always record one icon decision in the plan and, if icons exist, ship them as one inline SVG set at one size and one stroke, with the text label always visible.
Rationale: see N3.
Check (hosted/MCP): Match the rendered SVG set and visible labels to the plan's icon decision and N3.

A6. Always declare a radius scale by object type in `theme_css` (`--r-control`, `--r-card`, `--r-media`, `--r-pill`) and use only those tokens.
Rationale: the relationship between radii is the design.
Check (hosted/MCP): Inspect effective theme CSS and rendered radii: every object uses its declared --r-control, --r-card, --r-media or --r-pill token.

A7. Always meet WCAG 2.2 AA: 4.5:1 for text under 24px (18.67px bold), 3:1 for large text and for UI component boundaries, including muted text on the page background, accent on any tint, and button text on button fill.
Rationale: W3C 1.4.3 and 1.4.11; the RudraSetu guide itself flags #D52600 on #FBE9E6 as borderline.
Check (hosted/MCP): Measure actual foreground/background pairs, including muted text and buttons over imagery: at least 4.5:1 for normal text and 3:1 for large text and component boundaries.

A8. Always compose the PDP buy section to Baymard and Shopify requirements: untruncated title, price and compare-at, unit price if applicable, variant options as buttons, quantity, add-to-cart, a shipping and returns line, all within the first viewport on desktop and within 1.5 viewports at 390px; product media takes 50 to 60 percent of desktop width.
Rationale: users decide on the PDP; hidden price or delivery cost is a top abandonment cause (Baymard PDP research; Shopify Theme Store product page requirements).
Check (hosted/MCP): On the hosted PDP, verify all required buying controls within one desktop viewport and 1.5 mobile viewports at 390px, with media at 50 to 60 percent of desktop width.

A9. Always spend boldness once. Name the single memorable element in the plan; every other element is quiet: page background, body weight, hairlines, sentence case.
Rationale: one element can be remembered; the mirror test, remove one accessory (frontend-design; Chanel).
Check (hosted/MCP): The desktop and mobile squint test isolates the one plan-named bold element, not several competing accessories.

A10. For production-ready work, always run the hosted design review at 390 and 1280 before recording design approval. Fast drafts return `DRAFT_CREATED` first and may leave this review pending.
Rationale: the real renderer catches banding, hierarchy, hydration, and media problems without maintaining a second preview runtime.
Check (hosted/MCP): Record hosted preview URL, tested version and screenshots at 390 and 1280 with no blocking failure before design approval.

A11. Always ship the quality floor without announcing it: `:focus-visible` styles, `prefers-reduced-motion` handling, 48px minimum tap targets, alt text on product media, `lang` attributes on non-Latin text.
Check (hosted/MCP): Test keyboard focus, reduced motion, all 48px tap targets, media alternatives and language attributes on the hosted draft.

A12. Always write copy as design content: sentence case, active voice, the CTA says what happens ("Add to cart", not "Shop Now U+2192"), no placeholder or invented copy, brand voice from `voice_md` or the merchant.
Check (hosted/MCP): Read rendered copy and controls against the plan and brand voice. No generic action labels, placeholder content or invented facts.

## Tells (fail the squint test)

Cream page + high-contrast serif + terracotta accent as the only idea; identical rounded cards with one radius and one grey shadow; tracked-out ALL-CAPS eyebrow above every heading; meta strings joined with middle dots; `WORD  -  fragment` labels; `U+2192` appended to links and buttons; icon in a rounded tile above every heading; discount pills and "MOST POPULAR" ribbons; gradient washes; fade-up on every section; five gold stars with a round avatar and an italic quote; a monospace face for small labels; near-black `#0B0B0B` standing in for black.

Source audit: internal design-rules research (2026-09-05).

---

# Island intent labels

A saved `Preset: <island>/<intent>-<tone>` label records visual intent, not a versioned prop bundle or a schema variant. Translate the intent through `references/workflows/island-selection-workflow.md` using the current schema, and record the actual decision and any deviation in the page decision record. Use `references/authoring/css-and-styling.md` for scoped CSS; there is no static prop map to paste.

---

# Compile and draft protocol

House rules in `storefront-engine/references/design-rules.md` govern the
presentation. The source contract is `references/authoring/source-authoring.md`;
`references/source-artifact-workflow.md` owns artifact and manifest state.
Choose section order from the page-type contract, not from this protocol.

## Compile exact inputs

1. Reuse the bound workspace, store and theme; read current page context for
   edits through `lexsis_pages.edit_context` and editable source through
   `lexsis_pages.source` or `lexsis_pages.section_source`.
2. Prepare complete source and any page-wide theme CSS as values, not
   mandatory files. Resolve only the interactive
   decisions through `references/workflows/island-selection-workflow.md`.
3. Call `lexsis_pages.compile` with the exact `source`, `head`, `theme_css`
   and optional `scripts` inputs. `lexsis_pages.compile_artifact` retrieves
   an existing result by `compile_id` for inspection; it does not compile.
4. Read all `validation_errors`, publish validation and missing utility
   candidates. Repair the source rather than mutating compiled JSON.
5. Save the successful response and input hashes as compile evidence.

## Create or edit one draft

Use `lexsis_page_create.create` with `compile_id` and `publish: false`
only when the workspace has no existing page id. Otherwise use the relevant
versioned draft action: `page_update_section`, `page_patch`, `page_replace`,
`page_update_head`, `page_move_section`, or `page_remove_section` on
`lexsis_drafts`, with `expected_version` when the action supports it.
On a version conflict, read the latest context and reconcile; do not overwrite
blindly. Return the hosted draft URL and exact version as `DRAFT_CREATED`.

## Review and release boundary

A clean compile is structural evidence, not a visual pass. Hosted design
review and commerce checks follow `references/qa-recipe.md`. `DRAFT_CREATED`
may leave review pending; `DESIGN_APPROVED` cannot be claimed without hosted
review evidence. Publication follows `references/publishing.md` and requires
explicit authorization. Report the exact state and do not equate draft
creation, approval, publication, and live HTTP verification.

The exact mutually exclusive creation inputs and hosted verification
are owned by `references/source-artifact-workflow.md`.

---

# HTML-native source format

House rules in `storefront-engine/references/design-rules.md` govern the
page. `references/authoring/source-authoring.md` is the authoring contract;
`references/authoring/css-and-styling.md` owns CSS. This entry point covers
only the input shape passed to the compiler.

## Page structure

Author a source string with one delimiter and matching section id per section:

```html
<!-- section: faq -->
<section id="faq" class="px-4 py-16">
  <h2>Ordering questions</h2>
  <details>
    <summary class="flex min-h-[48px] items-center">Where are the shipping terms?</summary>
    <p>Read the product's shipping policy before ordering.</p>
  </details>
</section>
```

Use actual merchant policy copy and links. An interactive section contains
`<lx-island>` with one `application/json` child copied from the schema fetched
for that decision. `hydrate` is an authored attribute; generated
`data-island` and `data-props` markers are renderer output, not source.
Supported headless hooks and fallback markup are resolved through the same
live schema, not a static hook or prop table.

## Tool inputs

Pass `source`, structured `head`, optional `scripts` and any page-wide
`theme_css` directly to `lexsis_pages.compile`; no local files are created. Follow `references/source-artifact-workflow.md`. Templates come from
`lexsis_design.get_section` as editable `source`; compiled references are
inspection artifacts only. `references/generation-protocol.md` owns repairs,
draft creation and subsequent versioned edits.

The compiler escapes storage representations. Do not escape a whole section
or construct JSON strings of HTML manually. Valid HTML entities in authored
text or attribute values remain normal HTML; they are not an escaped page.
Motion, if the plan requires it, follows `references/animation-system.md`.

---

# Storefront Workflow

Use one owning command at a time.

## Normal Page Journey

```text
/setup
  U+2192 /plan-page
  U+2192 /design-page
  U+2192 /publish
```

- Setup is normally run once and refreshed only for changed stores/themes.
- Plan produces the complete page specification: strategy, final section
  copy, an asset decision for every section, claim gate, work queue and plan
  status, without islands. It waits for explicit approval.
- Design builds the approved plan: selects islands, resolves the plan's asset
  decisions, compiles source, creates one unpublished hosted draft, runs
  hosted QA at 390, 768 and 1280 with commerce checks, applies later edits
  with version protection, and returns `DESIGN_APPROVED`.
- Publish is a separate explicit release that gates on `DESIGN_APPROVED` for
  the same version.

Commands do not silently invoke one another. When a user intentionally starts
later, recover the minimum missing decision evidence and record the skipped command.

Infer question depth and publish intent from the user's complete request and
current conversation. Approval before design and before publish is never
inferred. Intent inference never authorizes publishing, paid generation, or
deletion.

## Optional Routes

- Use `/design-page` concept-first when the user wants a mobile-first mockup
  approved before source authoring.
- Use `/optimize` for an existing page and a specific outcome: it scores the
  page, proposes a plan with the same blocks, and applies approved changes.
- Use `/ab-test` to inspect a live Lexsis URL, build controlled variants, and
  create or evaluate an experiment.
- Use `/cart` for cart profile configuration.

## Shared Safety

- Identify one page type (`references/page-types/_index.md`) before templates,
  assets or proof; its `## Workflow` guides every later stage and its checklist
  is the default anatomy.
- Render proof only from the plan's Proof ledger and offers only from its
  Offer ledger; never invent reviews, counts, logos, badges or urgency.
- Generate imagery only for ALLOW purposes in
  `references/assets/generation-policy.md`; never the product, people as
  customers, results, badges or text in images.
- Bind every page to one saved store/theme pair.
- Read changing product, price, asset, schema, permission, analytics, and
  version data live.
- Search existing assets before paid generation.
- Resolve island schemas before authoring.
- Keep production changes in source-based MCP operations and stop on version drift.
- Create drafts with `publish:false`.
- Keep concept images out of production source and asset slots.
- Publish only after current QA and explicit approval.

---

# Conversion decisions

Use `references/consumer-behavior-cro.md` to choose a shopper uncertainty and a testable response, then the selected `references/page-types/_index.md` contract for section order and `references/copy/copy-frameworks.md` for the argument. House rules in `storefront-engine/references/design-rules.md` govern the presentation; a psychological hypothesis never authorizes unverified proof or urgency.

---

# Consumer Behavior and CRO Decision Framework

Use this reference to turn shopper behavior into page decisions. It is a
hypothesis library, not a checklist. A page should usually activate two or
three relevant patterns, not every pattern below.

## Decision Protocol

Before asking the merchant or choosing a module:

1. Read the product, variants, price, inventory, existing media, reviews,
   policies, audience, traffic source, and available analytics.
2. Classify the visitor's likely primary mode:
   - **confirm**  -  knows the product and wants confidence to buy;
   - **compare**  -  deciding between options or alternatives;
   - **explore**  -  needs inspiration or use-case education;
   - **complete**  -  wants the full solution, routine, or setup;
   - **replenish**  -  returning for a refill, replacement, or repeat order.
3. Write the three most important questions the shopper must answer before
   buying.
4. Select at most three behavioral patterns that answer those questions.
5. Map each selected pattern to evidence, one page response, any required
   asset, and one primary metric.

Do not add a carousel, bundle, urgency treatment, sticky CTA, quiz, or proof
module merely because the pattern exists. Every module must reduce a named
uncertainty or decision cost.

## Merchant Questions

Inspect available evidence first. Ask only when the answer changes the page,
requires unavailable business knowledge, or spends credits. Group no more than
three questions in one turn.

Useful conditional questions include:

- **Gallery gap:** "The current media shows the pack and texture, but not scale
  or in-use context. Can you supply the real scale and
  in-use photos, or should those jobs remain pending?"
- **Relationship:** "Should the recommendation help shoppers complete the
  routine, compare alternatives, replenish later, or should this page avoid
  recommendations?"
- **Compatibility:** "Do you have a verified model, size, shade, ingredient,
  room-dimension, or usage mapping for these add-ons?"
- **Risk:** "Which verified shipping, returns, trial, warranty, cancellation,
  or guarantee terms can appear beside the purchase decision?"
- **Audience state:** "Is this primarily a first purchase, an experienced
  buyer, or a returning/replenishment visit?"
- **Traffic context:** "Which promise or creative brought this traffic here,
  if the page must preserve message match?"

Never ask "Do you want custom images?" without first identifying the missing
decision job, proposed image count, purpose, and likely placement. Paid image
generation remains separately credit-gated.

## Behavioral Pattern Library

| Pattern | Shopper signal or uncertainty | Page response | Primary measurement |
|---|---|---|---|
| Scan-first decision packet | High-intent visitor wants to verify and act quickly | Make product identity, promise, price, variants, availability, delivery/returns cue, proof summary, and primary CTA scannable in the first decision area | Add-to-cart rate, time to CTA |
| Visual investigation | Product appearance materially affects choice | Give the gallery clear next-image cues and cover product, detail, in-use, scale, variation, included items, and result/proof jobs where relevant | Gallery engagement, conversion |
| Scale, fit, and sensory confidence | Size, fit, texture, finish, shade, or quantity is hard to judge | Add dimension diagrams, familiar-object scale, model measurements, texture close-ups, swatches, or use-context imagery | Returns, fit questions, conversion |
| Information scent | Shoppers need detail but will not parse a wall of copy | Lead with benefit and decision fact, then expose specifications, ingredients, care, or methodology through clear progressive disclosure | Detail interaction, conversion |
| Choice reduction | Too many variants, bundles, or recommendations compete | Prioritize the likely default, explain differences, and keep the first recommendation set to two or three choices | Variant completion, conversion |
| Guided comparison | Visitor is deciding between products or tiers | Compare only decision-driving attributes; state "best for" and meaningful trade-offs without manufacturing a winner | Comparison interaction, product selection |
| Compatibility confidence | Add-on usefulness depends on model, shade, size, ingredient, room, or regimen fit | Show the verified fit reason beside each recommendation and suppress incompatible or unavailable items | Attach rate, support questions, returns |
| Solution completeness | The hero SKU is only one part of the shopper's job | Present the minimum complete outfit, routine, stack, recipe, room, setup, care kit, or commissioning kit with individually selectable items | Attach rate, AOV, revenue per visitor |
| Sequence and next step | Products are understood as stages or order of use | Show when, how, and in what order products are used; distinguish morning/evening, setup/use/care, or beginner/advanced | Bundle attach rate, education engagement |
| Context and mental simulation | Shopper cannot picture ownership or final use | Show the product in the actual scene, occasion, room, routine, task, or before/after context using truthful media | Context-image engagement, conversion |
| Replenishment and continuity | Consumable, maintenance item, size progression, or replacement cycle exists | Explain serving/use count, refill timing, cadence, compatible replacement, or easy reorder without inventing depletion dates | Repeat purchase, subscription opt-in |
| Returning-customer shortcut | Existing buyers need less education and more continuity | Prefer refill, reorder, saved configuration, compatible replacement, or "what changed" paths when reliable customer context exists | Repeat conversion, time to purchase |
| Proof proximity | A claim creates doubt at a specific decision point | Place sourced review excerpts, customer media, certification, test evidence, or expert proof beside the claim it supports | Proof interaction, conversion |
| Risk reversal | Delivery, fit, efficacy expectations, warranty, returns, or subscription cancellation creates hesitation | Put verified policy and guarantee language beside the relevant CTA or choice; make conditions legible | Checkout progression, support contacts |
| Price comprehension | Shopper cannot understand total value or recurring cost | Show current price, factual compare-at price, unit/cost-per-use where accurate, bundle contents, cadence, and savings calculation without deceptive anchoring | Conversion, AOV, margin |
| Effort reduction | Selecting an add-on or completing the setup requires navigation and rework | Allow inline selection, preserve the primary product choice, and avoid forcing page exits for two or three simple additions | Attach rate, abandonment |
| Commitment and ownership | Configuration increases relevance but can also create work | Use short builders, quizzes, or progress only when answers materially change the recommendation; show editable selections and a clear result | Builder completion, conversion |
| Mobile context preservation | Long scrolling hides product identity and purchase state | Keep gallery cues visible, repeat concise product context at major decision points, use short sections, and use a non-obstructive sticky CTA only when helpful | Mobile conversion, CTA usage |
| Message match | Visitor arrives from a specific ad, search, creator, or campaign promise | Repeat the same product, outcome, offer, and visual context early; do not make cold traffic reconstruct the premise | Bounce, conversion by source |
| Ethical urgency | Real stock, cutoff, launch, or event timing matters | Show only verified availability or deadlines, explain the consequence plainly, and remove stale urgency automatically | Conversion, cancellations, trust |
| Post-purchase clarity | Shopper worries about what happens after payment | Explain delivery, setup, first use, support, returns, warranty, subscription management, or expected next step | Checkout completion, support questions |
| Cognitive and performance ease | Heavy media or many modules slow comprehension or rendering | Keep one primary action per decision area, remove duplicate modules, optimize media, and preserve fast visual stability | Core Web Vitals, bounce, conversion |

## Relationship-Based Merchandising

Name the customer's job instead of using a generic "Recommended for You."
Start with two or three relevant products and show why each belongs.

| Vertical | Useful relationship names and jobs |
|---|---|
| Fashion | Complete the Look, Shop the Occasion, Three Ways to Wear It, Fit Kit, Care for This |
| Beauty | Complete Your Routine, Morning vs Evening, Solve the Concern, Shade Companion, Starter vs Refill |
| Supplements | Build Your Stack, Goal Protocol, Time-of-Day Stack, 30-Day Start, Refill the Stack |
| Food | Pair It With, Shop the Recipe, Make It a Meal, Flavor Flight, Occasion Box |
| Home | Complete the Room, Shop the Scene, Finish the Surface, Install and Protect, Match the Finish |
| Electronics | Make It Work, Compatibility Check, Protect It, Creator Kit, Replace the Consumable |
| Pet | Complete Their Care Routine, Life-Stage Bundle, Enrichment Set, Refill Reminder |
| Baby | Set Up the Station, Feeding Stage Kit, Size-Up Reminder, Daycare Pack |
| Travel | Complete the Packing System, Trip Type Kit, Destination Weather Kit, Carry-On Kit |
| B2B | Commissioning Kit, Compatible Parts, Maintenance Kit, Reorder This Set, Job-Specific Kit |

The relationship may be complementary, compatible, sequential, protective,
replenishing, substitutive, occasion-based, or an upgrade. Record which one it
is. Do not infer medical compatibility, technical compatibility, shade match,
or safety from visual similarity.

## Gallery Job Coverage

Treat the gallery as decision support. Check only jobs relevant to the product:

- identity and every included item;
- multiple angles and important detail;
- scale, dimensions, fit, or model reference;
- texture, material, finish, shade, or consistency;
- in-use context and the intended environment;
- variation across color, size, flavor, or configuration;
- installation, sequence, routine, or setup;
- sourced result, proof, or customer media.

Use `references/workflows/section-asset-workflow.md` for unresolved gallery
jobs and inspection. That procedure applies the source/generation policies;
a behavioral hypothesis does not authorize synthetic product or result media.

## Plan Handoff

Add this compact block to `page plan`:

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

`/design-page` implements this block without reopening settled choices.
`/optimize` and `/ab-test` use it to form one controlled, measurable
hypothesis.

## Guardrails

- Treat every pattern as a testable hypothesis, not a guaranteed lift.
- Protect primary-product conversion when introducing cross-sells.
- Measure attach rate, AOV or revenue per visitor, conversion, margin,
  returns/refunds, and support questions as appropriate.
- Segment meaningful results by device, traffic source, new/returning status,
  and product family when data supports it.
- Never fabricate reviews, customer counts, scarcity, compatibility, savings,
  clinical outcomes, delivery promises, or personalization.
- Avoid dark patterns: preselected paid add-ons, hidden recurring terms,
  obstructive sticky controls, fake countdowns, confirmshaming, or difficult
  opt-out.

## Evidence Foundation

This framework synthesizes merchant-provided Shopify CRO research with:

- Baymard product-page, image-gallery, description, cross-sell, and mobile UX
  research: `https://baymard.com/research/product-page`
- Shopify related and complementary recommendation guidance:
  `https://shopify.dev/docs/apps/build/product-merchandising/recommendations`
- Shopify Search & Discovery recommendation guidance:
  `https://help.shopify.com/en/manual/online-store/search-and-discovery/product-recommendations`
- Nielsen Norman Group progressive-disclosure guidance:
  `https://www.nngroup.com/articles/progressive-disclosure/`
- UK Competition and Markets Authority guidance on urgency and price-reduction
  claims: `https://www.gov.uk/government/publications/online-choice-architecture-how-digital-design-can-harm-competition-and-consumers`

---

# Island composition

Use `references/workflows/island-selection-workflow.md` to select an active island and resolve its live schema. `references/authoring/source-authoring.md` owns source markup and supported headless behavior, while `references/authoring/css-and-styling.md` owns scoped styling. Section order comes from the page-type contract, not an island combination table.

---

# Style direction

A style direction translates the merchant's palette, typography, imagery and
object-radius scale into one coherent page. It does not override
`references/design-rules.md` or supply island props.

| Direction | Deliberate choice |
|---|---|
| Editorial | Strong image hierarchy, readable measure, restrained supporting type |
| Soft luxury | Quiet geometry, craftsmanship imagery, generous pacing |
| Brutalist | Firm alignment, explicit hierarchy, minimal ornament |
| Playful | Merchant-approved palette and composition, not decorative UI effects |
| Minimal | Sparse hierarchy with enough detail to make the purchase decision |

## Applying a direction

Record it in the plan. Apply tokens in `theme_css`; keep section
geometry in utilities unless the styling contract permits custom CSS.
`references/authoring/css-and-styling.md` owns scope, contrast, radii and
parts. After the live schema confirms a part, a visual override can be:

```css
#buy-box [data-part="cta"] { border-radius: var(--r-control); }
```

Do not add global part selectors, accent-tinted shadows, word accents,
background bands or motion to make a direction recognizable. Its identity
must survive without those effects. A saved island intent label is resolved
against the live schema, not copied as a prop bundle.

---

# Standalone asset operations

For page assets, execute `references/workflows/section-asset-workflow.md`.
For an asset-only request, accept the brand/store/theme binding, intended
role and delivery requirements without invoking page planning or design.
Eligibility and rights come from `references/assets/asset-sourcing-sequence.md`;
generation permissions come from `references/assets/generation-policy.md`.

## Import and upload mechanics

| Operation | Use |
|---|---|
| `lexsis_asset_library.search` | Find existing library assets; an empty query lets the user browse |
| `lexsis_assets.capabilities` | Discover current generation providers and capabilities |
| `lexsis_asset_import.import` | Import exactly one supplied source: URL, image base64 with MIME type, or conversation attachments |
| `lexsis_asset_upload.upload` | Open the local image/video upload UI |
| `lexsis_drafts.asset_generate` | Execute an approved generation request |
| `lexsis_assets.view` | Inspect the returned asset through the shared fit procedure |

Import arguments are exactly one of `url`, image `data` + `mime_type`, or
non-empty `attachments` with `attachment_id` per entry. Import never opens UI.
Upload arguments contain only the selected `workspace_id` and `theme_id`.
Wait for the user's uploaded-asset message; opening the panel is not a
completed upload. Without inline UI, request a URL or conversation attachment
and import it instead. `references/lexsis-mcp-contract.md` owns this contract.

## External-provider handoff

When the merchant chooses an available external provider, retain that provider
and its credit/approval evidence. Persist its output with
`lexsis_asset_import.import` before binding it to a page; use the returned
permanent asset URL, not a transient provider URL. Inspect it through the
shared asset workflow. Do not imply a provider exists merely because an old
example named it.

## Result record

Save the final bindings in
`work/storefront-assets/<brief-name>/asset-manifest.json`: role, source type,
asset id, permanent URL, and verification status. Shopify media retains its
product and media ids. Prompt history and rights evidence stay in the brief.
For an existing page, update only the requested slots and recompile once;
visible changes return to design approval. No page publication is implied.

---

# Hosted draft verification

Run by `/design-page` (Hosted Design Review) and `/optimize` Apply.

## Evidence gate

Follow `references/source-artifact-workflow.md`. There are no local QA steps,
page decision records or source-file prerequisites.

1. Check compiler results for the exact submitted inputs.
2. Reuse the existing unpublished draft, or create it once with `publish:false`.
3. Read persisted source, bundle and version through MCP; reconcile drift.
4. Run `lexsis_pages.integrity` and read `lexsis_pages.qa`.
5. Check the page-type contract, house rules and proof/offer evidence against
   that persisted source and the hosted draft. Type and copy findings are
   review notes; unsupported proof/offer content blocks readiness.

First drafts may be returned with QA pending. Production readiness requires
the hosted checks below; no browser access means no claimed visual pass.

## Browser QA (if available)

### Viewports to test:
- Mobile: 390px
- Tablet: 768px
- Desktop: 1280px

### Check for:
- [ ] No horizontal overflow at any viewport
- [ ] All images load (no broken/gray placeholders)
- [ ] Hero section visible above fold on both viewports
- [ ] Text readable without zooming on mobile
- [ ] Native disclosures and interactive islands respond to clicks (details, BuyBox selection)
- [ ] Expected Shopify variant enters the cart
- [ ] Cart opens and quantity/subtotal update
- [ ] Authored header and footer appear exactly once and in source order
- [ ] No renderer-injected shell or duplicate navigation is present
- [ ] Full-page hosted screenshots preserve the approved hierarchy and
      composition at all three viewports
- [ ] Dynamic island regions preserve the approved container geometry and
      placement
- [ ] Collection cards keep titles, prices, media, options, variants, and
      availability after hydration
- [ ] Quick Add is anchored to media top-right
- [ ] Desktop opens a right drawer and mobile opens a bottom sheet
- [ ] Sold-out variants are disabled; the chosen available variant is added
- [ ] Focus trap, Escape, and focus restoration work
- [ ] Product grids do not blank, flicker, restart media, or shift on hydration
- [ ] Asset thumbnails show visible media or actionable retry/unavailable state
- [ ] Functional-looking filter/sort controls work or are absent
- [ ] No console errors blocking render

Keep results with the hosted URL, source/bundle hash and tested version.
Record claims review, asset verification, screenshots, interaction evidence,
blockers and readiness. Save supported evidence with
`lexsis_drafts.page_record_qa` using its current schema; reread the QA record.

## Common Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| Gray product cards | Missing `image`/`media` in product data | Add image URLs or use `productIds` for auto-fetch |
| Native disclosure does not toggle | Broken details/summary markup or blocked input | Repair source and test keyboard/pointer input on the hosted draft |
| 401 on publish | OAuth session expired or revoked | Reconnect the MCP and complete browser OAuth |
| Insufficient scope on publish | Connection has Read or Build access | Reauthorize with Publish access after user approval |
| Images too large/slow | Using original Shopify CDN URLs | Use the supported image transformation for that URL; preserve its query parameters |

## Draft vs Live

- `publish: false` U+2192 draft at `/v/{slug}?shop={domain}&preview=1`
- `lexsis_page_create` is draft-only and rejects `publish:true`
- Publish later with `lexsis_live_ops` action `publish` after explicit approval
- Draft edits do not replace the public `published_version_id`

---

# Publishing and lifecycle

Publication promotes a reviewed draft; it does not create another page.
`references/source-artifact-workflow.md` owns source and version evidence.

## Publish gate

1. Resolve the existing page id and confirm its store/theme binding.
2. Read current `lexsis_pages.edit_context`, source and integrity.
3. Match the current version and source/bundle hashes to the approved hosted
   QA evidence from `references/qa-recipe.md`. Stale evidence blocks release.
4. Verify current publish permissions and entitlement.
5. Obtain explicit approval naming this page and version.
6. Call `lexsis_live_ops.publish` using the discovered argument schema.
7. Re-read the published version and verify the returned public URL. Report
   publication and live HTTP verification separately.

If no draft exists, use `references/generation-protocol.md` first. If a draft
exists, reuse its returned preview URL; previewing never creates another page.
No local source, CSS, manifest, compile artifact or QA file is required.

## Other lifecycle operations

`lexsis_live_ops.unpublish` and `lexsis_live_ops.rollback` require explicit
authorization and a confirmed target. Edits to a published page remain
draft-only until publish succeeds. A failed republish leaves the previous
published version in place; verify this rather than assuming recovery.

Variants follow `references/ab-testing.md`; every variant keeps its own
page/version and hosted QA evidence. Never infer publication from draft
creation, design approval, experiment creation or a request for a preview.

---

# Page generation

Choose the type through `references/page-types/_index.md`, execute `references/workflows/_how-to-read.md`, and use `references/generation-protocol.md` for compile, draft, and QA state transitions. Templates are starting source, not a second authority for section ordering.

---

# Storefront Page Editing

Run by `/design-page` (Existing Page Edits) and `/optimize` Apply.

Edit existing pages through canonical editable source and section-level remote
operations. Read `source-artifact-workflow.md` first.

## Edit Flow

1. Read `lexsis_pages.edit_context` and `lexsis_pages.source`.
2. Compare the current version with the last recorded version; reconcile drift.
3. Edit the returned source value and compile the complete changed inputs.
4. Compare section changes with the persisted baseline.
5. Patch only changed sections with `expected_version`,
   `expected_source_sha256` and an idempotency key where supported.
6. Update recorded version/hashes after success, then run `diff`, `integrity`
   and the affected checks on the hosted draft.

For existing pages, `page_id` is authoritative. Do not require the user to
reselect a workspace or pass `store_id`; an optional store ID is only an
assertion. Service-token store/workspace scopes remain authorization boundaries.

## Operations

### Update/Replace a Section

```
lexsis_drafts({
  action: "page_update_section",
  args: {
    page_id,
    section_id,
    source,
    expected_version,
    expected_source_sha256,
    idempotency_key
  }
})
```
- Replaces the compiled section from source-format HTML
- Auto-bumps page version
- Returns `version_conflict` if another edit landed first
- Use for: changing copy, swapping images, restyling

### Add a New Section

```
lexsis_drafts({
  action: "page_update_section",
  args: {
    page_id,
    source,
    position,
    expected_version,
    expected_source_sha256,
    idempotency_key
  }
})
```
- Position: `{ "before": "section-id" }`, `{ "after": "section-id" }`, or an
  index number
- Must include full section HTML

### Remove a Section

```
lexsis_drafts({ action: "page_remove_section", args: { page_id, section_id, expected_version } })
```
- Creates a reversible new page version
- Auto-bumps version

### Reorder Sections

```
lexsis_drafts({ action: "page_move_section", args: { page_id, section_id, position, expected_version } })
```
- Position is 0-indexed
- All other sections shift accordingly

## Best Practices

- Retain the intended change and returned version in the task handoff
- Always call `lexsis_pages` action `edit_context` before a write
- Stop on unexpected version drift
- Re-read source and reconcile against the current version when an edit returns `version_conflict`
- Reference section IDs from the page data (don't guess)
- Compile the complete editable source before section patching
- After editing, run `diff` and `integrity`
- Batch related multi-section changes with `page_patch` so they create one
  version.
- Use explicit remove operations for absent properties. `null` remains a JSON
  value and is not deletion.
- When changing a collection binding, setting `products` removes `productIds`
  and setting `productIds` removes `products`; never send both.
- Reusing an idempotency key with the same request returns the original result.
  Reusing it with different content is an error.
- Update input hashes and manifests only after a successful remote write.
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout

Minor edits do not repeat planning or create page files. Resolve the saved
binding or current MCP context; keep the existing page id authoritative.

For published pages, `current_version` can advance while the live renderer
remains pinned to `published_version_id`. Publish only after QA.

## Applying Reusable Sections

Read `merchant-templates.md`. `template_apply` follows the same edit
preconditions and materializes source into the page. After success, fetch edit
context, read back the persisted source and hashes, then run `diff` and `integrity`.

---

# MCP source and verification state

Author pages directly through MCP. Do not create local page decision records,
source/CSS files, compile artifacts, preview builds or local QA reports.
The persisted page source and bundle are the baseline; the hosted draft is
the only preview used by these workflows.

## Create one draft

1. Confirm the workspace, store and theme binding through saved context or
   current MCP reads. Prepare `source` and structured `head` with a title.
   Include `theme_css` only when supplying page-wide CSS. Omitting the field
   does not excuse missing theme tokens or accessibility styles.
2. Send the exact values to `lexsis_pages.compile`. Read blocking errors,
   warnings, missing utilities, hashes and the short-lived `compile_id`.
   Repair source, not compiled JSON.
3. Call `lexsis_page_create.create` with `compile_id`, creation metadata and
   `publish:false`. Omit `source`, `head`, `theme_css`, `scripts` and
   `runtime_dependencies` when passing `compile_id`. Alternatively send the
   exact source/head and optional CSS/scripts directly; create compiles them
   server-side. Never combine the two input modes.
4. Reuse an existing page id rather than spending another creation credit.
   If the compile id expires, recompile the unchanged inputs once.
5. Record the returned page id, version, preview URL and compile hash in the
   task handoff. Surface `DRAFT_CREATED` immediately; it is not a QA pass.

`lexsis_pages.compile_artifact` retrieves an existing compile result for
inspection; it is not another compile route. `lexsis_drafts.page_attach_bundle`
is recovery for a source write whose bundle attachment failed, with
`expected_version`; it is not a normal creation step.

## Edit the persisted source

1. Read `lexsis_pages.edit_context` and `lexsis_pages.source` or
   `lexsis_pages.section_source`. Confirm the target and current version.
2. Reconcile unexpected version drift before writing. Edit the source value
   returned by MCP, keeping stable section ids.
3. Compile changed inputs, compare the intended section changes and use the
   smallest source-based draft action with `expected_version`.
4. Update recorded version/hash evidence only after a successful write.
   Read back source and run `lexsis_pages.diff` and `lexsis_pages.integrity`.
5. Review the updated hosted draft. Editing a draft is not publishing it.

## Evidence without files

Keep the plan, proof/offer ledgers, confirmed asset decisions, approvals and
QA findings in the task's handoff record. `references/page-files.md` defines
the fields, not a filesystem requirement. Do not invent an MCP action for
storing a plan or manifest.

On continuation, recover the page through MCP and recover or re-establish
any missing evidence and approvals. A page id is not evidence that a claim,
asset right or previous approval was verified.

For production readiness, compare the reviewed inputs with the persisted
source, bundle and version; perform `references/qa-recipe.md` against the
hosted draft. Use `lexsis_pages.qa` to read recorded QA and
`lexsis_drafts.page_record_qa` to save supported evidence fields according to
the current schema. A tool acknowledgment does not replace browser evidence.
Missing browser access, evidence or matching hashes keeps QA pending.

Publication requires explicit approval for that same page and version under
`references/publishing.md`. No local validator or file can grant approval.

---

# Visual layout workflow

Use `references/workflows/_how-to-read.md` for the plan-to-design handoff and `references/design-concepts.md` when the merchant requests a visual concept first. The approved direction is implemented in the single source workspace defined by `references/source-artifact-workflow.md`.

---

# Public Storefront Workflow

The customer-facing pack has seven commands. Four form the normal page
journey:

```text
/setup
  U+2192 /plan-page
  U+2192 /design-page
  U+2192 /publish
```

| Command | Owns | Main output |
|---|---|---|
| `setup` | Saved store and theme design context | `setup.json` and design files |
| `plan-page` | The complete page specification: final section copy, an asset decision per section, claim gate, work queue and plan status | approved `page plan` (`PLAN_APPROVED`) |
| `design-page` | Plan gate, assets, islands, source, compile, one hosted draft, hosted QA at 390, 768 and 1280, later edits | `DRAFT_CREATED`, then `DESIGN_APPROVED` after hosted QA |
| `publish` | Explicit live release | published version |

Three optional commands support the workflow:

| Command | Owns |
|---|---|
| `optimize` | Score an existing page, propose a strict optimization plan, apply approved changes |
| `ab-test` | URL-first controlled variants and experiment evaluation |
| `cart` | Cart profile inspection, assignment, and editing |

## Rules

1. Each command owns one outcome and can be invoked independently.
2. Commands read artifacts from earlier steps but never invoke earlier steps
   automatically.
3. Explicit skips are recorded in the page record.
4. Every page binds one saved store/theme pair.
5. Persisted MCP source and version are the edit baseline.
6. Draft creation is not publishing approval.
7. Infer only question depth and publish-versus-draft intent from the whole
   request; the plan is always approved before design.
8. A visual concept is optional evidence inside `design-page`, not production
   page media.
9. Design creates `DRAFT_CREATED`, runs hosted QA and edits, and owns
   `DESIGN_APPROVED`; `publish` gates on it for the same version.

---

# Lexsis MCP Contract

Lexsis MCP is the system of record for templates, catalogue data, assets,
island schemas, compilation, drafts, remote versions, analytics, carts,
experiments, and publishing.

## Source and Template Authority

Page source is authoritative for section order and visible page chrome.
Headers, announcement bars, navigation, and footers are ordinary source
sections; the renderer must not inject a hidden shell around them.

Reusable user-owned sections use the merchant-template actions:

- `lexsis_template_library`: `list_mine`, `get_mine`
- `lexsis_drafts`: `template_create`, `template_update`, `template_apply`
- `lexsis_live_ops`: `template_publish`, `template_archive`

Read `merchant-templates.md` before creating, updating, or applying one. There
is no `lexsis_styles` router or Navigation Profile workflow.

MCP dependency metadata and an `.mcp.json` entry describe configuration. They
do not prove that the server or its tools are available in the current
session.

## Asset Import and Upload

`lexsis_asset_import.import` requires exactly one source: `url`, image
`data` + `mime_type`, or a non-empty `attachments` array of conversation
attachment IDs. It imports directly into the library and never opens the upload UI.
Do not call import without a source or combine multiple source types.

`lexsis_asset_upload.upload` exclusively opens the local image/video upload UI.
Pass only the selected `workspace_id` and `theme_id`; do not send URL, base64,
or attachment inputs to this action. In inline-UI hosts,
wait for the user's uploaded-asset message before using its asset ID and URL.
Opening the panel is not evidence that an asset was uploaded.

If the host has no inline UI, ask for a URL or conversation attachment and
use `lexsis_asset_import.import` with that source instead. Do not repeatedly
open an unsupported upload panel. `lexsis_asset_library.search` selects
existing library assets; it is not a local-file upload action.

## Managed Motion Compilation

Custom animation is authored in source as
`<script type="application/lexsis-motion">`. The `lexsis_pages` `compile`
action:

1. extracts each motion function into the owning section's `motion[]`
2. parses its AST and rejects unsafe globals, raw loops/observers/timers,
   arbitrary networking, dynamic code, programmatic clicks, and undeclared
   capabilities
3. validates page source, loop, and WebGL budgets
4. emits the animation manifest used for diagnostics and risk classification
5. preserves the module through source reads, page bundles, section patches,
   and versioned drafts

The renderer then supplies only the declared managed APIs. `three.load()` uses
the renderer-owned Three.js package and reserves a managed WebGL context;
`webgl.context()` supplies raw WebGL. Agents do not add Three.js, GSAP, Lottie,
or Rive CDN scripts.

Compilation proves that the module satisfies the contract. It does not prove
that a 3D composition is framed well or that an interaction feels correct.
Always review the hosted draft visually. Read `animation-system.md` before
authoring or editing managed motion.

## Resolve Actions with Exact Slots

The public skills declare the stable router and action pairs they use. Resolve
an unfamiliar input schema with the structured discovery fields:

```json
{
  "router": "lexsis_catalog",
  "action": "list"
}
```

Do not use a natural-language `query` for a known workflow action. The `query`
field is only a convenience when the router/action is genuinely unknown or
when mapping a former tool name.

`lexsis_discover` is an API directory, not a connection test and not the tool
that performs the operation. A response with `ok: true` and `count: 0` is a
lookup miss. It does not mean Lexsis MCP, the target router, or the storefront
is unavailable.

Before live Lexsis work:

1. Use the exact router/action pairs listed by the active skill.
2. When an action's arguments are unfamiliar, call `lexsis_discover` with
   `router` and `action`; never improvise a prose query for a known pair.
3. Invoke the real domain router for the operation.
4. Read changing products, variants, prices, availability, assets, island
   schemas, permissions, analytics, and remote versions live.

## When Lexsis Behaviour Is Unclear

`lexsis_support` action `search_docs` searches the Lexsis storefront
documentation and returns passages about islands, tools, recipes, page schema
and workflows. Use it when a behaviour is genuinely unclear, before guessing or
before telling the user something is impossible. It answers questions about the
product; it does not replace `lexsis_design` action `island_schema` for prop
shapes or `lexsis_discover` for an action's arguments.

## Recovery and Inspection Actions

Three actions exist for narrow situations and should not appear in a normal
build:

- `lexsis_pages` action `compile_artifact` retrieves a short-lived compiled
  bundle by `compile_id`. Draft creation consumes `compile_id` directly, so
  fetch the artifact only to inspect a compile result. Never fetch it merely to
  read the page back.
- `lexsis_drafts` action `page_attach_bundle` attaches an existing successful
  compile artifact to the current version without creating a new one. Use it
  only to recover a page whose source was stored but whose bundle attachment
  failed, with `expected_version`.
- `lexsis_pages` action `qa` reads the stored QA record for a page;
  `lexsis_drafts` action `page_record_qa` writes it.

## Reporting a Defect

`lexsis_drafts` action `send_feedback` files a bug or gap with the Lexsis dev
team. Use it when the platform, not the page, is at fault, and say so to the
user rather than filing silently. Categories: `island-bug`,
`island-variant-request`, `validator-issue`, `generation-quality`, `ux-issue`,
`docs-gap`, `composition-issue`, `api-bug`, `api-gap`, `platform-bug`, with a
severity. The distinction that matters: `docs-gap` means the guidance is
missing or wrong and documenting it would fix the problem, while `api-gap`
means no tool exists for a necessary operation and documentation would not.

File one when an island renders wrong with schema-valid props, the compiler
rejects something the contract allows, a tool returns a misleading result, or a
required primitive has no action. Do not file for a page-level mistake you can
fix yourself, and never let filing substitute for finishing or for telling the
user what is blocked.

## Error Handling

- `ok: true, count: 0` from discovery: keep working. Retry with the exact
  router/action pair, then use the current MCP tool schema or bundled Lexsis
  contract. Record discovery as degraded when appropriate.
- Missing router, authentication failure, transport failure, or an error from
  the actual domain call: report that concrete error and identify the affected
  operation.
- Continue work that does not depend on the failed live operation.
- Do not claim live data, successful compilation, a remote write, QA, or
  publishing when the corresponding real call did not succeed.
- Never substitute static HTML, cached catalogue data, or custom commerce
  controls as an equivalent successful Lexsis result.
- For a write, use only fields defined by the current MCP schema or bundled
  Lexsis contract. Do not guess mutation arguments.

### Explicit offline prototype

Continue without MCP only when the user explicitly requests an offline
prototype. Write it under an `offline-prototype/` directory, label it
non-production, and do not:

- mark planning, visual approval, asset readiness, draft readiness, QA, or
  publish readiness as complete
- claim live prices, inventory, variants, assets, commerce, or island behavior
- create or patch a Lexsis page

An offline prototype does not update the normal page record or replace the
standard Lexsis workflow.

### Individual capability unavailable

Continue only when the current skill defines a safe equivalent. Record the
capability, fallback, and limitation.

Examples:

- No suitable template result: custom composition is allowed after recording
  the searches and rejection reason.
- One island lacks safe preview data: static fallback is allowed for that
  island during visual review.
- Island schema or production compilation fails: do not record
  `DESIGN_APPROVED` for the page.

## Result Evidence

When useful for diagnosis, a Lexsis-dependent command result or `QA record`
reports:

- MCP connection status
- capabilities and resolution method used
- Lexsis router actions called
- selected template or reason for custom composition
- live product and asset bindings used
- fallbacks used
- blocking limitations

Do not store discovery logs, capability inventories, action transcripts, or
connection status in `page record`. The manifest is a compact workflow
state ledger.

`setup` has no page record, so it returns this evidence directly with its
saved setup paths.

---

# Merchant-Owned Section Templates

Merchant templates are reusable, versioned source-format sections. They use the
existing template and revision model; they are not renderer defaults, global
shell assignments, or a separate recipe system.

## Contract

- A template contains exactly one compilable source section.
- The section may be a Header, Footer, Announcement, product composition, or
  any future supported island composition.
- CSS remains inside canonical section source and follows the normal compiler
  and source-format rules.
- Applying a template copies its source into the target page and creates one
  ordinary page version. The page does not retain a live dependency on the
  template.
- Updating, publishing, archiving, or deleting template metadata never mutates
  pages that already materialized its source.
- Listing is metadata-only. Fetch one template before reading or editing its
  source.

## MCP Actions

Read:

```text
lexsis_template_library({ action: "list_mine", args: { workspace_id } })
lexsis_template_library({ action: "get_mine", args: { workspace_id, template_id } })
```

Reversible draft operations:

```text
lexsis_drafts({
  action: "template_create",
  args: { workspace_id, name, source, visibility, description?, section?, tags? }
})

lexsis_drafts({
  action: "template_update",
  args: { workspace_id, template_id, source?, name?, description?, visibility?, section?, tags? }
})

lexsis_drafts({
  action: "template_apply",
  args: {
    template_id,
    page_id,
    expected_version,
    expected_source_sha256?,
    position?,
    section_id?,
    idempotency_key?
  }
})
```

`position` is `first`, `last`, `{ "before": "<section-id>" }`, or
`{ "after": "<section-id>" }`. `section_id` optionally renames the copied
section so it does not collide with an existing page section.

Sensitive lifecycle operations require explicit approval:

```text
lexsis_live_ops({ action: "template_publish", args: { workspace_id, template_id, revision_id? } })
lexsis_live_ops({ action: "template_archive", args: { workspace_id, template_id } })
```

## Source Authority

Header, navigation, announcement, and footer are ordinary authored sections.
Do not:

- inject them at renderer level;
- depend on inherited header/footer flags;
- create a `shell`, `navigation_profile`, Recipes route, or `lexsis_styles`
  tool;
- regenerate an entire page when a reusable section can be applied;
- assume a template is Header/Footer-specific.

Use Templates U+2192 My templates for the user-owned library. Use the Design Library
for brand tokens and navigation/footer link data, not as a second page renderer.

---

# Lexsis Page Design Capabilities

Use this contract when designing, preparing assets, generating, or
structurally optimizing a Lexsis page. `/plan-page` does not load island or
implementation guidance.

## Theme and Brand Context

Select exactly one saved store/theme pair for a page.

- Use the saved `brand-design.md` for voice, art direction, component guidance,
  and explicit design don'ts.
- Use `lexsis_brand` action `get_theme` for the current complete theme when a
  live refresh is required.
- Use `lexsis_brand` action `compile_theme` when theme CSS must be derived from
  brand inputs.
- Exact theme tokens are the normal render source. However, an explicit
  `NEVER`, `must`, or `non-negotiable` rule in the saved design guide that
  directly contradicts a matching token is invalid theme context. Return
  `THEME_CONTEXT_CONFLICT`, name both values, and stop using that property until
  the saved theme or guide is corrected. Do not silently choose one.
- Never combine design files or CSS from multiple themes on one page.

The theme compiler provides WCAG-checked `--lx-*` variables including:

- `--lx-accent-color`
- `--lx-accent-color-hover`
- `--lx-accent-soft`
- `--lx-bg-color`
- `--lx-bg-surface`
- `--lx-surface-alt`
- `--lx-text-color`
- `--lx-text-muted`
- `--lx-border-color`
- optional `--lx-font-heading`, `--lx-font-body`, and `--lx-radius`

Use tokens for brand colors, typography, surfaces, borders, and radii. Avoid
hard-coded brand values inside sections.

## Tailwind and CSS

Lexsis compiles page classes with Tailwind at compile time. There is no runtime
Tailwind CDN.

- Use Tailwind utilities for layout, spacing, sizing, and responsive behavior.
- Work mobile-first, then enhance with responsive prefixes.
- Missing Tailwind utilities are blocking compiler errors unless the class is
  explicitly defined in theme or section CSS.
- Use section CSS only for intentional, scoped components or behavior.
- Do not recreate the page layout as a second CSS system.

Compiled CSS order is:

1. theme CSS
2. generated Tailwind utilities
3. section CSS in page order

Section CSS can override earlier rules at equal specificity. Keep global
tokens and page-wide rules in theme CSS, and scope section overrides by
section ID.

The renderer supplies base styles; do not recreate its reset. Motion follows
`references/design-rules.md` N10 and `references/animation-system.md`, not
a list of renderer keyframes to reuse by default.

## Template-First Composition

Before custom composition:

0. Ask whether the user wants to pick a kit or sections themselves. If so,
   browse with `query: ""` and the page type, industry, and mood filters, and
   wait for the `Design template selection:` message. Resolve a picked or
   pasted kit with `lexsis_template_library` action `get_kit`.
1. Discover `lexsis_template_library` actions `search_page_kits`,
   `search_sections`, and `get_kit`.
2. Only when the user declines: search page kits using page type, archetype,
   objective, industry, and mood, and present at most three candidates.
3. Treat a page kit as a coherent list of section-template IDs. There is no
   single page-kit instantiation action.
4. Fetch selected section source through `lexsis_design` action `get_section`,
   at most three IDs per call.
5. Adapt the returned source to the selected theme, plan, products, copy, and
   assets.

Template search returns metadata, not editable markup. `get_section` returns
authoring source with section delimiters, `<lx-island>` markup, and section
CSS/JS.

If the host renders the Template Gallery, wait for the user's
`Design template selection:` message; without a picker, offer the public
gallery URL and accept a pasted kit or template URL. Custom composition is
allowed only after recording the evaluated templates and why none fit.

## Islands

For every interactive element:

1. Discover `lexsis_design` actions `islands` and `island_schema`.
2. Use `islands` for selection guidance.
3. Resolve the exact selected schema.
4. Confirm lifecycle status is active.
5. Use the current required props and a supported native variant.
6. Style supported `data-part` hooks listed by the schema.
7. Use headless mode only when native variants cannot satisfy the approved
   design and every required hook is implemented.

Author islands as `<lx-island>` with one readable `application/json` child.
Never hand-author compiled `data-island` or `data-props` markup.

If the catalogue marks an island deprecated or retired, follow its
replacement guidance. The replacement may be another island or supported
native HTML/CSS such as `<details>`; do not force a deprecated island into the
page.

Do not replace BuyBox or another commerce island with a custom button.

## Hosted Preview

The design-stage source is compiled and then saved as one unpublished hosted
draft. That hosted renderer is the only interactive preview.

- Use current schemas and real product/media bindings before creation.
- Shoppable video, galleries, accordions, and similar islands are reviewed in
  the same runtime merchants will receive.
- Do not build a local renderer shell or record local hydration evidence.
- `/design-page` inspects 390px, 768px and 1280px with commerce checks before
  `DESIGN_APPROVED`.

## Asset Roles

Template results do not expose a separate media-slot schema. Derive required
roles, aspect ratios, and crop guidance from the selected section source,
approved layout, and island schema.

Use live Shopify media for product identity. Visually verify creator and
product imagery. Temporary or local placeholders never enter page source.

## Compact Manifest Evidence

Record the design decision:

```json
{
  "template": {
    "mode": "page-kit",
    "pageKitId": "kit-slug",
    "sectionTemplateIds": ["hero-slug", "buy-box-slug"]
  },
  "design": {
    "stylePack": "editorial",
    "compiledStyleManifest": null
  }
}
```

`template.mode` is `page-kit`, `sections`, or `custom`. Keep selection reasons
and evaluated alternatives in `page plan`, not the page record. After
compilation, store the returned style manifest under
`design.compiledStyleManifest`.

`stylePack` is the selected named pack, `custom` for an intentional scoped
treatment, or `existing-page` when adopting and preserving a remote page's
current design.

---

# Page Types: Identification Framework

Every storefront page is one of the thirty types below. `/plan-page` picks
exactly one before it searches templates, assets or proof, records it in the
`## Page type` block and in `page.pageType`, and then loads only that type's
file. `/design-page` and `/optimize` re-read the same file. Each
type file follows `references/page-types/_checklist-format.md` and ends with
a JSON checklist shared by the workflow and repository contract tests.

## 1. Inputs to read from the brief

Extract these seven facts before choosing. Ask only for the ones that change
the answer and that the catalog, brand, campaign and analytics cannot supply.

| Input | Values | Where it usually comes from |
|---|---|---|
| Traffic source | meta, tiktok, google-search, google-shopping, email, sms, organic, direct, influencer, affiliate, retargeting, marketplace | brief, `lexsis_campaigns.creatives`, analytics |
| Funnel stage | tof (cold), mof (warm), bof (hot), retention (owned) | traffic + whether the visitor has seen the product |
| Awareness (Schwartz) | unaware, problem-aware, solution-aware, product-aware, most-aware | traffic + ad creative + audience description |
| Desired action | buy now, add to cart, start quiz, join waitlist, subscribe, capture email, read then buy, browse, refer, reorder | brief |
| Product count | 1 SKU, 1 product with variants, 2 to 5 (kit/compare), 6 to 40 (collection), whole store | catalog |
| Offer shape | an offer id from `references/offers/offer-types.md`: `none`, `first-order`, `percent-off`, `fixed-off`, `bogo`, `gwp`, `bundle`, `bundle-decoy`, `subscribe-save`, `free-shipping`, `tiered-volume`, `pre-order-price`, `trial-sample`, `flash-sale`, `clearance`, `limited-edition`, and the rest of that list | brief, merchant |
| Campaign trigger | a campaign id from `references/offers/campaign-calendar.md`: `evergreen`, `launch`, `restock`, `seasonal`, `gifting`, `flash-sale`, `clearance`, `collab-drop`, `anniversary`, `cause`, `back-to-school`, `bfcm`, `end-of-season`, `founder-sale` | brief, calendar |

## 2. Decision tree

Walk top to bottom; stop at the first leaf that fits. Tie-breaks are in
section 4.

```text
Is the visitor's job to BUY (or add to cart) on this page?
+-- no - what is the job?
|   +-- answer questions / route to the right product ........... quiz-funnel
|   +-- leave an email or phone (giveaway, waitlist, early access)
|   |   +-- product not yet purchasable ....................... launch-waitlist-preorder
|   |   +-- incentive or contest ............................... lead-capture-giveaway
|   +-- read a story, learn who we are ......................... brand-story-founder
|   +-- understand the science, ingredients, materials, method . ingredient-science
|   +-- browse many products
|   |   +-- whole store, first visit ........................... homepage
|   |   +-- one category or collection ......................... collection-landing
|   |   +-- by recipient or price for a holiday ................ gift-guide
|   |   +-- outfits, rooms, looks with shoppable items ......... lookbook-shop-the-look
|   +-- get help, policies, answers ............................ faq-support-led
|   +-- refer a friend, join a programme, see tiers ............ referral-loyalty-vip
|   +-- just paid; what next .................................... thank-you-post-purchase
|   +-- order in volume for resale ............................. wholesale-b2b
+-- yes - has the visitor already seen this product or brand?
    +-- no (cold) - what brought them?
    |   +-- a social ad with a story or problem hook (meta, tiktok, native)
    |   |   +-- long-read wanted, price hidden until late ...... advertorial
    |   |   +-- "N reasons / best X" list framing ............. listicle
    |   |   +-- creator or customer video is the hero .......... ugc-creator-collab
    |   |   +-- one long video does the selling ................ video-sales-page
    |   |   +-- direct-response, single product, single CTA .... ad-landing-page
    |   +-- a search for the product or category (google, shopping)
    |   |   +-- "X vs Y", "alternatives" ....................... comparison-us-vs-them
    |   |   +-- "best X", "top N X", buyer's guide, roundup ..... seo-buyers-guide
    |   |   +-- product or category intent ..................... pdp (search-intent variant)
    |   +-- a sample, trial or starter offer ................... trial-sample
    +-- yes (warm or hot) - what is the page selling?
        +-- one product at full price, full store context ....... pdp
        +-- one product, paid-traffic focus, no navigation ...... pdp-hybrid-landing
        +-- two or more products as a set or configurator ....... bundle-kit
        +-- a recurring plan ..................................... subscription
        +-- a specific discount, code, GWP or BOGO .............. offer-page
        +-- many products at reduced prices for a window ........ sale-clearance-flash
        +-- an occasion or holiday assortment .................... seasonal-gifting
        +-- a product that is back or newly available ............ restock
        +-- a return visit after abandonment or a prior view ..... retargeting-warm
```

## 2b. Keyword lookup

A fast first pass before the tree. The tree still decides.

| Brief says | Type |
|---|---|
| "5 reasons", "top 7", "reasons why", "things you didn't know" (paid social, one product) | `listicle` |
| "best X", "top N X for Y", "buyer's guide", "roundup" (search intent) | `seo-buyers-guide` |
| "story", "article", "editorial", "we tried it", "here's what happened", native placement | `advertorial` |
| "vs", "compared to", "alternative to", "why switch" | `comparison-us-vs-them` |
| "find your", "which one is right", "shade finder", "size finder" | `quiz-funnel` |
| "bundle", "kit", "starter set", "build your own", "routine" | `bundle-kit` |
| "% off", "BOGO", "free gift", "GWP", "code", "deal" without a hard end | `offer-page` |
| "sale", "flash", "clearance", "ends", "48 hours" | `sale-clearance-flash` |
| "BFCM", "Diwali", "Rakhi", "Valentine", "Mother's Day", "Eid", "Christmas" with a buying window | `seasonal-gifting` |
| "gift guide", "gifts for", "under ₹999" without a hard date | `gift-guide` |
| "launch", "coming soon", "waitlist", "pre-order", "drop" | `launch-waitlist-preorder` |
| "restock", "back in stock", "notify me" | `restock` |
| "subscribe", "auto-ship", "membership" | `subscription` |
| "creator", "influencer", "collab", "x [name]", "code [NAME]" | `ugc-creator-collab` |
| "video", "VSL", "watch the presentation" | `video-sales-page` |
| "about", "our story", "founder", "why we started" | `brand-story-founder` |
| "ingredients", "science", "how it works", "clinical", "studies" | `ingredient-science` |
| "shop all", "collection", "category", "browse" | `collection-landing` |
| "homepage", "home" | `homepage` |
| "lookbook", "shop the look", "outfit", "styled" | `lookbook-shop-the-look` |
| "thank you", "order confirmation", "after checkout" | `thank-you-post-purchase` |
| "giveaway", "enter to win", "newsletter", "10% for email", "text club" | `lead-capture-giveaway` |
| "refer", "rewards", "VIP", "loyalty", "points" | `referral-loyalty-vip` |
| "retarget", "came back", "visited but didn't buy", "abandoned" | `retargeting-warm` |
| "FAQ", "help", "support", "questions" | `faq-support-led` |
| "sample", "trial", "try before you buy", "home try-on" | `trial-sample` |
| "wholesale", "B2B", "stockists", "bulk" | `wholesale-b2b` |
| "landing page", "LP", "ad page", "post-click" for one product | `ad-landing-page` (or `pdp-hybrid-landing` when variants or gallery matter) |
| "product page", "PDP", brand search, Google Shopping | `pdp` |
| "microsite", "campaign hub" | the type of its main page; other pages are separate plans |
| "mobile first", "one thumb" | a modifier, not a type; every type is mobile-first already |

## 3. Type catalogue

`Length` is sections between chrome. `Proof` is the checklist's module range.
`Nav` is the checklist value.

| Type id | One line | Stage | Awareness | Typical traffic | Length | CTAs | Proof | Nav |
|---|---|---|---|---|---|---|---|---|
| `ad-landing-page` | Single product, single CTA, message-matched to a paid ad | tof/mof | problemU+2192product | meta, tiktok, google | 8-11 | 3 | 2-4 | none |
| `pdp` | Full product page inside the store; gallery, buy box, details, reviews | mof/bof | product/most | organic, search, email, nav | 7-11 | 2 | 2-4 | full |
| `pdp-hybrid-landing` | PDP anatomy with landing-page focus: no nav, ad message match, one goal | mof | solutionU+2192product | meta, google shopping | 8-11 | 2-3 | 2-4 | none |
| `advertorial` | Editorial article that sells by story; price and CTA arrive late | tof | unaware/problem | meta, native, tiktok | 8-12 | 1-3 | 2-4 | none |
| `listicle` | Numbered reasons for one product; each reason answers an objection and earns a click | tof/mof | problem/solution | meta, tiktok | 8-13 | 3-6 | 2-4 | none/minimal |
| `seo-buyers-guide` | Search-intent roundup or "best X" guide: TOC, methodology, ranked entries, comparison table | tof/mof | problem/solution | google organic, google ads | 9-14 | per entry + 1 | 2-4 | full |
| `comparison-us-vs-them` | Attribute table against named or generic alternatives | mof | solution/product | google, retargeting | 7-10 | 2-3 | 2-3 | minimal |
| `quiz-funnel` | Questions route the visitor to a recommendation | tof/mof | problem/solution | meta, tiktok, email | 4-7 | 1 + result | 1-2 | none |
| `bundle-kit` | Fixed or build-your-own set with visible savings math | mof/bof | product | email, pdp cross-link, ads | 7-10 | 2 | 2-3 | minimal/full |
| `offer-page` | One named promotion (code, GWP, BOGO, first order) | mof/bof | product/most | email, sms, retargeting | 6-9 | 2-3 | 1-3 | minimal |
| `sale-clearance-flash` | Many products, reduced prices, real window | bof | most | email, sms, social | 5-8 | per card | 1-2 | full |
| `seasonal-gifting` | Occasion assortment with delivery cutoffs and gift options | mof | solution/product | email, social, search | 7-10 | per card + 1 | 1-3 | full |
| `gift-guide` | Curated picks by recipient or price band | tof/mof | solution | organic, email, social | 6-9 | per card | 1-2 | full |
| `launch-waitlist-preorder` | Not yet buyable: capture intent or take pre-orders | tof/mof | problem/solution | email, social, PR | 6-9 | 1-2 | 1-3 | minimal |
| `restock` | Product is back; convert the demand already there | bof/retention | most | email, sms | 5-7 | 2 | 1-2 | minimal |
| `subscription` | Recurring plan; cadence, savings, cancellation clarity | mof/bof | product | pdp, email, ads | 7-10 | 2 | 2-3 | minimal/full |
| `ugc-creator-collab` | Creator or customer content is the hero and the proof | tof/mof | problem/solution | tiktok, instagram, influencer | 6-9 | 2-3 | 3-5 | none |
| `video-sales-page` | One long video, then the offer | tof/mof | problem/solution | meta, youtube, email | 5-8 | 1-2 | 1-3 | none |
| `brand-story-founder` | Who we are and why; sells belief, not a SKU | tof/retention | unaware/problem | organic, nav, PR | 6-9 | 1-2 | 1-2 | full |
| `ingredient-science` | Mechanism, ingredients, materials, studies | mof | solution/product | organic, pdp link, google | 7-10 | 1-2 | 2-4 | full |
| `collection-landing` | One category; grid with filters and a short story | mof | solution | organic, nav, google | 5-8 | per card | 1-2 | full |
| `homepage` | Store front door; route to collections, best sellers, story | tof/retention | all | direct, organic, brand search | 7-10 | 2-3 | 2-3 | full |
| `lookbook-shop-the-look` | Editorial imagery with shoppable items | tof/mof | solution | instagram, organic, email | 5-8 | per look | 1-2 | full |
| `lead-capture-giveaway` | Email or SMS in exchange for an incentive | tof | unaware/problem | social, partner, ads | 3-6 | 1 | 1-2 | none |
| `referral-loyalty-vip` | Programme rules, tiers, rewards, join | retention | most | email, account, nav | 5-8 | 1-2 | 1-2 | full |
| `retargeting-warm` | Visitor saw it already; handle objections, restate offer | bof | product/most | meta/google retargeting | 5-8 | 2-3 | 2-4 | none/minimal |
| `thank-you-post-purchase` | Order confirmed; next steps, one relevant add-on, referral | retention | most | checkout | 3-6 | 1-2 | 0-1 | minimal |
| `faq-support-led` | Answers first; policies, shipping, sizing, care | mof/retention | product | organic, nav, support links | 4-7 | 1 | 0-2 | full |
| `trial-sample` | Low-risk first purchase; what happens after is explicit | tof/mof | solution | ads, email | 6-9 | 2 | 2-3 | minimal |
| `wholesale-b2b` | MOQ, tiers, lead times, line sheet, inquiry | mof | product | organic, outreach | 5-8 | 1-2 | 1-3 | minimal |

## 4. Tie-breaks between near neighbours

| If torn between | Choose | Because |
|---|---|---|
| `ad-landing-page` vs `pdp-hybrid-landing` | hybrid when the product has 3+ variants or a gallery that matters; ad-landing otherwise | hybrid keeps PDP buy mechanics; ad-landing keeps one story |
| `ad-landing-page` vs `advertorial` | advertorial when awareness is unaware/problem-aware and the ad is a story or "I tried" hook | cold readers need the premise before the price |
| `advertorial` vs `listicle` | listicle when the ad or search phrase is a number or "best/top/reasons" | frame must match the click |
| `listicle` vs `comparison-us-vs-them` | comparison when the visitor named a competitor or searched "vs" | intent is evaluative, not exploratory |
| `listicle` vs `seo-buyers-guide` | buyer's guide when traffic is search and the query is "best/top N"; listicle when traffic is paid social and the page sells one product | search readers expect a ranked, methodical roundup; social readers expect five reasons |
| `pdp` vs `pdp-hybrid-landing` | hybrid whenever the traffic is paid and the brief wants one goal | navigation on paid traffic leaks |
| `bundle-kit` vs `offer-page` | bundle when the value is the set; offer when the value is the discount | anatomy differs: savings math vs offer terms |
| `offer-page` vs `sale-clearance-flash` | sale when more than five products are discounted | grid, not buy box |
| `seasonal-gifting` vs `gift-guide` | gifting when there is a purchase window with cutoffs and gift options; guide when it is curation without a hard date | cutoff logic vs editorial |
| `launch-waitlist-preorder` vs `restock` | restock when the product sold before and has review data | proof exists |
| `ugc-creator-collab` vs `video-sales-page` | VSL when one long video carries the pitch; UGC when many short clips do | one hero vs many proofs |
| `retargeting-warm` vs `offer-page` | retargeting when the offer is secondary to objection handling | different first screen |
| `quiz-funnel` vs `lead-capture-giveaway` | quiz when answers change the recommendation; capture when they do not | a quiz that does not route is a form |
| `homepage` vs `collection-landing` | collection when one category is named | scope |
| `brand-story-founder` vs `ingredient-science` | science when the brief names ingredients, studies or "how it works" | mechanism vs meaning |
| Brief is silent on stage | the type that assumes less (`ad-landing-page` over `retargeting-warm`, `advertorial` over `ad-landing-page` for unaware audiences) | over-assuming knowledge loses cold visitors |

## 5. Awareness level U+2192 headline and page posture

Eugene Schwartz's five stages decide how much the page may assume and what
the headline leads with.

| Awareness | Visitor knows | Headline leads with | Page posture | Types |
|---|---|---|---|---|
| unaware | nothing relevant | a story, an identity, a surprising fact; never the product | educate first, price last | advertorial, brand-story, video-sales |
| problem-aware | the pain, not the fix | the problem named in their words | agitate briefly, reveal mechanism, then product | advertorial, listicle, ad-landing, quiz |
| solution-aware | the category, not you | the mechanism or outcome and why this one | differentiate, compare, prove | ad-landing, comparison, ingredient-science, ugc |
| product-aware | your product, not enough to buy | the product name plus the strongest claim or offer | proof, price clarity, risk reversal | pdp, hybrid, bundle, subscription, retargeting |
| most-aware | wants it; needs the deal or the nudge | product plus offer plus terms | buy box first, no education | offer, sale, restock, thank-you |

Rule: a page never assumes a higher awareness than the traffic supplies. Cold
social traffic is problem-aware at best. Brand search is product-aware.

## 6. Funnel stage defaults

| Stage | Assume | Proof density | Offer aggressiveness | Copy length | First CTA |
|---|---|---|---|---|---|
| tof | nothing; explain the premise | high, early and distributed | low; `first-order` or `free-shipping` in view, `gwp` or `trial-sample` only below the fold | longest | after the premise (hero for ad-landing; section 4+ for advertorial) |
| mof | category known; brand not trusted | high, beside claims | moderate; bundle, subscribe-and-save, GWP | medium | hero |
| bof | product known; objections remain | targeted; answer the objection | highest that the ledger verifies | short | hero, repeated |
| retention | brand trusted | light; continuity cues | loyalty, referral, reorder | shortest | hero |

`references/offers/funnel-stages.md` expands this table.

## 7. Recording the choice

Plan block (`page plan`):

```markdown
## Page type

**Type.** advertorial
**Funnel stage.** tof
**Awareness.** problem-aware
**Traffic.** meta
**Offer.** first-order
**Campaign.** evergreen
**Copy framework.** story-lead
**Mandatory sections omitted.** none
```

Manifest (`page record`): `page.pageType`, `page.funnelStage`,
`page.awareness`, `page.trafficSource`, plus `offer` and `campaign` blocks
(`references/page-files.md`).

## 8. Benchmarks and what they are worth

Use benchmarks to set relative expectations (quiz > landing page > PDP for
cold traffic; PDP beats a landing page for hot and branded-search traffic),
never as promised outcomes. Print the caveat with the number.

| Metric | Value | Source | Caveat |
|---|---|---|---|
| Median landing-page conversion, all industries | 6.6% | Unbounce Conversion Benchmark Report Q4 2024, https://unbounce.com/conversion-benchmark-report/ | counts form fills and other goals, not purchases |
| Ecommerce landing-page conversion | 2.35% to 4.2% | same report; summaries of the same data disagree | quote the range, never one number |
| Ecommerce landing page by channel | email 28.6%, paid search 5.1 to 5.7%, paid social 4.8% | https://unbounce.com/conversion-benchmark-report/ecommerce-conversion-rate/ | traffic source moves conversion more than page design |
| Reading level | grade 5 to 7 pages 5.6% vs professional 1.5% | same | correlational |
| Ecommerce landing-page word count | 285 to 930 words | same | classic landing page only, not advertorial |
| Average Shopify store conversion | 1.4% (top 20% above 3.2%, top 10% above 4.7%) | Littledata, https://www.littledata.io/ecommerce-conversion-rate | average across ~2,800 stores, 2023 |
| Shopify add-to-cart rate | 4.6% of sessions (top 10% above 9.6%) | Littledata | low ATC is a product-page problem |
| Cart abandonment | 70.2% mean of 50 studies | https://baymard.com/lists/cart-abandonment-rate | 42% "just browsing" is unavoidable |
| Landing page vs PDP by traffic heat | cold LP 3.8% vs PDP 2.4%; hot (cart abandoners) LP 6.5% vs PDP 7.2%; branded search LP 5.1% vs PDP 6.8% | https://mhigrowthengine.com/blog/landing-page-vs-product-page-dtc/ | practitioner averages |
| Cold Facebook traffic straight to PDP | about 0.5%; with an advertorial in between 3 to 5% | TrueProfit via https://www.getlandra.com/blog/advertorial-listicle-conversion-statistics | vendor, directional |
| Quiz results pages | one results page 10.6% vs 7.1% with 11 or more | https://docs.revenuehunt.com/customer-success/how-to-build-successful-quiz/ | vendor data |
| Back-in-stock alerts | about 25% when sent within 15 minutes, 10% after 4 hours | Klaviyo via https://ustechautomations.com/resources/blog/ecommerce-back-in-stock-notifications-how-to-2026 | vendor |
| Post-purchase one-click upsell | 3 to 8% take rate; thank-you page upsells about 1% | https://zipify.com/blog-post-purchase-upsells-shopify-2026/ | vendor network |
| Urgency | real promo countdown +8.3%; generic timer -11.4% revenue; cart urgency flat | https://crometrics.com/blog/urgency-that-actually-works/ | agency test portfolio |
| Sticky add-to-cart | -7.7% to +26% across tests | see `references/anti-patterns/cro-anti-patterns.md` | mixed; test, do not assume |
| Reading | users read about 20 to 28% of words; paragraph 4 gets 32% of eyes | https://www.nngroup.com/articles/how-little-do-users-read/ , https://www.nngroup.com/articles/website-reading/ | subheads carry long pages |

## 9. Universal rules across every type

1. Message match: the H1 restates the promise of the ad, email or creator
   post that sent the click (`references/copy/message-match.md`).
2. One destination: on single-goal types every CTA points at the same next
   step.
3. Mobile first: hero, first proof and CTA survive the first 390px screen as
   the type file lists them.
4. Proof is specific and checkable, and comes from the Proof ledger.
5. Urgency is real, specific and server-anchored, from the Offer ledger.
6. Plain language: grade 6 to 8, short paragraphs, a subhead every 300 to 500
   words on long pages.
7. A reviews block with 5 or more reviews shows the ratings distribution and
   lets it filter; below 5 it shows the count and quotes only.
8. Hero media is compressed and preloaded (`references/assets/slot-spec.md`).
9. Advertorials carry a visible "Advertisement" or "Sponsored" label;
   health claims stay within what the ledger substantiates.
10. Never send cold prospecting traffic to the homepage.

## 10. What the type does not decide

Vertical (`references/vertical-*.md`), traffic source
(`references/traffic-source-*.md`) and brand design layer on top of the type.
The type fixes anatomy, proof density, CTA logic, price timing and imagery
jobs. The vertical fixes which modules fill those slots (ingredient explorer
for beauty, supplement-facts panel for supplements, size guide for fashion).
The traffic file fixes tone and message match. House rules
(`references/design-rules.md`) override all three.

---

# Page-Type Checklist Format

Every file in `references/page-types/` (except `_index.md` and this file)
describes one page type in the same shape so that `/plan-page`, `/design-page`,
`/optimize` and repository contract tests can read it the same way. The
heart of each file is its `## Workflow`: the ordered thinking the model follows
for that type, section by section, with the asset decision, the island
decision and the tool call that settles each. The `## Checklist` JSON is the
default anatomy the workflow produces; deviate when the context calls for it
and note the deviation in the plan. House rules in `references/design-rules.md`
still apply to every page.

## How a skill uses a page-type file

1. `/plan-page` identifies the type with `references/page-types/_index.md`,
   records the `## Page type` block in `page plan` and `page.pageType` in
   `page record`, then loads only the matching file.
2. `/plan-page` follows the file's **Workflow**: the context reads first, then
   each section in order with its media decision (search, generate, ask or
   skip), island decision and copy ceiling. The **Checklist** JSON is the
   default the workflow lands on; a deviation is written under "Deviations
   from the type default" in the plan with its reason.
3. `/design-page` re-reads the same file before writing HTML and follows the
   Workflow's island and asset decisions while composing, with **Above the
   fold**, **Proof**, **Offer and CTA**, **Imagery** and **Copy** as the
   guide. Where source and plan disagree with the checklist, it lists the
   differences in the plan and continues.
4. Review the checklist against the plan, then the persisted source and
   hosted draft. Type deviations are advisory; proof/offer violations
   block readiness. Repository fixture checks test this contract separately.

## Required prose sections, in order

```markdown
# <Page type name>

One paragraph: what the page is for, who lands on it, what they must do.

## Identify it
Signals in the brief that select this type; near neighbours and how to tell
them apart (one line each).

## Anatomy
Numbered, ordered section list using the canonical ids below. Mark each
`mandatory`, `recommended` or `conditional: <condition>`. One sentence per
section on its job.

## Workflow
The ordered thinking for this type. Three fixed sub-headings:

### Context reads
Numbered tool calls run before any section is chosen, each with what to
extract from the result (image count and which jobs they cover, variant axes
and whether colour variants have images, price and compare-at, selling plans,
inventory, review count band, theme tokens and voice, asset library inventory
by tag, ad creative for message match).

### Section by section

Link `references/workflows/_how-to-read.md` once. It supplies the shared
asset/fallback, view-and-fit, island-resolution and copy procedures.
Keep one row per Anatomy section, in order, with type-specific inputs only:

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `<section id>` | Shopper job | Needed job, tag/query, crop and specific alternative | Native content or candidate family plus decision inputs | Type-specific message or ceiling | Data that settles the decision |

Do not repeat the shared procedures or enumerate props. Planning records
functional intent; design resolves the current island schema. Default copy
ceilings remain in the copy-policy owner, with deliberate type exceptions
recorded in the plan.

### Asset budget

A table records what the catalogue and library supply, which jobs are
missing, and type-specific alternatives. Execute gaps through the shared
asset workflow rather than reproducing its question and fallback rules.
A deliberately text-only section remains valid when the type specifies it.

## Above the fold (390px)
What must be visible in the first screen on mobile, in order. What must not.

## Proof
Which proof kinds, how many modules, where they sit, minimum evidence per
kind, and what replaces them when the store has none
(`references/proof/reviews-sourcing.md`).

## Offer and CTA
CTA count, first CTA position, sticky rule, CTA copy pattern, price reveal
timing, offer types that fit and offer types that do not
(`references/offers/offer-types.md`).

## Imagery
Required image jobs, hero treatment, lifestyle vs studio balance, video rule,
slots the plan must create (`references/assets/image-jobs-by-page-type.md`).

## Copy
Framework, headline pattern, reading level, length ceiling per section,
vocabulary constraints (`references/copy/copy-frameworks.md`).

## Never
Type-specific failures, one line each, each checkable.

## Examples
Two or three real pages with URLs and one line on what they do well.

## Checklist
One fenced ```json block, schema below.

## Sources
URLs.
```

## Checklist JSON schema

```json
{
  "page_type": "advertorial",
  "aliases": ["editorial pre-sell", "native article"],
  "funnel_stage": ["tof", "mof"],
  "awareness": ["problem-aware", "solution-aware"],
  "traffic": ["meta", "tiktok", "native"],
  "sections": { "min": 8, "max": 12 },
  "mandatory_sections": ["hero", "hook", "problem", ["mechanism", "how-it-works"], "reviews", "offer-bridge", "faq", "closing-cta"],
  "recommended_sections": ["dateline", "founder-note", "guarantee"],
  "forbidden_sections": ["announcement", "header", "product-grid", "countdown", "stock-indicator"],
  "nav": "none",
  "price_above_fold": "forbidden",
  "cta": { "min": 1, "max": 3, "first_after_section": 4, "sticky": "optional", "copy_pattern": "next-step" },
  "proof": { "min_modules": 2, "max_modules": 4, "required_kinds": ["review-quote"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count"] },
  "imagery": { "required_jobs": ["identity", "in-use", "result-or-context"], "hero": "editorial-lifestyle", "video": "optional", "min_images": 4 },
  "copy_framework": ["story-lead", "pas"],
  "offer_compat": { "allowed": ["first-order", "bundle", "free-shipping"], "forbidden": ["flash-sale", "clearance", "percent-off"] },
  "urgency": "none"
}
```

Field rules:

- `mandatory_sections`, `recommended_sections`, `forbidden_sections`: canonical
  ids from the vocabulary below. An inner array means "any one of these".
  A manifest section id `x` satisfies id `y` when `x == y` or `x` starts with
  `y + "-"` (so `reviews-skin-type` satisfies `reviews`).
- `nav`: `none` (logo only, not clickable), `minimal` (logo + one utility
  link), `full`.
- `price_above_fold`: `required`, `optional`, `forbidden`.
- `cta.first_after_section`: 0 means the first CTA is in the hero.
- `cta.sticky`: `required`, `optional`, `forbidden`.
- `cta.copy_pattern`: `add-to-cart`, `claim-offer`, `next-step`,
  `start-quiz`, `join-waitlist`, `subscribe`, `shop-collection`,
  `read-results`.
- `proof.*_kinds`: from the proof vocabulary below.
- `imagery.hero`: `packshot`, `product-in-hand`, `product-in-context`,
  `editorial-lifestyle`, `video-poster`, `typographic`, `grid`,
  `ugc-screenshot`. Before/after media never leads a hero
  (`references/proof/proof-ledger.md`, display rule 9).
- `imagery.video`: `required`, `optional`, `forbidden`.
- `copy_framework`: `pas`, `aida`, `bab`, `4ps`, `fab`, `story-lead`,
  `listicle`, `comparison`, `hook-story-offer`, `answer-first`,
  `qualifier-lead`.
- `offer_compat.allowed` / `forbidden`: offer ids from
  `references/offers/offer-types.md`, exactly: `none`, `percent-off`,
  `fixed-off`, `bogo`, `gwp`, `free-shipping`, `tiered-volume`, `bundle`,
  `bundle-decoy`, `subscribe-save`, `first-order`, `referral`, `loyalty`,
  `cashback`, `bnpl`, `trial-sample`, `mystery`, `pre-order-price`,
  `price-lock`, `flash-sale`, `clearance`, `limited-edition`, `gift-card`,
  `student-military`, `charity`. Hero placement and countdown rules are not
  offer ids; they live in `price_above_fold` and `urgency`.
- Campaign ids (manifest `campaign.type`) come from
  `references/offers/campaign-calendar.md`: `evergreen`, `launch`, `restock`,
  `seasonal`, `gifting`, `flash-sale`, `clearance`, `collab-drop`,
  `anniversary`, `cause`, `back-to-school`, `bfcm`, `end-of-season`,
  `founder-sale`.
- `urgency`: `none`, `verified-only`, `encouraged` (still verified).
- Every checklist value is the type's default, not a hard limit. A plan that
  deviates records the field, the new value and the reason under
  "Deviations from the type default".
- `awareness`: `unaware`, `problem-aware`, `solution-aware`,
  `product-aware`, `most-aware`.
- `funnel_stage`: `tof`, `mof`, `bof`, `retention`.

## Canonical section id vocabulary

Use these ids (or `id-suffix`) in plans, manifests and `<!-- section: id -->`
delimiters. Add a new id only by adding it here.

| Group | Ids |
|---|---|
| Chrome | `announcement`, `header`, `footer`, `sticky-cta`, `legal` |
| Opening | `hero`, `dateline`, `hook`, `toc`, `qualifier` (who this is / is not for) |
| Trust strip | `trust-bar` (shipping, returns, guarantee facts), `press-marquee` (linked media logos), `stats` (verified numbers), `certifications` |
| Narrative | `problem`, `agitation`, `discovery`, `story`, `founder-note`, `about`, `values`, `mission` |
| Explanation | `solution`, `mechanism`, `how-it-works`, `benefits`, `features`, `ingredients`, `specs`, `materials`, `sourcing`, `science`, `methodology`, `routine`, `usage`, `results-timeline` |
| Product | `gallery`, `buy-box`, `product-hero`, `variant-picker`, `size-guide`, `product-grid`, `product-spotlight`, `list-item`, `lookbook`, `shop-the-look`, `cross-sell`, `bundle-builder`, `quantity-breaks`, `subscription-toggle`, `plan-selector` |
| Offer | `offer`, `offer-bridge` (advertorial hand-off to product), `pricing`, `savings-math`, `gift-options`, `delivery-cutoff`, `countdown`, `stock-indicator`, `bnpl-line`, `shipping-returns`, `guarantee`, `payment-options` |
| Proof | `review-summary` (stars + count), `reviews`, `testimonial-spotlight`, `ugc-grid`, `video-testimonials`, `before-after`, `expert-endorsement`, `press-quotes`, `case-study`, `awards`, `community-count` |
| Comparison | `comparison`, `us-vs-them`, `alternatives`, `verdict`, `winner` |
| Interaction | `quiz`, `quiz-results`, `product-finder`, `calculator`, `video`, `shoppable-video`, `email-capture`, `sms-capture`, `waitlist-form`, `referral-form`, `giveaway-entry` |
| Closing | `faq`, `objections`, `closing-cta`, `final-offer`, `post-purchase-next-steps`, `related-reads`, `disclaimer` |

## Proof kind vocabulary

`review-summary`, `review-quote`, `review-list`, `review-with-media`,
`external-verified-quote`, `ugc-photo`, `ugc-video`, `creator-video`, `before-after`, `expert-quote`,
`founder-note`, `press-logo-linked`, `press-quote-linked`, `certification`,
`award`, `test-data`, `customer-count`, `sales-count`, `repeat-rate`,
`guarantee`, `policy-fact`, `case-study`, `community-screenshot`,
`social-proof-popup` (never), `live-viewer-count` (never), `stock-count`
(verified only), `press-logo-unlinked` (never).

## Image job vocabulary

`identity`, `detail`, `scale`, `texture`, `in-use`, `context`, `variation`,
`included-items`, `sequence`, `result-or-context`, `ingredient-or-material`,
`packaging`, `founder-or-team`, `ugc`, `diagram`, `comparison-visual`,
`gift-presentation`, `size-reference`, `swatch`, `label-or-facts-panel`.

---

# Reviews Sourcing

The tiered procedure that fills the review rows of the plan's `## Proof
ledger` (`references/proof/proof-ledger.md`). `/plan-page` runs tiers 0 to 3
against Lexsis before any template or asset call; tiers 4 and 5 run only when
tiers 1 to 3 return nothing usable. Output is ledger rows, never page copy.
Rule tags: LAW (statute, regulator, platform terms), RESEARCH (with [H]
academic or regulator, [M] large survey with method, [L] vendor or
practitioner), OPERATOR (Lexsis contract), HEURISTIC (house judgement).

Definitions. `n` is the count of published, product-matched reviews the API
returns for the exact product or active collection. `avg` is the arithmetic
mean of all published ratings for that scope, never of a `minRating` subset.
"Usable" means a row can reach `verified` under the ledger's per-kind table.

## Tier 0: read status

| Step | Call | Read | Then |
|---|---|---|---|
| 0.1 | `lexsis_catalog.reviews_status` | source connected (Judge.me), imported count, last sync | connected and count > 0: tier 1. Otherwise: tier 4 |
| 0.2 | write "Proof sources" line in `page plan` | source, count, sync date, tier reached | always, even when the answer is "none" |

## Tier 1: active collections

| Step | Call | Read | Then |
|---|---|---|---|
| 1.1 | `lexsis_catalog.review_collections` with `collection_status: "active"` | id, name, `item_count`, product scope | list them with counts in plan question 9 |
| 1.2 | `lexsis_catalog.review_collection_items` for the chosen collection | rating, body, author, date, media, verified flag | one `review-quote` or `review-list` row per rendered item, `collectionId` recorded |
| 1.3 | no active collection fits | | tier 2; optionally `lexsis_drafts.review_collection_create` as a draft shortlist, only when the user asks |

Only `active` collections serve on published pages. A draft the agent creates
is `pending` in the ledger until the merchant activates it in Storefront,
Reviews, Collections. If the host returns `UNKNOWN_ACTION`, ask the merchant
to paste a collection id.

## Tier 2: product reviews via the API

| Step | Call | Read | Ledger use |
|---|---|---|---|
| 2.1 | `lexsis_catalog.reviews` with `product_id`, `limit: 100` | total `n`, `avg`, newest date | `review-summary` row: avg, n, min rating present, as-of date |
| 2.2 | same with `rating_min: 5`, `4`, `3`, `2`, `1` (or read the distribution the response carries) | per-star counts | distribution for the summary; confirms no band is missing |
| 2.3 | same with `has_media: true` | count of photo or video reviews | `review-with-media` rows; UGC grid eligibility |
| 2.4 | same with `source_type` | Shop vs app vs import | verified badge semantics per source (RS10) |

### Count bands

| Band | n | Show | Do not show | Evidence |
|---|---|---|---|---|
| B0 | 0 | nothing review-shaped; go to tier 4 | stars, "loved by customers", placeholder cards | 45% will not buy with no reviews, PowerReviews 2023 n=8,153 [M] |
| B1 | 1 to 4 | individual cards, verbatim, fields present in data; "n reviews" text link | any average, star summary, distribution, carousel | 56% chose 4.5 from 12 ratings over 5.0 from 2, Baymard n=670 [H]; Baymard: hide the summary at 5 or fewer ratings [H] |
| B2 | 5 to 19 | avg to one decimal with n beside it every time; carousel of 3 to 6 cards; verified badge where data has it | distribution below 10 (optional 10 to 19); "rated 5.0" headline styling | most lift arrives by 5 reviews, Spiegel 2017 [H, single retailer, unreplicated] |
| B3 | 20 to 99 | avg + n; distribution bars as filters, expanded; sort control; at least one review of 3 stars or lower reachable without filtering when one exists | five-star-only carousel with no path to the rest | distribution used more than review text, Baymard [H]; 53% seek negative reviews, Baymard [H] |
| B4 | 100+ | everything in B3 plus media filter, attribute filters, merchant replies, corpus summary labelled as generated | aggregating other sites into the same average | conversion lift grows with displayed count to 1,000+, PowerReviews 8.8M pages [M, correlational] |

Spiegel found ratings of 4.2 to 4.7 convert better than 4.7 to 5.0
(https://spiegel.medill.northwestern.edu/how-online-reviews-influence-sales/).
That describes shopper psychology. It is never a target: removing five-star or
low-star reviews to land in the band is suppression (RS9).

### Display decision table

Module shape by band and page type (`references/page-types/_index.md`). Every
module is a ledger row; proof density stays inside the type checklist.

| Page type | B1 (1 to 4) | B2 (5 to 19) | B3 (20 to 99) | B4 (100+) |
|---|---|---|---|---|
| `ad-landing-page`, `pdp-hybrid-landing` | "n reviews" link near price; one quote beside the primary claim | avg + n near price; carousel 3 to 6; last-word quote above final CTA | as B2 plus "Read all n reviews" to a list | as B3; media filter |
| `pdp` | "n reviews" near title; cards mid-page | avg + n near title; carousel or short list | avg + n; distribution + list with filters mid or low page | full module with media and attribute filters, replies |
| `advertorial`, `video-sales-page` | one dated quote after the mechanism | two or three dated quotes inline, never a carousel | as B2 plus avg + n at the offer bridge | as B3 |
| `listicle` | one quote under the reason it matches | one quote per reason where a matching review exists; avg + n at the close | as B2 | as B2 |
| `comparison-us-vs-them` | none or one quote that names the alternative | avg + n near the verdict; quotes that name the alternative | as B2 | as B2 |
| `seo-buyers-guide` | one quote under the ranked entry it matches, labelled by product | per-entry avg + n labelled by product in the comparison table; never one guide-level average | as B2 | as B2 |
| `bundle-kit` | component quotes labelled by product | component avg + n labelled by product; no bundle average unless reviews are bundle-specific | as B2 | as B2 |
| `ugc-creator-collab` | none | `review-with-media` cards only, 3 to 6 | media grid 6 to 12 | as B3 |
| `restock`, `retargeting-warm` | one dated quote answering the objection | avg + n plus one objection quote | as B2 | as B2 |
| `launch-waitlist-preorder`, `thank-you-post-purchase`, `faq-support-led`, `lead-capture-giveaway` | none | none or a store-level avg + n labelled as store rating | as B2 | as B2 |
| luxury vertical (`references/vertical-luxury.md`) | one long-form quote | one long-form quote; no carousel, no counts | as B2 | as B2 |

### Review anatomy: field gating

Render a field only when the record contains it. Never fill a gap.

| Field | Render only if | Rendering |
|---|---|---|
| Rating | `rating` present, integer 1 to 5 from the author | as given; never recalculated (IS 19000 cl. 5.7.3) |
| Body | `body` present | verbatim; `[...]` trim only; "Read more" reveals the full text |
| Title | `title` present | verbatim |
| Name | `reviewer_name` present | first name + last initial, or as the app displays it publicly |
| Location | `location` present | city or region as stored |
| Date | `created_at` present | month and year at minimum; always shown |
| Verified badge | record links to an order, or `verified: true`, or Shop source | the app's own semantics; never on a CSV import without order linkage |
| Photo or video | media URL present and app terms cover display | native aspect; no crop that removes product or watermark |
| Variant | `variant` present | "Size M, Olive" |
| Recommends | explicit boolean present | text plus icon; never inferred from rating |
| Merchant reply | reply present | visually distinct, labelled as the store's reply |
| Incentivised | app flag present | "Incentivised review" label on the card and beside the summary |
| Source | always | "via Judge.me" or "via Shop"; third-party sources link out |

Never render: an avatar that is not the reviewer's, a stock face implied to be
the reviewer, a generated name, date or verified tick.

## Tier 3: proof-proximity candidates

| Step | Call | Read | Then |
|---|---|---|---|
| 3.1 | for each of the plan's three decision questions, `lexsis_catalog.reviews_search` with `query` = the claim in the shopper's words | candidate reviews with ids | row per candidate, status `pending`, section = the claim's section |
| 3.2 | `lexsis_catalog.reviews` by id (or the item in an active collection) | full record | confirm verbatim text, date, fields |
| 3.3 | plan question 9 lists candidates with a one-line excerpt | merchant confirms or an active collection already contains the item | status `verified`; else the row stays `pending` and does not render |

Semantic search returns candidates, not selections. A candidate that mentions
a limitation ("took two weeks", "runs small") is preferred over pure praise.

## Tier 4: zero-review playbook

Run only when tiers 1 to 3 return zero usable rows for both product and store.
Everything here produces evidence for the merchant and a consent shortlist;
only an `external-verified` row reaches the page.

```text
ZERO_REVIEW(store, product):
 1. Shop app reviews. Ask the merchant whether Shop reviews exist (Shopify admin,
    Shop, Reviews). Shop reviews are purchase-verified by construction and sync
    into Judge.me with a non-removable "Verified by Shop" badge.
    STOP if the sync brings n > 0: rerun tier 0.
 2. Brand-owned channels. Ask for: existing testimonials page (must hold evidence
    of genuineness and contact details, CAP 3.45); comments on the brand's own
    Instagram, TikTok or YouTube posts; customer emails, DMs or WhatsApp.
    The author owns each comment or message. Build a consent shortlist: post
    URL or message date, author handle, proposed quote, channels, duration.
    STOP the item until a recorded written "yes" exists (template in
    `references/proof/ugc-rights-and-display.md`).
 3. Public third-party sources. Search "<brand>" "<product>" reviews on each
    source in the table below. Record URL, date, count, rating, handle.
    Apply the per-source rule. Verify the author bought or used the product
    (EU Annex I 23b; FTC bona fide user); if unverifiable, at most a link.
 4. Decide. If at least one item has (a) platform-permitted reuse, (b) merchant
    written approval, (c) verbatim text, (d) live URL and attribution the
    platform allows: ledger row kind `external-verified`, section
    `testimonial-spotlight` captioned "What people are saying elsewhere" with
    the source named and linked. Never blended into an on-site average.
    STOP. Else tier 5.
```

| Source | May reach the page as | Evidence for the merchant only | Never |
|---|---|---|---|
| Shopify Shop app | synced reviews through tier 1 to 2 with the Shop badge | | copying Shop text outside the synced app |
| Brand site testimonials | quote with evidence of genuineness and contact details on file | | undocumented quotes |
| Brand Instagram or TikTok comments and tagged posts | quote or embed with the author's scoped written consent recorded | shortlist to request consent | a tag or hashtag treated as a licence; platform-licensed music |
| YouTube | official embed of a creator video with the creator's written permission and connection disclosed | shortlist | downloading or re-hosting; quoting comments |
| Customer emails, DMs, WhatsApp | quote with explicit consent for that quote, channel and duration; phone numbers, surnames, avatars redacted; channel and month labelled | shortlist | fabricated chat UI; screenshots without consent |
| Trustpilot | live TrustBox widget on a paid plan; free plan is a plain text link; quotes need reviewer permission or full anonymisation | aggregate and count | static star image; product-score widget on a landing page (Trustpilot brand guidelines Sep 2026) |
| Google Business Profile | Places API with author name, avatar, profile link, link to the source review, no caching, Google logo when off-map | aggregate and count | screenshots; feeding into the site average; expecting rich-result stars |
| Amazon | one dated text line "Rated 4.6/5 by 2,140 Amazon customers (as of Sep 2026)" with a link, screenshot on file | aggregate, themes, objections | verbatim review text; "Best Seller" or "Amazon's Choice" badge art (Amazon trademark licence) |
| Flipkart, Nykaa, Myntra | as Amazon (terms not fetched; applied by analogy) | aggregate, themes | verbatim text |
| Reddit | "Discussed on r/<sub>" with a link; a quote only with the author's written permission | objections, vocabulary | quoting without permission; any use in ads (Reddit Embeds Terms) |
| Creator videos (any platform) | hosted or embedded only with scoped written consent that names "website"; "Paid partnership" when paid | shortlist | organic consent stretched to ads or whitelisting |

## Tier 5: substitutes when no review row exists

Use in this order and stop at the first that verifies. Each is its own ledger
kind; none is review-shaped.

| Order | Kind | Minimum evidence | File |
|---|---|---|---|
| 1 | `guarantee`, `policy-fact` | policy page URL, exact terms (days, conditions, refund vs credit) | `references/offers/offer-ledger.md` |
| 2 | `certification` | issuer, certificate or licence number, scope, current | `references/proof/trust-badges-certifications.md` |
| 3 | `test-data` | lab or study report with method, n, date; numbers copied exactly | `references/proof/before-after-and-claims.md` |
| 4 | `founder-note` | named founder, role stated, approved text, no invented customer voices | `references/proof/before-after-and-claims.md` |
| 5 | `press-quote-linked`, `press-logo-linked` | fetched editorial URL naming the brand | `references/proof/press-and-media-mentions.md` |
| 6 | "first customers" programme | offer terms in the offer ledger; adequate stock (India CCPA bait rule); copy states reviews open after delivery | `references/offers/offer-ledger.md` |
| 7 | nothing | a page without proof is honest; a page with invented proof is a liability | |

## Rules

RS1. Never render a review element that is not a ledger row from tiers 0 to 3 or an `external-verified` row from tier 4. OPERATOR.
Check: each authored review island's `application/json` child binds the
confirmed collection or product scope using its live schema. Every static
quote id appears in the ledger. Inspect source-format JSON, not compiled
`data-props` markers in the source file.

RS2. Run tiers in order and stop at the first tier that yields usable rows; never open tier 4 while tier 1 or 2 has data. OPERATOR.
Check: the plan's "Proof sources" line names the tier reached and the calls made.

RS3. Show an average only at n >= 5, always beside n, to one decimal, computed from all published ratings for the scope. RESEARCH [H] Baymard; LAW (a headline 5.0 from two ratings is misleading by omission, FTC 465.7, CMA "publishing in a misleading way").
Check: every rating string is followed by a count in the same element (review the hits; prices also match the pattern).

RS4. Never show 5.0 unless every review is five stars and n >= 20; never show two decimals. HEURISTIC, mirrors `proof-ledger.md` display rule 3.

RS5. Show the distribution at n >= 20 (optional at 10 to 19, hidden below 10), expanded, every bar present including one-star, bars acting as mutually exclusive filters. RESEARCH [H] Baymard distribution summary.
Check: in the hosted draft the distribution element exists when the ledger's n >= 20 and lists five bars.

RS6. Recency gate: when the newest review is older than 12 months, do not place the average in the hero or buy box; render dated cards only. RESEARCH [M] PowerReviews (64% prefer fewer recent reviews), BrightLocal 2026.
Check: ledger `review-summary` row records newest date; if older than 12 months, section is not `hero`, `buy-box` or `review-summary`.

RS7. Never relabel a store-level aggregate as a product rating, never average bundle components into a bundle rating, never merge reviews across substantially different products or formulations. LAW FTC 465.3; CMA208 "porting"; FTC v. Bountiful ($600k, 2023).
Check: each `review-summary` row names the exact `product_id` or `collectionId` its numbers came from.

RS8. A `minRating` filter is allowed only on a carousel that is labelled as a selection ("Selected reviews"), links to the full list ("Read all n reviews"), and sits with an unfiltered avg + n. Never on the full list, never for `averageRating` or `totalReviews`. LAW FTC 465.7(b); DMCC banned practice 13.

RS9. Negative reviews stay reachable: at n >= 20 at least one review rated 3 or lower is visible without filtering when one exists; sort default is disclosed in one line and does not bury low ratings. LAW FTC 465.7; FTC v. Fashion Nova ($4.2M, 2022); IS 19000 (no discouraging negatives). RESEARCH [H] Baymard: presence of negatives makes positives believable.
Check: hosted draft at 1280 shows the sort label and, for B3+, at least one card with rating <= 3 in the default view.

RS10. Render each review field only when the record contains it (field-gating table). Verified badge only with order linkage or Shop source. LAW EU Annex I 23b (verification is material information); Shopify Shop badge semantics.
Check: no `verified` prop set to true on a static item whose ledger row lacks order linkage; no `avatar` URL that is not the reviewer's own media.

RS11. Quote verbatim. Trim with `[...]` only; keep the reviewer's specifics (variant, timeframe, use); prefer a quote that includes a limitation; never stitch sentences from two reviews; never fix grammar. LAW CAP 3.47; Trustpilot "quote reviews exactly as written"; IS 19000 (administrator may not edit content).
Check: each `review-quote` body is a substring of the API record with `[...]` removed.

RS12. Render merchant replies when present, visually distinct and labelled as the store's reply. RESEARCH [H] Baymard: 37% weigh the reply; 87% of sites never reply.
Check: reply markup uses a distinct class and the label "Reply from <store>".

RS13. Label incentivised reviews on the card and beside the summary when the app flags them; incentives may never be conditioned on sentiment. LAW FTC 465.4 and 465.5; CMA208; Google review-snippet policy.

RS14. Review islands take `collectionId` or `productIds`, `minRating`, `pageSize` <= 12; `averageRating` and `totalReviews` come only from the API total for the same scope; never `reviewsEndpoint`; never `SocialProofPopup`. OPERATOR.

RS15. Only `active` collections bind to `collectionId`; a draft collection is `pending` until the merchant activates it. The plan never activates a collection. OPERATOR.
Check: the `collectionId` in source matches an id returned with `collection_status: "active"` on the plan date.

RS16. `reviews_search` hits are `pending` until the merchant confirms them or an active collection contains them. OPERATOR.
Check: every row with source `reviews_search` has status `verified` only with a confirmation note (question 9 answer or collection id).

RS17. In band B0 render nothing review-shaped. An external item reaches the page only as `external-verified` with a live URL, platform-permitted reuse, merchant written approval, and verbatim text. Marketplace review text (Amazon, Flipkart, Nykaa, Myntra) is never verbatim; Reddit is never used in ads. LAW Amazon Conditions of Use; Reddit User Agreement and Embeds Terms; CAP 3.45.
Check: no `review-*` kind in the ledger when `reviews_status` count is 0; each `external-verified` row has four evidence fields.

RS18. When B0 persists after tier 4, use tier 5 substitutes in order; "nothing" is an acceptable outcome. HEURISTIC.
Check: plan records the substitute chosen and why the higher rows were unavailable.

RS19. Never write, paraphrase, summarise as if quoted, or generate a review; never present staff or founders as customers; never reuse a review for a different product. LAW FTC 16 CFR 465.2 and 465.5; FTC v. Rytr 2024; FTC v. Sunday Riley 2020; India E-Commerce Rules 2020 r.5(2).

RS20. Autoplay video reviews muted only; sound on tap; captions present. LAW WCAG 2.1 SC 1.4.2.

## Regulatory spine

| Jurisdiction | Instrument | In force | Bites on | Penalty | URL |
|---|---|---|---|---|---|
| US | FTC Consumer Reviews and Testimonials Rule, 16 CFR 465 | 21 Oct 2024 | fake or AI reviews (465.2), porting (465.3), sentiment-conditioned incentives (465.4), undisclosed insiders (465.5), suppression (465.7), bought indicators (465.8) | civil penalties per knowing violation | https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials |
| US | FTC Endorsement Guides, 16 CFR 255 | 26 Jul 2023 revision | atypical results (255.2(b)), procuring or editing reviews (255.2(d)), experts (255.3), material connections (255.5) | Section 5 FTC Act; > $50,000 per violation under penalty offence notices | https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising |
| UK | DMCC Act 2024 Sch. 20 banned practice 13; CMA208 | 6 Apr 2025 | fake or concealed incentivised reviews; publishing reviews in a misleading way; no reasonable steps to prevent them | CMA fines up to 10% of global turnover | https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices |
| UK | CAP Code 3.45 to 3.48 | current | evidence and contact details for each testimonial; permission; relates to the advertised product | ASA ruling, ad withdrawn, referral | https://www.asa.org.uk/advice-online/testimonials-and-endorsements.html |
| EU | Directive 2019/2161 amending UCPD, Annex I 23b and 23c, Art. 7(6) | 28 May 2022 | claiming reviews are from purchasers without verification; fake reviews; verification method is material information | national penalties | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32019L2161 |
| India | CPA 2019; CCPA Misleading Ads Guidelines 2022 | 9 Jun 2022 | endorsements must be genuine and current; disclaimers cannot cure | ₹10 lakh first, ₹50 lakh repeat; endorser ban 1 to 3 years | https://consumeraffairs.nic.in/theconsumerprotection/guidelines-prevention-misleading-advertisements-and-endorsements-misleading |
| India | Consumer Protection (E-Commerce) Rules 2020 r.5(2), 7(2) | 2020 | sellers may not pose as consumers and post reviews | CPA 2019 | https://taxguru.in/corporate-law/consumer-protection-e-commerce-rules-2020.html |
| India | BIS IS 19000:2022 | voluntary; QCO proposed May 2024 | no editing review content or ratings; publish moderation criteria; no discouraging negatives | certification of process | https://www.bis.gov.in/scheme-online-review-feb-26/ |

## Sources

- Spiegel Research Center 2017: https://spiegel.medill.northwestern.edu/how-online-reviews-influence-sales/ ; critique: https://cleancommit.io/blog/do-product-reviews-increase-conversion-rate/
- Baymard: https://baymard.com/blog/sort-by-customer-ratings ; https://baymard.com/blog/user-ratings-distribution-summary ; https://baymard.com/blog/respond-to-negative-user-reviews
- PowerReviews: https://www.powerreviews.com/power-of-reviews-2023/ ; https://www.powerreviews.com/right-volume-of-reviews/ ; https://www.powerreviews.com/review-volume-and-recency/
- BrightLocal 2026: https://www.brightlocal.com/research/local-consumer-review-survey/
- FTC FAQ on the reviews rule: https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers
- FTC v. Fashion Nova: https://www.ftc.gov/news-events/news/press-releases/2022/01/fashion-nova-will-pay-42-million-part-settlement-ftc-allegations-it-blocked-negative-reviews
- FTC v. Rytr: https://www.ftc.gov/news-events/news/press-releases/2024/12/ftc-approves-final-order-against-rytr-seller-ai-testimonial-review-service-providing-subscribers
- FTC v. Sunday Riley: https://www.ftc.gov/news-events/news/press-releases/2020/11/ftc-approves-final-consent-agreement-sunday-riley-modern-skincare-llc
- FTC v. Bountiful: https://techcrunch.com/2023/04/10/ftc-orders-supplement-maker-to-pay-600k-in-first-case-involving-hijacked-amazon-reviews/
- CMA208 fake reviews guidance: https://assets.publishing.service.gov.uk/media/67eeb64fe9c76fa33048c790/CMA208_-_Fake_reviews_guidance.pdf
- IS 19000:2022 text: https://www.medianama.com/wp-content/uploads/2022/12/19000_2022.pdf
- Shopify Shop reviews: https://help.shopify.com/en/manual/online-sales-channels/shop/product-reviews ; partner sync: https://help.shopify.com/en/manual/online-sales-channels/shop/product-reviews/sync-partner-apps
- Trustpilot brand guidelines: https://uk.corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026 ; showcasing reviews: https://help.trustpilot.com/s/article/Share-and-showcase-reviews
- Google Places policies: https://developers.google.com/maps/documentation/places/web-service/policies ; review snippet: https://developers.google.com/search/docs/appearance/structured-data/review-snippet
- Amazon Conditions of Use: https://www.amazon.com/gp/help/customer/display.html?nodeId=GLSBYFE9MGKKQXXM ; trademark licence: https://buywithprime.amazon.com/legal/trademark-license
- Reddit: https://redditinc.com/policies/user-agreement ; https://redditinc.com/policies/embeds-terms
- YouTube terms: https://www.youtube.com/static?template=terms ; Instagram terms: https://help.instagram.com/581066165581870/
- WCAG 1.4.2: https://www.w3.org/WAI/WCAG21/Understanding/audio-control.html

---

# Proof Ledger

Every trust element a page shows (a star, a count, a quote, a logo, a badge,
a photo of a customer, a "clinically tested" line) is a row in the plan's
`## Proof ledger` before design begins. `/design-page` renders only ledger
rows and fails hosted QA on any proof element not in the ledger; `/optimize`
may add proof only by adding a row first. This file
defines the block, the verification each kind needs, and the display rules.
Sourcing procedures live in `references/proof/reviews-sourcing.md` and the
sibling files.

## The block

```markdown
## Proof ledger

| # | Kind | Supports claim | Source | Evidence | Verified | Section | Status |
|---|---|---|---|---|---|---|---|
| P1 | review-summary | overall quality | lexsis_catalog.reviews product gid://.../123 | 4.6 avg, 212 reviews, min rating 1 | API 2026-09-10 | review-summary | verified |
| P2 | review-quote | "no more 3pm crash" | collection 7f2e... item 9a1c... | verbatim text, name initial + city as stored, 2026-04-02 | API | benefits | verified |
| P3 | press-logo-linked | credibility | Vogue India | https://www.vogue.in/... (article names the brand) | fetched 2026-09-10 | press-marquee | verified |
| P4 | certification | "FSSAI licensed" | merchant | licence no. 1001...; issuer FSSAI | merchant doc | trust-bar | verified |
| P5 | ugc-video | in-use proof | creator @..., rights email 2026-08-21 | asset id ... | merchant consent | ugc-grid | verified |
| P6 | customer-count | "50,000+ customers" | merchant | Shopify orders export, 51,204 unique customers to 2026-08-31 | merchant doc | stats | pending |
| P7 | before-after | "visible in 4 weeks" | merchant | none supplied | none |  -  | dropped |
```

Columns:

- **Kind**: one id from the proof kind vocabulary in
  `references/page-types/_checklist-format.md`.
- **Supports claim**: the exact page claim this proof stands beside. Proof
  without a claim is decoration; drop it.
- **Source**: the system, person or publication that holds the evidence.
- **Evidence**: the id, URL, count, document, or verbatim text.
- **Verified**: how and when (API date, fetched URL, merchant document,
  consent record). "Merchant says" is `pending` until a document or written
  confirmation exists.
- **Section**: the canonical section id where it renders.
- **Status**: `verified`, `pending` (may not render), `dropped` (with reason
  in the row).

## Verification required per kind

| Kind | Minimum evidence before `verified` | Never |
|---|---|---|
| review-summary | `lexsis_catalog.reviews` total and average for the exact product or collection; count >= 5 to show an average, >= 1 to show a count | rounding 4.3 to 5.0; "5.0" with under 20 reviews; stars without a count |
| review-quote / review-list / review-with-media | row exists in `lexsis_catalog.reviews` or `review_collection_items`; text verbatim; attribution exactly as stored; date present | edited wording beyond `[...]` trimming; invented names, cities, photos; five identical five-star quotes |
| external-verified-quote | public URL, platform terms allow reuse, merchant written approval, verbatim text, attribution the platform allows; manifest `reviews.source: external-verified` | marketplace text that the platform's terms forbid copying; quotes from DMs without consent |
| ugc-photo / ugc-video / creator-video | asset id in the library, rights record (email, contract, platform rights request), creator handle, paid disclosure flag when paid | stock people as customers; generated people; content without rights |
| before-after | merchant-supplied, same subject, same framing and lighting, unretouched, timeframe stated, consent, category permitted (`references/proof/before-after-and-claims.md`) | generated, composite, or "illustrative" results; medical outcomes without substantiation |
| expert-quote / founder-note | named person, credential verifiable, written approval, material connection disclosed | anonymous "doctors recommend"; invented titles |
| press-logo-linked / press-quote-linked | fetched article URL that names the brand or product; not a press release wire; paid placements disclosed as such | logos without a URL; "as seen in" for a wire release; podcast without episode link |
| certification / award | issuer, certificate or licence number, scope, current date; exact issuer wording (`references/proof/trust-badges-certifications.md`) | "FDA approved" for anything FDA does not approve; "dermatologist tested" without a test report; generated badge art |
| test-data / case-study | document or URL with method, sample, date; numbers copied exactly; disclaimer where required | "clinically proven" from an ingredient supplier's study applied to the product |
| customer-count / sales-count / repeat-rate | merchant export or analytics screenshot with date; rounded down; phrase "over N" | invented, rounded up, or extrapolated numbers |
| guarantee / policy-fact | store policy page URL or merchant confirmation; exact terms | "free returns" when returns cost; "lifetime" without terms |
| community-screenshot | platform, date, consent from the poster (or public brand-owned content) | screenshots of paid or fake accounts |
| stock-count | live `lexsis_catalog.get` inventory read at render time via island binding | fixed numbers in copy |
| social-proof-popup, live-viewer-count, press-logo-unlinked | never verified; never rendered |  -  |

## Display rules

1. **Proof proximity.** A quote or number sits beside the claim it supports,
   not pooled in one "testimonials" block. A standalone reviews section holds
   the breadth (list or carousel); claim-specific rows go inline.
2. **Density.** Modules within the type checklist's `proof.min_modules` and
   `max_modules`. A module is one section or one inline element; the same
   ledger row may render once.
3. **Stars.** Show stars only next to a numeric average and count (count of
   5 or more for an average). Distribution (or "n% recommend"): hidden below
   10 reviews, optional from 10 to 19, required and click-to-filter at 20 or
   more. Use the real average to one decimal; do not show 5.0 unless every
   review is five stars and there are at least 20. No average in the hero or
   buy box when the newest review is older than 12 months (recency gate).
   A filtered carousel (`minRating`) is labelled as a selection, links to the
   full unfiltered list, and sits beside the unfiltered average and count;
   `averageRating` and `totalReviews` are never computed from a filtered set.
4. **Quotes.** Verbatim. Trim with `[...]` only. Keep the reviewer's own
   specifics (product variant, timeframe, use). Attribution exactly as
   stored plus the date. Prefer reviews that mention the claim and, where
   possible, a limitation.
5. **Counts.** Round down, prefix "over", include the as-of month when older
   than 90 days. Never mix units ("customers" vs "orders").
6. **Press.** Monochrome logos at one height, each an `<a>` to the ledger
   URL with the publication as accessible name; three to six logos; caption
   "Press" or "In the press", never "As seen in" unless the outlet actually
   featured the product. Paid placements say "Sponsored feature". Mentions
   older than 24 months drop out (12 months for "as seen in" or "featured").
7. **Badges.** Issuer text next to the mark; monochrome; no generated art;
   one row, three to five badges, never repeated per section.
8. **UGC.** Native aspect (9:16 or 1:1), captions on video, click to play,
   creator handle, "Paid partnership" when paid, rights recorded.
9. **Before/after.** Same crop, labels "Before" and "After" with the
   interval, "Individual results vary" where the category requires it,
   never in the hero, never generated.
10. **Numbers in copy.** Every numeral inside a proof, trust, stats or press
    section appears in the ledger. the source/hosted review lists them; the review
    checks each.

## Fallback order when the ledger is thin

1. Guarantee and policy facts (returns, shipping, warranty) with exact terms.
2. Certifications and licences with issuer.
3. Product evidence: test data, ingredient sourcing, materials, process
   photos.
4. A founder note with a real name and signature.
5. Verified press with links.
6. A "first customers" programme: an honest invitation (early access,
   founder contact, review request) that says the product is new.
7. Nothing. A page with no proof section is honest; a page with invented
   proof is a liability.

---

# Generation policy

The ALLOW / ASK / NEVER model for AI-generated imagery on storefront pages.
It governs `lexsis_drafts.asset_generate` and any external generator
(image or video) reached through another MCP. `/plan-page` may plan a slot for
generation only from the ALLOW list; `/design-page` generates ALLOW slots after
credit confirmation and ASK slots only with the merchant's explicit yes; NEVER
items are not generated under any instruction. The only way to fill a NEVER
slot is for the merchant to supply real media through
`references/assets/asset-sourcing-sequence.md`. Prompt mechanics and
compositing recipes are in `references/design-enrichment.md`; where that file
suggests a prompt this policy forbids (gradient washes, hands holding the
product, generic lifestyle scenes), this policy wins.

Tags: LAW, RESEARCH, OPERATOR, HEURISTIC as defined in
`references/assets/image-jobs-by-page-type.md`.

## 1. What the MCP accepts

| `purpose` | `aspect` options | Output px | Transparent | Class |
|---|---|---|---|---|
| `hero_bg` | `landscape` | 1536 x 1024 | no | ALLOW |
| `hero_bg` | `portrait` (mobile crop) | 1024 x 1536 | no | ALLOW |
| `section_bg` | `landscape` | 1536 x 1024 | no | ALLOW |
| `card_bg` | `square` | 1024 x 1024 | no | ALLOW |
| `texture_fill` | `square`, seamless | 1024 x 1024 | no | ALLOW |
| `pattern_tile` | `square`, seamless | 1024 x 1024 | no | ALLOW |
| `decorative_element` | `square` | 1024 x 1024 | yes, separate provider | ALLOW |
| `product_composite` | `square` or `portrait` | 1024 x 1024 or 1024 x 1536 | no | ALLOW only over a real cut-out passed in `reference_images` |
| `product_lifestyle` | `portrait`, `square`, `landscape` | as above | no | ASK |

`icon_set` is a plan role, not an MCP purpose. It means "author one
monochrome inline SVG set" (one stroke width, 24px grid, `currentColor`),
allowed by N1 and N3 in `references/design-rules.md`. Raster icon generation is
NEVER. Every generated raster is at most 1536 px on its long side; that is
below the hero image minimum in `references/assets/slot-spec.md`, which is why
generation fills backdrops (low detail, cover-cropped) and never product
imagery.

## 2. NEVER

Blocking. No override by prompt, brief, design.md line or user instruction.
The merchant supplying real media is the only exit.

| Id | Never generate | Why | Instead |
|---|---|---|---|
| GN1 | The product itself when Shopify media exists or could exist, including a "cleaner" version of an existing shot | Misrepresentation of colour, size, texture or accessories; feed images must show the real product https://support.google.com/merchants/answer/7052112 ; ASCI draft prohibits exaggerating product features through visual representation https://www.ascionline.in/wp-content/uploads/2026/05/asci-ai-labelling-guidelines.pdf | Step 1 to 4 of the sourcing sequence; slot stays `planned` |
| GN2 | A different-looking or stand-in product when no media exists (pre-launch included) | Same as GN1; ASCI medium tier requires labelling of non-existent products and the shopper cannot tell a render from a photo | Merchant's own render captioned "Rendering; final packaging may vary", or typographic hero |
| GN3 | People presented as customers, reviewers, creators, founders, staff, experts or doctors | Testimonials by someone who does not exist are banned, 16 CFR 465 https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials ; ASCI "fabricating endorsements" and "AI generated fake doctor" are prohibited even if labelled | Real UGC with rights; real founder photo; no section |
| GN4 | Before/after, results, clinical or medical imagery (labs, charts implying efficacy, skin, hair or body change) | Before/after is an objective claim needing substantiation https://www.asa.org.uk/advice-online/before-and-after-photos.html ; "results not typical" does not cure deception https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance | `references/proof/before-after-and-claims.md` |
| GN5 | Press logos, certification badges, awards, seals, payment marks | Endorsement and certification fraud; `references/proof/trust-badges-certifications.md` requires issuer artwork | Issuer or outlet artwork with a ledger row |
| GN6 | Text, prices, labels, headlines, ingredient lists or facts panels inside an image | WCAG 1.4.5 https://www.w3.org/WAI/tutorials/images/ ; Google and Shopify overlay rules https://support.google.com/merchants/answer/6101131 , https://shopify.dev/docs/storefronts/themes/store/requirements | HTML text over the image |
| GN7 | Celebrities, lookalikes or any recognisable real person | Right of publicity; FTC celebrity avatar guidance https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers ; ASCI "likeness without consent" | None |
| GN8 | Competitor products or packaging, or generic products styled to resemble one | Trademark and comparative advertising exposure | Inline SVG silhouette labelled "other brands" |
| GN9 | Anything that will be captioned as a review, UGC, "from our customers" or a customer photo | 16 CFR 465 insiders and fake-review rules | Rights-cleared UGC only |
| GN10 | Unsafe use (baby, pets, tools, dosing) | ASCI prohibited tier "depicts unsafe situations" regardless of label | Real, correct-use photography |
| GN11 | Food, ingredients or formula presented as the merchant's own product or sourcing | GN1 by extension; net-impression deception | Real flat lays; stock raw material only as context |
| GN12 | Anything for the Google Shopping feed image slot or the first gallery position | Feed image must be a real, unobstructed photo https://support.google.com/merchants/answer/7052112 | Shopify media |

## 3. ALLOW

Generated after the merchant confirms the credit spend for the named batch.
Every ALLOW file: no people, no hands, no text, no products, no logos; brand
palette hexes from `lexsis_brand.brand_kit` passed in `brand_colors`;
provenance recorded per section 7.

| Purpose | Aspect | Prompt constraints | Negative list | Placement rule | Alt | Manifest role |
|---|---|---|---|---|---|---|
| `hero_bg` | `landscape` plus `portrait` for the mobile crop | Physical material or place (linen, paper, plaster wall, stone, wood, water, sky); soft depth; matte; a low-detail quiet zone where the HTML headline and CTA sit; luminance variance under 30% in that zone | text, letters, watermark, logo, person, hands, face, product, bottle, package, gradient wash, blob, bokeh, neon glow, 3D render | Only in the hero and only when the hero is the plan's bold moment (N2 full-bleed exception) or the section is typographic; a real cut-out is composited on top or no product is shown; one black-to-transparent legibility overlay at most (N7) | `alt=""`, `aria-hidden="true"` | `hero_bg` |
| `section_bg` | `landscape` | As `hero_bg`; even lower detail | As above | Only in the one full-bleed section the plan names as the bold moment (N2); never behind body copy blocks | `alt=""` | `section_bg` |
| `card_bg` | `square` | Flat material or tone; no objects | As above | Only inside a card that wraps a distinct object per N8 (product, proof artefact, table, form); never behind plain text | `alt=""` | `card_bg` |
| `texture_fill` | `square`, seamless | Abstract material grain (paper, linen, stone); tileable; no recognisable objects | As above plus "pattern of objects" | Page-wide behind the single `--lx-bg-color` at 8% opacity or less, or inside a media object; never per section (N2) | `alt=""` (inline `style` background on a `div`) | `texture_fill` |
| `pattern_tile` | `square`, seamless | Brand motif in one or two palette colours; geometric or botanical line work; tileable | As above | Same as `texture_fill`; never animated (N10) | `alt=""` | `pattern_tile` |
| `decorative_element` | `square`, `transparent: true` | Vector-like silhouette or brush mark in one palette colour; SVG preferred over PNG | As above plus "gradient", "glow", "3D" | At most two per page; never behind text; never floating, pulsing or parallax (N7, N10) | `alt=""`, `aria-hidden="true"` | `decorative_element` |
| `product_composite` | `square` or `portrait` | `reference_images` holds the real Shopify or library cut-out first, then a surface or scene; prompt places the product on the surface with realistic contact shadow; product pixels are not repainted, recoloured, relit beyond global grade or scaled non-uniformly; nothing added that could read as shipped with the product | text, hands, person, second product, brand signage, gift wrap, accessories | Fills `context` jobs only; never `identity`, `variation`, `included-items`, `gift-presentation` or gallery position one; caption "Product photo on a generated background" when the scene is photoreal (a room, a landscape) rather than a plain surface | Informative: "{Product} {variant} on {surface}" | `product_composite` |
| `icon_set` (authored SVG) | 24px grid | One stroke width, `stroke="currentColor"`, `fill="none"`, one size per context | Multi-colour, 3D, raster | Beside a visible text label, `aria-hidden="true"` (N3, A5) | n/a | `icon_set` |

Quality tier: `high` only for `hero_bg`; `medium` for `section_bg`,
`card_bg`, `product_composite`; `low` for `texture_fill`, `pattern_tile`,
`decorative_element` (`references/design-enrichment.md` cost table). House
cap: four generated assets per page (HEURISTIC).

## 4. ASK

Requires the merchant's explicit yes for the named slot in the same reply,
logged in the plan's Generation record with the merchant's words and date.
Never inferred from "go ahead" on the plan as a whole.

| Case | Question to put to the merchant | Conditions if approved |
|---|---|---|
| `product_lifestyle`: a scene around the real product where identity is preserved through a composited cut-out, or the merchant accepts illustrative context | "Slot A7 (in-use, benefits) would be a generated scene with your real product composited in. It will carry an 'AI-generated scene' caption and metadata, cannot be captioned as a customer photo, and Meta will label it if reused in ads. Generate it, or leave the section without an image?" | Visible caption near the image; `alt` names the product and says "generated scene"; never in `ugc-grid`, `reviews`, `testimonial-spotlight` or gallery position one; no people or hands; not for beauty shade or fit claims |
| Generated person or hands with the composited product (a synthetic model) | "This uses a synthetic model. It will be labelled 'AI-generated' and can never be presented as a customer, reviewer or staff. Proceed?" | Label visibly; ASCI medium tier "synthetic influencer" label; EU Art. 50 deep-fake label; never on `pdp` gallery, `ugc-creator-collab`, `brand-story-founder`; skin tone and body claims forbidden |
| Illustration or 3D-render style for the whole page | "The page would use an illustrated look for backdrops and decoration. Product images stay photographic. Accept the style?" | Products remain real photos; `alt` says "illustration"; style recorded in the Design direction block |
| Any generation on a page type whose checklist sets `imagery.hero` to `packshot` or `ugc-screenshot` | "This page type leads with a real product or customer image. Generated backdrops would sit below the hero only. Confirm?" | Hero stays real; generated assets only below the fold |
| Replacing a real but low-quality merchant photo with a composite | Show both; "Keep your photo or use the composite with your product cut out onto a generated surface?" | Original stays in the library; composite follows `product_composite` rules |
| Any batch beyond the four-asset cap or the plan's credit allowance | "This adds N generated assets at M credits (balance B). Proceed?" | Recorded count and cost |

RESEARCH context: when users did not know an image was generated there was no
trust penalty versus stock, but users who suspected generation reacted
negatively (n=77) https://www.nngroup.com/articles/ai-generated-images/ ;
marketers rank AI visuals far below UGC for trust (16% vs 33%)
https://www.nosto.com/blog/new-research-brands-prefer-ugc-for-diversity/ .
Default to real; spend generation on backdrops.

## 5. Prompt constraints for every call

1. Describe a material or place, never a mood word alone ("linen", not
   "premium vibe").
2. Add the negative list from the purpose row verbatim; always include
   "text, letters, logo, watermark, person, hands, face, product".
3. Pass `brand_colors` from `lexsis_brand.brand_kit`; never a default hex
   (N14).
4. Name the quiet zone position (left third, lower half) when HTML text will
   sit on the image.
5. Ask for even, diffuse light and low contrast; the legibility overlay does
   the rest (N7).
6. `style: photography` for backdrops unless the ASK illustration case is
   approved; never `3d_render` for anything near a product.
7. Store the exact prompt, negatives, aspect, style, quality, provider and
   returned asset id in the plan's Generation record.

## 6. Disclosure by jurisdiction

Applies to every generated or composited image on the page. "Metadata" means
`IPTC DigitalSourceType` = `TrainedAlgorithmicMedia` (fully generated) or
`CompositeSynthetic` (real product on generated scene), kept on the original
in the library. Hosts may re-encode and strip metadata, so the library record
and the plan carry provenance as well.

| Jurisdiction or platform | Obligation | What the page does | Tag | Source |
|---|---|---|---|---|
| EU, AI Act Art. 50 (applies 2026-08-02; marking grace to 2026-12-02 for earlier models) | Deployers label deep fakes (AI content resembling real persons, objects, places or events that would appear authentic) clearly at first exposure | ASK-tier realistic scene or human: visible label "AI-generated image" adjacent plus metadata. ALLOW backdrops without people or products: metadata only | LAW | https://digital-strategy.ec.europa.eu/en/factpages/quick-facts-transparency-rules-ai-systems ; https://www.orrick.com/en/insights/2026/08/eu-ai-act-transparency-obligations-for-ai-generated-content-article-50 |
| India, ASCI draft AI labelling guidelines (May 2026), aligned to IT Rules amendment of 2026-02-10 | High tier prohibited even if labelled (fake testimonials, exaggerated results, fake settings, likeness without consent, fake authority); Medium tier label required (synthetic influencers, realistic AI settings, non-existent products); Low tier no label (decorative backgrounds, minor enhancement) | High tier blocked by section 2; Medium tier gets "Created using AI" label; ALLOW backdrops need none | LAW (draft) | https://www.ascionline.in/wp-content/uploads/2026/05/asci-ai-labelling-guidelines.pdf ; https://www.thehindubusinessline.com/info-tech/asci-proposes-risk-based-approach-for-responsible-labelling-on-ads-made-with-ai/article70969237.ece |
| US, FTC 16 CFR 465 and Section 5 | No federal AI label law; deception judged on the net impression including images; fake or AI testimonials banned; NY GBL 396-b requires disclosure of synthetic performers in ads from 2026-06-09 (secondary source, verify) | Section 2 blocks the deceptive cases; synthetic humans labelled anyway | LAW | https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-465-trade-regulation-rule-use-consumer-reviews-testimonials-final-rule ; https://craftshift.com/disclose-ai-generated-product-images-shopify-2026/ |
| UK, ASA/CAP | Visual claims must not exaggerate; before/after follows testimonial evidence rules; retouching of product-relevant areas misleads even with a disclaimer | GN4, GN6 | LAW | https://www.asa.org.uk/advice-online/cosmetics-the-use-of-production-techniques.html |
| Meta ads | Auto-applies an "AI info" label to images created or significantly edited with generative AI; photorealistic AI humans labelled next to "Sponsored" | Expect labels when page assets are reused as ads; keep metadata intact | LAW (platform) | https://www.facebook.com/business/help/1010479435004531 ; https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/ |
| Google Merchant Center | All generated images carry `IPTC DigitalSourceType`; do not strip it; no visible watermark or overlay; feed image is a real photo | Feed image never generated (GN12); metadata preserved on any other image | LAW (platform) | https://support.google.com/merchants/answer/7052112 |
| Shopify | No merchant-facing disclosure rule; Shopify Magic watermarks its own output invisibly; CDN re-encoding may strip IPTC (secondary claim) | Provenance kept in the library record and plan, not only in the file | OPERATOR | https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic/media-generation |

## 7. Recording

Plan (`page plan`), one block after "## Asset slots":

```markdown
## Generation record

| Slot | Purpose | Aspect | Style / quality | Prompt (verbatim) | Negatives | Brand hexes | Provider | Asset id | Metadata set | Visible label | Approved by |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A3 | hero_bg | landscape + portrait | photography / high | "Unbleached linen surface, soft north window light, ..." | text, letters, logo, ... | #F5F0E6, #1F1D24 | lexsis | 2d9a... | TrainedAlgorithmicMedia | none | credits: merchant, 2026-09-10 |
| A7 | product_lifestyle | portrait | photography / medium | "..." | ... | ... | lexsis | 9f01... | CompositeSynthetic | "AI-generated scene" | "yes, generate A7" Aditi 2026-09-10 |
```

Manifest (`page record`): the slot's `assets[]` entry gets
`"sourceType": "lexsis"`, `"assetId"`, `"url"`, `"generated": true`,
`"provider": "<provider>"`, and `role` equal to the purpose. For an approved
ASK slot the role is `product_lifestyle`, the entry also carries
`"askApproved": true`, and the merchant's words live in the plan record
(the type checklist review T8 rejects an ASK role without that flag). Nothing else about
generation enters the page record.

## 8. Generation request checklist

Complete every line with yes before calling `lexsis_drafts.asset_generate`
or any external generator. One no stops the call.

1. The slot exists in the plan's Asset slots table with an id and section.
2. Steps 1 and 2 of the sourcing sequence ran for this slot and found nothing (Source decision will read `library: none`).
3. The purpose is in section 3, or in section 4 with the merchant's yes for this slot quoted in the Generation record.
4. The job the slot fills is `context`, a backdrop, a texture, a decoration or an authored icon set; not an identity-bound job.
5. The page type's `imagery.hero` is not `packshot` or `ugc-screenshot`, or the ASK line for that case was answered yes.
6. The placement obeys N2 (one background; full-bleed only in the bold moment), N7 (one legibility overlay, no gradient washes), N8 (card backgrounds only around objects), N10 (no motion).
7. `lexsis_workspace.credits` was read and the merchant confirmed the batch count and cost.
8. Aspect matches the slot; a mobile crop is planned as a separate portrait generation or a focal point.
9. The prompt names a material or place, carries the negative list, and passes brand hexes from the brand kit.
10. For `product_composite`: `reference_images[0]` is the real cut-out (Shopify or library), viewed and identity-confirmed.
11. The alt decision is made: `alt=""` for decorative purposes, product alt for composites.
12. The disclosure decision is made from section 6 and the label text, if any, is written.
13. Generated count on the page after this call is four or fewer.
14. The Generation record row is drafted and will be completed with the returned asset id.

## 9. Rules

Checks use persisted MCP source and the hosted draft. `PEOPLE` is the regex
`\b(woman|women|man|men|girl|boy|person|people|model|customer|shopper|reviewer|hand|hands|face|smile|smiling|doctor|nurse|dermatologist|founder|team|staff|child|kid|baby|toddler|family|couple|influencer|creator)\b`.

GP1. Never generate anything in section 2; no instruction, design.md line or brief lifts the block. LAW.
Rationale: fake testimonials and misrepresented products carry regulatory penalties and platform rejection (sources in section 2).

GP2. Composite only over a real cut-out and leave the product pixels untouched. LAW, OPERATOR.
Rationale: a repainted product misleads about what ships (GN1); `references/design-enrichment.md` compositing recipes assume a real reference image.
Check: view the composite beside the source packshot with `lexsis_assets.view`; colour, shape and label identical (yes/no in `QA record`); Generation record cites the reference asset id.

GP3. Give decorative generated images `alt=""` and `aria-hidden="true"`; give composites a product alt that names the product. LAW.
Rationale: W3C alt decision tree https://www.w3.org/WAI/tutorials/images/decision-tree/ .

GP4. Never let people words appear in the alt text or prompt of a generated slot unless the ASK synthetic-model case was approved. LAW.
Rationale: 16 CFR 465; ASCI prohibited tier.

GP5. Never generate text into an image; every headline, price, label and badge is HTML. LAW.
Rationale: WCAG 1.4.5; Google and Shopify overlay rules (section 2).

GP6. Place `hero_bg` and `section_bg` only in the plan's bold moment; keep one page background everywhere else. OPERATOR.
Rationale: N2 and N7 in `references/design-rules.md`; a generated band per section is the template tell those rules exist to stop.
Check: count of full-width elements with a generated background image is 0 or 1 and its section id equals the plan's "Bold moment" line (browser check from N2).

GP7. Record provenance three ways: metadata on the original, `generated: true` plus `provider` in the page record, and the Generation record in the plan. LAW.
Rationale: Google requires `IPTC DigitalSourceType`; EU and ASCI labelling decisions must be auditable; hosts may strip file metadata.

GP8. Show a visible label wherever section 6 requires one and place it adjacent to the image. LAW.
Rationale: EU Art. 50 first-exposure labelling; ASCI medium tier.

GP9. Read credits and obtain a yes for the named batch before spending; cap generated assets at four per page. OPERATOR, HEURISTIC.
Rationale: `/design-page` authorises page creation, not generation; more than a few generated backdrops read as a template.

GP10. Use `high` quality only for `hero_bg`; `medium` for section and card backgrounds and composites; `low` for textures and decoration. OPERATOR.
Rationale: cost table in `references/design-enrichment.md`.
Check: Generation record "Style / quality" column obeys the mapping.

GP11. Never place a generated image in the gallery, the first gallery position, the feed image or a proof section. LAW.
Rationale: GN12; feed and gallery positions carry product identity; proof sections carry testimony.
Check: no manifest entry with `generated: true` has `sectionId` in `gallery`, `buy-box`, `product-hero`, `reviews`, `ugc-grid`, `testimonial-spotlight`, `before-after`, `press-marquee`, `certifications`, `awards`.

GP12. Log every ASK approval with the merchant's words and the date; never infer approval from plan approval. OPERATOR.
Rationale: an ASK image carries a label and legal exposure the merchant must own.
Check: Generation record "Approved by" for ASK rows quotes text and a date; `PLAN_APPROVED` alone is not accepted.

GP13. Never add props, gifts, accessories or a second product to a composite that could read as shipped with the product. LAW.
Rationale: included-items misrepresentation; ASCI "exaggerating product features".
Check: view; the composite contains the product and a surface or scene only (yes/no).

GP14. Never use a generated image to fill `in-use`, `scale`, `size-reference`, `swatch`, `texture` of the product, `ingredient-or-material` presented as own sourcing, or `result-or-context` results. LAW, RESEARCH.
Rationale: these jobs are how the shopper judges the real product (Baymard in-scale, human model, health and beauty research cited in `image-jobs-by-page-type.md`).
Check: every `generated` slot's Role/purpose job is `context`, a backdrop, a texture fill, a decoration or an icon set.

## Sources

- Google Merchant product data spec (IPTC) https://support.google.com/merchants/answer/7052112 ; promotional overlays https://support.google.com/merchants/answer/6101131
- Shopify Theme Store requirements https://shopify.dev/docs/storefronts/themes/store/requirements ; Shopify Magic media https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic/media-generation
- FTC consumer reviews and testimonials rule https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials ; Q&A https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers ; Federal Register https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-465-trade-regulation-rule-use-consumer-reviews-testimonials-final-rule ; health products guidance https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance
- ASCI draft AI labelling guidelines https://www.ascionline.in/wp-content/uploads/2026/05/asci-ai-labelling-guidelines.pdf ; coverage https://www.thehindubusinessline.com/info-tech/asci-proposes-risk-based-approach-for-responsible-labelling-on-ads-made-with-ai/article70969237.ece
- EU AI Act Art. 50 quick facts https://digital-strategy.ec.europa.eu/en/factpages/quick-facts-transparency-rules-ai-systems ; Orrick summary https://www.orrick.com/en/insights/2026/08/eu-ai-act-transparency-obligations-for-ai-generated-content-article-50
- ASA before/after https://www.asa.org.uk/advice-online/before-and-after-photos.html ; production techniques https://www.asa.org.uk/advice-online/cosmetics-the-use-of-production-techniques.html
- Meta AI labels https://www.facebook.com/business/help/1010479435004531 ; newsroom https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/
- W3C images tutorial https://www.w3.org/WAI/tutorials/images/ ; alt decision tree https://www.w3.org/WAI/tutorials/images/decision-tree/
- NN/g AI-generated images https://www.nngroup.com/articles/ai-generated-images/ ; Nosto trust ranking https://www.nosto.com/blog/new-research-brands-prefer-ugc-for-diversity/
- Secondary (verify before legal reliance): Craftshift on Shopify AI disclosure https://craftshift.com/disclose-ai-generated-product-images-shopify-2026/

---

# Offer types

The canonical offer catalogue. `page record` `offer.type` takes exactly
one id from this file; page-type checklists list the same ids under
`offer_compat`. Every offer renders only from a verified row in the plan's
`## Offer ledger` (`references/offers/offer-ledger.md`). Price display rules
live in `references/offers/price-presentation.md`, urgency rules in
`references/offers/urgency-scarcity.md`, stage rules in
`references/offers/funnel-stages.md`, dark patterns in
`references/anti-patterns/dark-patterns.md`.

Tags: LAW (statute or regulator text), RESEARCH (peer-reviewed or large
sample), OPERATOR (practitioner data, directional), HEURISTIC (rule of thumb).
Section ids come from `references/page-types/_checklist-format.md`.

## Catalogue

### `none`
- Use when: luxury or prestige positioning; launches at full price; retargeting where the objection is not price; any page whose ledger has no verified offer row.
- Anatomy delta: no `offer`, `savings-math`, `countdown`, `stock-indicator`, `final-offer`. `trust-bar` carries shipping, returns and guarantee facts only.
- Math: list price alone; unit price in `specs` where law requires it (PP8).
- LAW: general price rules only (`price-presentation.md`).
- Anti-patterns: inventing a "value" or "worth" line to fill the gap; a fake compare-at to make list price look reduced.
- Metric: conversion rate. CTA: "Add to cart" ("Add to bag" for fashion and beauty).

### `percent-off`
- Use when: unit price under about $100 or ₹8,000 (RESEARCH, Rule of 100); catalogue-wide sale; mass or mid-market positioning. OPERATOR: 20% was the redemption and AOV sweet spot in Seguno's unique-code benchmark; 10% had the worst redemption (0.20%).
- Anatomy delta: `announcement` with depth and end date; struck compare-at plus sale price on every price instance in `buy-box` and `pricing`; `savings-math` line with currency saved; `legal` offer footnote within one scroll of the first price.
- Math: compare-at, sale price, computed currency saving. EU: percent computed from the 30-day lowest prior price (PP2).
- LAW: compare-at basis required in every market (PP1 to PP5). FTC 16 CFR 233.1: a nominal reduction may not be called a sale.
- Anti-patterns: perpetual sale; stacking with the first-order code; percent alone on goods over the Rule-of-100 line; ALL-CAPS "% OFF" pills (design-rules N9); any percent on a luxury page (OF3).
- Metric: conversion rate and contribution margin per order. CTA: "Add to cart"; headline "[depth] off [scope], ends [date]".

### `fixed-off`
- Use when: unit price over about $100 or ₹8,000; win-back; when a minimum-spend threshold is wanted. OPERATOR: minimum spend on amount-off codes correlated with 2.6x AOV ($100.79 vs $39.30, Seguno).
- Anatomy delta: as `percent-off`, plus a threshold line beside the offer ("$30 off orders over $150") and a cart progress indicator toward the threshold (cart profile, `references/cart-composition.md`).
- Math: currency off beside the price; in cart, the remaining amount to unlock.
- LAW: same compare-at rules; threshold and exclusions adjacent to the offer, not in a footnote (FTC 251.1 proximity by analogy; India CCPA drip pricing).
- Anti-patterns: threshold more than 50% above AOV; amount-off on items under $30 (reads small); threshold that differs from the checkout rule.
- Metric: AOV lift against a holdout, redemption rate. CTA: "Add to cart"; headline "Save $[n] on [product] this week".

### `bogo`
- Use when: product cost is low relative to price (OPERATOR, CTC: at 13 to 18% COGS a BOGO is a better take rate than 25% off and a bigger perceived offer); moving a second SKU or slow stock; consumables.
- Anatomy delta: `offer` names both items with images; `buy-box` shows the free line at 0 with a strike; an explicit "add both to cart" instruction because native Shopify Buy X Get Y never auto-adds the get item.
- Math: present as quantity gained, not percent saved (RESEARCH, Chen et al. 2012: bonus pack beat the equivalent price cut); show effective per-unit price ("2 for $40, $20 each").
- LAW: FTC 16 CFR 251.1 treats "buy one get one" as a Free claim: the paid item at its regular price (lowest with substantial sales in the prior 30 days); no size runs a Free offer more than 6 months in any 12. Stock for the free item must exist.
- Anti-patterns: "BOGO 50%" with no per-unit price; a code required but not stated near the offer; a get item of lower quality; "BOGO" as a word for non-US audiences.
- Metric: units per order, contribution margin per order. CTA: "Add both to cart".

### `gwp`
- Use when: prestige positioning where a price cut damages equity; AOV lift via threshold; sampling a new SKU; giving categories (pets, kids, beauty). OPERATOR: three named, pictured gifts at a $60 threshold beat 15% off by +25% AOV in a five-arm popup test (Convertibles).
- Anatomy delta: `offer` shows the gift as a product image with its retail value; threshold line adjacent; cart progress to the gift; gift line auto-added at 0 by a Discount Function, never theme JavaScript (which drops at checkout).
- Math: gift retail value, never cost; threshold gap in cart.
- LAW: FTC 251.1: all conditions "at the outset, in close conjunction with the offer"; an asterisk to a footnote is not adequate; "gift", "bonus", "complimentary" carry the same rules. India CCPA: free samples are not basket sneaking, but the gift may not raise the total payable.
- Anti-patterns: "a free gift" with no name or picture; threshold below current AOV; dead-stock gift; banner still up after the gift sells out.
- Metric: AOV lift, gift redemption, second-purchase rate of gifted customers. CTA: "Add to cart" on the product; "Claim your free [gift]" only on the gift module.

### `free-shipping`
- Use when: unexpected shipping is the top addressable abandonment cause. RESEARCH, Baymard: 40% of non-browsing abandoners cite extra costs; 64% look for shipping cost on the product page and 43% of sites do not show it.
- Anatomy delta: `announcement` with the threshold; a `shipping-returns` line in `buy-box`; cart progress bar with remaining amount; optional gap-filler `cross-sell` priced to close the gap.
- Math: threshold 15 to 30% above AOV (HEURISTIC). OPERATOR, 72technologies 14-store test: 1.5x AOV was the best revenue-per-session point; the bar was negative on revenue per session in 3 of 14 stores; a static banner beat the animated bar in 2 of 3 arms. Margin floor: all-in shipping cost divided by gross margin percent.
- LAW: the page threshold and the checkout shipping rate are the same number. India: delivery charge sits inside the single-figure total (E-Commerce Rules 6(5)(b)).
- Anti-patterns: threshold hidden until checkout; bar that resets between pages; free shipping stacked with a sitewide percent code; threshold above mobile AOV.
- Metric: revenue per session and contribution margin per order, never AOV alone. CTA: none of its own; announcement copy "Free shipping on orders over $[n]" (India: "Free delivery above ₹[n]. Pay on delivery available").

### `tiered-volume`
- Use when: consumables and replenishables where shipping cost barely rises with units (OPERATOR, CTC).
- Anatomy delta: `quantity-breaks` in the purchase block with per-unit price per tier; cart shows the tier reached and the gap to the next.
- Math: per-unit price and total saving at each tier; the single unit is the reference price. OPERATOR: single, 2-pack, 3-pack beat single and 3-pack; removing the 2-pack dropped 3-pack sales 15 to 25% (AccelerOI).
- LAW: the single-unit price must be the real selling price (PP1). Needs an app or Discount Function on Shopify.
- Anti-patterns: more than four tiers (RESEARCH, Chernev 2003 on choice overload); a higher tier with a worse per-unit price; a multi-pack pre-selected; "MOST POPULAR" ribbon (N9).
- Metric: units per order, tier mix. CTA: "Add to cart" with the selected tier; headline "Buy 2, save 10%. Buy 3, save 20%." with per-unit price beneath.

### `bundle`
- Use when: AOV is below the paid-media break-even (OPERATOR, Statlas: median new-customer AOV $74; 35% of brands under $75 lose on the first order); the value is the set.
- Anatomy delta: `product-hero` or `bundle-builder` with component images and "what's inside"; `savings-math` mandatory ("$87 separately, $59 as a set, save $28"); `comparison` table when a good, better, best ladder exists.
- Math: sum of components, bundle price, currency saved; percent only under the Rule-of-100 line. Do not pad with a cheap item to inflate the "separately" figure (RESEARCH, Chernev: low-value components lower willingness to pay).
- LAW: compare-at for a bundle is the sum of component prices actually sold at those prices (UK CMA principles cover bundles).
- Anti-patterns: no "vs buying separately" line; build-your-own with more than six slots; components never sold individually; percent-only saving on a bundle over $100.
- Metric: AOV, bundle attach rate, first-order contribution margin. CTA: "Get the set" or "Add the bundle".

### `bundle-decoy`
- Use when: a three-option ladder where the target tier should win and the attributes can be compared in a visible table.
- Anatomy delta: `plan-selector` or `pricing` with three tiers plus `comparison` (the decoy effect needs visible attribute comparison); target tier in the middle or as the option that dominates the decoy.
- Math: RESEARCH, Simonson 1989 asymmetric dominance; the Economist replication moved bundle share 32% to 84%, but replications show 10 to 18 point shifts, so plan on that. Every tier shows price and per-unit or per-item value.
- LAW: the decoy must be a real purchasable option at the shown price; a tier nobody can buy is bait (UK DMCC bait advertising; FTC 16 CFR 238).
- Anti-patterns: decoy not clearly dominated; all three tiers look poor (repulsion effect); highlighted middle tier with "BEST VALUE" chrome (N9).
- Metric: target-tier share, revenue per visitor. CTA: "Choose [tier name]".

### `subscribe-save`
- Use when: replenishable category. OPERATOR, Recharge 2026: subscribers place about 3x more orders than one-time shoppers.
- Anatomy delta: `subscription-toggle` in `buy-box` with one-time and subscribe prices side by side; frequency selector; "skip, swap or cancel anytime" adjacent; renewal price and cadence stated before the buy button.
- Math: both prices and the saving per delivery; per-day framing allowed for consumables (RESEARCH, Gourville 1998: 52% vs 30% acceptance for the same annual cost framed daily).
- LAW: US ROSCA: material terms before billing details, express informed consent, simple cancellation (the 2024 FTC Negative Option Rule was vacated July 2025; ROSCA and state auto-renewal laws still apply). UK DMCC subscription rules phase in from 2026. India CCPA lists "subscription trap".
- Anti-patterns: subscribe pre-selected; intro discount so deep that churn follows expiry (OPERATOR, Recharge 2022); renewal price hidden; cancellation path missing from the page.
- Metric: subscription attach rate, 90-day retention, first-order margin after discount. CTA: "Subscribe and save [n]%" with renewal terms directly beneath.

### `first-order`
- Use when: cold or TOF acquisition where price is the stated objection. OPERATOR: popups with a discount convert 7.45% vs 4.60% without (Wisepops via Farabi Ulder); 10% and 20% first offers show near-identical repeat rate and LTV, so 10% is the margin-efficient default.
- Anatomy delta: `sticky-cta` bar or a timed `email-capture`; code shown in `buy-box` and pre-filled in cart; "first order" eligibility stated on the offer.
- Math: 10% under $50 AOV; free shipping or GWP over $80 AOV with over 55% margin (OPERATOR, Blossom).
- LAW: if email or SMS is collected, consent wording per market; never gate the code behind pre-ticked marketing consent (forced action, basket sneaking).
- Anti-patterns: code visible to returning customers (trains abandon-and-return); mobile popup that fails Google's interstitial guidance; deeper than the sitewide sale running at the same time.
- Metric: net revenue per new subscriber, not popup submit rate. CTA: "Add to cart"; offer line "10% off your first order" (never "Unlock").

### `referral`
- Use when: the visitor has already bought. OPERATOR, ReferralCandy: referred customers are 10.7x more likely to refer (3.27% vs 0.30%); 83% of advocates refer exactly once.
- Anatomy delta: `referral-form` on `thank-you-post-purchase` and `referral-loyalty-vip`; the referred friend's landing page states both rewards and who referred them.
- Math: both sides of the reward in currency ("Give $15, get $15"); expiry and minimum spend adjacent.
- LAW: the friend's reward is a discount or Free claim (FTC 251.1); incentivised reviews disclosed (UK DMCC banned practice 13; FTC Endorsement Guides).
- Anti-patterns: referral module on a cold page (nobody has bought); reward that is store credit with expiry but not labelled as such.
- Metric: referral order share, share-action rate. CTA: "Share your link".

### `loyalty`
- Use when: retention pages, account pages, early access. OPERATOR, CTC: give VIPs early access and exclusive drops, not a deeper discount.
- Anatomy delta: points-earned line in `buy-box` ("Earn 120 points"); tier badge; "members get early access" `announcement` shown only to logged-in visitors.
- Math: points value in currency where the programme defines it; expiry stated.
- LAW: expiry and redemption terms disclosed; India CCPA "interface interference" if points value is obscured.
- Anti-patterns: loyalty widget above the fold on TOF pages; points shown to visitors who cannot join.
- Metric: repeat rate, redemption rate. CTA: "Get early access", "Join [programme]".

### `cashback`
- Use when: India and marketplace-trained audiences; bank or UPI cashback is the dominant festive mechanic (Redseer festive 2025).
- Anatomy delta: `payment-options` strip near the price ("10% instant discount with [bank] cards, up to ₹1,500"); terms link adjacent.
- Math: cap, minimum order, and whether the cashback is instant or post-settlement.
- LAW: cashback conditions are material terms; "up to" must be achievable by a meaningful share of buyers (UK CAP "up to" standard; India CCPA misleading advertisement).
- Anti-patterns: store credit labelled cashback; bank list hidden; cap omitted.
- Metric: payment-method mix, prepaid share. CTA: none of its own; line "[n]% instant discount with [bank] cards, up to ₹[cap]. T&C."

### `bnpl`
- Use when: AOV $80 to $400 (₹3,000 and up) and considered purchases. OPERATOR: Shop Pay Installments 15 to 30% higher AOV on qualifying carts (Digital Heroes citing Shopify Editions); moving the callout from below add-to-cart to under the price lifted installment selection 9% for one brand (D2C Times).
- Anatomy delta: `bnpl-line` directly under the price in `buy-box`, not only at checkout; `payment-options` logos in `trust-bar`.
- Math: total price first, then the split, count and interest ("$99, or 4 payments of $24.75"); "0% APR" only if true; India "₹999/month x 6, no-cost EMI" with bank list and the note that interest is absorbed as a discount.
- LAW: US TILA / Reg Z triggering terms; UK FCA BNPL regulation from 2026; EU Consumer Credit Directive 2023; India RBI digital-lending guidelines. Full price always more prominent than the installment.
- Anti-patterns: installment larger than the total; BNPL as the only price; more than two providers; shown under the provider's eligibility floor.
- Metric: conversion on carts above the floor; repeat rate by payment cohort. CTA: none; the line sits under price.

### `trial-sample`
- Use when: high-consideration consumables (skincare, supplements) where the objection is "will it work for me".
- Anatomy delta: `product-hero` with the sample and the full-size price visible; shipping cost on the page; `post-purchase-next-steps` states what happens after the trial.
- Math: trial price, shipping, full-size price; if the trial converts to a subscription, renewal price and date.
- LAW: FTC 251.1: "Free" with a shipping charge needs the charge at the outset; conversion to paid needs ROSCA consent and cancellation; UK DMCC subscription rules; India "subscription trap".
- Anti-patterns: auto-enrol without a separate un-ticked consent; "free" in the headline with "$4.95 S&H" in the footer.
- Metric: trial-to-paid conversion. CTA: "Try it for $[n]" or "Get your sample".

### `mystery`
- Use when: clearance of mixed inventory to an engaged base; retention audiences.
- Anatomy delta: `offer` with "guaranteed value of at least $[n]"; category or size selector; "no returns on mystery items" stated before add-to-cart.
- Math: guaranteed value is a compare-at claim and needs a basis (PP1).
- LAW: returns exclusions disclosed pre-purchase (UK CRA 2015; India E-Commerce Rules 6(5)(g)); statutory withdrawal rights cannot be waived in the EU.
- Anti-patterns: on any TOF page; value guarantee built on inflated RRPs.
- Metric: sell-through, return rate. CTA: "Add the mystery box".

### `pre-order-price`
- Use when: a launch or restock where the visitor pays now (deposit or full) for a product that ships later.
- Anatomy delta: "Pre-order" state in `buy-box`; "Estimated to ship by [date]" beside the price and beside the button; deposit and full price shown separately; cancellation line in `shipping-returns`.
- Math: Shopify UX guidance: never strike the full price against a deposit. "Pre-order $89 (launch price $109)" is a future-price comparison and is fair only if the price actually rises afterwards (UK CTSI).
- LAW: FTC Mail Order Rule 16 CFR 435: reasonable basis for the ship date, 30 days if none stated, revised date plus cancel or refund right on delay. Shopify pre-order policy mirrors this.
- Anti-patterns: "ships soon" without a date; charging months ahead without saying so; countdown to a ship date the merchant cannot meet.
- Metric: pre-order conversion, cancellation rate. CTA: "Pre-order. Ships by [date]".

### `price-lock`
- Use when: a waitlist or subscription where the merchant promises to hold today's price for a stated period or cohort.
- Anatomy delta: `offer` line stating the locked price, duration and conditions; on `subscription` pages, "your price stays $[n] per delivery for 12 months" beside the toggle.
- Math: locked price, comparison price only if it is a real current or scheduled price.
- LAW: a price-lock is a contract term: state duration, what ends it, and what happens after. UK CTSI: an "after the promotion" price is fair only if it really rises.
- Anti-patterns: "prices going up soon" with no scheduled increase; lock that silently expires into a higher renewal.
- Metric: waitlist-to-order or subscription retention. CTA: "Lock in $[n]" or "Join the waitlist".

### `flash-sale`
- Use when: a genuinely short window (hours) and a list to notify. OPERATOR, Attentive: hours, not days; send SMS off the hour to avoid carrier congestion.
- Anatomy delta: `sticky-cta` or `announcement` with a server-side `countdown` to the real end; sale `product-grid`; price reverts automatically at zero. Requires the page-type checklist `urgency` to be `verified-only` or `encouraged`.
- Math: as `percent-off` or `fixed-off` on each card.
- LAW: UK DMCC Sch. 20, EU UCPD Annex I.7, India CCPA false urgency (`urgency-scarcity.md`). Never extend a "last chance" deadline.
- Anti-patterns: six-day "flash" sale; timer on any TOF page; timer without an `offer.endsAt`.
- Metric: revenue per send, cumulative revenue past the window (nets out pull-forward). CTA: "Add to cart"; headline "[depth] off [set] until [time] [tz]".

### `clearance`
- Use when: end of season or discontinued lines. OPERATOR, CTC: go deep on end-of-line stock late in season rather than a 70%-off site in March.
- Anatomy delta: separate "Last chance" `product-grid`; "Final sale, no returns" on card and `buy-box`; sizes remaining shown from live inventory via `stock-indicator`.
- Math: genuine compare-at per SKU; "up to X% off" only when a meaningful share of SKUs sit at the maximum (PP23).
- LAW: compare-at basis still required; "final sale" cannot remove statutory rights (UK CRA; EU 14-day withdrawal; India return-terms disclosure).
- Anti-patterns: clearance stock in the hero of an evergreen page; "up to 70%" where one SKU is 70%; any clearance on a luxury page.
- Metric: sell-through, margin recovered. CTA: "Add to cart"; card label "Final sale".

### `limited-edition`
- Use when: a real unit cap or collaboration. RESEARCH, Barton et al. 2022 meta-analysis (131 studies): scarcity effects roughly double for unfamiliar brands (0.41 vs 0.21) and are larger for high-involvement products.
- Anatomy delta: unit count in `product-hero` ("Edition of 500"); drop date and time; `waitlist-form` pre-drop; "sold out" state stays visible post-drop; no percent off, ever.
- Math: none beyond price; the counter binds to live inventory and stops at the cap.
- LAW: the cap must be true and not replenished under the same "limited" label (UK DMCC banned practice on availability; India CCPA false scarcity).
- Anti-patterns: "limited" with no number; restocking a "limited" SKU; discount on a drop.
- Metric: sell-out time, waitlist conversion. CTA: "Join the waitlist" pre-drop; "Add to cart" during; "Notify me" after.

### `gift-card`
- Use when: shipping cutoffs have passed; last-minute gifting; "they choose".
- Anatomy delta: denomination selector, schedule-send date, personal message field, no shipping line; becomes the hero of `seasonal-gifting` after the last cutoff.
- Math: face value only. Never show a gift card at a discount unless the merchant funds it.
- LAW: US CARD Act: no expiry under 5 years, fee limits; UK and EU: expiry and fees disclosed; India RBI PPI rules: minimum one-year validity.
- Anti-patterns: gift card as a hero before cutoffs have passed; "bonus" card value without terms.
- Metric: gift-card revenue share in the post-cutoff window. CTA: "Send a gift card".

### `student-military`
- Use when: a verification partner (SheerID, ID.me, UNiDAYS) is connected and the segment matters to the brand.
- Anatomy delta: verification-gated code in `offer` or `faq`; eligibility stated; hidden from segments known to be ineligible.
- Math: as `percent-off` or `fixed-off`, against the real selling price.
- LAW: never presented as a general sale; UK CMA: the reference price is still the real selling price.
- Anti-patterns: eligibility hidden until after the code fails; the gated code visible in the hero of a general page.
- Metric: verified redemptions. CTA: "Verify and save".

### `charity`
- Use when: a cause campaign with a named recipient; brand story pages. RESEARCH, Gneezy et al.: pay-what-you-want with half to charity reached 4.49% purchase at a $5.33 average and was profitable.
- Anatomy delta: "[n]% or $[n] of every order goes to [named charity]" adjacent to price; running total only if real; end date; any donation add-on un-ticked.
- Math: amount or percent per order, cap, period.
- LAW: name the charity, share, period and cap (UK CAP Code; FTC charitable-solicitation guidance; India CCPA "disguised advertisement"). India CCPA lists pre-ticked charity add-ons as basket sneaking.
- Anti-patterns: "a portion of proceeds"; cause badge on an unrelated product; discount stacked on a cause campaign.
- Metric: conversion versus the same page without the cause line, donation total. CTA: "Shop and give".

## Cross-cutting rules

OF1. One offer per page. `offer.type` holds one id; a second offer needs its own ledger block and a reason. Exempt page types: `sale-clearance-flash`, `seasonal-gifting` (offer-ledger rule 6).

OF2. Rule of 100. Always show the currency saving (offer-ledger rule 2). Under $100 or ₹8,000 the percent may lead ("32% off, save $28"); above it currency leads and percent is optional ("Save $128 (18%)"); never a percent without the currency amount on high-ticket goods. RESEARCH: Berger; JBR 2015 three-study replication. The ₹8,000 crossover is HEURISTIC.
Check: every `savings-math` line contains a currency figure; the leading figure matches the side of the line the ledger price falls on.

OF3. Luxury never shows percent, a struck price, a timer, "sale" or "clearance". Allowed ids: `none`, `gwp`, `free-shipping` (phrased "complimentary shipping", no threshold), `limited-edition`, `pre-order-price`, `price-lock`, `loyalty`, `gift-card`. RESEARCH and OPERATOR: Kapferer and Bastien anti-laws; Langer on price volatility and equity decay.

OF4. Bundle, tiered and BOGO pages show their arithmetic. `bundle`, `bundle-decoy`, `tiered-volume`, `bogo` require a `savings-math` or `quantity-breaks` section whose figures are ledger rows.

OF5. "Free", "gift", "bonus" and "complimentary" appear only when the buyer pays nothing extra and the conditions sit in the same section (LAW, FTC 16 CFR 251.1; UK banned practice; EU UCPD Annex I.20).
Check: every section containing `\bfree\b` also contains the threshold, shipping cost or eligibility text; no `*` after "free".

OF6. No pre-ticked add-on, subscription, gift wrap, insurance, donation or upsell (LAW, India CCPA basket sneaking; ROSCA; EU CRD Art 22). Detail in `references/anti-patterns/dark-patterns.md`.

OF7. The offer moves down the page as awareness falls. On `tof` page types the offer section index is greater than the `mechanism`, `how-it-works` or `solution` index; on `bof` types the offer is in the hero (`funnel-stages.md` FS4).
Check: compare section order in `page record` against `page.funnelStage`.

OF8. Retargeting never shows a deeper discount than the visitor already saw, and never the first-order code (OPERATOR: trains abandonment).
Check: `page.pageType` is `retargeting-warm` implies `offer.type` is not `first-order` and the ledger notes the prior offer depth.

OF9. Free-offer frequency. A size or SKU carries a Free or BOGO offer no more than 6 months in any 12, with 30 days between offers and at most three per year (LAW, FTC 251.1(h)).
Check: ledger row for `bogo` or `gwp` records the months this year the offer has run on that SKU.

OF10. Compare-at is struck-through text only; no pills, ribbons or caps (design-rules N9).
Check: the hosted offer presentation passes N9.

OF11. Promise only what the discount configuration can do. Native BXGY does not auto-add the get item; a GWP auto-add needs a Discount Function; tiered pricing needs an app or Function; shipping discounts never combine with each other; at most 25 active automatic discounts (Shopify Help).
Check: ledger row O9 names the mechanic (code, automatic, Function, app) and the page instruction matches it.

OF12. Terms travel with the offer: exclusions, stacking, regions, code, minimum spend and cancellation terms within one scroll of the first offer mention (offer-ledger rule 4).
Check: the `legal` or `disclaimer` text for the offer is in the same or the next section as the first `offer`, `pricing` or `buy-box`.

OF13. Unknown market means the strictest rule: EU 30-day prior price, UK duration and volume, India MRP display and single-figure total.
Check: `page record` has a market list, or the ledger notes "strictest applied".

OF14. Never render an offer the merchant has not confirmed on the offer-ledger "Claims to confirm" list. Missing timing, compare-at basis or stock answers mean the price renders alone: no strike, no urgency, no scarcity.
Check: every offer-ledger row that the page uses has status `verified`.

## Offer by page type compatibility

Rows are the 30 page type ids from `references/page-types/_index.md`;
columns are the 25 offer ids in catalogue order. Cells: `yes` fits; `ask` fits
only under the condition named in the offer's entry above (merchant confirms
it, ledger records it); `no` never. A page-type file's `offer_compat` may
narrow this table but not widen it.

| Page type | none | percent-off | fixed-off | bogo | gwp | free-shipping | tiered-volume | bundle | bundle-decoy | subscribe-save | first-order | referral | loyalty | cashback | bnpl | trial-sample | mystery | pre-order-price | price-lock | flash-sale | clearance | limited-edition | gift-card | student-military | charity |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ad-landing-page | yes | ask | ask | ask | ask | yes | no | ask | ask | ask | yes | no | no | no | ask | yes | no | no | no | no | no | ask | no | no | ask |
| pdp | yes | ask | ask | ask | yes | yes | ask | yes | ask | yes | ask | ask | ask | ask | ask | ask | no | ask | ask | no | no | ask | ask | ask | ask |
| pdp-hybrid-landing | yes | ask | ask | ask | yes | yes | ask | yes | ask | yes | yes | no | no | ask | ask | ask | no | ask | no | no | no | ask | no | no | ask |
| advertorial | yes | ask | ask | no | ask | ask | no | ask | no | no | ask | no | no | no | no | yes | no | no | no | no | no | no | no | no | ask |
| listicle | yes | ask | ask | ask | ask | ask | no | yes | no | no | ask | no | no | no | ask | yes | no | no | no | no | no | no | no | no | no |
| seo-buyers-guide | yes | ask | ask | no | ask | yes | no | yes | no | no | ask | no | no | no | ask | ask | no | no | no | no | no | no | no | no | no |
| comparison-us-vs-them | yes | ask | ask | no | ask | yes | no | ask | no | ask | ask | no | no | no | ask | ask | no | no | no | no | no | no | no | no | no |
| quiz-funnel | yes | no | no | no | no | no | no | yes | ask | ask | ask | no | no | no | no | yes | no | no | no | no | no | no | no | no | no |
| bundle-kit | yes | no | yes | yes | yes | yes | yes | yes | yes | yes | ask | no | ask | ask | yes | no | no | no | no | no | no | ask | no | no | no |
| offer-page | yes | yes | yes | yes | yes | yes | yes | yes | ask | ask | yes | no | ask | yes | yes | ask | ask | ask | ask | ask | ask | ask | ask | ask | ask |
| sale-clearance-flash | yes | yes | yes | yes | yes | yes | ask | yes | no | no | no | no | yes | yes | yes | no | yes | no | no | yes | yes | no | no | ask | no |
| seasonal-gifting | yes | ask | yes | ask | yes | yes | no | yes | no | no | ask | no | ask | ask | yes | no | ask | no | no | ask | ask | yes | yes | no | ask |
| gift-guide | yes | ask | ask | no | yes | yes | no | yes | no | no | ask | no | no | ask | ask | no | no | no | no | no | no | yes | yes | no | ask |
| launch-waitlist-preorder | yes | no | no | no | yes | yes | no | yes | no | no | no | ask | yes | ask | ask | no | no | yes | yes | no | no | yes | no | no | ask |
| restock | yes | no | no | no | ask | yes | ask | ask | no | yes | no | no | ask | ask | ask | no | no | no | ask | no | no | ask | no | no | no |
| subscription | yes | no | no | no | yes | yes | ask | yes | yes | yes | yes | ask | yes | no | no | yes | no | no | yes | no | no | no | no | no | no |
| ugc-creator-collab | yes | ask | ask | no | yes | yes | no | yes | no | no | yes | no | no | no | ask | yes | no | ask | no | no | no | yes | no | no | no |
| video-sales-page | yes | ask | ask | no | ask | ask | no | yes | no | no | ask | no | no | no | ask | yes | no | no | no | no | no | ask | no | no | no |
| brand-story-founder | yes | no | no | no | no | ask | no | no | no | no | ask | ask | ask | no | no | no | no | no | no | no | no | ask | no | no | yes |
| ingredient-science | yes | no | no | no | no | yes | no | ask | no | ask | ask | no | no | no | no | ask | no | no | no | no | no | no | no | no | no |
| collection-landing | yes | ask | ask | ask | yes | yes | no | yes | no | no | ask | no | ask | ask | ask | no | no | no | no | ask | ask | ask | no | no | ask |
| homepage | yes | ask | ask | ask | yes | yes | no | yes | no | no | ask | ask | yes | ask | no | ask | no | ask | no | ask | ask | ask | ask | ask | ask |
| lookbook-shop-the-look | yes | no | no | no | ask | yes | no | yes | no | no | ask | no | no | no | ask | no | no | no | no | no | no | ask | no | no | no |
| lead-capture-giveaway | yes | no | no | no | ask | ask | no | no | no | no | yes | ask | no | no | no | ask | no | no | no | no | no | ask | no | no | ask |
| referral-loyalty-vip | yes | no | no | no | no | yes | no | no | no | no | no | yes | yes | no | no | no | ask | no | no | no | no | yes | ask | ask | no |
| retargeting-warm | yes | yes | yes | yes | yes | yes | yes | yes | ask | yes | no | no | yes | yes | yes | yes | ask | no | ask | ask | ask | yes | no | ask | no |
| thank-you-post-purchase | yes | no | no | no | no | no | no | no | no | ask | no | yes | yes | no | no | no | no | no | no | no | no | no | no | no | ask |
| faq-support-led | yes | no | no | no | no | yes | no | no | no | no | no | no | ask | no | ask | no | no | no | no | no | no | no | ask | ask | no |
| trial-sample | yes | no | no | no | no | yes | no | no | no | ask | no | no | no | no | no | yes | no | no | no | no | no | no | no | no | no |
| wholesale-b2b | yes | no | no | no | no | ask | yes | ask | ask | no | no | no | no | no | no | ask | no | no | ask | no | no | no | no | no | no |

Reading notes: `ask` on TOF types (`ad-landing-page`, `advertorial`,
`listicle`, `video-sales-page`) always means below the fold and after the
mechanism (OF7). `ask` for `percent-off` and `fixed-off` on `pdp`,
`seo-buyers-guide` and `collection-landing` means a verified compare-at basis
exists for every discounted entry. `ask` on `retargeting-warm` for `mystery`
and `clearance` means existing customers only. `charity` on
`thank-you-post-purchase` means a round-up that is never pre-ticked.
`wholesale-b2b` `tiered-volume` means MOQ price breaks, not a consumer promo.

## Sources

- Shopify discount types and combinations: https://help.shopify.com/en/manual/discounts/discount-types and https://help.shopify.com/en/manual/discounts/combining-discounts/discount-combinations
- Berger, Rule of 100: https://jonahberger.com/fuzzy-math-what-makes-something-seem-like-a-good-deal/ ; JBR 2015 replication: https://www.sciencedirect.com/science/article/abs/pii/S0148296315003513
- Seguno unique-code benchmarks: https://www.seguno.com/unique-discount-code-benchmarks
- Common Thread Collective BFCM offer database: https://commonthreadco.com/blogs/ecommerce-playbook/dig-in-bfcm-offer-database-2023 and https://commonthreadco.com/blogs/ecommerce-playbook/how-to-craft-the-best-bfcm-offer-this-year
- Chen, Marmorstein, Tsiros and Rao 2012 (bonus packs): https://doi.org/10.1509/jm.10.0443
- FTC 16 CFR 251.1 (Free): https://www.law.cornell.edu/cfr/text/16/251.1 ; 16 CFR 233.1 (deceptive pricing): https://www.law.cornell.edu/cfr/text/16/233.1 ; Mail Order Rule: https://www.ftc.gov/business-guidance/resources/business-guide-ftcs-mail-internet-or-telephone-order-merchandise-rule
- Convertibles GWP vs discount popup test: https://convertibles.dev/blogs/case-studies/free-gifts-vs-discounts-popup-offers-case-study
- Baymard cart abandonment and shipping-cost research: https://baymard.com/lists/cart-abandonment-rate and https://baymard.com/blog/show-shipping-costs-on-product-pages
- 72technologies free-shipping bar test: https://www.72technologies.com/blog/free-shipping-threshold-bar-ab-test-results
- AccelerOI pricing psychology (quantity breaks): https://www.acceleroi.com/blog/psychology-of-pricing
- Chernev 2003 (choice overload): https://ideas.repec.org/a/oup/jconrs/v30y2003i2p170-83.html
- Statlas AOV data (Taylor Holiday): https://www.linkedin.com/posts/taylor-holiday-a169b322_we-track-store-and-analyze-conversations-activity-7471272309199265792-Xc7H
- CXL pricing experiments (decoy, anchoring, PWYW): https://cxl.com/blog/pricing-experiments-you-might-not-know-but-can-learn-from/
- UK CMA reference-pricing principles: https://assets.publishing.service.gov.uk/media/66ab4347a3c2a28abb50db3c/Discount_and_reference_pricing_principles.pdf ; CTSI pricing guidance: https://www.businesscompanion.info/en/guidance-for-traders-on-pricing-practices
- Recharge subscription trend report 2026: https://getrecharge.com/reports/subscription-trend-report-2026/ ; Gourville 1998: https://doi.org/10.1086/209517
- FTC negative option and ROSCA: https://www.ftc.gov/business-guidance/blog/2024/10/click-cancel-ftcs-amended-negative-option-rule-what-it-means-your-business
- Welcome offer benchmarks: https://farabiulder.com/blog/welcome-offer-benchmarks and https://www.blossomecom.com/blogs/welcome-offer-optimization-ecommerce
- ReferralCandy referred-customer study: https://www.referralcandy.com/blog/referred-customers-study/
- Redseer festive 2025: https://redseer.com/articles/festive-2025-day-0-ecommerce-sales-surge-25-with-gst-boost-demand-led-by-smartphones-and-tvs/
- BNPL placement and AOV: https://digitalheroesco.com/journal/shopify-afterpay-klarna-shop-pay-integration/ and https://d2c-times.com/shopifys-shop-pay-installments-surge-is-rewriting-dtc-checkout-economics/
- Shopify pre-order UX guidelines: https://shopify.dev/docs/storefronts/themes/pricing-payments/preorder-tbyb/preorder-tbyb-ux-guidelines
- Attentive BFCM campaign guidance: https://www.attentive.com/black-friday-cyber-monday-2026/articles/bfcm-campaigns-that-convert
- Barton, Zlatevska and Oppewal 2022 scarcity meta-analysis (via Clean Commit): https://cleancommit.io/blog/do-countdown-timers-work/
- India CCPA Dark Patterns Guidelines 2023: https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf ; E-Commerce Rules 2020: https://ibclaw.in/consumer-protection-e-commerce-rules-2020/
- Luxury pricing: https://aws2.campaignasia.com/article/why-pricing-is-the-easy-growth-trap-in-luxury/482956 and https://www.vogue.com/article/should-luxury-brands-reduce-their-prices

---

# Dark patterns

Catalogue of deceptive interface practices a generated page must never
contain. Each entry gives the regulator's definition, an ecommerce example,
the page-builder rule, a severity and a check. `/plan-page` applies these when
it writes the Offer ledger; `/design-page` applies them in Compose step 6;
the source/hosted review runs the O1 to O4 checks. Offer-specific detail lives in
`references/offers/offer-ledger.md`, `references/offers/price-presentation.md`
and `references/offers/urgency-scarcity.md`; proof detail in
`references/proof/proof-ledger.md`. This file is the canonical list; the two
offer files and `references/consumer-behavior-cro.md` (Guardrails) point here.

Severity: BLOCK (legal exposure; the page does not ship), FAIL (fix before
publish), WARN (fix unless the plan records a reason). Tag: LAW (a regulator
names it), RESEARCH (usability evidence), OPERATOR (practitioner consensus),
HEURISTIC (this project's judgement).

Inspect the persisted source and hosted purchase flow.

## 1. Regulatory frame

| Regime | Scope | Status | Text |
|---|---|---|---|
| India CCPA, Guidelines for Prevention and Regulation of Dark Patterns, 2023 | 13 named patterns in Annexure 1; applies to all platforms, advertisers and sellers offering goods or services in India; list extensible | In force since 30 Nov 2023; self-audit advisory 5 Jun 2025 with notices issued | https://consumeraffairs.nic.in/theconsumerprotection/guidelines-prevention-and-regulation-dark-patterns-2023 ; https://consumeraffairs.nic.in/latestnews/ccpa-advisory-terms-consumer-protection-act-2019-self-audit-e-commerce-platforms |
| US FTC, Bringing Dark Patterns to Light (Sep 2022) | Four buckets: induce false beliefs; hide or delay material information; unauthorised charges (ROSCA); obscure privacy choices | Staff report; enforced under FTC Act s.5 and ROSCA | https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf |
| US FTC, Rule on the Use of Consumer Reviews and Testimonials, 16 CFR 465 | Fake or AI-generated reviews, bought reviews, insider reviews, suppression of negative reviews | Final rule 14 Aug 2024; civil penalties | https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials |
| US FTC, Endorsement Guides, 16 CFR 255 (2023) | Disclosure of material connections; typicality of results claims | Guides; enforced under s.5 | https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising |
| US ROSCA (15 USC 8401) | Disclose material terms before billing information; express informed consent; simple cancellation | In force. The 2024 amended Negative Option Rule was vacated by the Eighth Circuit on 8 Jul 2025; ROSCA and state auto-renewal laws still apply | https://ecf.ca8.uscourts.gov/opndir/25/07/243137P.pdf |
| EU DSA Art. 25 | Platforms may not design interfaces that deceive, manipulate or materially distort decisions; names prominence bias, repeated prompts, harder-to-cancel | In force since 17 Feb 2024 (platforms; single-brand stores fall under UCPD) | https://www.digitalacts.eu/regulation/digital-service-act/article/25/online-interface-design-and-organisation |
| EU UCPD Annex I | Blacklist incl. false limited-availability statements (item 7), advertorial without disclosure (item 11), "free" that costs (item 20) | In force for all B2C traders | https://www.europarl.europa.eu/RegData/etudes/ATAG/2025/767191/EPRS_ATA(2025)767191_EN.pdf |
| CJEU Planet49, C-673/17 | Pre-ticked boxes are not consent | Judgment 1 Oct 2019 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A62017CJ0673 |
| UK CMA, Online Choice Architecture (Apr 2022) + DMCC Act 2024 | 21 practices; drip pricing, reference pricing, sludge, forced outcomes starred as almost always harmful; CMA direct fines up to 10 percent of global turnover from 6 Apr 2025 | Guidance + statute | https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1066524/Online_choice_architecture_discussion_paper.pdf ; https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices |
| deceptive.design (Brignull) | Reference taxonomy: sneaking, hidden costs, hidden subscription, trick wording, confirmshaming, fake scarcity, fake urgency, fake social proof, forced action, hard to cancel, preselection, obstruction, nagging, disguised ads, visual interference, comparison prevention | Taxonomy, not law | https://deceptive.design/types/ |
| EU Digital Fairness Act (proposal) | Expected to codify dark patterns and switch addictive design (infinite scroll, autoplay) off by default | Proposal expected end 2026 | https://www.dentons.com/en/insights/articles/2026/june/9/the-digital-fairness-act-dark-patterns-addictive-designs-and-influencer-marketing |

Prevalence (CMA evidence review): 75 percent of the top 200 US ecommerce sites carried at least one impulse-buying choice-architecture practice; the ICPEN/OECD 2021 sweep of 1,300 sites found over a fifth with harmful practices, led by pre-ticked defaults, scarcity claims and drip pricing. https://www.gov.uk/government/publications/online-choice-architecture-how-digital-design-can-harm-competition-and-consumers/evidence-review-of-online-choice-architecture-and-consumer-and-competition-harm

## 2. Catalogue

### DP1. False urgency (timers)  BLOCK  LAW
- Definition. CCPA Annexure 1, item 1: "falsely stating or implying the sense of urgency or scarcity so as to mislead a user into making an immediate purchase". FTC bucket I: countdown timers on offers that are not time-limited. UCPD Annex I item 7. CMA: countdown clocks that reset.
- Example. A "Sale ends in 14:59" timer that restarts on every page load; "limited time" sales where the same deal continues after the deadline (Emma Sleep undertakings, 22 May 2026: https://www.gov.uk/cma-cases/emma-group-consumer-protection-case ).
- Rule. A countdown binds to the Offer ledger's confirmed `endsAt` (ISO datetime with timezone), disappears after it, and the deal actually ends. No per-session, per-visitor or resetting timers. No "ends soon" in static copy.

### DP2. Fake scarcity (stock)  BLOCK  LAW
- Definition. CCPA item 1(ii): "stating that quantities of a particular product or service are more limited than they actually are". FTC: "almost sold out" with ample supply. UK banned practice: pretending a product is available only for a very limited time.
- Example. "Only 3 left!" hardcoded in copy on a made-to-order item; "Low stock" badge on every variant.
- Rule. Stock statements come only from a live inventory binding (`lexsis_catalog.get` at render) and read the real count. "Limited edition" states the run size from the ledger. No stock words in static copy.

### DP3. Fake popularity (viewer and purchase counts)  BLOCK  LAW
- Definition. CCPA item 1(i): "showing false popularity of a product or service". FTC bucket I: false "others are viewing" and "recently purchased" notices. deceptive.design: fake social proof.
- Example. "23 people are viewing this" from a random-number script; "Priya from Mumbai just bought" popups with no order behind them.
- Rule. No viewer counts, activity feeds or "recently bought" toasts of any kind, even if fed by analytics; the proof vocabulary lists `social-proof-popup` and `live-viewer-count` as never rendered. Aggregate counts ("over 51,000 customers") only as verified proof-ledger rows.

### DP4. Basket sneaking  BLOCK  LAW
- Definition. CCPA item 2: "inclusion of additional items such as products, services, payments to charity or donation at the time of checkout from a platform, without the consent of the user, such that the total amount payable by the user is more than the amount payable for the product(s) and/or service(s) chosen by the user". Free samples and disclosed necessary fees are exempt.
- Example. Sports Direct added a GBP 1 magazine to every basket (https://deceptive.design/types/sneaking ); shipping protection auto-added in the cart drawer.
- Rule. Nothing enters the cart that the shopper did not tap. Cart-drawer add-ons are opt-in buttons, not pre-added lines. A bundle is one product the shopper chose, not silently combined items.

### DP5. Preselection (pre-ticked paid add-ons and consent)  BLOCK  LAW
- Definition. deceptive.design "preselection"; CJEU Planet49: pre-ticked boxes are not consent; GDPR Recital 32; EU Consumer Rights Directive Art. 22: no default options that require payment; CCPA basket sneaking covers paid defaults.
- Example. Gift wrap, insurance, donation, warranty, or "Subscribe and save" ticked by default; marketing checkbox pre-checked under the email field.
- Rule. No `checked` on any checkbox or radio whose label carries a price, a cadence, or a consent verb. Purchase type defaults to one-time. Marketing and SMS consent boxes start unchecked and are never `required`.
- Check.

### DP6. Confirmshaming  BLOCK  LAW
- Definition. CCPA item 3: "using a phrase, video, audio or any other means to create a sense of fear or shame or ridicule or guilt in the mind of the user so as to nudge the user to act in a certain way". Amazon's "No, I don't want Free Shipping" decline button is now banned by court order (https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-secures-historic-25-billion-settlement-against-amazon ).
- Example. "No thanks, I like paying full price"; "I don't care about my skin".
- Rule. Decline and close labels are neutral: "No thanks", "Close", "Not now", "Continue without". No first-person self-deprecation, no consequence framing, no sarcasm.

### DP7. Forced action  BLOCK  LAW
- Definition. CCPA item 4: "forcing a user into taking an action that would require the user to buy any additional good(s) or subscribe or sign up for an unrelated service or share personal information, in order to buy or subscribe to the product or service originally intended by the user". Baymard: 18 to 19 percent of US shoppers abandoned a checkout because the site wanted an account. https://baymard.com/lists/cart-abandonment-rate
- Example. Email gate before the price is shown; "Create an account to continue"; forced app download.
- Rule. Guest checkout is the primary path. No gate on price, shipping, reviews or the CTA. Email and phone are asked once, optional unless needed for delivery, and marketing consent is separate.

### DP8. Subscription trap, hard to cancel, roach motel  BLOCK  LAW
- Definition. CCPA item 5: making cancellation "impossible or a complex and lengthy process", hiding the cancel option, forcing payment details for a free trial, or giving "ambiguous instructions for cancellation". ROSCA: simple cancellation mechanism. DSA Art. 25(3)(c): termination may not be harder than subscribing. FTC v. Amazon, Vonage (USD 100M, 2022: https://www.ftc.gov/news-events/news/press-releases/2022/11/ftc-action-against-vonage-results-100-million-customers-trapped-illegal-dark-patterns-junk-fees-when-trying-cancel-service ) and Adobe (2024: https://www.ftc.gov/news-events/news/press-releases/2024/06/ftc-takes-action-against-adobe-executives-hiding-fees-preventing-consumers-easily-cancelling ).
- Example. "Cancel anytime" in the hero, "call us Monday to Friday" in the terms.
- Rule. The cancellation path is one sentence beside the subscribe control ("Pause or cancel from your account, no call needed") and it is true for this store's subscription app. Free trials state the conversion date and price in the CTA block.

### DP9. Hidden recurring terms (SaaS billing, hidden subscription)  BLOCK  LAW
- Definition. CCPA item 12 "SaaS billing": generating and collecting recurring payments "by exploiting positive acquisition loops in recurring subscriptions ... as surreptitiously as possible", including silent trial conversion. ROSCA s.4: all material terms clearly and conspicuously before obtaining billing information. deceptive.design "hidden subscription".
- Example. "$19" in the buy box, "/month" in 10 px grey; first-charge date only in the confirmation email.
- Rule. Recurring amount, cadence, first-charge date, renewal price after any intro period and the cancel path sit in the same visual block as the price, at body size and contrast. A subscribe option never wins by default (DP5).
- Check.

### DP10. Interface interference, visual interference, false hierarchy  BLOCK  LAW
- Definition. CCPA item 6: "a design element that manipulates the user interface in ways that (a) highlights certain specific information; and (b) obscures other relevant information relative to the other information". DSA Art. 25(3)(a): giving more prominence to certain choices. FTC bucket II: un-bolded fees "sandwiched between bold paragraphs".
- Example. Bright "Yes, upgrade" button with a grey 12 px "no" text link; a close icon at 2:1 contrast; compare-at price larger than the price paid.
- Rule. In any binary choice (consent, upsell, subscription vs one-time), both options are the same element type, within 1.5x of each other's area, both at 4.5:1. Close controls meet A11's 48 x 48 CSS px floor, have 3:1 contrast and close on first tap. The price paid is never smaller than the compare-at.
- Check (browser).
```js
(() => { const d = document.querySelector('[role=dialog]'); if (!d) return 'no dialog';
  const a = d.querySelector('[data-action=accept]'), r = d.querySelector('[data-action=decline]');
  if (!a || !r) return 'FAIL missing accept/decline';
  const A = a.getBoundingClientRect(), R = r.getBoundingClientRect();
  return ((A.width*A.height)/(R.width*R.height) <= 1.5 && a.tagName === r.tagName) ? 'ok' : 'FAIL parity'; })()
```

### DP11. Bait and switch  BLOCK  LAW
- Definition. CCPA item 7: "advertising a particular outcome based on the user's action but deceptively serving an alternate outcome". UK banned practices 5 and 6 (bait advertising; bait and switch). FTC 16 CFR 238.
- Example. Ad shows the GBP 29 colourway; the page lands on a GBP 39 variant with the cheap one "unavailable"; sold-out size silently replaced.
- Rule. The SKU, variant, colour, flavour, size and price in the ad and the hero are what lands in the cart. Sold-out variants are disabled and labelled "Notify me", never swapped. See `references/copy/message-match.md` MM3.
- Check. Manifest `campaign.adVariantId`, hero `data-variant-id` and buy-box default variant are identical; the cart preload URL carries the same variant id.

### DP12. Drip pricing and hidden costs  BLOCK  LAW
- Definition. CCPA item 8: "elements of prices are not revealed upfront or are revealed surreptitiously", including revealing price "post-confirmation" and "free" that requires a paid continuation. UK DMCC: the full price belongs in the invitation to purchase. FTC fees rule (16 CFR 464 for tickets and lodging; s.5 elsewhere). CMA evidence 4/4 stars. Baymard: extra costs are the top abandonment reason at 39 to 40 percent; 64 percent of shoppers look for shipping cost on the product page. https://baymard.com/lists/cart-abandonment-rate ; https://baymard.com/blog/show-shipping-costs-on-product-pages
- Example. "$49" hero, "$8.95 handling" at payment; "Free" trial with shipping charged; tax added after the address step with no earlier signal.
- Rule. The price on the page is the price at checkout. Shipping cost or the free-shipping threshold, tax wording ("inclusive of all taxes" or "plus tax") and any mandatory fee appear within one viewport of the primary CTA. See `references/offers/price-presentation.md` PP1 and PP21.
- Check. For every `buy-box`, `pricing` or `offer` section: section text matches `shipping|delivery` and `tax|GST|inclusive`. Every `<s>`, `<del>` or compare-at element traces to an offer-ledger row with a `compare_at_basis`.

### DP13. Disguised advertisement  BLOCK  LAW
- Definition. CCPA item 9: "posing, masking advertisements as other types of content such as user generated content or new articles or false advertisements". UK banned practice 11 (advertorial without disclosure). FTC native advertising guidance; Endorsement Guides: disclosures "difficult to miss" and "unavoidable".
- Example. Fake newspaper masthead; "By our health desk" byline on a sales page; comment thread with invented commenters.
- Rule. `advertorial` and `listicle` pages carry a visible "Advertisement" or "Sponsored by [brand]" label inside the first 600 px at 390, plus the compliance line in the footer. No fake mastheads, bylines of people who do not exist, or invented comments. Paid creators say "Paid partnership".
- Check (browser, 390).
```js
(() => { if (!/advertorial|listicle/.test(document.body.dataset.pageType||'')) return 'n/a';
  return [...document.querySelectorAll('body *')].some(e => e.children.length===0 && /advertis(ement|ing)|sponsored|paid partnership/i.test(e.textContent) && e.getBoundingClientRect().top < 600) ? 'ok' : 'FAIL label'; })()
```

### DP14. Nagging  BLOCK  LAW
- Definition. CCPA item 10: "disrupted and annoyed by repeated and persistent interactions, in the form of requests, information, options, or interruptions ... unless specifically permitted by the user". DSA Art. 25(3)(b): repeatedly requesting a choice already made, especially by pop-ups. NN/g "overlay overload". https://www.nngroup.com/articles/overlay-overload/
- Example. Email popup on every page view after dismissal; notification prompt with no "No".
- Rule. One marketing popup per session, remembered for at least 7 days after dismissal and 30 days after conversion. Never two overlays at once. Consent UI first; marketing waits until it is gone.
- Check. Popup island props: `frequencyCapDays >= 7`. Browser: `[...document.querySelectorAll('[role=dialog],[data-overlay]')].filter(e => e.offsetParent !== null).length <= 1` at every scroll position.

### DP15. Trick wording, trick question  BLOCK  LAW
- Definition. CCPA item 11: "deliberate use of confusing or vague language like confusing wording, double negatives, or other similar tricks, in order to misguide or misdirect a user". CMA: complex language starred as almost always harmful.
- Example. "Uncheck to not receive no updates"; a toggle labelled "Opt out" whose on state means subscribed.
- Rule. Choice labels are affirmative, single-clause, no negation: "Email me offers" / "No thanks". Toggle labels describe the on state. No double negatives anywhere in choice UI.

### DP16. Rogue malware and fake system UI  BLOCK  LAW
- Definition. CCPA item 13: scareware and ransomware tactics.
- Rule. No fake virus warnings, fake OS dialogs, fake download buttons, fake "connection lost" banners.

### DP17. Fake reviews and undisclosed incentives  BLOCK  LAW
- Definition. FTC 16 CFR 465 bans fake, AI-generated or bought reviews, insider reviews without disclosure, and suppression of negative reviews (Fashion Nova, USD 4.2M, 2022: https://www.ftc.gov/news-events/news/press-releases/2022/01/fashion-nova-will-pay-42-million-part-settlement-ftc-allegations-it-blocked-negative-reviews-website ). UK DMCC banned practice on fake reviews. Endorsement Guides: incentivised reviews disclosed; results claims need typicality.
- Rule. Every quote, star, count and photo of a customer is a `verified` row in the proof ledger (`references/proof/proof-ledger.md`); sourcing in `references/proof/reviews-sourcing.md`. No invented names, avatars or cities. Never only five-star sets. "Results not typical" alone is not a disclosure.

### DP18. Misdirection  BLOCK  LAW
- Definition. deceptive.design: design that steers attention to the seller's preferred option and away from the shopper's. CMA "sensory manipulation" and "decoys". Overlaps DP10 but concerns steering rather than hiding.
- Example. A highlighted "MOST POPULAR" middle tier that exists only to make the top tier look cheap; a colour-only difference between "one-time" and "subscribe" that favours subscribe.
- Rule. Plan tiers are presented with the same visual weight; a recommended tier is labelled with a reason from the ledger ("Most ordered in the last 90 days" with the count), never a ribbon (design-rules N9). One-time and subscribe options are visually equal with one-time first.

### DP19. Obstruction and sludge  FAIL  LAW
- Definition. deceptive.design "obstruction"; CMA "sludge": excessive friction on the action the shopper wants (returns, cancellation, contact).
- Rule. Returns, refund, cancellation and contact information reach in at most two taps from any CTA: a one-line statement under the CTA linked to the full policy.

### DP20. Comparison prevention  WARN  LAW
- Definition. deceptive.design: making it hard to compare prices or features; CMA "partitioned pricing".
- Rule. Comparison tables use one unit per row, the same attribute set for every column, and no blank cell where the competitor actually has the feature. Per-unit price is shown wherever pack sizes differ.
- Check. In `comparison` and `us-vs-them` sections, every row has a value in every column; no cell is only a dash for a named competitor unless the plan records the source.

### DP21. Fictitious former price  BLOCK  LAW
- Definition. FTC 16 CFR 233.1; UK CMA duration and volume tests (Emma Sleep was/now judgment 30 Jul 2026); EU Price Indication Directive 30-day prior price; India MRP rules.
- Rule. A struck-through price exists only with an offer-ledger `compare_at_basis`. Detail in `references/offers/price-presentation.md` PP1 to PP5.
- Check. Every `<s>`, `<del>`, `[data-part=compare-at]` carries `data-source="compare_at_price"` or the ledger row id.

### DP22. Faux progress and fake processing  BLOCK  LAW
- Definition. FTC bucket I (induce false beliefs); CCPA interface interference. Progress indicators and "analysing your answers..." delays that do not reflect real work.
- Example. "Applying your discount... 87 percent" spinner; "Step 2 of 3" on a one-step form; quiz "Building your routine" delay with a fixed timer.
- Rule. Progress UI reflects real remaining steps from the funnel definition. No decorative delays or fake percentages.

## 3. Enforcement cases to cite when a merchant pushes back

| Case | Pattern | Outcome | URL |
|---|---|---|---|
| FTC v. Amazon (Prime), 2023 to 2025 | Subscription trap, confirmshaming decline, hidden terms | USD 2.5B (USD 1B penalty, USD 1.5B refunds); decline button must be clear and neutral | https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-secures-historic-25-billion-settlement-against-amazon |
| FTC v. Epic Games, 2022 | Dark patterns causing unwanted charges | USD 245M refunds | https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations |
| FTC v. Vonage, 2022 | Hard to cancel, junk fees | USD 100M | https://www.ftc.gov/news-events/news/press-releases/2022/11/ftc-action-against-vonage-results-100-million-customers-trapped-illegal-dark-patterns-junk-fees-when-trying-cancel-service |
| FTC v. Adobe, 2024 | Hidden early-termination fee, obstructed cancellation | Complaint filed | https://www.ftc.gov/news-events/news/press-releases/2024/06/ftc-takes-action-against-adobe-executives-hiding-fees-preventing-consumers-easily-cancelling |
| FTC v. Fashion Nova, 2022 | Suppressed negative reviews | USD 4.2M | https://www.ftc.gov/news-events/news/press-releases/2022/01/fashion-nova-will-pay-42-million-part-settlement-ftc-allegations-it-blocked-negative-reviews-website |
| CMA v. Emma Sleep, 2022 to 2026 | Countdown timers, "high demand" claims, misleading discounts; was/now pricing | Court-confirmed undertakings 22 May 2026; High Court judgment on reference pricing 30 Jul 2026 | https://www.gov.uk/cma-cases/emma-group-consumer-protection-case |
| CMA and Simba Sleep | Genuineness of "was" prices | Formal undertakings | https://www.gov.uk/government/news/cma-launches-court-action-against-emma-to-protect-uk-consumers |
| CJEU Planet49, 2019 | Pre-ticked consent | Pre-ticked boxes invalid | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A62017CJ0673 |
| India CCPA advisory, 5 Jun 2025 | All 13 patterns | Mandatory self-audit within 3 months; notices to platforms | https://consumeraffairs.nic.in/latestnews/ccpa-advisory-terms-consumer-protection-act-2019-self-audit-e-commerce-platforms |
| Sports Direct, 2015 | Basket sneaking (GBP 1 magazine) | Public backlash, practice withdrawn | https://deceptive.design/types/sneaking |

---

# Copy anti-patterns

The canonical vocabulary and structure blacklist for generated page copy.
`/design-page` applies it in Compose step 8; `brand_kit.banned_phrases`
is merged in at run time. Positive rules for headlines, CTAs, FAQs and
microcopy are in `references/copy/headline-and-cta-rules.md`; frameworks in
`references/copy/copy-frameworks.md`; sourcing real language in
`references/copy/voice-of-customer-mining.md`.

Scope of a hit. FAIL when the word or structure appears in an `h1`, `h2`,
`h3`, subhead, button, link label, CTA microcopy or announcement bar. WARN
when it appears in body text fewer than two times; FAIL at two or more body
hits. Text inside `<blockquote>` and review islands is exempt: reviews are
verbatim (`references/proof/proof-ledger.md` rule 4).

Severity BLOCK, FAIL, WARN describes the editorial rule, not permission to
invent claims. Review authored copy outside verbatim quotes against this list
on the persisted source and hosted page; no local extraction script is used.

## 1. Evidence

- Kobak et al., Science Advances 2024/25, 15M PubMed abstracts: after ChatGPT, 379 style words spiked; "delves" 28x, "underscores" 13.8x, "showcasing" 10.7x; 66 percent of excess style words are verbs. https://arxiv.org/html/2406.07016v5
- Pangram (vendor, per 10k words, AI vs human): em dashes 17 vs 2 (10x), triads 19 vs 5 (4x), "not just X but Y" 3 vs 1 (3x), "delve into" class phrases 30 vs 3, bullet lists 9x, emoji 2x. https://www.pangram.com/signs-of-ai-writing
- Community catalogues derived from Wikipedia "Signs of AI writing": antithesis cadence, "from X to Y" sweeps, colon reveals, fragment punchlines. https://github.com/crypdick/unslop/blob/main/skills/unslop/references/ai-writing-patterns.md
- Copyhackers/Beachway: a headline lifted from a real review beat the marketing-written one by over 400 percent in clicks. Real language wins; generic language loses. https://copyhackers.com/2014/10/amazon-review-mining/

## 2. Vocabulary blacklist

CP1 (FAIL in headings and controls; WARN then FAIL in body; RESEARCH, OPERATOR). None of the following appears outside verbatim quotes. The lint list is the union of the three blocks plus `brand_kit.banned_phrases`.

Verbs and verb phrases:
```text
elevate, unleash, unlock (except a literal gate: "Unlock free shipping at ₹999" is allowed), delve, embrace, indulge,
discover (as an imperative opener), experience (as an imperative opener), transform your, revolutionize, revolutionise,
empower, harness, leverage, supercharge, streamline, optimize (consumer copy), reimagine, redefine, showcase, foster,
navigate (metaphorical), dive into, take ... to the next level, say goodbye to, say hello to, look no further, treat yourself
```

Adjectives and nouns:
```text
seamless, effortless, game-changer, game-changing, revolutionary, cutting-edge, next-level, next-generation, state-of-the-art,
world-class, best-in-class, innovative, unparalleled, unmatched, unrivalled, ultimate, premium (unqualified; allowed inside a tier or product name),
luxurious (unqualified), exquisite, meticulous, meticulously, intricate, curated, bespoke (unless made to order), artisanal (unless hand-made),
holistic, synergy, robust, tapestry, realm, journey (metaphorical), landscape (metaphorical), testament, beacon, pivotal, crucial,
vibrant, dynamic, must-have, perfect for, stunning, breathtaking, elevated, sleek, effortlessly chic
```

Phrases and openers:
```text
elevate your routine, in today's fast-paced world, whether you're X or Y, it's not just X, it's Y, not just ... but (also), more than just,
Imagine ... (opener), Picture this, Introducing (headline), crafted with care, crafted with love, premium quality, designed with you in mind,
the perfect blend of, at its finest, like never before, you deserve, the secret to, your go-to, made for modern life, we've got you covered,
sit back and relax, the best part?, here's the thing, let's face it, in a world where, gone are the days, nestled, boasts, a testament to,
from X to Y and everything in between, welcome to, at [Brand], we believe, discover the difference, experience the difference, the ultimate,
your journey, level up, game on, ready to ..., unlock your potential, step into, dive in
```

Allowlist handling. `brand_kit.allowlist` (or the plan's "Copy allowlist" line) removes a term when it is literal: a brand named "Elevate", a tier named "Premium", a hair oil that is literally "curated" by a named person. Every allowlisted hit is recorded in `page plan` with the reason.

## 3. Claims

| Id | Tell | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| CP2 | Superlatives and objective claims without substantiation: best, #1, No.1, most trusted, most advanced, clinically proven, doctor recommended, dermatologist tested, award-winning, 100% natural, chemical-free, toxin-free, guaranteed results, proven to | FTC: objective claims need a reasonable basis before publication; "clinically proven" needs that evidence. India ASCI/CCPA: "No.1" only with market-share data; disclaimers may not contradict the claim. Each hit must map to a proof-ledger row (`test-data`, `award`, `certification`, `customer-count`). https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business ; https://www.ascionline.in/wp-content/uploads/2022/09/asci_june_july_2020_ccc_pr.pdf | BLOCK | LAW |
| CP3 | Hedged non-claims: may help support, can help promote, is believed to, designed to help, supports healthy ... | Either a substantiated fact with a number, or cut the sentence. Where regulation mandates a hedge (supplement structure/function claims), keep the mandated wording and pair it with dose, ingredient or study n. | WARN | OPERATOR |
| CP4 | "Results not typical" or "results may vary" as the only qualifier beside a results testimonial | FTC Endorsement Guides: disclose the generally expected result in the same block; the bare disclaimer does not comply. https://www.govinfo.gov/content/pkg/CFR-2023-title16-vol1/pdf/CFR-2023-title16-vol1-part255.pdf | BLOCK | LAW |

## 4. Structure tells

| Id | Tell | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| CP5 | Em-dash chains | At most one em dash per 150 words; none in headings, buttons or subheads. Prefer a full stop. Pangram: 10x more em dashes in AI text. | FAIL | RESEARCH |
| CP6 | Rule of three everywhere ("soft, breathable, and durable") | At most one adjective triad per section. Lists of specifics beat adjective triads. | WARN | RESEARCH |
| CP7 | Antithesis: "not just X, it's Y", "isn't just ... it's", "more than just" | Zero. | FAIL | RESEARCH |
| CP8 | Rhetorical-question openers ("Tired of ...?", "Ever wondered ...?") | At most one question heading per page; never the h1 unless the type uses `qualifier-lead` and the question genuinely selects the reader. | WARN | OPERATOR |
| CP9 | "Imagine ..." or "Picture this" | Zero. | FAIL | RESEARCH |
| CP10 | Exclamation marks | Zero outside verbatim reviews. | FAIL | OPERATOR |
| CP11 | Uniform sentence and paragraph length | Standard deviation of sentence length at least 4 words per section; no three consecutive paragraphs within 10 percent of the same word count. | WARN | HEURISTIC |
| CP12 | Identical section rhythm (headline, subhead, three bullets, CTA, repeated) | Adjacent sections never share the same layout skeleton (`references/anti-patterns/design-anti-patterns.md` DA14). | FAIL | OPERATOR |
| CP13 | Alliterative or fragment triad headlines ("Pure. Potent. Proven.") | At most one fragment-triad heading per page. | FAIL | RESEARCH |
| CP14 | Summary and conclusion language ("In conclusion", "Ultimately", "Overall", "To sum up") | Zero. A landing page asks; it does not conclude. | FAIL | OPERATOR |
| CP15 | Colon reveal in headings ("The result: skin that ...") | At most one per page. | WARN | RESEARCH |
| CP16 | Title Case Headings | Sentence case for headings, subheads, buttons, labels; product names keep brand casing. USAGov moved to sentence case sitewide in 2023 with no trust drop. https://www.usa.gov/blog/2023/09/making-the-case-for-sentence-case | FAIL | RESEARCH |
| CP17 | Bold-label bullets ("**Fast:** ...", "**Simple:** ...") | Zero. Write the specific. | FAIL | RESEARCH |
| CP18 | False ranges ("from busy parents to pro athletes") | Only when X and Y are real endpoints of one scale the merchant serves. | WARN | RESEARCH |
| CP19 | Generic openers ("Welcome to ...", "At [Brand], we believe ...", "We are passionate about") | Zero. Lead with the shopper's problem or a specific. | FAIL | OPERATOR |
| CP20 | Subhead restates the headline | The subhead resolves the headline (mechanism, proof or who it is for); token overlap with the h1 under 50 percent. | FAIL | OPERATOR |

## 5. Punctuation and case

| Id | Tell | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| CP21 | Hype punctuation: "!!", "?!", "..." trails in headings | Zero. | FAIL | OPERATOR |
| CP22 | ALL-CAPS words of six or more letters | None outside a `CAPS_ALLOWLIST` of acronyms and registered marks (GST, FSSAI, UPI, MRP, BIS, ISO, NSF, USDA, SPF, COD, EMI, BNPL). Labels of three words or fewer may be caps only under a merchant-stated rule (design-rules N5). | FAIL | RESEARCH |
| CP23 | Arrow glyphs or "->" in link and button text | Design-rules N12. | FAIL | OPERATOR |
| CP24 | Emoji anywhere in copy | Design-rules N1. | FAIL | OPERATOR |
| CP25 | Middle dots (U+00B7) joining meta strings ("Free shipping", dot, "30-day returns", dot, "Made in India") | Use a full stop or separate lines; N12 names middle-dot joins as chrome. | WARN | OPERATOR |

## 6. CTA and control copy

| Id | Tell | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| CP26 | Stock CTA labels: Shop Now, Get Started, Learn More, Buy Now (tof/mof), Submit, Click here, Continue (no object), OK, Yes, Go, Read more | Design-rules A12; `references/copy/headline-and-cta-rules.md` HC12 to HC14. The CTA is verb plus object plus outcome or price, at most four words, sentence case. | FAIL | OPERATOR |
| CP27 | CTA that does not start with a verb, or exceeds four words | HC12. | FAIL | OPERATOR |
| CP28 | "Free" with an asterisk or a later condition | Offers OF5: the condition sits in the same line. | BLOCK | LAW |

## 7. Placeholder and model leakage

| Id | Tell | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| CP29 | Placeholder text: lorem ipsum, TODO, TBD, [brand], [product], {{ }}, "Your headline here", "Insert ...", "Product name", "Lorem" | Zero. A12 already forbids placeholder copy. | BLOCK | OPERATOR |
| CP30 | Framework labels leaking into copy ("Problem:", "Agitate:", "Solution:", "Benefit:", "Call to action") | Zero. Frameworks shape the order, never the words. | FAIL | OPERATOR |
| CP31 | Assistant voice leaking ("As an AI", "Certainly", "Here's a", "I hope this helps", "Feel free to") | Zero. | BLOCK | OPERATOR |

## 8. Brand voice

| Id | Tell | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| CP32 | A `brand_kit.banned_phrases` entry appears | BLOCK in any position, including body. Merged into the lint list at run time; the plan's "Copy allowlist" cannot override a merchant ban. | BLOCK | OPERATOR |
| CP33 | Register mismatch with `voice_md` (jokey copy for a clinical brand; clinical copy for a playful brand) | Reviewed by an LLM pass against the voice adjectives and "we say / we don't say" pairs; not regex. | WARN | OPERATOR |
| CP34 | Brand name outnumbers "you/your" | Second person leads; Apple's iPhone 5 copy used "you/your" more than "iPhone" and "Apple" combined. https://neilpatel.com/blog/write-copy-like-apple/ | WARN | RESEARCH |
| CP35 | Spelling locale drift (color and colour on one page) | One locale from `brand_kit` or the store market. | WARN | OPERATOR |

## 10. Rewrite procedure for a hit

1. Ask Harry Dry's three questions of the sentence: can the reader visualise it, can it be falsified, could no competitor say it. A line failing all three is deleted, not rephrased. https://www.demandcurve.com/lessons/fundamental-rules-of-good-copy
2. Replace the banned word with what specifically happens: "seamless" becomes "arrives assembled, no tools"; "premium quality" becomes the material, weight or test.
3. Pull the replacement from the voice-of-customer worksheet (`references/copy/voice-of-customer-mining.md`) before inventing one.
4. Re-run the section checks; a heading hit blocks compile, a body hit produces a rewrite note in `QA record` with the span and the rule id.

---

# Lexsis MCP Tool Sequence by Stage

The exact `router.action` order for a page, from setup to publish. Skills list
the actions they own; this file shows how they chain and what each call must
return before the next one runs. Resolve an unfamiliar argument schema with
`lexsis_discover` using structured `router` and `action` fields, never a
prose query for a known pair (`references/lexsis-mcp-contract.md`).

Legend: **R** read, **W** reversible write, **$** spends credits (confirm
first), **!** requires explicit approval (`lexsis_live_ops`).

## Stage 0: Setup (once per store/theme)

| # | Call | Type | Needed before |
|---|---|---|---|
| 1 | `lexsis_workspace.list` then `.get` | R | everything |
| 2 | `lexsis_workspace.stores` | R | choosing the store |
| 3 | `lexsis_brand.context` | R | any design decision |
| 4 | `lexsis_brand.brand_kit` | R | palette, fonts, voice, banned phrases |
| 5 | `lexsis_brand.list_themes` then `.get_theme` | R | `theme_css` |
| 6 | `lexsis_brand.navigation` | R | header/footer links (full-nav types only) |
| 7 | `lexsis_design.guide` | R | `brand-design.md` |

Output: `work/storefront/setup/setup.json` plus saved brand and theme files.
Everything below reads the saved pair and refreshes only volatile data.

## Stage 1: Plan

Order matters: identify the type before searching anything.

| # | Call | Type | Purpose | Gate |
|---|---|---|---|---|
| 1 | read `setup.json` | local | one store/theme pair | stop if missing |
| 2 | `lexsis_catalog.list` then `.get` per product | R | title, variants, prices, availability, media, description | every product on the page |
| 3 | walk `references/page-types/_index.md`, then the type's `## Workflow` context reads | local | `pageType`, funnel stage, awareness, offer, campaign; image count and jobs, variant axes, review band | record `## Page type` block |
| 4 | `lexsis_campaigns.creatives` then `.analyze` (or view the creative yourself) | R | message match for ad-driven types | ad-landing, advertorial, listicle, retargeting |
| 5 | `lexsis_campaigns.personas` then `.match_persona` | R | vocabulary, pain points | when personas exist |
| 6 | `lexsis_catalog.reviews_status` | R | is a review source connected, how many imported | before any proof plan |
| 7 | `lexsis_catalog.review_collections` (`collection_status: "active"`) | R | curated sets with counts | if connected |
| 8 | `lexsis_catalog.reviews` (`rating_min`, `has_media`, `product_id`) | R | count, media, distribution | if connected |
| 9 | `lexsis_catalog.reviews_search` (`query` = the page's key claim) | R | proof-proximity candidates | one call per top decision question |
| 10 | host web search + `lexsis_assets.view` | R | zero-review playbook tiers 3 to 5 | only when 6 to 8 return nothing usable (`references/proof/reviews-sourcing.md`) |
| 11 | `lexsis_template_library.search_page_kits` (`query: ""`, filters) | R | user picks or skill picks a direction | after page type is fixed |
| 12 | `lexsis_template_library.search_sections` | R | when no kit fits | at most three candidates |
| 13 | `lexsis_template_library.get_kit` | R | resolve a slug or URL | user-picked kit |
| 14 | `lexsis_asset_library.search` (`theme_id`, `mode: "tags"`, then semantic) | R | resolve slots the user did not pick | after gallery jobs mapped |
| 15 | `lexsis_assets.view` | R | verify identity-sensitive picks | every product or person image |
| 16 | `lexsis_asset_import.import` or `lexsis_asset_upload.upload` | W | import a supplied URL, image base64 plus MIME type, or attachments; use upload only for the local-file UI | before any generation; wait for the user's uploaded-asset message for UI uploads; without inline UI, ask for a URL or attachment and import it |
| 17 | `lexsis_workspace.credits` | R | balance before asking | before 18 |
| 18 | `lexsis_drafts.asset_generate` | W $ | only ALLOW-list purposes (`references/assets/generation-policy.md`) | one confirmation per batch |
| 19 | `lexsis_capture.funnel_templates` then `.funnel_template` | R | quiz, gift-reveal, personalised-offer structure | quiz-funnel and lead-capture types |
| 19b | `lexsis_capture.form_schemas`, then `.submissions` for an existing form | R | field shapes; whether a live form already collects what the page needs (PII is redacted) | lead-capture, giveaway, wholesale, waitlist |
| 20 | `lexsis_drafts.review_collection_create` | W | draft shortlist for the merchant to activate | only when asked |

Output: `page plan` with Page type, Page strategy, Design direction, Consumer
decision model, Section specification, Asset slots with decisions, Proof
ledger, Offer ledger, Claim gate, Work queue, Plan status; compact
`page record`. Review the type checklist before approval; the plan waits for
explicit approval before design.

## Stage 2: Design

| # | Call | Type | Purpose | Gate |
|---|---|---|---|---|
| 1 | read plan + manifest + page-type file | local | follow its `## Workflow`; note deviations | ask only when a deviation is unexplained |
| 2 | `lexsis_brand.context`, `.get_theme` | R | live tokens | compare with saved; `THEME_CONTEXT_CONFLICT` on value clash |
| 3 | `lexsis_template_library.get_kit` then `lexsis_design.get_section` (1 to 3 ids per call, kit order) | R | authoring source | only ids in the page record |
| 4 | `lexsis_template_library.list_mine` then `.get_mine` | R | merchant's saved sections | when the user names one |
| 5 | `lexsis_design.islands` | R | compact catalog | select only interactive needs |
| 6 | `lexsis_design.island_schema` | R | exact props | per island actually used, or per compile error |
| 7 | `lexsis_catalog.get` | R | current variant ids, prices | before binding BuyBox |
| 8 | `lexsis_catalog.reviews` / `.review_collection_items` | R | `collectionId` or `productIds`, `minRating`, real totals | review islands only |
| 9 | `lexsis_asset_library.search`, `lexsis_assets.view`, `lexsis_asset_import.import`, `lexsis_asset_upload.upload` | R/W | resolve `planned` slots; import supplied sources, upload for local-file UI only | never placeholders; wait for the user's uploaded-asset message for UI uploads |
| 10 | `lexsis_workspace.credits` then `lexsis_drafts.asset_generate` | W $ | remaining ALLOW-list gaps | ask first |
| 11 | `lexsis_pages.compile` | R | validation_errors as the work list | loop until clean |
| 12 | `lexsis_page_create.create` (`publish: false`) | W | one hosted draft | once per page; reuse `remote.pageId` after |
| 13 | host browser at 390, 768 and 1280 | local | hosted design review and commerce checks | always before `DESIGN_APPROVED` |
| 14 | `lexsis_drafts.page_update_section` / `.page_patch` (`expected_version`) | W | fix review findings | never a second draft |

Output: persisted page id/version, hosted preview and compile evidence;
`DRAFT_CREATED`, later `DESIGN_APPROVED`. No local page files are created.

## Stage 3: Hosted QA and edits (inside `/design-page` and `/optimize`)

| # | Call | Type | Purpose |
|---|---|---|---|
| 1 | `lexsis_pages.edit_context` then `.source` | R | detect version drift |
| 2 | `lexsis_catalog.get` | R | refresh variants and prices |
| 3 | `lexsis_design.island_schema` | R | islands still active |
| 4 | `lexsis_pages.compile` | R | clean artifact |
| 5 | `lexsis_pages.integrity` then `.qa` | R | hosted QA record |
| 6 | `lexsis_drafts.page_record_qa` | W | store QA evidence |
| 7 | `lexsis_drafts.page_update_head` | W | title, description, fonts |
| 8 | `lexsis_cart.get` then `lexsis_drafts.cart_set` | R/W | cart profile matches the offer |
| 9 | `lexsis_capture.get_funnel`, `.validate_funnel`, `.preview_funnel`; `lexsis_drafts.funnel_update` | R/W | a funnel draft's steps read back, validated, previewed and adjusted before review |
| 10 | `lexsis_support.search_docs` | R | only when a Lexsis behaviour is unclear |

Output: `DESIGN_APPROVED` for the reviewed page version.

## Stage 4: Publish and after

| # | Call | Type | Purpose |
|---|---|---|---|
| 1 | `lexsis_live_ops.publish` | W ! | named page and version only |
| 2 | `lexsis_analytics.page`, `.timeseries`, `.attribution` | R | first-week read |
| 3 | `lexsis_drafts.page_duplicate` then `.experiment_create` | W | challengers (`/ab-test`) |
| 4 | `lexsis_analytics.experiment` then `lexsis_live_ops.scale_winner` | R / W ! | evaluate, then scale |
| 5 | `lexsis_live_ops.rollback` / `.unpublish` | W ! | undo |

## Never

- Never call `lexsis_page_create.create` when `remote.pageId` exists.
- Never call `lexsis_drafts.asset_generate` before `lexsis_asset_library.search`
  and `lexsis_catalog.get` have been checked for the same slot.
- Never fill review props from anything other than `lexsis_catalog.reviews`
  or `.review_collection_items`.
- Never use `lexsis_discover` as a health check; a zero-count directory
  result is a lookup miss.
- Never call a `lexsis_live_ops` action without the user's explicit approval
  for that page and version in the current conversation.

---

# MCP router/action inventory

Derived from the `CONSOLIDATED_ROUTERS` declaration in the sibling MCP
service on 2026-09-11: 18 routers, 92 actions. Re-derive this inventory when
that source changes. This lists operation names, not arguments or island
props; resolve an unfamiliar action schema before calling it.

| Router | Actions |
|---|---|
| `lexsis_workspace` | `lexsis_workspace.list`, `lexsis_workspace.get`, `lexsis_workspace.stores`, `lexsis_workspace.credits` |
| `lexsis_assets` | `lexsis_assets.capabilities`, `lexsis_assets.view` |
| `lexsis_asset_library` | `lexsis_asset_library.search` |
| `lexsis_asset_import` | `lexsis_asset_import.import` |
| `lexsis_asset_upload` | `lexsis_asset_upload.upload` |
| `lexsis_campaigns` | `lexsis_campaigns.creatives`, `lexsis_campaigns.analyze`, `lexsis_campaigns.frames`, `lexsis_campaigns.personas`, `lexsis_campaigns.match_persona` |
| `lexsis_brand` | `lexsis_brand.context`, `lexsis_brand.brand_kit`, `lexsis_brand.list_themes`, `lexsis_brand.get_theme`, `lexsis_brand.navigation`, `lexsis_brand.compile_theme` |
| `lexsis_catalog` | `lexsis_catalog.list`, `lexsis_catalog.get`, `lexsis_catalog.reviews_status`, `lexsis_catalog.reviews`, `lexsis_catalog.reviews_search`, `lexsis_catalog.review_collections`, `lexsis_catalog.review_collection_items` |
| `lexsis_pages` | `lexsis_pages.list`, `lexsis_pages.find`, `lexsis_pages.get`, `lexsis_pages.edit_context`, `lexsis_pages.content`, `lexsis_pages.source`, `lexsis_pages.section_source`, `lexsis_pages.inspect`, `lexsis_pages.diff`, `lexsis_pages.integrity`, `lexsis_pages.qa`, `lexsis_pages.compile`, `lexsis_pages.compile_artifact` |
| `lexsis_drafts` | `lexsis_drafts.asset_generate`, `lexsis_drafts.theme_update`, `lexsis_drafts.page_replace`, `lexsis_drafts.page_patch`, `lexsis_drafts.page_attach_bundle`, `lexsis_drafts.page_update_section`, `lexsis_drafts.page_remove_section`, `lexsis_drafts.page_move_section`, `lexsis_drafts.page_update_head`, `lexsis_drafts.page_record_qa`, `lexsis_drafts.page_duplicate`, `lexsis_drafts.page_variation`, `lexsis_drafts.template_create`, `lexsis_drafts.template_update`, `lexsis_drafts.template_apply`, `lexsis_drafts.experiment_create`, `lexsis_drafts.funnel_create`, `lexsis_drafts.funnel_update`, `lexsis_drafts.cart_set`, `lexsis_drafts.cart_edit`, `lexsis_drafts.review_collection_create`, `lexsis_drafts.send_feedback` |
| `lexsis_page_create` | `lexsis_page_create.create` |
| `lexsis_live_ops` | `lexsis_live_ops.publish`, `lexsis_live_ops.unpublish`, `lexsis_live_ops.delete`, `lexsis_live_ops.rollback`, `lexsis_live_ops.template_publish`, `lexsis_live_ops.template_archive`, `lexsis_live_ops.scale_winner` |
| `lexsis_design` | `lexsis_design.guide`, `lexsis_design.islands`, `lexsis_design.island_schema`, `lexsis_design.get_section` |
| `lexsis_template_library` | `lexsis_template_library.search_sections`, `lexsis_template_library.search_page_kits`, `lexsis_template_library.get_kit`, `lexsis_template_library.list_mine`, `lexsis_template_library.get_mine` |
| `lexsis_analytics` | `lexsis_analytics.timeseries`, `lexsis_analytics.page`, `lexsis_analytics.attribution`, `lexsis_analytics.experiment` |
| `lexsis_capture` | `lexsis_capture.form_schemas`, `lexsis_capture.submissions`, `lexsis_capture.funnel_templates`, `lexsis_capture.funnel_template`, `lexsis_capture.get_funnel`, `lexsis_capture.validate_funnel`, `lexsis_capture.preview_funnel` |
| `lexsis_cart` | `lexsis_cart.get` |
| `lexsis_support` | `lexsis_support.search_docs` |

---

# Shared page workflow

The compiler determines valid input. `references/design-rules.md` owns house
requirements; domain policy owns evidence and permissions. The selected
page-type contract owns anatomy and type-specific decisions. Workflows
execute those decisions, never relax their requirements.

## Reading order

1. Select one contract through `references/page-types/_index.md`.
2. Read its context requirements and checklist. Keep the required headings
   and JSON contract; record deviations with their reasons.
3. Execute each section's type-specific row through the four procedures
   below. Read each procedure once, then apply it to every relevant section.
4. Reconcile the asset budget and evidence, then inspect compiler results and
   perform the hosted review at 390, 768 and 1280 before `DESIGN_APPROVED`.

## Four procedures

| Procedure | Single home | Type-specific inputs |
|---|---|---|
| Asset acquisition and missing-slot handling | `references/workflows/section-asset-workflow.md` section 1 | Job, source/tag, crop, required count and legitimate fallback |
| View and section fit | `references/workflows/section-asset-workflow.md` section 2 | Product/variant, composition, adjacent slots and intended crop |
| Interactive selection | `references/workflows/island-selection-workflow.md` | Candidate family and the decision that requires behavior |
| Copy execution | `references/workflows/copy-workflow.md` | Message, evidence, specific ceilings and CTA destination |

A type file supplies the differences, not another copy of these procedures.
"Media: no" is a valid type-specific decision; not every section needs an
image. Static facts, native disclosures and tables remain legitimate content.

## Planning and design responsibilities

`/plan-page` resolves context and asset jobs, records functional intent and
visual direction, and names deviations. It does not choose schema props or
force an island. `/design-page` executes the interactive-selection procedure
against the current catalog and schemas, then compiles the source. Reopen a
planned decision only when new evidence or a contract conflict requires it.
A saved preset label is descriptive intent, not a prop bundle to paste.

## Evidence and handoff

Use `references/page-files.md` and `references/source-artifact-workflow.md`
for page/campaign records, direct MCP authoring and version evidence. Do not create
another ledger format here. Source eligibility and generation permissions
remain in `references/assets/`; proof and offer rows remain in their domain
ledgers. Production claims need the appropriate confirmed evidence.

Type deviations and copy findings are review notes; unsupported proof and
offers block readiness. Review notes do not make unsupported claims acceptable.
Hosted evidence and draft/release state follow `references/qa-recipe.md`
and `references/workflow-intent.md`.

---

# Section asset workflow

This is the single execution procedure for sourcing, missing-slot handling,
and visual fit. Type files provide jobs, tags, crops and budgets; policy
lives in `references/assets/asset-sourcing-sequence.md`,
`references/assets/generation-policy.md`, `references/assets/slot-spec.md`,
`references/assets/video-rules.md` and the relevant proof ledger.

## 1. Acquisition and missing-slot handling

1. Read the type's section job and budget. Decide whether imagery is needed;
   a native disclosure or factual table does not need a decorative image.
2. Inventory real catalogue media, the merchant's selections, and existing
   library assets before planning new media. Assign each candidate its actual
   job, product/variant, dimensions and rights evidence.
3. Follow the source eligibility order in
   `references/assets/asset-sourcing-sequence.md`. Use the type's search tags
   and queries. A missing tag is not proof that the library is empty.
4. Run the fit review in section 2 before binding a candidate. Retain rejection
   reasons so the same unsuitable image is not proposed repeatedly.
5. For a remaining slot, consult `references/assets/generation-policy.md`.
   That file owns ALLOW / ASK / NEVER, credit approval, identity protection,
   prompts and generation records. Do not infer permission from a page type.
6. Tell the merchant what is missing: section, job, aspect, count and why it
   matters. Offer **upload**, **generate** only where that policy permits it,
   or **skip/merge** with an explanation of what the page loses. Group gaps
   into one useful message, not a question for each section.
7. A fast draft may use the closest existing asset that honestly performs a
   suitable job, or leave the slot `planned`. Record all unresolved slots in
   the plan and draft summary. Do not silently remove a required section.
   Production readiness requires resolution of its required slots; an
   explicit type deviation still needs a reason and appropriate evidence.
8. Skip or merge a section only on the merchant's decision. A generation ban
   is not permission to invent media, substitute irrelevant stock, or hide
   the missing job behind a decorative band.

### Import, upload and selection

- `lexsis_asset_library.search` selects existing assets. With an empty query,
  wait for the `Design asset selection:` message when inline selection UI is
  available; map its selection order to the named slots.
- `lexsis_asset_import.import` persists an available URL, image base64 with
  MIME type, or conversation attachments. Supply exactly one source.
- `lexsis_asset_upload.upload` opens the local-file UI. Scope it to the
  selected workspace/theme and wait for the user's uploaded-asset message.
  Without inline UI, ask for a URL or conversation attachment and import it.
  Opening a panel is not an upload. The exact argument contract is in
  `references/lexsis-mcp-contract.md`.

### Search efficiently

Use the current search schema. Tags such as `hero`, `lifestyle`,
`product-shot`, `social-proof` and `logo` are conventions, not a closed enum.
Try semantic queries for missing jobs and filename lookup for a supplied
filename. Where supported, OCR search helps identify baked-in overlays and
similarity search around a verified seed helps maintain a coherent set.
Result geometry screens candidates before the visual review; metadata never
replaces inspection. Keep the selected workspace and theme binding explicit.

## 2. View and fit review

Nothing is used sight unseen. Open each candidate with `lexsis_assets.view`;
if the host cannot display it, inspect the returned permanent URL with the
available image viewer. Judge the asset **in its intended section**:

| Check | Required decision |
|---|---|
| Identity and job | Correct product/variant; the image actually demonstrates the assigned job |
| Crop | Desktop and mobile crops preserve the subject and required detail |
| Text placement | Copy has an appropriate quiet region, or moves outside the image; A7 still governs contrast |
| Set consistency | View adjacent/grid candidates together; they should read as one shoot rather than unrelated finds |
| Palette | The image works with the plan's visual direction without falsifying product appearance |
| Resolution | Detail survives at the actual mobile and desktop rendered sizes |
| Source integrity | Rights are recorded; no misleading overlay, watermark or competitor branding; genuine product labels remain readable where the job requires them |

A near-uniform preview can be a failed preview. Inspect the original URL
before rejecting the asset or spending credits on a replacement. Apply this
same review after generation; payment is not evidence of suitability. A
rejected generation returns to the policy's bounded repair/fallback route.

## 3. Asset budget and record

The type's budget records supplied jobs, missing jobs and type-specific
alternatives. It does not redefine source permissions. Assign each slot a
source decision, rights basis, final asset or Shopify media id, and status.
Use the workspace record defined in `references/page-files.md`; generation
records follow the generation-policy owner. Mark rejected or unresolved jobs
accurately even when a different verified image allows a reversible draft.

Example merchant message: "The kit has a packaging image but no image of
all included items. Supply one overhead kit photo, or choose to omit the
optional unboxing section; the included-items job is still pending."

## 4. Write to the resolved job

After the media decision, execute `references/workflows/copy-workflow.md`.
Do not invent benefit imagery or pad the copy because a requested image is
missing. A deliberately text-only section follows its type contract.

---

# Live island selection

This is the single procedure for choosing interactive components. A page
contract names candidate families and decision inputs, not a prop schema.
Planning records functional intent; design resolves implementation.
`references/authoring/source-authoring.md` owns markup, and
`references/authoring/css-and-styling.md` owns styling.

## 1. Decide whether behavior is required

Use static HTML for factual text, comparisons, native disclosures, linked
logos, tables, navigation anchors and simple product lists. Add an island
only for required state, catalogue binding, media behavior, capture,
subscription/variant selection or an overlay. Do not create an island merely
because a legacy file named one.

## 2. Resolve the current catalog and schema

1. Read the type's decision inputs: product and media count, variant axes,
   selling plans, review availability, capture purpose and page length.
2. Call `lexsis_design.islands` for the compact current catalog. Exclude
   entries marked deprecated and entries disallowed by domain policy.
3. Call `lexsis_design.island_schema` for the selected candidate. Read its
   supported variants, required props, defaults, authoring examples,
   hydration mode, parts, CSS variables and headless support.
4. Select only a variant and props justified by the actual page decision.
   Bind real catalogue/ledger ids. Do not infer a field from a sibling
   island, old prose example, intent label or bundled prop map.
5. Check defaults against the house requirements. Disable incidental motion
   when the plan does not authorize it; a schema default is not a policy
   exemption. Do not hide data with filters when the section claims to show
   the full distribution.
6. Use source-format examples from that live schema and compile. Revisit the
   schema when an error or an unmet behavior requires it; never fetch every
   full schema without a decision that needs it.

## 3. Candidate families

| Job | Candidate direction | Decision inputs |
|---|---|---|
| Purchase | BuyBox | Actual product, variants, selling plans and approved design |
| Gallery | ProductGallery, ProductHero, ImageZoom | Image count/jobs, aspect, variant images and inspection needs |
| Linked purchase bar | StickyBar | Page length and the live purchase synchronization contract |
| Product browsing | QuickAdd, ProductCarousel, FeaturedCollectionStage | Need for commerce behavior beyond native product links |
| Reviews | ReviewCarousel, ReviewList | Eligibility and scope from `references/proof/reviews-sourcing.md` |
| Product explanation | IngredientExplorer, BeforeAfter | Verified product/evidence requirements, not decorative proof |
| Media | VideoPlayer, MediaCarousel, ShoppableVideoFeed | User-controlled behavior required by the type |
| Capture | EmailCapture, FunnelRuntime | Real form schema and the type's authorized goal |
| Availability or deadline | InventoryIndicator, CountdownTimer | Verified offer-ledger basis and type permission |
| Navigation/overlay | SiteHeader, Navbar, Footer, MobileMenu, Modal | Required navigation or interaction, with one owner per role |

These are candidate names, not a frozen catalog or prop map. Re-check the
current catalog before use. Policy owners decide whether a candidate's job
is allowed; an available component is not permission to deploy it.

## 4. Purchase state and styling

Keep one owner for purchase state. When the live schemas support linked
BuyBox and StickyBar controls, use their matching synchronization key and
complete variant catalog so variant, quantity, effective price, selling plan,
availability and cart-pending state remain consistent. External selectors
must use the group's supported scoped-event contract. Never replace this
with two independent cart handlers. If the current schemas cannot express
the intended linkage, route the secondary control back to the main form.

Record actual variant/props and schema evidence in the page decision record. A
`Preset: <island>/<intent>-<tone>` label describes the desired appearance; it
is not executable configuration. Resolve its intent now and record deviations.
Use only live schema parts/CSS variables, scoped by section id.

## 5. Retired jobs

| Retired component name | Current implementation |
|---|---|
| FAQ | Native `details` and `summary` |
| Tabs | Native radio controls with labels or disclosures |
| Marquee | Static linked logo/list markup; no ticker by default |
| StatCards | Static semantic figures with sourced values |
| BackToTop | Native anchor to a stable page id |
| Carousel | Native scroll snap or a justified active specialist |
| CartDrawer | Cart V2 through `head.use_cart_v2` |
| Countdown | CountdownTimer, only after ledger and live-schema checks |

Retained schema files for older pages are compatibility artifacts. They do
not authorize using retired components in new source. Non-existent names
have no schema to resolve; use the native job or an active catalog candidate.

---

# Copy execution

This workflow applies copy policy; it does not define another blacklist,
word-budget table or persuasion framework. Defaults and numeric ceilings
live in `references/copy/headline-and-cta-rules.md`. Framework selection lives
in `references/copy/copy-frameworks.md`; paid-traffic assessment lives in
`references/copy/message-match.md`.

## Procedure

1. Read the section's purpose, resolved media job, evidence and CTA target.
   Write the copy to what the shopper can actually inspect, including a
   deliberate text-only section where the type specifies one.
2. Apply the default ceilings from the copy-policy owner. The type may supply
   a specific message, section budget or deliberate exception; record the
   reason instead of copying the universal ceiling into every type file.
3. Use the merchant's voice and concrete product facts. Keep quotations
   verbatim and trace proof/offer numbers to their ledger rows.
4. Make the CTA describe its real action and destination. A navigation link
   must not pretend to add to cart. Preserve the selected type's goal model.
5. Check the actual layout at review widths. Rework an overlong heading or
   paragraph rather than hiding content, reducing contrast or inventing an
   image. Alt text follows `references/assets/slot-spec.md`.
6. Review the blacklist in `references/anti-patterns/copy-anti-patterns.md`
   and house N1/N3/N5/N6/N12/A12. Run copy lint as an advisory review;
   unsupported proof or offer content remains blocking in hosted design review.

---

# Source authoring

The compiler owns acceptance of source. House requirements are in
`references/design-rules.md`; CSS is owned by
`references/authoring/css-and-styling.md`. This file owns markup mechanics,
not another style policy or island-selection table.

## Source inputs

Author one source value and pass it directly to MCP. Pass structured `head`,
optional `scripts` and any page-wide `theme_css` separately from the HTML.
`references/source-artifact-workflow.md` owns the direct-input contract and
persisted version evidence; no HTML or CSS file is created.

## Section identity

A section starts at `<!-- section: kebab-case-id -->` and continues to the
next delimiter. Use one matching `<section id="kebab-case-id">` per delimiter.
Ids come from `references/page-types/_checklist-format.md`, including its
suffix convention. Keep ids stable across patches; renaming can break
anchors and version history. Announcement, header, footer and navigation are
ordinary source sections in the declared order, not a hidden renderer shell.

## Island markup

Resolve interactive decisions through
`references/workflows/island-selection-workflow.md`. For the chosen island,
use `<lx-island name="...">` with one readable `application/json` child
containing the props confirmed by its current schema. Use the live schema's
authoring example rather than a static prop map.

Allowed source attributes are `name`, `hydrate`, `class`, `id`, `style`,
and `headless` where supported. Read the hydration default and headless
contract live. A different island's defaults or hooks are not evidence.
Source uses `hydrate`; `data-island`, `data-props` and `data-hydrate` are
compiled renderer markers and are not hand-authored source.

A fallback is one `data-lx-island-fallback` child alongside the JSON child.
It contains readable static information, not a competing purchase handler.
Supported headless behavior is different from fallback content: fetch the
current required hooks, preserve their state contract, and test the result.
Navigation hydration hooks likewise come from the selected live schema.

Cart behavior comes from `head.use_cart_v2` and the published cart profile,
not an authored cart section. Required singleton roles and linked purchase
state are resolved in the island-selection owner.

## Native content

Use semantic HTML for content that does not need an island: disclosures,
comparison tables, static statistics, linked logos and product navigation.
Preserve native keyboard/focus behavior. A radio group needs real labels;
a table needs meaningful headers and an appropriate caption. House A11 owns
control sizing. Native markup is not a license to recreate cart logic.

## Head and external code

- `head.title` contains the real title; approved font stylesheet URLs belong
  in structured `head.fonts`, not CSS imports or section link tags.
- `scripts[]` is for approved integrations and analytics. Animation engines
  use the managed loaders described in `references/animation-system.md`.
- Keep JSON and JSON-LD scripts in their supported HTML locations. Never
  escape a whole section into an HTML string; valid HTML entities in text
  and attribute values remain ordinary HTML.
- Custom motion uses `application/lexsis-motion` under the house budget.
  Follow the managed API contract rather than copying raw timers, global
  DOM access, observers, storage, networking or programmatic clicks into JS.
- Plain top-level section script is compatibility behavior, not a route
  around the compiler's managed-code checks.

## Compile handoff

Write complete source, then follow `references/generation-protocol.md` for
exact-input compilation, repair, draft creation or versioned editing. A clean
compile does not prove visual quality. Hosted design review and production
readiness follow `references/qa-recipe.md`.

---

# CSS and styling

The compiler accepts or rejects CSS and utilities. House visual and
accessibility rules live in `references/design-rules.md`; do not weaken
them through a theme, template, preset or component default.

## 1. Cascade and ownership

The cascade is theme CSS, generated Tailwind utilities, then section CSS in
page order. The renderer supplies its reset and base styles; do not duplicate
them. The page-wide `theme_css` value owns theme tokens, the plan's radius/type scales,
page-wide focus styles and reduced-motion handling. Literal utility classes
own layout, spacing, sizing, responsive behavior and state styling.
Section CSS is exceptional and always scoped to its section id.

## 2. Utilities first

Author mobile first using literal classes supported by the compiler. Do not
construct class names at runtime, add a Tailwind CDN, or invent unconfigured
utilities. Resolve every `missing_candidates` entry rather than assuming it
will render. The house rules own the spacing/type scales and permitted
state feedback; this file does not define another set of values.

## 3. Section CSS jobs

Use section CSS only for geometry utilities cannot express, visual overrides
of schema-declared parts/variables, the plan's named motion, a feature-query
fallback, or a scoped print/RTL adjustment. Complex named-grid geometry can
need CSS; ordinary columns and breakpoints remain utilities.

Every selector begins with the section id. Scope each selector in a comma
list separately. Keyframes have unique section-qualified names. Never add
page-global element selectors, a second container system, or `!important`.
Tokens belong in the theme; do not redefine brand variables inside sections.

## 4. Tokens and contrast

Use the theme's verified `--lx-*` values and plan-declared object radius
tokens. `--lx-text-muted` is the secondary text pairing; opacity on primary
text is not a substitute for a contrast-checked color. A7 owns contrast.
N2 owns surfaces and its exhaustive exceptions. N7 owns effects; no accent
glow is allowed under the name of a neutral shadow.

An inline reference to a theme token is valid, as is an approved image focal
point. Do not use inline styles to rebuild layout already covered by
utilities. A page-level token override belongs in `theme_css` and must
still satisfy the house requirements and binding rules.

## 5. Island styling

Discover `parts` and `css_vars` from `lexsis_design.island_schema` for the
selected component. Prefer its supported CSS variables for geometry; use
scoped part selectors for visual properties. Do not assume another island
has the same parts. Do not target implementation classes or override an
island's internal layout with `display`, positioning or a new grid.

After the live schema confirms the part, a visual override can be:

```css
#buy-box [data-part="cta"] { border-radius: var(--r-control); }
```

A saved preset label is visual intent, not frozen configuration. Resolve the
actual props and styling now; record the result and any intentional departure
in the workspace. Do not paste a static per-island prop or hydration table.

## 6. Responsive and accessible implementation

Follow A3/A4/A7/A11 for type, measure, contrast and interaction sizing.
A11's 48px minimum governs every authored tap target; external 24px or 44px
floors do not reduce it. Review at the workflow's specified widths, including
390px and 1280px for hosted design approval. Use native scrolling rather than
clipping content or intercepting input. Preserve visible keyboard focus.

## 7. Motion and repair

N10 owns the motion budget. `references/animation-system.md` owns managed
motion syntax and runtime APIs. A shared renderer animation is not permission
to deploy a banned effect. Static content remains visible when motion fails.

When styling fails: check source syntax, the compiler's missing utilities,
selector scope, live schema parts and CSS variables, then cascade order.
Fix the owning layer rather than escalating specificity or patching compiled
output. Recompile the exact inputs and inspect the hosted result.

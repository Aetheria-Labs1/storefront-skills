<!-- GENERATED from skills/ by scripts/build-distributions.py — DO NOT EDIT.
     storefront-skills v7.9.0 · 12 skills · 47 active islands -->

# Lexsis Storefront Skills — Knowledge Base

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

# Skill: analyze-page

> Analyze a URL, screenshot, or ad into a safe storefront brief. Use for inspiration, message-match, or existing-page diagnosis; this skill does not generate page source.

# Analyze a Page or Creative

Choose one mode:

- **Inspiration:** extract reusable layout and interaction patterns.
- **Own-page review:** identify design and conversion weaknesses.
- **Message-match:** compare an ad or screenshot with the intended landing
  page.

Generic URL or screenshot analysis can use the host browser without Lexsis and
reports `MCP status: not-required`. Any request that reads a Lexsis campaign,
catalogue, page, asset, or stored analysis requires the normal MCP preflight.
Use the exact actions required by the evidence:
`lexsis_campaigns.creatives`, `lexsis_campaigns.analyze`,
`lexsis_campaigns.frames`, `lexsis_catalog.list`, `lexsis_catalog.get`,
`lexsis_pages.get`, `lexsis_pages.inspect`, `lexsis_pages.source`, and
`lexsis_assets.view`. Resolve an unfamiliar schema with exact
`router` + `action` discovery. An empty discovery match does not make the
domain router unavailable. Report an actual failed live call and do not
replace missing evidence with assumptions.

## Capture

When a URL is available, use the host browser capability to inspect desktop
and mobile views, headings, sections, CTAs, media, and interactions. If browser
access is unavailable, use supplied screenshots and state what could not be
verified.

For ads, use `lexsis_campaigns` analysis actions when available.

## Analyze

Record:

- page type and audience
- section order and visual rhythm
- desktop/mobile behavior
- CTA and trust placement
- useful interaction patterns and candidate Lexsis islands
- message-match strengths or gaps
- accessibility or usability issues visible in the evidence

Do not use unsupported benchmark percentages or generic lift claims.

## Brand Safety

Carry forward structure and design intent only. Exclude competitor copy,
logos, product imagery, pricing, claims, reviews, testimonials, and protected
brand elements.

## Return

Return `PAGE_ANALYSIS`:

```text
Mode: [inspiration | own-page | message-match]
Source: [...]
Page type: [...]
Reusable structure: [...]
Responsive behavior: [...]
Conversion observations: [...]
Candidate islands: [...]
Avoid copying: [...]
Evidence limits: [...]
```

Include MCP status, discovered capabilities, actions, fallbacks, and blockers
when Lexsis was used. This can inform `/plan-page` for a new page or
`/optimize` for an existing one.

---

# Skill: asset-prep

> Independently search, generate, import, or replace storefront media. Works from an asset brief or an existing page workspace and is not a required page-generation stage.

# Prepare Assets

Use this skill for asset-only work. It does not require `/plan-page` or
`/design-page`, and other skills must not invoke it automatically.

Use `lexsis_asset_library.search`, `lexsis_catalog.list`,
`lexsis_catalog.get`, `lexsis_workspace.credits`,
`lexsis_drafts.asset_generate`, `lexsis_asset_import.import`,
`lexsis_asset_upload.upload`, and
`lexsis_assets.view`.

Import requires exactly one source: `url`, image `data` + `mime_type`, or
`attachments`. It never opens the upload UI. Use `lexsis_asset_upload.upload`
with the selected `workspace_id` and `theme_id` for local-file uploads, and
wait for the user's uploaded-asset message before using the result. If the
host has no inline UI, ask for a URL or conversation attachment and import
that source instead; never call import with no source.

## Choose a Mode

### Standalone

Accept an asset brief containing the brand/store, roles, dimensions, crops,
style, and intended use. Search, generate, import, and verify the requested
media. Save results under `work/storefront-assets/<brief-name>/asset-manifest.json`.

### Existing Page

Read the page source and compact manifest. Work only on the requested missing,
placeholder, or replacement roles. Do not redesign unrelated sections.

## Source Order

For each role:

1. Ask whether the user wants to pick from the library first
   (`lexsis_asset_library.search` with `query: ""`, the `theme_id`, and
   `mode: "tags"` for a category such as `banner` or `logo`; wait for the
   `Design asset selection:` message). Otherwise search existing Lexsis assets.
2. Use real Shopify product media for product identity.
3. Ask before spending generation credits.
4. Prefer Lexsis generation. If another image-generation tool is available,
   offer it as an explicit provider choice.
5. Import external-tool results into Lexsis.
6. Inspect the final asset and verify identity-sensitive imagery.

Use supported icons, SVG, or CSS for ordinary interface icons. Do not generate
raster UI icons unless the brief explicitly requires custom artwork.

## Page Updates

When working on a page:

- replace the asset in `lexsis-source.html`
- store only the final binding in `page-manifest.json`
- recompile once after all requested assets are updated
- set `design.status` to `changes-pending-approval` for visible changes

Do not create a second HTML source or local preview. Page source must use
permanent Lexsis or Shopify media.

## Asset Record

Keep the machine record compact:

```json
{
  "role": "hero",
  "sectionId": "hero",
  "sourceType": "lexsis",
  "assetId": "...",
  "url": "https://...",
  "status": "verified"
}
```

Shopify media uses `productId` and `mediaId`. Put crop guidance, alt-text
intent, prompt history, and creative reasoning in the brief or plan, not the
page manifest.

## Return

Return the final asset paths or bindings, provider used, verification result,
and any unresolved roles.

---

# Skill: build

> Create the fastest useful unpublished Lexsis storefront draft from a prompt, optional template URL, or automatically selected page kit. Use for first versions and rapid iteration; use generate for production-ready QA.

# Build a Fast Draft

Create an unpublished draft without requiring the full planning and visual
approval workflow.

Read:

- `references/fast-build.md`
- `references/page-types/_index.md`, then only the matching
  `references/page-types/<type>.md` and its `## Workflow`
- `references/workflows/section-asset-workflow.md` and
  `references/workflows/island-selection-workflow.md`
- `references/authoring/css-and-styling.md` and
  `references/authoring/source-authoring.md`
- `references/assets/generation-policy.md` and
  `references/proof/reviews-sourcing.md`
- `references/animation-system.md` when the request names custom motion
- `references/consumer-behavior-cro.md`
- `references/workflow-intent.md`

Use `lexsis_catalog.list`, `lexsis_catalog.get`,
`lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`,
`lexsis_template_library.get_kit`, `lexsis_design.get_section`,
`lexsis_design.islands`, `lexsis_design.island_schema`,
`lexsis_asset_library.search`, `lexsis_brand.context`,
`lexsis_brand.get_theme`, `lexsis_pages.compile`, and
`lexsis_page_create.create`.

Use `lexsis_workspace.credits`, `lexsis_assets.capabilities`,
`lexsis_assets.view`, and `lexsis_drafts.asset_generate` only when existing
media cannot satisfy a required production slot. Confirm before paid
generation unless the user already explicitly authorized it.

Infer the complete request:

- A supplied template or page-kit URL is authoritative.
- Without a template, select the best coherent page kit for `fast-draft`
  intent.
- If the user asks to choose among templates, show the picker and wait.
- If the user asks for a visual mockup before source, route to
  `/design-page`'s concept-first path instead.
- If the user asks to publish live, route to `/publish`; this skill creates
  with `publish:false` only.

Build the page around real imagery, not around colour and copy. Identify the
page type first, then per section decide the media before the copy: catalog
media, then the asset library, then merchant-owned sources. Open every
candidate with `lexsis_assets.view` and run the fit review in
`references/workflows/section-asset-workflow.md` before using it, viewing a
section's set together so it reads as one shoot, so the kit's sample imagery is replaced with viewed catalog or library assets. When a slot
cannot be filled, leave it `planned` and name it in the draft summary so the
merchant can upload the file or authorise generation; never spend generation
credits without that yes, and never substitute a colour band, an emoji row or
icon tiles for a missing image. Resolve islands live through
`lexsis_design.islands` and `lexsis_design.island_schema`.

Follow `references/fast-build.md`. Compile once, permit one targeted repair,
create the draft, and return `DRAFT_CREATED` immediately. Do not run design
critique, hosted QA, commerce QA, hash reconciliation, or full workspace
validation before returning the preview.

---

# Skill: build-with-template

> Create an unpublished Lexsis storefront draft directly from a supplied page-kit or section-template URL. Use when the template is already chosen and visual design approval should be skipped.

# Build with a Chosen Template

Require a page-kit or section-template URL, slug, or id. If none is supplied,
ask for it or route a general fast-build request to `/build`.

Read:

- `references/fast-build.md`
- `references/page-types/_index.md`, then only the matching
  `references/page-types/<type>.md` and its `## Workflow`
- `references/workflows/section-asset-workflow.md` and
  `references/workflows/island-selection-workflow.md`
- `references/authoring/css-and-styling.md` and
  `references/authoring/source-authoring.md`
- `references/assets/generation-policy.md` and
  `references/proof/reviews-sourcing.md`
- `references/animation-system.md` when the template contains custom motion
- `references/consumer-behavior-cro.md`
- `references/workflow-intent.md`

Use `lexsis_template_library.get_kit`, `lexsis_design.get_section`,
`lexsis_catalog.get`, `lexsis_design.islands`,
`lexsis_design.island_schema`, `lexsis_asset_library.search`,
`lexsis_brand.context`, `lexsis_brand.get_theme`,
`lexsis_pages.compile`, and `lexsis_page_create.create`.

Use `lexsis_workspace.credits`, `lexsis_assets.capabilities`,
`lexsis_assets.view`, and `lexsis_drafts.asset_generate` only for required
production gaps and only after credit authorization.

Build the page around real imagery, not around colour and copy. Identify the
page type first, then per section decide the media before the copy: catalog
media, then the asset library, then merchant-owned sources. Open every
candidate with `lexsis_assets.view` and run the fit review in
`references/workflows/section-asset-workflow.md` before using it, viewing a
section's set together so it reads as one shoot, so the template's sample
imagery is replaced with viewed catalog or library assets. When a slot cannot
be filled, leave it `planned` and name it in the draft summary so the merchant
can upload the file or authorise generation; never spend generation credits
without that yes, and never substitute a colour band, an emoji row or icon
tiles for a missing image. Re-check the template's island props against the
current schema through `lexsis_design.island_schema` rather than trusting them.

Treat the supplied template direction as authoritative. Follow
`references/fast-build.md`, skip the visual-concept and design-approval stages,
compile once with at most one targeted repair, create with `publish:false`, and
return `DRAFT_CREATED`.

This skill never publishes live and never upgrades the result to
`DRAFT_READY`; use `/generate` and `/publish` for those outcomes.

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

> Turn an approved one-page storefront plan into canonical Lexsis source and an unpublished hosted draft, confirming any asset slots the plan left unresolved.

# Design the Page

Create the real page source, compile it, and create one unpublished hosted
draft for review. Never publish.

Read:

- `references/design-rules.md`
- the plan's `references/page-types/<type>.md` (its `## Workflow` names the
  island and asset decision per section) and
  `references/page-types/_checklist-format.md` for the vocabulary
- `references/workflows/island-selection-workflow.md` (variant and prop
  decision tables per island) and
  `references/workflows/section-asset-workflow.md`
- `references/authoring/css-and-styling.md` and
  `references/authoring/source-authoring.md` before writing any class or
  section CSS
- `references/mcp-playbooks/tool-sequence-by-stage.md` (Stage 2) and the
  matching row of `references/mcp-playbooks/tool-sequence-by-page-type.md`
- `references/animation-system.md` when the plan names a motion moment
- `references/consumer-behavior-cro.md`
- `references/island-presets.md`
- `references/merchant-templates.md`
- `references/workflow-intent.md`
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

Use `lexsis_brand.context`, `lexsis_brand.get_theme`,
`lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`, `lexsis_design.guide`,
`lexsis_design.islands`, `lexsis_design.island_schema`,
`lexsis_design.get_section`, `lexsis_template_library.get_kit`,
`lexsis_asset_library.search`, `lexsis_catalog.get`, `lexsis_catalog.reviews`,
`lexsis_catalog.review_collection_items`, `lexsis_brand.navigation` (full-nav
types only), `lexsis_assets.capabilities`, `lexsis_assets.view`,
`lexsis_workspace.credits`,
`lexsis_drafts.asset_generate`, `lexsis_asset_import.import`,
`lexsis_asset_upload.upload`, and
`lexsis_pages.compile`, and `lexsis_page_create.create`.

When the user wants one of their saved reusable sections, use
`lexsis_template_library.list_mine` and `get_mine`. Treat its source as a
starting section in the page, not as an inherited renderer shell.
Resolve only unfamiliar argument schemas through exact router/action
discovery.

## Inputs

Use the approved `page-plan.md` and its saved workspace, store and theme
binding, inside the campaign folder the plan opened
(`work/campaigns/<campaign-slug>/pages/<page-handle>/`). Campaign-level media
in `../../assets/` is available to every page of the campaign; page-only media
stays in the page's own `assets/`. The plan
defines strategy, the Design direction, the Imagery and background plan, the
asset slots and section intent; it must not define islands or implementation
details.

Implement the plan's Consumer decision model without adding generic CRO
modules. Preserve its visitor mode, top decision questions, selected patterns,
gallery jobs, merchandising relationship, risk treatment, mobile context, and
metric. Reopen a decision only when live catalog, asset, or policy evidence
contradicts the plan.

If the user explicitly skips `/plan-page`, write a short one-page plan with
the same blocks (including the Page type block, Proof ledger and, when an
offer exists, the Offer ledger) and record the skip. Never run `/setup` or
`/plan-page` automatically.

## Page-Type Workflow

Before any template fetch or HTML, read `page.pageType` from the manifest and
the matching `references/page-types/<type>.md`. Its `## Workflow` already
names, per section, the media decision and the island decision the plan made
from the context reads; your job is to execute them. Run
`python3 <plan-page-skill>/scripts/plan_lint.py <page-workspace>` and read
its WARN rows together with the plan's "Deviations from the type default":
a deviation the plan explains is a decision, a deviation it does not mention
is a question for the plan owner. A review section with no review data or
urgency with no verified basis is the one case to stop and ask.

For each section, in order:

1. **Media first.** Resolve the section's slots exactly as the plan decided
   (catalog media, library asset, imported file, or an ALLOW-purpose
   generation). If a slot is still empty at this point, follow
   `references/workflows/section-asset-workflow.md`: one more library search
   with the right tag, then decide whether an allowed generation purpose
   fits, then put one question to the merchant that names what is missing
   (section, job, aspect, count) and offers upload through
   `lexsis_asset_import.import` or MCP generation when feasible (the credit
   confirmation and any ASK approval travel in that same answer). Skip or
   merge the section only when the merchant chooses. Never ship the
   section as a colour band, an emoji row, icon tiles or copy alone, and
   never leave a missing asset unreported.
2. **Island second.** Take the plan's island decision, call
   `lexsis_design.island_schema` for that island only, and pick the variant
   and props from what the live schema offers using the plan's decision
   inputs (image count for gallery layout and thumbnails, variant axes for
   swatches vs buttons, review band for carousel vs list, page length for a
   sticky bar), as `references/workflows/island-selection-workflow.md`
   describes. Record the chosen variant and the inputs in `islands[]`.
3. **Copy third.** Short, in the plan's framework, no emoji, no filler.

Carry these type defaults into composition:

- **Above the fold (390px).** Build the type's first screen exactly as listed;
  nothing else enters it.
- **CTA.** Count, first position, sticky behaviour and copy pattern from the
  checklist `cta` block. Every CTA on a single-goal type performs the same
  action.
- **Nav.** `none` means logo only, not a link; `minimal` means logo plus one
  utility link; `full` means the store navigation from `lexsis_brand.navigation`.
- **Price.** `price_above_fold` is obeyed at 390 and 1280.
- **Proof density.** Module count inside the checklist range; kinds only from
  the ledger.

## Infer the Design Mode

Use `references/workflow-intent.md` and the manifest evidence. A correction in
the current request overrides the saved mode.

- `fast-draft`: make reasonable reversible choices, compile a coherent page,
  create the unpublished draft, and expose the hosted preview immediately.
  Deeper critique is follow-up work.
- `production-ready`: create the hosted draft first, then run the hosted
  Design Review before marking the design approved.

An explicit `/design-page` request authorizes one page-creation credit for the
named page. It does not authorize paid asset generation, a duplicate page, or
publishing. Ask immediately before spending asset-generation credits when
existing library, catalog, or imported assets cannot satisfy the page.

If optional design, preset, or merchant-template guidance is unavailable, warn
once and continue from the page plan, saved brand, live schemas, and compiler.
Missing canonical source-format or compile-contract inputs remain blocking.

## Choose the Visual Route

Infer this from the request rather than always presenting a gate:

- Use the concept-first path when the user asks for a mockup, wants to approve
  the appearance before implementation, or explicitly chooses visual
  exploration.
- Continue directly to source for fast-draft, template-first, and
  build-the-page requests.
- If the user genuinely has not indicated whether they want visual approval,
  offer two choices in one line: generate a mobile-first concept, or continue
  directly to the hosted draft.
- A supplied template URL plus a request for the fastest draft should route to
  `/build` or `/build-with-template`, not through this skill.

For concept-first work, follow `references/design-concepts.md`. Use the
existing Lexsis image generator, show mobile first, and return
`CONCEPT_READY`. Generate the desktop adaptation after the mobile direction is
approved unless the user requested both together. The concept is design
evidence only: keep it out of production `assets[]` and never use its URL in
page source.

After concept approval, derive the real production asset gaps, confirm any
remaining paid generation batch, resolve those slots, and continue with the
ordinary Design Direction, Compose, Compile, Hosted Draft, and Approval stages.

## Design Direction Gate

Before writing any HTML, read the "Design direction" block in `page-plan.md`
and `references/design-rules.md`. If the plan has no design
direction, write one now (palette of four to six named hex values, type roles
and scale, layout concept, wireframe with slot ids, icon decision, the one
bold moment) and record it in the plan before continuing.

Precedence, in order: house rules (`design-rules.md`) > merchant-stated brand
rules (`voice_md`, owner notes) > brand-kit token values > generated design.md
guidance > brand-kit preview blueprint and presets. A lower layer may narrow a
higher one, never widen it. Token values win over prose for values; if a token
value fails WCAG AA against its documented pairing, return
`THEME_CONTEXT_CONFLICT` with both values. Style guidance never raises a
conflict; it is overridden and recorded in `page-plan.md` under "Overrides of
brand design.md".

## Asset Gap Confirmation

The plan already resolved the asset slots. Read `assets[]` from the manifest:

1. Slots with `status: verified`, including everything the user picked in
   the plan, are final; use their ids and URLs as-is.
2. List only `planned` slots. `validate_page_workspace.py --phase design`
   reports them as `asset_slot_unresolved` warnings.
3. In `fast-draft`, resolve them from the existing library or Shopify media
   using the plan and brand direction. Ask only before paid generation or when
   the unresolved choice would materially change the campaign. In
   `production-ready`, ask once whether to generate or pick existing media.
4. Import externally generated media into Lexsis before production use. View
   every asset with `lexsis_assets.view` before it enters the source and run
   the fit review in `references/workflows/section-asset-workflow.md` against
   the section it belongs to: subject, crop at the slot aspect, a quiet area
   where the headline and body sit, consistency with the neighbouring slots,
   palette, no baked-in text or watermark. Never place an asset on the page
   from its filename, tag or search rank alone. Then set `status: verified` on
   each resolved slot.

Use Lexsis icons, supported SVG, or CSS for ordinary interface icons. When the
plan's Icons decision names a set to generate, generate one monochrome SVG set
(one stroke, one size) and import it. Never fall back to emoji as icons; emoji
appear only where the plan's "Emoji in copy" line allows them, inside running
text.

Generation obeys `references/assets/generation-policy.md`. ALLOW purposes
(`hero_bg`, `section_bg`, `card_bg`, `texture_fill`, `pattern_tile`,
`decorative_element`, `product_composite` over a real cut-out) may be
generated after confirmation; `icon_set` is a plan role meaning "author one
monochrome inline SVG set", never a raster generation. ASK purposes need the merchant's
explicit yes for that slot. NEVER purposes are not generated under any
instruction short of the merchant supplying the media themselves: the
product itself when Shopify media exists or could exist, a person presented
as a customer, reviewer, creator or staff, before/after or result imagery,
press logos, badges, certifications or awards, text or prices inside images,
and competitor products. A slot whose job is on the NEVER list stays
`planned` and the section is built without it or removed with a note.

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
3. Convert each planned section into responsive layout and copy, following the
   wireframe, the Imagery and background plan, and the slot ids.
   Header, Announcement, Navigation, and Footer are included here in their
   intended source order when required.
4. Read the compact island catalog and select only the likely interactive
   components. Do not fetch every full schema in advance.
   When the plan names a preset (`Preset: <island>/<intent>-<tone>`), apply it
   from `references/island-presets.md` verbatim: props,
   `hydrate`, and its scoped CSS. Check its `requires` first. Unknown id:
   return `PRESET_NOT_FOUND`. Any deviation is recorded as
   `islands[].presetOverrides`; never edit a preset in place for one page.
5. Proof renders only from the plan's Proof ledger
   (`references/proof/proof-ledger.md`). Review islands use the ledger's
   `collectionId` or `productIds`, `minRating`, `pageSize` of 12 or fewer.
   Omit `reviewsEndpoint`; the page supplies it at runtime. `averageRating`
   and `totalReviews` only from the `lexsis_catalog.reviews` total. `none`
   means no review island. Never `SocialProofPopup`, never a live viewer or
   purchase count. Star glyphs appear only next to a real average and count.
   Every press logo is an `<a>` to the ledger's article URL, monochrome, one
   height; a logo with no URL is not rendered. Badges and certifications
   carry the ledger's issuer text. Quotes are verbatim with the ledger's
   attribution. Every numeral in a proof section appears in the ledger.
6. Offers render from the Offer ledger following
   `references/offers/price-presentation.md`: current price first, compare-at
   struck through only with a recorded basis and a `data-source` attribute
   naming it, savings in the merchant's currency, unit or per-day price only when accurate, shipping and tax
   language from the store. Countdown and stock islands are bound to the
   ledger's confirmed end date or live inventory, never a fixed number or a
   timer that resets. Nothing in `references/anti-patterns/dark-patterns.md`
   ships: no pre-selected paid add-ons, no confirmshaming dismiss copy, no
   hidden recurring terms, no fake urgency.
7. Write a rough but complete `lexsis-source.html` with stable section
   delimiters from the canonical vocabulary, minimal island props, and the
   documented examples as a starting point.
8. Write copy as design content using the plan's framework
   (`references/copy/copy-frameworks.md`) and
   `references/copy/headline-and-cta-rules.md`: sentence case, the CTA names
   the action and outcome, the first sentence of every FAQ answer answers,
   and no word or structure from
   `references/anti-patterns/copy-anti-patterns.md`. For ad-driven traffic,
   the hero headline and visual satisfy `references/copy/message-match.md`.
9. Write global page rules to `page-theme.css`; keep section-specific CSS
   beside its section. `references/authoring/css-and-styling.md` decides which
   layer a rule belongs to: tokens and the radius and type scales in theme CSS,
   all layout in utilities, and section CSS only for a scoped component's
   geometry, an island's `data-part` hooks, one scoped keyframe, or a fallback.
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
    slot's aspect, minimum resolution, descriptive alt text (empty alt for
    decorative), `loading="lazy"` below the fold and the hero preloaded;
    video is click-to-play or muted loop with a poster and captions
    (`references/assets/video-rules.md`).

## Parallel Section Generation

If the runtime can spawn sub-agents, each may write one section's markup and
scoped CSS from its plan line, wireframe box, slot ids and preset. The parent
assembles `lexsis-source.html` in plan order, owns `page-theme.css`, compiles
once, and creates the draft. Sub-agents never compile, never edit shared CSS,
and never spend credits. Without sub-agents, write the sections sequentially.

## Compile and Create the Draft

Compile the rough complete source, CSS, head, scripts, and bindings early. The
compiler is the authoritative compatibility check.

1. Use `validation_errors` as the work list.
2. Fetch a full island schema only for an island named by an error or when a
   required behavior remains unclear.
3. Fix the source while preserving the planned composition.
4. Recompile until blocking errors are clear.
5. Save the exact clean response and input hashes in `compile-artifact.json`.

Create with the exact clean compile ID and current source fields using
`lexsis_page_create.create` with `publish:false`. Record page ID, version,
preview URL, local hashes, compile bundle hash, `status: draft_created`,
`design.status: pending-approval`, and `qa.status: pending`.

If the compile ID expires, recompile the same unchanged inputs once. If the
manifest already contains a page ID, do not spend another creation credit:
fetch its current version and edit that draft through `/generate`.

Return the hosted preview immediately as `DRAFT_CREATED`. A failed later
review never erases or conceals the working draft.

## Hosted Design Review

Required for `production-ready` and whenever the user asks to approve the
design. It is optional follow-up for `fast-draft`.

Use the hosted preview at 390px and 1280px. Run
`python3 <design-page-skill>/scripts/design_lint.py <page-workspace>` and then
check real renderer output for fonts, media, hydration, overflow, clipping,
hierarchy, and usable responsive layout. Tablet and full commerce QA remain
owned by `/generate`.

Look at both hosted screenshots and answer each question in one line:
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
   - Does every proof element on screen trace to a Proof ledger row (open the
     press links, count the stars against the ledger total)?
   - Is any item from `references/anti-patterns/mobile-anti-patterns.md`
     visible: stacked sticky bars over 15% of the viewport, hover-only
     controls, text under 16px, side-by-side buttons under 48px?

Write results to `qa-report.md` when review is attempted. Fix local source,
compile once, update the existing draft with expected-version protection, and
rerun only failed checks. Never create a replacement draft for a visual fix.

If browser automation is unavailable, return the hosted preview URL with
`DRAFT_CREATED` and state that hosted design QA remains pending. Never mark
design approval or hydration as passed without hosted evidence.

## Approval

Show:

```text
Hosted preview: [url]
Draft: [page id] version [version]
Page type: [type] · deviations [none | list]
Hosted review: [not requested | pending | passed]
Sections: [ordered list]
Interactive components: [islands]
Presets: [ids]
Proof rendered: [n ledger rows] · dropped: [rows and why]
Offer rendered: [terms | none]
Reused assets: [slots]
Generated assets: [slots with purposes]
Unresolved assets: [slots, incl. blocked by generation policy]
Copy lint: [passed | findings]
Concept: [not requested | asset ids and approval]
```

On approval, set `design.status: approved`. Record only final IDs, compact
island schema evidence, presets and overrides, and source, theme,
configuration, structure, and bundle hashes in the manifest. Do not store
creative explanations or tool transcripts there.

Any later visible source, CSS, copy, layout, island, or asset change returns
the design to `changes-pending-approval`.

## Return

Return the source, theme, compile-artifact path, page ID, version, hosted
preview URL, sections, selected islands and presets, asset summary, and
`DRAFT_CREATED`. After explicit hosted approval, return `DESIGN_APPROVED`.

### design-page reference: page-layout

# Page Layout

The design stage approves hierarchy, section proportions, image placement,
typography, color balance, desktop composition, mobile stacking, CTA
placement, and island presentation.

Write:

- `lexsis-source.html` — the canonical readable page source
- `page-theme.css` — global theme tokens and page-wide custom CSS
- `compile-artifact.json` — exact compile response and input hashes

Use ordinary HTML for static content and active Lexsis islands for useful
interactions. A supporting composition image may guide art direction, but it
must never become the page.

Start from the selected page kit or section templates. Use the selected
theme's `--lx-*` tokens and Tailwind utilities rather than rebuilding the
brand system inside each section. Record one coherent style treatment in the
manifest.

Search existing store and product assets first, show one combined asset
summary, and ask once before generating missing or optional media. Every asset
used in source must have a permanent Lexsis or Shopify URL.

Create the unpublished hosted draft after a clean compile. Review that hosted
draft at 390px and 1280px. `/generate` owns tablet and full commerce QA.

Approval hashes the exact source, page theme, head, scripts, structure, and
compiled bundle. `/generate` promotes this source instead of recreating it.

---

# Skill: generate

> Create an unpublished Lexsis storefront draft early, then synchronize and QA it to production readiness when the user's intent calls for deeper verification.

# Generate the Draft

Create a remote draft from canonical local source. Draft creation is
reversible; publishing remains a separate explicit action.

Read:

- `references/workflow-intent.md`
- `references/source-and-sync.md`
- `references/animation-system.md` when source contains or requires motion
- `references/consumer-behavior-cro.md` when planning or design was skipped
- `references/page-editing.md` only for an existing page
- `references/merchant-templates.md` only when reusing a merchant template
- `references/qa-recipe.md` for production-ready QA
- `references/authoring/css-and-styling.md` and
  `references/authoring/source-authoring.md` when repairing source
- the plan's `references/page-types/<type>.md` and
  `references/proof/proof-ledger.md` for the production gate
- `references/anti-patterns/copy-anti-patterns.md`,
  `references/anti-patterns/dark-patterns.md` and
  `references/anti-patterns/mobile-anti-patterns.md` for hosted QA

Use `lexsis_catalog.get`, `lexsis_design.island_schema`,
`lexsis_pages.compile`, `lexsis_pages.edit_context`,
`lexsis_pages.source`, `lexsis_pages.integrity`, and
`lexsis_page_create.create`.

## Infer the Outcome

Infer intent from the whole request and conversation using
`references/workflow-intent.md`; do not require a trigger phrase.

- `fast-draft` is the default for reversible ambiguity and requests to create,
  try, preview, explore, or iterate.
- `production-ready` applies when the user asks for final polish, exhaustive
  QA, campaign handoff, or launch preparation.
- `publish` routes to `/publish`; this skill never infers live-release
  approval.

State the inferred mode briefly and record compact evidence in `workflow`.
A request to create a draft authorizes one page-creation credit for the named
page. Intent inference never authorizes a duplicate page, paid asset
generation, publication, deletion, or destructive replacement.

## Inputs and Setup Reuse

Use `lexsis-source.html`, `page-theme.css`, and the compact schema-v3 manifest
from the page workspace inside its campaign folder. Reuse the workspace, store
and theme binding recorded in the manifest and `campaign.json`, resolved
through `work/storefront/setup/setup.json`. Do not call setup again when that
binding is valid, and never switch workspace, store or theme for an existing
page.

Refresh only volatile creation data: selected products and variants, prices,
availability, permissions, active island schemas, and an existing page's
version. Never preserve a stale hardcoded Shopify variant ID when current
catalog data or a dynamic product binding can resolve it.

If `/plan-page` or `/design-page` was intentionally skipped, create the minimum
missing local artifact, record the skip, and continue. Use
`references/consumer-behavior-cro.md` to record a minimum visitor mode, top
decision questions, at most two relevant patterns, gallery gaps, and primary
metric. Do not claim design approval that did not happen.

## Draft-Creation Gate

Before the first remote draft, require only:

- a valid saved store/theme binding and draft-write permission
- non-empty canonical source, theme CSS, title, and page handle
- current product/variant bindings with no known invalid hardcoded variant
- permanent assets rather than local URLs
- custom fonts backed by full HTTPS stylesheet URLs in `head.fonts`, or an
  intentional system-font stack
- a clean compiler result

Do not block first draft creation on critique screenshots, exhaustive hashes,
hosted responsive QA, commerce QA, or a `DRAFT_READY` validator result.

Optional design or QA guidance that cannot be read produces one warning and
does not block the draft. Missing source-format, manifest, or compile-contract
inputs remain blocking.

## Compile from the Workspace

Prepare exact tool inputs with the bundled adapter:

```bash
python3 <generate-skill>/scripts/prepare_workspace_compile.py \
  <page-workspace> \
  --output <page-workspace>/compile-request.json
```

Use the adapter's `compile` object as the exact arguments to
`lexsis_pages.compile`. Use summary mode; do not request or echo the full
compiled bundle merely to inspect it.

If `remote.pageId`, `remote.lastKnownVersion`, and `remote.previewUrl` already
exist, fetch the current edit context and reuse that draft. Do not call
`lexsis_page_create.create` again. Compile only when local inputs changed, then
patch the existing draft with expected-version protection.

When no remote draft exists, compile once from the current files. Immediately
pass the returned `compile_id` and the adapter's `create` fields to
`lexsis_page_create.create` with `publish:false`.

If a compile ID expires before creation, recompile the same verified inputs
once. If the client cannot reuse the ID, create with the exact source, head,
theme CSS, and scripts from the adapter. Expiry is not a reason to repeat
planning, critique, asset search, or approval.

## Return or Reuse the Reversible Draft

As soon as creation succeeds, or after an existing draft is confirmed current:

1. Record page ID, version, preview URL, local hashes, and compile bundle hash.
2. Set manifest `status` to `draft_created` and QA to `pending`.
3. Run the validator with `--phase draft-created`.
4. Surface the preview immediately as `DRAFT_CREATED`.

Do not delete, replace, or conceal a working draft because later QA finds an
issue.

## Production-Ready Follow-Through

After the preview exists, continue best-effort verification unless the user
asked to stop at a first draft.

For `production-ready`, or when upgrading an existing `DRAFT_CREATED`:

1. Fetch persisted source, bundle, and version evidence.
2. Reject remote/local hash drift and repair the draft from current local
   source.
3. Review the page's imagery as one campaign, not merely as individually valid
   assets.
4. Run hosted QA at 390px, 768px, and 1280px.
5. Verify typography, media, hydration, overflow, responsive geometry,
   expected Shopify variant, cart opening, quantity, subtotal, Quick Add,
   product-grid stability, thumbnails, and authored header/footer order.
6. Run `python3 <plan-page-skill>/scripts/plan_lint.py <page-workspace>` and
   `python3 <design-page-skill>/scripts/design_lint.py <page-workspace>`.
   Proof and offer findings (a proof element outside the Proof ledger, an
   offer element outside the Offer ledger, a dark-pattern hit) block; type
   deviations and copy findings are review notes unless the plan did not
   record them. Check the 390px first screen against the type file's
   "Above the fold" list and every numeral in proof sections against the
   ledger.
7. Write evidence and blockers to `qa-report.md`.
8. Set `status: qa_passed` only when all blocking checks pass, then run the
   validator with `--phase draft` and live remote hashes.

Return `DRAFT_READY` only after synchronization and every blocking QA check
passes. Otherwise return the existing `DRAFT_CREATED` with specific blockers
and the next repair action.

## Later Edits

Fetch edit context and stop on unexpected version drift. Change local source
first, compile changed inputs once, patch only changed sections with
`expected_version`, and update synchronization state only after success.

## Return

Always return the working directory, source path, page ID, version, preview
URL, inferred intent mode, and current state: `DRAFT_CREATED` or
`DRAFT_READY`. Include the QA report when QA was attempted.

### generate reference: source-and-sync

# Production Source and Synchronization

`lexsis-source.html` and `page-theme.css` are the editable source of truth.
`compile-artifact.json` is generated. The hosted draft is the only interactive
preview.

Headers, announcement bars, navigation, and footers live in
`lexsis-source.html` like every other section. Portable bundles preserve that
exact section order and contain no renderer-level `shell` or
`navigation_profile`.

Use `scripts/migrate_page_workspace_v3.py <working-directory>` for legacy
manifests.

## Compile Reuse

Compare the current source, theme CSS, configuration, structure, and bundle
hashes with `compile-artifact.json`.

- Matching inputs: reuse the compile artifact.
- Any changed or missing input: compile once and replace the artifact.
- Never recompile solely because `/generate` began in a new conversation.

## Creation

Draft creation and production readiness are separate states.

1. Inspect `remote.pageId`, version, and preview URL.
2. If they exist, fetch edit context and reuse that draft; never create a
   duplicate page merely because another skill or conversation began.
3. Validate the compact manifest and canonical source with the
   `draft-created` gate.
4. Refresh only volatile products, variants, prices, permissions, and remote
   version data.
5. Compile the current workspace inputs once when no matching clean artifact
   exists.
6. Create with `publish: false` only when no remote draft exists; otherwise
   patch changed sections with expected-version protection.
7. Save page ID, version, preview URL, compile hash, and `status:
   draft_created`.
8. Return `DRAFT_CREATED` immediately.
9. Fetch persisted source and remote hashes, then run hosted QA.
10. Save synchronized state and `status: qa_passed` only when every
   production-ready check succeeds.

A failed post-creation check does not erase or invalidate the reversible
draft. Report the draft and its blockers.

## Intent Evidence

Record the inferred mode compactly in `workflow`:

```json
{
  "intentMode": "fast-draft",
  "intentConfidence": "high",
  "intentSignals": ["requested a preview", "delegated specifics"],
  "userOverride": false
}
```

Intent evidence explains routing; it never grants publish or paid-generation
permission.

## Editing

1. Fetch and compare the remote version.
2. Change local source.
3. Compile only if inputs changed.
4. Compare section hashes.
5. Patch changed sections with `expected_version`.
6. Save returned version and hashes after success.

Remote content must never be the only copy of an intentional change.

When reusing a merchant template, apply it to the remote page only after the
same source has been inserted into the canonical local source. Record the new
remote version and hashes only after the apply succeeds.

---

# Skill: optimize

> Diagnose and improve an existing Lexsis storefront page for a specific business outcome. Starts with a focused optimization brief before making local-first section edits.

# Optimize a Page

Read:

- `references/evidence-led-cro.md`
- `references/consumer-behavior-cro.md`
- `references/authoring/css-and-styling.md` before any CSS or class change
- `references/animation-system.md` before adding or editing motion

Use the needed exact actions from
`lexsis_pages.edit_context`, `lexsis_pages.source`,
`lexsis_pages.section_source`, `lexsis_pages.compile`,
`lexsis_pages.integrity`, `lexsis_pages.diff`, `lexsis_analytics.page`,
`lexsis_analytics.timeseries`, `lexsis_analytics.attribution`,
`lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`,
`lexsis_drafts.page_update_section`, and `lexsis_drafts.page_patch`. Resolve
only unfamiliar schemas through exact router/action discovery. A zero-result
directory lookup does not make page or analytics data unavailable. If the
actual live read fails, state that limitation; generic CRO guidance is not a
substitute.

The full skill pack includes optional deeper design guidance at
`references/lexsis-design-capabilities.md`. Every edit obeys
the house rules in `references/design-rules.md`; an
optimization never adds emoji, gradients, hover transforms, or a section
background.

Start by confirming:

1. Target outcome: conversion, add-to-cart, AOV, bounce, trust, mobile UX,
   speed, or SEO.
2. Target page, audience, and traffic source.
3. Diagnosis only or permission to edit.
4. Copy, sections, SEO fields, or offers that must remain unchanged.

Do not edit until the objective and scope are clear.

Confirm the page's store/theme binding exists in
`work/storefront/setup/setup.json`. If it is missing, stop with
`Run /setup for this store and theme first.` Never run setup automatically.

## Use Relevant Guidance Only

Read only the matching section of `references/industry-cro.md`.

Use general guidance when no industry fits. Treat analytics and observed user
behavior as stronger evidence than generic patterns.

## Diagnose

1. Locate the page and read its analytics, structure, source, and current
   remote version.
2. Open its local page workspace. If missing, adopt the remote source into the
   standard local files before editing.
3. Compare the remote version with the manifest and stop on unexpected drift.
4. For a structural redesign, search relevant page kits and sections and
   compare them with the current structure. Do not force template comparison
   for copy-only, offer-only, metadata, or minor visual changes.
5. Classify proposed changes as keep, improve, replace, remove, or test.
6. Use the consumer-behavior framework to identify the visitor mode, top
   unanswered decision question, and the smallest relevant behavioral
   hypothesis. Analytics and observed behavior override generic guidance.
7. Present an optimization brief:

```text
Outcome:
Evidence:
Main friction:
Visitor mode:
Behavioral hypothesis:
Proposed sections:
Protected elements:
Expected measurement:
Experiment recommended: yes/no
```

Obtain approval before making material changes.

## Apply Approved Changes

Modify `lexsis-source.html` first. Validate and compile the complete local
source with `page-theme.css`, compare section hashes, and patch only changed
sections with `expected_version`. A visible source or CSS change requires a
new compiled preview and design approval before the remote patch. Update the
manifest only after the remote write succeeds. Then run `diff`, `integrity`,
responsive checks, and affected commerce checks.

Never make an intentional remote-only edit. Preserve the URL and SEO fields
unless the user approved changing them.

## Experiment Handoff

When the value of a change is uncertain and traffic supports measurement,
return a focused hypothesis for `/ab-test` instead of presenting the change
as proven.

## Return

Return the approved objective, evidence, changed sections, page version,
verification results, template comparison when applicable, MCP evidence, and
whether an experiment is recommended.

### optimize reference: evidence-led-cro

# Evidence-Led CRO

Use this reference after the user selects an outcome.

## Evidence Order

Prefer:

1. Page analytics and funnel events.
2. Observed desktop/mobile behavior.
3. Product, offer, and traffic-source context.
4. Customer research or support evidence.
5. General ecommerce patterns.

Do not attach a predicted lift to a change unless the user has comparable
first-party experiment evidence.

## Outcome Checks

- **Conversion:** message match, offer clarity, trust, decision friction.
- **Add-to-cart:** product comprehension, variant selection, price visibility,
  stock state, CTA placement, media.
- **AOV:** bundle relevance, quantity breaks, complementary products, shipping
  threshold clarity.
- **Bounce:** load experience, first-screen relevance, intrusive elements,
  traffic-message mismatch.
- **Trust:** claim evidence, returns, shipping, reviews, creator attribution.
- **Mobile:** reading order, tap targets, sticky elements, overflow, media
  controls, form effort.
- **Speed:** image weight, video loading, fonts, scripts, layout shift.
- **SEO:** search intent, title/meta, headings, copy depth, internal links,
  structured data.

Keep strong sections unchanged. Separate certain fixes from ideas that should
be tested.

### optimize reference: industry-cro

# Industry CRO Patterns

Read only the matching section. These are decision prompts, not guaranteed
uplifts.

## Beauty

- Show texture, finish, shade, routine position, and realistic use.
- Keep ingredient and outcome claims tied to evidence.
- Check shade/variant selection and mobile gallery usability.
- Use before/after media only with permission and clear context.

## Supplements and Wellness

- Clarify use, serving size, ingredients, suitability, and safety language.
- Separate supported evidence from customer anecdotes.
- Make subscription terms, quantity, and price-per-serving understandable.
- Avoid fabricated scarcity, clinical claims, and implied endorsements.

## Fashion

- Prioritize fit, sizing, material, movement, and return information.
- Verify color/size variants and unavailable states.
- Use video or shoppable media for styling when it helps product understanding.
- Keep imagery consistent with the actual product and variant.

## Food and Beverage

- Clarify flavor, ingredients, allergens, quantity, storage, and delivery.
- Show pack size and bundle savings without hiding unit price.
- Use appetite-led media while keeping the delivered product recognizable.

## Luxury

- Protect visual restraint, provenance, craftsmanship, and service details.
- Avoid fake urgency, dense badge walls, and discount-first framing.
- Check high-resolution media, typography, spacing, and concierge paths.

## Home

- Clarify dimensions, scale, materials, installation, delivery, and returns.
- Use contextual room imagery without hiding product details.
- Check variant, finish, and bundle compatibility.

## General

- Use the product, audience, traffic source, and selected metric to decide.
- Prefer a focused hypothesis over a full redesign without evidence.

---

# Skill: plan-page

> Turn campaign and product requirements into a concise one-page storefront plan with a design direction, wireframe, imagery plan and resolved asset slots. Use before page design; this skill does not choose islands or implementation details.

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

## Bind the Workspace and Open the Campaign Folder

Read `work/storefront/setup/setup.json`. Select one saved workspace, store and
theme triple: the one the user names, otherwise the saved defaults. Read that
store's brand design and that theme's CSS. If the selection is not saved, stop
with `Run /setup for this store and theme first.` State the workspace, store
and theme in one line so a wrong default is visible immediately, and never mix
files from two themes, stores or workspaces on one page.

Then infer the campaign folder from the request with the table in
`references/page-files.md` (occasion and year, named sale, product launch,
evergreen funnel, channel test, collaboration, or `adhoc-<yyyy-mm>` when the
request is not campaign-shaped). Reuse the folder when this page continues an
existing campaign, including a variant or an edit; open a new one when the
occasion, offer or product changes. Say which folder is in use.

```text
work/campaigns/<campaign-slug>/
├── campaign.json     binding and campaign facts
├── campaign.md       one-page brief
├── assets/           media shared across this campaign's pages
└── pages/<page-handle>/
```

Write `campaign.json` with the binding and the confirmed campaign facts, and
`campaign.md` with the brief, before the page workspace. A campaign folder
holds one workspace, store and theme binding; a second store means a second
folder. Every page repeats the binding in its own manifest.

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

Record the route in `page-plan.md`. Do not force every user to choose among all
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

Write this block at the top of `page-plan.md` and mirror it in the manifest
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
   merchant; in fast-draft, proceed with the closest existing asset or a
   `planned` slot and still list it. Assets carry the page; plain colour
   does not.

The `## Checklist` JSON is the default this workflow lands on. When the
context argues for something else (a PDP with two images, a store with no
reviews, a brand whose voice bans a section), deviate and record it under
"Deviations from the type default". Run
`python3 <plan-page-skill>/scripts/plan_lint.py <page-workspace>` before
presenting the plan and treat its WARN rows as that deviation list.

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

Record only the selected kit or section IDs in the manifest (`template.mode`
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

Each lane returns only its block. The parent merges them into `page-plan.md`,
runs the generic-default check, resolves conflicts by the house rules, and asks
only unresolved questions required by the inferred mode. Lanes never write
files or spend credits.

## Write a One-Page Plan

Keep `page-plan.md` concise enough to scan in one view. Include:

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

### Design direction (required block in page-plan.md)

Write this block before the section list. Read the saved brand design, the
theme tokens and `references/design-rules.md` first. Fill
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
| A1 | gallery | product_media | 4:5 | shopify media | gid://…/ProductImage/… | verified |
| A2 | story | context | 3:2 | library | asset 7f2e… | verified |
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
   `selection_order` (A1, A2, …). Confirm the mapping in one line or take a
   one-line remap. Without a picker: Storefront → Design library → Assets;
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
   the manifest. A slot the user postpones stays `planned`; `/design-page`
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
`UNKNOWN_ACTION`, ask the user to pick a collection in Storefront → Reviews →
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
live inventory read. Mirror the summary in the manifest `offer` block.

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

Create the page directory under `work/campaigns/<campaign-slug>/pages/`, its
`assets/`, and a compact schema-v3 `page-manifest.json` using
`references/page-files.md`, including `campaignSlug`, `campaignPath`, the
workspace, store and theme ids, one `assets[]` entry per slot, and the
`reviews` block. Add the page handle to `campaign.json` `pages[]`. Do not create source,
preview, compile, or QA files.

## Approval

Present:

```text
Page:
Campaign: <campaign-slug> (<campaign type>)
Binding: <workspace> / <store> / <theme>
Page type: <type> · <funnel stage> · <awareness> · <traffic>
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

Return the campaign path, the page working directory, plan path, manifest path,
the workspace, store and theme in effect, the asset slot summary, the
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

---

# Skill: publish

> Publish a synchronized and QA-passed Lexsis storefront draft. Use only when the user explicitly asks to release a specific page version.

# Publish a Page

Publishing is a separate, explicit action. Do not rebuild the page here.

Read `references/workflow-intent.md`. Intent inference may distinguish a draft
request from a live-release request, but it never substitutes for explicit
approval naming the page and version. A request to preview, create, finish,
review, or make a page production-ready is not publication approval.

Use `lexsis_pages.edit_context`, `lexsis_pages.integrity`,
`lexsis_pages.source`, `lexsis_workspace.get`, and
`lexsis_live_ops.publish`. Resolve unfamiliar argument schemas with exact
router/action discovery. Do not use a prose query for these known actions. An
empty discovery result is not a publishing outage; the actual context,
entitlement, or publish call determines availability. A local QA report cannot
authorize or substitute for a successful live publish.

## Gate

1. Read the page manifest and QA report.
2. Confirm the saved store/theme binding still exists.
3. Confirm the current local bundle and section hashes match the synchronized
   values in the manifest.
4. Read `lexsis_pages` action `edit_context`.
5. Confirm the remote version equals `remote.lastKnownVersion`.
6. Confirm responsive, local-versus-hosted visual regression, commerce, copy,
   claims, assets, and integrity checks passed against that same version and
   local bundle.
7. Run the workspace validator with `--phase publish`, the live remote version,
   and source and bundle hashes fetched from that draft.
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
├── setup.json
└── workspaces/
    └── <workspace-id>/
        └── stores/
            └── <store-id>/
                ├── brand-design.md
                └── themes/
                    └── <theme-id>.css
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
  its own campaign folder or its own page workspace. Never combine design
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

# Storefront Craft Guide — Start Here

> **Not real islands:** `CompareTable`. They have no schema. Verify every island name
> against `lexsis_design` action `islands`; the replacement for each job is in
> `references/workflows/island-selection-workflow.md`.

> House rules in `storefront-engine/references/design-rules.md` override every example below.
> Examples show structure and copy intent; their styling (gradients, hover transforms,
> uppercase labels, pills, emoji, section fills) is illustrative and must not be copied.
> Where an example conflicts with a house rule, the rule wins.

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

Load this skill first on any storefront page generation task.

---

## Architecture: Vibe-Code

Pages are **source-format HTML + compiled Tailwind CSS + CSS custom properties
+ React islands**. No component JSON. The AI generates readable HTML directly
and Lexsis compiles it.

**Authoring source:**
```html
<!-- section: hero -->
<section id="hero">
  <lx-island name="BuyBox">
    <script type="application/json">
      {
        "product": {
          "title": "Product name",
          "variants": []
        }
      }
    </script>
  </lx-island>
</section>
```

The compiler produces VibePage storage JSON and hydrated `data-island`
markers. Do not write that compiled representation by hand.

---

## Skills Map

| Skill | Purpose | Load when... |
|---|---|---|
| `craft-guide` | This file — architecture, flow, quality bar | Always first |
| `workflow-orchestration` | Tool sequencing, parallelization, flow selection | Always — load after craft-guide |
| `conversion-psychology` | Universal persuasion: pricing, urgency, trust, CTA psychology | Always — load for any ecommerce page |
| `animation-system` | Managed WAAPI, GSAP, Canvas, WebGL, Three.js, Lottie and Rive | Only when the plan names one motion moment |
| `visual-craft` | Typography, spacing, color, micro-interactions | Polishing visual quality |
| `design-enrichment` | AI image generation + compositing pipeline | Need custom images/textures |
| `premium-patterns` | Proven high-converting section patterns in HTML | Building hero, trust, CTA sections |
| `island-patterns` | Per-island wrapper HTML + combination recipes | Using commerce/engagement islands |
| **Verticals** | | |
| `vertical-beauty` | Beauty/skincare: ingredient storytelling, before/after, editorial | Beauty, skincare, haircare, fragrance |
| `vertical-supplements` | Supplements: dark mode, clinical proof, comparison, urgency | Vitamins, protein, nootropics, fitness |
| `vertical-fashion` | Fashion: editorial layouts, lookbook grids, dramatic type | Clothing, shoes, accessories, streetwear |
| `vertical-food` | Food/bev: sensory photography, warm palettes, subscription | Food, coffee, snacks, meal kits |
| `vertical-luxury` | Luxury: restraint, whitespace, minimal sections, quiet CTAs | Jewelry, watches, designer, AOV>$300 |
| `vertical-home` | Home: room context, dimensions, material stories | Furniture, decor, candles, textiles |
| **Traffic Sources** | | |
| `traffic-source-meta` | Meta ads: message match, mobile-first, trust stacking | Facebook/Instagram ad landing pages |
| `traffic-source-google` | Google: intent matching, info density, CompareTable, FAQ | Google Ads/SEO landing pages |
| `traffic-source-tiktok` | TikTok: 3-sec hook, video-first, UGC aesthetic, 6-8 sections | TikTok/Reels/Shorts traffic |
| **Workflows** | | |
| `reference-pdp-remix` | Competitor PDP deconstruction and rebuild | Rebuilding a reference URL for your brand |

---

## Generation Flow (Overview)

```
1. lexsis_discover({ query: "page creation" }) → authoritative action schemas
2. [Optional] lexsis_asset_library({ action: "search", args: {...} }) → find existing brand assets
3. [Optional] lexsis_drafts({ action: "asset_generate", args: {...} }) → get image URLs
4. Agent authors source-format HTML with `<lx-island>` components
5. lexsis_pages({ action: "compile", args: { source, head, theme_css, scripts } }) → compile + validation
6. lexsis_page_create({ action: "create", args: { source, head, theme_css, scripts, slug, publish: false } }) → persist as draft, returns preview URL
7. lexsis_live_ops({ action: "publish", args: { page_id } }) → go live (ONLY after the user explicitly approves)
```

---

## CSS Variables (Brand Theming)

All sections use these CSS custom properties (set in `theme_css`):

| Variable | Purpose |
|---|---|
| `--lx-accent-color` | Primary brand/CTA color |
| `--lx-accent-color-hover` | Hover state |
| `--lx-text-color` | Primary text |
| `--lx-text-muted` | Secondary text |
| `--lx-bg-color` | Page background |
| `--lx-bg-surface` | Card background (never a section background) |
| `--lx-border-color` | Borders and dividers |
| `--lx-font-heading` | Heading font family |
| `--lx-font-body` | Body font family |

Use via `style="color: var(--lx-accent-color)"` or `style="font-family: var(--lx-font-heading)"`.

---

## Quality Bar

**Great page:**
- Mobile-first (works at 375px, enhances at lg:)
- Uses CSS vars for all brand colors/fonts (no hardcoded hex)
- Proper heading hierarchy (h1 → h2 → h3)
- Islands for all interactive commerce (BuyBox, Cart, Reviews)
- Generated/library images — no broken placeholder URLs in production
- No emoji as icons, one page background, one icon set, one bold moment
- Trust signals near purchase points
- Sticky add-to-cart on PDP

**Mediocre page:**
- Hardcoded colors instead of CSS vars
- Desktop-only layout
- Missing islands (raw HTML buttons instead of BuyBox)
- placeholder.co images shipped to production
- Emoji as icons, alternating section fills, mixed icon sets, scattered motion
- Trust badges missing

---

## Anti-Patterns (NEVER do these)

1. **No `fetch()` or XHR in section JS** — blocked by hydrator security
2. **No `eval()`, `localStorage`, `WebSocket`** — blocked
3. **No `@import` in section CSS** — blocked
4. **No external `url()` in CSS** — only inline colors via `--lx-*` tokens
5. **No duplicate section IDs** — each must be unique kebab-case
6. **No `<script src="...">` in HTML.** The section `js` field is compiler
   output, not something you author: in source you write a top-level
   `<script>` inside the section, and almost always you write none. Anything
   needing a timer, an observer or global access belongs in a managed motion
   module (`references/animation-system.md`) or an island; approved
   integrations go in `scripts[]`.
7. **No framework code** — no React/Vue/Angular in section HTML (islands handle interactivity)
8. **Don't fake commerce** — always use BuyBox island for add-to-cart, never a plain button

---

## Section ID Naming

Use descriptive kebab-case: `hero`, `product-gallery`, `social-proof`, `ingredients`, `faq`, `sticky-cta`, `trust-badges`, `footer`. Never `section-1`, `section-2`.

---

## Island Rules

- Author props in the `<lx-island>` JSON script child; the compiler writes
  `data-props`
- Use the live island catalogue and exact selected schema; do not rely on a
  fixed island count
- Follow lifecycle replacement guidance for deprecated or superseded islands
- One `BuyBox` per page (multiple breaks cart state)
- Cart: `head.use_cart_v2: true` on every commerce page (`CartDrawer` V1 deprecated — never author a cart section)
- `StickyBar` needs `triggerOffset` — distance in px before it appears
- `ReviewCarousel` can use custom reviews array OR fetch from Shopify via productId

---

## Tailwind Usage

- Lexsis compiles referenced utilities into one immutable page CSS artifact;
  there is no runtime Tailwind CDN
- Use responsive prefixes: `sm:`, `md:`, `lg:`, `xl:`
- Prefer utilities over custom CSS (only use section `css` for keyframes/animations)
- Use `clamp()` for fluid typography: `text-[clamp(2rem,5vw,4rem)]`
- Container: `max-w-7xl mx-auto px-4 sm:px-6 lg:px-8`

---

## Image Strategy

1. **Always check `lexsis_asset_library` action `search` first** — brand's uploaded assets are free and on-brand
2. **Use `lexsis_catalog.list` for product images** — never generate fake product shots
3. **`lexsis_drafts` action `asset_generate` for custom imagery** — hero backgrounds, lifestyle contexts, textures
4. **`lexsis_drafts` action `asset_generate` with `reference_images` for composites** — product-on-background, texture overlays
5. **Place URLs directly in HTML** — `<img src="${url}" />` or inline `style="background-image: url(...)"`
6. **Load `design-enrichment` skill** for full asset generation pipeline details
7. **For video, reference imagery, or external AI tools** → see `asset-pipeline.md` for multi-source strategy

---

# Managed Motion — Storefront Agent Reference

> The active storefront design rules override every example below.
> Motion is not a default decoration. Use it when the page plan names one
> meaningful moment or when motion directly answers a shopper action.

Lexsis supports open-ended custom animation without requiring a named scene or
a custom island for every visual idea. Agents author the composition; the MCP
compiler and renderer own capability validation, resource loading, lifecycle,
cleanup, reduced motion, and performance limits.

## Choose the lightest valid approach

| Need | Use |
|---|---|
| Hover, focus, or a small entrance | CSS transition or shared keyframe |
| Common reveal, parallax, pin, or marquee behavior | `data-behavior="gsap-*"` preset |
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
<!-- section: product-object -->
<section class="product-object">
  <canvas class="product-canvas" aria-label="Interactive product view"></canvas>
  <img
    class="product-fallback"
    src="https://cdn.example.com/product-static.webp"
    alt="Product front view"
  >
</section>

<script
  type="application/lexsis-motion"
  data-motion-id="product-object"
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

1. Author the source section and motion block in `lexsis-source.html`.
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
`page-plan.md` under "Overrides of brand design.md".

Loaded by `/plan-page` (Design direction block), `/design-page` (Design Direction
Gate and hosted review), `/generate` (Production Gate) and `/optimize`.
`design-page/scripts/design_lint.py <workspace>` runs the static checks and prints
the results table.

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

Format per rule: imperative sentence; rationale; a check the agent can run. Checks are written for macOS (BSD grep has no `-P`; use `perl -CSD`). `$W` is the page workspace, e.g. `work/campaigns/<campaign-slug>/pages/<handle>`. Browser checks run in the hosted draft via the browser tool's evaluate call.

### 2.1 NEVER

N1. Never use emoji by default, and never as icons: not in tickers, trust strips, badges, buttons, alt text, island JSON props or CSS `content`. Emoji may appear in copy only when the user explicitly insists; record it in `page-plan.md` under "Design direction › Emoji in copy" with the merchant's wording, and keep every occurrence inside running text. When the page needs icons and no inline SVG set fits, generate a monochrome SVG icon set (one stroke, one size); never substitute emoji.
Rationale: glyphs render differently per OS vendor, ignore `currentColor` and stroke weight, are announced by Unicode name to screen readers, and are the most recognised marker of AI-generated pages (Miller et al. 2018; uxskill).
Check:
```bash
perl -CSD -ne 'while(/([\x{1F000}-\x{1FAFF}\x{2600}-\x{27BF}\x{2B00}-\x{2BFF}\x{2300}-\x{23FF}\x{1F1E6}-\x{1F1FF}\x{FE0F}\x{200D}\x{203C}\x{2049}])/g){print "$ARGV:$.: $1\n"}' $W/lexsis-source.html $W/page-theme.css | wc -l   # 0, unless page-plan.md records "Emoji in copy: allowed"; then every hit must be inside copy, none as an icon
```

N2. Never change the background from section to section. The page has one background, `--lx-bg-color`, from below the navbar to above the footer. Allowed exceptions, exhaustively: the announcement bar, the navbar, the footer, and at most one full-bleed moment that `page-plan.md` names under "Design direction › Bold moment". A `<section>` or any full-width wrapper painted `--lx-bg-surface`, `--lx-surface-alt` or `--lx-secondary-color` is a band and fails, even if it is white.
Rationale: bands are a template's way of faking structure; separation belongs to spacing, type scale and hairlines (NN/g grouping; Stellae). Alternating fills are also the reason the rejected page read as five stacked templates.
Check (browser):
```js
(() => { const body = getComputedStyle(document.body).backgroundColor, vw = document.documentElement.clientWidth;
  return [...document.querySelectorAll('body *')].filter(el => { const cs = getComputedStyle(el);
    return cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && cs.backgroundColor !== body && el.getBoundingClientRect().width >= vw - 2 && el.getBoundingClientRect().height > 40; })
    .map(el => ({ el: el.id || el.className || el.tagName, bg: getComputedStyle(el).backgroundColor })); })()
```
Pass when the list contains only announcement, nav, footer elements and at most one element whose id matches the plan's bold moment.

N3. Never use emoji, images or mixed libraries as icons. Icons are one inline SVG set, one stroke weight, `stroke="currentColor"`, `fill="none"`, one size per context, `aria-hidden="true"` with a visible text label. Or no icons.
Rationale: two stroke languages on one screen is a tell; icons that garnish headings are skipped by readers (uxskill icons).
Check:
```bash
grep -o 'stroke-width="[^"]*"' $W/lexsis-source.html | sort -u | wc -l   # 0 or 1
grep -c '<img[^>]*class="[^"]*icon' $W/lexsis-source.html                 # 0
```

N4. Never use more than two type families. A non-Latin script gets one matching family declared with `[lang]`; it does not count.
Rationale: one display face plus one workhorse is the ceiling for coherence (frontend-design; Shopify Theme Store "Consistent typography").
Check:
```bash
grep -oE "family=[A-Za-z+]+" $W/page-theme.css | sort -u | wc -l          # <= 3 including the [lang] family
```

N5. Never set eyebrow labels in ALL-CAPS unless a merchant-stated brand rule (not a generator-observed one) requires it, and then at most one per three sections.
Rationale: the tracked-out caps eyebrow above every heading is the highest-frequency AI tell (designer-skill avoid-ai-slop; frontend-design).
Check:
```bash
grep -cE 'uppercase|text-transform:\s*uppercase' $W/lexsis-source.html $W/page-theme.css   # 0, or <= ceil(sections/3) with a stated rule
```

N6. Never accent a single word or phrase inside a headline with colour, italic, weight or underline.
Rationale: the one-word accent is a default treatment, not a decision (frontend-design).
Check:
```bash
perl -0ne 'print scalar(() = /<h[1-3][^>]*>[^<]*<(span|em|strong|i|b|mark)/g), "\n"' $W/lexsis-source.html   # 0
```

N7. Never use gradient washes, glow shadows, shimmer, pulse, float, animated backgrounds, or `hover:scale` / `hover:-translate` / `hover:scale-1xx` on cards, buttons or images. The only permitted gradient is a black-to-transparent overlay on a photograph for text legibility inside the plan-named bold moment.
Rationale: gradient + hover-lift is the SaaS-card kit that reads as generated regardless of brand (Sailop; frontend-design).
Check:
```bash
grep -nE 'gradient\(|bg-gradient|shimmer|animate-pulse|pulseRing|float-|hover:scale|hover:-translate|scale\(1\.[0-9]|box-shadow:\s*0 0 ' $W/lexsis-source.html $W/page-theme.css | wc -l   # 0, or only the plan-named overlay
grep -nE 'box-shadow:[^;}]*(--lx-accent|color-mix\()' $W/lexsis-source.html $W/page-theme.css | wc -l   # 0; a shadow tinted with the accent is a glow whatever its offsets
```

N8. Never wrap plain text in a card. A card (`--lx-bg-surface`, border, or shadow with radius) surrounds a distinct object only: a product, a proof artefact with an image, a table, a form, a quoted review. Paragraphs, lists and FAQs sit on the page background.
Rationale: identical rounded cards chop content into interchangeable units and signal that nothing is more important than anything else (uxskill tells; NN/g common region "use sparingly").
Check: for each element matching `\.rs-card|bg-surface|rounded-[a-z0-9]+.*shadow`, confirm it contains `<img`, `<table`, `<form`, `<blockquote` or a price. Manual pass on the 1280 screenshot; count cards that contain only text; must be 0.

N9. Never render discount or status pills in ALL-CAPS or with percentages ("31% OFF", "BEST VALUE", "MOST POPULAR", "NEW ARRIVALS") unless the merchant runs a named sale recorded in the plan's confirmed claims. Compare-at price is struck-through text only.
Rationale: the OFF pill and the highlighted middle tier are stock conversion-template chrome; Baymard's guidance is to show the price and compare-at clearly, not to shout.
Check:
```bash
grep -nE '\b[0-9]{1,2}% ?OFF\b|BEST VALUE|MOST POPULAR|LIMITED TIME|NEW ARRIVAL' $W/lexsis-source.html | wc -l   # 0
```

N10. Never add motion that is not answering a user action, except one orchestrated moment named in the plan. No fade-up per section, no stagger, no counters, no parallax, no marquee ticker unless the announcement bar's own island provides it. Custom motion must follow `animation-system.md` and use `application/lexsis-motion`, not raw observers, timers, or global DOM access.
Rationale: scattered entrance effects are the generic default; one moment lands, ten do not (frontend-design; Sailop).
Check:
```bash
grep -cE 'application/lexsis-motion|data-behavior="gsap-|@keyframes|animation:' $W/lexsis-source.html $W/page-theme.css   # 0, or exactly the plan-named moment
grep -cE 'data-reduced-motion=|prefers-reduced-motion' $W/lexsis-source.html $W/page-theme.css   # >= 1 if any animation exists
grep -cE 'new (IntersectionObserver|ResizeObserver|MutationObserver)|requestAnimationFrame|setInterval' $W/lexsis-source.html   # 0
```

N11. Never show proof you cannot source: star glyphs, review counts, customer counts, "Only N left", countdowns, "as seen in" logos. Every number in a proof section traces to "Claims confirmed" in the plan.
Rationale: fabricated proof destroys trust and is itself a tell (five gold stars + round avatar + italic quote). The engine's own `generate-pdp.md` line 64 already says never invent reviewers.
Check: list every numeral in sections tagged proof/trust/reviews; each must appear in `page-plan.md` under confirmed claims.

N12. Never append `→` or `»` to link and button text, join meta strings with middle dots, or place an icon in a rounded tile above a heading (icon-tile-stack).
Rationale: template chrome that appears whatever the subject (frontend-design; designer-skill).
Check:
```bash
grep -cE '(→|&rarr;|»)\s*</(a|button)' $W/lexsis-source.html   # 0
grep -cE 'w-1[0-6] h-1[0-6][^"]*rounded' $W/lexsis-source.html   # 0
```

N13. Never mix radii on the same object type or use one radius on everything. Declare a radius scale by object type and use only those tokens.
Rationale: uniform `rounded-2xl` on cards, buttons, inputs and images is the absence of a system (Sailop "rounded-2xl on everything").
Check:
```bash
grep -ohE 'border-radius:\s*[^;]+|rounded(-[a-z0-9\[\]]+)?' $W/lexsis-source.html $W/page-theme.css | sort | uniq -c | sort -rn   # <= 4 distinct values, each mapped to a type in page-theme.css comments
```

N14. Never hardcode off-brand hex or Tailwind default colours. Colours come from `--lx-*` tokens or the plan's named palette.
Rationale: `#667eea`, `#764ba2`, `#8b5cf6`, `#f9fafb`, `text-yellow-400` appear throughout the engine references and mark a page as templated (uxskill tells).
Check:
```bash
grep -nEi '#667eea|#764ba2|#8b5cf6|#f9fafb|#6366f1|#7c3aed|text-(yellow|gray|slate|purple|indigo)-[0-9]' $W/lexsis-source.html $W/page-theme.css | wc -l   # 0
```

### 2.2 ALWAYS

A1. Always write the Design direction block in `page-plan.md` before any HTML: palette of 4 to 6 named hex with roles; type roles, families and one modular ratio; layout concept in one sentence plus an ASCII wireframe at 1280 and 390; alignment rule; icon decision; the one bold moment; the background rule with its single named exception or "none"; motion decision; the generic-default check with at least three concrete differences; the list of brand-design.md lines being overridden.
Rationale: the plan-review-build-critique loop is what stops the model averaging toward the centre of its training data (frontend-design).
Check: `grep -c '^\*\*' page-plan.md` under "## Design direction" returns all 10 field labels from the template in section 3.1; none is empty or "TBD".

A2. Always separate sections with a spacing scale and, where a break is needed, one 1px hairline in `--lx-border-color`. Use one 8-point scale; section padding comes from at most two pairs (e.g. 64/96 and 40/56 mobile/desktop).
Rationale: proximity and whitespace carry grouping; a line is a subtle, universally understood divider; colour is emotional and should be spent on pacing, not plumbing (NN/g; Stellae; Tubik).
Check: `grep -oE 'padding:\s*[0-9]+px' $W/page-theme.css | sort -u` yields values from the 8-pt scale only; `grep -c 'border-top: 1px solid var(--lx-border-color)'` is the only divider mechanism.

A3. Always build hierarchy with a single modular type scale (one ratio, 1.2 to 1.333 for commerce), no more than three sizes visible on one screen, one `<h1>`, one `<h2>` per section, headings 1.1 to 1.2 line-height, body 1.5 to 1.7.
Rationale: three sizes give hierarchy without noise; NN/g and accessibility.build converge on this.
Check: `grep -c '<h1' $W/lexsis-source.html` is 1; every `font-size` in `page-theme.css` is a step of the declared ratio (list them: `grep -oE 'font-size:\s*[^;]+' | sort -u`).

A4. Always keep body measure between 45 and 80 characters at every viewport; give serif body 0.05 more line-height than sans. Constrain text containers with `max-width` in `ch` (60 to 70ch), not px.
Rationale: WCAG 1.4.8 caps body at 80 characters; legibility research centres on 45 to 75 (Butterick 45 to 90).
Check (browser, 1280):
```js
(() => [...document.querySelectorAll('p, li, figcaption')].map(p => ({ t: p.textContent.trim().slice(0,40), cpl: Math.round(p.getBoundingClientRect().width / (parseFloat(getComputedStyle(p).fontSize) * 0.5)) })).filter(x => x.cpl > 80))()   // []
```

A5. Always record one icon decision in the plan and, if icons exist, ship them as one inline SVG set at one size and one stroke, with the text label always visible.
Rationale: see N3. Check: as N3, plus `grep -c 'aria-hidden="true"'` equals the SVG count.

A6. Always declare a radius scale by object type in `page-theme.css` (`--r-control`, `--r-card`, `--r-media`, `--r-pill`) and use only those tokens.
Rationale: the relationship between radii is the design. Check: `grep -c 'border-radius: var(--r-' $W/page-theme.css $W/lexsis-source.html` equals the total count of `border-radius` declarations.

A7. Always meet WCAG 2.2 AA: 4.5:1 for text under 24px (18.67px bold), 3:1 for large text and for UI component boundaries, including muted text on the page background, accent on any tint, and button text on button fill.
Rationale: W3C 1.4.3 and 1.4.11; the RudraSetu guide itself flags #D52600 on #FBE9E6 as borderline.
Check:
```bash
python3 - <<'PY'
def L(h):
    r,g,b=[int(h.lstrip('#')[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
def ratio(a,b):
    x,y=sorted([L(a),L(b)],reverse=True); return round((x+0.05)/(y+0.05),2)
pairs={'text/page':('#1F1D24','#F5F0E6'),'muted/page':('#6B6560','#F5F0E6'),'accent/page':('#D52600','#F5F0E6'),'accent/tint':('#D52600','#FBE9E6'),'cream/charcoal btn':('#F5F0E6','#1F1D24'),'cream/maroon bar':('#F5F0E6','#8B1A00')}
for k,(a,b) in pairs.items(): print(k, ratio(a,b))
PY
```
Every text pair >= 4.5, every large-text or component pair >= 3.

A8. Always compose the PDP buy section to Baymard and Shopify requirements: untruncated title, price and compare-at, unit price if applicable, variant options as buttons, quantity, add-to-cart, a shipping and returns line, all within the first viewport on desktop and within 1.5 viewports at 390px; product media takes 50 to 60 percent of desktop width.
Rationale: users decide on the PDP; hidden price or delivery cost is a top abandonment cause (Baymard PDP research; Shopify Theme Store product page requirements).
Check: at 390 screenshot, price and add-to-cart appear above y = 1266px; at 1280, both appear above y = 800px.

A9. Always spend boldness once. Name the single memorable element in the plan; every other element is quiet: page background, body weight, hairlines, sentence case.
Rationale: one element can be remembered; the mirror test, remove one accessory (frontend-design; Chanel).
Check: the 1280 screenshot has exactly one element that a squint test isolates; it matches the plan's bold moment.

A10. For production-ready work, always run the hosted design review at 390 and 1280 before recording design approval. Fast drafts return `DRAFT_CREATED` first and may leave this review pending.
Rationale: the real renderer catches banding, hierarchy, hydration, and media problems without maintaining a second preview runtime.
Check: `$W/qa-report.md` records the hosted preview URL, tested version, both viewports, and no blocking design failure before `design.status` becomes `approved`.

A11. Always ship the quality floor without announcing it: `:focus-visible` styles, `prefers-reduced-motion` handling, 48px minimum tap targets, alt text on product media, `lang` attributes on non-Latin text.
Check: `grep -c ':focus-visible' $W/page-theme.css` >= 1; `grep -c 'prefers-reduced-motion'` >= 1 when animation exists; `grep -c 'lang="'` >= 1 when Devanagari is present.

A12. Always write copy as design content: sentence case, active voice, the CTA says what happens ("Add to cart", not "Shop Now →"), no placeholder or invented copy, brand voice from `voice_md` or the merchant.
Check: `grep -cE '>(Shop Now|Get Started|Learn More|Buy Now)\s*(→)?<' $W/lexsis-source.html` is 0; no "lorem".


## Tells (fail the squint test)

Cream page + high-contrast serif + terracotta accent as the only idea; identical rounded cards with one radius and one grey shadow; tracked-out ALL-CAPS eyebrow above every heading; meta strings joined with middle dots; `WORD — fragment` labels; `→` appended to links and buttons; icon in a rounded tile above every heading; discount pills and "MOST POPULAR" ribbons; gradient washes; fade-up on every section; five gold stars with a round avatar and an italic quote; a monospace face for small labels; near-black `#0B0B0B` standing in for black.

Source audit: internal design-rules research (2026-09-05).

---

# Island Presets

Named, pre-validated prop and CSS presets for the active Lexsis islands. A preset id is a
design-intent token the plan may name (`Preset: buybox/compact-dark`); `/design-page`
applies it verbatim and records any deviation as `presetOverrides` in the manifest.
Every preset respects `storefront-engine/references/design-rules.md`: no emoji, no gradients, transparent island
surfaces on the single page background, no icon glyphs unless the page has no other
icon set, no motion effects. Verified against island schema 5.1.0 on 2026-09-05; when
`island_schema` reports a different version, re-verify before use.

## 2. Per-island reference

### 2.1 SiteHeader

Compound announcement bar + navbar. Category navigation. Hydrate default `immediate`. Variants: none. Headless: no (but supports *hydration mode*: author your own `<header>` markup with `data-lx-header="root|announcement|announcement-text|announcement-dismiss"` and `data-lx-nav="root|cart-trigger|cart-count|mobile-trigger|mobile-panel|link|logo"` as the child of `<lx-island>`; props then only carry behavior). Max 1 per page, first section; never combine with a separate Navbar.

UI-controlling props (schema v5.1.0):

| Prop | Type | Values / default | Effect |
|---|---|---|---|
| `sticky` | boolean | - | header pins to top |
| `transparent` | boolean | - | no nav background until scroll (hero overlap) |
| `offsetTop` | string | CSS length | top offset when sticky |
| `cartMode` | enum | `drawer` \| `link` | cart icon opens drawer or navigates to `cartUrl` |
| `hideCart` | boolean | - | removes cart trigger |
| `dismissible` / `rotateInterval` | boolean / number | top-level, hydration mode only | announcement close button, rotation ms |
| `announcement.backgroundColor`, `.textColor` | string | hex or `var(--lx-*)` | announcement bar paint (allowed exception to one-background rule) |
| `announcement.speed` | number | ms; keep >= 4000 | rotation speed |
| `announcement.dismissible` | boolean | - | close button |
| `navbar.transparent` | boolean | - | same as top-level for legacy mode |
| `navbar.style` | object | `bgColor, textColor, accentColor, logoHeight, height, borderBottom, fontFamily, fontSize, fontWeight, padding, maxWidth, dropdownBg, dropdownTextColor, mobileBg, mobileTextColor` (all string) | full nav paint and type; schema types these as `?object`, examples pass strings |
| `navbar.hideCart` | boolean | - | - |

Data props: `announcement.messages[]` (string, keep < 60 chars), `announcement.link`, `navbar.logo{src|text, alt, url}` (use `text` wordmark when no logo asset), `navbar.links[{label,url,children[]}]`, `navbar.cta{label,url}`, `navbar.cartCount` (omit; auto-synced), `cartUrl`, `messages[]` (hydration mode).

CSS vars declared: `--lx-accent-color` only. `--lx-header-*`, `--lx-nav-*` from the earlier capture: unconfirmed, not in schema.
Parts: `announcement, announcement-dismiss, announcement-text, cart-badge, cart-trigger, cta, dropdown, dropdown-item, link, links, logo, mobile-link, mobile-panel, mobile-trigger, nav, root`.
Fallback: hydration-mode markup *is* the fallback; for legacy (props-only) mode give a plain `<header>` with logo link and 3-5 `<a>` links as the `data-lx-island-fallback` child.
Gotchas: `navbar.style.*` values must be strings even though schema prints `?object`. Announcement paint is the only place a non-page background is allowed besides footer. Do not set `cartCount`.

### 2.2 Navbar

Nav only (use when no announcement, or when announcement should scroll away). Hydrate `immediate`. Variants: none. Hydration mode as above with `data-lx-nav` tags. Must be a direct page child, not inside a section wrapper, for sticky to work.

UI-controlling props: `sticky`, `transparent`, `offsetTop`, `cartMode` (`drawer|link`), `hideCart`, `style{bgColor, textColor, accentColor, logoHeight, height, borderBottom, fontFamily, fontSize, fontWeight, padding, maxWidth, dropdownBg, dropdownTextColor, mobileBg, mobileTextColor}`, `cart{icon: cart|bag|basket, svg, image, label, badgeColor}`.
Data props: `logo{src|html, alt, url}` (required), `links[{label,url,children[]}]` (required), `cta{label,url}`, `cartUrl`, `cartCount` (omit).
CSS vars: `--lx-accent-color`. Parts: `cart-badge, cart-trigger, cta, dropdown, dropdown-item, link, links, logo, mobile-link, mobile-panel, mobile-trigger, root`.
Fallback: plain `<nav>` with logo and links.
Gotchas: `cart.svg` lets you supply the page's single inline SVG set icon (house rule: one stroke weight, `currentColor`); prefer it over `cart.icon` when the page already uses custom SVGs. `logo.html` accepts an inline SVG wordmark.

### 2.3 AnnouncementBar

Standalone rotating message strip. Hydrate `immediate`. Variants: none (earlier capture's `default|gradient|ticker|minimal` do not exist; a gradient would also break house rules). Max 1 per page; pair with Navbar, never with SiteHeader.

UI-controlling props: `backgroundColor` (string), `textColor` (string), `sticky` (boolean, default false), `dismissible` (boolean, default false; only meaningful with `sticky`), `speed` (number ms, default 4000, keep >= 4000).
Data props: `messages[]` (required, string), `link` (string, whole bar becomes a link).
CSS vars: `--lx-accent-color`. Parts: `close-btn, icon, link, root, text`.
Fallback: one `<p>` with the first message.
Gotchas: the `icon` part exists but no prop controls it; hide it with `[data-part="icon"]{display:none}` when the page has no icon set. Text must be emoji-free (house rule and validator check).

### 2.4 ProductGallery

PDP media gallery (thumbnail rails, grids, collage, masonry; image + video; lightbox; variant sync). Category commerce. Hydrate `immediate`. Headless: no. Variants = `layout` values.

UI-controlling props:

| Prop | Type | Values / default | Effect |
|---|---|---|---|
| `layout` | enum | `horizontal` (default) \| `vertical` \| `stacked` \| `grid` \| `collageLeft` \| `collageRight` \| `twoColumn` \| `masonry` | desktop arrangement |
| `mobileLayout` | enum | `stacked` \| `swipe` | always set explicitly for grid/collage/masonry |
| `thumbPosition` | enum | `left` \| `right` \| `bottom` \| `top` | rail placement for horizontal/vertical |
| `transition` | enum | `none` \| `slide` \| `fade` (default) \| `zoom` \| `kenBurns` | avoid kenBurns (motion) |
| `objectFit` | enum | `cover` (default) \| `contain` | contain for packshots on white |
| `maxHeight` | string | CSS length | caps main media |
| `enableLightbox` | boolean | - | adds `open-lightbox` control |
| `autoplay` / `interval` | boolean / number | false / 4000 | avoid on PDP |

Data props: `media[]` (current; `images[]` is deprecated and kept as an alias; item `{src|url, alt, type: image|video, poster, mobileSrc, srcSet, sizes, fit, objectPosition, sources[], provider}`), `listenForVariant` (boolean; needs a VariantSwatches emitter).

CSS vars (declared, long list; the useful subset): `--lx-product-gallery-bg, -border, -radius, -gap, -mobile-gap, -mobile-peek, -mobile-ratio, -columns, -tile-ratio, -featured-ratio, -stacked-ratio, -masonry-tall-ratio, -masonry-wide-ratio, -focus-width, -focus-offset, -open-bg, -open-color, -open-shadow`; `--lx-media-carousel-arrow-{bg,border,color,hover-bg,offset,radius,shadow,size}`, `--lx-media-carousel-dot-{color,active-color,active-scale,gap,offset,shadow,size}`, `--lx-media-carousel-{bg,duration,ease,fit,radius,placeholder}`; `--lx-media-lightbox-{backdrop,close-*,control-*,max-width,max-height,media-bg,padding,mobile-padding,z-index}`; `--lx-video-*` and `--lx-shoppable-*` (video tiles only); `--lx-accent-color, --lx-bg-surface, --lx-text-color`.
Parts (useful subset): `root, viewport, track, slide, main-media, media, image, video, thumbnail-strip, thumbnail, grid, grid-item, controls, previous, next, dots, dot, open-lightbox, lightbox, lightbox-close, lightbox-content, adaptive-video-*`.
Fallback: first image as `<img>` at the gallery aspect ratio.
Gotchas: the compile validator accepts `media` or legacy `images`; each item needs `src` (or `url`). Presets use `media`.

### 2.5 ProductHero

Large hero gallery for split PDP layouts (media 50-60 percent of viewport beside BuyBox). Category commerce. Hydrate `visible` (design QA must scroll it into view). Headless: no. Variants = `layout`.

UI-controlling props:

| Prop | Type | Values / default |
|---|---|---|
| `layout` | enum | `stacked` \| `splitLeft` (default) \| `splitRight` \| `fullHeight` |
| `thumbnails` | enum | `none` \| `rail` (default) \| `dots` |
| `thumbnailPosition` | enum | `left` (default) \| `right` \| `bottom` (no `top`) |
| `navigation` | enum | `none` \| `arrows` \| `floatingArrows` (default) |
| `aspectRatio` | string | `3:4` default; `1:1`, `4:5` |
| `maxHeight` | string | `85vh` default |
| `transition` | enum | `none` \| `slide` \| `fade` (default) \| `zoom` \| `kenBurns` |
| `showIndicators` | boolean | - |
| `autoplay`, `interval`, `hoverAdvance` | boolean, number, boolean | false, 4000, false |
| `className` | string | passes through to root |

Data props: `images[]` (required; `{url, alt, type, poster, objectFit, objectPosition}`; note key is `url` here, `src` in ProductGallery), `listenForVariant`.
CSS vars: `--lx-hero-bg, --lx-hero-radius, --lx-hero-thumb-radius, --lx-hero-thumb-size, --lx-hero-thumb-gap, --lx-hero-arrow-bg, --lx-hero-arrow-size, --lx-hero-arrow-offset, --lx-hero-transition-duration, --lx-accent-color, --lx-border-color` (schema also lists a stray `--lx-hero-` prefix entry).
Parts: `root, media-pane, slide, thumbnail-rail, thumbnail, nav-prev, nav-next, dot`.
Fallback: first image `<img>` with the chosen aspect ratio.
Gotchas: default `85vh` pushes BuyBox below the fold on mobile; presets cap at `560px`-`640px`. Set `--lx-hero-bg: transparent`. Confirmed working styling pattern: `#id{--lx-accent-color:...;--lx-hero-radius:12px;--lx-hero-thumb-radius:10px}` and `#id [data-part="thumbnail"]{...}`.

### 2.6 BuyBox

Primary purchase UI: price, variant buttons, quantity, add-to-cart, optional trust badges, notify-me. Category commerce. Hydrate `immediate`. Headless: **yes** (hooks `add` required; `price, compare-price, variant-option[data-variant-id], qty, qty-inc, qty-dec, stock, error`; state classes `lx-selected lx-disabled lx-adding lx-added`). Max 1 per page. Requires `head.use_cart_v2: true` for cart feedback.

UI-controlling props:

| Prop | Type | Values / default | Effect |
|---|---|---|---|
| `variant` | enum | `default` \| `compact` \| `expanded` | compact drops qty and variant selector (single-variant only); expanded adds trust badges block |
| `showPrice` | boolean | true | hide when the section renders its own price |
| `showVariantSelector` | boolean | true | set false when VariantSwatches is used |
| `showTrustBadges` | boolean | - | badges row; default icons are the island's own set (see gotcha) |
| `buttonStyle` | object | `{borderRadius, padding, fontSize}` strings | CTA shape without CSS |
| `animate` | boolean \| string | true | add-to-cart feedback motion |
| `ctaText` | string | - | button label |

Data props: `product{title, price, compareAtPrice, variants[{id,title,price,available}]}` (required; `id` is the Shopify variant GID), `listenForEvents` (boolean, pair with VariantSwatches). `productId` shown in `index.md` and old layouts is **not** in the v5.1 schema.
CSS vars: `--lx-accent-color` only. Parts: `root, cta, variants, variant-btn, qty, qty-btn, trust-badges, notify`.
Fallback: static price `<p>` plus a disabled-looking `<a>` to `/products/{{product.handle}}`; never a working custom button.
Gotchas: `showTrustBadges` icons are not controllable by prop; if the page has no icon set or a different SVG set, set `showTrustBadges:false` (house rule: one icon style). Earlier capture's variants `standard|full-width|split|minimal` do not exist. Do not duplicate title/price outside the island unless `showPrice:false`.

### 2.7 StickyBar

Bottom-fixed CTA re-surfacing add-to-cart (product mode) or a collection link (collection mode). Category commerce. Hydrate `immediate`. Variants: none. Headless: no. Place after the BuyBox section.

UI-controlling props: `showAfter` (string CSS selector, e.g. `"#buy"`, or number px; **always set**), `animate` (boolean | string, default true; `false` for quiet pages), `cta` (string, default "Add to Cart").
Data props: `product{title, price, compareAtPrice?, image?, variantId}` (variantId required in product mode) **or** `collection{label, url, subtitle?, image?}`.
CSS vars: `--lx-accent-color, --lx-text-color`. Parts: `root, bar, cta, product-image, product-info, product-price, product-title`.
Fallback: none needed (bar is hidden until scroll); an empty child is fine.
Gotchas: no bar background prop; the bar paints its own surface (accepted: it is fixed chrome, not a section). Style `[data-part="bar"]` for border-top/shadow removal. Omit `product.image` for a text-only bar.

### 2.8 ProductCarousel

Horizontal product-card rail ("You may also like"). Category commerce. Hydrate `immediate`. Variants: none; card look via `cardVariant`. Headless: no. Needs 4+ products; `showQuickAdd` requires cart v2.

UI-controlling props:

| Prop | Type | Values | Effect |
|---|---|---|---|
| `cardVariant` | enum | `default` \| `compact` \| `compactRows` | card density; compactRows renders a list |
| `mediaTransition` | enum | `none` \| `slide` \| `fade` \| `zoom` \| `kenBurns` | card image swap on hover-advance |
| `hoverAdvance` / `hoverAdvanceMode` / `hoverInterval` | boolean / `next`\|`cycle` / number | cycles card media on hover; off for quiet pages |
| `showQuickAdd`, `showWishlist`, `showLearnMore`, `showQuickView` | boolean | - | card actions; each adds a button (icon buttons use the island's icon set) |
| `animate` | boolean \| string | - | staggered fade-up on entry |
| `columns` | number | - | ignored in carousel context per anti-pattern note; unconfirmed effect |
| `title` | string | - | heading rendered by island (`heading`/`title` parts) |

Data props: `products[{id, handle, title, subtitle?, price, compareAtPrice?, badge?, image? | media[]?, variants[]?}]` (required).
CSS vars: same media-carousel/featured-media/video family as ProductGallery plus `--lx-surface-alt, --lx-text-muted, --lx-border-color, --lx-bg-surface, --lx-accent-color, --lx-text-color`. No dedicated card radius/border var; use parts.
Parts (useful): `root, heading, title, track, viewport, slide, card-wrapper, image, badge, price, compare-price, quick-add, nav-prev, nav-next, dots, dot, row, row-image, row-title, row-price, row-subtitle, row-list, media-placeholder`.
Fallback: 4 static cards (`<a>` + `<img>` + title + price) in a 2/4 grid.
Gotchas: omit `title` and render the section h2 yourself to keep heading hierarchy in the wrapper (contract: h2 owned by section). `showWishlist`/`showQuickView` add icon buttons in the island's own icon style; leave off when the page uses its own SVG set.

### 2.9 Footer

Site footer: link columns, logo, tagline, social, newsletter, copyright. Category navigation. Hydrate `immediate`. Variants: none; layout via `style.layout`. Hydration mode: author your own `<footer data-lx-footer="root">` with optional `newsletter-form`, `newsletter-input`, `newsletter-success`, `year` tags. Max 1, last section. Footer may paint its own background (house-rule exception).

UI-controlling props:

| Prop | Type | Values |
|---|---|---|
| `style.layout` | enum | `simple` \| `centered` \| `columns` \| `editorialGrid` \| `newsletterSplit` |
| `style.bgColor, textColor, linkColor, linkHoverColor, headingColor, accentColor, borderColor` | string | colors |
| `style.fontFamily, fontSize, padding, maxWidth, logoHeight, logoFilter` | string | type, spacing, logo treatment (`logoFilter: "invert(1)"` for dark footers) |
| `borderStyle` | enum | `none` \| `solid` \| `dashed` (top rule) |
| `tileLayout` | boolean | social links as tiles (`social-tiles` part) |

Data props: `columns[{heading?, links[{label,url}]}]`, `links[]` (simple layout), `logo{src, alt}`, `tagline`, `copyright`, `socialLinks[{platform, url, icon?}]`, `newsletter{heading, placeholder, buttonText}`, `successMessage`.
CSS vars: `--lx-accent-color`. Parts: `root, columns, nav-rows, newsletter, social-tiles`.
Fallback: hydration-mode markup, or a `<footer>` with links and copyright.
Gotchas: social icons are the island's own glyphs; `socialLinks[].icon` accepts a string (URL or inline SVG; unconfirmed which). If the page has no icon set, prefer text social links via `columns` and omit `socialLinks`. Old `layouts/compact.json` uses `style.variant`/`style.inline`/`newsletter.enabled`, none of which exist in v5.1.

### 2.10 ReviewCarousel

Rotating or grid review showcase with stars, verified flag, avatars, optional media. Category social_proof. Hydrate `visible`. Headless: no. Two data modes: static `reviews[]` (wins if non-empty) or fetch (`collectionId` or `productIds` + filters; the page supplies the endpoint at runtime, never write `reviewsEndpoint`). Mid-page or after product details, never first. Needs 3+ real reviews; never fabricate.

UI-controlling props:

| Prop | Type | Values / default | Effect |
|---|---|---|---|
| `variant` | enum | `default` \| `compact` \| `minimal` \| `grid` (default `default`) | default = one card carousel; compact = short strip; minimal = quote-only (short bodies only); grid = all at once |
| `autoplay` | boolean | true | set false for grid and for quiet pages |
| `interval` | number | 5000, keep >= 4000 | - |
| `pageSize` | number | 10, max 20 | fetch mode count |

Data props: `reviews[{id?, author, rating, title?, body, date?, verified?, avatar?, helpful_count?, media[]?}]` (static, only real reviews from `lexsis_catalog.reviews`), or fetch mode `collectionId` (an active collection from the plan's Proof sources line) or `productIds[]`, plus `reviewSnapshotId`, `minRating`, `sort` (`recent|highest|most_helpful`). Omit `reviewsEndpoint`.
CSS vars: `--lx-accent-color` (avatar bg, active dot), `--lx-text-color` (author). Parts: `root, card, avatar, author, body, title, date, verified, media-preview, nav-prev, nav-next, dots, dot, load-more`.
Fallback: 3 static blockquotes with author lines.
Gotchas: stars and the verified check are island glyphs (not controllable); acceptable as the page's single icon set only if the rest of the page uses no other icons, otherwise hide `[data-part="verified"]` and rely on the "Verified" text. `index.md` mentions `card-grid` on `--lx-surface-alt` backgrounds; house rules forbid that, so cards sit on the page background with a hairline border. `card` default may carry a shadow; flatten via `[data-part="card"]{box-shadow:none;border:1px solid var(--lx-border-color)}`.

### 2.11 InventoryIndicator

Low-stock urgency: "Only X left" pill, progress bar, or inline text. Category commerce. Hydrate `immediate`. Headless: no. Auto-hides above `lowStockThreshold`; can listen for `variant:changed`.

UI-controlling props: `variant` (`badge` default | `bar` | `text`), `showExactCount` (boolean, default true), `lowStockThreshold` (number, default 5; controls when it appears), `urgentThreshold` (number, default 3; colour escalation).
Data props: `variantId`, `quantity` (number; static preview value), `listenForEvents` (boolean, default false).
CSS vars: `--lx-inventory-urgent-color`, `--lx-inventory-low-color`, `--lx-inventory-ok-color` (state colours; fall back to the island defaults). Parts: `root, dot, message, bar-track, bar-fill`.
Fallback: none; the island hides itself when stock is high, so an empty child is correct.
Gotchas: set the three state vars in the section `<style>` when the brand palette has no red. Do not use for pre-order products.

### 2.12 DeliveryEstimate

"Order within Xh, arrives by <date>" line with optional free-shipping threshold. Category commerce. Hydrate `immediate`. Headless: no. Countdown updates each minute; returns nothing after cutoff.

UI-controlling props: `variant` (`inline` default | `card` | `banner`), `showCountdown` (boolean, default true).
Data props: `estimatedDays` (number, default 4), `cutoffHour` (number 0-23, default 14; store timezone, unconfirmed), `freeShippingThreshold` (number, minor units per example `5000`; unconfirmed currency handling).
CSS vars: `--lx-accent-color, --lx-text-color`. Parts: `root, icon, text, date`.
Fallback: one `<p>` "Ships in {{shipping.days}} business days".
Gotchas: `card` and `banner` variants paint their own surface, which violates the one-background rule; presets use `inline` only, or `card` with `[data-part="root"]{background:transparent;border:1px solid var(--lx-border-color)}`. The `icon` part is an island glyph; hide it when the page has no icon set. Keep it out of pages with international or variable shipping.

#### Shared notes for section 2

- **Fallback child.** A direct `data-lx-island-fallback` child inside
  `<lx-island>` may provide readable server-rendered content until the hosted
  island hydrates. Keep it simple, class-free or Tailwind-only (every class
  must compile), and free of interactive controls that could be mistaken for
  the island.
- **`animate` type.** Schema shows `boolean|boolean|string|string|string` for BuyBox, StickyBar, ProductCarousel; accepted string values are undocumented. Presets use booleans only.
- **Manifest evidence per island** (from `validate_page_workspace.py`): `{sectionId, name, schemaVersion, lifecycleStatus:"active", mode:"native"|"headless"}`, in source order.

## 3. Presets

Conventions: id is `<island-lowercase>/<intent>-<tone>`. Each preset is `props` (goes verbatim into the `<script type="application/json">`) plus optional `css` (goes into the section `<style>`, scoped by the island wrapper id `{{id}}`). Placeholders `{{...}}` are replaced by `/design-page` from catalog, brand and plan data. Colour strings use `var(--lx-*)` tokens; island `style.*` props are applied as inline styles so `var()` resolves (confirmed for hex, expected for `var()`; verify on first compile). Tones: `light` = page background, dark text; `dark` = inverted strip (`--lx-text-color` bg); `quiet` = no motion, no chrome; `editorial` = square corners, hairlines, letterspaced caps.

### 3.1 SiteHeader

**siteheader/sticky-light** - default PDP/landing header: inverted announcement strip, white nav with hairline. Use when the plan has an announcement message.
```json
{"props":{"sticky":true,"cartMode":"drawer","announcement":{"messages":["{{announcement.message_1}}","{{announcement.message_2}}"],"speed":5000,"dismissible":false,"backgroundColor":"var(--lx-text-color)","textColor":"var(--lx-bg-color)"},"navbar":{"logo":{"src":"{{brand.logo_url}}","alt":"{{brand.name}}","url":"/"},"links":"{{nav.links}}","style":{"bgColor":"var(--lx-bg-color)","textColor":"var(--lx-text-color)","accentColor":"var(--lx-accent-color)","height":"64px","logoHeight":"28px","maxWidth":"1280px","fontFamily":"var(--lx-font-body)","fontSize":"14px","fontWeight":"500","borderBottom":"1px solid var(--lx-border-color)","dropdownBg":"var(--lx-bg-color)","dropdownTextColor":"var(--lx-text-color)","mobileBg":"var(--lx-bg-color)","mobileTextColor":"var(--lx-text-color)"}}}}
```

**siteheader/transparent-dark** - nav floats over the plan's single full-bleed hero, text light, no announcement. Use only when the section directly below is that full-bleed moment.
```json
{"props":{"sticky":true,"transparent":true,"cartMode":"drawer","navbar":{"logo":{"src":"{{brand.logo_url_light}}","alt":"{{brand.name}}","url":"/"},"links":"{{nav.links}}","transparent":true,"style":{"textColor":"#ffffff","accentColor":"#ffffff","height":"72px","logoHeight":"28px","maxWidth":"1280px","fontSize":"14px","fontWeight":"500","borderBottom":"none","mobileBg":"var(--lx-text-color)","mobileTextColor":"var(--lx-bg-color)"}}}}
```

**siteheader/minimal-light** - non-sticky, no announcement, one CTA. Use for campaign landing pages with a single conversion goal.
```json
{"props":{"sticky":false,"cartMode":"link","cartUrl":"/cart","navbar":{"logo":{"text":"{{brand.name}}","url":"/"},"links":[{"label":"Shop","url":"{{nav.shop_url}}"}],"cta":{"label":"{{cta.text}}","url":"#buy"},"style":{"bgColor":"var(--lx-bg-color)","textColor":"var(--lx-text-color)","accentColor":"var(--lx-accent-color)","height":"72px","fontSize":"14px","fontWeight":"400","borderBottom":"none","maxWidth":"1280px"}}}}
```
```css
#{{id}} [data-part="cta"]{border-radius:var(--lx-radius,8px);padding:10px 18px}
```

### 3.2 Navbar

**navbar/sticky-light** - same look as siteheader/sticky-light without the strip. Use when no announcement, or when pairing with `announcementbar/*` that should scroll away.
```json
{"props":{"sticky":true,"cartMode":"drawer","logo":{"src":"{{brand.logo_url}}","alt":"{{brand.name}}","url":"/"},"links":"{{nav.links}}","cart":{"icon":"bag"},"style":{"bgColor":"var(--lx-bg-color)","textColor":"var(--lx-text-color)","accentColor":"var(--lx-accent-color)","height":"64px","logoHeight":"28px","maxWidth":"1280px","fontSize":"14px","fontWeight":"500","borderBottom":"1px solid var(--lx-border-color)","dropdownBg":"var(--lx-bg-color)","dropdownTextColor":"var(--lx-text-color)","mobileBg":"var(--lx-bg-color)","mobileTextColor":"var(--lx-text-color)"}}}
```

**navbar/transparent-dark** - light text over the hero, CTA pill. Use only above the plan's full-bleed moment.
```json
{"props":{"sticky":true,"transparent":true,"cartMode":"drawer","logo":{"src":"{{brand.logo_url_light}}","alt":"{{brand.name}}","url":"/"},"links":"{{nav.links}}","cta":{"label":"{{cta.text}}","url":"#buy"},"cart":{"icon":"bag","badgeColor":"#ffffff"},"style":{"textColor":"#ffffff","accentColor":"#ffffff","height":"72px","logoHeight":"28px","borderBottom":"none","mobileBg":"var(--lx-text-color)","mobileTextColor":"var(--lx-bg-color)"}}}
```
```css
#{{id}} [data-part="cta"]{background:#ffffff;color:var(--lx-text-color);border-radius:9999px;padding:10px 18px}
```

### 3.3 AnnouncementBar

**announcementbar/static-dark** - one message, inverted strip, no controls. Use for shipping or guarantee line.
```json
{"props":{"messages":["{{announcement.message_1}}"],"backgroundColor":"var(--lx-text-color)","textColor":"var(--lx-bg-color)","dismissible":false,"sticky":false}}
```
```css
#{{id}} [data-part="icon"]{display:none}
#{{id}} [data-part="text"]{font-size:13px;letter-spacing:.02em}
```

**announcementbar/rotating-accent** - 2-3 rotating promo lines on the accent colour. Use during a campaign window; pair with `navbar/sticky-light`.
```json
{"props":{"messages":["{{announcement.message_1}}","{{announcement.message_2}}","{{announcement.message_3}}"],"speed":5000,"backgroundColor":"var(--lx-accent-color)","textColor":"#ffffff","link":"{{announcement.url}}","dismissible":false,"sticky":false}}
```
```css
#{{id}} [data-part="icon"]{display:none}
```


### 3.4 ProductGallery

Shared flat-chrome CSS used by all three (flatten arrows, dots, no island surface):
```css
#{{id}}{--lx-product-gallery-bg:transparent;--lx-media-carousel-bg:transparent;--lx-media-carousel-arrow-bg:var(--lx-bg-color);--lx-media-carousel-arrow-border:1px solid var(--lx-border-color);--lx-media-carousel-arrow-color:var(--lx-text-color);--lx-media-carousel-arrow-hover-bg:var(--lx-bg-color);--lx-media-carousel-arrow-shadow:none;--lx-media-carousel-arrow-radius:9999px;--lx-media-carousel-arrow-size:40px;--lx-media-carousel-dot-color:var(--lx-border-color);--lx-media-carousel-dot-active-color:var(--lx-text-color);--lx-media-carousel-dot-active-scale:1;--lx-media-carousel-dot-shadow:none;--lx-product-gallery-focus-width:2px;--lx-media-lightbox-backdrop:rgba(0,0,0,.92);--lx-media-lightbox-close-bg:transparent;--lx-media-lightbox-close-border:1px solid rgba(255,255,255,.4);--lx-media-lightbox-close-color:#ffffff}
```

**productgallery/rail-bottom-light** - main image with thumbnail strip below, rounded, lightbox. Default PDP gallery.
```json
{"props":{"media":"{{product.media}}","layout":"horizontal","thumbPosition":"bottom","mobileLayout":"swipe","transition":"fade","objectFit":"cover","enableLightbox":true,"autoplay":false,"listenForVariant":false}}
```
```css
#{{id}}{--lx-product-gallery-radius:var(--lx-radius,12px);--lx-product-gallery-gap:12px;--lx-product-gallery-mobile-ratio:1/1}
#{{id}} [data-part="thumbnail"]{border:1px solid var(--lx-border-color);border-radius:var(--lx-radius,8px)}
```

**productgallery/rail-left-editorial** - vertical rail on the left, square corners, `contain` for packshots, no transition. Use for fashion or premium goods with studio imagery.
```json
{"props":{"media":"{{product.media}}","layout":"vertical","thumbPosition":"left","mobileLayout":"swipe","transition":"none","objectFit":"contain","enableLightbox":true,"autoplay":false}}
```
```css
#{{id}}{--lx-product-gallery-radius:0;--lx-media-carousel-radius:0;--lx-media-carousel-arrow-radius:0;--lx-product-gallery-gap:16px;--lx-product-gallery-border:1px solid var(--lx-border-color)}
#{{id}} [data-part="thumbnail"]{border-radius:0;border:1px solid transparent}
```

**productgallery/stacked-quiet** - all images stacked full-width on desktop, swipe rail on mobile, no lightbox, no motion. Use for long-scroll editorial PDPs where the BuyBox is sticky beside the media.
```json
{"props":{"media":"{{product.media}}","layout":"stacked","mobileLayout":"swipe","transition":"none","objectFit":"cover","enableLightbox":false,"autoplay":false}}
```
```css
#{{id}}{--lx-product-gallery-radius:var(--lx-radius,8px);--lx-product-gallery-gap:8px;--lx-product-gallery-stacked-ratio:4/5;--lx-product-gallery-mobile-peek:24px}
```

### 3.5 ProductHero

**producthero/split-rail-light** - hero beside BuyBox, thumbnails under the image, arrows inside frame, capped height. Default premium PDP.
```json
{"props":{"images":"{{product.hero_images}}","layout":"splitLeft","thumbnails":"rail","thumbnailPosition":"bottom","navigation":"arrows","aspectRatio":"4:5","maxHeight":"640px","transition":"fade","autoplay":false,"hoverAdvance":false}}
```
```css
#{{id}}{--lx-hero-bg:transparent;--lx-hero-radius:var(--lx-radius,12px);--lx-hero-thumb-radius:var(--lx-radius,8px);--lx-hero-thumb-size:64px;--lx-hero-thumb-gap:8px;--lx-hero-arrow-bg:var(--lx-bg-color);--lx-hero-arrow-size:40px;--lx-hero-arrow-offset:12px;--lx-hero-transition-duration:300ms}
#{{id}} [data-part="thumbnail"]{border:1px solid var(--lx-border-color)}
```

**producthero/stacked-dots-quiet** - square image, dots only, no arrows, mobile-first. Use when the product has 2-4 images and the page is copy-led.
```json
{"props":{"images":"{{product.hero_images}}","layout":"stacked","thumbnails":"dots","navigation":"none","showIndicators":true,"aspectRatio":"1:1","maxHeight":"560px","transition":"fade","autoplay":false,"hoverAdvance":false}}
```
```css
#{{id}}{--lx-hero-bg:transparent;--lx-hero-radius:var(--lx-radius,12px);--lx-hero-transition-duration:250ms}
#{{id}} [data-part="dot"]{background:var(--lx-border-color)}
```

**producthero/fullheight-sharp-dark** - full-height, square corners, floating arrows on dark chips, no thumbnails. Use only as the plan's one full-bleed moment (pairs with `siteheader/transparent-dark`).
```json
{"props":{"images":"{{product.hero_images}}","layout":"fullHeight","thumbnails":"none","navigation":"floatingArrows","aspectRatio":"3:4","maxHeight":"85vh","transition":"slide","autoplay":false,"hoverAdvance":false}}
```
```css
#{{id}}{--lx-hero-bg:var(--lx-text-color);--lx-hero-radius:0;--lx-hero-arrow-bg:rgba(0,0,0,.6);--lx-hero-arrow-size:44px;--lx-hero-arrow-offset:16px;--lx-hero-transition-duration:400ms}
```

### 3.6 BuyBox

Data block shared by all BuyBox presets: `"product":{"title":"{{product.title}}","price":"{{product.price}}","compareAtPrice":"{{product.compare_at_price}}","variants":"{{product.variants}}"}` where `{{product.variants}}` expands to `[{"id":"gid://shopify/ProductVariant/...","title":"...","price":"...","available":true}]`.

**buybox/default-light** - variant buttons, quantity, accent CTA with the page radius, no trust badges (page owns its icons). Default PDP.
```json
{"props":{"product":"{{product}}","variant":"default","ctaText":"{{cta.text}}","showPrice":true,"showVariantSelector":true,"showTrustBadges":false,"animate":true,"buttonStyle":{"borderRadius":"var(--lx-radius,8px)","padding":"16px 24px","fontSize":"15px"}}}
```
```css
#{{id}} [data-part="variant-btn"]{border:1px solid var(--lx-border-color);border-radius:var(--lx-radius,8px);background:transparent;color:var(--lx-text-color)}
#{{id}} [data-part="qty"],#{{id}} [data-part="qty-btn"]{border-color:var(--lx-border-color);border-radius:var(--lx-radius,8px)}
```

**buybox/compact-dark** - single-variant product, no quantity, black square CTA with letterspaced label. Use in bundles, upsell rows, or sticky sidebars.
```json
{"props":{"product":"{{product}}","variant":"compact","ctaText":"{{cta.text}}","showPrice":true,"showTrustBadges":false,"animate":false,"buttonStyle":{"borderRadius":"0","padding":"18px 28px","fontSize":"13px"}}}
```
```css
#{{id}} [data-part="cta"]{background:var(--lx-text-color);color:var(--lx-bg-color);text-transform:uppercase;letter-spacing:.08em;font-weight:600}
```

**buybox/expanded-editorial** - expanded layout, pill CTA and pill variant buttons; trust badges on only when the page has no other icon set. Use for premium PDPs with a long BuyBox column.
```json
{"props":{"product":"{{product}}","variant":"expanded","ctaText":"{{cta.text}}","showPrice":true,"showVariantSelector":true,"showTrustBadges":"{{page.icon_set == 'none'}}","animate":true,"buttonStyle":{"borderRadius":"9999px","padding":"18px 32px","fontSize":"15px"}}}
```
```css
#{{id}} [data-part="variant-btn"]{border-radius:9999px;border:1px solid var(--lx-border-color);background:transparent;padding:8px 16px;font-size:13px}
#{{id}} [data-part="trust-badges"]{opacity:.8;font-size:13px}
```

### 3.7 StickyBar

**stickybar/product-light** - page-coloured bar, hairline top, accent CTA, appears after the BuyBox section. Default PDP.
```json
{"props":{"product":{"title":"{{product.title}}","price":"{{product.price}}","compareAtPrice":"{{product.compare_at_price}}","image":"{{product.image_thumb}}","variantId":"{{product.default_variant_id}}"},"cta":"{{cta.text}}","showAfter":"#{{sections.buybox.id}}","animate":true}}
```
```css
#{{id}} [data-part="bar"]{background:var(--lx-bg-color);color:var(--lx-text-color);border-top:1px solid var(--lx-border-color);box-shadow:none}
#{{id}} [data-part="cta"]{border-radius:var(--lx-radius,8px)}
#{{id}} [data-part="product-image"]{border-radius:var(--lx-radius,6px)}
```

**stickybar/product-dark** - inverted bar, no image, no animation. Use on quiet or editorial pages.
```json
{"props":{"product":{"title":"{{product.title}}","price":"{{product.price}}","variantId":"{{product.default_variant_id}}"},"cta":"{{cta.text}}","showAfter":"#{{sections.buybox.id}}","animate":false}}
```
```css
#{{id}} [data-part="bar"]{background:var(--lx-text-color);color:var(--lx-bg-color);box-shadow:none}
#{{id}} [data-part="cta"]{background:var(--lx-bg-color);color:var(--lx-text-color);border-radius:0}
#{{id}} [data-part="product-price"]{color:var(--lx-bg-color);opacity:.8}
```

**stickybar/collection-light** - collection/campaign destination instead of add-to-cart. Use on listicle, gift-guide and collection landers.
```json
{"props":{"collection":{"label":"{{collection.cta_label}}","url":"{{collection.url}}","subtitle":"{{collection.subtitle}}"},"showAfter":"#{{sections.first_content.id}}","animate":true}}
```
```css
#{{id}} [data-part="bar"]{background:var(--lx-bg-color);border-top:1px solid var(--lx-border-color);box-shadow:none}
```

### 3.8 ProductCarousel

Shared flat-chrome CSS (same arrow/dot variables as the gallery):
```css
#{{id}}{--lx-media-carousel-arrow-bg:var(--lx-bg-color);--lx-media-carousel-arrow-border:1px solid var(--lx-border-color);--lx-media-carousel-arrow-color:var(--lx-text-color);--lx-media-carousel-arrow-shadow:none;--lx-media-carousel-arrow-radius:9999px;--lx-media-carousel-dot-color:var(--lx-border-color);--lx-media-carousel-dot-active-color:var(--lx-text-color);--lx-media-carousel-dot-shadow:none;--lx-media-carousel-radius:var(--lx-radius,8px)}
#{{id}} [data-part="card-wrapper"]{background:transparent;border:1px solid var(--lx-border-color);border-radius:var(--lx-radius,8px);box-shadow:none;transition:none}
#{{id}} [data-part="badge"]{border-radius:var(--lx-radius,4px);background:var(--lx-text-color);color:var(--lx-bg-color)}
```

**productcarousel/cards-quiet** - plain cards, no actions, no hover media, no entry animation; section owns the h2. Default "You may also like".
```json
{"props":{"products":"{{related.products}}","cardVariant":"default","showQuickAdd":false,"showLearnMore":false,"showWishlist":false,"showQuickView":false,"hoverAdvance":false,"mediaTransition":"none","animate":false}}
```

**productcarousel/cards-quickadd-light** - adds the quick-add button (requires `head.use_cart_v2:true`), fade media swap, entry fade. Use on collection and bundle pages.
```json
{"props":{"products":"{{related.products}}","cardVariant":"default","showQuickAdd":true,"showLearnMore":false,"showWishlist":false,"showQuickView":false,"hoverAdvance":false,"mediaTransition":"fade","animate":true}}
```
```css
#{{id}} [data-part="quick-add"]{border-radius:var(--lx-radius,8px);background:var(--lx-accent-color);color:#ffffff}
```

**productcarousel/rows-compact** - list rows (image, title, price) for sidebars and "complete the set". Use with 3-5 products.
```json
{"props":{"products":"{{related.products}}","cardVariant":"compactRows","showQuickAdd":false,"showLearnMore":false,"hoverAdvance":false,"mediaTransition":"none","animate":false}}
```
```css
#{{id}} [data-part="row"]{border-bottom:1px solid var(--lx-border-color);padding:12px 0}
#{{id}} [data-part="row-image"]{border-radius:var(--lx-radius,6px)}
```

### 3.9 Footer

**footer/columns-dark** - inverted footer, 3-4 link columns, text social links (no glyphs), no newsletter. Default.
```json
{"props":{"logo":{"src":"{{brand.logo_url}}","alt":"{{brand.name}}"},"tagline":"{{brand.tagline}}","columns":"{{footer.columns}}","copyright":"{{brand.copyright}}","borderStyle":"none","tileLayout":false,"style":{"layout":"columns","bgColor":"var(--lx-text-color)","textColor":"var(--lx-bg-color)","linkColor":"var(--lx-bg-color)","linkHoverColor":"var(--lx-accent-color)","headingColor":"var(--lx-bg-color)","accentColor":"var(--lx-accent-color)","borderColor":"rgba(255,255,255,.15)","fontFamily":"var(--lx-font-body)","fontSize":"14px","padding":"64px 0 32px","maxWidth":"1280px","logoHeight":"24px","logoFilter":"invert(1)"}}}
```

**footer/simple-light** - one row of links, hairline top, page background. Use on campaign landers.
```json
{"props":{"logo":{"src":"{{brand.logo_url}}","alt":"{{brand.name}}"},"links":"{{footer.links}}","copyright":"{{brand.copyright}}","borderStyle":"solid","style":{"layout":"simple","bgColor":"var(--lx-bg-color)","textColor":"var(--lx-text-muted)","linkColor":"var(--lx-text-color)","linkHoverColor":"var(--lx-accent-color)","borderColor":"var(--lx-border-color)","fontSize":"13px","padding":"32px 0","maxWidth":"1280px","logoHeight":"20px"}}}
```

**footer/newsletter-split-light** - newsletter on one side, columns on the other, page background with hairline. Use when the plan names email capture as a goal and no EmailCapture island is on the page.
```json
{"props":{"logo":{"src":"{{brand.logo_url}}","alt":"{{brand.name}}"},"columns":"{{footer.columns}}","newsletter":{"heading":"{{newsletter.heading}}","placeholder":"Email address","buttonText":"Subscribe"},"successMessage":"Thanks, you are on the list.","copyright":"{{brand.copyright}}","borderStyle":"solid","style":{"layout":"newsletterSplit","bgColor":"var(--lx-bg-color)","textColor":"var(--lx-text-color)","linkColor":"var(--lx-text-color)","linkHoverColor":"var(--lx-accent-color)","headingColor":"var(--lx-text-color)","accentColor":"var(--lx-accent-color)","borderColor":"var(--lx-border-color)","fontSize":"14px","padding":"64px 0 32px","maxWidth":"1280px","logoHeight":"24px"}}}
```
```css
#{{id}} [data-part="newsletter"] input{border:1px solid var(--lx-border-color);border-radius:var(--lx-radius,8px);background:transparent}
#{{id}} [data-part="newsletter"] button{border-radius:var(--lx-radius,8px)}
```

### 3.10 ReviewCarousel

Shared flat card CSS:
```css
#{{id}} [data-part="card"]{background:transparent;border:1px solid var(--lx-border-color);border-radius:var(--lx-radius,12px);box-shadow:none}
#{{id}} [data-part="nav-prev"],#{{id}} [data-part="nav-next"]{background:var(--lx-bg-color);border:1px solid var(--lx-border-color);color:var(--lx-text-color);box-shadow:none}
#{{id}} [data-part="dot"]{background:var(--lx-border-color)}
```

**reviewcarousel/grid-flat** - all reviews visible, no motion. Default when 3-6 reviews.
```json
{"props":{"collectionId":"{{reviews.collection_id}}","minRating":4,"pageSize":8,"variant":"grid","autoplay":false}}
```

**reviewcarousel/single-quiet** - one card at a time, manual arrows, no autoplay. Use when review bodies are long.
```json
{"props":{"collectionId":"{{reviews.collection_id}}","minRating":4,"pageSize":6,"variant":"default","autoplay":false,"interval":6000}}
```

**reviewcarousel/strip-compact** - short strip of one-line reviews with slow rotation. Use near the BuyBox as a proof line, bodies under 60 chars.
```json
{"props":{"collectionId":"{{reviews.collection_id}}","minRating":4,"pageSize":6,"variant":"compact","autoplay":true,"interval":6000}}
```
```css
#{{id}} [data-part="verified"]{display:none}
```

### 3.11 InventoryIndicator

**inventoryindicator/text-quiet** - inline sentence under the price, shows only below 10 units. Default.
```json
{"props":{"variantId":"{{product.default_variant_id}}","quantity":"{{product.inventory_quantity}}","variant":"text","showExactCount":true,"lowStockThreshold":10,"urgentThreshold":3,"listenForEvents":true}}
```
```css
#{{id}} [data-part="message"]{color:var(--lx-text-muted);font-size:13px}
#{{id}} [data-part="dot"]{background:var(--lx-accent-color)}
```

**inventoryindicator/bar-accent** - thin progress bar in the accent colour. Use for drops and limited runs.
```json
{"props":{"variantId":"{{product.default_variant_id}}","quantity":"{{product.inventory_quantity}}","variant":"bar","showExactCount":true,"lowStockThreshold":25,"urgentThreshold":5,"listenForEvents":true}}
```
```css
#{{id}} [data-part="bar-track"]{background:var(--lx-border-color);height:4px;border-radius:9999px}
#{{id}} [data-part="bar-fill"]{background:var(--lx-accent-color);border-radius:9999px}
```

**inventoryindicator/badge-outline** - outlined pill, no exact count. Use when stock numbers should stay private.
```json
{"props":{"variantId":"{{product.default_variant_id}}","quantity":"{{product.inventory_quantity}}","variant":"badge","showExactCount":false,"lowStockThreshold":5,"urgentThreshold":2,"listenForEvents":true}}
```
```css
#{{id}} [data-part="root"]{background:transparent;border:1px solid var(--lx-border-color);color:var(--lx-text-color);border-radius:9999px;padding:4px 10px;font-size:12px}
```

### 3.12 DeliveryEstimate

**deliveryestimate/inline-quiet** - one muted line, no icon, countdown on. Default under the BuyBox CTA.
```json
{"props":{"variant":"inline","estimatedDays":"{{shipping.days}}","cutoffHour":"{{shipping.cutoff_hour}}","showCountdown":true}}
```
```css
#{{id}} [data-part="icon"]{display:none}
#{{id}} [data-part="text"]{color:var(--lx-text-muted);font-size:13px}
#{{id}} [data-part="date"]{color:var(--lx-text-color);font-weight:600}
```

**deliveryestimate/card-outline** - card variant with its surface removed, hairline border, free-shipping threshold. Use in a "shipping and returns" block.
```json
{"props":{"variant":"card","estimatedDays":"{{shipping.days}}","cutoffHour":"{{shipping.cutoff_hour}}","showCountdown":true,"freeShippingThreshold":"{{shipping.free_threshold_minor}}"}}
```
```css
#{{id}} [data-part="root"]{background:transparent;border:1px solid var(--lx-border-color);border-radius:var(--lx-radius,12px);box-shadow:none}
#{{id}} [data-part="icon"]{display:none}
```

`banner` variant intentionally has no preset: it paints a full-width surface, which breaks the one-background rule.

## 4. Preset system proposal

Goal: a plan says `BuyBox: preset buybox/compact-dark`; design applies exact props and CSS; compile and the validator can prove it. Smallest change that does this: one reference file, one line in `page-plan.md` per section, one field per manifest island. No new tool, no runtime change.

### 4.1 File location and shape

`skills/storefront-engine/references/island-presets.md` (loaded by `/plan-page` for `Preset:` ids and by `/design-page` next to `design-rules.md`). One `##` per island, one `###` per preset id, each with a single fenced `json` block containing the whole preset entry (props + css + metadata). Markdown keeps it human-reviewable; the fenced block is machine-extractable with the same regex the validator already uses for `<script type="application/json">`.

Optionally mirror as `skills/design-page/assets/island-presets.json` (array of entries) if a script needs to load it; generate it from the `.md`, do not hand-maintain two copies.

### 4.2 Preset entry schema (minimal JSON Schema)

```json
{"$schema":"https://json-schema.org/draft/2020-12/schema","title":"LexsisIslandPreset","type":"object","required":["id","island","schemaVersion","props"],"additionalProperties":false,
 "properties":{
  "id":{"type":"string","pattern":"^[a-z]+/[a-z0-9]+(-[a-z0-9]+)+$","description":"<island-lowercase>/<intent>-<tone>"},
  "island":{"type":"string","description":"Exact runtime island name, e.g. BuyBox"},
  "schemaVersion":{"type":"string","description":"island_schema version the preset was verified against, e.g. 5.1.0"},
  "hydrate":{"type":"string","enum":["immediate","visible","idle","interaction"]},
  "mode":{"type":"string","enum":["native","headless"],"default":"native"},
  "props":{"type":"object","description":"Verbatim island props; string values may contain {{placeholders}}"},
  "css":{"type":"string","description":"Section CSS scoped with #{{id}}; only [data-part] selectors and --lx-* variables"},
  "requires":{"type":"object","properties":{"cartV2":{"type":"boolean"},"iconSet":{"type":"string","enum":["none","page"]},"fullBleedMoment":{"type":"boolean"},"minItems":{"type":"integer"}}},
  "placeholders":{"type":"array","items":{"type":"string"},"description":"Every {{token}} used, so design can check bindings"},
  "use":{"type":"string","description":"One line: when to pick it"},
  "houseRules":{"type":"array","items":{"type":"string"},"description":"Rules this preset was checked against: no-emoji, no-gradient, one-background, one-icon-set, no-motion-effects"}
 }}
```

Example entry:
```json
{"id":"buybox/compact-dark","island":"BuyBox","schemaVersion":"5.1.0","hydrate":"immediate","mode":"native","props":{"product":"{{product}}","variant":"compact","ctaText":"{{cta.text}}","showTrustBadges":false,"animate":false,"buttonStyle":{"borderRadius":"0","padding":"18px 28px","fontSize":"13px"}},"css":"#{{id}} [data-part=\"cta\"]{background:var(--lx-text-color);color:var(--lx-bg-color);text-transform:uppercase;letter-spacing:.08em}","requires":{"cartV2":true},"placeholders":["product","cta.text"],"use":"Single-variant product in bundles, upsell rows, sticky sidebars.","houseRules":["no-emoji","no-gradient","one-background","one-icon-set","no-motion-effects"]}
```

### 4.3 How `/plan-page` selects

`plan-page/SKILL.md` today forbids island names and props in the plan. Keep that for props, relax it for preset ids: a preset id is a *design intent token*, not implementation. Add one optional line per section in `page-plan.md`:

```text
## Sections
3. Buy
   Purpose: convert; primary CTA.
   Preset: buybox/compact-dark, stickybar/product-dark
```

Rules: ids must exist in `island-presets.md`; the plan lists at most one preset per island role; the plan's "Design direction" block names the tone once (`light`, `dark`, `quiet`, `editorial`) and every chosen preset's tone must match it or be listed as an explicit exception. Header and footer presets are picked in the "Design direction" block, not per section.

### 4.4 How `/design-page` applies and overrides

1. Read `island-presets.md`; for each `Preset:` line resolve the entry. Unknown id = stop and ask (return `PRESET_NOT_FOUND`).
2. Check `requires`: `cartV2` -> `head.use_cart_v2:true`; `iconSet:"none"` -> the page uses no other icons; `fullBleedMoment` -> the plan names one; `minItems` -> enough products/reviews. Fail = pick the sibling preset with the same intent or return `PRESET_REQUIREMENT_UNMET`.
3. Emit `<lx-island name="{{island}}" id="{{sectionId}}-{{islandLower}}" hydrate="{{hydrate}}">` with `props` after placeholder substitution, and append `css` (with `#{{id}}` substituted) to that section's `<style>`.
4. Overrides: a section may add `Preset override:` lines in the plan or the designer may deviate; every deviation is recorded in the manifest as `islands[].presetOverrides` (JSON merge patch against the preset props) and in `page-plan.md` under "Design direction". No silent edits to preset props.
5. Never edit a preset in place for one page; add a new id if a new look is needed.

### 4.5 How compile validates

- `lexsis_pages compile` remains the authority for prop shape; presets are pre-validated once per `schemaVersion`, so a compile error on a preset-applied island means either an override or a schema drift. Log the island `version` from `island_schema` and fail fast when it differs from `preset.schemaVersion`.
- Extend `validate_page_workspace.py` (design phase) with three cheap checks: (a) every `islands[].preset` id exists in the preset file; (b) props in source equal preset props after substitution plus recorded `presetOverrides` (deep-equal after removing `{{...}}`-bound keys); (c) preset `css` text is present in the section's `<style>`. Emit `island_preset_mismatch` as a blocking finding in `SOURCE_PHASES`.
- House-rule checks already in `design-rules.md` (emoji grep, distinct backgrounds) run unchanged; presets are pre-checked against them, and `houseRules` records which.

### 4.6 Manifest

`islands[]` already carries `{sectionId, name, schemaVersion, lifecycleStatus, mode}`. Add:

```json
{"sectionId":"buy","name":"BuyBox","schemaVersion":"5.1.0","lifecycleStatus":"active","mode":"native","preset":"buybox/compact-dark","presetOverrides":{"ctaText":"Add to bag"}}
```

`preset` is a string or `null` (custom composition, rationale in `page-plan.md`). `presetOverrides` omitted when empty. `design.stylePack` stays; a preset set is not a style pack, but when a page uses presets of a single tone, record `design.presetTone`.

Source: internal island-preset audit (2026-09-10).

---

# Generation Protocol — How Pages Are Built

> House rules in `storefront-engine/references/design-rules.md` override every example below.
> Examples show structure and copy intent; their styling (gradients, hover transforms,
> uppercase labels, pills, emoji, section fills) is illustrative and must not be copied.
> Where an example conflicts with a house rule, the rule wins.

> This is the canonical reference for how AI agents generate storefront pages using the Lexsis AI MCP. All operational skills reference this protocol.

> **Compiled runtime reference:** any `data-island` or `data-props` snippets in
> storage-format examples below are renderer output, not page source. New pages
> use `<lx-island>` with a JSON script child as defined in `source-format.md`.

---

## MCP Workflow (Correct Order)

```
1. Read the selected store/theme from `work/storefront/setup/setup.json`
2. Read its saved brand design and exact theme CSS
3. Read current products, variants, assets, permissions, and island schemas
4. Require a valid page plan and a completed design asset decision, or record
   explicit skips
5. Promote the approved canonical source with final production assets
6. lexsis_pages → compile
7. lexsis_page_create → create draft
8. Host-agent responsive and commerce verification
```

Setup provides slow-changing design context. Commerce, assets, schemas,
permissions, analytics, and remote versions are always read live.

For a first draft explicitly routed through `/build` or
`/build-with-template`, create the minimum plan and source artifacts, record
`plan-page` and `design-page` in `workflow.skippedSkills`, compile once with at
most one targeted repair, and create with `publish:false`. Return
`DRAFT_CREATED` before critique, hosted QA, commerce QA, or hash
reconciliation. Those checks belong to a later `/generate` upgrade.

An optional visual concept inside `/design-page` uses existing Lexsis image
generation and remains design evidence only. Never insert the concept image
into page source or treat generated text inside it as factual copy.

> **Brand kit ↔ design.md precedence**: exact tokens normally come from the
> saved theme, while design.md supplies style philosophy and component guidance.
> Before authoring, compare any explicit `NEVER`, `must`, or `non-negotiable`
> design rule with the matching token. If they directly contradict each other,
> return `THEME_CONTEXT_CONFLICT` with both values and stop using that property
> until the theme or guide is corrected. Never silently choose a
> property-by-property winner or invent a blended rule.

> **Documentation precedence**: live MCP contracts win over bundled docs. For
> islands, use `vibe://schema/island/{name}` (or `lexsis_design` action
> `island_schema`) first, bundled
> `references/islands/{slug}/schema.json` second, and prose/layout examples
> last. Never merge prop shapes from different versions.

> **Authoring format**: write pages in the HTML-native **source format** (`source-format.md`) — plain HTML sections delimited by `<!-- section: id -->`, islands as `<lx-island name>` with a JSON `<script>` child. The compiler produces VibePage JSON and does all escaping.

> **Local source**: follow `source-artifact-workflow.md`.
> `lexsis-source.html` is the canonical editable visual and production
> artifact. It is compiled and saved as one unpublished hosted draft during
> `/design-page`; `/generate` reuses that draft for deeper QA.

> **Templates**: search before drafting. Retrieve templates you intend to edit
> with `lexsis_design` action `get_section`. Each returned `source` is ready for
> editing and compiling. `format: "compiled_reference"` is renderer output and cannot be passed directly to
> source-authoring tools.

---

## Two-Phase Generation (Fast Iteration Pattern)

### Phase 4a — Draft Source HTML

Generate the FULL page as source-format HTML first:
- Plain HTML + Tailwind, sections delimited by `<!-- section: id -->`
- Focus on layout, visual hierarchy, spacing, typography
- Write all copy naturally — apostrophes/quotes need no escaping
- Set all colors via `--lx-*` CSS variables (from `lexsis_brand.compile_theme`)
- Mobile-first responsive; use shared keyframes, `data-behavior="gsap-*"`
  presets, or `application/lexsis-motion` only for the plan-named motion moment
- Islands go in directly as `<lx-island name="BuyBox">` with a JSON `<script>` child — use `lexsis_design` action `island_schema` for exact prop shapes

### Phase 4b — Compile & Fix

Run `lexsis_pages` action `compile`:
- Returns the compiled VibePage + compile issues + publish validation
- Fix reported issues in the source (unknown islands, bad props, missing hooks) and re-compile
- Require `missing_candidates` to be empty
- When clean, `lexsis_page_create` action `create` persists a draft; retrieve
  source later with `lexsis_pages` action `source`

### Why Two-Phase?
- Compile is instant and deterministic — validation before anything persists
- The hosted draft is the one renderer source of truth
- Separates source compatibility from hosted visual and commerce QA
- Escaping failures are impossible: the compiler, not the model, writes `data-props`

---

## VibePage JSON Structure (storage format — compiler output)

> You do not write this by hand. The source-format compiler produces it as the storage and rendering format.

```json
{
  "head": {
    "title": "Page Title — Brand Name",
    "fonts": ["https://fonts.googleapis.com/css2?family=..."],
    "use_cart_v2": true
  },
  "theme_css": ":root { --lx-accent-color: #4F46E5; --lx-font-heading: 'Playfair Display', serif; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section>...</section>",
      "css": "...",
      "js": "...",
      "motion": [{ "version": 1, "id": "hero-object", "capabilities": ["three"] }]
    }
  ]
}
```

### Rules
- **Tailwind CSS** in HTML class attributes. The compiler emits one
  deterministic `compiled_page_css`; there is no runtime Tailwind CDN.
- **CSS Variables** (`--lx-*`) for all brand colors/fonts — set in `theme_css` (generate with `lexsis_brand.compile_theme`)
- **Islands** compile to `data-island="Name"` + `data-props='JSON'` attributes (in source format, write `<lx-island>` instead)
- **Section IDs** must be unique, kebab-case: "hero", "social-proof", "faq"
- **Managed motion** is authored as
  `<script type="application/lexsis-motion">` and compiled into `motion[]`.
  Read `animation-system.md`; never hand-write the compiled object.
- **Section JS** is compatibility-only. It is lifecycle-wrapped and cannot use
  global DOM queries, unmanaged observers/loops, programmatic clicks, fetch,
  eval, or storage.
- **Shared keyframes** already loaded: fadeUp, fadeIn, scaleIn, slideInLeft,
  slideInRight, marquee, float, shimmer, wordFade, pulseRing. GSAP presets and
  managed custom motion are available, never by default.
- **No @import, no external URLs in CSS**. Page `scripts[]` is for approved
  integrations, not GSAP, Three.js, Lottie, or Rive.

### Available CSS Variables (override in theme_css)
| Variable | Default | Purpose |
|----------|---------|---------|
| `--lx-accent-color` | #5055aa | Primary CTA color |
| `--lx-accent-color-hover` | #4045aa | Hover state |
| `--lx-text-color` | #1a1a2e | Primary text |
| `--lx-text-muted` | #6b7280 | Secondary text |
| `--lx-bg-color` | #ffffff | Page background |
| `--lx-bg-surface` | #ffffff | Card backgrounds |
| `--lx-border-color` | #e5e7eb | Borders/dividers |
| `--lx-font-heading` | system-ui | Heading font |
| `--lx-font-body` | system-ui | Body font |
| `--lx-surface-alt` | #f9fafb | Component tint (chips, hover fills, selected state); never a section background |
| `--lx-lavender` | #c9b8e8 | Secondary accent |
| `--lx-teal` | #5bc8c0 | Tertiary accent |

---

## Visual Verification (Critical Step)

After `lexsis_page_create` returns a `preview_url`, always verify visually.
Use the calling agent's browser capability; Lexsis does not create a shared
Playwright session or browser pool.

Test 390px, 768px, and 1280px. Use screenshots when available. Otherwise use
computed styles, DOM bounds, scroll dimensions, image completeness, hover
state, and console inspection. If the host has no browser capability, return
the preview URL and state that visual QA remains.

### What to Check
- [ ] Hero section visible above fold (no scroll needed for headline + CTA)
- [ ] Brand colors applied (not default purple)
- [ ] Fonts loading (not system fallback)
- [ ] Images rendering (not broken placeholders)
- [ ] Mobile layout not broken (stack columns, readable text)
- [ ] Islands hydrated (BuyBox shows product, not empty div)
- [ ] CTA buttons have proper contrast (WCAG AA: 4.5:1 min)
- [ ] No horizontal scroll on mobile
- [ ] Section spacing consistent (not cramped or overly spaced)

---

## Island Integration Reference

Islands are React components that hydrate client-side. They handle interactive commerce functionality.

### How to Embed
```html
<lx-island name="IslandName">
  <script type="application/json">{ "key": "value" }</script>
</lx-island>
```

### Key Islands by Use Case

The catalog is the source of truth: read `lexsis_design` action `islands`, then
`island_schema` for the one you pick. Prop shapes below are indicative only.

| Need | Island | Note |
|------|--------|------|
| Add to cart | BuyBox | the only commerce island for purchase; never a custom button |
| Product images | ProductGallery, or ProductHero for a split PDP hero | layout by image count |
| Cart | none on the page | Cart V2 through `head.use_cart_v2` and the cart profile; CartDrawer is deprecated |
| Reviews | ReviewCarousel or ReviewList | bound to a real collection or product ids from the Proof ledger |
| FAQ accordion | none | native `<details>`/`<summary>`; the FAQ island is deprecated |
| Email capture | EmailCapture | consent copy is authored HTML beside it |
| Announcement | AnnouncementBar | one message; paired with Navbar, not SiteHeader |
| Navigation | Navbar or SiteHeader, plus MobileMenu | full-nav page types only |
| Footer | Footer | last section |
| Product grid | none | a card composition per `references/product-grid.md` with QuickAdd, or FeaturedCollectionStage for a group |
| Trust badges | none | static HTML with the issuer text from the Proof ledger |
| Countdown | CountdownTimer | required prop is `endDate`; only with a verified end |
| Recent-purchase popup | none, ever | fabricated proof (`references/proof/proof-ledger.md`) |

### Prop Data Sources
- Product data → `lexsis_catalog` action `get` or `list`
- Navigation → `lexsis_brand` action `navigation`
- Reviews → `lexsis_catalog` actions `reviews_status`, `review_collections`,
  `reviews` (the plan's Proof sources line); island props `collectionId` or
  `productIds` plus `minRating`, never `reviewsEndpoint`; never invent
  reviewers, ratings, locations, or counts
- Brand tokens → `lexsis_brand` action `brand_kit` or `lexsis_brand.get_theme`

### Locale and Market Rules

- Derive currency, tax language, shipping promises, and payment methods from
  the selected store. Do not default every page to USD or to India.
- For India storefronts, format INR with `₹`, use pincode-aware delivery
  language, and mention GST, COD, or UPI only when store data confirms them.
- Localize names, units, dates, and cities without fabricating regional proof.

---

## Deprecated Tools (DO NOT USE)

These tools appeared in older skill versions but are no longer available:

| Removed | Replacement |
|---------|-------------|
| `get_theme_json` | `lexsis_brand` action `brand_kit` (includes theme data) |
| `provision_store` | Handle via onboarding flow, not page generation |
| `extract_brand_design` / `capture_design_source` / `list_design_sources` | No replacement — no MCP tool for reference-URL design extraction currently exists |
| `lexsis_template_library.search_sections` returning `html`/`css`/`js` inline | Search is metadata-only now; call `lexsis_design.get_section({ ids })` for compile-ready source |

`lexsis_design.islands` and `lexsis_design.island_schema` remain active tools — use them for island discovery and schema lookups, alongside the `vibe://catalog/islands` resource.

---

## Quality Gates (Before Publishing)

1. `lexsis_pages` action `compile`
2. `lexsis_pages` action `integrity`
3. Host-agent visual verification

If compile fails, fix source and retry. If integrity warns, assess and fix.
If visual QA fails, update local source, compile the complete page, patch only
changed sections with `expected_version`, update the manifest, then repeat QA.

---

# Source Format — HTML-Native Page Authoring (V2)

> House rules in `storefront-engine/references/design-rules.md` override every example below.
> Examples show structure and copy intent; their styling (gradients, hover transforms,
> uppercase labels, pills, emoji, section fills) is illustrative and must not be copied.
> Where an example conflicts with a house rule, the rule wins.

> **This is the preferred way to author pages.** Write plain HTML with
> `<lx-island>` elements; `lexsis_pages` action `compile` and
> `lexsis_page_create` action `create` compile it deterministically. Never
> hand-write `data-island` / `data-props` or escape HTML into JSON strings.

For durable page work, store this format in `lexsis-source.html` and follow
`source-artifact-workflow.md`. The design workflow authors that same file,
dry-run compiles it with `page-theme.css`, and hydrates the compiled result
through the exported island preview runtime.

## Why this format exists

The old path (VibePage JSON with HTML in strings and JSON inside `data-props='...'` attributes) forced triple escaping and caused the top agent failure classes: entity-escaped markup rendering as literal text, apostrophes in copy breaking props, giant-blob page updates. In source format those failures are impossible by construction.

## The format

```html
<!-- section: hero -->
<section class="py-12 md:py-16 lg:py-20" style="background-color: var(--lx-bg-color)">
  <h1 class="text-4xl md:text-5xl font-bold" style="font-family: var(--lx-font-heading)">
    Don't miss the "Summer Drop"
  </h1>

  <lx-island name="CountdownTimer" hydrate="visible">
    <script type="application/json">
      { "endDate": "2026-09-15T00:00:00Z", "style": "flip" }
    </script>
  </lx-island>
</section>

<style>
  /* becomes section.css — scope selectors to this section */
  .hero-lede { max-width: 62ch; }
</style>

<script
  type="application/lexsis-motion"
  data-motion-id="hero-entrance"
  data-capabilities="waapi"
  data-mode="entrance"
  data-importance="decorative"
  data-reduced-motion="static"
>
({ dom, waapi }) => {
  const lede = dom.query(".hero-lede");
  if (!lede) return;
  waapi.animate(lede, [
    { opacity: 0.25, transform: "translateY(18px)" },
    { opacity: 1, transform: "translateY(0)" }
  ], { duration: 600, fill: "both" });
}
</script>

<!-- section: faq -->
<section class="py-12">
  <details>
    <summary>Can I return it?</summary>
    <p>Yes — 30 days, no questions asked.</p>
  </details>
</section>
```

### Rules

1. **Sections** are delimited by `<!-- section: kebab-case-id -->` comments. Ids must be unique.
2. **Islands** are `<lx-island name="IslandName">` with props as a `<script type="application/json">` child. Write natural copy — apostrophes, quotes, em-dashes are all fine; no escaping needed.
3. **`<lx-island>` attributes**: `name` (required), `hydrate` (`immediate|visible|idle|interaction`), `headless` (headless mode — see below), plus `class`/`id`/`style` which pass through to the compiled element.
4. **Section CSS** goes in a top-level `<style>` block. New custom animation
   goes in `<script type="application/lexsis-motion">`. Plain top-level
   `<script>` remains compatibility section JS. `application/json` / `ld+json`
   scripts stay in the HTML.
5. **External libraries** do not go in section HTML. Approved analytics and
   integrations use `scripts`; GSAP, Three.js, Lottie, and Rive use managed
   motion loaders instead.
6. **`head`, `theme_css`, `scripts`** are structured tool arguments. Save the
   selected theme and approved page-wide additions in `page-theme.css`, then
   pass that file's exact contents as `theme_css`.
7. Tailwind classes compile into one `compiled_page_css` artifact. Fix every
   missing candidate; do not add Tailwind CDN or a separate generated sheet.

### Tool workflow

```
lexsis_brand → list_themes/get_theme → theme_css
draft source HTML (whole page)
lexsis_pages { action: "compile", args: { source, head, theme_css, scripts } }
fix any issues, then:
lexsis_page_create { action: "create", args: { source, head, theme_css, scripts, slug, publish: false } }
edits: lexsis_drafts → page_update_section or page_patch
round-trip: lexsis_pages → source/section_source → lexsis_drafts
```

`page_update_section` compiles one section and upserts it. `page_patch` batches
related localized changes into one version. Pass `expected_version`.

## Starting From a Template

Search the section library before writing a section from scratch. When you pick
a template, request editable source:

```text
lexsis_design({ action: "get_section", args: { ids: ["template-id"] } })
```

The response's `source` is one complete source-format section: a delimiter,
`<lx-island>` markup, and the template CSS/JS. Tailor it, then run
`lexsis_pages` action `compile`.

`format: "compiled_reference"` is renderer output containing
`data-island` / `data-props`. It is useful for inspection but must never be
given to source-authoring tools.

## Headless islands (fully custom markup)

For maximum design freedom, add `headless` and author the island's internals yourself; behavior attaches to `data-lx-*` hooks. Currently supported: **BuyBox** (plus the long-standing Navbar/Footer/SiteHeader hydration modes — see island-patterns.md).

```html
<lx-island name="BuyBox" headless>
  <script type="application/json">
    { "product": { "title": "Serum", "price": "$49.00", "variants": [
      { "id": "v1", "title": "30ml", "price": "$49.00", "available": true },
      { "id": "v2", "title": "50ml", "price": "$69.00", "available": true }
    ] } }
  </script>

  <p class="text-3xl font-bold" data-lx-buybox="price">$49.00</p>
  <div class="flex gap-2">
    <button data-lx-buybox="variant-option" data-variant-id="v1" class="px-4 py-2 border rounded-full">30ml</button>
    <button data-lx-buybox="variant-option" data-variant-id="v2" class="px-4 py-2 border rounded-full">50ml</button>
  </div>
  <div class="flex items-center gap-3">
    <button data-lx-buybox="qty-dec">−</button>
    <span data-lx-buybox="qty">1</span>
    <button data-lx-buybox="qty-inc">+</button>
  </div>
  <button data-lx-buybox="add" class="w-full py-4 rounded-full text-white"
          style="background: var(--lx-accent-color)">Add to Cart</button>
  <p data-lx-buybox="error" class="text-red-600 text-sm">Couldn't add — try again.</p>
</lx-island>
```

### BuyBox hooks

| Hook | Required | Behavior |
|---|---|---|
| `add` | **yes** | add-to-cart trigger; gets `lx-adding` / `lx-added` classes |
| `price` | recommended | text kept in sync with selected variant/plan |
| `compare-price` | no | compare-at price; hidden when none |
| `variant-option` | no | one per variant, needs `data-variant-id="v1"`; gets `lx-selected` / `lx-disabled` |
| `qty` / `qty-inc` / `qty-dec` | no | quantity display (or `<input>`) + stepper |
| `stock` | no | availability text; override via `data-in-stock-text` / `data-out-of-stock-text` |
| `error` | no | revealed when add-to-cart fails |

Style the state classes in section CSS: `.lx-selected { ... }`, `.lx-adding { opacity: .6 }`, `.lx-disabled { pointer-events: none; opacity: .4 }`.

## Animations

Read `animation-system.md` before authoring any plan-named custom motion.

### Presets — `data-behavior`

```html
<section data-behavior="gsap-reveal" data-config='{"targets":".card","y":40,"stagger":0.1}'>
<div data-behavior="gsap-parallax" data-config='{"speed":0.3}'>
<section data-behavior="gsap-pin" data-config='{"stepDuration":0.5}'>  <!-- children: [data-pin-step] -->
<div data-behavior="gsap-marquee-scroll" data-config='{"distance":-200}'>
```

Presets use the renderer-owned pinned GSAP loader and respect reduced motion.
Also available (CSS-driven, pre-existing): `scroll-reveal`, `accordion`,
`horizontal-scroll`, `content-slider`, and `sticky-reveal`.

### Custom managed motion

Use `<script type="application/lexsis-motion">` for custom WAAPI, GSAP, SVG,
Canvas 2D, WebGL, Three.js, Lottie, Rive, video, pointer, scroll, or runtime
event work. Declare capabilities and use managed timers, observers, loops,
assets, and engine loaders. Do not add animation libraries through `scripts`.

The MCP compiler extracts managed motion into `section.motion[]`, validates the
AST and performance budgets, and round-trips it through source reads and page
patches. Plain section JS remains only for compatibility behavior.

## What NOT to do

```html
<!-- Don't: hand-written island markers (old format — compiler rejects raw usage in source) -->
<div data-island="FAQ" data-props='{"items":[...]}'></div>

<!-- Don't: escaped HTML — never escape anything -->
&lt;section&gt;...&lt;/section&gt;

<!-- Don't: external scripts in section HTML — use the scripts param -->
<script src="https://cdn.example.com/lib.js"></script>
```

---

# Storefront Workflow

Use one owning command at a time.

## Normal Page Journey

```text
/setup
  → /plan-page
  → /design-page
  → /generate
  → /publish
```

- Setup is normally run once and refreshed only for changed stores/themes.
- Plan defines a concise campaign and section strategy without islands.
- Design selects islands, resolves page assets, compiles source, and creates
  one unpublished hosted draft.
- Generate reuses that draft when present, then owns synchronization and
  production-ready hosted QA.
- Publish is a separate explicit release.

Commands do not silently invoke one another. When a user intentionally starts
later, create the minimum missing artifact and record the skipped command.

Infer `fast-draft`, `production-ready`, or `publish` from the user's complete
request and current conversation. Reversible ambiguity defaults to
`fast-draft`; consequential ambiguity still requires clarification. Intent
inference never authorizes publishing, paid generation, or deletion.

## Optional Routes

- Use `/analyze-page` before planning when a URL, screenshot, or ad matters.
- Use `/asset-prep` independently for standalone or replacement asset work.
- Use `/design-page` concept-first when the user wants a mobile-first mockup
  approved before source authoring.
- Use `/build` for the fastest unpublished draft from a prompt or an
  automatically selected page kit.
- Use `/build-with-template` when the user already supplied the page-kit or
  section-template URL.
- Use `/optimize` for an existing page and a specific outcome.
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
- Keep production changes local-first and stop on version drift.
- Create drafts with `publish:false`.
- Keep concept images out of production source and asset slots.
- Limit fast-build compilation to one initial attempt and one targeted repair.
- Publish only after current QA and explicit approval.

---

# Conversion Psychology — Storefront Design Intelligence

> **Not real islands:** `CompareTable`. They have no schema. Verify every island name
> against `lexsis_design` action `islands`; the replacement for each job is in
> `references/workflows/island-selection-workflow.md`.

> House rules in `storefront-engine/references/design-rules.md` override every example below.
> Examples show structure and copy intent; their styling (gradients, hover transforms,
> uppercase labels, pills, emoji, section fills) is illustrative and must not be copied.
> Where an example conflicts with a house rule, the rule wins.

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

> When to load: ALWAYS. Read before generating any ecommerce page.

## The Conversion Stack (AIDA → Sections)

Map the AIDA framework to section order. Each stage requires specific psychology and placement.

### Short Page (5-7 sections) — Impulse / Low-consideration products

1. **Attention (1 section)**: Hero section
   - Product image or typographic hero on the page background. No gradient.
   - Benefit-driven headline (6-10 words)
   - `font-size: clamp(2.5rem, 5vw, 3.5rem)` for headline
   - Sticky CTA bar for persistent action

2. **Interest (2 sections)**: Value props + social proof stats
   - 3 benefits max, as a definition list or asymmetric two-column; icons only if the plan's icon decision says so
   - Numbers: customer count, star rating, review count
   - `py-8 md:py-12` spacing

3. **Desire (2 sections)**: Reviews + transformation proof
   - Star-first review display, 3-6 reviews
   - Before/after images or testimonial carousel
   - `data-island="ReviewCarousel"` for dynamic trust

4. **Action (2 sections)**: CTA + footer
   - Urgency element (countdown or inventory indicator)
   - CTA names the action in brand voice ("Add to cart")
   - `data-island="CountdownTimer"` or `data-island="InventoryIndicator"`

### Medium Page (8-12 sections) — Considered purchase / New-to-brand

1. **Attention (1)**: Hero with video or interactive media
2. **Interest (3)**: Value props → logo carousel → stats
   - Logo carousel = trust transfer from known brands
3. **Desire (5)**: Feature grid → testimonials → before/after → reviews → comparison table
   - 3-6 features as a definition list or asymmetric two-column; icons only if the plan's icon decision says so
   - Transformation proof with `data-island="BeforeAfter"`
   - Compare you vs. 2 alternatives (3 columns max)
4. **Action (3)**: FAQ → CTA → footer
   - Preemptive objection handling (5-8 questions)
   - `data-island="EmailCapture"` for fence-sitters
   - `data-island="FAQ"` for progressive disclosure

### Long Page (12-16 sections) — High-ticket / Complex products

1. **Attention (2)**: Hero + announcement bar
   - Free shipping threshold / promo in bar
2. **Interest (4)**: Value props → logo carousel → stats → press mentions
   - Layer authority progressively: claims → endorsements → proof
3. **Desire (7)**: Feature showcase → testimonials → case study → feature grid → reviews → comparison → risk reversal
   - Hero feature with `data-island="VideoPlayer"`
   - Full customer journey (problem → solution → result)
   - Guarantee + return policy badge-driven
4. **Action (3)**: FAQ → dual CTA → footer
   - Dual CTA: buy now / learn more
   - `data-island="BundleBuilder"` for upsells

**Section Order Rules:**
- Never reviews before value props (prove value before social proof)
- FAQ immediately before final CTA (remove last objection)
- Stats or logo carousel within first 3 sections for trust anchoring
- Footer always last (consistency signal)

---

## Above-the-Fold Rules

What MUST be visible without scroll (< 900px viewport height). Violating this kills 40%+ of conversions.

### PDP (Product Detail Page)

**Mandatory visible elements:**
- Product image (left 50-60% width, min 600px tall)
- Product title (max 2 lines)
- Price + compare_at_price (if discounted)
- Star rating + review count (clickable to reviews)
- Primary CTA button
- 1-2 trust lines as plain text (free shipping, guarantee)

**HTML pattern:**
```html
<section class="grid md:grid-cols-2 gap-8 max-w-7xl mx-auto px-4 py-8">
  <div class="relative">
    <img src="/product.jpg" alt="Product" class="w-full h-auto rounded-lg" />
  </div>
  <div class="flex flex-col justify-center space-y-6">
    <h1 class="text-4xl md:text-5xl font-bold leading-tight" style="color:var(--lx-text-color)">
      Premium Product Name
    </h1>
    <p class="text-lg md:text-xl opacity-80">One-line benefit promise that resonates</p>
    <div class="flex items-baseline gap-3">
      <span class="text-3xl font-bold" style="color:var(--lx-text-color)">$89.00</span>
      <!-- compare-at only when Shopify has one: struck text, no pill -->
      <span class="text-lg line-through opacity-40">$129.00</span>
    </div>
    <!-- rating as plain text, only when the count is real -->
    <p class="text-sm opacity-70">4.8 from 312 reviews</p>
    <div data-island="BuyBox" data-props='{"productId":"gid://shopify/Product/123","ctaText":"Add to cart","showQuantity":true}'></div>
    <!-- trust line: plain text over a 1px hairline, no icons, no emoji -->
    <p class="text-sm pt-4 opacity-70" style="border-top:1px solid var(--lx-border-color)">Free shipping. Money-back guarantee.</p>
  </div>
</section>
```

### Landing Page (paid traffic)

**Mandatory visible:**
- Headline with specific benefit (not generic)
- Subline addressing pain point
- Hero image/video showing product in use
- Primary CTA (above fold)
- 1 trust signal (review stars or customer count)

**HTML pattern:**
```html
<section class="relative min-h-screen flex items-center justify-center text-center px-4 py-20" style="background:var(--lx-bg-color)">
  <div class="max-w-4xl mx-auto space-y-8">
    <h1 class="text-5xl md:text-7xl font-bold leading-none" style="color:var(--lx-text-color);font-family:var(--lx-font-heading)">
      Get Flawless Skin in 30 Days
    </h1>
    <p class="text-xl md:text-2xl" style="color:var(--lx-text-muted)">
      Without harsh chemicals or expensive treatments. Guaranteed.
    </p>
    <button class="px-10 py-5 text-xl font-bold rounded-lg transition-colors hover:bg-[var(--lx-accent-color-hover)]" style="background:var(--lx-accent-color);color:white">
      Start your transformation
    </button>
    <p class="text-sm" style="color:var(--lx-text-muted)">Join 47,000+ customers who transformed their skin</p>
  </div>
  <div data-island="CountdownTimer" data-props='{"endDate":"2026-06-30T23:59:59Z","message":"Offer ends in:","urgencyThreshold":3600}'></div>
  <div data-island="SocialProofPopup" data-props='{"displayDuration":5000,"interval":15000,"maxPopups":3}'></div>
</section>
```

Never hardcode hex; use `--lx-*` tokens.

### Collection Page

**Mandatory visible:**
- Category headline + product count
- Filter bar (collapsible on mobile)
- First 4-6 products (2x3 grid desktop, 2 columns mobile)
- Sort dropdown
- Trust signal (delivery promise or return policy)

**Layout rule:** First product fold < 600px from top on desktop, < 800px on mobile.

---

## Price Psychology Patterns

### Anchoring (strikethrough + current)

Show original price crossed out. The "minimum 20%, optimal 30-40%" heuristic is market-specific; never apply it to a merchant's real price list. Show compare-at only when Shopify has one. No percentage pill unless the merchant runs a named sale.

```html
<div class="flex items-baseline gap-3">
  <span class="text-3xl font-bold" style="color:var(--lx-text-color)">$79.99</span>
  <span class="text-lg line-through opacity-40">$119.99</span>
</div>
<p class="text-sm mt-2 opacity-70">Save $40 today</p>
```

### Charm Pricing

Market-specific (US DTC); never apply to a merchant's real price list. Where the merchant already prices this way: .97, .95 or .99 for mid-market ($50-$300), .00 for premium ($500+).

**Examples:**
- Low-ticket (<$50): $29.97, $14.99
- Mid-ticket ($50-$300): $129.95, $79.97
- High-ticket ($300+): $999.00, $1,500.00

### Bundle Pricing (quantity breaks)

Show per-unit savings, not just total discount.

```html
<!-- equal cards; the recommended tier gets a 1px accent border and one sentence-case line — no scale, no caps pill, no glow -->
<div class="grid md:grid-cols-3 gap-4">
  <div class="p-6 rounded-lg" style="border:1px solid var(--lx-border-color)">
    <div class="text-center space-y-2">
      <p class="text-sm opacity-60">Buy 1</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$59.99</p>
      <p class="text-sm opacity-70">$59.99 each</p>
      <button class="w-full px-4 py-2 mt-4 rounded" style="border:1px solid var(--lx-accent-color);color:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
  <div class="p-6 rounded-lg" style="border:1px solid var(--lx-accent-color)">
    <div class="text-center space-y-2">
      <p class="text-sm" style="color:var(--lx-accent-color)">Most chosen</p>
      <p class="text-sm opacity-60">Buy 3</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$119.99</p>
      <p class="text-sm opacity-70">$40.00 each — Save $60</p>
      <button class="w-full px-4 py-2 mt-4 rounded font-bold text-white transition-colors hover:bg-[var(--lx-accent-color-hover)]" style="background:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
  <div class="p-6 rounded-lg" style="border:1px solid var(--lx-border-color)">
    <div class="text-center space-y-2">
      <p class="text-sm opacity-60">Buy 2</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$99.99</p>
      <p class="text-sm opacity-70">$50.00 each — Save $20</p>
      <button class="w-full px-4 py-2 mt-4 rounded" style="border:1px solid var(--lx-accent-color);color:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
</div>
```

### Payment Splitting (Afterpay/Klarna)

Show "or 4 payments of $X" beneath price. Increases conversion 20-30% for $100+ items.

```html
<div class="space-y-2">
  <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$159.99</p>
  <p class="text-sm opacity-70">or 4 interest-free payments of $40.00 with <strong>Afterpay</strong></p>
</div>
```

### Decoy Pricing (3-tier)

Always show 3 options. Middle option is the target, positioned as "most popular".

```html
<!-- equal cards; the target tier gets a 1px accent border and a sentence-case line — no scale, no caps pill, no glow, no glyph bullets -->
<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto">
  <div class="p-8 rounded-lg" style="border:1px solid var(--lx-border-color)">
    <h3 class="text-2xl font-bold mb-2">Basic</h3>
    <p class="text-4xl font-bold mb-4" style="color:var(--lx-text-color)">$49.99</p>
    <ul class="space-y-3 mb-6 text-sm">
      <li>Feature A</li>
      <li>Feature B</li>
    </ul>
    <button class="w-full px-6 py-3 rounded" style="border:1px solid var(--lx-accent-color);color:var(--lx-accent-color)">
      Choose Basic
    </button>
  </div>
  <div class="p-8 rounded-lg" style="border:1px solid var(--lx-accent-color)">
    <p class="text-sm mb-2" style="color:var(--lx-accent-color)">Most popular</p>
    <h3 class="text-2xl font-bold mb-2">Pro</h3>
    <div class="flex items-baseline gap-2 mb-4">
      <p class="text-4xl font-bold" style="color:var(--lx-text-color)">$89.99</p>
      <p class="text-lg line-through opacity-40">$129.99</p>
    </div>
    <ul class="space-y-3 mb-6 text-sm">
      <li>Feature A</li>
      <li>Feature B</li>
      <li>Feature C</li>
      <li>Feature D</li>
    </ul>
    <button class="w-full px-6 py-3 rounded font-bold text-white transition-colors hover:bg-[var(--lx-accent-color-hover)]" style="background:var(--lx-accent-color)">
      Choose Pro
    </button>
  </div>
  <div class="p-8 rounded-lg" style="border:1px solid var(--lx-border-color)">
    <h3 class="text-2xl font-bold mb-2">Premium</h3>
    <p class="text-4xl font-bold mb-4" style="color:var(--lx-text-color)">$149.99</p>
    <ul class="space-y-3 mb-6 text-sm">
      <li>Everything in Pro</li>
      <li>Feature E</li>
      <li>Feature F</li>
      <li>Priority support</li>
    </ul>
    <button class="w-full px-6 py-3 rounded" style="border:1px solid var(--lx-accent-color);color:var(--lx-accent-color)">
      Choose Premium
    </button>
  </div>
</div>
```

---

## Social Proof Hierarchy

Rank order by persuasive power (highest to lowest). Use this sequence in sections.

### 1. Numbers (stats bar)

Raw metrics. Most credible when specific and large.

```html
<!-- figures inline on the page background; sentence-case labels; no band, no oversized accent numerals -->
<section class="py-16 px-4">
  <div class="grid grid-cols-2 md:grid-cols-4 gap-8 max-w-6xl mx-auto">
    <div>
      <p class="text-3xl md:text-4xl font-bold" style="color:var(--lx-text-color);font-family:var(--lx-font-heading)">{{customer_total}}</p>
      <p class="text-sm mt-2" style="color:var(--lx-text-muted)">Happy customers</p>
    </div>
    <div>
      <p class="text-3xl md:text-4xl font-bold" style="color:var(--lx-text-color);font-family:var(--lx-font-heading)">{{average_rating}}/5</p>
      <p class="text-sm mt-2" style="color:var(--lx-text-muted)">Average rating</p>
    </div>
    <div>
      <p class="text-3xl md:text-4xl font-bold" style="color:var(--lx-text-color);font-family:var(--lx-font-heading)">{{review_total}}</p>
      <p class="text-sm mt-2" style="color:var(--lx-text-muted)">Verified reviews</p>
    </div>
    <div>
      <p class="text-3xl md:text-4xl font-bold" style="color:var(--lx-text-color);font-family:var(--lx-font-heading)">{{recommend_pct}}</p>
      <p class="text-sm mt-2" style="color:var(--lx-text-muted)">Would recommend</p>
    </div>
  </div>
</section>
```

Every `{{…}}` figure is a placeholder for a value returned by `lexsis_catalog` action `reviews` (`total`, ratings) or a claim the merchant confirmed in the plan. Never type a number here; omit the figure when no source exists (house rule N11).


**When to use:** First 3 sections. Anchor trust before storytelling.

### 2. Faces (testimonial cards)

A real person's words with their name and city. Most effective for emotional products (beauty, wellness, lifestyle).

```html
<!-- one featured quote in the heading face; name and city muted; no stars, no avatar ring, no card -->
<section class="py-16 px-4">
  <div class="max-w-3xl mx-auto">
    <blockquote class="text-2xl md:text-3xl leading-snug" style="color:var(--lx-text-color);font-family:var(--lx-font-heading)">
      "This completely changed how I approach skincare. I saw results in just 2 weeks."
    </blockquote>
    <p class="mt-6 text-sm" style="color:var(--lx-text-muted)">Sarah M., Portland — verified buyer</p>
  </div>
</section>
```

**When to use:** After interest stage, before feature deep-dive. One featured quote per section; a plain list of 3-6 only if the plan asks for it.

### 3. Logos (logo carousel)

Trust transfer from known brands. Works for B2B, press mentions, "as seen on".

```html
<!-- page background, static: no band, no hover effects -->
<section class="py-12 px-4">
  <div class="max-w-6xl mx-auto">
    <p class="text-center text-sm mb-8" style="color:var(--lx-text-muted)">Trusted by leading brands</p>
    <div class="flex justify-center items-center gap-12 flex-wrap">
      <img src="/logos/forbes.svg" alt="Forbes" class="h-10 opacity-60" />
      <img src="/logos/techcrunch.svg" alt="TechCrunch" class="h-10 opacity-60" />
      <img src="/logos/wsj.svg" alt="Wall Street Journal" class="h-10 opacity-60" />
    </div>
  </div>
</section>
```

**When to use:** Section 2-3. Before testimonials, after value props.

### 4. Quotes (review list)

Text-only reviews. Lowest impact but high volume works (10+ reviews).

```html
<section class="py-16 px-4">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-3xl md:text-4xl font-bold text-center mb-12" style="color:var(--lx-text-color)">What customers say</h2>
    <div data-island="ReviewCarousel" data-props='{"collectionId":"<active collection id from the plan>","minRating":4,"pageSize":8,"variant":"grid"}'></div>
  </div>
</section>
```

**When to use:** Mid-page (sections 5-8). Pile-on after testimonials for reinforcement.

---

## Urgency & Scarcity

Three types. Each requires different implementation and psychology.

### 1. Real Scarcity (Inventory)

Only use if actually tracking inventory. False scarcity destroys brand trust.

```html
<!-- text only: no emoji, no tinted pill -->
<p class="text-sm font-semibold" style="color:var(--lx-text-color)">Only 7 left in stock</p>
<div data-island="InventoryIndicator" data-props='{"threshold":10,"lowStockMessage":"Only {count} left in stock","outOfStockMessage":"Sold out — join waitlist"}'></div>
```

**When to use:** High-demand products, limited editions, seasonal items.

### 2. Deadline (Countdown)

Time-limited offers. Must have real expiration.

```html
<!-- deadline bars live in the announcement bar (the only permitted band, house rule N2) and use its tokens — never a red hex fill, never emoji -->
<div data-island="AnnouncementBar" data-props='{"message":"Summer sale: 30% off ends soon","link":"#shop","dismissible":false}'></div>
<div data-island="CountdownTimer" data-props='{"endDate":"2026-06-30T23:59:59Z","message":"Ends in","urgencyThreshold":3600}'></div>
```

**When to use:** Flash sales, product launches, abandoned cart recovery.

### 3. Exclusivity (Limited Access)

Member-only, waitlist, invite-only framing.

```html
<section class="py-20 px-4 text-center">
  <div class="max-w-2xl mx-auto space-y-6">
    <h2 class="text-4xl font-bold" style="color:var(--lx-text-color)">Join the Waitlist</h2>
    <p class="text-lg opacity-80">Limited to 500 founding members. Next batch ships August 2026.</p>
    <p class="text-sm font-semibold" style="color:var(--lx-text-muted)">127 spots remaining</p>
    <div data-island="EmailCapture" data-props='{"placeholder":"Enter your email","buttonText":"Reserve Your Spot"}'></div>
  </div>
</section>
```

**When to use:** Pre-launch, beta access, VIP tiers.

### Anti-Patterns (Fake Urgency)

| Don't | Why | Do |
|----------|-----|-------|
| Evergreen countdowns (timer resets on refresh) | Users notice, trust tanks | Use real sale end dates, or remove timer |
| "Only 2 left!" for digital products | Obvious lie | Use enrollment caps ("Only 50 spots in this cohort") |
| "Sale ends tonight" every night | Cried wolf effect | Run real weekly/monthly sales with calendar |
| SocialProofPopup with fake names | "John from New York just bought" on loop | Only use if pulling real order events from API |

---

## Cognitive Load Management

Max 3 choices per section. More options = decision paralysis = abandonment.

### Feature Grid (3 features, not 7)

**Good (3 features):**
```html
<!-- definition list, no icons -->
<section class="py-16 px-4">
  <dl class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
    <div>
      <dt class="text-xl font-bold">Fast results</dt>
      <dd class="mt-2 opacity-80">See improvements in 7 days or less</dd>
    </div>
    <div>
      <dt class="text-xl font-bold">Risk-free</dt>
      <dd class="mt-2 opacity-80">60-day money-back guarantee</dd>
    </div>
    <div>
      <dt class="text-xl font-bold">Loved by customers</dt>
      <dd class="mt-2 opacity-80">Join 47,000+ happy customers</dd>
    </div>
  </dl>
</section>
```

**If you have 6+ features:** Split into 2 sections (benefits vs. technical specs).

### CompareTable (3 columns max, 5-8 rows)

```html
<div data-island="CompareTable" data-props='{"columns":[{"name":"Competitor A","highlight":false},{"name":"You","highlight":true},{"name":"Competitor B","highlight":false}],"rows":[{"feature":"Feature 1","values":["No","Yes","No"]},{"feature":"Feature 2","values":["Yes","Yes","No"]},{"feature":"Feature 3","values":["No","Yes","Yes"]}]}'></div>
```

### Progressive Disclosure (Tabs/FAQ)

Use islands for deep info. Don't dump paragraphs.

```html
<div data-island="Tabs" data-props='{"tabs":[{"label":"How It Works","content":"..."},{"label":"Ingredients","content":"..."},{"label":"Shipping","content":"..."}]}'></div>
<div data-island="FAQ" data-props='{"items":[{"question":"How long does shipping take?","answer":"2-3 business days."}]}'></div>
```

---

## Trust Escalation Ladder

Move visitors from low-commitment → high-commitment actions. Don't ask for the sale immediately.

### Sequence:

1. **Browse encouragement** (no commitment)
   - Hero: "Explore our collection"
   - Value props: "See why 47,000+ customers love us"

2. **Email capture** (small commitment)
   - Offer: "Get 10% off your first order"
   - Placement: Section 3-5
   - `data-island="EmailCapture"`

3. **Cart confidence** (medium commitment)
   - `data-island="BuyBox"` with "Add to Cart"
   - Show: trust badges, free shipping, easy returns

4. **Purchase trigger** (high commitment)
   - Final CTA: "Complete your order"
   - Add: `data-island="CountdownTimer"` or `data-island="InventoryIndicator"`
   - Show: risk reversal (guarantee)

---

## CTA Psychology

Button copy is conversion science. Every word matters.

### Name the Action in Brand Voice

**Bad (vague):**
- "Get Started"
- "Submit"
- "Download"

**Good (names the action, brand voice, sentence case):**
- "Add to cart"
- "Start free trial"
- "Send me the guide"

**Why it works:** The visitor knows exactly what happens next. No "MY"/"ME" caps — shouted first-person reads as template copy.

```html
<button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
  Add to cart
</button>
```

### Benefit-Driven Copy

**Bad (action-only):**
- "Submit"
- "Continue"
- "Next"

**Good (action + benefit):**
- "Get My Discount"
- "Unlock Free Shipping"
- "Claim My Spot"

```html
<button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
  Claim My 30% Off
</button>
```

### Contrast Principle

CTA button must have 4.5:1 contrast ratio against background (WCAG AA). Use high-chroma colors.

```html
<button class="px-8 py-4 text-lg font-bold rounded-lg transition-colors hover:bg-[var(--lx-accent-color-hover)]" style="background:var(--lx-accent-color);color:white">
  Add to cart
</button>
```

**Contrast pairs (tokens, never hex):**
- Accent CTA on page: `var(--lx-accent-color)` on `var(--lx-bg-color)`
- Inverted CTA on dark: `var(--lx-bg-color)` on `var(--lx-text-color)`
- Check the merchant's real token values against 4.5:1; never substitute a hardcoded hex.

### Button Hierarchy

**Primary (main action):**
```html
<button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
  Buy Now — $89
</button>
```

**Secondary (alternative action):**
```html
<button class="px-6 py-3 rounded-lg" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
  Learn More
</button>
```

**Ghost (low-commitment):**
```html
<button class="px-6 py-3 rounded-lg hover:bg-opacity-10" style="color:var(--lx-accent-color)">
  View Details
</button>
```

**Link (minimal friction):**
```html
<a href="#learn-more" class="underline" style="color:var(--lx-accent-color)">
  Learn More
</a>
```

### Dual CTA (high + low commitment)

Offer high-commitment + low-commitment options.

```html
<div class="flex gap-4 justify-center">
  <button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
    Buy Now — $89
  </button>
  <button class="px-6 py-3 rounded-lg" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
    Learn More
  </button>
</div>
```

**When to use:** High-ticket products ($300+), complex products needing education.

---

## Visual Hierarchy for Conversion

Eye-flow patterns direct attention to CTAs.

### Focal Points (element styles)

Use scale, color, and whitespace to create hierarchy.

**Headline (most important):**
```html
<h1 class="text-5xl md:text-7xl font-extrabold leading-tight mb-4" style="color:var(--lx-text-color)">
  Transform Your Skin in 30 Days
</h1>
```

**Subline (secondary):**
```html
<p class="text-xl md:text-2xl leading-relaxed mb-8" style="color:var(--lx-text-muted)">
  Clinically proven formula with visible results in just 2 weeks
</p>
```

**CTA (action):**
```html
<button class="px-10 py-5 text-xl font-bold rounded-lg transition-colors hover:bg-[var(--lx-accent-color-hover)]" style="background:var(--lx-accent-color);color:white">
  Add to cart
</button>
```

### Whitespace for Emphasis

Surround CTAs with empty space (min 2rem padding).

```html
<section class="py-20 px-4">
  <!-- CTA content -->
</section>
```

---

## Anti-Patterns (Conversion Killers)

| Don't | Why | Do |
|----|-----|-----|
| Generic headlines ("Welcome to Our Store") | No hook, no benefit | "Get [Specific Benefit] in [Timeframe]" |
| Hidden prices ("Contact for Pricing") | Friction, distrust | Show price upfront (even if high) |
| Walls of text (5-paragraph descriptions) | Cognitive overload | Bullet points, max 3 benefits |
| Too many CTAs (3+ above fold) | Decision paralysis | 1 primary CTA, 1 optional secondary |
| Tiny mobile buttons (40px tap target) | Poor UX, missed clicks | 48px minimum (py-3 or py-4) |
| Auto-playing video with sound | Annoys users | Muted autoplay, click to unmute |
| No trust signals above fold | Credibility gap | Add star rating or customer count near CTA |
| Fake urgency (evergreen countdown) | Trust erosion | Real sale end dates or remove timer |
| Cluttered forms (8-field email capture) | Abandonment | Email only with `data-island="EmailCapture"` |
| Slow load times (5+ second hero load) | Bounce rate spike | Optimize images, lazy-load below fold |
| No mobile optimization (desktop-only) | Poor mobile UX | Responsive spacing, clamp() font sizes |
| Unclear value prop ("We're the best") | Generic, meaningless | "Save 10 hours/week with automated [task]" |
| No risk reversal (no guarantee) | Fear of loss | Risk reversal section before final CTA |
| Dead-end pages (no next step) | Lost momentum | Every section ends with CTA or link |
| Inconsistent branding (5 button styles) | Unprofessional | Consistent colors via CSS vars |

---

## Complete Page Recipes

### Recipe 1: Lead Gen (Email Capture)

**Goal:** Maximize email signups for nurture sequence.

**VibePage structure (abbreviated):**
```json
{
  "head": {
    "title": "Get the Ultimate Skincare Guide",
    "fonts": ["<from lexsis_brand.compile_theme>"]
  },
  "theme_css": "<output of lexsis_brand.compile_theme — never hand-written hex>",
  "sections": [
    {
      "id": "hero",
      "html": "<section class='py-20 px-4 text-center' style='background:var(--lx-bg-color)'><div class='max-w-3xl mx-auto space-y-6'><h1 class='text-5xl md:text-6xl font-bold' style='color:var(--lx-text-color);font-family:var(--lx-font-heading)'>Get the Flawless Skin Guide</h1><p class='text-xl' style='color:var(--lx-text-muted)'>Learn how to achieve radiant skin in 30 days. Free download.</p><div data-island='EmailCapture' data-props='{\"placeholder\":\"Enter your email\",\"buttonText\":\"Send Me the Guide\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "value-props",
      "html": "<section class='py-16 px-4'><dl class='grid md:grid-cols-3 gap-8 max-w-5xl mx-auto'><div><dt class='text-xl font-bold'>Science-backed methods</dt><dd class='mt-2 opacity-80'>Proven techniques from dermatologists</dd></div><div><dt class='text-xl font-bold'>Natural ingredients</dt><dd class='mt-2 opacity-80'>No harsh chemicals or side effects</dd></div><div><dt class='text-xl font-bold'>30-day results</dt><dd class='mt-2 opacity-80'>See visible improvements in one month</dd></div></dl></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "stats",
      "html": "<section class='py-12 px-4'><div class='grid grid-cols-2 gap-8 max-w-4xl mx-auto'><div><p class='text-3xl font-bold' style='color:var(--lx-text-color);font-family:var(--lx-font-heading)'>47,000+</p><p class='text-sm mt-2' style='color:var(--lx-text-muted)'>Downloads</p></div><div><p class='text-3xl font-bold' style='color:var(--lx-text-color);font-family:var(--lx-font-heading)'>4.9/5</p><p class='text-sm mt-2' style='color:var(--lx-text-muted)'>Rating</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "cta",
      "html": "<section class='py-20 px-4 text-center'><div class='max-w-2xl mx-auto space-y-6'><h2 class='text-4xl font-bold' style='color:var(--lx-text-color)'>Ready to Get Started?</h2><div data-island='EmailCapture' data-props='{\"placeholder\":\"Enter your email\",\"buttonText\":\"Download Now — It\\'s Free\"}'></div></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

### Recipe 2: Direct Purchase (Low-ticket <$100)

**Goal:** Impulse buy, minimal friction.

**VibePage structure (abbreviated):**
```json
{
  "sections": [
    {
      "id": "hero",
      "html": "<section class='grid md:grid-cols-2 gap-8 max-w-7xl mx-auto px-4 py-8'><div><img src='/product.jpg' class='w-full rounded-lg'/></div><div class='flex flex-col justify-center space-y-6'><h1 class='text-5xl font-bold' style='color:var(--lx-text-color)'>Premium Serum</h1><p class='text-xl opacity-80'>Transform your skin in 30 days</p><div class='flex items-baseline gap-3'><span class='text-3xl font-bold' style='color:var(--lx-text-color)'>$79.99</span><span class='text-lg line-through opacity-40'>$119.99</span></div><div data-island='BuyBox' data-props='{\"productId\":\"gid://shopify/Product/123\",\"ctaText\":\"Add to Cart — Free Shipping\"}'></div></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

### Recipe 3: High-AOV ($500+)

**Goal:** Build trust for expensive purchase.

**VibePage structure (abbreviated):**
```json
{
  "sections": [
    {
      "id": "hero",
      "html": "<section class='relative min-h-screen flex items-center justify-center px-4' style='background:url(/hero.jpg) center/cover'><div class='max-w-3xl text-center space-y-6 text-white'><h1 class='text-6xl font-extrabold'>Enterprise CRM Platform</h1><p class='text-2xl'>Trusted by Fortune 500 companies</p><button class='px-8 py-4 text-lg font-bold rounded-lg' style='background:white;color:var(--lx-accent-color)'>Schedule a Demo</button></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "logos",
      "html": "<section class='py-12 px-4'><p class='text-center text-sm mb-8' style='color:var(--lx-text-muted)'>Trusted by industry leaders</p><div class='flex justify-center gap-12 flex-wrap'><img src='/logos/company1.svg' class='h-10 opacity-60'/><img src='/logos/company2.svg' class='h-10 opacity-60'/><img src='/logos/company3.svg' class='h-10 opacity-60'/></div></section>",
      "css": "",
      "js": ""
    }
  ]
}
```

---

**End of conversion-psychology.md**

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
   - **confirm** — knows the product and wants confidence to buy;
   - **compare** — deciding between options or alternatives;
   - **explore** — needs inspiration or use-case education;
   - **complete** — wants the full solution, routine, or setup;
   - **replenish** — returning for a refill, replacement, or repeat order.
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

- **Gallery gap:** “The current media shows the pack and texture, but not scale
  or in-use context. Should I use existing media only, or generate two custom
  gallery images for those jobs?”
- **Relationship:** “Should the recommendation help shoppers complete the
  routine, compare alternatives, replenish later, or should this page avoid
  recommendations?”
- **Compatibility:** “Do you have a verified model, size, shade, ingredient,
  room-dimension, or usage mapping for these add-ons?”
- **Risk:** “Which verified shipping, returns, trial, warranty, cancellation,
  or guarantee terms can appear beside the purchase decision?”
- **Audience state:** “Is this primarily a first purchase, an experienced
  buyer, or a returning/replenishment visit?”
- **Traffic context:** “Which promise or creative brought this traffic here,
  if the page must preserve message match?”

Never ask “Do you want custom images?” without first identifying the missing
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
| Guided comparison | Visitor is deciding between products or tiers | Compare only decision-driving attributes; state “best for” and meaningful trade-offs without manufacturing a winner | Comparison interaction, product selection |
| Compatibility confidence | Add-on usefulness depends on model, shade, size, ingredient, room, or regimen fit | Show the verified fit reason beside each recommendation and suppress incompatible or unavailable items | Attach rate, support questions, returns |
| Solution completeness | The hero SKU is only one part of the shopper's job | Present the minimum complete outfit, routine, stack, recipe, room, setup, care kit, or commissioning kit with individually selectable items | Attach rate, AOV, revenue per visitor |
| Sequence and next step | Products are understood as stages or order of use | Show when, how, and in what order products are used; distinguish morning/evening, setup/use/care, or beginner/advanced | Bundle attach rate, education engagement |
| Context and mental simulation | Shopper cannot picture ownership or final use | Show the product in the actual scene, occasion, room, routine, task, or before/after context using truthful media | Context-image engagement, conversion |
| Replenishment and continuity | Consumable, maintenance item, size progression, or replacement cycle exists | Explain serving/use count, refill timing, cadence, compatible replacement, or easy reorder without inventing depletion dates | Repeat purchase, subscription opt-in |
| Returning-customer shortcut | Existing buyers need less education and more continuity | Prefer refill, reorder, saved configuration, compatible replacement, or “what changed” paths when reliable customer context exists | Repeat conversion, time to purchase |
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

Name the customer's job instead of using a generic “Recommended for You.”
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

Existing media wins. When a decision-critical job is missing, create a planned
asset slot with the job as its purpose. Ask once whether to use existing media,
import a supplied asset, or generate the named gaps. Never generate a
replacement product identity image when verified Shopify media exists.

## Plan Handoff

Add this compact block to `page-plan.md`:

```markdown
## Consumer decision model

**Primary visitor mode.** confirm | compare | explore | complete | replenish
**Top decision questions.** Three shopper questions this page must answer.
**Selected behavioral patterns.** At most three, each with observed evidence.
**First decision area.** Facts, proof, and action visible before deeper detail.
**Gallery jobs.** covered; missing; asset slots created for missing jobs.
**Guided merchandising.** relationship name, reason, 2–3 products or none.
**Risk and trust.** sourced proof/policy placed beside the relevant decision.
**Mobile context.** what remains visible or is repeated during long scroll.
**Hypothesis and metric.** one primary behavior change and measurement.
```

`/design-page` implements this block without reopening settled choices.
`/build` creates the minimum version from available evidence. `/optimize` and
`/ab-test` use it to form one controlled, measurable hypothesis.

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

# Island Patterns — Wrapper HTML & Combination Recipes

> **Not real islands:** `CompareTable`, `ExitIntent`, `TrustBadgeBar`. They have no schema. Verify every island name
> against `lexsis_design` action `islands`; the replacement for each job is in
> `references/workflows/island-selection-workflow.md`.

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

How to properly embed, wrap, and combine React islands in vibe-code HTML sections. Load when using commerce or engagement islands.

---

## Island Embedding Rules

1. `data-island` attribute = exact island name (case-sensitive)
2. `data-props` = valid JSON in **single-quoted** attribute value
3. One `BuyBox` per page (multiple breaks cart state)
4. Cart: set `head.use_cart_v2: true` on every commerce page — never author a cart section (`CartDrawer` is deprecated V1)
5. Islands hydrate client-side — surrounding HTML renders immediately (SSR)
6. Never put islands inside other islands
7. Always wrap in a containing section with proper spacing

---

## Commerce Islands

### BuyBox — Primary Purchase Action

**Always pair with surrounding context (title, price are in the BuyBox island itself):**

```html
<section class="px-4 sm:px-6 lg:px-8 py-8">
  <div class="max-w-2xl mx-auto">
    <div data-island="BuyBox" data-props='{"productId":"gid://shopify/Product/123","ctaText":"Add to Cart"}'></div>
  </div>
</section>
```

**PDP layout — Gallery + BuyBox side by side:**

```html
<section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 lg:py-16">
  <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12">
    <!-- Left: Gallery -->
    <div data-island="ProductGallery" data-props='{"productId":"gid://shopify/Product/123","layout":"grid","enableLightbox":true}'></div>
    <!-- Right: BuyBox -->
    <div class="lg:sticky lg:top-24 lg:self-start">
      <div data-island="BuyBox" data-props='{"productId":"gid://shopify/Product/123","ctaText":"Add to Cart"}'></div>
    </div>
  </div>
</section>
```

### Cart — V2 is the default (CartDrawer V1 is DEPRECATED)

Set `head.use_cart_v2: true` on every commerce page. The renderer injects the resolved published cart profile separately, so **never author a cart section in the page**. Use `lexsis_cart.get`, `lexsis_drafts.cart_set`, and `lexsis_drafts.cart_edit` for MCP cart work. Full composition guide: load the `cart-composition` reference.

```jsonc
{ "head": { "title": "...", "use_cart_v2": true } }   // that's the whole cart setup
```

Legacy note: `CartDrawer` (V1) exists only on old pages that predate cart profiles. Don't add it to new pages; when editing a legacy page, prefer migrating it (remove CartDrawer, set the flag).

### StickyBar — Scroll-triggered Bottom CTA

```html
<section>
  <div data-island="StickyBar" data-props='{"productId":"gid://shopify/Product/123","cta":"Add to Cart","showAfter":"#primary-buy-box"}'></div>
</section>
```

`showAfter` is a CSS selector. Give the primary BuyBox wrapper a stable ID and
use that selector so the bar appears only after the primary purchase UI leaves
the viewport.

### QuantityBreaks — Volume Discounts

Place directly below or beside BuyBox:

```html
<section class="px-4 sm:px-6 lg:px-8 pb-6">
  <div class="max-w-2xl mx-auto">
    <div data-island="QuantityBreaks" data-props='{"productId":"gid://shopify/Product/123","tierQuantities":[2,3,5],"variant":"cards"}'></div>
  </div>
</section>
```

### ProductCarousel — Cross-sells / Related

```html
<section class="py-12 lg:py-20 px-4 sm:px-6 lg:px-8" style="background:var(--lx-bg-surface)">
  <div class="max-w-7xl mx-auto">
    <h2 class="text-center font-bold mb-8" style="font-family:var(--lx-font-heading);font-size:clamp(1.25rem,2.5vw,2rem)">
      You May Also Like
    </h2>
    <div data-island="ProductCarousel" data-props='{"productIds":["gid://shopify/Product/1","gid://shopify/Product/2","gid://shopify/Product/3","gid://shopify/Product/4"],"columns":4,"showQuickAdd":true}'></div>
  </div>
</section>
```

### ProductGallery — Image Gallery with Zoom

```html
<div data-island="ProductGallery" data-props='{"productId":"gid://shopify/Product/123","layout":"grid","enableLightbox":true}'></div>
```

Layout options: `"grid"` (thumbnails below), `"stack"` (vertical scroll), `"carousel"` (swipe).

---

## Social Proof Islands

### ReviewCarousel — Customer Reviews

**With custom reviews (no Shopify fetch):**

```html
<section class="py-12 lg:py-20 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-10">
      <p class="text-xs uppercase tracking-[0.2em] mb-2" style="color:var(--lx-accent-color)">Testimonials</p>
      <h2 class="font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">What Customers Say</h2>
    </div>
    <div data-island="ReviewCarousel" data-props='{"collectionId":"<review collection uuid from the plan>","minRating":4,"pageSize":8,"variant":"grid"}'></div>
  </div>
</section>
```

**Data source.** Reviews come from the merchant's imported library
(`lexsis_catalog` actions `reviews_status`, `review_collections`, `reviews`,
`reviews_search`) as recorded in the plan's Proof sources line. Pass
`collectionId` (an active collection) or `productIds`; omit
`reviewsEndpoint`, the page supplies it at runtime. Use the carousel only with
3 or more real reviews. For 1-2 verified reviews, render static testimonial
cards quoting them. If there are no reviews, use product proof, certifications,
guarantees, or verified press instead. Never fabricate names, ratings,
locations, or review counts.

### Trust Signals — Static HTML

```html
<section class="py-4 border-y" style="border-color:var(--lx-border-color)">
  <ul class="grid grid-cols-2 gap-4 text-sm md:grid-cols-4">
    <li>Secure checkout</li>
    <li>Free shipping</li>
    <li>Easy returns</li>
    <li>Quality guarantee</li>
  </ul>
</section>
```

### SocialProofPopup — Recent Activity Toasts

Place once (invisible section):

```html
<section class="hidden">
  <div data-island="SocialProofPopup" data-props='{"events":[{"name":"Priya","product":"Daily Face Serum","location":"Mumbai","time":"2 minutes ago"},{"name":"Rohit","product":"Daily Face Serum","location":"Delhi","time":"5 minutes ago"}],"position":"bottom-left","interval":8000}'></div>
</section>
```

Use localized names, currency, tax/shipping language, and city references only
when the selected store market supports them. For an India storefront, prefer
INR (`₹`), pincode-aware delivery language, and COD/UPI claims only when those
payment methods are actually configured.

---

## Content Patterns

### FAQ — Native Accordion

```html
<section class="py-12 lg:py-20 px-4">
  <div class="max-w-3xl mx-auto">
    <h2 class="text-center font-bold mb-10" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">
      Frequently Asked Questions
    </h2>
    <div class="space-y-3">
      <details><summary>How do I use this product?</summary><p>Apply 2-3 drops to clean skin morning and night.</p></details>
      <details><summary>Is it suitable for sensitive skin?</summary><p>Use only verified product guidance here.</p></details>
    </div>
  </div>
</section>
```

### Tabbed Content — Native Disclosure

```html
<section class="py-12 px-4">
  <div class="max-w-4xl mx-auto">
    <details open><summary>Details</summary><p>Full product details and specifications.</p></details>
    <details><summary>Ingredients</summary><p>Use verified ingredient data.</p></details>
    <details><summary>How to Use</summary><p>Use verified usage instructions.</p></details>
  </div>
</section>
```

### BeforeAfter — Comparison Slider

```html
<section class="py-12 lg:py-20 px-4">
  <div class="max-w-2xl mx-auto text-center">
    <h2 class="font-bold mb-8" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">
      Real Results
    </h2>
    <div data-island="BeforeAfter" data-props='{"before":{"src":"BEFORE_IMAGE_URL","label":"Day 1"},"after":{"src":"AFTER_IMAGE_URL","label":"Day 30"}}'></div>
  </div>
</section>
```

---

## Engagement Islands

### IngredientExplorer — Interactive Ingredients

```html
<section class="py-12 lg:py-20 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-4xl mx-auto">
    <div class="text-center mb-10">
      <p class="text-xs uppercase tracking-[0.2em] mb-2" style="color:var(--lx-accent-color)">Transparency</p>
      <h2 class="font-bold" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">What's Inside</h2>
    </div>
    <div data-island="IngredientExplorer" data-props='{"ingredients":[{"name":"Hyaluronic Acid","description":"Multi-molecular weight complex","benefit":"Deep multi-layer hydration"},{"name":"Niacinamide 5%","description":"Vitamin B3 derivative","benefit":"Minimizes pores, evens tone"},{"name":"Ceramide Complex","description":"Skin-identical lipids","benefit":"Repairs moisture barrier"}],"layout":"grid"}'></div>
  </div>
</section>
```

### Product Comparison — Static Table

```html
<section class="py-12 lg:py-20 px-4">
  <div class="max-w-4xl mx-auto">
    <h2 class="text-center font-bold mb-10" style="font-family:var(--lx-font-heading);font-size:clamp(1.5rem,3vw,2.25rem)">
      Why We're Different
    </h2>
    <table class="w-full text-left">
      <thead><tr><th>Feature</th><th>Our product</th><th>Alternative</th></tr></thead>
      <tbody><tr><td>Clean ingredients</td><td>Yes</td><td>Check source</td></tr></tbody>
    </table>
  </div>
</section>
```

### EmailCapture — Lead Capture

```html
<section class="py-12 lg:py-16 px-4" style="background:var(--lx-accent-color)">
  <div class="max-w-xl mx-auto text-center">
    <h2 class="text-white text-2xl font-bold mb-2" style="font-family:var(--lx-font-heading)">Join the Club</h2>
    <p class="text-white/70 text-sm mb-6">Get 10% off your first order + early access to new launches.</p>
    <div data-island="EmailCapture" data-props='{"placeholder":"Enter your email","buttonText":"Get 10% Off","discount":"10% off your first order","variant":"compact"}'></div>
  </div>
</section>
```

### Modal — Exit-Intent Offer

Place once (invisible):

```html
<section class="hidden">
  <div data-island="Modal" data-props='{"trigger":"exit_intent","headline":"Wait! Don't leave empty-handed","body":"Use code EXIT15 for 15% off your first order","triggerLabel":"Claim My Discount","position":"center"}'></div>
</section>
```

---

## Common Combinations

### PDP Core (minimum viable PDP)

```
1. ProductGallery + BuyBox (side-by-side on desktop)
2. Static trust row (immediately below)
3. Native details/ingredient disclosures
4. ReviewCarousel
5. StickyBar (scroll-triggered)
6. head.use_cart_v2: true (cart injected — no section needed)
```

### Landing Page Core

```
1. Hero section (HTML, no island)
2. Static trust row
3. Benefits section (HTML grid)
4. BeforeAfter or IngredientExplorer
5. ReviewCarousel
6. EmailCapture or BuyBox
7. Native FAQ details
8. Modal with exit-intent trigger (hidden)
```

### Collection Page

```
1. Collection header (HTML)
2. ProductCarousel (featured picks)
3. Product grid with QuickAdd per card
4. TrustBadgeBar
5. EmailCapture (footer)
```

---

## Data-Props Formatting Rules

1. **Single quotes** around attribute value: `data-props='...'`
2. **Double quotes** inside JSON: `{"key":"value"}`
3. **No apostrophes** in text values — use `'` or rephrase
4. **No line breaks** in data-props — must be one line
5. **Numbers without quotes**: `{"qty":2,"discount":10}`
6. **Booleans without quotes**: `{"autoPlay":true}`
7. **Arrays**: `{"items":[{...},{...}]}`

### Escaping gotchas

```html
<!-- WRONG: apostrophe breaks parsing -->
<div data-props='{"text":"Don't miss out"}'></div>

<!-- RIGHT: avoid apostrophes -->
<div data-props='{"text":"Do not miss out"}'></div>

<!-- RIGHT: use HTML entity in surrounding HTML, not in props -->
```

---

## PDP Template Recipes

### DTC Beauty PDP

```
ProductGallery (vertical, listenForVariant:true)
├── VariantSwatches (color, image type)
├── SubscriptionToggle
├── BuyBox (listenForEvents:true, showVariantSelector:false)
├── DeliveryEstimate (variant:"inline")
├── TrustBadgeBar (compact)
├── PaymentOptions (variant:"inline", listenForEvents:true)
├── InventoryIndicator (variant:"badge", listenForEvents:true)
├── Tabs (underline)
├── ReviewCarousel
├── BundleBuilder (layout:"horizontal")
├── ProductCarousel ("You may also like")
├── StickyBar
└── SocialProofPopup    # cart: head.use_cart_v2: true (injected)
```

### Fashion/Apparel PDP

```
ProductGallery (layout:"grid", listenForVariant:true)
├── VariantSwatches (color, image) + VariantSwatches (type:"size_grid", axis mode)
├── OptionResolver (productId)
├── SizeGuide
├── BuyBox (variant:"expanded", listenForEvents:true, showVariantSelector:false)
├── InventoryIndicator (variant:"text", listenForEvents:true)
├── DeliveryEstimate (variant:"card")
├── Tabs (style:"underline")
├── ReviewCarousel
├── BundleBuilder (title:"Complete the look", layout:"stacked")
├── ProductCarousel
├── StickyBar
└── ExitIntent          # cart: head.use_cart_v2: true (injected)
```

### Supplements/Wellness PDP

```
ProductGallery (vertical)
├── VariantSwatches (flat, image type for flavors)
├── QuantityBreaks
├── SubscriptionToggle
├── BuyBox (listenForEvents:true)
├── PaymentOptions (variant:"expandable")
├── TrustBadgeBar (badges: GMP, vegan, lab-tested)
├── IngredientExplorer (layout:"interactive")
├── FAQ (style:"accordion")
├── ReviewCarousel
├── CompareTable (vs competitors)
├── BundleBuilder (title:"Stack for results")
├── StickyBar
└── CountdownTimer      # cart: head.use_cart_v2: true (injected) (style:"simple", inline with price)
```

### Personalized Product PDP (Gifts/Jewelry)

```
ProductGallery (layout:"grid")
├── VariantSwatches (type:"text")
├── BuyBox (variant:"expanded", listenForEvents:true)
├── DeliveryEstimate (variant:"banner")
├── PaymentOptions (variant:"inline")
├── Tabs
├── ReviewCarousel
├── ProductCarousel ("Complete the gift set")
└── StickyBar            # cart: head.use_cart_v2: true (injected)
```

### Island Communication on PDP

Key event flows for PDP islands:
- VariantSwatches → (variant:changed) → BuyBox, ProductGallery, InventoryIndicator, PaymentOptions
- OptionResolver → (variant:changed) → all listeners above (for multi-axis products)
- SubscriptionToggle → (subscription:changed) → BuyBox
- BundleBuilder → (bundle:add) → cart drawer (injected cart profile)
- InventoryIndicator → (inventory:updated) → StickyBar, BuyBox

Always set `listenForEvents:true` on listener islands when they co-exist with emitters.

---

## New PDP Islands (v2)

### ProductHero — Split-Layout PDP Hero

Premium split-hero for PDPs. Media pane on one side, BuyBox on the other.

```html
<div data-island="ProductHero" data-props='{"images":[{"url":"/product-1.jpg","objectFit":"contain","objectPosition":"center"},{"url":"/product-2.jpg","objectFit":"cover"}],"layout":"splitLeft","thumbnails":"rail","thumbnailPosition":"left","navigation":"floatingArrows","transition":"fade","listenForVariant":true}'></div>
```

**Layout options:** `splitLeft` (media left 60%), `splitRight`, `fullHeight`, `stacked`
**ALWAYS PAIR WITH:** BuyBox in the adjacent grid cell. Use CSS grid in the containing HTML section to create the split.

### ProductCarousel — Related Products

Mixed-type grid with center feature card for bundles or highlighted products.

```html
<div data-island="ProductCarousel" data-props='{"products":[{"id":"123","title":"Product A","price":"$29","image":"/a.jpg"},{"id":"456","title":"Product B","price":"$35","image":"/b.jpg"}],"columns":2,"showQuickAdd":true}'></div>
```

### Product Detail Cards — Static HTML

Information cards for product specs, taste profiles, pairings, certifications.

```html
<div class="grid gap-4 md:grid-cols-2">
  <article><h3>Taste Profile</h3><p>Bright citrus · Smooth finish · Medium body</p></article>
  <article><h3>Pairs With</h3><p>Dark chocolate · Aged cheese · Fresh berries</p></article>
</div>
```

Place below the ProductHero/BuyBox section and above reviews.

---

## Navigation Islands — Hydration Mode (Preferred)

Navigation islands (Navbar, Footer, SiteHeader) support **hydration mode**: you generate ANY HTML/CSS, then place `data-lx-*` tags on functional elements. The island attaches behavior (cart state, mobile toggle, newsletter) without touching your design.

### Why Hydration Mode?

- Complete design freedom — any layout, any CSS
- Only 2-5 behavior props (vs 15+ style props in legacy mode)
- Cart state auto-syncs — no prop management
- Publish validator enforces required tags — can't ship broken nav

### Navbar — Hydration Mode

**Required tags:** `data-lx-nav="root|cart-trigger|cart-count|mobile-trigger|mobile-panel"`

**Behavior props:** `sticky` (bool), `cartMode` ("drawer"|"link"), `transparent` (bool)

```html
<div data-island="Navbar" data-props='{"sticky":true,"cartMode":"drawer"}'>
  <nav data-lx-nav="root" class="fixed top-0 w-full z-50 bg-white/95 backdrop-blur border-b border-gray-100">
    <div class="max-w-7xl mx-auto px-6 flex items-center justify-between h-16">
      <a href="/" data-lx-nav="logo">
        <img src="{{brand_logo}}" class="h-8" alt="{{brand_name}}" />
      </a>
      <nav class="hidden lg:flex items-center gap-8">
        <a href="/collections" data-lx-nav="link" class="text-sm font-medium">Shop</a>
        <a href="/about" data-lx-nav="link" class="text-sm font-medium">About</a>
      </nav>
      <div class="flex items-center gap-4">
        <button data-lx-nav="cart-trigger" class="relative p-2">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4zM3 6h18M16 10a4 4 0 01-8 0"/>
          </svg>
          <span data-lx-nav="cart-count" class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-black text-white text-[10px] flex items-center justify-center" style="display:none"></span>
        </button>
        <button data-lx-nav="mobile-trigger" class="lg:hidden p-2">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M3 12h18M3 6h18M3 18h18"/>
          </svg>
        </button>
      </div>
    </div>
    <div data-lx-nav="mobile-panel" class="hidden lg:hidden border-t px-6 py-4">
      <a href="/collections" class="block py-3 text-sm font-medium">Shop</a>
      <a href="/about" class="block py-3 text-sm font-medium">About</a>
    </div>
  </nav>
</div>
```

**CSS requirement** (include in section CSS):
```css
[data-lx-nav="mobile-panel"] { display: none; }
[data-lx-nav="mobile-panel"].lx-open { display: block; }
```

**Dropdowns (optional):**
```html
<div class="relative">
  <a href="/shop" data-lx-nav="dropdown-trigger">Shop ▾</a>
  <div data-lx-nav="dropdown-panel" class="absolute top-full mt-2 bg-white shadow-lg rounded-lg p-4">
    <a href="/collections/new" class="block py-2 text-sm">New Arrivals</a>
  </div>
</div>
```

**Hide cart (no cart-trigger/cart-count needed):**
```html
<div data-island="Navbar" data-props='{"sticky":true,"hideCart":true}'>
```

### Footer — Hydration Mode

**Required tags:** `data-lx-footer="root"`  
**Optional tags:** `newsletter-form`, `newsletter-input`, `newsletter-success`, `year`

```html
<div data-island="Footer" data-props='{"links":[]}'>
  <footer data-lx-footer="root" class="bg-gray-950 text-gray-300 py-16 px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-12">
      <div>
        <img src="{{brand_logo}}" class="h-8 mb-4 invert" alt="{{brand_name}}" />
        <p class="text-sm text-gray-400">{{brand_tagline}}</p>
      </div>
      <div>
        <h4 class="text-white font-semibold text-sm mb-4">Shop</h4>
        <a href="/collections" class="block text-sm py-1.5 text-gray-400 hover:text-white">All Products</a>
      </div>
      <div>
        <h4 class="text-white font-semibold text-sm mb-4">Newsletter</h4>
        <form data-lx-footer="newsletter-form" class="flex">
          <input data-lx-footer="newsletter-input" type="email" placeholder="your@email.com" class="flex-1 px-3 py-2 bg-gray-900 border border-gray-700 text-sm text-white rounded-l" />
          <button type="submit" class="px-4 py-2 bg-white text-black text-sm font-medium rounded-r">→</button>
        </form>
        <p data-lx-footer="newsletter-success" style="display:none" class="text-sm text-green-400 mt-2"></p>
      </div>
    </div>
    <div class="max-w-7xl mx-auto mt-10 pt-6 border-t border-gray-800 text-sm text-gray-500">
      © <span data-lx-footer="year"></span> All rights reserved.
    </div>
  </footer>
</div>
```

### SiteHeader — Hydration Mode

Combines announcement + navbar. Uses BOTH `data-lx-header` and `data-lx-nav` tags.

**Required tags:** `data-lx-header="root"` + same nav tags as Navbar

```html
<div data-island="SiteHeader" data-props='{"sticky":true,"announcement":{"messages":["Free shipping over $75","New summer collection"],"dismissible":true},"navbar":{"logo":{"src":"BRAND_LOGO_URL"},"links":[]}}'>
  <header data-lx-header="root" class="fixed top-0 w-full z-50">
    <div data-lx-header="announcement" class="bg-black text-white text-center py-2 text-xs relative">
      <span data-lx-header="announcement-text">Free shipping over $75</span>
      <button data-lx-header="announcement-dismiss" class="absolute right-3 top-1/2 -translate-y-1/2">&times;</button>
    </div>
    <nav class="bg-white border-b">
      <!-- Same data-lx-nav tags as Navbar example above -->
    </nav>
  </header>
</div>
```

### Tag Reference

| Tag | Islands | Behavior |
|-----|---------|----------|
| `data-lx-nav="root"` | Navbar, SiteHeader | Sticky/scroll attaches here |
| `data-lx-nav="cart-trigger"` | Navbar, SiteHeader | Click → open cart drawer or navigate |
| `data-lx-nav="cart-count"` | Navbar, SiteHeader | textContent auto-updated from $cartLines |
| `data-lx-nav="mobile-trigger"` | Navbar, SiteHeader | Click toggles mobile-panel .lx-open class |
| `data-lx-nav="mobile-panel"` | Navbar, SiteHeader | Toggle target for mobile menu |
| `data-lx-nav="dropdown-trigger"` | Navbar, SiteHeader | Hover shows dropdown-panel |
| `data-lx-nav="dropdown-panel"` | Navbar, SiteHeader | Shown/hidden on hover (same parent) |
| `data-lx-footer="root"` | Footer | Root element |
| `data-lx-footer="newsletter-form"` | Footer | Form submit → POST endpoint |
| `data-lx-footer="newsletter-input"` | Footer | Email input |
| `data-lx-footer="newsletter-success"` | Footer | Shown after successful submit |
| `data-lx-footer="year"` | Footer | textContent = current year |
| `data-lx-header="root"` | SiteHeader | Root + spacer via ResizeObserver |
| `data-lx-header="announcement"` | SiteHeader | Hidden on dismiss |
| `data-lx-header="announcement-text"` | SiteHeader | Rotates through messages[] |
| `data-lx-header="announcement-dismiss"` | SiteHeader | Click hides + persists to sessionStorage |

### Validation (Publish Blocks If Missing)

The publish validator enforces required tags when hydration mode detected:
- Navbar/SiteHeader: `root` + `cart-trigger` + `cart-count` + `mobile-trigger` + `mobile-panel`
- Footer: `root`
- Cart tags skipped if `hideCart: true` in props

---

# Style Packs — Named `data-part` CSS Bundles

> Scope every rule in a pack to its section id, as
> `references/island-presets.md` does with `#{{id}} [data-part=...]`. An
> unscoped `[data-part]` selector becomes page-global once compiled. Any
> accent-tinted `box-shadow` in a pack is a glow and is banned by
> `references/design-rules.md` N7 regardless of its offsets.

> House rules in `storefront-engine/references/design-rules.md` override every example below.
> Examples show structure and copy intent; their styling (gradients, hover transforms,
> uppercase labels, pills, emoji, section fills) is illustrative and must not be copied.
> Where an example conflicts with a house rule, the rule wins.

> Pre-tested visual treatments for rendered-mode islands. Pick ONE pack per page and paste its island overrides into the relevant sections' `<style>` blocks. Packs only touch visual properties (radius, borders, shadows, typography case/tracking) via `[data-part]` selectors and `--lx-*` variables — never layout. For fully custom island markup use headless mode instead (source-format.md).

## Choosing

| Pack | Feel | Best for |
|---|---|---|
| `editorial` | serif confidence, hairline rules, generous air | premium skincare, fashion, coffee |
| `soft-luxury` | pill shapes, soft shadows, muted warmth | beauty, wellness, jewelry |
| `brutalist` | hard edges, thick borders, high contrast | streetwear, drops, gen-z brands |
| `playful` | big radii, bouncy hovers, chunky buttons | kids, snacks, novelty, pets |
| `minimal` | flat, monochrome, quiet CTAs | tech accessories, tools, minimal brands |

## editorial

```css
[data-part="cta"] { border-radius: 0; text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.85rem; padding: 1.1rem 2.5rem; }
[data-part="variant-btn"] { border-radius: 0; border-width: 1px; text-transform: uppercase; letter-spacing: 0.08em; font-size: 0.75rem; }
[data-part="heading"] { font-family: var(--lx-font-heading); font-weight: 400; letter-spacing: -0.01em; }
[data-part="item"] { border: none; border-bottom: 1px solid var(--lx-border-color); border-radius: 0; }
[data-part="badge"] { border-radius: 0; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.65rem; }
```

## soft-luxury

```css
[data-part="cta"] { border-radius: 9999px; box-shadow: 0 8px 24px color-mix(in srgb, var(--lx-accent-color) 35%, transparent); padding: 1rem 2.75rem; }
[data-part="variant-btn"] { border-radius: 9999px; border-color: var(--lx-border-color); }
[data-part="item"] { border-radius: 1.25rem; border: 1px solid var(--lx-border-color); box-shadow: 0 2px 12px rgb(0 0 0 / 0.04); }
[data-part="badge"] { border-radius: 9999px; }
[data-part="trust-badges"] { opacity: 0.75; }
```

## brutalist

```css
[data-part="cta"] { border-radius: 0; border: 3px solid var(--lx-text-color); box-shadow: 4px 4px 0 var(--lx-text-color); text-transform: uppercase; font-weight: 800; }
[data-part="cta"]:hover { background: var(--lx-accent-color-hover); }
[data-part="variant-btn"] { border-radius: 0; border: 2px solid var(--lx-text-color); font-weight: 700; }
[data-part="item"] { border: 2px solid var(--lx-text-color); border-radius: 0; box-shadow: 4px 4px 0 var(--lx-border-color); }
[data-part="badge"] { border-radius: 0; border: 2px solid var(--lx-text-color); font-weight: 800; }
```

## playful

```css
[data-part="cta"] { border-radius: 1.25rem; font-weight: 800; padding: 1.1rem 2.5rem; transition: background-color 150ms ease; }
[data-part="cta"]:hover { background: var(--lx-accent-color-hover); text-decoration: underline; }
[data-part="variant-btn"] { border-radius: 1rem; border-width: 2px; font-weight: 700; }
[data-part="item"] { border-radius: 1.5rem; border: 2px solid var(--lx-border-color); }
[data-part="badge"] { border-radius: 9999px; font-weight: 800; }
```

## minimal

```css
[data-part="cta"] { border-radius: 0.375rem; box-shadow: none; font-weight: 500; }
[data-part="variant-btn"] { border-radius: 0.375rem; border-color: var(--lx-border-color); font-weight: 400; }
[data-part="item"] { border: none; border-radius: 0.5rem; background: var(--lx-surface-alt); box-shadow: none; } /* --lx-surface-alt is a component tint, never a section background */
[data-part="badge"] { border-radius: 0.25rem; font-weight: 500; }
[data-part="trust-badges"] { filter: grayscale(1); opacity: 0.6; }
```

## Rules

1. One pack per page — mixing packs is the #1 way to make a page look broken.
2. Scope to a section if two islands need different treatments: `#hero [data-part="cta"] { ... }`.
3. Packs compose with `lexsis_brand.compile_theme` output — they reference `--lx-*` variables, never hardcode colors.
4. Check the island's `schema.json` `parts` array before targeting a part name (`lexsis_design.island_schema`).
5. Packs never override `design-rules.md`.

---

# Asset Pipeline — Multi-Source Visual Strategy

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

> **Inputs:** A standalone asset brief or an existing page workspace
> **Outputs:** Verified permanent asset bindings
> **When to load:** During `/design-page` asset selection or an independent
> `/asset-prep` request.

---

## Decision Tree

```
Need an image or video for a section?
│
├─ lexsis_asset_library({ action: "search", args: { query, workspace_id, theme_id } })
│  → found good match?
│  ├─ YES → use it (free, on-brand)
│  └─ NO ↓
│
├─ Product shot needed?
│  ├─ YES → use real images from lexsis_catalog action list/get
│  └─ NO ↓
│
├─ What type of asset?
│  ├─ Static image (background, lifestyle, texture, composite)
│  │  └─ lexsis_drafts action asset_generate
│  │
│  ├─ Video (hero, demo, UGC-style)
│  │  └─ External MCP: HiggsField / Runway / Kling
│  │
│  ├─ Reference/mood imagery (competitor screenshots, inspiration)
│  │  └─ External MCP: Exa (web_search_exa)
│  │
│  ├─ Stock photography (realistic, non-AI look needed)
│  │  └─ External MCP: Unsplash / Pexels
│  │
│  └─ Specialized illustration (custom style beyond built-in)
│     └─ External MCP: OpenArt
│
└─ After sourcing → lexsis_asset_import action import
```

---

## Built-In Tools (Lexsis AI MCP)

| Tool | What it does | Cost |
|------|-------------|------|
| `lexsis_asset_library` → `search` | Search workspace assets | Free |
| `lexsis_drafts` → `asset_generate` | Generate, composite, inpaint, or restyle | Credits |
| `lexsis_assets` → `view` | Verify an asset | Free |
| `lexsis_asset_import` → `import` | Import exactly one source: URL, image base64 plus MIME type, or conversation attachments; never opens UI | Free |
| `lexsis_asset_upload` → `upload` | Open the local image/video upload panel; wait for the user's uploaded-asset message with the resulting asset id and URL | Free |

Ask the user whether they want to pick from the library before searching; an empty `query` browses and opens the asset picker (`Design asset selection:` carries `asset_ids` and `selection_order`). Pass `workspace_id` explicitly when multiple workspaces
are available and the selected `theme_id` whenever the discovered action
schema supports it.

For import, supply exactly one of `url`, image `data` + `mime_type`, or a
non-empty `attachments` array with `attachment_id` per entry. Never call
import without a source. For the upload UI, call `lexsis_asset_upload` with
`action: "upload"` and only `workspace_id` and `theme_id` in `args`.
Opening the panel does not import an asset. Wait for the user's uploaded-asset
message; if inline UI is unavailable, ask for a URL or conversation attachment
and use `lexsis_asset_import` with `action: "import"` instead.

See `design-enrichment.md` for detailed prompt patterns, style selection guide, compositing recipes, and HTML placement patterns.

---

## External MCPs (Detected at Runtime)

These tools are available when the user has the corresponding MCP installed. Check availability before suggesting.

### Exa — Image Research & Reference

```
web_search_exa({ query: "skincare brand hero photography editorial style" })
```

Use for: mood boards, competitor visual research, finding reference imagery to brief `lexsis_drafts` action `asset_generate` more precisely, sourcing real lifestyle photos.

**Flow:** Exa search → find URL → `lexsis_asset_import` action `import` → use
the returned permanent URL.

### HiggsField / Runway / Kling — Video Generation

Use when: TikTok traffic source, fashion/luxury vertical, product demo needed, brand has no existing video content.

**Flow:**
1. Generate video via external MCP (short clip, 3-8 seconds)
2. `lexsis_campaigns.frames` → pull best frame as thumbnail
3. Use video URL in HeroMedia island or `<video>` tag
4. Set click-to-play; a muted loop is allowed only as the plan's single motion moment (`references/assets/video-rules.md`)

**Video placement patterns:**
- Hero: click-to-play with compelling thumbnail image
- Product demo: inline player after benefits section
- Social proof: UGC-style video carousel
- Background: muted loop, heavily dimmed (luxury only)

### OpenArt — Specialized AI Illustration

Use when: `lexsis_drafts(action: "asset_generate", args: style: "illustration")` doesn't provide enough control over style, need specific artistic direction, or brand has a custom illustration language.

### Unsplash / Pexels — Stock Photography

Use when: brand has no library assets, AI generation looks too synthetic, need real-world photography (locations, hands, diverse models).

---

## Feeding External Assets Into Pages

All external assets MUST be persisted before use:

```
1. Source asset via external MCP → get URL
2. lexsis_asset_import({
     action: "import",
     args: { url, purpose: "hero_bg", tags: ["lifestyle", "summer"], workspace_id, theme_id }
   })
   → returns { asset_id, url, width, height }
3. Use returned URL in page HTML (same as built-in assets)
```

This ensures: the asset is stored in the brand's library, available for reuse, and won't break if the external source goes down.

---

## Per-Page-Type Asset Budget

| Page Type | Hero (high) | Supporting imagery (medium) | Lifestyle (medium) | Video | Total assets |
|-----------|-------------|---------------------|--------------------|----|------|
| PDP | 1 | 0-1 | 1 | 0-1 | 2-4 |
| Landing | 1 | 2-3 | 0-1 | 0-1 | 3-5 |
| Homepage | 1 | 1 | 0 | 0 | 2 |
| Editorial | 1 | 3-4 | 2-3 | 0-1 | 6-9 |
| Collection | 0-1 | 0 | 0 | 0 | 0-1 |
| Bundle | 1 | 1 | 0 | 0 | 2-3 |

**Rules:**
- Check `lexsis_workspace` action `credits` before generation
- Use `quality: "medium"` default; `"high"` only for hero images
- Products have their own Shopify images — never generate product shots

---

## Video in Pages

### When Video Converts Better
- TikTok/Reels traffic (video-native audience)
- Fashion/beauty (texture, movement, try-on)
- Luxury (cinematic brand storytelling)
- Product demos (85% say video convinced them to buy)

### Technical Integration
```html
<!-- Click-to-play video hero -->
<lx-island name="HeroMedia">
  <script type="application/json">
    { "type": "video", "videoSrc": "VIDEO_URL", "poster": "THUMBNAIL_URL", "autoplay": false }
  </script>
</lx-island>

<!-- Inline video (no island needed for simple playback) -->
<video class="w-full rounded-xl" poster="THUMBNAIL_URL" controls playsinline>
  <source src="VIDEO_URL" type="video/mp4" />
</video>
```

### Anti-Patterns
- NEVER autoplay video with sound; see `references/assets/video-rules.md` for the muted-loop exception
- NEVER use video as only hero content (needs fallback image)
- NEVER serve uncompressed video; use the imported CDN URL

---

## Compact Asset Record

After sourcing, update `page-manifest.json` and return:

```json
{
  "role": "hero",
  "sectionId": "hero",
  "sourceType": "lexsis",
  "assetId": "asset-uuid",
  "url": "https://cdn.trylexsis.com/assets/abc123.jpg",
  "status": "verified"
}
```

Shopify catalog media uses `sourceType: "shopify"` with `productId` and
`mediaId` instead of `assetId`. Never require a Lexsis asset ID for a Shopify
image.

Keep crop guidance, alt-text intent, prompts, and creative reasoning in the
plan or standalone asset brief. Asset names alone do not establish identity.
Visually inspect product, creator, and endorsement imagery. Generation uses
only permanent verified URLs.

---

## Cost Control

1. `lexsis_asset_library` action `search` first
2. `lexsis_workspace` action `credits` before expensive operations
3. Prefer `quality: "medium"` — reserve `"high"` for hero only
4. External MCP assets → `lexsis_asset_import` action `import`
5. The page background for sections that don't need imagery
6. Reuse: one hero image can serve as dimmed background for 2-3 sections

---

# Before Showing Draft to Merchant — QA Recipe

## Pre-flight Checklist

1. **Validate local artifacts** — run the shared page workspace validator
2. **Compile complete source** — `lexsis_pages` action `compile`
3. **Save as draft** — `lexsis_page_create` action `create` with `publish:false`
4. **Fetch and compare persisted source/content** — reject hash drift
5. **Check integrity** — `lexsis_pages` action `integrity`

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
- [ ] Interactive islands respond to clicks (FAQ accordion, BuyBox variant selection)
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

Write the result to `qa-report.md`, including source hash, remote version, copy
lint, claims review, asset verification, blockers, and publish readiness.

## Common Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| Gray product cards | Missing `image`/`media` in product data | Add image URLs or use `productIds` for auto-fetch |
| FAQ items don't toggle | Missing island hydration script | Ensure page includes island runtime |
| 401 on publish | OAuth session expired or revoked | Reconnect the MCP and complete browser OAuth |
| Insufficient scope on publish | Connection has Read or Build access | Reauthorize with Publish access after user approval |
| Images too large/slow | Using original Shopify CDN URLs | Append `&width=800` to resize |

## Draft vs Live

- `publish: false` → draft at `/v/{slug}?shop={domain}&preview=1`
- `lexsis_page_create` is draft-only and rejects `publish:true`
- Publish later with `lexsis_live_ops` action `publish` after explicit approval
- Draft edits do not replace the public `published_version_id`

---

# Storefront Publishing & Lifecycle

Manage page publishing, previews, and lifecycle.

## Publish Flow

1. Require local artifacts from `source-artifact-workflow.md`
2. Confirm the page's saved store/theme binding
3. `lexsis_pages` action `compile`
4. `lexsis_page_create` action `create` with `publish:false`
5. Fetch persisted source/content and record matching local and remote hashes
6. `lexsis_pages` action `integrity`
7. Verify the hosted draft at 390px, 768px, and 1280px, then run commerce QA
8. Recheck remote version and local synchronization
9. `lexsis_live_ops` action `publish` after explicit approval

## Operations

### Create Draft (New Page)
```
lexsis_pages({ action: "compile", args: { source, head, theme_css, scripts } })
lexsis_page_create({ action: "create", args: { source, head, theme_css, scripts, slug, publish: false } })
```
Returns: page_id, page_url, preview_url

### Preview (Draft)
```
lexsis_page_create({ action: "create", args: { source, head, theme_css, scripts, slug, publish: false } })
```
Returns: preview_url (not visible to store visitors)

### Publish Existing Page
```
lexsis_live_ops({ action: "publish", args: { page_id } })
```
Promotes the exact reviewed version to `published_version_id`.

### Unpublish
```
lexsis_live_ops({ action: "unpublish", args: { page_id } })
```
Takes page offline but preserves it in DB.

Use the experiment workflow for duplication and variants so each remote page
has its own local source and manifest first.

## Prerequisites

- The manifest's store and theme exist in the saved one-time setup
- Current permissions and store entitlement are read live
- Require `qa-report.md` with no blocking failures
- Require local source, page theme, remote bundle, and remote version to match
  the manifest baseline

Edits to a published page remain draft-only until publish succeeds. A failed
republish keeps the prior public version live.

## Post-Publish

After publishing, the page is served via:
- Shopify store (native page)
- pages.lexsis.app (standalone via edge worker)
- Custom domain (if tracking domain configured)

---

# Storefront Page Generation

> **Full workflow:** See `generation-protocol.md` for Phases 1-5 execution (context gathering, HTML generation, validation, publishing, visual verification).

Use `source-artifact-workflow.md` for the local working directory, static
visual-reference placeholders, readable canonical source, synchronization, and
section-patch policy.

This file covers quick-reference patterns for generation.

---

## Template-First Rule

Always search `lexsis_template_library.search_sections` before generating sections from scratch. It returns metadata only — fetch markup for the ids you pick with `lexsis_design.get_section`:

```
lexsis_template_library.search_sections({ query: "hero with video background for fashion", section: "hero", industry: "fashion", mood: "editorial" })
lexsis_design.get_section({ ids: ["<chosen id from results>"] })
```

- If a suitable template is found: fetch and use it. The fetched `source`
  contains the section markup, CSS, and JS ready to tailor with brand-specific
  copy/images, then pass to
  `lexsis_pages` action `compile`.
- If no match: generate from scratch in Phase 4.

Templates are conversion-proven, pixel-perfect, and faster than custom generation.
Use `format: "compiled_reference"` only to inspect renderer output; never paste its
`data-island` / `data-props` markup into source-authoring tools.

For a full page, check `lexsis_template_library.search_page_kits` before assembling sections one at a time — it returns curated multi-section groupings that already share one palette/vertical:

```
lexsis_template_library.search_page_kits({ query: "clinical supplements PDP", page_type: "pdp", industry: "supplements" })
```

---

## Page Type Section Defaults

**Product Landing (PDP)** — 8-10 sections:
Hero (split) → Gallery → BuyBox → Benefits → Ingredients/Specs → Reviews → Related Products → FAQ → Sticky CTA → Footer

**Campaign Landing** — 10 sections:
Hero → Problem/Pain → Solution → Key Benefits → Social Proof → How It Works → Comparison → Offer/Pricing → FAQ → CTA

**Homepage** — 7-8 sections:
Hero → Featured Products → Brand Story → Categories → Testimonials → Newsletter → Trust Bar → Footer

**Collection** — 6 sections:
Hero Banner → Filter/Sort → Product Grid → Promo Card → Social Proof → Footer

**Editorial** — 6-8 sections:
Full-Bleed Hero → Intro Copy → Shoppable Gallery → Content Block → Product Spotlight → Related Reads → Footer

**Listicle** — 7-9 sections:
Hero + TOC → Methodology → Numbered Items → Comparison Table → Verdict → FAQ → CTA

**Bundle** — 6-8 sections:
Hero + Savings Hook → Step Progress → Product Selection → Social Proof → FAQ → Sticky Summary

---

# Storefront Page Editing

Edit existing pages through canonical local source and section-level remote
operations. Read `source-artifact-workflow.md` first.

## Edit Flow

1. Open the local working directory. If an older page has no local files,
   create them from the current remote page once and record the synchronized
   baseline before editing.
2. `lexsis_pages` action `edit_context`
3. Compare its version with `manifest.remote.lastKnownVersion`; stop on drift.
4. Edit `lexsis-source.html`.
5. Run the local source gate and compile the complete source.
6. Compare current section hashes with the synchronized baseline.
7. Patch only changed sections with `expected_version`,
   `expected_source_sha256`, and an idempotency key.
8. Update manifest version/hashes after success, then run `diff` and `integrity`.

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

- Never make the remote page the only copy of an intentional change
- Always call `lexsis_pages` action `edit_context` before a write
- Stop on unexpected version drift
- Re-read source and reconcile locally when an edit returns `version_conflict`
- Reference section IDs from the page data (don't guess)
- Compile the complete local source before section patching
- After editing, run `diff` and `integrity`
- Batch related multi-section changes with `page_patch` so they create one
  version.
- Use explicit remove operations for absent properties. `null` remains a JSON
  value and is not deletion.
- When changing a collection binding, setting `products` removes `productIds`
  and setting `productIds` removes `products`; never send both.
- Reusing an idempotency key with the same request returns the original result.
  Reusing it with different content is an error.
- Update local hashes and manifests only after a successful remote write.
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout

Minor edits do not repeat planning, but they still require a local source
workspace and a matching saved store/theme setup. Adoption creates page files;
it does not rerun `setup`.

For published pages, `current_version` can advance while the live renderer
remains pinned to `published_version_id`. Publish only after QA.

## Applying Reusable Sections

Read `merchant-templates.md`. `template_apply` follows the same edit
preconditions and materializes source into the page. After success, fetch edit
context, update the local source and hashes, then run `diff` and `integrity`.

---

# Storefront Page Files

Use local files to pass work between commands without depending on chat
history.

## Workspace

```text
work/campaigns/<campaign-slug>/pages/<page-handle>/
├── page-plan.md
├── page-manifest.json
├── lexsis-source.html
├── page-theme.css
├── compile-artifact.json
├── qa-report.md
└── assets/
```

Files appear progressively. Planning creates only the plan, compact manifest,
and assets directory. Design creates source, CSS, a compile artifact, and the
unpublished hosted draft. Generation creates or updates the QA report and
remote synchronization state.

## Compact Manifest

Use `schemaVersion: 3`.

The manifest is a machine state ledger. Store only:

- page, workspace, store, and theme IDs
- compact inferred workflow intent and any user override
- selected template and section IDs
- compact product and final asset bindings
- section order and compact island schema evidence
- approved local hashes
- remote page ID, version, hashes, and section hashes
- compact QA status

Do not store copy intent, claims research, template-search transcripts,
omitted-component explanations, generation prompts, crop prose, or QA
narrative. Those belong in `page-plan.md`, an asset brief, or `qa-report.md`.

Do not prefill future stages with null fields.

## Design State

`/design-page` adds:

```json
{
  "config": {
    "head": {},
    "scripts": [],
    "productBinding": {},
    "commerceConfig": {}
  },
  "assets": [],
  "islands": [],
  "design": {
    "status": "pending-approval",
    "stylePack": "editorial",
    "compiledStyleManifest": {},
    "sourceHash": "...",
    "themeCssHash": "...",
    "configHash": "...",
    "structureHash": "...",
    "bundleHash": "...",
    "compiledBundleHash": "..."
  }
}
```

`lexsis-source.html` and `page-theme.css` are the only editable design inputs.
`compile-artifact.json` is generated. The hosted draft is the only interactive
preview and the renderer source of truth.

## Remote State

Immediately after unpublished creation, `/design-page`, `/build`, or
`/generate` adds:

```json
{
  "status": "draft_created",
  "workflow": {
    "intentMode": "fast-draft",
    "intentConfidence": "high",
    "intentSignals": ["requested a preview"],
    "userOverride": false
  },
  "sync": {
    "lastCompiledBundleHash": "..."
  },
  "remote": {
    "pageId": "...",
    "lastKnownVersion": 1,
    "previewUrl": "https://..."
  },
  "qa": {
    "status": "pending"
  }
}
```

This state is `DRAFT_CREATED`; it does not claim remote synchronization or
hosted QA.

After production-ready verification, `/generate` upgrades the state:

```json
{
  "status": "qa_passed",
  "sync": {
    "lastCompiledBundleHash": "...",
    "lastSyncedBundleHash": "...",
    "lastSyncedSectionHashes": {},
    "lastChangedSections": [],
    "remoteSourceHash": "...",
    "remoteBundleHash": "..."
  },
  "remote": {
    "pageId": "...",
    "lastKnownVersion": 1,
    "previewUrl": "https://..."
  },
  "qa": {
    "status": "passed",
    "version": 1,
    "bundleHash": "...",
    "checks": {
      "responsive": true,
      "visualRegression": true,
      "commerce": true,
      "copy": true,
      "claims": true,
      "assets": true,
      "integrity": true
    }
  }
}
```

Detailed screenshots, interaction results, blockers, and publish readiness stay
in `qa-report.md`.

## Synchronization

For creation, use the clean design compile artifact when its input hashes still
match. Recompile only after an input changes. After draft creation, fetch the
persisted source and remote bundle and reject hash drift.

`lexsis_page_create` action `create` consumes the `compile_id` directly, so a
normal build never fetches the bundle itself. `lexsis_pages` action
`compile_artifact` retrieves a stored bundle by `compile_id` for inspection
only, and `lexsis_drafts` action `page_attach_bundle` exists solely to recover
a page whose source was stored but whose bundle attachment failed (pass
`expected_version`).

For editing:

1. Fetch the remote version and stop on drift.
2. Change local source first.
3. Compile only if an input changed.
4. Compare section hashes.
5. Patch only changed sections with `expected_version`.
6. Update synchronization state only after success.

Legacy schema-v1 and schema-v2 workspaces use
`skills/generate/scripts/migrate_page_workspace_v3.py`. Existing local preview
files and hydration fields are ignored for compatibility; they are never
required or regenerated.

---

# Design Page Workflow

`/design-page` turns an approved one-page section plan into canonical Lexsis
source and one unpublished hosted draft.

It owns:

- existing-asset inventory and the single generation decision
- responsive layout and copy composition
- island selection and schema resolution
- `lexsis-source.html` and `page-theme.css`
- one clean compile artifact and hosted preview URL
- hosted 390px and 1280px approval

The plan supplies section intent, not islands. `/generate` supplies tablet and
full real-commerce QA.

Local and temporary placeholder assets are not allowed. Source must use
permanent Lexsis or Shopify media before draft creation.

An optional `/asset-prep` run may replace or improve media, but it is not a
required handoff. Any visible replacement returns the design to
`changes-pending-approval`.

---

# Public Storefront Workflow

The customer-facing pack has twelve commands. Five form the normal page
journey:

```text
/setup
  → /plan-page
  → /design-page
  → /generate
  → /publish
```

| Command | Owns | Main output |
|---|---|---|
| `setup` | Saved store and theme design context | `setup.json` and design files |
| `plan-page` | One-page campaign and section strategy | approved `page-plan.md` |
| `design-page` | Assets, islands, source, compile, and hosted design review | `DRAFT_CREATED` or `DESIGN_APPROVED` |
| `generate` | Draft creation when needed, then synchronization and hosted QA | `DRAFT_CREATED` or `DRAFT_READY` |
| `publish` | Explicit live release | published version |

Seven optional commands support the workflow:

| Command | Owns |
|---|---|
| `analyze-page` | URL, screenshot, ad, or own-page analysis |
| `asset-prep` | Independent asset search, generation, import, or replacement |
| `optimize` | Outcome-led existing-page improvement |
| `ab-test` | URL-first controlled variants and experiment evaluation |
| `cart` | Cart profile inspection, assignment, and editing |
| `build` | Fast unpublished draft from a prompt or selected/automatic page kit |
| `build-with-template` | Fast unpublished draft from an explicit template URL |

## Rules

1. Each command owns one outcome and can be invoked independently.
2. Commands read artifacts from earlier steps but never invoke earlier steps
   automatically.
3. Explicit skips are recorded in the page manifest.
4. Every page binds one saved store/theme pair.
5. `lexsis-source.html` is the production source of truth.
6. Draft creation is not publishing approval.
7. Infer fast-draft versus production-ready intent from the whole request;
   reversible ambiguity defaults to fast-draft.
8. A visual concept is optional evidence inside `design-page`, not production
   page media.
9. Design and fast-build routes create `DRAFT_CREATED`; `generate` reuses that
   draft and owns upgrading it to `DRAFT_READY`.

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

An offline prototype does not update the normal page manifest or replace the
standard Lexsis workflow.

### Individual capability unavailable

Continue only when the current skill defines a safe equivalent. Record the
capability, fallback, and limitation.

Examples:

- No suitable template result: custom composition is allowed after recording
  the searches and rejection reason.
- One island lacks safe preview data: static fallback is allowed for that
  island during visual review.
- Island schema or production compilation fails: do not mark the page
  production-ready.

## Result Evidence

When useful for diagnosis, a Lexsis-dependent command result or `qa-report.md`
reports:

- MCP connection status
- capabilities and resolution method used
- Lexsis router actions called
- selected template or reason for custom composition
- live product and asset bindings used
- fallbacks used
- blocking limitations

Do not store discovery logs, capability inventories, action transcripts, or
connection status in `page-manifest.json`. The manifest is a compact workflow
state ledger.

`setup` has no page manifest, so it returns this evidence directly with its
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

Use Templates → My templates for the user-owned library. Use the Design Library
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

The renderer already supplies its reset, base typography, smooth scrolling,
and shared keyframes:

`fadeUp`, `fadeIn`, `scaleIn`, `slideInLeft`, `slideInRight`, `marquee`,
`float`, `shimmer`, `wordFade`, and `pulseRing`.

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

If the catalogue marks an island deprecated or superseded, follow its
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
- `/design-page` inspects 390px and 1280px when approval is requested.
- `/generate` adds 768px, synchronization evidence, and full commerce QA.

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
and evaluated alternatives in `page-plan.md`, not the manifest. After
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
file. `/design-page`, `/build` and `/generate` re-read the same file. Each
type file follows `references/page-types/_checklist-format.md` and ends with
a JSON checklist that `plan-page/scripts/plan_lint.py` enforces.

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
├── no ─ what is the job?
│   ├── answer questions / route to the right product ........... quiz-funnel
│   ├── leave an email or phone (giveaway, waitlist, early access)
│   │   ├── product not yet purchasable ....................... launch-waitlist-preorder
│   │   └── incentive or contest ............................... lead-capture-giveaway
│   ├── read a story, learn who we are ......................... brand-story-founder
│   ├── understand the science, ingredients, materials, method . ingredient-science
│   ├── browse many products
│   │   ├── whole store, first visit ........................... homepage
│   │   ├── one category or collection ......................... collection-landing
│   │   ├── by recipient or price for a holiday ................ gift-guide
│   │   └── outfits, rooms, looks with shoppable items ......... lookbook-shop-the-look
│   ├── get help, policies, answers ............................ faq-support-led
│   ├── refer a friend, join a programme, see tiers ............ referral-loyalty-vip
│   ├── just paid; what next .................................... thank-you-post-purchase
│   └── order in volume for resale ............................. wholesale-b2b
└── yes ─ has the visitor already seen this product or brand?
    ├── no (cold) ─ what brought them?
    │   ├── a social ad with a story or problem hook (meta, tiktok, native)
    │   │   ├── long-read wanted, price hidden until late ...... advertorial
    │   │   ├── "N reasons / best X" list framing ............. listicle
    │   │   ├── creator or customer video is the hero .......... ugc-creator-collab
    │   │   ├── one long video does the selling ................ video-sales-page
    │   │   └── direct-response, single product, single CTA .... ad-landing-page
    │   ├── a search for the product or category (google, shopping)
    │   │   ├── "X vs Y", "alternatives" ....................... comparison-us-vs-them
    │   │   ├── "best X", "top N X", buyer's guide, roundup ..... seo-buyers-guide
    │   │   └── product or category intent ..................... pdp (search-intent variant)
    │   └── a sample, trial or starter offer ................... trial-sample
    └── yes (warm or hot) ─ what is the page selling?
        ├── one product at full price, full store context ....... pdp
        ├── one product, paid-traffic focus, no navigation ...... pdp-hybrid-landing
        ├── two or more products as a set or configurator ....... bundle-kit
        ├── a recurring plan ..................................... subscription
        ├── a specific discount, code, GWP or BOGO .............. offer-page
        ├── many products at reduced prices for a window ........ sale-clearance-flash
        ├── an occasion or holiday assortment .................... seasonal-gifting
        ├── a product that is back or newly available ............ restock
        └── a return visit after abandonment or a prior view ..... retargeting-warm
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
| `ad-landing-page` | Single product, single CTA, message-matched to a paid ad | tof/mof | problem→product | meta, tiktok, google | 8–11 | 3 | 2–4 | none |
| `pdp` | Full product page inside the store; gallery, buy box, details, reviews | mof/bof | product/most | organic, search, email, nav | 7–11 | 2 | 2–4 | full |
| `pdp-hybrid-landing` | PDP anatomy with landing-page focus: no nav, ad message match, one goal | mof | solution→product | meta, google shopping | 8–11 | 2–3 | 2–4 | none |
| `advertorial` | Editorial article that sells by story; price and CTA arrive late | tof | unaware/problem | meta, native, tiktok | 8–12 | 1–3 | 2–4 | none |
| `listicle` | Numbered reasons for one product; each reason answers an objection and earns a click | tof/mof | problem/solution | meta, tiktok | 8–13 | 3–6 | 2–4 | none/minimal |
| `seo-buyers-guide` | Search-intent roundup or "best X" guide: TOC, methodology, ranked entries, comparison table | tof/mof | problem/solution | google organic, google ads | 9–14 | per entry + 1 | 2–4 | full |
| `comparison-us-vs-them` | Attribute table against named or generic alternatives | mof | solution/product | google, retargeting | 7–10 | 2–3 | 2–3 | minimal |
| `quiz-funnel` | Questions route the visitor to a recommendation | tof/mof | problem/solution | meta, tiktok, email | 4–7 | 1 + result | 1–2 | none |
| `bundle-kit` | Fixed or build-your-own set with visible savings math | mof/bof | product | email, pdp cross-link, ads | 7–10 | 2 | 2–3 | minimal/full |
| `offer-page` | One named promotion (code, GWP, BOGO, first order) | mof/bof | product/most | email, sms, retargeting | 6–9 | 2–3 | 1–3 | minimal |
| `sale-clearance-flash` | Many products, reduced prices, real window | bof | most | email, sms, social | 5–8 | per card | 1–2 | full |
| `seasonal-gifting` | Occasion assortment with delivery cutoffs and gift options | mof | solution/product | email, social, search | 7–10 | per card + 1 | 1–3 | full |
| `gift-guide` | Curated picks by recipient or price band | tof/mof | solution | organic, email, social | 6–9 | per card | 1–2 | full |
| `launch-waitlist-preorder` | Not yet buyable: capture intent or take pre-orders | tof/mof | problem/solution | email, social, PR | 6–9 | 1–2 | 1–3 | minimal |
| `restock` | Product is back; convert the demand already there | bof/retention | most | email, sms | 5–7 | 2 | 1–2 | minimal |
| `subscription` | Recurring plan; cadence, savings, cancellation clarity | mof/bof | product | pdp, email, ads | 7–10 | 2 | 2–3 | minimal/full |
| `ugc-creator-collab` | Creator or customer content is the hero and the proof | tof/mof | problem/solution | tiktok, instagram, influencer | 6–9 | 2–3 | 3–5 | none |
| `video-sales-page` | One long video, then the offer | tof/mof | problem/solution | meta, youtube, email | 5–8 | 1–2 | 1–3 | none |
| `brand-story-founder` | Who we are and why; sells belief, not a SKU | tof/retention | unaware/problem | organic, nav, PR | 6–9 | 1–2 | 1–2 | full |
| `ingredient-science` | Mechanism, ingredients, materials, studies | mof | solution/product | organic, pdp link, google | 7–10 | 1–2 | 2–4 | full |
| `collection-landing` | One category; grid with filters and a short story | mof | solution | organic, nav, google | 5–8 | per card | 1–2 | full |
| `homepage` | Store front door; route to collections, best sellers, story | tof/retention | all | direct, organic, brand search | 7–10 | 2–3 | 2–3 | full |
| `lookbook-shop-the-look` | Editorial imagery with shoppable items | tof/mof | solution | instagram, organic, email | 5–8 | per look | 1–2 | full |
| `lead-capture-giveaway` | Email or SMS in exchange for an incentive | tof | unaware/problem | social, partner, ads | 3–6 | 1 | 1–2 | none |
| `referral-loyalty-vip` | Programme rules, tiers, rewards, join | retention | most | email, account, nav | 5–8 | 1–2 | 1–2 | full |
| `retargeting-warm` | Visitor saw it already; handle objections, restate offer | bof | product/most | meta/google retargeting | 5–8 | 2–3 | 2–4 | none/minimal |
| `thank-you-post-purchase` | Order confirmed; next steps, one relevant add-on, referral | retention | most | checkout | 3–6 | 1–2 | 0–1 | minimal |
| `faq-support-led` | Answers first; policies, shipping, sizing, care | mof/retention | product | organic, nav, support links | 4–7 | 1 | 0–2 | full |
| `trial-sample` | Low-risk first purchase; what happens after is explicit | tof/mof | solution | ads, email | 6–9 | 2 | 2–3 | minimal |
| `wholesale-b2b` | MOQ, tiers, lead times, line sheet, inquiry | mof | product | organic, outreach | 5–8 | 1–2 | 1–3 | minimal |

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

## 5. Awareness level → headline and page posture

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

Plan block (`page-plan.md`):

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

Manifest (`page-manifest.json`): `page.pageType`, `page.funnelStage`,
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
`/build` and `plan-page/scripts/plan_lint.py` can read it the same way. The
heart of each file is its `## Workflow`: the ordered thinking the model follows
for that type, section by section, with the asset decision, the island
decision and the tool call that settles each. The `## Checklist` JSON is the
default anatomy the workflow produces; deviate when the context calls for it
and note the deviation in the plan. House rules in `references/design-rules.md`
still apply to every page.

## How a skill uses a page-type file

1. `/plan-page` identifies the type with `references/page-types/_index.md`,
   records the `## Page type` block in `page-plan.md` and `page.pageType` in
   `page-manifest.json`, then loads only the matching file.
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
4. `python3 <plan-page-skill>/scripts/plan_lint.py <page-workspace>` prints
   the mechanical review (advisory by default; `--strict` exits non-zero).

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
One block per Anatomy section, in order:

**`<section id>`**
- Purpose: one line.
- Media: needs imagery yes/no; which image job(s); search order (catalog
  media, then the `lexsis_asset_library.search` tag, then semantic, then
  merchant-owned sources); every candidate is opened with
  `lexsis_assets.view` and judged against this section before it is used;
  generation purpose if nothing is found and the
  policy allows it; otherwise tell the merchant exactly what is missing and
  offer upload (`lexsis_asset_upload.upload`) or MCP generation when
  feasible. The section is skipped or merged only if the merchant chooses.
  Follows `references/workflows/section-asset-workflow.md`.
- Island: `none`, or the island name and the context that decides its
  configuration (image count, variant axes, review band, page length,
  vertical). Variants and props are not listed here; they are resolved live
  from `lexsis_design.islands` and `lexsis_design.island_schema` as
  `references/workflows/island-selection-workflow.md` describes.
- Copy: pattern and ceiling.
- Decide with: the data or tool call that settles the choices above.

### Asset budget
A table: what the catalog and library already supply for this type, which
jobs are usually missing, and for each missing job whether to reuse, generate
(with purpose) when the policy allows, or tell the merchant and offer upload
or generation. A missing asset is always reported to the merchant; a section
is skipped or merged only on the merchant's decision. Never fill a gap with a
colour band, emoji, icon tiles or a wall of copy; a section is imagery plus a
few words, or the merchant decides what happens to it.

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
| 0.2 | write "Proof sources" line in `page-plan.md` | source, count, sync date, tier reached | always, even when the answer is "none" |

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
| Body | `body` present | verbatim; `[…]` trim only; "Read more" reveals the full text |
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
Check: every `ReviewCarousel` or `ReviewList` `data-props` carries `collectionId` or `productIds`; any static `reviews[]` item id appears in the ledger.
```bash
perl -ne 'while(/data-island="Review[A-Za-z]*"[^>]*data-props=\x27([^\x27]*)\x27/g){print "unbound\n" unless $1=~/collectionId|productIds/}' $W/lexsis-source.html | wc -l   # 0
```

RS2. Run tiers in order and stop at the first tier that yields usable rows; never open tier 4 while tier 1 or 2 has data. OPERATOR.
Check: the plan's "Proof sources" line names the tier reached and the calls made.

RS3. Show an average only at n >= 5, always beside n, to one decimal, computed from all published ratings for the scope. RESEARCH [H] Baymard; LAW (a headline 5.0 from two ratings is misleading by omission, FTC 465.7, CMA "publishing in a misleading way").
Check: every rating string is followed by a count in the same element (review the hits; prices also match the pattern).
```bash
grep -oE '[0-5]\.[0-9](/5| out of 5)[^<]{0,40}' $W/lexsis-source.html | grep -vcE '[0-9][0-9,]* (reviews|ratings)'   # 0
```

RS4. Never show 5.0 unless every review is five stars and n >= 20; never show two decimals. HEURISTIC, mirrors `proof-ledger.md` display rule 3.
Check: `grep -c '5\.0' $W/lexsis-source.html` is 0 unless the ledger row records n >= 20 and a distribution of 100% five-star.

RS5. Show the distribution at n >= 20 (optional at 10 to 19, hidden below 10), expanded, every bar present including one-star, bars acting as mutually exclusive filters. RESEARCH [H] Baymard distribution summary.
Check: in the hosted draft the distribution element exists when the ledger's n >= 20 and lists five bars.

RS6. Recency gate: when the newest review is older than 12 months, do not place the average in the hero or buy box; render dated cards only. RESEARCH [M] PowerReviews (64% prefer fewer recent reviews), BrightLocal 2026.
Check: ledger `review-summary` row records newest date; if older than 12 months, section is not `hero`, `buy-box` or `review-summary`.

RS7. Never relabel a store-level aggregate as a product rating, never average bundle components into a bundle rating, never merge reviews across substantially different products or formulations. LAW FTC 465.3; CMA208 "porting"; FTC v. Bountiful ($600k, 2023).
Check: each `review-summary` row names the exact `product_id` or `collectionId` its numbers came from.

RS8. A `minRating` filter is allowed only on a carousel that is labelled as a selection ("Selected reviews"), links to the full list ("Read all n reviews"), and sits with an unfiltered avg + n. Never on the full list, never for `averageRating` or `totalReviews`. LAW FTC 465.7(b); DMCC banned practice 13.
Check:
```bash
grep -oE '"minRating":[[:space:]]*[2-5]' $W/lexsis-source.html | wc -l   # 0, or each carousel section also contains 'Read all' and the ledger avg + n
```

RS9. Negative reviews stay reachable: at n >= 20 at least one review rated 3 or lower is visible without filtering when one exists; sort default is disclosed in one line and does not bury low ratings. LAW FTC 465.7; FTC v. Fashion Nova ($4.2M, 2022); IS 19000 (no discouraging negatives). RESEARCH [H] Baymard: presence of negatives makes positives believable.
Check: hosted draft at 1280 shows the sort label and, for B3+, at least one card with rating <= 3 in the default view.

RS10. Render each review field only when the record contains it (field-gating table). Verified badge only with order linkage or Shop source. LAW EU Annex I 23b (verification is material information); Shopify Shop badge semantics.
Check: no `verified` prop set to true on a static item whose ledger row lacks order linkage; no `avatar` URL that is not the reviewer's own media.

RS11. Quote verbatim. Trim with `[…]` only; keep the reviewer's specifics (variant, timeframe, use); prefer a quote that includes a limitation; never stitch sentences from two reviews; never fix grammar. LAW CAP 3.47; Trustpilot "quote reviews exactly as written"; IS 19000 (administrator may not edit content).
Check: each `review-quote` body is a substring of the API record with `[…]` removed.

RS12. Render merchant replies when present, visually distinct and labelled as the store's reply. RESEARCH [H] Baymard: 37% weigh the reply; 87% of sites never reply.
Check: reply markup uses a distinct class and the label "Reply from <store>".

RS13. Label incentivised reviews on the card and beside the summary when the app flags them; incentives may never be conditioned on sentiment. LAW FTC 465.4 and 465.5; CMA208; Google review-snippet policy.
Check: if any record has the incentivised flag, `grep -c 'Incentivised' $W/lexsis-source.html` >= 2.

RS14. Review islands take `collectionId` or `productIds`, `minRating`, `pageSize` <= 12; `averageRating` and `totalReviews` come only from the API total for the same scope; never `reviewsEndpoint`; never `SocialProofPopup`. OPERATOR.
Check:
```bash
grep -cE 'SocialProofPopup|reviewsEndpoint|"pageSize":[[:space:]]*(1[3-9]|[2-9][0-9])' $W/lexsis-source.html   # 0
```

RS15. Only `active` collections bind to `collectionId`; a draft collection is `pending` until the merchant activates it. The plan never activates a collection. OPERATOR.
Check: the `collectionId` in source matches an id returned with `collection_status: "active"` on the plan date.

RS16. `reviews_search` hits are `pending` until the merchant confirms them or an active collection contains them. OPERATOR.
Check: every row with source `reviews_search` has status `verified` only with a confirmation note (question 9 answer or collection id).

RS17. In band B0 render nothing review-shaped. An external item reaches the page only as `external-verified` with a live URL, platform-permitted reuse, merchant written approval, and verbatim text. Marketplace review text (Amazon, Flipkart, Nykaa, Myntra) is never verbatim; Reddit is never used in ads. LAW Amazon Conditions of Use; Reddit User Agreement and Embeds Terms; CAP 3.45.
Check: no `review-*` kind in the ledger when `reviews_status` count is 0; each `external-verified` row has four evidence fields.

RS18. When B0 persists after tier 4, use tier 5 substitutes in order; "nothing" is an acceptable outcome. HEURISTIC.
Check: plan records the substitute chosen and why the higher rows were unavailable.

RS19. Never write, paraphrase, summarise as if quoted, or generate a review; never present staff or founders as customers; never reuse a review for a different product. LAW FTC 16 CFR 465.2 and 465.5; FTC v. Rytr 2024; FTC v. Sunday Riley 2020; India E-Commerce Rules 2020 r.5(2).
Check: `grep -ciE 'lorem|example review|sample review|\[name\]|\[city\]' $W/lexsis-source.html` is 0; no review text exists in source that is absent from the API.

RS20. Autoplay video reviews muted only; sound on tap; captions present. LAW WCAG 2.1 SC 1.4.2.
Check:
```bash
perl -ne 'print if /<video[^>]*autoplay(?![^>]*muted)/' $W/lexsis-source.html | wc -l   # 0
```

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
rows; `/generate` fails production QA on any proof element that is not in the
ledger; `/optimize` may add proof only by adding a row first. This file
defines the block, the verification each kind needs, and the display rules.
Sourcing procedures live in `references/proof/reviews-sourcing.md` and the
sibling files.

## The block

```markdown
## Proof ledger

| # | Kind | Supports claim | Source | Evidence | Verified | Section | Status |
|---|---|---|---|---|---|---|---|
| P1 | review-summary | overall quality | lexsis_catalog.reviews product gid://…/123 | 4.6 avg, 212 reviews, min rating 1 | API 2026-09-10 | review-summary | verified |
| P2 | review-quote | "no more 3pm crash" | collection 7f2e… item 9a1c… | verbatim text, name initial + city as stored, 2026-04-02 | API | benefits | verified |
| P3 | press-logo-linked | credibility | Vogue India | https://www.vogue.in/… (article names the brand) | fetched 2026-09-10 | press-marquee | verified |
| P4 | certification | "FSSAI licensed" | merchant | licence no. 1001…; issuer FSSAI | merchant doc | trust-bar | verified |
| P5 | ugc-video | in-use proof | creator @…, rights email 2026-08-21 | asset id … | merchant consent | ugc-grid | verified |
| P6 | customer-count | "50,000+ customers" | merchant | Shopify orders export, 51,204 unique customers to 2026-08-31 | merchant doc | stats | pending |
| P7 | before-after | "visible in 4 weeks" | merchant | none supplied | none | — | dropped |
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
| review-summary | `lexsis_catalog.reviews` total and average for the exact product or collection; count ≥ 5 to show an average, ≥ 1 to show a count | rounding 4.3 to 5.0; "5.0" with under 20 reviews; stars without a count |
| review-quote / review-list / review-with-media | row exists in `lexsis_catalog.reviews` or `review_collection_items`; text verbatim; attribution exactly as stored; date present | edited wording beyond `[…]` trimming; invented names, cities, photos; five identical five-star quotes |
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
| social-proof-popup, live-viewer-count, press-logo-unlinked | never verified; never rendered | — |

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
4. **Quotes.** Verbatim. Trim with `[…]` only. Keep the reviewer's own
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
    section appears in the ledger. `design_lint.py` lists them; the review
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

## Lint hooks

- `plan_lint.py` T9: a reviews section requires `manifest.reviews.available
  > 0` from an allowed source.
- `design_lint.py`: emoji stars (N1), fabricated pills (N9), numerals in
  proof sections (N11, manual), unlinked press logos (`<img>` inside a
  `press-marquee` section that is not wrapped in `<a href`), forbidden kinds
  (`SocialProofPopup`, "people are viewing", "bought in the last").

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

Plan (`page-plan.md`), one block after "## Asset slots":

```markdown
## Generation record

| Slot | Purpose | Aspect | Style / quality | Prompt (verbatim) | Negatives | Brand hexes | Provider | Asset id | Metadata set | Visible label | Approved by |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A3 | hero_bg | landscape + portrait | photography / high | "Unbleached linen surface, soft north window light, ..." | text, letters, logo, ... | #F5F0E6, #1F1D24 | lexsis | 2d9a... | TrainedAlgorithmicMedia | none | credits: merchant, 2026-09-10 |
| A7 | product_lifestyle | portrait | photography / medium | "..." | ... | ... | lexsis | 9f01... | CompositeSynthetic | "AI-generated scene" | "yes, generate A7" Aditi 2026-09-10 |
```

Manifest (`page-manifest.json`): the slot's `assets[]` entry gets
`"sourceType": "lexsis"`, `"assetId"`, `"url"`, `"generated": true`,
`"provider": "<provider>"`, and `role` equal to the purpose. For an approved
ASK slot the role is `product_lifestyle`, the entry also carries
`"askApproved": true`, and the merchant's words live in the plan record
(`plan_lint.py` T8 rejects an ASK role without that flag). Nothing else about
generation enters the manifest.

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

`$W` is the page workspace. `PEOPLE` is the regex
`\b(woman|women|man|men|girl|boy|person|people|model|customer|shopper|reviewer|hand|hands|face|smile|smiling|doctor|nurse|dermatologist|founder|team|staff|child|kid|baby|toddler|family|couple|influencer|creator)\b`.

GP1. Never generate anything in section 2; no instruction, design.md line or brief lifts the block. LAW.
Rationale: fake testimonials and misrepresented products carry regulatory penalties and platform rejection (sources in section 2).
Check: `python3 -c "import json;a=[x for x in json.load(open('$W/page-manifest.json'))['assets'] if x.get('generated')];print([x['slotId'] for x in a if x['role'] not in ('hero_bg','section_bg','card_bg','texture_fill','pattern_tile','decorative_element','product_composite','product_lifestyle','icon_set')])"` prints `[]`; every `product_lifestyle` row in the Generation record has a non-empty "Approved by".

GP2. Composite only over a real cut-out and leave the product pixels untouched. LAW, OPERATOR.
Rationale: a repainted product misleads about what ships (GN1); `references/design-enrichment.md` compositing recipes assume a real reference image.
Check: view the composite beside the source packshot with `lexsis_assets.view`; colour, shape and label identical (yes/no in `qa-report.md`); Generation record cites the reference asset id.

GP3. Give decorative generated images `alt=""` and `aria-hidden="true"`; give composites a product alt that names the product. LAW.
Rationale: W3C alt decision tree https://www.w3.org/WAI/tutorials/images/decision-tree/ .
Check: for each generated decorative URL `U`, `grep -c "src=\"U\"[^>]*alt=\"\"" $W/lexsis-source.html` is 1; for composites the alt contains the product name.

GP4. Never let people words appear in the alt text or prompt of a generated slot unless the ASK synthetic-model case was approved. LAW.
Rationale: 16 CFR 465; ASCI prohibited tier.
Check: `grep -oE 'alt="[^"]*"' $W/lexsis-source.html` filtered to generated slot URLs, then `perl -ne 'print if /PEOPLE/i'` prints nothing; the same regex over the Generation record prompts prints nothing unless the row's "Approved by" quotes the synthetic-model yes.

GP5. Never generate text into an image; every headline, price, label and badge is HTML. LAW.
Rationale: WCAG 1.4.5; Google and Shopify overlay rules (section 2).
Check: `perl -ne 'print if /\b(text|letters|typography|lettering|headline|price|label|badge|logo|caption)\b/i' <<< "<prompt>"` matches only inside the negative list; view the output for stray glyphs.

GP6. Place `hero_bg` and `section_bg` only in the plan's bold moment; keep one page background everywhere else. OPERATOR.
Rationale: N2 and N7 in `references/design-rules.md`; a generated band per section is the template tell those rules exist to stop.
Check: count of full-width elements with a generated background image is 0 or 1 and its section id equals the plan's "Bold moment" line (browser check from N2).

GP7. Record provenance three ways: metadata on the original, `generated: true` plus `provider` in the manifest, and the Generation record in the plan. LAW.
Rationale: Google requires `IPTC DigitalSourceType`; EU and ASCI labelling decisions must be auditable; hosts may strip file metadata.
Check: `exiftool -DigitalSourceType <original>` prints a value when the tool is available; `grep -c '"generated": true' $W/page-manifest.json` equals the Generation record row count.

GP8. Show a visible label wherever section 6 requires one and place it adjacent to the image. LAW.
Rationale: EU Art. 50 first-exposure labelling; ASCI medium tier.
Check: for every record row with a non-empty "Visible label", `grep -c '<label text>' $W/lexsis-source.html` is at least 1 within the same section.

GP9. Read credits and obtain a yes for the named batch before spending; cap generated assets at four per page. OPERATOR, HEURISTIC.
Rationale: `/design-page` authorises page creation, not generation; more than a few generated backdrops read as a template.
Check: `grep -c '"generated": true' $W/page-manifest.json` is 4 or fewer; the session shows `lexsis_workspace.credits` before the first generate call.

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

The canonical offer catalogue. `page-manifest.json` `offer.type` takes exactly
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
Check: `grep -c '<!-- section: offer' $W/lexsis-source.html` is 0 or 1 unless `page.pageType` is exempt.

OF2. Rule of 100. Always show the currency saving (offer-ledger rule 2). Under $100 or ₹8,000 the percent may lead ("32% off, save $28"); above it currency leads and percent is optional ("Save $128 (18%)"); never a percent without the currency amount on high-ticket goods. RESEARCH: Berger; JBR 2015 three-study replication. The ₹8,000 crossover is HEURISTIC.
Check: every `savings-math` line contains a currency figure; the leading figure matches the side of the line the ledger price falls on.

OF3. Luxury never shows percent, a struck price, a timer, "sale" or "clearance". Allowed ids: `none`, `gwp`, `free-shipping` (phrased "complimentary shipping", no threshold), `limited-edition`, `pre-order-price`, `price-lock`, `loyalty`, `gift-card`. RESEARCH and OPERATOR: Kapferer and Bastien anti-laws; Langer on price volatility and equity decay.
Check: when the plan loads `references/vertical-luxury.md`, `offer.type` is in the allowed list and `grep -ciE 'sale|% off|save [$₹£€]' $W/lexsis-source.html` is 0.

OF4. Bundle, tiered and BOGO pages show their arithmetic. `bundle`, `bundle-decoy`, `tiered-volume`, `bogo` require a `savings-math` or `quantity-breaks` section whose figures are ledger rows.
Check: `offer.type` in that set implies `grep -cE '<!-- section: (savings-math|quantity-breaks)' $W/lexsis-source.html` is at least 1.

OF5. "Free", "gift", "bonus" and "complimentary" appear only when the buyer pays nothing extra and the conditions sit in the same section (LAW, FTC 16 CFR 251.1; UK banned practice; EU UCPD Annex I.20).
Check: every section containing `\bfree\b` also contains the threshold, shipping cost or eligibility text; no `*` after "free".

OF6. No pre-ticked add-on, subscription, gift wrap, insurance, donation or upsell (LAW, India CCPA basket sneaking; ROSCA; EU CRD Art 22). Detail in `references/anti-patterns/dark-patterns.md`.
Check: `grep -cE '<input[^>]*checked' $W/lexsis-source.html` is 0 outside variant pickers.

OF7. The offer moves down the page as awareness falls. On `tof` page types the offer section index is greater than the `mechanism`, `how-it-works` or `solution` index; on `bof` types the offer is in the hero (`funnel-stages.md` FS4).
Check: compare section order in `page-manifest.json` against `page.funnelStage`.

OF8. Retargeting never shows a deeper discount than the visitor already saw, and never the first-order code (OPERATOR: trains abandonment).
Check: `page.pageType` is `retargeting-warm` implies `offer.type` is not `first-order` and the ledger notes the prior offer depth.

OF9. Free-offer frequency. A size or SKU carries a Free or BOGO offer no more than 6 months in any 12, with 30 days between offers and at most three per year (LAW, FTC 251.1(h)).
Check: ledger row for `bogo` or `gwp` records the months this year the offer has run on that SKU.

OF10. Compare-at is struck-through text only; no pills, ribbons or caps (design-rules N9).
Check: design-rules N9 grep returns 0.

OF11. Promise only what the discount configuration can do. Native BXGY does not auto-add the get item; a GWP auto-add needs a Discount Function; tiered pricing needs an app or Function; shipping discounts never combine with each other; at most 25 active automatic discounts (Shopify Help).
Check: ledger row O9 names the mechanic (code, automatic, Function, app) and the page instruction matches it.

OF12. Terms travel with the offer: exclusions, stacking, regions, code, minimum spend and cancellation terms within one scroll of the first offer mention (offer-ledger rule 4).
Check: the `legal` or `disclaimer` text for the offer is in the same or the next section as the first `offer`, `pricing` or `buy-box`.

OF13. Unknown market means the strictest rule: EU 30-day prior price, UK duration and volume, India MRP display and single-figure total.
Check: `page-manifest.json` has a market list, or the ledger notes "strictest applied".

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
`design_lint.py` runs the O1 to O4 checks. Offer-specific detail lives in
`references/offers/offer-ledger.md`, `references/offers/price-presentation.md`
and `references/offers/urgency-scarcity.md`; proof detail in
`references/proof/proof-ledger.md`. This file is the canonical list; the two
offer files and `references/consumer-behavior-cro.md` (Guardrails) point here.

Severity: BLOCK (legal exposure; the page does not ship), FAIL (fix before
publish), WARN (fix unless the plan records a reason). Tag: LAW (a regulator
names it), RESEARCH (usability evidence), OPERATOR (practitioner consensus),
HEURISTIC (this project's judgement).

Checks use `$W` for the page workspace (`work/campaigns/<campaign-slug>/pages/<handle>`) and
`$T` for the extracted text: `perl -pe 's/<[^>]+>/ /g' $W/lexsis-source.html > $T`.
Browser checks run in the hosted draft at 390 and 1280.

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
- Check. `grep -c '<lx-island name="Countdown' $W/lexsis-source.html` is 0, or `grep -ciE 'end date.*20[0-9]{2}-[0-9]{2}-[0-9]{2}' $W/page-plan.md` is at least 1 (lint O2). `grep -ciE '\b(ends? (soon|tonight|today|in)|last chance|limited time|hurry)\b' $T` is 0 (lint O1).

### DP2. Fake scarcity (stock)  BLOCK  LAW
- Definition. CCPA item 1(ii): "stating that quantities of a particular product or service are more limited than they actually are". FTC: "almost sold out" with ample supply. UK banned practice: pretending a product is available only for a very limited time.
- Example. "Only 3 left!" hardcoded in copy on a made-to-order item; "Low stock" badge on every variant.
- Rule. Stock statements come only from a live inventory binding (`lexsis_catalog.get` at render) and read the real count. "Limited edition" states the run size from the ledger. No stock words in static copy.
- Check. `grep -ciE '\b(only [0-9]+ left|low stock|almost gone|selling fast|limited stock|while (stocks|supplies) last)\b' $T` is 0 (lint O1). Any `stock-indicator` section requires `offer.stockVerified` in the manifest (plan_lint T10).

### DP3. Fake popularity (viewer and purchase counts)  BLOCK  LAW
- Definition. CCPA item 1(i): "showing false popularity of a product or service". FTC bucket I: false "others are viewing" and "recently purchased" notices. deceptive.design: fake social proof.
- Example. "23 people are viewing this" from a random-number script; "Priya from Mumbai just bought" popups with no order behind them.
- Rule. No viewer counts, activity feeds or "recently bought" toasts of any kind, even if fed by analytics; the proof vocabulary lists `social-proof-popup` and `live-viewer-count` as never rendered. Aggregate counts ("over 51,000 customers") only as verified proof-ledger rows.
- Check. `grep -ciE 'SocialProofPopup|people are viewing|viewing this|bought in the last|just (bought|purchased|ordered)' $W/lexsis-source.html` is 0 (lint P1).

### DP4. Basket sneaking  BLOCK  LAW
- Definition. CCPA item 2: "inclusion of additional items such as products, services, payments to charity or donation at the time of checkout from a platform, without the consent of the user, such that the total amount payable by the user is more than the amount payable for the product(s) and/or service(s) chosen by the user". Free samples and disclosed necessary fees are exempt.
- Example. Sports Direct added a GBP 1 magazine to every basket (https://deceptive.design/types/sneaking ); shipping protection auto-added in the cart drawer.
- Rule. Nothing enters the cart that the shopper did not tap. Cart-drawer add-ons are opt-in buttons, not pre-added lines. A bundle is one product the shopper chose, not silently combined items.
- Check. Cart island props contain no `autoAdd`, `preselected` or default add-on ids: `grep -ciE 'auto-?add|pre-?select(ed)?=.?true' $W/lexsis-source.html` is 0. Browser: add the hero product; the cart total equals the displayed price plus stated shipping and tax only.

### DP5. Preselection (pre-ticked paid add-ons and consent)  BLOCK  LAW
- Definition. deceptive.design "preselection"; CJEU Planet49: pre-ticked boxes are not consent; GDPR Recital 32; EU Consumer Rights Directive Art. 22: no default options that require payment; CCPA basket sneaking covers paid defaults.
- Example. Gift wrap, insurance, donation, warranty, or "Subscribe and save" ticked by default; marketing checkbox pre-checked under the email field.
- Rule. No `checked` on any checkbox or radio whose label carries a price, a cadence, or a consent verb. Purchase type defaults to one-time. Marketing and SMS consent boxes start unchecked and are never `required`.
- Check.
```bash
grep -cE '<input[^>]*type="(checkbox|radio)"[^>]*\bchecked\b' $W/lexsis-source.html   # 0 unless data-lx-default marks a free, non-consent default (lint O3)
grep -ciE '<input[^>]*(consent|marketing|sms|newsletter)[^>]*\brequired\b' $W/lexsis-source.html   # 0
```

### DP6. Confirmshaming  BLOCK  LAW
- Definition. CCPA item 3: "using a phrase, video, audio or any other means to create a sense of fear or shame or ridicule or guilt in the mind of the user so as to nudge the user to act in a certain way". Amazon's "No, I don't want Free Shipping" decline button is now banned by court order (https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-secures-historic-25-billion-settlement-against-amazon ).
- Example. "No thanks, I like paying full price"; "I don't care about my skin".
- Rule. Decline and close labels are neutral: "No thanks", "Close", "Not now", "Continue without". No first-person self-deprecation, no consequence framing, no sarcasm.
- Check. `grep -ciE "no,? (thanks,? )?i (don'?t|do not|hate|prefer|like paying|want to pay)|i'?ll (pay full price|stay|pass on)|(full price|miss out|rather|don'?t care|waste)" $T` is 0 (lint O4 plus additions in section 4).

### DP7. Forced action  BLOCK  LAW
- Definition. CCPA item 4: "forcing a user into taking an action that would require the user to buy any additional good(s) or subscribe or sign up for an unrelated service or share personal information, in order to buy or subscribe to the product or service originally intended by the user". Baymard: 18 to 19 percent of US shoppers abandoned a checkout because the site wanted an account. https://baymard.com/lists/cart-abandonment-rate
- Example. Email gate before the price is shown; "Create an account to continue"; forced app download.
- Rule. Guest checkout is the primary path. No gate on price, shipping, reviews or the CTA. Email and phone are asked once, optional unless needed for delivery, and marketing consent is separate.
- Check. Every primary CTA href resolves to the cart or checkout, never to a capture step: `grep -oE 'href="[^"]*"' $W/lexsis-source.html` for elements inside `buy-box` or `sticky-cta` sections contains no `#signup`, `/account`, `/register`. No `<lx-island name="Popup"` or dialog carries `dismissible="false"`.

### DP8. Subscription trap, hard to cancel, roach motel  BLOCK  LAW
- Definition. CCPA item 5: making cancellation "impossible or a complex and lengthy process", hiding the cancel option, forcing payment details for a free trial, or giving "ambiguous instructions for cancellation". ROSCA: simple cancellation mechanism. DSA Art. 25(3)(c): termination may not be harder than subscribing. FTC v. Amazon, Vonage (USD 100M, 2022: https://www.ftc.gov/news-events/news/press-releases/2022/11/ftc-action-against-vonage-results-100-million-customers-trapped-illegal-dark-patterns-junk-fees-when-trying-cancel-service ) and Adobe (2024: https://www.ftc.gov/news-events/news/press-releases/2024/06/ftc-takes-action-against-adobe-executives-hiding-fees-preventing-consumers-easily-cancelling ).
- Example. "Cancel anytime" in the hero, "call us Monday to Friday" in the terms.
- Rule. The cancellation path is one sentence beside the subscribe control ("Pause or cancel from your account, no call needed") and it is true for this store's subscription app. Free trials state the conversion date and price in the CTA block.
- Check. For every `subscription-toggle` or `plan-selector` section: `grep -ciE 'cancel' <section text>` is at least 1 and the offer ledger row "subscription terms" is `verified`.

### DP9. Hidden recurring terms (SaaS billing, hidden subscription)  BLOCK  LAW
- Definition. CCPA item 12 "SaaS billing": generating and collecting recurring payments "by exploiting positive acquisition loops in recurring subscriptions ... as surreptitiously as possible", including silent trial conversion. ROSCA s.4: all material terms clearly and conspicuously before obtaining billing information. deceptive.design "hidden subscription".
- Example. "$19" in the buy box, "/month" in 10 px grey; first-charge date only in the confirmation email.
- Rule. Recurring amount, cadence, first-charge date, renewal price after any intro period and the cancel path sit in the same visual block as the price, at body size and contrast. A subscribe option never wins by default (DP5).
- Check.
```bash
perl -0ne 'while(/<!-- section: (subscription-toggle|plan-selector|pricing)[^>]*-->(.*?)(?=<!-- section:|\z)/sg){ $s=$2; print "$1: ", ($s=~/(every|per|\/)\s*(month|week|[0-9]+ days)/i && $s=~/cancel/i ? "ok" : "MISSING cadence or cancel"), "\n" }' $W/lexsis-source.html
```

### DP10. Interface interference, visual interference, false hierarchy  BLOCK  LAW
- Definition. CCPA item 6: "a design element that manipulates the user interface in ways that (a) highlights certain specific information; and (b) obscures other relevant information relative to the other information". DSA Art. 25(3)(a): giving more prominence to certain choices. FTC bucket II: un-bolded fees "sandwiched between bold paragraphs".
- Example. Bright "Yes, upgrade" button with a grey 12 px "no" text link; a close icon at 2:1 contrast; compare-at price larger than the price paid.
- Rule. In any binary choice (consent, upsell, subscription vs one-time), both options are the same element type, within 1.5x of each other's area, both at 4.5:1. Close controls are at least 24 x 24 CSS px at 3:1 and close on first tap. The price paid is never smaller than the compare-at.
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
- Check. `grep -ciE '\b(opt.?out|un(check|tick|subscribe)|do not|don'"'"'t) .*(receive|get|miss)\b|not .* (unless|except|without)' $T` restricted to label and button text is 0.

### DP16. Rogue malware and fake system UI  BLOCK  LAW
- Definition. CCPA item 13: scareware and ransomware tactics.
- Rule. No fake virus warnings, fake OS dialogs, fake download buttons, fake "connection lost" banners.
- Check. `grep -ciE 'virus|infected|your (device|phone|computer) (is|has)|system alert' $T` is 0.

### DP17. Fake reviews and undisclosed incentives  BLOCK  LAW
- Definition. FTC 16 CFR 465 bans fake, AI-generated or bought reviews, insider reviews without disclosure, and suppression of negative reviews (Fashion Nova, USD 4.2M, 2022: https://www.ftc.gov/news-events/news/press-releases/2022/01/fashion-nova-will-pay-42-million-part-settlement-ftc-allegations-it-blocked-negative-reviews-website ). UK DMCC banned practice on fake reviews. Endorsement Guides: incentivised reviews disclosed; results claims need typicality.
- Rule. Every quote, star, count and photo of a customer is a `verified` row in the proof ledger (`references/proof/proof-ledger.md`); sourcing in `references/proof/reviews-sourcing.md`. No invented names, avatars or cities. Never only five-star sets. "Results not typical" alone is not a disclosure.
- Check. lint P1 to P4 and N11; `grep -ciE 'results (may )?(not typical|vary)' $T` hits require a "generally expected results" statement in the same section.

### DP18. Misdirection  BLOCK  LAW
- Definition. deceptive.design: design that steers attention to the seller's preferred option and away from the shopper's. CMA "sensory manipulation" and "decoys". Overlaps DP10 but concerns steering rather than hiding.
- Example. A highlighted "MOST POPULAR" middle tier that exists only to make the top tier look cheap; a colour-only difference between "one-time" and "subscribe" that favours subscribe.
- Rule. Plan tiers are presented with the same visual weight; a recommended tier is labelled with a reason from the ledger ("Most ordered in the last 90 days" with the count), never a ribbon (design-rules N9). One-time and subscribe options are visually equal with one-time first.
- Check. `grep -cE 'BEST VALUE|MOST POPULAR|RECOMMENDED' $W/lexsis-source.html` is 0 (lint N9). Purchase-type radio order: one-time appears before subscribe in DOM.

### DP19. Obstruction and sludge  FAIL  LAW
- Definition. deceptive.design "obstruction"; CMA "sludge": excessive friction on the action the shopper wants (returns, cancellation, contact).
- Rule. Returns, refund, cancellation and contact information reach in at most two taps from any CTA: a one-line statement under the CTA linked to the full policy.
- Check. `grep -ciE 'return|refund|guarantee' <buy-box or closing-cta section text>` is at least 1 and contains an `<a href` to the policy URL recorded in the offer ledger.

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
- Check. `grep -cE 'data-part="progress"' $W/lexsis-source.html` equals the count of those with `data-steps-total`. `grep -ciE 'analy[sz]ing|calculating|applying your' $T` is 0 unless a real async call exists.

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

## 4. Lint alignment

`design_lint.py` already carries O1 (stock and hurry phrases), O2 (countdown without plan end date), O3 (pre-checked inputs), O4 (confirmshaming) and P1 (social-proof popups and live counts). Adopt these additions:

```python
# O1 extension (DP1, DP2): add to STOCK_PHRASES
r"|\bends? (soon|tonight|today|in)\b|\blimited time\b|\bwhile (stocks|supplies) last\b|\blow stock\b"
# O4 extension (DP6): decline copy with consequence framing
CONFIRMSHAME_EXT = r"i'?ll (pay full price|stay|pass on)|\b(full price|miss out|rather|don'?t care|waste)\b"   # apply to text inside [data-action=decline], button, a
# O5 NEW (DP5, DP7): required consent inputs
r'<input[^>]*(consent|marketing|sms|newsletter)[^>]*\brequired\b'          # expect 0
# O6 NEW (DP9): subscription sections must state cadence and cancel path
# for each <!-- section: (subscription-toggle|plan-selector|pricing) --> body: require /(every|per|\/)\s*(month|week|\d+ days)/i and /cancel/i
# O7 NEW (DP12): buy-box / pricing / offer section must mention shipping and tax
# for each <!-- section: (buy-box|pricing|offer) --> body: require /shipping|delivery/i and /tax|gst|inclusive/i
# O8 NEW (DP13): advertorial / listicle label
# if manifest page.pageType in {advertorial, listicle}: require /advertis(ement|ing)|sponsored|paid partnership/i in the first 600 px (browser) or before the third section delimiter (static)
# O9 NEW (DP15): negated choice labels
r"\b(opt.?out|un(check|tick|subscribe)|do not|don'?t) .*(receive|get|miss)\b"   # within <label>, <button> text; expect 0
# O10 NEW (DP16, DP22): fake system UI and faux processing
r"\b(virus|infected|system alert|analy[sz]ing your|applying your discount)\b"    # expect 0
# O11 NEW (DP18): tier ribbons already in N9; add
r"\bRECOMMENDED\b"
# O12 NEW (DP21): strike-through without source
r"<(s|del)\b(?![^>]*data-source=)"   # expect 0
```

Browser-only checks (record in `qa-report.md`): DP10 parity script, DP13 label position, DP14 single-overlay assertion, DP4 cart-total equality.

---

# Copy anti-patterns

The canonical vocabulary and structure blacklist for generated page copy.
`/design-page` applies it in Compose step 8; `design_lint.py` C1 to C4
mirror the lists below (update both together); `brand_kit.banned_phrases`
is merged in at run time. Positive rules for headlines, CTAs, FAQs and
microcopy are in `references/copy/headline-and-cta-rules.md`; frameworks in
`references/copy/copy-frameworks.md`; sourcing real language in
`references/copy/voice-of-customer-mining.md`.

Scope of a hit. FAIL when the word or structure appears in an `h1`, `h2`,
`h3`, subhead, button, link label, CTA microcopy or announcement bar. WARN
when it appears in body text fewer than two times; FAIL at two or more body
hits. Text inside `<blockquote>` and review islands is exempt: reviews are
verbatim (`references/proof/proof-ledger.md` rule 4).

Severity BLOCK, FAIL, WARN. Tag LAW, RESEARCH, OPERATOR, HEURISTIC. `$T` is
the extracted text with quotes removed:
`perl -0pe 's/<blockquote.*?<\/blockquote>//sg; s/<lx-island name="Review.*?<\/lx-island>//sg; s/<[^>]+>/ /g' $W/lexsis-source.html > $T`.

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

Allowlist handling. `brand_kit.allowlist` (or the plan's "Copy allowlist" line) removes a term when it is literal: a brand named "Elevate", a tier named "Premium", a hair oil that is literally "curated" by a named person. Every allowlisted hit is recorded in `page-plan.md` with the reason.

## 3. Claims

| Id | Tell | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|
| CP2 | Superlatives and objective claims without substantiation: best, #1, No.1, most trusted, most advanced, clinically proven, doctor recommended, dermatologist tested, award-winning, 100% natural, chemical-free, toxin-free, guaranteed results, proven to | FTC: objective claims need a reasonable basis before publication; "clinically proven" needs that evidence. India ASCI/CCPA: "No.1" only with market-share data; disclaimers may not contradict the claim. Each hit must map to a proof-ledger row (`test-data`, `award`, `certification`, `customer-count`). https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business ; https://www.ascionline.in/wp-content/uploads/2022/09/asci_june_july_2020_ccc_pr.pdf | BLOCK | LAW | `grep -niE '\b(#\s?1|no\.?\s?1|number one|the best|world'"'"'s (best|most)|most (trusted|advanced|popular|loved)|clinically (proven|tested)|(doctor|dermatologist)[- ](recommended|tested)|award[- ]winning|100% (natural|safe|effective)|chemical-free|toxin-free|guaranteed results|proven to)\b' $T`; every line maps to a ledger row |
| CP3 | Hedged non-claims: may help support, can help promote, is believed to, designed to help, supports healthy ... | Either a substantiated fact with a number, or cut the sentence. Where regulation mandates a hedge (supplement structure/function claims), keep the mandated wording and pair it with dose, ingredient or study n. | WARN | OPERATOR | `grep -ciE '\b(may help|can help|might help|is believed to|designed to help|helps? support|supports? (healthy|overall))\b' $T` |
| CP4 | "Results not typical" or "results may vary" as the only qualifier beside a results testimonial | FTC Endorsement Guides: disclose the generally expected result in the same block; the bare disclaimer does not comply. https://www.govinfo.gov/content/pkg/CFR-2023-title16-vol1/pdf/CFR-2023-title16-vol1-part255.pdf | BLOCK | LAW | any hit of `results (may )?(not typical|vary)` requires `generally|typical(ly)? (see|lose|gain|report)` in the same section |

## 4. Structure tells

| Id | Tell | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|
| CP5 | Em-dash chains | At most one em dash per 150 words; none in headings, buttons or subheads. Prefer a full stop. Pangram: 10x more em dashes in AI text. | FAIL | RESEARCH | lint C3 (headline chains); `perl -ne '$d+=()=/\x{2014}|\x{2013}| - /g; $w+=split; END{printf "%.2f per 150w\n",$d/($w/150)}' $T` under 1.0 |
| CP6 | Rule of three everywhere ("soft, breathable, and durable") | At most one adjective triad per section. Lists of specifics beat adjective triads. | WARN | RESEARCH | `grep -ciE '\b\w+, \w+,? and \w+\b'` per section text at most 1 |
| CP7 | Antithesis: "not just X, it's Y", "isn't just ... it's", "more than just" | Zero. | FAIL | RESEARCH | `grep -ciE "(isn'?t|not|is more than) just\b.*\b(but|it'?s|it is)\b" $T` is 0 |
| CP8 | Rhetorical-question openers ("Tired of ...?", "Ever wondered ...?") | At most one question heading per page; never the h1 unless the type uses `qualifier-lead` and the question genuinely selects the reader. | WARN | OPERATOR | `grep -c '?' <headings>` at most 1 |
| CP9 | "Imagine ..." or "Picture this" | Zero. | FAIL | RESEARCH | `grep -ciE '^\s*(imagine|picture this)\b' $T` is 0 |
| CP10 | Exclamation marks | Zero outside verbatim reviews. | FAIL | OPERATOR | `grep -c '!' $T` is 0 |
| CP11 | Uniform sentence and paragraph length | Standard deviation of sentence length at least 4 words per section; no three consecutive paragraphs within 10 percent of the same word count. | WARN | HEURISTIC | sentence-length variance script in section 9 |
| CP12 | Identical section rhythm (headline, subhead, three bullets, CTA, repeated) | Adjacent sections never share the same layout skeleton (`references/anti-patterns/design-anti-patterns.md` DA14). | FAIL | OPERATOR | DA14 check |
| CP13 | Alliterative or fragment triad headlines ("Pure. Potent. Proven.") | At most one fragment-triad heading per page. | FAIL | RESEARCH | `grep -cE '^[A-Z][a-z]+\. [A-Z][a-z]+\. [A-Z][a-z]+\.$' <headings>` at most 1 |
| CP14 | Summary and conclusion language ("In conclusion", "Ultimately", "Overall", "To sum up") | Zero. A landing page asks; it does not conclude. | FAIL | OPERATOR | `grep -ciE '\b(in conclusion|ultimately|overall|to sum up|in summary|all in all)\b' $T` is 0 |
| CP15 | Colon reveal in headings ("The result: skin that ...") | At most one per page. | WARN | RESEARCH | `grep -c ': ' <headings>` at most 1 |
| CP16 | Title Case Headings | Sentence case for headings, subheads, buttons, labels; product names keep brand casing. USAGov moved to sentence case sitewide in 2023 with no trust drop. https://www.usa.gov/blog/2023/09/making-the-case-for-sentence-case | FAIL | RESEARCH | `grep -cE '^([A-Z][a-z]+\s){3,}[A-Z][a-z]+' <headings>` is 0 after the product-name allowlist |
| CP17 | Bold-label bullets ("**Fast:** ...", "**Simple:** ...") | Zero. Write the specific. | FAIL | RESEARCH | `grep -cE '<li>\s*<(strong|b)>[^<]{1,20}:</(strong|b)>' $W/lexsis-source.html` is 0 |
| CP18 | False ranges ("from busy parents to pro athletes") | Only when X and Y are real endpoints of one scale the merchant serves. | WARN | RESEARCH | `grep -ciE '\bfrom \w+( \w+)? to \w+( \w+)?( and everything in between)?\b' $T`; each hit reviewed |
| CP19 | Generic openers ("Welcome to ...", "At [Brand], we believe ...", "We are passionate about") | Zero. Lead with the shopper's problem or a specific. | FAIL | OPERATOR | `grep -ciE '^\s*(welcome to|at [A-Z][A-Za-z]+,? we (believe|are passionate)|we are passionate)' $T` is 0 |
| CP20 | Subhead restates the headline | The subhead resolves the headline (mechanism, proof or who it is for); token overlap with the h1 under 50 percent. | FAIL | OPERATOR | overlap script in section 9 |

## 5. Punctuation and case

| Id | Tell | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|
| CP21 | Hype punctuation: "!!", "?!", "..." trails in headings | Zero. | FAIL | OPERATOR | lint C2 `!{2,}|\?!` |
| CP22 | ALL-CAPS words of six or more letters | None outside a `CAPS_ALLOWLIST` of acronyms and registered marks (GST, FSSAI, UPI, MRP, BIS, ISO, NSF, USDA, SPF, COD, EMI, BNPL). Labels of three words or fewer may be caps only under a merchant-stated rule (design-rules N5). | FAIL | RESEARCH | lint C2 `[A-Z]{6,}(?![a-z])` after allowlist removal |
| CP23 | Arrow glyphs or "->" in link and button text | Design-rules N12. | FAIL | OPERATOR | lint N12 |
| CP24 | Emoji anywhere in copy | Design-rules N1. | FAIL | OPERATOR | lint N1 |
| CP25 | Middle dots (U+00B7) joining meta strings ("Free shipping", dot, "30-day returns", dot, "Made in India") | Use a full stop or separate lines; N12 names middle-dot joins as chrome. | WARN | OPERATOR | `grep -c '\xc2\xb7' $W/lexsis-source.html` is 0 |

## 6. CTA and control copy

| Id | Tell | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|
| CP26 | Stock CTA labels: Shop Now, Get Started, Learn More, Buy Now (tof/mof), Submit, Click here, Continue (no object), OK, Yes, Go, Read more | Design-rules A12; `references/copy/headline-and-cta-rules.md` HC12 to HC14. The CTA is verb plus object plus outcome or price, at most four words, sentence case. | FAIL | OPERATOR | lint A12 and C4 plus the extension in section 10 |
| CP27 | CTA that does not start with a verb, or exceeds four words | HC12. | FAIL | OPERATOR | CTA verb script in section 9 |
| CP28 | "Free" with an asterisk or a later condition | Offers OF5: the condition sits in the same line. | BLOCK | LAW | `grep -ciE '\bfree\*' $T` is 0 |

## 7. Placeholder and model leakage

| Id | Tell | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|
| CP29 | Placeholder text: lorem ipsum, TODO, TBD, [brand], [product], {{ }}, "Your headline here", "Insert ...", "Product name", "Lorem" | Zero. A12 already forbids placeholder copy. | BLOCK | OPERATOR | `grep -ciE 'lorem|ipsum|\bTODO\b|\bTBD\b|\[(brand|product|name|city|number)\]|\{\{|your (headline|text|copy) here|insert (your|a|the)|product name here' $W/lexsis-source.html` is 0 |
| CP30 | Framework labels leaking into copy ("Problem:", "Agitate:", "Solution:", "Benefit:", "Call to action") | Zero. Frameworks shape the order, never the words. | FAIL | OPERATOR | `grep -ciE '^\s*(problem|agitat(e|ion)|solution|benefit|proof|push|hook|story|offer|call to action)\s*:' $T` is 0 |
| CP31 | Assistant voice leaking ("As an AI", "Certainly", "Here's a", "I hope this helps", "Feel free to") | Zero. | BLOCK | OPERATOR | `grep -ciE "as an ai|certainly|here'?s an? |i hope this|feel free to|let me know" $T` is 0 |

## 8. Brand voice

| Id | Tell | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|
| CP32 | A `brand_kit.banned_phrases` entry appears | BLOCK in any position, including body. Merged into the lint list at run time; the plan's "Copy allowlist" cannot override a merchant ban. | BLOCK | OPERATOR | `for p in "${BANNED[@]}"; do grep -ciF "$p" $T; done` all 0 |
| CP33 | Register mismatch with `voice_md` (jokey copy for a clinical brand; clinical copy for a playful brand) | Reviewed by an LLM pass against the voice adjectives and "we say / we don't say" pairs; not regex. | WARN | OPERATOR | one-line finding per section in `qa-report.md` |
| CP34 | Brand name outnumbers "you/your" | Second person leads; Apple's iPhone 5 copy used "you/your" more than "iPhone" and "Apple" combined. https://neilpatel.com/blog/write-copy-like-apple/ | WARN | RESEARCH | ratio script in section 9 |
| CP35 | Spelling locale drift (color and colour on one page) | One locale from `brand_kit` or the store market. | WARN | OPERATOR | `grep -ciE '\bcolor\b' $T` and `grep -ciE '\bcolour\b' $T` are not both non-zero |

## 9. Canonical regex and scripts

Python `re` form, case-insensitive, applied to `$T`. Lines marked `# lint` are already in `design_lint.py`; `# NEW` are additions for the lead to adopt.

```python
SLOP_WORDS = r"\b(elevate[sd]?|unleash(es|ed)?|unlock(s|ed)?|delve[sd]?|seamless(ly)?|game-?changer|game-?changing|revolutioni[sz]e[sd]?|revolutionary|effortless(ly)?|curated|indulge|embrace|look no further|say goodbye to|in today'?s fast-paced|whether you'?re|it'?s not just|crafted with (care|love|passion)|meticulously|premium quality|world-class|cutting-edge|next-level|transform(s|ed)? your|elevate your|discover the (power|magic|difference)|experience the (difference|magic)|the ultimate|your journey|treat yourself|introducing the)\b"   # lint C1
SLOP_WORDS_EXT = r"\b(empower(s|ed|ing)?|harness(es|ed)?|leverage[sd]?|supercharge[sd]?|streamline[sd]?|reimagine[sd]?|redefine[sd]?|showcas(e|es|ed|ing)|foster(s|ed)?|dive into|next-gen(eration)?|state-of-the-art|best-in-class|innovative|unparalleled|unmatched|unrivall?ed|exquisite|meticulous|intricate|bespoke|artisanal|holistic|synergy|robust|tapestry|realm|testament|beacon|pivotal|crucial|vibrant|must-have|perfect for|stunning|breathtaking|say hello to|designed with you in mind|the perfect blend|at its finest|like never before|you deserve|the secret to|your go-to|made for modern life|we'?ve got you covered|sit back and relax|the best part\?|here'?s the thing|let'?s face it|in a world where|gone are the days|nestled|boasts|a testament to|and everything in between|welcome to|at [A-Z][a-z]+,? we believe|level up|unlock your potential|step into|dive in)\b"   # NEW
HYPE_PUNCT = r"!{2,}|\?!|[A-Z]{6,}(?![a-z])"   # lint C2 (apply CAPS_ALLOWLIST first)
CAPS_ALLOWLIST = {"FSSAI","GST","UPI","MRP","BIS","ISO","NSF","USDA","SPF","COD","EMI","BNPL","INCI","GMP","HACCP"}   # NEW
HEADLINE_EMDASH = r"<h[1-3][^>]*>[^<]*\u2014[^<]*\u2014"   # lint C3 (the script uses the literal em dash)
STOCK_CTA = r">\s*(Submit|Click here|Learn more)\s*<"   # lint C4
STOCK_CTA_EXT = r">\s*(Shop now|Get started|Buy now|Read more|Continue|OK|Yes|Go|Sign up|Download)\s*(<|$)"   # NEW (Buy now only when funnelStage != bof)
ANTITHESIS = r"(isn'?t|not|is more than) just\b.*\b(but|it'?s|it is)\b"   # NEW
IMAGINE = r"^\s*(imagine|picture this)\b"   # NEW
SUMMARY = r"\b(in conclusion|ultimately|overall|to sum up|in summary|all in all)\b"   # NEW
GENERIC_OPENER = r"^\s*(welcome to|at [A-Z][A-Za-z]+,? we (believe|are passionate)|we are passionate)"   # NEW
BOLD_LABEL_BULLET = r"<li>\s*<(strong|b)>[^<]{1,20}:</(strong|b)>"   # NEW (source html)
SUPERLATIVE = r"\b(#\s?1|no\.?\s?1|number one|the best|world'?s (best|most)|most (trusted|advanced|popular|loved)|clinically (proven|tested)|(doctor|dermatologist)[- ](recommended|tested)|award[- ]winning|100% (natural|safe|effective)|chemical-free|toxin-free|guaranteed results|proven to)\b"   # NEW, BLOCK unless ledger row
HEDGE = r"\b(may help|can help|might help|is believed to|designed to help|helps? support|supports? (healthy|overall))\b"   # NEW, WARN
RESULTS_DISCLAIMER = r"results (may )?(not typical|vary)"   # NEW, BLOCK without 'generally expected'
PLACEHOLDER = r"lorem|ipsum|\bTODO\b|\bTBD\b|\[(brand|product|name|city|number)\]|\{\{|your (headline|text|copy) here|insert (your|a|the)|product name here"   # NEW, BLOCK
FRAMEWORK_LABEL = r"^\s*(problem|agitat(e|ion)|solution|benefit|proof|push|hook|story|offer|call to action)\s*:"   # NEW
ASSISTANT_VOICE = r"as an ai|certainly|here'?s an? |i hope this|feel free to|let me know"   # NEW, BLOCK
FREE_ASTERISK = r"\bfree\*"   # NEW, BLOCK
TITLE_CASE_HEADING = r"^([A-Z][a-z]+\s){3,}[A-Z][a-z]+"   # NEW, on heading text after product-name allowlist
FRAGMENT_TRIAD = r"^[A-Z][a-z]+\. [A-Z][a-z]+\. [A-Z][a-z]+\.$"   # NEW, on heading text, allow 1
```

```python
# CP11 sentence-length variance, CP20 subhead overlap, CP27 CTA verb, CP34 you/brand ratio
import re, statistics
def sentences(t): return [s for s in re.split(r'[.!?]+\s', t) if s.strip()]
def cp11(section_text):
    L = [len(s.split()) for s in sentences(section_text)]
    return len(L) < 3 or statistics.pstdev(L) >= 4
def cp20(h1, sub):
    a, b = set(re.findall(r'\w+', h1.lower())), set(re.findall(r'\w+', sub.lower()))
    return len(a & b) / max(1, len(b)) < 0.5
VERBS = {'add','get','start','claim','buy','shop','send','try','join','grab','order','choose','see','show','save','pre-order','subscribe','reserve','book','take','find','build','pick','complete','apply','check'}
def cp27(label):
    w = label.strip().lower().split()
    return 1 <= len(w) <= 4 and w[0] in VERBS and (len(w) > 1 or w[0] in {'buy','shop','order','subscribe'})
def cp34(text, brand):
    return len(re.findall(r'\byou(r|rs)?\b', text, re.I)) >= len(re.findall(re.escape(brand), text, re.I))
```

## 10. Rewrite procedure for a hit

1. Ask Harry Dry's three questions of the sentence: can the reader visualise it, can it be falsified, could no competitor say it. A line failing all three is deleted, not rephrased. https://www.demandcurve.com/lessons/fundamental-rules-of-good-copy
2. Replace the banned word with what specifically happens: "seamless" becomes "arrives assembled, no tools"; "premium quality" becomes the material, weight or test.
3. Pull the replacement from the voice-of-customer worksheet (`references/copy/voice-of-customer-mining.md`) before inventing one.
4. Re-run the section checks; a heading hit blocks compile, a body hit produces a rewrite note in `qa-report.md` with the span and the rule id.

## 11. Lint alignment

`design_lint.py` today: C1 `SLOP_WORDS`, C2 `HYPE_PUNCT`, C3 headline em-dash chains, C4 Submit/Click here/Learn more. Adopt, in this order of value:

1. Merge `SLOP_WORDS_EXT` into C1 and honour `brand_kit.allowlist` plus the plan's "Copy allowlist" line (CP1).
2. Merge `brand_kit.banned_phrases` as literal, case-insensitive matches, BLOCK in any position (CP32).
3. Add `CAPS_ALLOWLIST` stripping before C2 (CP22).
4. Add `STOCK_CTA_EXT` to C4, with "Buy now" gated on `manifest.page.funnelStage != "bof"` (CP26).
5. New checks C5 `ANTITHESIS`, C6 `IMAGINE`, C7 `SUMMARY`, C8 `GENERIC_OPENER`, C9 `BOLD_LABEL_BULLET`, C10 `PLACEHOLDER` (BLOCK), C11 `FRAMEWORK_LABEL`, C12 `ASSISTANT_VOICE` (BLOCK), C13 `FREE_ASTERISK` (BLOCK), C14 `SUPERLATIVE` (BLOCK unless a ledger row is named in `page-plan.md` "Claims confirmed"), C15 `HEDGE` (WARN), C16 `RESULTS_DISCLAIMER` (BLOCK without a "generally expected" phrase in the same section).
6. Heading-text checks C17 `TITLE_CASE_HEADING`, C18 `FRAGMENT_TRIAD` (allow 1), C19 question headings (allow 1), C20 colon reveals (allow 1), C21 em-dash density under 1 per 150 words on `$T`.
7. Structural scripts C22 `cp11`, C23 `cp20`, C24 `cp27` on every button and `a.btn` label, C25 `cp34`.
8. Scope: run C1 and the structure checks on `$T` with `<blockquote>` and review islands removed, and report heading hits as FAIL and body hits as WARN (FAIL at two or more).

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
| 5 | `lexsis_brand.list_themes` then `.get_theme` | R | `page-theme.css` |
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

Output: `page-plan.md` with Page type, Design direction, Consumer decision
model, Proof ledger, Offer ledger, Imagery plan, Asset slots; compact
`page-manifest.json`. Run `plan_lint.py` before approval.

## Stage 2: Design

| # | Call | Type | Purpose | Gate |
|---|---|---|---|---|
| 1 | read plan + manifest + page-type file | local | follow its `## Workflow`; note deviations | ask only when a deviation is unexplained |
| 2 | `lexsis_brand.context`, `.get_theme` | R | live tokens | compare with saved; `THEME_CONTEXT_CONFLICT` on value clash |
| 3 | `lexsis_template_library.get_kit` then `lexsis_design.get_section` (1 to 3 ids per call, kit order) | R | authoring source | only ids in the manifest |
| 4 | `lexsis_template_library.list_mine` then `.get_mine` | R | merchant's saved sections | when the user names one |
| 5 | `lexsis_design.islands` | R | compact catalog | select only interactive needs |
| 6 | `lexsis_design.island_schema` | R | exact props | per island actually used, or per compile error |
| 7 | `lexsis_catalog.get` | R | current variant ids, prices | before binding BuyBox |
| 8 | `lexsis_catalog.reviews` / `.review_collection_items` | R | `collectionId` or `productIds`, `minRating`, real totals | review islands only |
| 9 | `lexsis_asset_library.search`, `lexsis_assets.view`, `lexsis_asset_import.import`, `lexsis_asset_upload.upload` | R/W | resolve `planned` slots; import supplied sources, upload for local-file UI only | never placeholders; wait for the user's uploaded-asset message for UI uploads |
| 10 | `lexsis_workspace.credits` then `lexsis_drafts.asset_generate` | W $ | remaining ALLOW-list gaps | ask first |
| 11 | `lexsis_pages.compile` | R | validation_errors as the work list | loop until clean |
| 12 | `lexsis_page_create.create` (`publish: false`) | W | one hosted draft | once per page; reuse `remote.pageId` after |
| 13 | host browser at 390 and 1280 | local | hosted design review | production-ready only |
| 14 | `lexsis_drafts.page_update_section` / `.page_patch` (`expected_version`) | W | fix review findings | never a second draft |

Output: `lexsis-source.html`, `page-theme.css`, `compile-artifact.json`,
`DRAFT_CREATED`, later `DESIGN_APPROVED`.

## Stage 3: Generate (sync + QA)

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

Output: `DRAFT_READY`.

## Stage 4: Publish and after

| # | Call | Type | Purpose |
|---|---|---|---|
| 1 | `lexsis_live_ops.publish` | W ! | named page and version only |
| 2 | `lexsis_analytics.page`, `.timeseries`, `.attribution` | R | first-week read |
| 3 | `lexsis_drafts.page_variation` then `.experiment_create` | W | challengers (`/ab-test`) |
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

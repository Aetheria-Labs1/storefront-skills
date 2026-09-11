---
name: design-page
description: Turn an approved one-page storefront plan into canonical Lexsis source and an unpublished hosted draft, confirming any asset slots the plan left unresolved.
---

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

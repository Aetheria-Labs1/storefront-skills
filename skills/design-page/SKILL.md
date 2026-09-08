---
name: design-page
description: Turn an approved one-page storefront plan into canonical Lexsis source and an unpublished hosted draft, confirming any asset slots the plan left unresolved.
---

# Design the Page

Create the real page source, compile it, and create one unpublished hosted
draft for review. Never publish.

Read:

- `references/design-rules.md`
- `references/animation-system.md` when the plan names a motion moment
- `references/consumer-behavior-cro.md`
- `references/island-presets.md`
- `references/merchant-templates.md`
- `references/workflow-intent.md`
- `references/design-concepts.md` only when the user wants a visual concept
  before source authoring
- `references/page-layout.md`

Use `lexsis_brand.context`, `lexsis_brand.get_theme`,
`lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`, `lexsis_design.guide`,
`lexsis_design.islands`, `lexsis_design.island_schema`,
`lexsis_design.get_section`, `lexsis_template_library.get_kit`,
`lexsis_asset_library.search`, `lexsis_catalog.get`, `lexsis_catalog.reviews`,
`lexsis_assets.capabilities`, `lexsis_assets.view`,
`lexsis_workspace.credits`,
`lexsis_drafts.asset_generate`, `lexsis_asset_upload.import`, and
`lexsis_pages.compile`, and `lexsis_page_create.create`.

When the user wants one of their saved reusable sections, use
`lexsis_template_library.list_mine` and `get_mine`. Treat its source as a
starting section in the page, not as an inherited renderer shell.
Resolve only unfamiliar argument schemas through exact router/action
discovery.

## Inputs

Use the approved `page-plan.md` and its saved store/theme binding. The plan
defines strategy, the Design direction, the Imagery and background plan, the
asset slots and section intent; it must not define islands or implementation
details.

Implement the plan's Consumer decision model without adding generic CRO
modules. Preserve its visitor mode, top decision questions, selected patterns,
gallery jobs, merchandising relationship, risk treatment, mobile context, and
metric. Reopen a decision only when live catalog, asset, or policy evidence
contradicts the plan.

If the user explicitly skips `/plan-page`, write a short one-page plan with
the same blocks and record the skip. Never run `/setup` or `/plan-page`
automatically.

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
4. Import externally generated media into Lexsis before production use, verify
   identity-sensitive imagery with `lexsis_assets.view`, and set
   `status: verified` on each resolved slot.

Use Lexsis icons, supported SVG, or CSS for ordinary interface icons. When the
plan's Icons decision names a set to generate, generate one monochrome SVG set
(one stroke, one size) and import it. Never fall back to emoji as icons; emoji
appear only where the plan's "Emoji in copy" line allows them, inside running
text. Image generation is otherwise for imagery, banners, and illustrations.

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
5. Review islands follow the plan's Proof sources line: `collectionId` or
   `productIds`, `minRating`, `pageSize` of 12 or fewer. Omit
   `reviewsEndpoint`; the page supplies it at runtime. `averageRating` and
   `totalReviews` only from the `lexsis_catalog.reviews` total. `none` means no
   review island. Never `SocialProofPopup`.
6. Write a rough but complete `lexsis-source.html` with stable section
   delimiters, minimal island props, and the documented examples as a starting
   point.
7. Write global page rules to `page-theme.css`; keep section-specific CSS
   beside its section.
8. Use LX tokens for brand values and compile-time Tailwind utilities for
   layout. Do not use a runtime Tailwind CDN.
9. Compare explicit `NEVER`, `must`, and `non-negotiable` rules in the saved
   brand design with matching theme tokens. On a direct value contradiction,
   return `THEME_CONTEXT_CONFLICT` with both values. Do not silently choose one.
10. Use ordinary HTML for static content and `<lx-island>` source for supported
   interactions. Use headless mode only with complete required hooks.
11. Keep island props schema-valid and use current product bindings. Real
    commerce is tested on the hosted draft.
12. For guided merchandising, show two or three relevant choices by default,
    name the relationship, show why each item belongs, and preserve the primary
    product decision. Never use an unlabeled generic recommendation carousel.

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
Hosted review: [not requested | pending | passed]
Sections: [ordered list]
Interactive components: [islands]
Presets: [ids]
Reused assets: [slots]
Generated assets: [slots]
Unresolved assets: [slots]
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

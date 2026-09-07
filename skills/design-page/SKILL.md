---
name: design-page
description: Turn an approved one-page storefront plan into canonical Lexsis source and a responsive interactive preview, confirming any asset slots the plan left unresolved.
---

# Design the Page

Create the real page source and its browser-reviewable preview. Do not create
a remote draft or publish.

Read:

- `references/design-rules.md`
- `references/island-presets.md`
- `references/merchant-templates.md`
- `references/workflow-intent.md`
- `references/page-layout.md`
- `references/island-preview.md`

Use `lexsis_brand.context`, `lexsis_brand.get_theme`,
`lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`, `lexsis_design.guide`,
`lexsis_design.islands`, `lexsis_design.island_schema`,
`lexsis_design.get_section`, `lexsis_template_library.get_kit`,
`lexsis_asset_library.search`, `lexsis_catalog.get`, `lexsis_catalog.reviews`,
`lexsis_assets.view`, `lexsis_workspace.credits`,
`lexsis_drafts.asset_generate`, `lexsis_asset_upload.import`, and
`lexsis_pages.compile`.

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

If the user explicitly skips `/plan-page`, write a short one-page plan with
the same blocks and record the skip. Never run `/setup` or `/plan-page`
automatically.

## Infer the Design Mode

Use `references/workflow-intent.md` and the manifest evidence. A correction in
the current request overrides the saved mode.

- `fast-draft`: make reasonable reversible choices, compile a coherent page,
  and expose the first useful preview quickly. Run only the light source,
  responsive hierarchy, hydration, font, and asset checks needed to avoid a
  broken draft. Deeper critique is follow-up work.
- `production-ready`: run the full Design Direction and Self-Critique gates
  before marking the design approved.

Neither mode authorizes paid generation. Ask immediately before spending
credits when existing library, catalog, or imported assets cannot satisfy the
page.

If optional design, preset, or merchant-template guidance is unavailable, warn
once and continue from the page plan, saved brand, live schemas, and compiler.
Missing canonical source-format or compile-contract inputs remain blocking.

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
   `production-ready`, ask once whether to generate, pick existing media, or
   keep a bundled preview placeholder for local review.
4. Import externally generated media into Lexsis before production use, verify
   identity-sensitive imagery with `lexsis_assets.view`, and set
   `status: verified` on each resolved slot.

Use Lexsis icons, supported SVG, or CSS for ordinary interface icons. When the
plan's Icons decision names a set to generate, generate one monochrome SVG set
(one stroke, one size) and import it. Never fall back to emoji as icons; emoji
appear only where the plan's "Emoji in copy" line allows them, inside running
text. Image generation is otherwise for imagery, banners, and illustrations.

Placeholders are allowed only in the local preview and cannot pass
`/generate`. When a store has no usable logo image, use an accessible text
wordmark or plain HTML header for the local design. Do not substitute a
product image or generic logo placeholder.

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
11. Keep preview props safe and presentation-focused. Real commerce is tested
   on the hosted draft.

## Parallel Section Generation

If the runtime can spawn sub-agents, each may write one section's markup and
scoped CSS from its plan line, wireframe box, slot ids and preset. The parent
assembles `lexsis-source.html` in plan order, owns `page-theme.css`, compiles
once, and runs the Self-Critique Gate. Sub-agents never compile, never edit
shared CSS, and never spend credits. Without sub-agents, write the sections
sequentially.

## Compile and Preview

Compile the rough complete source, CSS, head, scripts, and bindings early. The
compiler is the authoritative compatibility check.

1. Use `validation_errors` as the work list.
2. Fetch a full island schema only for an island named by an error or when a
   required behavior remains unclear.
3. Fix the source while preserving the planned composition.
4. Recompile until blocking errors are clear.
5. Save the exact clean response and input hashes in `compile-artifact.json`.

Build the preview with the script bundled beside this skill. Resolve its path
from the loaded skill directory rather than assuming the repository is the
current working directory:

```bash
python3 <design-page-skill>/scripts/build_page_preview.py \
  <page-workspace>/compile-artifact.json \
  <page-workspace>/page-preview.html \
  --theme-css <page-workspace>/page-theme.css
```

In `fast-draft`, show the first compiled preview as soon as the section
structure, responsive hierarchy, expected fonts, assets, and hydration are
recognizable. Label it `ROUGH_PREVIEW`; critique and polish may continue after
the user can see the direction.

In `production-ready`, do not mark the design approved until the
Self-Critique Gate passes.

Inspect 390px and 1280px. Confirm the expected islands hydrate and there is no
overflow, clipping, broken hierarchy, or unusable responsive layout. Tablet,
hosted visual comparison, and real cart behavior belong to `/generate`.

The local hydration check must respect each island's strategy:

- `immediate` must hydrate during initial readiness.
- `visible`, `idle`, and `interaction` may remain pending until their trigger.
- Browser QA should scroll through visible islands and exercise interaction
  islands before final approval.

If browser automation cannot access the preview, return
`DESIGN_PREVIEW_READY_QA_PENDING` with the preview path and the checks that still
need manual confirmation. Never record hydration as passed without evidence.

## Self-Critique Gate

Required for `production-ready`. In `fast-draft`, it runs after the first
preview and may remain pending without blocking `/generate`.

Output: `<page-workspace>/design-critique.md`,
`critique-390.png`, `critique-1280.png`.

1. Mechanical checks. Run
   `python3 <design-page-skill>/scripts/design_lint.py <page-workspace>` and
   paste its table into the critique, then run the remaining checks from
   `design-rules.md` §2.1 and §2.2 that the script does not cover. All of N1
   to N14 must be 0 or within the stated allowance; A3, A6, A7, A11, A12 must
   PASS.

2. Screenshots. Open `page-preview.html` in the browser tool. Capture
   full-page screenshots at 390 x 844 and 1280 x 800. Run the N2 background
   script and the A4 line-length script at 1280 and paste their results into
   the critique.

3. Look at both screenshots and answer each question in one line:
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

4. Fix, recompile, rerun 1 to 3. When the table has no FAIL and every question
   in 3 has an answer, show the preview and label it `ROUGH_PREVIEW` if asset
   polish remains. If the browser tool is unavailable, return
   `DESIGN_PREVIEW_READY_QA_PENDING` and list the visual checks that were not
   performed; never mark them passed.

## Approval

Show:

```text
Preview: [path]
Critique: design-critique.md (no FAIL)
Sections: [ordered list]
Interactive components: [islands]
Presets: [ids]
Reused assets: [slots]
Generated assets: [slots]
Temporary placeholders: [slots]
```

On approval, record only final IDs, compact island schema evidence, presets
and overrides, and source, theme, configuration, structure, and bundle hashes
in the manifest. Do not store creative explanations or tool transcripts there.

Any later visible source, CSS, copy, layout, island, or asset change returns
the design to `changes-pending-approval`.

## Return

Return the source, theme, preview, critique, compile-artifact paths, sections,
selected islands and presets, asset summary, and `DESIGN_APPROVED`.

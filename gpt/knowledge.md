<!-- GENERATED from skills/ by scripts/build-distributions.py — DO NOT EDIT.
     storefront-skills v7.2.1 · 10 skills · 47 active islands -->

# Lexsis Storefront Skills — Knowledge Base

## Workflows

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
`lexsis_drafts.asset_generate`, `lexsis_asset_upload.import`, and
`lexsis_assets.view`.

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

1. Search existing Lexsis assets.
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
- regenerate `page-preview.html`
- set `design.status` to `changes-pending-approval` for visible changes

Do not create a second HTML source. Placeholders may remain for local preview,
but `/generate` rejects them.

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

> Turn an approved one-page storefront plan into canonical Lexsis source and a responsive interactive preview, confirming any asset slots the plan left unresolved.

# Design the Page

Create the real page source and its browser-reviewable preview. Do not create
a remote draft or publish.

Read:

- `storefront-engine/references/design-rules.md`
- `storefront-engine/references/island-presets.md`
- `references/page-layout.md`
- `references/island-preview.md`

Use `lexsis_brand.context`, `lexsis_brand.get_theme`,
`lexsis_template_library.search_page_kits`,
`lexsis_template_library.search_sections`, `lexsis_design.guide`,
`lexsis_design.islands`, `lexsis_design.island_schema`,
`lexsis_design.get_section`, `lexsis_asset_library.search`,
`lexsis_catalog.get`, `lexsis_assets.view`, `lexsis_workspace.credits`,
`lexsis_drafts.asset_generate`, `lexsis_asset_upload.import`, and
`lexsis_pages.compile`.
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

## Design Direction Gate

Before writing any HTML, read the "Design direction" block in `page-plan.md`
and `storefront-engine/references/design-rules.md`. If the plan has no design
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

1. Slots with `status: verified` are final; use their ids and URLs as-is.
2. List only `planned` slots. `validate_page_workspace.py --phase design`
   reports them as `asset_slot_unresolved` warnings.
3. Ask once whether to generate them now (Lexsis first; offer other available
   image tools as an explicit provider choice), pick from the library or
   Shopify media, or keep a bundled preview placeholder for local review.
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
2. Use the template direction from the plan. Fetch selected section source;
   search again only when the plan has no usable template direction.
3. Convert each planned section into responsive layout and copy, following the
   wireframe, the Imagery and background plan, and the slot ids.
4. Read the compact island catalog and select only the likely interactive
   components. Do not fetch every full schema in advance.
   When the plan names a preset (`Preset: <island>/<intent>-<tone>`), apply it
   from `storefront-engine/references/island-presets.md` verbatim: props,
   `hydrate`, and its scoped CSS. Check its `requires` first. Unknown id:
   return `PRESET_NOT_FOUND`. Any deviation is recorded as
   `islands[].presetOverrides`; never edit a preset in place for one page.
5. Write a rough but complete `lexsis-source.html` with stable section
   delimiters, minimal island props, and the documented examples as a starting
   point.
6. Write global page rules to `page-theme.css`; keep section-specific CSS
   beside its section.
7. Use LX tokens for brand values and compile-time Tailwind utilities for
   layout. Do not use a runtime Tailwind CDN.
8. Compare explicit `NEVER`, `must`, and `non-negotiable` rules in the saved
   brand design with matching theme tokens. On a direct value contradiction,
   return `THEME_CONTEXT_CONFLICT` with both values. Do not silently choose one.
9. Use ordinary HTML for static content and `<lx-island>` source for supported
   interactions. Use headless mode only with complete required hooks.
10. Keep preview props safe and presentation-focused. Real commerce is tested
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

Do not show a preview path until the Self-Critique Gate passes. Then show the
first compiled preview as soon as the section structure and responsive
hierarchy are recognizable. Label it `ROUGH_PREVIEW`; asset polish and final
validation may continue after the user can see the direction.

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

Runs after the first clean compile and before any preview path or screenshot
is shown to the user. Output: `<page-workspace>/design-critique.md`,
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

### design-page reference: island-preview

# Island Preview

The browser runtime hydrates compiled `data-island` markers, not raw
`<lx-island>` authoring tags.

## Build

1. Resolve the live island schema.
2. Confirm active lifecycle status, required props, native variants, styling
   parts, and any headless hooks.
3. Prefer native mode and style only schema-listed parts.
4. Add readable `<lx-island>` source with preview props to
   `lexsis-source.html`.
5. Include a direct `data-lx-island-fallback` child.
6. Dry-run compile the complete canonical source with `page-theme.css`.
7. Require no missing Tailwind candidates.
8. Save the compile response and exact input hashes in
   `compile-artifact.json`.
9. Run:

```bash
python3 skills/design-page/scripts/build_page_preview.py \
  compile-artifact.json \
  work/visual-pages/<page-handle>/page-preview.html \
  --theme-css work/visual-pages/<page-handle>/page-theme.css
```

The builder uses the bundled shell, the exported Lexsis island runtime, and
the compiled section markup. Never hand-author `data-island` or `data-props`.

## Preview Data

Prefer real read-only product and media data. Use direct poster/video sources
and complete product objects when supported. If valid safe data is unavailable,
leave the fallback visible and record `previewMode: "fallback"`.

After opening the preview, require `data-lx-hydration-status="passed"` and
`window.__LEXSIS_PREVIEW_STATUS__.state === "passed"`. Fallback mode is useful
while iterating, but a required production island in fallback mode blocks
visual approval.

An island fallback is local to that island. It never authorizes replacing the
production island with custom controls.

ShoppableVideoFeed can run with real media while using a presentation mode
that does not navigate or write. Commerce and navigation islands should use
read-only props or fallback HTML.

## Preview Boundary

The shell does not add a content-security policy or replace browser network,
form, popup, or link behavior. Keep design-stage props presentation-focused
and avoid configuring real checkout or external navigation actions.

Real product resolution, add-to-cart, cart totals, and checkout are verified
only on the hosted Lexsis draft.

### design-page reference: page-layout

# Page Layout

The design stage approves hierarchy, section proportions, image placement,
typography, color balance, desktop composition, mobile stacking, CTA
placement, and island presentation.

Write:

- `lexsis-source.html` — the canonical readable page source
- `page-theme.css` — global theme tokens and page-wide custom CSS
- `compile-artifact.json` — exact compile response and input hashes
- `page-preview.html` — generated browser preview; never edit it directly

Use ordinary HTML for static content and active Lexsis islands only for useful
interaction previews. A supporting composition image may guide art direction,
but it must never become the page.

Start from the selected page kit or section templates. Use the selected
theme's `--lx-*` tokens and Tailwind utilities rather than rebuilding the
brand system inside each section. Record one coherent style treatment in the
manifest.

Search existing store and product assets first, show one combined asset
summary, and ask once before generating missing or optional media. When
generation is postponed, copy a bundled placeholder into the page workspace
and record it as `sourceType: "preview-placeholder"`.

Review at 390px and 1280px. `/generate` owns tablet and hosted-draft QA.

Approval hashes the exact source, page theme, head, scripts, structure, and
compiled bundle. `/generate` promotes this source instead of recreating it.

---

# Skill: experiment

> Create or evaluate a focused Lexsis storefront experiment from a clear hypothesis. Keeps every variant synchronized with its own local source before remote writes.

# Run a Storefront Experiment

Use this for a measurable comparison, not ordinary page editing.

Use `lexsis_pages.edit_context`, `lexsis_pages.source`,
`lexsis_pages.compile`, `lexsis_pages.integrity`, `lexsis_analytics.page`,
`lexsis_analytics.experiment`, `lexsis_drafts.page_duplicate`,
`lexsis_drafts.page_variation`, and `lexsis_drafts.experiment_create`.
Resolve unfamiliar argument schemas with exact router/action discovery. Do
not interpret an empty discovery result as a page or analytics outage. Report
any failure from the actual read or mutation and do not claim that operation
succeeded.

Confirm the base page's store/theme binding exists in
`work/storefront/setup/setup.json`. If it is missing, stop and ask the user to
run `/setup`; never invoke setup automatically.

## Define the Test

Confirm:

- page and current baseline version
- one primary hypothesis
- primary metric and guardrail metrics
- intended audience or traffic segment
- approved traffic split and stopping rule

Change as few elements as needed to test the hypothesis. If several unrelated
ideas are bundled together, split them into separate tests.

## Local-First Variants

Before duplicating or changing a remote page:

1. Confirm the base page has synchronized local source and manifest.
2. Create a separate local directory, source file, and manifest for each
   variant.
3. Apply the variant change locally.
4. Validate and compile the complete variant source.
5. Create or update the remote variant with the expected base version.
6. Store every returned page ID and version locally.
7. Run integrity, responsive, and affected commerce checks.

Never let a remote variant become the only copy of a change.

## Launch

Use the currently discovered Lexsis experiment actions and schemas. Confirm
entitlement and credits before creation. Do not publish a base page or variant
without explicit approval.

## Evaluate

Read the experiment's current status and results from Lexsis. Report:

- sample sizes and exposure split
- primary and guardrail metric movement
- whether the configured decision rule has been reached
- data-quality or targeting concerns
- recommended action: continue, stop, promote, or discard

Do not call a winner from directional movement alone.

## Return

Return the hypothesis, local variant paths, remote page/version IDs, experiment
ID, launch state, current decision, and MCP evidence.

---

# Skill: generate

> Promote approved canonical page source into a synchronized Lexsis draft and run hosted responsive, fidelity, and commerce QA.

# Generate the Draft

Create and verify a remote draft from the approved local page. Do not redesign
the page or publish it.

Read `references/source-and-sync.md`.

Use `lexsis_catalog.get`, `lexsis_design.island_schema`,
`lexsis_pages.compile`, `lexsis_pages.edit_context`,
`lexsis_pages.source`, `lexsis_pages.integrity`, and
`lexsis_page_create.create`.

## Inputs

Use the local source and compact schema-v3 manifest. `/asset-prep` is optional
and is never a required handoff. Final assets may have been selected or
generated directly by `/design-page`, imported independently, or prepared with
`/asset-prep`.

If `/design-page` was explicitly skipped, author the canonical source once and
record that skip without claiming design approval. Never invoke another skill
automatically.

Refresh only volatile data needed for creation: selected product variants,
prices, availability, permissions, and the remote page version when editing.
Do not reread unchanged setup, brand, theme, template, or asset-search context.

## Production Gate

Before draft creation:

- no preview placeholder remains
- all media URLs are permanent
- product and variant IDs are current
- selected island schemas remain active
- source, CSS, configuration, and bindings match the approved design hashes
- local validation passes
- `design-critique.md` exists with no FAIL and its hashes match the approved
  source (see `storefront-engine/references/design-rules.md`)
- no `planned` asset slot remains in the manifest

If assets are unresolved, report the missing roles. The user may return to
`/design-page`, run `/asset-prep`, or supply assets directly.

## Reuse the Compile Artifact

Read `compile-artifact.json`.

- Reuse it when source, theme CSS, configuration, structure, and bundle hashes
  still match and the selected live bindings have not changed.
- Recompile only when any compile input changed or the artifact is absent,
  invalid, or from an incompatible compiler surface.
- Never compile the same unchanged bundle merely because a new skill started.

Create with `publish: false`. Use a supported compile ID when available;
otherwise submit the exact source, CSS, head, scripts, and bindings represented
by the clean compile artifact.

Fetch the persisted source and page state immediately. Record only the page
ID, version, preview URL, local/remote hashes, and section hashes in the
manifest. A hash mismatch is blocking.

## Hosted QA

At 390px, 768px, and 1280px verify:

- the hosted draft matches the approved local design
- geometry, typography, color, spacing, and media remain faithful
- islands hydrate
- no overflow, clipping, or broken media exists
- the primary CTA uses the expected Shopify variant
- variant selection, cart opening, quantity, and subtotal work
- copy, claims, assets, and integrity pass

Write detailed evidence and blockers to `qa-report.md`. Store only compact QA
status, checked version, checked bundle hash, and check booleans in the
manifest.

Run the validator with `--phase draft` and live remote hashes. Return
`DRAFT_READY` only when synchronization and all blocking QA checks pass.

## Later Edits

Fetch the remote version and stop on drift. Change local source first, compile
only when inputs changed, patch only changed sections with `expected_version`,
and update local synchronization state after success.

## Return

Return the working directory, source, compile artifact, page ID, version,
preview URL, QA report, and `DRAFT_READY`.

### generate reference: source-and-sync

# Production Source and Synchronization

`lexsis-source.html` and `page-theme.css` are the editable source of truth.
`compile-artifact.json` and `page-preview.html` are generated.

Use `scripts/migrate_page_workspace_v3.py <working-directory>` for legacy
manifests.

## Compile Reuse

Compare the current source, theme CSS, configuration, structure, and bundle
hashes with `compile-artifact.json`.

- Matching inputs: reuse the compile artifact.
- Any changed or missing input: compile once and replace the artifact.
- Never recompile solely because `/generate` began in a new conversation.

## Creation

1. Validate the compact manifest and canonical source.
2. Confirm no preview placeholder remains.
3. Refresh only volatile products, variants, prices, permissions, and remote
   version data.
4. Reuse or refresh the compile artifact.
5. Create with `publish: false`.
6. Fetch persisted source and remote hashes.
7. Save compact `sync`, `remote`, and `qa` records.

## Editing

1. Fetch and compare the remote version.
2. Change local source.
3. Compile only if inputs changed.
4. Compare section hashes.
5. Patch changed sections with `expected_version`.
6. Save returned version and hashes after success.

Remote content must never be the only copy of an intentional change.

---

# Skill: optimize

> Diagnose and improve an existing Lexsis storefront page for a specific business outcome. Starts with a focused optimization brief before making local-first section edits.

# Optimize a Page

Read:

- `references/evidence-led-cro.md`

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
`storefront-engine/references/lexsis-design-capabilities.md`. Every edit obeys
the house rules in `storefront-engine/references/design-rules.md`; an
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
6. Present an optimization brief:

```text
Outcome:
Evidence:
Main friction:
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
return a focused hypothesis for `/experiment` instead of presenting the change
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

### plan-page reference: page-files

# Initial Page Files

Create:

```text
work/visual-pages/<page-handle>/
├── page-plan.md
├── page-manifest.json
└── assets/
```

Start with a compact progressive manifest:

```json
{
  "schemaVersion": 3,
  "status": "planned",
  "workflow": {
    "skippedSkills": []
  },
  "page": {
    "title": "...",
    "handle": "...",
    "archetype": "landing"
  },
  "workspaceId": "...",
  "storeId": "...",
  "themeId": "...",
  "setupPath": "work/storefront/setup/setup.json",
  "template": {
    "mode": "page-kit",
    "pageKitId": "...",
    "sectionTemplateIds": ["..."]
  },
  "sections": [
    "hero",
    "benefits",
    "closing-cta"
  ],
  "products": [
    {
      "productId": "...",
      "variantIds": ["..."]
    }
  ],
  "assets": [
    {
      "slotId": "A1",
      "role": "hero_bg",
      "sectionId": "hero",
      "sourceType": "lexsis",
      "assetId": "...",
      "url": "https://...",
      "status": "verified"
    },
    {
      "slotId": "A2",
      "role": "product_lifestyle",
      "sectionId": "benefits",
      "sourceType": "pending",
      "status": "planned"
    }
  ]
}
```

`template.mode` is `page-kit`, `sections`, or `custom`. For custom
composition, keep the rationale in `page-plan.md`; do not store template
search transcripts in JSON.

`assets[]` holds one entry per asset slot in the plan. `sourceType` is
`lexsis` (with `assetId`), `shopify` (with `productId` and `mediaId`),
`preview-placeholder`, or `pending` while the slot is still `planned`.
`status` is `verified` or `planned`.

The manifest grows only when later stages have real state to record:

- `/plan-page` writes `assets[]` (verified or planned).
- `/design-page` adds compact `config`, `islands`, and `design` records,
  resolves `planned` assets, and records `islands[].preset` and
  `islands[].presetOverrides` when a preset is applied.
- `/generate` adds `sync`, `remote`, and `qa`.

Do not prefill null production, approval, hash, QA, or remote fields. Do not
store copy intent, claims, occasion research, omitted components, or creative
notes in the manifest.

---

# Skill: publish

> Publish a synchronized and QA-passed Lexsis storefront draft. Use only when the user explicitly asks to release a specific page version.

# Publish a Page

Publishing is a separate, explicit action. Do not rebuild the page here.

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

> Connect a Lexsis storefront workspace and save reusable brand and theme design context. Run once initially, then only to add or refresh a store or theme.

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
2. Resolve the authorized workspace and connected stores.
3. When several stores or themes exist, ask the user which ones to save and
   which store/theme should be the default. Show names, not raw IDs.
4. For each selected store, read the brand kit, design guide, voice, and
   navigation. For each selected theme, read its exact theme CSS.
5. Write:

```text
work/storefront/setup/
├── setup.json
└── stores/
    └── <store-id>/
        ├── brand-design.md
        └── themes/
            └── <theme-id>.css
```

`setup.json` indexes every saved store/theme pair and identifies one default:

```json
{
  "schemaVersion": 1,
  "workspaceId": "...",
  "defaultStoreId": "...",
  "defaultThemeId": "...",
  "stores": [
    {
      "storeId": "...",
      "storeName": "Main Store",
      "brandDesignPath": "stores/<store-id>/brand-design.md",
      "themes": [
        {
          "themeId": "...",
          "themeName": "Light",
          "themeCssPath": "stores/<store-id>/themes/<theme-id>.css"
        }
      ]
    }
  ]
}
```

The default theme must belong to the default store. Adding a theme must not
replace another theme's CSS or another store's design file.

## Reuse

If a requested store/theme is already saved, reuse it. Refresh only when the
user asks, adds a store/theme, or Lexsis reports that the saved binding is no
longer valid.

Do not cache changing commerce or operational data. Page skills still read
current products, variants, prices, assets, island schemas, permissions,
credits, analytics, and remote page versions from Lexsis.

Never save credentials, cookies, authorization headers, or tokens.

## Return

Return the setup path, saved store/theme names, default selection, MCP status,
discovered capabilities, actions called, fallbacks, and blockers. Other skills
read this setup independently and never invoke `/setup` automatically.

---

## Reference Knowledge

---

# Storefront Craft Guide — Start Here

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
| `animation-system` | CSS animations, scroll-reveal, headline effects | Only when the plan names one motion moment |
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
6. **No `<script src="...">` in HTML** — use section `js` field for vanilla JS
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

# Design Rules

House rules for every generated page. They override generated brand `design.md`
guidance and brand-kit preview blueprints. Record every override in
`page-plan.md` under "Overrides of brand design.md".

Loaded by `/plan-page` (Design direction block), `/design-page` (Design Direction
Gate and Self-Critique Gate), `/generate` (Production Gate) and `/optimize`.
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

Format per rule: imperative sentence; rationale; a check the agent can run. Checks are written for macOS (BSD grep has no `-P`; use `perl -CSD`). `$W` is the page workspace, e.g. `work/visual-pages/<handle>`. Browser checks run in the preview via the browser tool's evaluate call.

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

N10. Never add motion that is not answering a user action, except one orchestrated moment named in the plan. No fade-up per section, no stagger, no counters, no parallax, no marquee ticker unless the announcement bar's own island provides it.
Rationale: scattered entrance effects are the generic default; one moment lands, ten do not (frontend-design; Sailop).
Check:
```bash
grep -cE 'data-reveal|IntersectionObserver|@keyframes|animation:' $W/lexsis-source.html $W/page-theme.css   # 0, or exactly the plan-named moment
grep -c 'prefers-reduced-motion' $W/page-theme.css   # 1 if any animation exists
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

A10. Always run the self-critique gate (section 3.2) with screenshots at 390 and 1280 and write `design-critique.md` before showing any preview path.
Rationale: a picture catches what grep cannot: banding, hierarchy, an eye that lands in the wrong place.
Check: `$W/design-critique.md` exists, has a results table with no FAIL, and references two screenshot files.

A11. Always ship the quality floor without announcing it: `:focus-visible` styles, `prefers-reduced-motion` handling, 48px minimum tap targets, alt text on product media, `lang` attributes on non-Latin text.
Check: `grep -c ':focus-visible' $W/page-theme.css` >= 1; `grep -c 'prefers-reduced-motion'` >= 1 when animation exists; `grep -c 'lang="'` >= 1 when Devanagari is present.

A12. Always write copy as design content: sentence case, active voice, the CTA says what happens ("Add to cart", not "Shop Now →"), no placeholder or invented copy, brand voice from `voice_md` or the merchant.
Check: `grep -cE '>(Shop Now|Get Started|Learn More|Buy Now)\s*(→)?<' $W/lexsis-source.html` is 0; no "lorem".


## Tells (fail the squint test)

Cream page + high-contrast serif + terracotta accent as the only idea; identical rounded cards with one radius and one grey shadow; tracked-out ALL-CAPS eyebrow above every heading; meta strings joined with middle dots; `WORD — fragment` labels; `→` appended to links and buttons; icon in a rounded tile above every heading; discount pills and "MOST POPULAR" ribbons; gradient washes; fade-up on every section; five gold stars with a round avatar and an italic quote; a monospace face for small labels; near-black `#0B0B0B` standing in for black.

Source audit: `work/research/lexsis-design-rules.md` (2026-09-05).

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

Rotating or grid review showcase with stars, verified flag, avatars, optional media. Category social_proof. Hydrate `visible`. Headless: no. Two data modes: static `reviews[]` (wins if non-empty) or fetch (`reviewsEndpoint` + filters). Mid-page or after product details, never first. Needs 3+ real reviews; never fabricate.

UI-controlling props:

| Prop | Type | Values / default | Effect |
|---|---|---|---|
| `variant` | enum | `default` \| `compact` \| `minimal` \| `grid` (default `default`) | default = one card carousel; compact = short strip; minimal = quote-only (short bodies only); grid = all at once |
| `autoplay` | boolean | true | set false for grid and for quiet pages |
| `interval` | number | 5000, keep >= 4000 | - |
| `pageSize` | number | 10, max 20 | fetch mode count |

Data props: `reviews[{id?, author, rating, title?, body, date?, verified?, avatar?, helpful_count?, media[]?}]`, `reviewsEndpoint`, `productIds[]`, `collectionId`, `reviewSnapshotId`, `minRating`, `sort` (`recent|highest|most_helpful`).
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

- **Fallback child.** `design-page/references/island-preview.md` asks for a direct `data-lx-island-fallback` child inside `<lx-island>`; `build_page_preview.py` does not reference that attribute, so its runtime handling is unconfirmed. Keep fallback markup simple, class-free or Tailwind-only (every class must compile), and free of interactive controls that could be mistaken for the island.
- **`animate` type.** Schema shows `boolean|boolean|string|string|string` for BuyBox, StickyBar, ProductCarousel; accepted string values are undocumented. Presets use booleans only.
- **Manifest evidence per island** (from `validate_page_workspace.py`): `{sectionId, name, schemaVersion, lifecycleStatus:"active", mode:"native"|"headless", previewMode:"hydrated"|"fallback"}`, in source order.

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
{"props":{"reviews":"{{reviews.top}}","variant":"grid","autoplay":false}}
```

**reviewcarousel/single-quiet** - one card at a time, manual arrows, no autoplay. Use when review bodies are long.
```json
{"props":{"reviews":"{{reviews.top}}","variant":"default","autoplay":false,"interval":6000}}
```

**reviewcarousel/strip-compact** - short strip of one-line reviews with slow rotation. Use near the BuyBox as a proof line, bodies under 60 chars.
```json
{"props":{"reviews":"{{reviews.short}}","variant":"compact","autoplay":true,"interval":6000}}
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

`islands[]` already carries `{sectionId, name, schemaVersion, lifecycleStatus, mode, previewMode}`. Add:

```json
{"sectionId":"buy","name":"BuyBox","schemaVersion":"5.1.0","lifecycleStatus":"active","mode":"native","previewMode":"hydrated","preset":"buybox/compact-dark","presetOverrides":{"ctaText":"Add to bag"}}
```

`preset` is a string or `null` (custom composition, rationale in `page-plan.md`). `presetOverrides` omitted when empty. `design.stylePack` stays; a preset set is not a style pack, but when a page uses presets of a single tone, record `design.presetTone`.

Source: `work/research/lexsis-island-presets.md`.

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
> artifact. It is dry-run compiled into an interactive local preview during
> `/design-page`, then promoted unchanged by `/generate`.

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
- Mobile-first responsive; shared keyframes or `data-behavior="gsap-*"` presets only for the one plan-named animation moment
- Islands go in directly as `<lx-island name="BuyBox">` with a JSON `<script>` child — use `lexsis_design` action `island_schema` for exact prop shapes

### Phase 4b — Compile & Fix

Run `lexsis_pages` action `compile`:
- Returns the compiled VibePage + compile issues + publish validation
- Fix reported issues in the source (unknown islands, bad props, missing hooks) and re-compile
- Require `missing_candidates` to be empty
- When clean, `lexsis_page_create` action `create` persists a draft; retrieve
  source later with `lexsis_pages` action `source`

### Why Two-Phase?
- Compiled visual source runs in the reusable local island preview shell
- Compile is instant and deterministic — validation before anything persists
- Separates design decisions from data-wiring decisions
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
    { "id": "hero", "html": "<section>...</section>", "css": "...", "js": "..." }
  ]
}
```

### Rules
- **Tailwind CSS** in HTML class attributes. The compiler emits one
  deterministic `compiled_page_css`; there is no runtime Tailwind CDN.
- **CSS Variables** (`--lx-*`) for all brand colors/fonts — set in `theme_css` (generate with `lexsis_brand.compile_theme`)
- **Islands** compile to `data-island="Name"` + `data-props='JSON'` attributes (in source format, write `<lx-island>` instead)
- **Section IDs** must be unique, kebab-case: "hero", "social-proof", "faq"
- **Section JS** is sandboxed — no fetch/XHR/eval/localStorage. Only DOM manipulation + IntersectionObserver. Runs after immediate islands mount; `lx:hydrated` / `lx:islands-ready` events signal island readiness
- **Shared keyframes** already loaded: fadeUp, fadeIn, scaleIn, slideInLeft, slideInRight, marquee, float, shimmer, wordFade, pulseRing. GSAP presets via `data-behavior="gsap-reveal|gsap-parallax|gsap-pin|gsap-marquee-scroll"` — available, never by default; use only for the one plan-named moment
- **No @import, no external URLs in CSS**; external JS libs go in `scripts[]`, never section HTML

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

| Need | Island | Key Props |
|------|--------|-----------|
| Add to cart | BuyBox | product.title, product.price, product.variants |
| Product images | ProductGallery | images[], layout |
| Cart drawer | DrawerShell | Contains CartLines + CartCheckoutButton |
| Reviews | ReviewCarousel | provider, productId |
| FAQ accordion | FAQ | items[{question, answer}] |
| Email capture | EmailCapture | provider, listId |
| Announcement | AnnouncementBar | message, link, dismissible |
| Navigation | Navbar / SiteHeader | links[], logo |
| Footer | Footer | links[], social[], newsletter |
| Product grid | EditorialProductGrid | products[], columns |
| Trust badges | TrustBadgeBar | badges[{icon, text}] |
| Social proof popup | SocialProofPopup | provider, delay |

### Prop Data Sources
- Product data → `lexsis_catalog` action `get` or `list`
- Navigation → `lexsis_brand` action `navigation`
- Reviews → configured review source or public reviews endpoint; never invent
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

<script>
  /* becomes section.js — sandboxed; `section` is bound to this section's element */
  section.querySelectorAll('.hero-lede').forEach(el => el.classList.add('ready'));
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
4. **Section CSS** goes in a top-level `<style>` block; **section JS** in a top-level `<script>` block (multiple blocks are concatenated). `application/json` / `ld+json` scripts stay in the HTML.
5. **External libraries** do not go in section HTML—pass them through `scripts`.
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

### Presets (no JS needed) — `data-behavior`

```html
<section data-behavior="gsap-reveal" data-config='{"targets":".card","y":40,"stagger":0.1}'>
<div data-behavior="gsap-parallax" data-config='{"speed":0.3}'>
<section data-behavior="gsap-pin" data-config='{"stepDuration":0.5}'>  <!-- children: [data-pin-step] -->
<div data-behavior="gsap-marquee-scroll" data-config='{"distance":-200}'>
```

Presets lazy-load GSAP from CDN themselves and respect `prefers-reduced-motion`. Also available (CSS-driven, pre-existing): `scroll-reveal`, `accordion`, `horizontal-scroll`, `content-slider`, `sticky-reveal`.

### Custom GSAP in section JS

Load the library via the `scripts` param, then write timelines in the section `<script>`:

```json
"scripts": [
  { "src": "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js", "position": "body-end" },
  { "src": "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js", "position": "body-end" }
]
```

The compiler warns (`missing_animation_lib`) if section JS references gsap without either a scripts entry or a `gsap-*` preset on the page. Section JS runs after immediate islands mount; for work that depends on a deferred island, listen for its `lx:hydrated` event (bubbles, `detail.island`) or the document-level `lx:islands-ready`.

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
- Design selects islands, resolves page assets, and creates the interactive
  source preview.
- Generate owns production source, draft creation, and hosted QA.
- Publish is a separate explicit release.

Commands do not silently invoke one another. When a user intentionally starts
later, create the minimum missing artifact and record the skipped command.

## Optional Routes

- Use `/analyze-page` before planning when a URL, screenshot, or ad matters.
- Use `/asset-prep` independently for standalone or replacement asset work.
- Use `/optimize` for an existing page and a specific outcome.
- Use `/experiment` for a measurable hypothesis.
- Use `/cart` for cart profile configuration.

## Shared Safety

- Bind every page to one saved store/theme pair.
- Read changing product, price, asset, schema, permission, analytics, and
  version data live.
- Search existing assets before paid generation.
- Resolve island schemas before authoring.
- Keep production changes local-first and stop on version drift.
- Create drafts with `publish:false`.
- Publish only after current QA and explicit approval.

---

# Conversion Psychology — Storefront Design Intelligence

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
      <p class="text-3xl md:text-4xl font-bold" style="color:var(--lx-text-color);font-family:var(--lx-font-heading)">247,000+</p>
      <p class="text-sm mt-2" style="color:var(--lx-text-muted)">Happy customers</p>
    </div>
    <div>
      <p class="text-3xl md:text-4xl font-bold" style="color:var(--lx-text-color);font-family:var(--lx-font-heading)">4.8/5.0</p>
      <p class="text-sm mt-2" style="color:var(--lx-text-muted)">Average rating</p>
    </div>
    <div>
      <p class="text-3xl md:text-4xl font-bold" style="color:var(--lx-text-color);font-family:var(--lx-font-heading)">12,000+</p>
      <p class="text-sm mt-2" style="color:var(--lx-text-muted)">Five-star reviews</p>
    </div>
    <div>
      <p class="text-3xl md:text-4xl font-bold" style="color:var(--lx-text-color);font-family:var(--lx-font-heading)">94%</p>
      <p class="text-sm mt-2" style="color:var(--lx-text-muted)">Would recommend</p>
    </div>
  </div>
</section>
```

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
    <h2 class="text-3xl md:text-4xl font-bold text-center mb-12" style="color:var(--lx-text-color)">12,000+ 5-Star Reviews</h2>
    <div data-island="ReviewCarousel" data-props='{"autoplay":true,"reviewsPerView":3,"reviews":[{"rating":5,"text":"Exceeded expectations. Results were visible in days. Highly recommend.","author":"John D.","verified":true,"date":"2026-06-15"}]}'></div>
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

# Island Patterns — Wrapper HTML & Combination Recipes

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
    <div data-island="ReviewCarousel" data-props='{"reviews":[{"author":"Priya M.","rating":5,"body":"Amazing results in just one week!","date":"2026-05-01"},{"author":"Ananya R.","rating":5,"body":"Best serum I have ever used.","date":"2026-04-15"},{"author":"Kavita S.","rating":4,"body":"Great for sensitive skin.","date":"2026-03-20"}],"autoplay":true}'></div>
  </div>
</section>
```

**With Shopify product reviews (auto-fetch):**

```html
<div data-island="ReviewCarousel" data-props='{"reviewsEndpoint":"/api/v1/storefront/public/reviews/PAGE_SHORT_ID","productIds":["gid://shopify/Product/123"],"autoplay":true}'></div>
```

Use the carousel only with 3 or more real reviews. For 1-2 verified reviews,
render static testimonial cards. If there are no reviews, use product proof,
certifications, guarantees, or verified press instead. Never fabricate names,
ratings, locations, or review counts.

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
└─ After sourcing → lexsis_asset_upload action import
```

---

## Built-In Tools (Lexsis AI MCP)

| Tool | What it does | Cost |
|------|-------------|------|
| `lexsis_asset_library` → `search` | Search workspace assets | Free |
| `lexsis_drafts` → `asset_generate` | Generate, composite, inpaint, or restyle | Credits |
| `lexsis_assets` → `view` | Verify an asset | Free |
| `lexsis_asset_upload` → `import` | Import URL, base64, attachments, or use upload picker | Free |

Always search first. Pass `workspace_id` explicitly when multiple workspaces
are available and the selected `theme_id` whenever the discovered action
schema supports it.

See `design-enrichment.md` for detailed prompt patterns, style selection guide, compositing recipes, and HTML placement patterns.

---

## External MCPs (Detected at Runtime)

These tools are available when the user has the corresponding MCP installed. Check availability before suggesting.

### Exa — Image Research & Reference

```
web_search_exa({ query: "skincare brand hero photography editorial style" })
```

Use for: mood boards, competitor visual research, finding reference imagery to brief `lexsis_drafts` action `asset_generate` more precisely, sourcing real lifestyle photos.

**Flow:** Exa search → find URL → `lexsis_asset_upload` action `import` → use
the returned permanent URL.

### HiggsField / Runway / Kling — Video Generation

Use when: TikTok traffic source, fashion/luxury vertical, product demo needed, brand has no existing video content.

**Flow:**
1. Generate video via external MCP (short clip, 3-8 seconds)
2. `lexsis_campaigns.frames` → pull best frame as thumbnail
3. Use video URL in HeroMedia island or `<video>` tag
4. Set click-to-play (NEVER autoplay — costs 7% CVR)

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
2. lexsis_asset_upload({
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
- NEVER autoplay video (-7% CVR)
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
4. External MCP assets → `lexsis_asset_upload` action `import`
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
- [ ] Inherited header and footer are correct
- [ ] Full-page hosted screenshots match `page-preview.html` at all three
      viewports
- [ ] Dynamic island regions preserve the approved container geometry and
      placement
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
7. Compare the compiled local preview and hosted draft at 390px, 768px, and
   1280px, then run commerce QA
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
7. Patch only changed sections with `expected_version`.
8. Update manifest version/hashes after success, then run `diff` and `integrity`.

For existing pages, `page_id` is authoritative. Do not require the user to
reselect a workspace or pass `store_id`; an optional store ID is only an
assertion. Service-token store/workspace scopes remain authorization boundaries.

## Operations

### Update/Replace a Section

```
lexsis_drafts({
  action: "page_update_section",
  args: { page_id, section_id, source, expected_version }
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
  args: { page_id, source, position, expected_version }
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
- Batch related multi-section changes with `page_patch` so they create one version
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout

Minor edits do not repeat planning, but they still require a local source
workspace and a matching saved store/theme setup. Adoption creates page files;
it does not rerun `setup`.

For published pages, `current_version` can advance while the live renderer
remains pinned to `published_version_id`. Publish only after QA.

---

# Storefront Page Files

Use local files to pass work between commands without depending on chat
history.

## Workspace

```text
work/visual-pages/<page-handle>/
├── page-plan.md
├── page-manifest.json
├── lexsis-source.html
├── page-theme.css
├── compile-artifact.json
├── page-preview.html
├── qa-report.md
└── assets/
```

Files appear progressively. Planning creates only the plan, compact manifest,
and assets directory. Design creates source, CSS, compile artifact, and
preview. Generation creates the QA report and remote synchronization state.

## Compact Manifest

Use `schemaVersion: 3`.

The manifest is a machine state ledger. Store only:

- page, workspace, store, and theme IDs
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
    "status": "approved",
    "stylePack": "editorial",
    "compiledStyleManifest": {},
    "sourceHash": "...",
    "themeCssHash": "...",
    "configHash": "...",
    "structureHash": "...",
    "bundleHash": "...",
    "compiledBundleHash": "...",
    "hydration": {
      "status": "passed",
      "bundleHash": "...",
      "expectedIslands": [],
      "hydratedIslands": [],
      "checkedAt": "..."
    }
  }
}
```

`lexsis-source.html` and `page-theme.css` are the only editable design inputs.
`compile-artifact.json` and `page-preview.html` are generated.

## Remote State

`/generate` adds:

```json
{
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

For editing:

1. Fetch the remote version and stop on drift.
2. Change local source first.
3. Compile only if an input changed.
4. Compare section hashes.
5. Patch only changed sections with `expected_version`.
6. Update synchronization state only after success.

Legacy schema-v1 and schema-v2 workspaces use
`skills/generate/scripts/migrate_page_workspace_v3.py`.

---

# Island Preview

Use this during `/design-page`.

1. Resolve the selected island's active schema.
2. Author readable `<lx-island>` source with safe preview data.
3. Compile the complete canonical page.
4. Save the response and input hashes in `compile-artifact.json`.
5. Run `design-page/scripts/build_page_preview.py`.
6. Save `page-preview.html`.
7. Confirm every required island hydrates before design approval.

The preview uses compiled renderer markup and the exported Lexsis island
runtime. Never hand-author `data-island` or `data-props`.

Fallback HTML may keep an isolated component visible while iterating, but a
required production island in fallback mode blocks approval. Real product
resolution and cart behavior are verified on the hosted draft.

---

# Design Page Workflow

`/design-page` turns an approved one-page section plan into canonical Lexsis
source and an interactive local preview.

It owns:

- existing-asset inventory and the single generation decision
- responsive layout and copy composition
- island selection and schema resolution
- `lexsis-source.html` and `page-theme.css`
- one clean compile artifact and `page-preview.html`
- 390px and 1280px approval

The plan supplies section intent, not islands. `/generate` supplies tablet,
hosted-fidelity, and real-commerce QA.

Placeholders are allowed while reviewing the local design. They are recorded
as `sourceType: "preview-placeholder"` and cannot pass production validation.

An optional `/asset-prep` run may replace or improve media, but it is not a
required handoff. Any visible replacement returns the design to
`changes-pending-approval`.

---

# Public Storefront Workflow

The customer-facing pack has ten commands. Five form the normal page journey:

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
| `design-page` | Assets, islands, source, and responsive preview | canonical source and preview |
| `generate` | Production source, draft, and hosted QA | `DRAFT_READY` |
| `publish` | Explicit live release | published version |

Four optional commands support the workflow:

| Command | Owns |
|---|---|
| `analyze-page` | URL, screenshot, ad, or own-page analysis |
| `asset-prep` | Independent asset search, generation, import, or replacement |
| `optimize` | Outcome-led existing-page improvement |
| `experiment` | Controlled variants and result evaluation |
| `cart` | Cart profile inspection, assignment, and editing |

## Rules

1. Each command owns one outcome and can be invoked independently.
2. Commands read artifacts from earlier steps but never invoke earlier steps
   automatically.
3. Explicit skips are recorded in the page manifest.
4. Every page binds one saved store/theme pair.
5. `lexsis-source.html` is the production source of truth.
6. Draft creation is not publishing approval.

---

# Lexsis MCP Contract

Lexsis MCP is the system of record for templates, catalogue data, assets,
island schemas, compilation, drafts, remote versions, analytics, carts,
experiments, and publishing.

MCP dependency metadata and an `.mcp.json` entry describe configuration. They
do not prove that the server or its tools are available in the current
session.

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

1. Discover `lexsis_template_library` actions `search_page_kits` and
   `search_sections`.
2. Search page kits using page type, archetype, objective, industry, and mood.
3. Treat a page kit as a coherent list of section-template IDs. There is no
   single page-kit instantiation action.
4. Fetch selected section source through `lexsis_design` action `get_section`,
   at most three IDs per call.
5. Adapt the returned source to the selected theme, plan, products, copy, and
   assets.

Template search returns metadata, not editable markup. `get_section` returns
authoring source with section delimiters, `<lx-island>` markup, and section
CSS/JS.

If the host renders an interactive template picker, wait for the user's
selection. Custom composition is allowed only after recording the evaluated
templates and why none fit.

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

## Visual Preview

The design-stage source is compiled without saving. The local preview uses the
compiled markup and exported Lexsis island runtime.

- Use real compiled islands when schema-valid preview data exists.
- Shoppable video, galleries, accordions, and similar islands should run in
  the preview when their media and props are valid.
- A static fallback is permitted only for the affected island when it cannot
  compile or lacks safe preview data.
- Local interaction demonstrates presentation; hosted-draft QA certifies real
  product resolution, cart behavior, checkout-related behavior, and remote
  integrations.

Inspect 390px and 1280px during design. `/generate` adds 768px and hosted QA.

## Asset Roles

Template results do not expose a separate media-slot schema. Derive required
roles, aspect ratios, and crop guidance from the selected section source,
approved layout, and island schema.

Use live Shopify media for product identity. Visually verify creator and
product imagery. Temporary placeholders are visual-stage inputs only.

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

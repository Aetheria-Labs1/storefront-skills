<!-- GENERATED from skills/ by scripts/build-distributions.py — DO NOT EDIT.
     storefront-skills v7.0.0 · 10 skills · 47 active islands -->

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
Confirm `lexsis_discover` is available and discover the exact actions needed.
If that preflight fails, return `BLOCKED_LEXSIS_MCP` rather than replacing
missing live data with assumptions.

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

> Replace visual-page placeholders with verified production images and video. Searches Lexsis and Shopify first, then generates or imports only what is still missing.

# Prepare Page Assets

Use the approved plan and visual mockup to finalize media. Do not author the
production page or create a draft.

Before reading live assets or changing the page workspace, confirm
`lexsis_discover` is available and discover the exact asset, catalogue,
generation, upload, and inspection actions needed by this run. If discovery
fails, return `BLOCKED_LEXSIS_MCP` without changing page artifacts.

The full skill pack includes optional deeper design guidance at
`storefront-engine/references/lexsis-design-capabilities.md`.

Read the page's saved store/theme binding. Stop if it does not match
`work/storefront/setup/setup.json`; never run setup automatically.

Read the selected template section sources and island schemas. Derive media
roles, aspect ratios, and crop guidance from those sources and the approved
layout; do not assume template search returns a separate media-slot schema.

## Source Order

For each asset role:

1. Search `lexsis_asset_library`.
2. For product media, use the real Shopify media from `lexsis_catalog`.
3. If a non-product image is still missing, check credits and use
   `lexsis_drafts` action `asset_generate`.
4. If an external tool supplies media, persist it through
   `lexsis_asset_upload` action `import`.
5. Inspect the final asset with `lexsis_assets` action `view`.

Pass the selected workspace and theme IDs whenever the current action schema
supports them. Never generate product pack shots or infer identity from a file
name. Creator and product imagery must be visually verified.

## Update the Mockup

Replace every `preview-placeholder` asset in the page workspace and manifest
with a permanent Lexsis or Shopify asset. Regenerate `visual-preview.html` so
the approved composition can be checked with final media.

Every manifest asset records:

```json
{
  "role": "hero",
  "sectionId": "hero",
  "sourceType": "lexsis",
  "assetId": "...",
  "url": "https://...",
  "width": 1600,
  "height": 1200,
  "desktopCrop": "center",
  "mobileCrop": "center top",
  "altTextIntent": "Product beside a glass",
  "verificationStatus": "verified"
}
```

Shopify media uses `productId` and `mediaId` instead of `assetId`.

## Gate

Before completion, confirm:

- no bundled placeholder remains
- every URL is permanent
- desktop and mobile crops work
- identity-sensitive media was visually verified
- generated media does not make unsupported product claims

## Return

Update `page-manifest.json` and return `ASSETS_READY` with the verified roles,
IDs, URLs, dimensions, crops, alt-text intent, template evidence, and MCP
evidence. The next normal command is `/generate`.

---

# Skill: cart

> Inspect, assign, or edit Lexsis cart profiles for a storefront page. Covers offers, shipping goals, subscriptions, responsive behavior, and scoped cart styling.

# Configure a Cart

Cart profiles are managed separately from page section HTML.

Confirm `lexsis_discover` is available and discover the exact cart read/write
actions needed by this request. If discovery fails, return
`BLOCKED_LEXSIS_MCP`; do not infer the effective cart profile from page HTML.

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

# Skill: experiment

> Create or evaluate a focused Lexsis storefront experiment from a clear hypothesis. Keeps every variant synchronized with its own local source before remote writes.

# Run a Storefront Experiment

Use this for a measurable comparison, not ordinary page editing.

Confirm `lexsis_discover` is available and discover the exact page, analytics,
experiment, and draft actions needed by this request. If discovery fails,
return `BLOCKED_LEXSIS_MCP` without creating local or remote variants.

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

> Turn an approved plan, visual mockup, and verified assets into readable Lexsis source, a compiled draft, and a synchronized QA report.

# Generate the Draft

Own production source, compilation, draft creation, and hosted interaction QA.
Do not publish.

Read `references/source-and-sync.md`.

Complete a fresh MCP preflight before reading live data or changing production
artifacts. Do not trust an earlier skill's connection as proof that MCP is
available in this session. Discover the exact catalogue, template, brand,
island, compile, page-create, and edit actions needed by this run. If discovery
fails, return `BLOCKED_LEXSIS_MCP` without changing production artifacts.

When the full Lexsis skill pack is installed, also read
`storefront-engine/references/lexsis-design-capabilities.md` for the detailed
LX token, Tailwind, template, and island styling contract. The production
rules below remain complete when that shared reference is unavailable.

## Inputs

Use the page workspace created by earlier commands. If the user explicitly
skipped planning, visual design, or asset preparation, create the minimum
replacement artifact and record that skill in `workflow.skippedSkills`.
Never invoke another skill automatically.

Confirm the manifest's store/theme pair is saved in setup. Read current
products, variants, prices, availability, permissions, credits, assets, island
schemas, and remote versions live.

## Author the Source

1. Treat the approved plan and visual composition as the design contract.
2. Reuse the selected page kit or section-template source. When earlier skills
   were explicitly skipped, search and fetch templates before custom
   composition.
3. Replace preview values and temporary media with verified live bindings.
4. Resolve every island's current active schema again. Prefer native variants
   and validated styling parts; use headless mode only with complete hooks.
5. Write complete, readable `lexsis-source.html` before compiling.
6. Use one `<!-- section: id -->` followed by `<section id="id">` per section.
7. Keep island JSON readable where practical.
8. Use LX tokens for brand values and Tailwind utilities for layout. Do not
   depend on a runtime Tailwind CDN.
9. Use native commerce islands; never replace BuyBox or another commerce
   interaction with a custom button.
10. Keep production comments to section delimiters and exclude inline handlers,
   unsupported scripts, local paths, placeholders, and complete-page images.

Run:

```bash
python3 skills/generate/scripts/validate_page_workspace.py \
  work/visual-pages/<page-handle> --phase precompile
```

Fix all blocking source, copy, claim, price, and asset findings.

## Compile and Create

Dry-run the complete source with `lexsis_pages` action `compile`. Fix all
compiler errors, including every missing Tailwind candidate, before calling
`lexsis_page_create` action `create` with `publish: false`.

Store the returned page ID, version, and preview URL in the manifest. Record
the source bundle hash and section hashes as the synchronized baseline.
Store the compiler style manifest under `design.compiledStyleManifest`.
`lexsis-source.html` remains the editable source of truth.

## Hosted QA

At 390px, 768px, and 1280px verify:

- composition matches the approved mockup
- no overflow, clipping, broken media, or wrong theme
- islands hydrate
- primary CTA adds the expected Shopify variant
- variant selection, cart opening, quantity, and subtotal work
- copy, claims, assets, header, footer, and integrity pass

Write `qa-report.md` and update the manifest's QA fields.

## Later Edits

Read the remote version and stop on unexpected drift. Change local source,
compile the full page, identify changed section hashes, patch only those
sections with `expected_version`, then update the manifest after success.

## Return

Return:

```text
working_directory
page_plan_path
page_manifest_path
visual_source_path
visual_preview_path
source_html_path
compile_result
page_id
page_version
preview_url
qa_report_path
```

Return `DRAFT_READY` only when synchronization and blocking QA checks pass.
Include the required MCP, template, binding, fallback, and blocker evidence.

### generate reference: source-and-sync

# Production Source and Synchronization

## Page Files

The page workspace contains:

```text
page-plan.md
page-manifest.json
visual-source.html
visual-preview.html
lexsis-source.html
qa-report.md
assets/
```

Visual files may be absent only when the user explicitly skipped the visual
stage.

## Source Format

Use one stable delimiter and matching section ID:

```html
<!-- section: hero -->
<section id="hero">
  <lx-island name="BuyBox" hydrate="immediate">
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

Keep HTML and island JSON readable. Section IDs are unique. Production source
contains no temporary asset paths, preview placeholders, inline event handlers,
unsupported scripts, internal notes, or hand-authored runtime island markup.

Resolve the current schema before every island. Prefer native presentation and
use headless variants only when their required hooks are fully implemented.

## Compile and Create

Validate locally, compile the complete source without saving, fix every
blocking issue including missing Tailwind candidates, then create with
`publish:false`.

Save the returned page ID, version, preview URL, bundle hash, and per-section
hashes. Save the returned style manifest under
`design.compiledStyleManifest`. The bundle hash covers source, head, theme
CSS, and page scripts.

### Creation Example

1. Discover the exact `lexsis_pages.compile` and
   `lexsis_page_create.create` schemas.
2. Compile the complete local source with the selected head, theme CSS, theme
   ID, scripts, and product binding.
3. Fix every blocking issue without saving remotely.
4. Create the page as a draft with `publish:false`.
5. Save the returned page ID, version, preview URL, bundle hash, section
   hashes, and style manifest.

## Edits

1. Fetch the remote version and compare it with the manifest.
2. Stop on drift.
3. Change local source.
4. Validate and compile the complete page.
5. Read `changedSections` from the validator.
6. Patch only those sections with `expected_version`.
7. Update local hashes and version only after success.

Remote content must never be the only copy of an intentional change.

### One-Section Edit Example

For a hero-only change:

1. Fetch the current remote version and stop if it differs from the manifest.
2. Edit only the hero block in `lexsis-source.html`.
3. Compile the complete local page.
4. Confirm the validator reports only `hero` in `changedSections`.
5. Patch the hero source with the discovered section-update action and
   `expected_version`.
6. Save the returned version and new hashes only after the patch succeeds.
7. Repeat responsive, asset, copy, and affected interaction checks.

## QA

Record MCP status, capabilities, actions, template decision, live bindings,
fallbacks, compilation, local bundle, remote version, 390px/768px/1280px
results, commerce interaction, copy, claims, assets, integrity, blockers, and
publish readiness in `qa-report.md`.

---

# Skill: optimize

> Diagnose and improve an existing Lexsis storefront page for a specific business outcome. Starts with a focused optimization brief before making local-first section edits.

# Optimize a Page

Read:

- `references/evidence-led-cro.md`

Before reading the Lexsis page, analytics, or remote version, confirm
`lexsis_discover` is available and discover the exact page, analytics,
template, compile, and edit actions required by this run. If discovery fails,
return `BLOCKED_LEXSIS_MCP`; generic CRO guidance is not a substitute for
unavailable live page data.

The full skill pack includes optional deeper design guidance at
`storefront-engine/references/lexsis-design-capabilities.md`.

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
source, compare section hashes, and patch only changed sections with
`expected_version`. Update the manifest only after the remote write succeeds.
Then run `diff`, `integrity`, responsive checks, and affected commerce checks.

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

> Turn campaign and product requirements into an approved storefront page plan. Use before visual design; this skill does not generate mockups, assets, or page source.

# Plan a Page

Create the strategy and section blueprint for one storefront page.

Read:

- `references/page-files.md`

Before creating or changing the page workspace, confirm `lexsis_discover` is
available and discover the exact catalogue and template actions required by
this run. Configuration alone is not proof of connection. If discovery fails,
return `BLOCKED_LEXSIS_MCP` without changing page artifacts.

When the full Lexsis skill pack is installed, the optional detailed contracts
are under `storefront-engine/references/lexsis-mcp-contract.md` and
`storefront-engine/references/lexsis-design-capabilities.md`.

Read `work/storefront/setup/setup.json`, select one saved store/theme pair, and
read its brand design and theme CSS. Prefer an explicit selection, then an
existing page binding, then an unambiguous default. If the selection is not
saved, stop with `Run /setup for this store and theme first.`

## Ask Only What Is Missing

Collect:

1. Page or campaign type.
2. Product or collection.
3. Audience and customer problem.
4. Traffic source.
5. Primary conversion goal and CTA.
6. Required proof, claims, offers, or sections.

Ask no more than four questions at once. Read current products, variants,
prices, and availability from `lexsis_catalog`; do not rely on setup for them.
If a URL, screenshot, or ad is important, use the compact output from
`/analyze-page`.

## Select a Template Direction

Discover the current template actions, then search page kits using the page
type, archetype, objective, industry, and mood. A kit is a coherent list of
section-template IDs, not a page-instantiation action.

If no suitable kit exists, search individual sections. In a host with an
interactive template picker, wait for the user's selection. Record evaluated
results, the selected kit/sections, or the reason for a custom composition.

## Produce `page-plan.md`

Include:

- objective, buyer, traffic source, and primary CTA
- selected workspace, store, theme, product, and collection
- ordered section map with copy intent
- visual rhythm and desktop/mobile behavior
- asset roles
- required islands
- claims requiring evidence
- selected template direction and adaptation intent

Start `page-manifest.json` using `references/page-files.md`, including the MCP,
template, and design records. Create the page working directory and `assets/`,
but do not write visual or production HTML.

## Approval

Present a compact summary:

```text
Page: [type]
Goal: [conversion goal]
Audience: [buyer]
Sections: [ordered list]
Islands: [list]
Assets needed: [list]
Claims to verify: [list]
```

Wait for approval and update the plan when requested.

## Return

Return `working_directory`, `page_plan_path`, `page_manifest_path`, and
`PLAN_APPROVED`, plus the required MCP and template evidence. The next normal
command is `/visual-page`, but this skill is complete after the plan is
approved.

### plan-page reference: page-files

# Initial Page Files

Create:

```text
work/visual-pages/<page-handle>/
├── page-plan.md
├── page-manifest.json
├── qa-report.md
└── assets/
```

Start the manifest with:

```json
{
  "schemaVersion": 1,
  "status": "planned",
  "workflow": { "skippedSkills": [] },
  "mcp": {
    "status": "connected",
    "checkedAt": "2026-09-04T12:00:00Z",
    "surfaceVersion": "3.0",
    "capabilities": [
      {
        "router": "lexsis_catalog",
        "actions": ["get"]
      }
    ]
  },
  "page": {
    "title": "...",
    "handle": "...",
    "archetype": "landing"
  },
  "workspaceId": "...",
  "storeId": "...",
  "themeId": "...",
  "template": {
    "mode": "page-kit",
    "pageKitId": "...",
    "sectionTemplateIds": ["..."],
    "evaluatedTemplates": [],
    "selectionReason": "...",
    "selectedAt": "2026-09-04T12:00:00Z"
  },
  "design": {
    "themeId": "...",
    "themeSource": "saved-and-verified",
    "stylePack": null,
    "compiledStyleManifest": null
  },
  "setupPath": "work/storefront/setup/setup.json",
  "brandDesignPath": "...",
  "themeCssPath": "...",
  "pageConfig": {
    "head": {},
    "themeCss": "",
    "scripts": []
  },
  "productBindings": [],
  "assets": [],
  "sections": [],
  "islands": [],
  "visual": {
    "status": "pending",
    "sourcePath": "visual-source.html",
    "previewPath": "visual-preview.html"
  },
  "sourceSync": {
    "lastCompiledBundleHash": null,
    "lastSyncedBundleHash": null,
    "lastSyncedSectionHashes": {},
    "lastChangedSections": []
  },
  "qa": {
    "status": "pending",
    "checkedVersion": null,
    "checkedBundleHash": null,
    "responsive": false,
    "commerce": false,
    "copy": false,
    "claims": false,
    "assets": false,
    "integrity": false
  },
  "remote": {
    "pageId": null,
    "lastKnownVersion": null,
    "previewUrl": null
  }
}
```

The page binds one saved store/theme pair. Do not write visual or production
source during planning. `template.mode` is `page-kit`, `sections`, or `custom`.
Custom composition requires recorded template evaluation and a
`selectionReason`. Do not invent a template version when Lexsis does not
return one.

---

# Skill: publish

> Publish a synchronized and QA-passed Lexsis storefront draft. Use only when the user explicitly asks to release a specific page version.

# Publish a Page

Publishing is a separate, explicit action. Do not rebuild the page here.

Complete a fresh MCP preflight and discover the exact page-context,
entitlement, and publish actions required by this run. If discovery fails,
return `BLOCKED_LEXSIS_MCP`; a local QA report cannot authorize or substitute
for a live publish action.

## Gate

1. Read the page manifest and QA report.
2. Confirm the saved store/theme binding still exists.
3. Confirm the current local bundle and section hashes match the synchronized
   values in the manifest.
4. Read `lexsis_pages` action `edit_context`.
5. Confirm the remote version equals `remote.lastKnownVersion`.
6. Confirm responsive, commerce, copy, claims, assets, and integrity checks
   passed against that same version and local bundle.
7. Confirm the store has the required entitlement.
8. Ask for explicit approval naming the page and version.

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

A successful `lexsis_discover` call is required; MCP configuration alone is
not a connection check. If discovery fails, return `BLOCKED_LEXSIS_MCP`
without writing setup files.

## What to Save

1. Use `lexsis_discover` for the exact workspace, store, brand, theme, design,
   and navigation actions required by this run.
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

# Skill: visual-page

> Turn an approved storefront plan into a responsive, theme-aware mockup using compiled Lexsis templates and islands. Static fallbacks are limited to isolated preview failures.

# Create the Visual Page

Create the design-stage mockup only. Do not prepare final assets, create a
Lexsis draft, or publish.

Read:

- `references/visual-layout.md`
- `references/island-preview.md`

Complete the MCP preflight before reading or changing standard page artifacts.
MCP unavailable means `BLOCKED_LEXSIS_MCP`, not a silent static replacement.
Discover the exact brand, template, design, island, and compile actions needed
by this run.

When the full Lexsis skill pack is installed, also read
`storefront-engine/references/lexsis-design-capabilities.md` for the detailed
LX token, Tailwind, template, and island styling contract. The workflow below
remains complete when that shared reference is unavailable.

## Inputs

Use an approved `page-plan.md` and its saved store/theme binding. If the user
explicitly skips `/plan-page`, write a short plan from the brief and record the
skip. Never run `/setup` or `/plan-page` automatically.

Use existing Lexsis or Shopify media first. When an image is still missing,
copy an appropriate neutral file from `assets/placeholders/` into the page
workspace. Placeholders are for design approval only.

## Load the Design System

1. Read the saved brand design and exact selected theme CSS.
2. Refresh the complete theme with the discovered `lexsis_brand` action when
   the binding is stale or the task needs current theme configuration.
3. Search page kits before custom composition.
4. Fetch the selected section-template source in batches of at most three.
5. Choose one coherent style treatment for the page.
6. Use LX theme tokens for brand values and Tailwind utilities for responsive
   layout.

## Build the Mockup

1. Write readable `visual-source.html` with stable section delimiters.
2. Use ordinary HTML for static content.
3. Discover candidate islands, then resolve each selected island's current
   schema, lifecycle, native variants, required props, styling parts, and
   headless hooks.
4. Prefer a native variant and schema-supported `data-part` styling. Use
   headless mode only when the native variants cannot satisfy the approved
   design and all required hooks are implemented.
5. Author supported interactions as `<lx-island>` with schema-valid preview
   props and a readable `[data-lx-island-fallback]` child.
6. Dry-run `lexsis_pages` action `compile` on the complete visual source. Fix
   missing Tailwind candidates and all blocking compiler errors.
7. Save the compile response and run
   `scripts/build_visual_preview.py <compile-response.json>
   <page-workspace>/visual-preview.html`, passing the selected theme CSS and
   optional preview data files.
8. Save the returned style manifest in `design.compiledStyleManifest`.
9. Load the preview at 390px, 768px, and 1280px.

The preview shell loads Lexsis's exported island runtime without changing
normal browser behavior. Keep visual-stage props presentation-focused and do
not treat local add-to-cart, checkout, or navigation behavior as certified.
The preview may demonstrate selection, video, carousel, and other client
interactions; commerce behavior is tested on the hosted draft.

For an island that cannot compile or lacks safe preview data, use static
fallback HTML only for that island and record `previewMode: "fallback"` in the
manifest. State that the island remains a production blocker until its live
schema and production compile succeed. Never invent island names or props.

## Complex Islands

Shoppable video, galleries, before/after, and other active islands should use
the real island runtime whenever valid media and props exist. Follow lifecycle
replacement guidance when an interaction is deprecated; for example, use
supported native markup when the schema recommends it.
BuyBox and other commerce islands may render with preview data, but real
variant/cart behavior is tested later on the hosted draft.

## Approval

Show:

```text
Visual mockup: [path]
Store/theme: [names]
Sections: [ordered list]
Interactive previews: [islands]
Static fallbacks: [islands]
Temporary assets: [list]
```

Wait for visual approval. Update the source first, recompile, and regenerate
the preview after changes.

## Return

Return `visual_source_path`, `visual_preview_path`, the approved section list,
island preview modes, template evidence, MCP evidence, and `VISUAL_APPROVED`.
The next normal command is `/asset-prep`.

### visual-page reference: island-preview

# Island Preview

The browser runtime hydrates compiled `data-island` markers, not raw
`<lx-island>` authoring tags.

## Build

1. Resolve the live island schema.
2. Confirm active lifecycle status, required props, native variants, styling
   parts, and any headless hooks.
3. Prefer native mode and style only schema-listed parts.
4. Add readable `<lx-island>` source with preview props.
5. Include a direct `data-lx-island-fallback` child.
6. Dry-run compile the complete visual source.
7. Require no missing Tailwind candidates.
8. Save the compile response as JSON.
9. Run:

```bash
python3 skills/visual-page/scripts/build_visual_preview.py \
  compile-response.json \
  work/visual-pages/<page-handle>/visual-preview.html \
  --theme-css work/storefront/setup/stores/<store-id>/themes/<theme-id>.css
```

The builder uses the bundled shell, the exported Lexsis island runtime, and
the compiled section markup. Never hand-author `data-island` or `data-props`.

## Preview Data

Prefer real read-only product and media data. Use direct poster/video sources
and complete product objects when supported. If valid safe data is unavailable,
leave the fallback visible and record `previewMode: "fallback"`.

An island fallback is local to that island. It never authorizes replacing the
production island with custom controls.

ShoppableVideoFeed can run with real media while using a presentation mode
that does not navigate or write. Commerce and navigation islands should use
read-only props or fallback HTML.

## Preview Boundary

The shell does not add a content-security policy or replace browser network,
form, popup, or link behavior. Keep visual-stage props presentation-focused
and avoid configuring real checkout or external navigation actions.

Real product resolution, add-to-cart, cart totals, and checkout are verified
only on the hosted Lexsis draft.

### visual-page reference: visual-layout

# Visual Layout

The visual stage approves hierarchy, section proportions, image placement,
typography, color balance, desktop composition, mobile stacking, CTA
placement, and island presentation.

Write:

- `visual-source.html` — readable design-stage authoring source
- `visual-preview.html` — generated browser preview

Use ordinary HTML for static content and active Lexsis islands only for useful
interaction previews. A supporting composition image may guide art direction,
but it must never become the page.

Start from the selected page kit or section templates. Use the selected
theme's `--lx-*` tokens and Tailwind utilities rather than rebuilding the
brand system inside each section. Record one coherent style treatment in the
manifest.

Search existing store and product assets first. When media is still missing,
copy a bundled placeholder into the page workspace and record it as
`sourceType: "preview-placeholder"`.

Review at 390px, 768px, and 1280px. Show which islands use the runtime, which
use static fallbacks, and which assets remain temporary.

---

## Reference Knowledge

---

# Storefront Craft Guide — Start Here

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
| `animation-system` | CSS animations, scroll-reveal, headline effects | Adding motion to sections |
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
| `--lx-bg-surface` | Card/section background |
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
- Smooth scroll reveal on key sections
- Trust signals near purchase points
- Sticky add-to-cart on PDP

**Mediocre page:**
- Hardcoded colors instead of CSS vars
- Desktop-only layout
- Missing islands (raw HTML buttons instead of BuyBox)
- placeholder.co images shipped to production
- No animations or visual rhythm
- Trust badges missing

---

## Anti-Patterns (NEVER do these)

1. **No `fetch()` or XHR in section JS** — blocked by hydrator security
2. **No `eval()`, `localStorage`, `WebSocket`** — blocked
3. **No `@import` in section CSS** — blocked
4. **No external `url()` in CSS** — only inline gradients/colors
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

# Generation Protocol — How Pages Are Built

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
4. Require a valid page plan and verified assets, or record explicit skips
5. Author complete production source
6. lexsis_pages → compile
7. lexsis_page_create → create draft
8. Host-agent responsive and commerce verification
```

Setup provides slow-changing design context. Commerce, assets, schemas,
permissions, analytics, and remote versions are always read live.

> **Brand kit ↔ design.md precedence**: when the two disagree, **exact tokens (colors, fonts, radius, spacing values) come from the brand kit**; **style philosophy, component guidance, and explicit don'ts come from design.md**. Conflict on a token → use the kit's value, applied within design.md's don'ts. Don't stall trying to reconcile them.

> **Documentation precedence**: live MCP contracts win over bundled docs. For
> islands, use `vibe://schema/island/{name}` (or `lexsis_design` action
> `island_schema`) first, bundled
> `references/islands/{slug}/schema.json` second, and prose/layout examples
> last. Never merge prop shapes from different versions.

> **Authoring format**: write pages in the HTML-native **source format** (`source-format.md`) — plain HTML sections delimited by `<!-- section: id -->`, islands as `<lx-island name>` with a JSON `<script>` child. The compiler produces VibePage JSON and does all escaping.

> **Local source**: follow `source-artifact-workflow.md`.
> `lexsis-source.html` is the canonical editable production artifact.
> `visual-source.html` is separately dry-run compiled into an interactive local
> preview and may contain temporary design-stage values.

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
- Mobile-first responsive; shared keyframes or `data-behavior="gsap-*"` presets for animation
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
- **Shared keyframes** already loaded: fadeUp, fadeIn, scaleIn, slideInLeft, slideInRight, marquee, float, shimmer, wordFade, pulseRing. GSAP presets via `data-behavior="gsap-reveal|gsap-parallax|gsap-pin|gsap-marquee-scroll"`
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
| `--lx-surface-alt` | #f9fafb | Alternating section bg |
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

> **This is the preferred way to author pages.** Write plain HTML with
> `<lx-island>` elements; `lexsis_pages` action `compile` and
> `lexsis_page_create` action `create` compile it deterministically. Never
> hand-write `data-island` / `data-props` or escape HTML into JSON strings.

For durable page work, store this format in `lexsis-source.html` and follow
`source-artifact-workflow.md`. The visual workflow uses the same readable
authoring syntax in `visual-source.html`, dry-run compiles it, and hydrates the
compiled result through the exported island preview runtime.

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
  .hero-glow { box-shadow: 0 0 40px var(--lx-accent-color); }
</style>

<script>
  /* becomes section.js — sandboxed; `section` is bound to this section's element */
  section.querySelectorAll('.hero-glow').forEach(el => el.classList.add('ready'));
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
6. **`head`, `theme_css`, `scripts`** are structured tool arguments. Prefer
   `theme_css` from `lexsis_brand` action `lexsis_brand.get_theme`.
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
<!-- ❌ hand-written island markers (old format — compiler rejects raw usage in source) -->
<div data-island="FAQ" data-props='{"items":[...]}'></div>

<!-- ❌ escaped HTML — never escape anything -->
&lt;section&gt;...&lt;/section&gt;

<!-- ❌ external scripts in section HTML — use the scripts param -->
<script src="https://cdn.example.com/lib.js"></script>
```

---

# Storefront Workflow

Use one owning command at a time.

## Normal Page Journey

```text
/setup
  → /plan-page
  → /visual-page
  → /asset-prep
  → /generate
  → /publish
```

- Setup is normally run once and refreshed only for changed stores/themes.
- Plan defines the campaign and page strategy.
- Visual creates the responsive mockup and interactive island preview.
- Asset prep replaces all temporary media.
- Generate owns production source, draft creation, and hosted QA.
- Publish is a separate explicit release.

Commands do not silently invoke one another. When a user intentionally starts
later, create the minimum missing artifact and record the skipped command.

## Optional Routes

- Use `/analyze-page` before planning when a URL, screenshot, or ad matters.
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

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

> When to load: ALWAYS. Read before generating any ecommerce page.

## The Conversion Stack (AIDA → Sections)

Map the AIDA framework to section order. Each stage requires specific psychology and placement.

### Short Page (5-7 sections) — Impulse / Low-consideration products

1. **Attention (1 section)**: Hero section
   - High-contrast gradient or bold product image
   - Benefit-driven headline (6-10 words)
   - `font-size: clamp(2.5rem, 5vw, 3.5rem)` for headline
   - Sticky CTA bar for persistent action

2. **Interest (2 sections)**: Value props + social proof stats
   - 3 icon-driven benefits max
   - Numbers: customer count, star rating, review count
   - `py-8 md:py-12` spacing

3. **Desire (2 sections)**: Reviews + transformation proof
   - Star-first review display, 3-6 reviews
   - Before/after images or testimonial carousel
   - `data-island="ReviewCarousel"` for dynamic trust

4. **Action (2 sections)**: CTA + footer
   - Urgency element (countdown or inventory indicator)
   - First-person CTA copy: "Get MY [benefit]"
   - `data-island="CountdownTimer"` or `data-island="InventoryIndicator"`

### Medium Page (8-12 sections) — Considered purchase / New-to-brand

1. **Attention (1)**: Hero with video or interactive media
2. **Interest (3)**: Value props → logo carousel → stats
   - Logo carousel = trust transfer from known brands
   - Neutral background between hero and body
3. **Desire (5)**: Feature grid → testimonials → before/after → reviews → comparison table
   - 3-6 features with icons
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
- 1-2 trust badges (free shipping, guarantee)

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
      <span class="text-lg line-through opacity-40">$129.00</span>
      <span class="text-xs font-semibold px-2 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">31% OFF</span>
    </div>
    <div class="flex items-center gap-2">
      <div class="flex">
        <span class="text-yellow-400">★★★★★</span>
      </div>
      <span class="text-sm opacity-70">(2,847 reviews)</span>
    </div>
    <div data-island="BuyBox" data-props='{"productId":"gid://shopify/Product/123","ctaText":"Add to Cart — Free Shipping","showQuantity":true}'></div>
    <div class="flex gap-4 pt-4">
      <div class="flex items-center gap-2">
        <span class="text-2xl">🚚</span>
        <span class="text-sm">Free Shipping</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="text-2xl">💯</span>
        <span class="text-sm">Money-Back Guarantee</span>
      </div>
    </div>
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
<section class="relative min-h-screen flex items-center justify-center text-center px-4 py-20" style="background:linear-gradient(135deg, #667eea 0%, #764ba2 100%)">
  <div class="max-w-4xl mx-auto space-y-8">
    <h1 class="text-5xl md:text-7xl font-extrabold leading-none text-white">
      Get Flawless Skin in 30 Days
    </h1>
    <p class="text-xl md:text-2xl text-white/90">
      Without harsh chemicals or expensive treatments. Guaranteed.
    </p>
    <button class="px-10 py-5 text-xl font-bold rounded-lg transition-transform hover:scale-105" style="background:white;color:var(--lx-accent-color)">
      Start MY Transformation
    </button>
    <p class="text-white/80 text-sm">Join 47,000+ customers who transformed their skin</p>
  </div>
  <div data-island="CountdownTimer" data-props='{"endDate":"2026-06-30T23:59:59Z","message":"Offer ends in:","urgencyThreshold":3600}'></div>
  <div data-island="SocialProofPopup" data-props='{"displayDuration":5000,"interval":15000,"maxPopups":3}'></div>
</section>
```

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

Show original price crossed out. Minimum 20% discount to be credible, optimal 30-40%.

```html
<div class="flex items-baseline gap-3">
  <span class="text-3xl font-bold" style="color:var(--lx-text-color)">$79.99</span>
  <span class="text-lg line-through opacity-40">$119.99</span>
  <span class="text-xs font-semibold px-2 py-1 rounded-full" style="background:var(--lx-accent-color);color:white">33% OFF</span>
</div>
<p class="text-sm mt-2 opacity-70">Save $40 today</p>
```

### Charm Pricing

End prices in .97, .95, or .99. Never .00 for mid-market ($50-$300). Use .00 only for premium ($500+).

**Examples:**
- Low-ticket (<$50): $29.97, $14.99
- Mid-ticket ($50-$300): $129.95, $79.97
- High-ticket ($300+): $999.00, $1,500.00

### Bundle Pricing (quantity breaks)

Show per-unit savings, not just total discount.

```html
<div class="grid md:grid-cols-3 gap-4">
  <div class="p-6 border rounded-lg" style="border-color:var(--lx-border-color)">
    <div class="text-center space-y-2">
      <p class="text-sm uppercase tracking-wide opacity-60">Buy 1</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$59.99</p>
      <p class="text-sm opacity-70">$59.99 each</p>
      <button class="w-full px-4 py-2 mt-4 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
  <div class="p-6 border-2 rounded-lg relative transform scale-105" style="border-color:var(--lx-accent-color);box-shadow:0 20px 60px rgba(102,126,234,0.2)">
    <span class="absolute -top-3 left-1/2 -translate-x-1/2 px-3 py-1 text-xs font-semibold rounded-full text-white" style="background:var(--lx-accent-color)">BEST VALUE</span>
    <div class="text-center space-y-2">
      <p class="text-sm uppercase tracking-wide opacity-60">Buy 3</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$119.99</p>
      <p class="text-sm opacity-70">$40.00 each — Save $60</p>
      <button class="w-full px-4 py-3 mt-4 rounded font-bold text-white" style="background:var(--lx-accent-color)">
        Select
      </button>
    </div>
  </div>
  <div class="p-6 border rounded-lg" style="border-color:var(--lx-border-color)">
    <div class="text-center space-y-2">
      <p class="text-sm uppercase tracking-wide opacity-60">Buy 2</p>
      <p class="text-3xl font-bold" style="color:var(--lx-text-color)">$99.99</p>
      <p class="text-sm opacity-70">$50.00 each — Save $20</p>
      <button class="w-full px-4 py-2 mt-4 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
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
<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto">
  <div class="p-8 rounded-lg" style="border:1px solid var(--lx-border-color)">
    <h3 class="text-2xl font-bold mb-2">Basic</h3>
    <p class="text-4xl font-bold mb-4" style="color:var(--lx-text-color)">$49.99</p>
    <ul class="space-y-3 mb-6">
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature A</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature B</span>
      </li>
    </ul>
    <button class="w-full px-6 py-3 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
      Get Started
    </button>
  </div>
  <div class="p-8 rounded-lg relative transform scale-105" style="border:3px solid var(--lx-accent-color);box-shadow:0 20px 60px rgba(0,0,0,0.2)">
    <span class="absolute -top-4 left-1/2 -translate-x-1/2 px-4 py-1 text-sm font-semibold rounded-full text-white" style="background:var(--lx-accent-color)">MOST POPULAR</span>
    <h3 class="text-2xl font-bold mb-2">Pro</h3>
    <div class="flex items-baseline gap-2 mb-4">
      <p class="text-4xl font-bold" style="color:var(--lx-text-color)">$89.99</p>
      <p class="text-lg line-through opacity-40">$129.99</p>
    </div>
    <ul class="space-y-3 mb-6">
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature A</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature B</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature C</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature D</span>
      </li>
    </ul>
    <button class="w-full px-6 py-3 rounded font-bold text-white" style="background:var(--lx-accent-color)">
      Start Pro Trial
    </button>
  </div>
  <div class="p-8 rounded-lg" style="border:1px solid var(--lx-border-color)">
    <h3 class="text-2xl font-bold mb-2">Premium</h3>
    <p class="text-4xl font-bold mb-4" style="color:var(--lx-text-color)">$149.99</p>
    <ul class="space-y-3 mb-6">
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Everything in Pro</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature E</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Feature F</span>
      </li>
      <li class="flex items-center gap-2">
        <span style="color:var(--lx-accent-color)">✓</span>
        <span>Priority Support</span>
      </li>
    </ul>
    <button class="w-full px-6 py-3 rounded" style="border:2px solid var(--lx-accent-color);color:var(--lx-accent-color)">
      Go Premium
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
<section class="py-16 px-4" style="background:var(--lx-bg-surface)">
  <div class="grid grid-cols-2 md:grid-cols-4 gap-8 max-w-6xl mx-auto text-center">
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">247,000+</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">Happy Customers</p>
    </div>
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">4.8/5.0</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">Average Rating</p>
    </div>
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">12,000+</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">5-Star Reviews</p>
    </div>
    <div>
      <p class="text-5xl md:text-6xl font-extrabold" style="color:var(--lx-accent-color)">94%</p>
      <p class="text-sm uppercase tracking-wide mt-2 opacity-70">Would Recommend</p>
    </div>
  </div>
</section>
```

**When to use:** First 3 sections. Anchor trust before storytelling.

### 2. Faces (testimonial cards)

Photos + quotes. Most effective for emotional products (beauty, wellness, lifestyle).

```html
<section class="py-16 px-4">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-3xl md:text-4xl font-bold text-center mb-12" style="color:var(--lx-text-color)">What Our Customers Say</h2>
    <div class="grid md:grid-cols-3 gap-8">
      <div class="p-6 rounded-lg" style="background:var(--lx-bg-surface)">
        <div class="flex items-center gap-4 mb-4">
          <img src="/testimonials/sarah.jpg" alt="Sarah M." class="w-20 h-20 rounded-full" style="border:4px solid var(--lx-accent-color)" />
          <div>
            <p class="font-bold">Sarah M.</p>
            <p class="text-sm opacity-70">Verified Buyer</p>
            <div class="flex text-yellow-400">★★★★★</div>
          </div>
        </div>
        <p class="text-lg italic leading-relaxed opacity-90">
          "This completely changed how I approach skincare. I saw results in just 2 weeks."
        </p>
      </div>
      <!-- Repeat for more testimonials -->
    </div>
  </div>
</section>
```

**When to use:** After interest stage, before feature deep-dive. 3-6 testimonials max per section.

### 3. Logos (logo carousel)

Trust transfer from known brands. Works for B2B, press mentions, "as seen on".

```html
<section class="py-12 px-4" style="background:var(--lx-bg-surface)">
  <div class="max-w-6xl mx-auto">
    <p class="text-center text-sm uppercase tracking-wide mb-8 opacity-70">Trusted by Leading Brands</p>
    <div class="flex justify-center items-center gap-12 flex-wrap">
      <img src="/logos/forbes.svg" alt="Forbes" class="h-10 opacity-60 hover:opacity-100 transition-opacity grayscale hover:grayscale-0" />
      <img src="/logos/techcrunch.svg" alt="TechCrunch" class="h-10 opacity-60 hover:opacity-100 transition-opacity grayscale hover:grayscale-0" />
      <img src="/logos/wsj.svg" alt="Wall Street Journal" class="h-10 opacity-60 hover:opacity-100 transition-opacity grayscale hover:grayscale-0" />
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
<div class="inline-flex items-center gap-2 px-4 py-2 rounded" style="background:#fff3cd;color:#856404">
  <span class="font-semibold">⚠️ Only 7 left in stock</span>
</div>
<div data-island="InventoryIndicator" data-props='{"threshold":10,"lowStockMessage":"Only {count} left in stock","outOfStockMessage":"Sold out — join waitlist"}'></div>
```

**When to use:** High-demand products, limited editions, seasonal items.

### 2. Deadline (Countdown)

Time-limited offers. Must have real expiration.

```html
<div class="sticky top-0 z-50 py-3 px-4 text-center text-white font-semibold text-sm" style="background:#c9302c">
  🔥 Summer Sale: 30% Off Ends in
  <div data-island="CountdownTimer" data-props='{"endDate":"2026-06-30T23:59:59Z","message":"","urgencyThreshold":3600}'></div>
  <a href="#shop" class="ml-4 underline">Shop Now</a>
</div>
```

**When to use:** Flash sales, product launches, abandoned cart recovery.

### 3. Exclusivity (Limited Access)

Member-only, waitlist, invite-only framing.

```html
<section class="py-20 px-4 text-center" style="background:var(--lx-bg-surface)">
  <div class="max-w-2xl mx-auto space-y-6">
    <h2 class="text-4xl font-bold" style="color:var(--lx-text-color)">Join the Waitlist</h2>
    <p class="text-lg opacity-80">Limited to 500 founding members. Next batch ships August 2026.</p>
    <div class="inline-block px-4 py-2 rounded-full text-sm font-semibold" style="background:#f0f0f0">
      127 spots remaining
    </div>
    <div data-island="EmailCapture" data-props='{"placeholder":"Enter your email","buttonText":"Reserve Your Spot"}'></div>
  </div>
</section>
```

**When to use:** Pre-launch, beta access, VIP tiers.

### Anti-Patterns (Fake Urgency)

| ❌ Don't | Why | ✅ Do |
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
<section class="py-16 px-4">
  <div class="grid md:grid-cols-3 gap-8 max-w-5xl mx-auto">
    <div class="text-center space-y-4">
      <span class="text-5xl">⚡</span>
      <h3 class="text-xl font-bold">Fast Results</h3>
      <p class="opacity-80">See improvements in 7 days or less</p>
    </div>
    <div class="text-center space-y-4">
      <span class="text-5xl">🛡️</span>
      <h3 class="text-xl font-bold">Risk-Free</h3>
      <p class="opacity-80">60-day money-back guarantee</p>
    </div>
    <div class="text-center space-y-4">
      <span class="text-5xl">❤️</span>
      <h3 class="text-xl font-bold">Love It</h3>
      <p class="opacity-80">Join 47,000+ happy customers</p>
    </div>
  </div>
</section>
```

**If you have 6+ features:** Split into 2 sections (benefits vs. technical specs).

### CompareTable (3 columns max, 5-8 rows)

```html
<div data-island="CompareTable" data-props='{"columns":[{"name":"Competitor A","highlight":false},{"name":"You","highlight":true},{"name":"Competitor B","highlight":false}],"rows":[{"feature":"Feature 1","values":["❌","✅","❌"]},{"feature":"Feature 2","values":["✅","✅","❌"]},{"feature":"Feature 3","values":["❌","✅","✅"]}]}'></div>
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

### First-Person Labels

**Bad (second-person):**
- "Get Started"
- "Buy Now"
- "Download the Guide"

**Good (first-person):**
- "Start MY Free Trial"
- "Add to MY Cart"
- "Send ME the Guide"

**Why it works:** First-person creates ownership before purchase.

```html
<button class="px-8 py-4 text-lg font-bold rounded-lg" style="background:var(--lx-accent-color);color:white">
  Start MY Transformation
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
<button class="px-8 py-4 text-lg font-bold rounded-lg shadow-lg transition-transform hover:scale-105" style="background:var(--lx-accent-color);color:white;box-shadow:0 4px 12px rgba(102,126,234,0.4)">
  Add to Cart
</button>
```

**Color pairs (high contrast):**
- Blue CTA on white: `#667eea` / `#ffffff`
- Red CTA on dark: `#c9302c` / `#1a1a1a`
- Green CTA on light: `#28a745` / `#f9fafb`

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
<button class="px-10 py-5 text-xl font-bold rounded-lg shadow-2xl transition-transform hover:scale-105" style="background:var(--lx-accent-color);color:white;box-shadow:0 8px 24px rgba(102,126,234,0.5)">
  Get Started
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

| ❌ | Why | ✅ |
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
    "fonts": ["https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap"]
  },
  "theme_css": ":root { --lx-accent-color: #667eea; --lx-text-color: #1a1a1a; --lx-bg-color: #ffffff; --lx-bg-surface: #f9fafb; }",
  "sections": [
    {
      "id": "hero",
      "html": "<section class='py-20 px-4 text-center' style='background:linear-gradient(135deg, #667eea 0%, #764ba2 100%)'><div class='max-w-3xl mx-auto space-y-6'><h1 class='text-5xl md:text-6xl font-extrabold text-white'>Get the Flawless Skin Guide</h1><p class='text-xl text-white/90'>Learn how to achieve radiant skin in 30 days. Free download.</p><div data-island='EmailCapture' data-props='{\"placeholder\":\"Enter your email\",\"buttonText\":\"Send Me the Guide\"}'></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "value-props",
      "html": "<section class='py-16 px-4'><div class='grid md:grid-cols-3 gap-8 max-w-5xl mx-auto'><div class='text-center space-y-4'><span class='text-5xl'>✓</span><h3 class='text-xl font-bold'>Science-Backed Methods</h3><p class='opacity-80'>Proven techniques from dermatologists</p></div><div class='text-center space-y-4'><span class='text-5xl'>✓</span><h3 class='text-xl font-bold'>Natural Ingredients</h3><p class='opacity-80'>No harsh chemicals or side effects</p></div><div class='text-center space-y-4'><span class='text-5xl'>✓</span><h3 class='text-xl font-bold'>30-Day Results</h3><p class='opacity-80'>See visible improvements in one month</p></div></div></section>",
      "css": "",
      "js": ""
    },
    {
      "id": "stats",
      "html": "<section class='py-12 px-4' style='background:var(--lx-bg-surface)'><div class='grid grid-cols-2 gap-8 max-w-4xl mx-auto text-center'><div><p class='text-5xl font-extrabold' style='color:var(--lx-accent-color)'>47,000+</p><p class='text-sm uppercase mt-2 opacity-70'>Downloads</p></div><div><p class='text-5xl font-extrabold' style='color:var(--lx-accent-color)'>4.9/5</p><p class='text-sm uppercase mt-2 opacity-70'>Rating</p></div></div></section>",
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
      "html": "<section class='grid md:grid-cols-2 gap-8 max-w-7xl mx-auto px-4 py-8'><div><img src='/product.jpg' class='w-full rounded-lg'/></div><div class='flex flex-col justify-center space-y-6'><h1 class='text-5xl font-bold' style='color:var(--lx-text-color)'>Premium Serum</h1><p class='text-xl opacity-80'>Transform your skin in 30 days</p><div class='flex items-baseline gap-3'><span class='text-3xl font-bold' style='color:var(--lx-text-color)'>$79.99</span><span class='text-lg line-through opacity-40'>$119.99</span><span class='text-xs font-semibold px-2 py-1 rounded-full text-white' style='background:var(--lx-accent-color)'>33% OFF</span></div><div data-island='BuyBox' data-props='{\"productId\":\"gid://shopify/Product/123\",\"ctaText\":\"Add to Cart — Free Shipping\"}'></div></div></section>",
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
      "html": "<section class='py-12 px-4' style='background:var(--lx-bg-surface)'><p class='text-center text-sm uppercase tracking-wide mb-8 opacity-70'>Trusted by Industry Leaders</p><div class='flex justify-center gap-12 flex-wrap'><img src='/logos/company1.svg' class='h-10 opacity-60'/><img src='/logos/company2.svg' class='h-10 opacity-60'/><img src='/logos/company3.svg' class='h-10 opacity-60'/></div></section>",
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
      <button data-lx-header="announcement-dismiss" class="absolute right-3 top-1/2 -translate-y-1/2">✕</button>
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
[data-part="cta"]:hover { transform: translate(-2px, -2px); box-shadow: 6px 6px 0 var(--lx-text-color); }
[data-part="variant-btn"] { border-radius: 0; border: 2px solid var(--lx-text-color); font-weight: 700; }
[data-part="item"] { border: 2px solid var(--lx-text-color); border-radius: 0; box-shadow: 4px 4px 0 var(--lx-border-color); }
[data-part="badge"] { border-radius: 0; border: 2px solid var(--lx-text-color); font-weight: 800; }
```

## playful

```css
[data-part="cta"] { border-radius: 1.25rem; font-weight: 800; padding: 1.1rem 2.5rem; transition: transform 150ms ease; }
[data-part="cta"]:hover { transform: scale(1.04) rotate(-1deg); }
[data-part="variant-btn"] { border-radius: 1rem; border-width: 2px; font-weight: 700; }
[data-part="item"] { border-radius: 1.5rem; border: 2px solid var(--lx-border-color); }
[data-part="badge"] { border-radius: 9999px; font-weight: 800; }
```

## minimal

```css
[data-part="cta"] { border-radius: 0.375rem; box-shadow: none; font-weight: 500; }
[data-part="variant-btn"] { border-radius: 0.375rem; border-color: var(--lx-border-color); font-weight: 400; }
[data-part="item"] { border: none; border-radius: 0.5rem; background: var(--lx-surface-alt); box-shadow: none; }
[data-part="badge"] { border-radius: 0.25rem; font-weight: 500; }
[data-part="trust-badges"] { filter: grayscale(1); opacity: 0.6; }
```

## Rules

1. One pack per page — mixing packs is the #1 way to make a page look broken.
2. Scope to a section if two islands need different treatments: `#hero [data-part="cta"] { ... }`.
3. Packs compose with `lexsis_brand.compile_theme` output — they reference `--lx-*` variables, never hardcode colors.
4. Check the island's `schema.json` `parts` array before targeting a part name (`lexsis_design.island_schema`).

---

# Asset Pipeline — Multi-Source Visual Strategy

> **Compiled runtime reference:** any `data-island` or `data-props` snippets below are renderer output, not page source. For new pages, use `<lx-island>` with a JSON script child as defined in `source-format.md`, then call `lexsis_pages` with action `compile`.

> **Inputs:** Approved page plan (from `/plan-page` workflow)
> **Outputs:** Asset manifest (URLs + purposes + section mapping)
> **When to load:** After page plan is approved, before HTML generation.

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

| Page Type | Hero (high) | Section BGs (medium) | Lifestyle (medium) | Video | Total assets |
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

## Asset Manifest (Output Format)

After sourcing, update `page-manifest.json` and return:

```json
{
  "role": "hero",
  "sectionId": "hero",
  "sourceType": "lexsis",
  "assetId": "asset-uuid",
  "url": "https://cdn.trylexsis.com/assets/abc123.jpg",
  "width": 1600,
  "height": 1200,
  "desktopCrop": "center",
  "mobileCrop": "center top",
  "altTextIntent": "Product pouch beside a glass",
  "verificationStatus": "verified"
}
```

Shopify catalog media uses `sourceType: "shopify"` with `productId` and
`mediaId` instead of `assetId`. Never require a Lexsis asset ID for a Shopify
image.

Asset names alone do not establish identity. Visually inspect product, creator,
and endorsement imagery. Generation uses only permanent verified URLs.

---

## Cost Control

1. `lexsis_asset_library` action `search` first
2. `lexsis_workspace` action `credits` before expensive operations
3. Prefer `quality: "medium"` — reserve `"high"` for hero only
4. External MCP assets → `lexsis_asset_upload` action `import`
5. CSS gradients/solid colors for sections that don't need imagery
6. Reuse: one hero image can serve as dimmed background for 2-3 sections

---

# Before Showing Draft to Merchant — QA Recipe

## Pre-flight Checklist

1. **Validate local artifacts** — run the shared page workspace validator
2. **Compile complete source** — `lexsis_pages` action `compile`
3. **Save as draft** — `lexsis_page_create` action `create` with `publish:false`
4. **Record page ID/version/hashes** — update `page-manifest.json`
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
- [ ] Production composition still matches `visual-preview.html`
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
5. Record page ID, version, preview URL, and synchronized source hashes
6. `lexsis_pages` action `integrity`
7. Host-agent browser and commerce QA at 390px, 768px, and 1280px
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
- Require local source hash and remote version to match the manifest baseline

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

Use these files to pass work between the public storefront commands without
requiring one command to invoke another.

## Setup Context

`/setup` creates:

```text
work/storefront/setup/
├── setup.json
└── stores/
    └── <store-id>/
        ├── brand-design.md
        └── themes/
            └── <theme-id>.css
```

A page binds exactly one saved store and theme. Several themes may be saved,
but a page must not mix their design files.

Setup is reused for slow-changing design context. Products, prices, variants,
assets, island schemas, permissions, analytics, and page versions remain live
reads.

## Page Workspace

```text
work/visual-pages/<page-handle>/
├── page-plan.md
├── page-manifest.json
├── visual-source.html
├── visual-preview.html
├── lexsis-source.html
├── qa-report.md
└── assets/
```

- `page-plan.md` is the approved strategy and section blueprint.
- `visual-source.html` is readable design-stage HTML and may use preview data.
- `visual-preview.html` is generated from a dry-run compile and the Lexsis
  island preview shell.
- `lexsis-source.html` is the canonical editable production source.
- `qa-report.md` records draft and interaction verification.

Visual files are optional only when the user explicitly skips `/visual-page`.
Production source is never optional once a draft exists.

## Manifest

Use `schemaVersion: 1`:

```json
{
  "schemaVersion": 1,
  "status": "planned",
  "workflow": {
    "skippedSkills": []
  },
  "mcp": {
    "status": "connected",
    "checkedAt": "2026-09-04T12:00:00Z",
    "surfaceVersion": "3.0",
    "capabilities": [
      {
        "router": "lexsis_pages",
        "actions": ["compile"]
      }
    ]
  },
  "page": {
    "title": "SuperYou Pro Creatine",
    "handle": "superyou-pro-creatine",
    "archetype": "landing"
  },
  "workspaceId": "...",
  "storeId": "...",
  "themeId": "...",
  "template": {
    "mode": "page-kit",
    "pageKitId": "kit-slug",
    "sectionTemplateIds": ["hero-slug", "buy-box-slug"],
    "evaluatedTemplates": [],
    "selectionReason": "Matches the approved PDP structure",
    "selectedAt": "2026-09-04T12:00:00Z"
  },
  "design": {
    "themeId": "...",
    "themeSource": "saved-and-verified",
    "stylePack": "editorial",
    "compiledStyleManifest": null
  },
  "setupPath": "work/storefront/setup/setup.json",
  "brandDesignPath": "work/storefront/setup/stores/<store-id>/brand-design.md",
  "themeCssPath": "work/storefront/setup/stores/<store-id>/themes/<theme-id>.css",
  "pageConfig": {
    "head": {},
    "themeCss": "",
    "scripts": []
  },
  "productBindings": [],
  "assets": [],
  "sections": ["announcement", "hero", "benefits", "faq"],
  "islands": [
    {
      "sectionId": "hero",
      "name": "BuyBox",
      "schema": {
        "version": "5.0.0",
        "lifecycleStatus": "active",
        "resolvedAt": "2026-09-04T12:00:00Z"
      },
      "productionMode": "native",
      "previewMode": "hydrated",
      "previewData": true
    }
  ],
  "visual": {
    "status": "pending",
    "sourcePath": "visual-source.html",
    "previewPath": "visual-preview.html"
  },
  "sourceSync": {
    "lastCompiledBundleHash": null,
    "lastSyncedBundleHash": null,
    "lastSyncedSectionHashes": {},
    "lastChangedSections": []
  },
  "qa": {
    "status": "pending",
    "checkedVersion": null,
    "checkedBundleHash": null,
    "responsive": false,
    "commerce": false,
    "copy": false,
    "claims": false,
    "assets": false,
    "integrity": false
  },
  "remote": {
    "pageId": null,
    "lastKnownVersion": null,
    "previewUrl": null
  }
}
```

`previewMode` is `hydrated` when the real exported island runs locally and
`fallback` when the mockup shows static fallback HTML.

`template.mode` is `page-kit`, `sections`, or `custom`. A custom composition
records evaluated templates and why they were rejected. The current template
API does not guarantee a version field, so preserve selected IDs rather than
inventing one.

After a successful production compile, save the compiler's returned
`style_manifest` under `design.compiledStyleManifest`.

## Skill Skips

Commands are independently invokable and never run another command
automatically.

- Skipping planning requires a short replacement `page-plan.md`.
- Skipping visual design sets `visual.status: "skipped"`.
- Skipping asset preparation requires `/generate` to create the same verified
  asset records.

Record each explicit skip in `workflow.skippedSkills`.

## Source Rules

Both visual and production source use stable boundaries:

```html
<!-- section: hero -->
<section id="hero">
  ...
</section>
```

Section delimiters and IDs match, IDs are unique, JSON is valid, and source is
normally formatted.

Visual source may use preview copy, bundled assets, and schema-valid island
preview data. Production source may not contain any preview placeholder,
temporary URL, local path, unsupported script, internal note, or unverified
asset.

## Synchronization

The production bundle hash covers `lexsis-source.html` plus page head, theme
CSS, and scripts.

For creation:

1. Validate local files.
2. Compile the complete source without saving.
3. Create the draft with `publish: false`.
4. Save page ID, version, preview URL, bundle hash, and section hashes.

For editing:

1. Fetch the current remote version.
2. Stop when it differs from `remote.lastKnownVersion`.
3. Change local source first.
4. Validate and compile the complete source.
5. Compare section hashes.
6. Patch only changed sections with `expected_version`.
7. Update the manifest only after a successful write.

Remote content must never be the only copy of an intentional change.

## QA Report

```markdown
# QA Report

- MCP status: connected/blocked
- MCP surface version: <version>
- Capabilities used: <routers/actions>
- Lexsis actions called: <ordered summary>
- Template: <kit/sections/custom reason>
- Live bindings: <products/assets>
- Fallbacks: none or list
- Compilation: pass/fail
- Source bundle: <hash>
- Remote version: <version>
- Desktop 1280px: pass/fail
- Tablet 768px: pass/fail
- Mobile 390px: pass/fail
- Commerce: pass/fail
- Copy: pass/fail
- Claims: pass/fail
- Assets: pass/fail
- Integrity: pass/fail
- Blockers: none or list
- Publish readiness: ready/not ready
```

Publishing requires matching local and remote versions, current passing QA,
the required entitlement, and explicit approval.

---

# Interactive Island Preview

Use this only for `/visual-page`.

## Why Compilation Is Required

The browser runtime hydrates compiled `data-island` markers; it does not
hydrate raw `<lx-island>` authoring tags. Keep authoring readable, then call
`lexsis_pages` action `compile` without saving.

Compiled runtime reference:

```html
<div data-island="ShoppableVideoFeed" data-props="..."></div>
```

Do not author that runtime markup by hand. Use the compiler output so prop
escaping remains correct.

## Build the Preview

1. Resolve the island's live schema.
2. Add `<lx-island>` to `visual-source.html`.
3. Include a static direct child marked `data-lx-island-fallback`.
4. Compile the full visual source.
5. Save the compile response as JSON.
6. Run `visual-page/scripts/build_visual_preview.py` to fill the reusable shell
   with:
   - selected theme CSS
   - compiled section wrappers and section CSS
   - the compiled section array
   - optional test cart data, commerce config, and product binding
7. Save the result as `visual-preview.html`.

The shell loads:

```text
https://storefront.trylexsis.com/islands/storefront.css
https://storefront.trylexsis.com/islands/islands.js
```

Then it calls `window.LexsisIslands.hydrateIslands(...)`.

## Preview Data

- Prefer real read-only product and media data.
- Preview copy may be temporary.
- Use direct media URLs and full product objects when supported.
- Never invent unsupported props.
- If valid data is unavailable, leave the fallback visible and record
  `previewMode: "fallback"`.

ShoppableVideoFeed can use the real island with direct poster/video sources.
Use an action mode that does not claim a successful cart write during visual
approval.

## Preview Boundary

The shell does not add a content-security policy or override normal browser
network, form, popup, or link behavior. It is a design preview, not a Shopify
storefront.

Do not configure preview islands with checkout, external navigation, or other
write-oriented actions. Use presentation-focused modes or static fallback HTML
when an island cannot provide a useful visual preview without live commerce.

Selection, playback, galleries, accordions, and other client behavior can be
reviewed locally. Real product resolution, add-to-cart, cart totals, checkout,
and store-origin behavior must be verified on the Lexsis-hosted draft created
by `/generate`.

---

# Visual Layout Workflow

`/visual-page` turns an approved plan into a browser-reviewable mockup. It does
not create the production draft.

## Design Decisions

The visual stage approves:

- hierarchy and section proportions
- image placement and crop direction
- typography and color balance
- desktop composition and mobile stacking
- CTA placement
- island choice and presentation

Use placeholder copy where final copy is not approved. A composition image may
support art direction, but it must never become the page itself.

## Files

Write:

- `visual-source.html` — readable authoring source
- `visual-preview.html` — compiled local browser preview

Static content stays ordinary HTML. Supported interactions use
schema-validated `<lx-island>` source and a static
`data-lx-island-fallback` child. Read `island-preview.md` for the runtime
contract.

Use existing store and product assets first. Copy bundled placeholders into
the page's `assets/` directory only when an image is still missing. Record each
one as `sourceType: "preview-placeholder"` so `/asset-prep` can replace it.

## Approval Gate

Review at 390px, 768px, and 1280px. Show which islands are hydrated, which use
fallback HTML, and which assets are temporary.

After approval, preserve the composition. `/asset-prep` replaces temporary
media, and `/generate` converts preview bindings into production bindings.

---

# Public Storefront Workflow

The customer-facing pack has ten commands. Six form the normal page journey:

```text
/setup
  → /plan-page
  → /visual-page
  → /asset-prep
  → /generate
  → /publish
```

| Command | Owns | Main output |
|---|---|---|
| `setup` | Saved store and theme design context | `setup.json` and design files |
| `plan-page` | Campaign and page strategy | approved `page-plan.md` |
| `visual-page` | Responsive mockup and island preview | visual source and preview |
| `asset-prep` | Final verified media | asset manifest |
| `generate` | Production source, draft, and hosted QA | `DRAFT_READY` |
| `publish` | Explicit live release | published version |

Four optional commands support the workflow:

| Command | Owns |
|---|---|
| `analyze-page` | URL, screenshot, ad, or own-page analysis |
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

## Required Preflight

Before reading live Lexsis data or creating, reading, or changing standard
page artifacts:

1. Confirm that the `lexsis-ai` MCP server exposes `lexsis_discover`.
2. Call `lexsis_discover` for each router/action needed by the current skill.
   Use the returned schema as authoritative; never guess arguments from memory.
3. Record the successful discovery in `page-manifest.json` when a page
   workspace exists.
4. Use live Lexsis reads for changing data such as products, variants, prices,
   availability, assets, island schemas, permissions, analytics, and remote
   versions.

Discover only the capabilities required for the current task. Do not load the
entire action catalogue when a small targeted query is enough.

## Failure Policy

### MCP unavailable

If `lexsis_discover` is absent, fails, or cannot return the required action
schemas:

- stop with `BLOCKED_LEXSIS_MCP`
- name the unavailable capabilities
- do not create or modify standard page artifacts
- do not present static HTML, cached catalogue data, or custom commerce
  controls as an equivalent Lexsis result

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

## Manifest Evidence

Record the latest successful preflight:

```json
{
  "mcp": {
    "status": "connected",
    "checkedAt": "2026-09-04T12:00:00Z",
    "surfaceVersion": "3.0",
    "capabilities": [
      {
        "router": "lexsis_template_library",
        "actions": ["search_page_kits", "search_sections"]
      }
    ]
  }
}
```

Store capability names, not full schemas or credentials. Update this record
when another skill performs a new preflight.

## Result Evidence

Every Lexsis-dependent result reports:

- MCP connection status
- discovered capabilities used
- Lexsis router actions called
- selected template or reason for custom composition
- live product and asset bindings used
- fallbacks used
- blocking limitations

`setup` has no page manifest, so it returns this evidence directly with its
saved setup paths.

---

# Lexsis Page Design Capabilities

Use this contract when planning, visualizing, preparing assets, generating, or
structurally optimizing a Lexsis page.

## Theme and Brand Context

Select exactly one saved store/theme pair for a page.

- Use the saved `brand-design.md` for voice, art direction, component guidance,
  and explicit design don'ts.
- Use `lexsis_brand` action `get_theme` for the current complete theme when a
  live refresh is required.
- Use `lexsis_brand` action `compile_theme` when theme CSS must be derived from
  brand inputs.
- Exact theme tokens win over prose when values conflict.
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

Inspect 390px, 768px, and 1280px layouts.

## Asset Roles

Template results do not expose a separate media-slot schema. Derive required
roles, aspect ratios, and crop guidance from the selected section source,
approved layout, and island schema.

Use live Shopify media for product identity. Visually verify creator and
product imagery. Temporary placeholders are visual-stage inputs only.

## Manifest Evidence

Record the design decision:

```json
{
  "template": {
    "mode": "page-kit",
    "pageKitId": "kit-slug",
    "sectionTemplateIds": ["hero-slug", "buy-box-slug"],
    "evaluatedTemplates": [],
    "selectionReason": "Matches the approved PDP structure",
    "selectedAt": "2026-09-04T12:00:00Z"
  },
  "design": {
    "themeId": "theme-id",
    "themeSource": "saved-and-verified",
    "stylePack": "editorial",
    "compiledStyleManifest": null
  }
}
```

`template.mode` is `page-kit`, `sections`, or `custom`. Do not invent a
template version when the live result does not expose one. After compilation,
store the returned style manifest under `design.compiledStyleManifest`.

`stylePack` is the selected named pack, `custom` for an intentional scoped
treatment, or `existing-page` when adopting and preserving a remote page's
current design.

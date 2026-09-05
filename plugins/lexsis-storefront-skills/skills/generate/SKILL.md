---
name: generate
description: Turn an approved plan, visual mockup, and verified assets into readable Lexsis source, a compiled draft, and a synchronized QA report.
---

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

## Promote the Approved Source

1. Treat `lexsis-source.html` and `page-theme.css` as the approved design
   contract. Do not recreate, simplify, or reinterpret them.
2. Reuse the selected page kit or section-template source. When earlier skills
   were explicitly skipped, search and fetch templates before custom
   composition.
3. If `/visual-page` was explicitly skipped, author the canonical source and
   page theme once, record the skip, and continue without claiming visual
   fidelity approval.
4. Require `/asset-prep` to have replaced temporary media. If asset preparation
   was explicitly skipped, verify and update assets locally before compiling.
5. Resolve every island's current active schema again. Prefer native variants
   and validated styling parts; use headless mode only with complete hooks.
6. Use one `<!-- section: id -->` followed by `<section id="id">` per section.
7. Keep island JSON readable where practical.
8. Keep global design CSS in `page-theme.css` and section-specific CSS beside
   its section in `lexsis-source.html`.
9. Use LX tokens for brand values and Tailwind utilities for layout. Do not
   depend on a runtime Tailwind CDN.
10. Use native commerce islands; never replace BuyBox or another commerce
   interaction with a custom button.
11. Keep production comments to section delimiters and exclude inline handlers,
   unsupported scripts, local paths, placeholders, and complete-page images.

When a visual is approved, generation may update live binding records in the
manifest or compiler arguments, but it must not change source, copy, classes,
section order, island placement, or CSS. A visible source or asset change
returns the visual to `changes-pending-approval`.

Run:

```bash
python3 skills/generate/scripts/validate_page_workspace.py \
  work/visual-pages/<page-handle> --phase precompile
```

Fix all blocking source, copy, claim, price, and asset findings.

## Compile and Create

Dry-run the exact approved bundle with `lexsis_pages` action `compile`. Confirm
its source, theme, configuration, structure, and bundle hashes match the
approved visual before calling `lexsis_page_create` action `create` with
`publish: false`.

If discovery exposes compile-artifact creation, create from the returned
`compile_id` and pass its expected bundle hash. Otherwise submit the exact
compiled source, CSS, head, and scripts bytes to page creation, then fetch the
persisted remote source and content immediately. A hash mismatch is blocking;
never accept a draft created from different input.

Store the returned page ID, version, and preview URL in the manifest. Record
the local, compiled, persisted-source, remote-bundle, and section hashes as the
synchronized baseline.
Store the compiler style manifest under `design.compiledStyleManifest`.
`lexsis-source.html` remains the editable source of truth.

## Hosted QA

At 390px, 768px, and 1280px verify:

- composition matches the approved mockup
- full-page screenshots of the generated preview and hosted draft match in
  geometry, typography, color, spacing, and media
- no overflow, clipping, broken media, or wrong theme
- islands hydrate
- primary CTA adds the expected Shopify variant
- variant selection, cart opening, quantity, and subtotal work
- copy, claims, assets, header, footer, and integrity pass

Write `qa-report.md` and update the manifest's QA fields.
Record `qa.visualRegression: true` only after the three viewport comparisons
pass. Review dynamic island regions manually while comparing their container
geometry and placement.

Run the validator with `--phase draft` after hosted QA. Return `DRAFT_READY`
only when fidelity, synchronization, hydration, responsive checks, and
commerce checks pass. Pass the source and bundle hashes fetched live from the
remote draft to `--remote-source-hash` and `--remote-bundle-hash`.

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
source_html_path
page_theme_path
visual_preview_path
compile_artifact_path
compile_result
page_id
page_version
preview_url
qa_report_path
```

Return `DRAFT_READY` only when synchronization and blocking QA checks pass.
Include the required MCP, template, binding, fallback, and blocker evidence.

---
name: generate
description: Turn an approved plan, visual mockup, and verified assets into readable Lexsis source, a compiled draft, and a synchronized QA report.
---

# Generate the Draft

Own production source, compilation, draft creation, and hosted interaction QA.
Do not publish.

Read `references/source-and-sync.md`.

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
2. Replace preview values and temporary media with verified live bindings.
3. Resolve every island's current active schema again.
4. Write complete, readable `lexsis-source.html` before compiling.
5. Use one `<!-- section: id -->` followed by `<section id="id">` per section.
6. Keep island JSON readable where practical.
7. Use native commerce islands; never replace BuyBox or another commerce
   interaction with a custom button.
8. Keep production comments to section delimiters and exclude inline handlers,
   unsupported scripts, local paths, placeholders, and complete-page images.

Run:

```bash
python3 skills/generate/scripts/validate_page_workspace.py \
  work/visual-pages/<page-handle> --phase precompile
```

Fix all blocking source, copy, claim, price, and asset findings.

## Compile and Create

Dry-run the complete source with `lexsis_pages` action `compile`. Fix all
compiler errors before calling `lexsis_page_create` action `create` with
`publish: false`.

Store the returned page ID, version, and preview URL in the manifest. Record
the source bundle hash and section hashes as the synchronized baseline.
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

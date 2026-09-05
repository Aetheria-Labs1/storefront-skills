---
name: generate
description: Promote approved canonical page source into a synchronized Lexsis draft and run hosted responsive, fidelity, and commerce QA.
---

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

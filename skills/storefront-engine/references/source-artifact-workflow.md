# Storefront Page Files

Use these files to pass work between the public storefront commands without
requiring one command to invoke another.

## Setup Context

`/setup` saves reusable brand design and one or more theme files under
`work/storefront/setup/`. A page binds exactly one saved store and theme.
Products, prices, variants, assets, island schemas, permissions, analytics,
and remote page versions remain live reads.

## Page Workspace

```text
work/visual-pages/<page-handle>/
├── page-plan.md
├── page-manifest.json
├── lexsis-source.html
├── page-theme.css
├── compile-artifact.json
├── visual-preview.html
├── qa-report.md
└── assets/
```

- `lexsis-source.html` is the only editable HTML source from visual design
  through publishing.
- Section-specific CSS stays in top-level `<style>` blocks beside its section.
- `page-theme.css` contains global tokens and page-wide custom CSS and is
  passed as the compiler's `theme_css`.
- `compile-artifact.json` stores the exact compile response and input hashes.
- `visual-preview.html` is generated from that compile response and is never
  edited or submitted as source.

## Manifest

Use `schemaVersion: 2`. Keep the normal MCP, template, setup, design, binding,
asset, section, island, QA, and remote records, plus:

```json
{
  "schemaVersion": 2,
  "themeCssPath": "work/storefront/setup/stores/<store-id>/themes/<theme-id>.css",
  "pageThemeCssPath": "page-theme.css",
  "pageConfig": {
    "head": {},
    "scripts": []
  },
  "compileInputs": {
    "productBinding": {},
    "commerceConfig": {}
  },
  "visual": {
    "status": "pending",
    "sourcePath": "lexsis-source.html",
    "themeCssPath": "page-theme.css",
    "previewPath": "visual-preview.html",
    "compileArtifactPath": "compile-artifact.json",
    "approvedSourceHash": null,
    "approvedThemeCssHash": null,
    "approvedConfigHash": null,
    "approvedStructureHash": null,
    "approvedBundleHash": null,
    "approvedCompileBundleHash": null,
    "hydrationStatus": "pending",
    "hydrationEvidence": null
  },
  "fidelity": {
    "status": "pending",
    "productionBundleHash": null,
    "remoteSourceHash": null,
    "remoteBundleHash": null,
    "changedBindingPaths": [],
    "approvedExceptions": []
  },
  "sourceSync": {
    "lastCompiledBundleHash": null,
    "lastSyncedBundleHash": null,
    "lastSyncedSectionHashes": {},
    "lastChangedSections": []
  }
}
```

`themeCssPath` is the reusable `/setup` source. `pageThemeCssPath` is the
page-local compile input. Do not duplicate the full CSS inside the manifest.

`visual.status` is `pending`, `changes-pending-approval`, `approved`,
`skipped`, or `not-used`. `not-used` is reserved for adopting an existing page.
An approved visual cannot be relabelled `not-used` to bypass fidelity checks.

## Compile Artifact

Write:

```json
{
  "schemaVersion": 1,
  "sourceHash": "...",
  "themeCssHash": "...",
  "configHash": "...",
  "structureHash": "...",
  "bundleHash": "...",
  "compiledBundleHash": "...",
  "compiledAt": "2026-09-05T12:00:00Z",
  "response": {}
}
```

`response` is the unmodified Lexsis compile result used to generate the
preview. `compiledBundleHash` is derived from that response. The local bundle
hash covers `lexsis-source.html`, `page-theme.css`, `pageConfig.head`,
`pageConfig.scripts`, and every value in `compileInputs`.

## Visual Approval and Assets

`/visual-page` creates the canonical source and page theme, compiles them, and
generates the preview from `compile-artifact.json`. Approval records all
visual hashes and requires every production island instance to hydrate. Record
the browser-observed expected and hydrated instance keys, check time, and
approved bundle hash in `visual.hydrationEvidence`.

`/asset-prep` replaces temporary media in the canonical source. Any visible
asset or crop change sets `visual.status` to `changes-pending-approval`, then
recompiles and regenerates the preview. Approval hashes are refreshed only
after the final-media preview is approved.

If the user explicitly skips `/visual-page`, record the skip and let
`/generate` create the canonical source once. Do not claim visual fidelity
approval for a skipped stage.

## Generation and Synchronization

`/generate` promotes the approved source. It must not change layout, classes,
copy, section order, island placement, or CSS. Prefer live product bindings in
compiler arguments or manifest records instead of rewriting visible source.

For creation:

1. Validate the local workspace.
2. Compile the exact local bundle without saving.
3. Confirm it matches the approved hashes.
4. Create with `publish: false`, using a discovered `compile_id` when
   supported or the exact compiled input bytes otherwise.
5. Fetch the persisted remote source and page content and calculate their
   hashes independently.
6. Reject source or bundle hash drift.
7. Save page ID, version, preview URL, local and remote hashes, and section
   hashes.

Run the `draft` validator with the live remote source and bundle hashes.
Manifest values alone are not sufficient remote evidence.

For editing:

1. Fetch the current remote version and stop on drift.
2. Change local source or page theme first.
3. Recompile the complete bundle.
4. Require renewed visual approval for visible changes.
5. Compare section hashes and patch only changed sections with
   `expected_version`.
6. Update local versions and hashes only after a successful write.

Remote content must never be the only copy of an intentional change.

## Completion Gate

`DRAFT_READY` requires:

- approved source hashes still match, unless visual design was explicitly
  skipped
- preview hydration passed
- compile and persisted remote hashes match
- remote version is recorded
- responsive QA passed at 390px, 768px, and 1280px
- local preview and hosted draft visual regression passed
- commerce, copy, claims, assets, and integrity checks passed

Publishing additionally requires the current entitlement and explicit user
approval for the synchronized page version.

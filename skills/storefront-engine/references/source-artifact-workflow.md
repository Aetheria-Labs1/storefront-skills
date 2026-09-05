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

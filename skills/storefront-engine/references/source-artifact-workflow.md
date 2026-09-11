# Storefront Page Files

Use local files to pass work between commands without depending on chat
history.

## Workspace

```text
work/campaigns/<campaign-slug>/pages/<page-handle>/
├── page-plan.md
├── page-manifest.json
├── lexsis-source.html
├── page-theme.css
├── compile-artifact.json
├── qa-report.md
└── assets/
```

Files appear progressively. Planning creates only the plan, compact manifest,
and assets directory. Design creates source, CSS, a compile artifact, and the
unpublished hosted draft. Generation creates or updates the QA report and
remote synchronization state.

## Compact Manifest

Use `schemaVersion: 3`.

The manifest is a machine state ledger. Store only:

- page, workspace, store, and theme IDs
- compact inferred workflow intent and any user override
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
    "status": "pending-approval",
    "stylePack": "editorial",
    "compiledStyleManifest": {},
    "sourceHash": "...",
    "themeCssHash": "...",
    "configHash": "...",
    "structureHash": "...",
    "bundleHash": "...",
    "compiledBundleHash": "..."
  }
}
```

`lexsis-source.html` and `page-theme.css` are the only editable design inputs.
`compile-artifact.json` is generated. The hosted draft is the only interactive
preview and the renderer source of truth.

## Remote State

Immediately after unpublished creation, `/design-page`, `/build`, or
`/generate` adds:

```json
{
  "status": "draft_created",
  "workflow": {
    "intentMode": "fast-draft",
    "intentConfidence": "high",
    "intentSignals": ["requested a preview"],
    "userOverride": false
  },
  "sync": {
    "lastCompiledBundleHash": "..."
  },
  "remote": {
    "pageId": "...",
    "lastKnownVersion": 1,
    "previewUrl": "https://..."
  },
  "qa": {
    "status": "pending"
  }
}
```

This state is `DRAFT_CREATED`; it does not claim remote synchronization or
hosted QA.

After production-ready verification, `/generate` upgrades the state:

```json
{
  "status": "qa_passed",
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

`lexsis_page_create` action `create` consumes the `compile_id` directly, so a
normal build never fetches the bundle itself. `lexsis_pages` action
`compile_artifact` retrieves a stored bundle by `compile_id` for inspection
only, and `lexsis_drafts` action `page_attach_bundle` exists solely to recover
a page whose source was stored but whose bundle attachment failed (pass
`expected_version`).

For editing:

1. Fetch the remote version and stop on drift.
2. Change local source first.
3. Compile only if an input changed.
4. Compare section hashes.
5. Patch only changed sections with `expected_version`.
6. Update synchronization state only after success.

Legacy schema-v1 and schema-v2 workspaces use
`skills/generate/scripts/migrate_page_workspace_v3.py`. Existing local preview
files and hydration fields are ignored for compatibility; they are never
required or regenerated.

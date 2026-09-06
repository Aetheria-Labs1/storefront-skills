# Production Source and Synchronization

`lexsis-source.html` and `page-theme.css` are the editable source of truth.
`compile-artifact.json` and `page-preview.html` are generated.

Headers, announcement bars, navigation, and footers live in
`lexsis-source.html` like every other section. Portable bundles preserve that
exact section order and contain no renderer-level `shell` or
`navigation_profile`.

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

When reusing a merchant template, apply it to the remote page only after the
same source has been inserted into the canonical local source. Record the new
remote version and hashes only after the apply succeeds.

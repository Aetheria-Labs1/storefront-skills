# Production Source and Synchronization

`lexsis-source.html` and `page-theme.css` are the editable source of truth.
`compile-artifact.json` is generated. The hosted draft is the only interactive
preview.

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

Draft creation and production readiness are separate states.

1. Inspect `remote.pageId`, version, and preview URL.
2. If they exist, fetch edit context and reuse that draft; never create a
   duplicate page merely because another skill or conversation began.
3. Validate the compact manifest and canonical source with the
   `draft-created` gate.
4. Refresh only volatile products, variants, prices, permissions, and remote
   version data.
5. Compile the current workspace inputs once when no matching clean artifact
   exists.
6. Create with `publish: false` only when no remote draft exists; otherwise
   patch changed sections with expected-version protection.
7. Save page ID, version, preview URL, compile hash, and `status:
   draft_created`.
8. Return `DRAFT_CREATED` immediately.
9. Fetch persisted source and remote hashes, then run hosted QA.
10. Save synchronized state and `status: qa_passed` only when every
   production-ready check succeeds.

A failed post-creation check does not erase or invalidate the reversible
draft. Report the draft and its blockers.

## Intent Evidence

Record the inferred mode compactly in `workflow`:

```json
{
  "intentMode": "fast-draft",
  "intentConfidence": "high",
  "intentSignals": ["requested a preview", "delegated specifics"],
  "userOverride": false
}
```

Intent evidence explains routing; it never grants publish or paid-generation
permission.

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

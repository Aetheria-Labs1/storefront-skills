# Storefront Page Editing

Run by `/design-page` (Existing Page Edits) and `/optimize` Apply.

Edit existing pages through canonical editable source and section-level remote
operations. Read `source-artifact-workflow.md` first.

## Edit Flow

1. Read `lexsis_pages.edit_context` and `lexsis_pages.source`.
2. Compare the current version with the last recorded version; reconcile drift.
3. Edit the returned source value and compile the complete changed inputs.
4. Compare section changes with the persisted baseline.
5. Patch only changed sections with `expected_version`,
   `expected_source_sha256` and an idempotency key where supported.
6. Update recorded version/hashes after success, then run `diff`, `integrity`
   and the affected checks on the hosted draft.

For existing pages, `page_id` is authoritative. Do not require the user to
reselect a workspace or pass `store_id`; an optional store ID is only an
assertion. Service-token store/workspace scopes remain authorization boundaries.

## Operations

### Update/Replace a Section

```
lexsis_drafts({
  action: "page_update_section",
  args: {
    page_id,
    section_id,
    source,
    expected_version,
    expected_source_sha256,
    idempotency_key
  }
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
  args: {
    page_id,
    source,
    position,
    expected_version,
    expected_source_sha256,
    idempotency_key
  }
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

- Retain the intended change and returned version in the task handoff
- Always call `lexsis_pages` action `edit_context` before a write
- Stop on unexpected version drift
- Re-read source and reconcile against the current version when an edit returns `version_conflict`
- Reference section IDs from the page data (don't guess)
- Compile the complete editable source before section patching
- After editing, run `diff` and `integrity`
- Batch related multi-section changes with `page_patch` so they create one
  version.
- Use explicit remove operations for absent properties. `null` remains a JSON
  value and is not deletion.
- When changing a collection binding, setting `products` removes `productIds`
  and setting `productIds` removes `products`; never send both.
- Reusing an idempotency key with the same request returns the original result.
  Reusing it with different content is an error.
- Update input hashes and manifests only after a successful remote write.
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout

Minor edits do not repeat planning or create page files. Resolve the saved
binding or current MCP context; keep the existing page id authoritative.

For published pages, `current_version` can advance while the live renderer
remains pinned to `published_version_id`. Publish only after QA.

## Applying Reusable Sections

Read `merchant-templates.md`. `template_apply` follows the same edit
preconditions and materializes source into the page. After success, fetch edit
context, read back the persisted source and hashes, then run `diff` and `integrity`.

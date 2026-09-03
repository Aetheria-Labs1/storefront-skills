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

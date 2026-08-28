# Storefront Page Editing

Edit existing pages using section-level operations.

## Edit Flow

1. `lexsis_pages` action `find`
2. `lexsis_pages` action `edit_context`
3. `lexsis_pages` actions `section_source`, `source`, or `inspect`
4. Edit exactly one source-format section
5. `lexsis_drafts` action `page_update_section` or `page_patch`
6. `lexsis_pages` actions `diff` and `integrity`

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
- Position: "before:{section_id}" or "after:{section_id}" or index number
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

- Always call `lexsis_pages` action `edit_context` before a write
- Re-read context/source and rebase when an edit returns `version_conflict`
- Reference section IDs from the page data (don't guess)
- After editing, run `diff` and `integrity`
- Batch related multi-section changes with `page_patch` so they create one version
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout

Minor edits use this workflow directly. They do not repeat the new-page planning
workflow; the existing page retains its approved plan.

For published pages, `current_version` can advance while the live renderer
remains pinned to `published_version_id`. Publish only after QA.

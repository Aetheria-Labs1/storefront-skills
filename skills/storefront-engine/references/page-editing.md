# Storefront Page Editing

Edit existing pages using section-level operations.

## Edit Flow

1. `find_page` — locate the target page
2. `get_page_edit_context` — resolve the page's store, workspace, theme, source availability, and current version
3. `get_page_source` and `inspect_page_sections` — read source and structure
4. Edit exactly one source-format section
5. `update_section_from_source` — compile, preflight, and save with `expected_version`
6. `check_page_integrity` — verify the completed page

For existing pages, `page_id` is authoritative. Do not require the user to
reselect a workspace or pass `store_id`; an optional store ID is only an
assertion. Service-token store/workspace scopes remain authorization boundaries.

## Operations

### Update/Replace a Section

```
update_section_from_source({
  page_id,
  section_id,
  source,
  expected_version
})
```
- Replaces the compiled section from source-format HTML
- Auto-bumps page version
- Returns `version_conflict` if another edit landed first
- Use for: changing copy, swapping images, restyling

### Add a New Section

```
update_section_from_source({
  page_id,
  source,
  position,
  expected_version
})
```
- Position: "before:{section_id}" or "after:{section_id}" or index number
- Must include full section HTML

### Remove a Section

```
remove_page_section(page_id, section_id)
```
- Irreversible — confirm with user first
- Auto-bumps version

### Reorder Sections

```
move_page_section(page_id, section_id, new_position)
```
- Position is 0-indexed
- All other sections shift accordingly

## Best Practices

- Always call `get_page_edit_context` before a write
- Re-read context/source and rebase when an edit returns `version_conflict`
- Reference section IDs from the page data (don't guess)
- After editing, run `check_page_integrity` before telling the user it is done
- For multi-section changes, batch them (each call bumps version)
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout

Minor edits use this workflow directly. They do not repeat the new-page planning
workflow; the existing page retains its approved plan.

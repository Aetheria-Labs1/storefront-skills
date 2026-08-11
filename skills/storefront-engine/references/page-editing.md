# Storefront Page Editing

Edit existing pages using section-level operations.

## Edit Flow

1. `find_page` — locate the target page
2. `get_page_source` and `inspect_page_sections` — read source and structure
3. Edit exactly one source-format section
4. `update_section_from_source` — compile, preflight, and save
5. `check_page_integrity` — verify the completed page

## Operations

### Update/Replace a Section

```
update_section_from_source({ page_id, section_id, source })
```
- Replaces the compiled section from source-format HTML
- Auto-bumps page version
- Use for: changing copy, swapping images, restyling

### Add a New Section

```
update_section_from_source({ page_id, source, position })
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

- Always `get_page` first to understand current structure
- Reference section IDs from the page data (don't guess)
- After editing, run `check_page_integrity` before telling the user it is done
- For multi-section changes, batch them (each call bumps version)
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout

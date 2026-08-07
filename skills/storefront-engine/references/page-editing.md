# Storefront Page Editing

Edit existing pages using section-level operations.

## Edit Flow

1. `list_pages` — find target page
2. `get_page` — read current page structure + HTML
3. Make changes (one of the operations below)
4. `validate_vibe_page` — verify changes are valid
5. Page auto-versions on each mutation

## Operations

### Update/Replace a Section

```
update_page_section(page_id, section_id, { html, css, settings })
```
- Can replace HTML entirely or patch specific parts
- Auto-bumps page version
- Use for: changing copy, swapping images, restyling

### Add a New Section

```
update_page_section(page_id, null, { html, css, settings, position })
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
- After editing, run `validate_vibe_page` before telling user it's done
- For multi-section changes, batch them (each call bumps version)
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout

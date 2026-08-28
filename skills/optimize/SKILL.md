---
name: optimize
description: CRO-optimize an existing page — analyzes conversion weaknesses and applies fixes (redesign sections, add trust signals, fix CTAs, improve mobile UX)
---

# Optimize Storefront Page

CRO-optimize an existing page — analyzes conversion weaknesses and applies fixes (redesign sections, add trust signals, fix CTAs, improve mobile UX)

## Context

- **cro-research**: > Compiled from Baymard Institute, Unbounce, Shopify, CXL, Conversion Rate Experts, Nielsen Norman Group, Littledata, HubSpot, Optimizely, Wordstream, and Awwwards analysis. Data points sourced 2024-2026.
- **conversion-psychology**: > When to load: ALWAYS. Read before generating any ecommerce page.

## Workflow

# Storefront Page Editing

Edit existing pages using section-level operations.

## Edit Flow

1. `lexsis_pages` action `find`
2. `lexsis_pages` actions `edit_context`, `source`, and `inspect`
3. Make section-level source changes
4. `lexsis_drafts` action `page_update_section` or `page_patch`
5. `lexsis_pages` actions `diff` and `integrity`

## Operations

### Update/Replace a Section

```
lexsis_drafts({ action: "page_update_section", args: { page_id, section_id, source, expected_version } })
```
- Replaces the compiled section from one source-format section
- Auto-bumps page version
- Use for: changing copy, swapping images, restyling

### Add a New Section

```
lexsis_drafts({ action: "page_update_section", args: { page_id, source, position, expected_version } })
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

- Always read `edit_context` before writing
- Reference section IDs from the page data (don't guess)
- After edits, run `diff` and `integrity`
- Batch related changes with `page_patch` so they create one version
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout


# Page Redesign (Modernize/Refresh Existing Page)

Visually refresh an existing page using performance data to preserve what works and redesign what does not.

## Prerequisites

- Target page exists (published or draft)
- Brand kit up to date (may have changed since page creation)
- Page analytics available for performance-informed decisions

## Workflow

### Step 1 — Context Gathering

```
lexsis_workspace → get/stores
lexsis_brand → brand_kit/list_themes/get_theme
lexsis_design → guide
```

These four calls ALWAYS run first. No exceptions.

### Step 2 — Locate and Inspect Target Page

```
lexsis_pages({ action: "find", args: { query: "page name or slug" } })
```
Or:
```
lexsis_pages({ action: "list", args: { status: "published" } })
```

Then load full page data:
```
lexsis_pages({ action: "get", args: { page_id } })
lexsis_pages({ action: "inspect", args: { page_id } })
```

Understand: section count, section types, content blocks, current `--lx-*` variables, islands in use.

### Step 3 — Analyze Performance

```
lexsis_analytics({ action: "page", args: { page_id } })
```

Categorize each section:
- **KEEP** — high CVR, proven copy, minor visual polish only
- **REDESIGN** — same content, new layout/styling
- **REPLACE** — low-performing, rebuild approach
- **REMOVE** — adds friction, no conversion value

Key rule: NEVER redesign sections that are converting well. Analytics data overrides aesthetic preferences.

### Step 4 — Apply Section-by-Section Updates

For each section to change:
```
lexsis_drafts({ action: "page_update_section", args: { page_id, section_id, source, expected_version } })
```

For reordering (if scroll-depth data suggests better flow):
```
lexsis_drafts({ action: "page_move_section", args: { page_id, section_id, position, expected_version } })
```

All updated sections must use `--lx-*` CSS variables from current brand kit. No hardcoded colors or fonts.

### Step 5 — Validate

```
lexsis_pages({ action: "integrity", args: { page_id, archetype } })
```

Ensure no broken islands, valid HTML structure, responsive layout intact.

### Step 6 — Show Before/After

```
lexsis_pages({ action: "diff", args: { page_id, version_a: previous_version, version_b: current_version } })
```

Present structural diff to user for approval before publishing.

### Step 7 — Load Preview and Verify Visually

```
lexsis_pages({ action: "get", args: { page_id } })
```

Use the returned `preview_url`.

Use the host agent's browser capability at 390px, 768px, and 1280px. Lexsis
does not create a shared browser session. If unavailable, provide the preview
URL and state that visual verification remains.

Checklist:
- [ ] Brand colors applied (current kit, not old defaults)
- [ ] Fonts loading correctly (not system fallback)
- [ ] High-CVR sections unchanged in structure
- [ ] Mobile layout intact or improved
- [ ] All islands still functional (cart, forms)
- [ ] Section spacing consistent
- [ ] No horizontal scroll on mobile

If issues are found, patch through `lexsis_drafts`, then re-verify.

### Step 8 — Go Live (User Confirms)

Only after user approves:
```
lexsis_live_ops({ action: "publish", args: { page_id } })
```

If redesign later hurts metrics: `rollback_page_version(page_id, version_id)` is available.

## Decision Points

| Question | Decision |
|----------|----------|
| Full rebuild or section-by-section? | >70% sections changing = full rebuild is faster |
| Keep copy or rewrite? | Keep unless analytics show messaging problems |
| Preserve section order? | Yes, unless scroll-depth shows clear drop-off pattern |
| Same section types or new? | Prefer new layouts for freshness; same types if copy fits |
| A/B test old vs new? | Recommend if page has >500 daily visitors |

## Quality Gates

- URL/slug PRESERVED (never change -- breaks SEO and ad links)
- Page title and meta description preserved unless explicitly requested
- High-CVR sections retain their copy and core structure
- New design matches current brand kit (`--lx-*` variables)
- Mobile responsiveness maintained or improved
- All existing islands remain functional
- Version history intact (rollback available)
- Page passes `lexsis_pages` action `integrity` with zero errors

## Optional Follow-Up

This skill can end with a validated page update. `publish` is available for an
explicit release request, while `experiment` can use a testable hypothesis
when the user wants a controlled comparison.

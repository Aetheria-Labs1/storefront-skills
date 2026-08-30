# Page Redesign (Modernize/Refresh Existing Page)

Visually refresh an existing page using performance data to preserve what works and redesign what does not.

## Prerequisites

- Target page exists (published or draft)
- Brand kit up to date (may have changed since page creation)
- Page analytics available for performance-informed decisions

## Workflow

### Step 1 — Context Gathering

```
lexsis_workspace.get()          → workspace ID, plan tier
lexsis_workspace.stores()           → store domain, Shopify data
lexsis_brand(action: "brand_kit", args: {})                  → logo, fonts, colors, voice, radius
lexsis_design.guide()                  → brand brief, design philosophy, constraints
```

These four calls ALWAYS run first. No exceptions.

### Step 2 — Locate and Inspect Target Page

```
lexsis_pages.find({ query: "page name or slug" })
```
Or:
```
lexsis_pages.list({ status: "published" })
```

Then load full page data:
```
lexsis_pages.get(page_id)
lexsis_pages.inspect(page_id)
```

Understand: section count, section types, content blocks, current `--lx-*` variables, islands in use.

### Step 3 — Analyze Performance

```
lexsis_analytics.page(page_id)
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
lexsis_drafts.page_update_section({ page_id, section_id, source })
```

For reordering (if scroll-depth data suggests better flow):
```
lexsis_drafts.page_move_section(page_id, section_id, new_position)
```

All updated sections must use `--lx-*` CSS variables from current brand kit. No hardcoded colors or fonts.

### Step 5 — Validate

```
lexsis_pages.integrity({ page_id, archetype })
```

Ensure no broken islands, valid HTML structure, responsive layout intact.

### Step 6 — Show Before/After

```
lexsis_pages.diff(page_id, { from: previous_version, to: current_version })
```

Present structural diff to user for approval before publishing.

### Step 7 — Load Preview and Verify Visually

```
lexsis_pages.get(page_id)
```

Use the returned `preview_url`.

**Claude Code (Playwright MCP):**
```
browser_navigate({ url: preview_url })
browser_take_screenshot()
```

**Codex:** Use built-in browser to open preview_url.

**Other IDEs:** Provide URL: "Preview: {url} -- open to verify."

Checklist:
- [ ] Brand colors applied (current kit, not old defaults)
- [ ] Fonts loading correctly (not system fallback)
- [ ] High-CVR sections unchanged in structure
- [ ] Mobile layout intact or improved
- [ ] All islands still functional (cart, forms)
- [ ] Section spacing consistent
- [ ] No horizontal scroll on mobile

If issues found: `lexsis_drafts.page_update_section` to fix, then re-verify.

### Step 8 — Go Live (User Confirms)

Only after user approves:
```
lexsis_live_ops(action: "publish", args: page_id)
```

If redesign later hurts metrics: `lexsis_live_ops.rollback(page_id, version_id)` is available.

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
- Page passes `lexsis_pages.integrity` with zero errors

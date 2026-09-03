# Personalization Variant (Persona-Specific Page Versions)

Read `source-artifact-workflow.md`. Every persona variant has its own readable
local source, manifest, synchronized remote version, and QA record.

Create targeted page variants adapting messaging, imagery, social proof, and CTAs to each audience segment's motivations and objections.

## Prerequisites

- Base page exists (the page to personalize from)
- Personas defined or user describes target audiences
- Brand kit available (shared across all variants)

## Workflow

### Step 1 — Context Gathering

Confirm the base page's saved store/theme binding and synchronized local
source. Read current access, personas, products, assets, analytics, and remote
version live.

### Step 2 — Load Personas and Base Page

```
lexsis_campaigns.personas()
```

Review available audience segments. If none exist, define inline: name, demographics, pain points, motivations, objections, buying stage, tone preference.

```
lexsis_pages.get(page_id)
lexsis_pages.content(page_id)
```

Understand current structure, copy, and section types. This is the default variant.

### Step 3 — Plan Persona Adaptations

For each selected persona, identify what changes (ordered by conversion impact):

| Priority | Element | Personalization Strategy |
|----------|---------|--------------------------|
| 1 | Hero headline + subheadline | Tone shift: urgent for deal-seekers, aspirational for status-seekers (+202% CVR) |
| 2 | Hero image | Demographic match: age, lifestyle, environment |
| 3 | Social proof selection | Relevant testimonials matching persona's concern |
| 4 | CTA text | Motivation match: savings-focused vs quality-focused vs speed-focused |
| 5 | Section ordering | Pain-first for problem-aware, solution-first for solution-aware |

Not everything changes. Keep brand identity (colors, fonts, logo) consistent across all variants.

### Step 4 — Source Persona-Matched Assets

For each persona:
```
lexsis_asset_library({ action: "search", args: { query: "<persona-relevant imagery>", workspace_id, theme_id } })
```

Find images reflecting the persona's world. Generate if needed:
```
lexsis_drafts({ action: "asset_generate", args: { prompt: "...", demographic: "<persona context>", workspace_id, theme_id } })
```

### Step 5 — Create Each Variant

For each persona, first create
`work/visual-pages/<base-handle>--<persona-key>/`, copy the synchronized base
files, make the persona changes in local source, run the source gate, and
compile the complete variant. Derive the remote change set from that local
diff, then:

```
lexsis_drafts({
  action: "page_variation",
  args: {
    page_id,
    name: "<persona_name> variant",
    changes
  }
})
```

Record the returned page ID/version and verify the remote result matches the
local variant bundle.

All variants use the same `--lx-*` CSS variables (brand stays consistent). Only content, imagery, and tone change.

Islands remain identical across variants unless the experiment specifically
tests props:
```html
<lx-island name="BuyBox">
  <script type="application/json">
    { "product": { "title": "...", "price": "$29.99", "variants": [] } }
  </script>
</lx-island>
```

### Step 6 — Validate All Variants

For each variant:
```
lexsis_pages.integrity({ page_id: variant_page_id, archetype })
```

Ensure all render correctly, islands work, mobile intact.

### Step 7 — Visual Verification (Each Variant)

**Claude Code (Playwright MCP):**
```
browser_navigate({ url: variant_preview_url })
browser_take_screenshot()
```

**Codex:** Use built-in browser to open each variant's preview_url.

**Other IDEs:** Provide URLs: "Variant A: {url_a}, Variant B: {url_b} -- open to verify."

Checklist (per variant):
- [ ] Headline tone matches persona (urgent vs aspirational vs analytical)
- [ ] Hero image reflects persona demographic
- [ ] CTA language aligns with persona motivation
- [ ] Social proof relevant to persona's concerns
- [ ] Brand identity consistent (`--lx-*` variables unchanged)
- [ ] Mobile layout intact
- [ ] Islands hydrated correctly

### Step 8 — (Optional) Set Up Persona-Targeted Experiment

```
lexsis_drafts(action: "experiment_create", args: {
  page_id: base_page_id,
  variants: [
    { page_id: variant_a_id, weight: 33, targeting: { persona: "deal-seekers" } },
    { page_id: variant_b_id, weight: 33, targeting: { persona: "quality-seekers" } },
    { page_id: base_page_id, weight: 34, targeting: { default: true } }
  ]
})
```

Traffic routes to matching persona variant based on UTM/audience signals.

## Decision Points

| Question | Decision |
|----------|----------|
| Which personas? | Top 2-3 highest-value segments (by revenue or volume) |
| What to personalize? | Headlines + hero image + CTA = highest impact; start there |
| Full rewrite or selective? | Selective: 3-5 elements max per variant to isolate impact |
| Auto-assign or manual? | Auto if UTM/referrer identifies segment; manual for broad traffic |
| How many variants? | 2-4 max -- more variants need more traffic for significance |

## Quality Gates

- Each variant feels genuinely tailored (not just a headline swap)
- Imagery matches persona demographic and psychographic profile
- CTA language aligns with persona motivation
- Social proof relevant to persona (industry-matched, use-case-matched)
- All variants share same `--lx-*` brand identity
- Each variant passes `lexsis_pages.integrity` independently
- Tone consistent within each variant (headline tone = body copy tone)
- Structural integrity maintained (no broken sections or islands)

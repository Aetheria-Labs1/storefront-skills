# Personalization Variant (Persona-Specific Page Versions)

Create targeted page variants adapting messaging, imagery, social proof, and CTAs to each audience segment's motivations and objections.

## Prerequisites

- Base page exists (the page to personalize from)
- Personas defined or user describes target audiences
- Brand kit available (shared across all variants)

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
get_brand_kit()                  → logo, fonts, colors, voice, radius
```

These three calls ALWAYS run first. No exceptions.

### Step 2 — Load Personas and Base Page

```
list_personas()
```

Review available audience segments. If none exist, define inline: name, demographics, pain points, motivations, objections, buying stage, tone preference.

```
get_page(page_id)
get_page_content(page_id)
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
search_design_library({ query: "<persona-relevant imagery>" })
```

Find images reflecting the persona's world. Generate if needed:
```
generate_asset({ prompt: "...", demographic: "<persona context>" })
```

### Step 5 — Create Each Variant

For each persona:
```
create_page_variation(page_id, {
  name: "<persona_name> variant",
  changes: {
    sections: [
      { section_id: "hero", html: "...", css: "..." },
      { section_id: "social-proof", html: "..." },
      { section_id: "cta-block", html: "..." }
    ]
  }
})
```

All variants use the same `--lx-*` CSS variables (brand stays consistent). Only content, imagery, and tone change.

Islands remain identical across variants -- only the surrounding copy/imagery adapts:
```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[...]}}'></div>
```

### Step 6 — Validate All Variants

For each variant:
```
validate_vibe_page(variant_page_id)
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
create_ab_test({
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
- Each variant passes `validate_vibe_page` independently
- Tone consistent within each variant (headline tone = body copy tone)
- Structural integrity maintained (no broken sections or islands)

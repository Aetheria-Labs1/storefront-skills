---
name: experiment
description: Set up A/B tests, personalization variants, and monitor experiment results — hypothesis-driven testing with statistical significance tracking
---

# Run Storefront Experiment

Set up A/B tests, personalization variants, and monitor experiment results — hypothesis-driven testing with statistical significance tracking

## Context

- **conversion-psychology**: > When to load: ALWAYS. Read before generating any ecommerce page.

## Workflow

# Storefront Analytics & Experiments

Access page performance data and manage A/B experiments.

## Analytics Tools

### Page-Level Deep Dive
```
lexsis_analytics({ action: "page", args: { page_id } })
```
Returns: CVR, bounce rate, time on page, traffic sources, device split, top-performing sections.

### Time Series Trends
```
lexsis_analytics({ action: "timeseries", args: { metric: "conversions", period: "daily", range: "30d" } })
```
Returns: daily/weekly trends for hits, conversions, revenue, AOV.

### Revenue Attribution
```
lexsis_analytics({ action: "attribution", args: { page_id? } })
```
Returns: ROAS by channel, revenue per page, top campaigns driving conversions.

## A/B Testing Flow

### 1. Create Experiment
```
lexsis_drafts({
  action: "experiment_create",
  args: {
    page_id: "...",
    variants: [{ blueprint_id: "...", weight: 50 }, { blueprint_id: "...", weight: 50 }]
  }
})
```

### 2. Monitor Results
```
lexsis_analytics({ action: "experiment", args: { experiment_id } })
```
Returns: CVR per variant, statistical significance (mSPRT), sample sizes, winner recommendation.

### 3. Scale Winner
```
lexsis_live_ops({ action: "scale_winner", args: { experiment_id, variant_id: "..." } })
```
Scales winning variant to 100% traffic, marks experiment complete.

## Best Practices

- Wait for statistical significance before scaling winner
- Minimum ~1000 visitors per variant for reliable results
- Check device split — a variant may win on mobile but lose on desktop
- Use `get_attribution` to understand which traffic sources convert best
- Compare page analytics before/after changes to measure impact


# Personalization Variant (Persona-Specific Page Versions)

Create targeted page variants adapting messaging, imagery, social proof, and CTAs to each audience segment's motivations and objections.

## Prerequisites

- Base page exists (the page to personalize from)
- Personas defined or user describes target audiences
- Brand kit available (shared across all variants)

## Workflow

### Step 1 — Context Gathering

```
lexsis_workspace → get/stores
lexsis_brand → brand_kit/list_themes/get_theme
```

These three calls ALWAYS run first. No exceptions.

### Step 2 — Load Personas and Base Page

```
lexsis_campaigns({ action: "personas", args: { workspace_id } })
```

Review available audience segments. If none exist, define inline: name, demographics, pain points, motivations, objections, buying stage, tone preference.

```
lexsis_pages({ action: "get", args: { page_id } })
lexsis_pages({ action: "content", args: { page_id } })
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
lexsis_asset_library({ action: "search", args: { query: "<persona-relevant imagery>", workspace_id } })
```

Find images reflecting the persona's world. Generate if needed:
```
lexsis_drafts({ action: "asset_generate", args: { prompt: "...", demographic: "<persona context>", workspace_id } })
```

### Step 5 — Create Each Variant

For each persona:
```
lexsis_drafts({
  action: "page_variation",
  args: {
    page_id,
    name: "<persona_name> variant",
    changes: {
      sections: [
        { section_id: "hero", html: "...", css: "..." },
        { section_id: "social-proof", html: "..." },
        { section_id: "cta-block", html: "..." }
      ]
    }
  }
})
```

All variants use the same `--lx-*` CSS variables (brand stays consistent). Only content, imagery, and tone change.

Islands remain identical across variants -- only the surrounding copy/imagery adapts.
When a prop change is part of the experiment, edit source-format markup:
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
lexsis_pages({ action: "integrity", args: { page_id: variant_page_id, archetype } })
```

Ensure all render correctly, islands work, mobile intact.

### Step 7 — Visual Verification (Each Variant)

Use the host agent's browser capability at 390px, 768px, and 1280px for every
variant. Lexsis does not create shared browser sessions. If browser access is
unavailable, provide the preview URLs and state that visual QA remains.

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
lexsis_drafts({
  action: "experiment_create",
  args: {
    page_id: base_page_id,
    variants: [
      { page_id: variant_a_id, weight: 33, targeting: { persona: "deal-seekers" } },
      { page_id: variant_b_id, weight: 33, targeting: { persona: "quality-seekers" } },
      { page_id: base_page_id, weight: 34, targeting: { default: true } }
    ]
  }
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
- Each variant passes `lexsis_pages` action `integrity` independently
- Tone consistent within each variant (headline tone = body copy tone)
- Structural integrity maintained (no broken sections or islands)


# A/B Test Variant (Hypothesis-Driven Experiment)

Clone an existing page, apply a single focused change based on a clear hypothesis, launch a controlled experiment, and monitor for statistical significance via mSPRT.

## Prerequisites

- Target page exists and is published (needs traffic)
- Sufficient traffic (minimum 200 daily visitors, recommend 500+)
- Clear metric to optimize (CVR, AOV, bounce rate, scroll depth)

## Workflow

### Step 1 — Context Gathering

```
lexsis_workspace → get/stores
```

These two calls ALWAYS run first. No exceptions.

### Step 2 — Load Current Page and Baseline

```
lexsis_pages({ action: "get", args: { page_id } })
lexsis_analytics({ action: "page", args: { page_id } })
```

Record baseline performance:
- Conversion rate (primary metric)
- Bounce rate, average time on page
- Scroll depth, CTA click-through
- Revenue per visitor

This is the control to beat.

### Step 3 — Formulate Hypothesis

Structure: "Changing **[element]** from **[current]** to **[proposed]** will improve **[metric]** by **[estimated %]** because **[reason based on user behavior]**."

Document the hypothesis BEFORE creating the variant. Not post-hoc.

Common high-impact tests (ordered by typical lift):
1. Hero headline copy (+5-15% CVR)
2. CTA button color/text (+3-10% CTR)
3. Social proof placement (+5-22% depending on type)
4. Hero image: lifestyle vs product-focused (+8-12%)
5. Section ordering: problem-first vs solution-first (+3-7%)
6. Price anchoring: was/now vs % off (+4-8%)

### Step 4 — Create the Variant

```
lexsis_drafts({ action: "page_duplicate", args: { page_id } })
```

Creates exact copy. Then apply the SINGLE focused change:
```
lexsis_drafts({
  action: "page_update_section",
  args: { page_id: variant_page_id, section_id, source, expected_version }
})
```

RULE: ONE change per test. Multiple changes make attribution impossible.

All styling via `--lx-*` CSS variables. Islands remain unchanged unless the
test specifically targets island props:
```html
<lx-island name="BuyBox">
  <script type="application/json">
    { "product": { "title": "...", "price": "$29.99", "variants": [] } }
  </script>
</lx-island>
```

### Step 5 — Validate Variant

```
lexsis_pages({ action: "integrity", args: { page_id: variant_page_id, archetype } })
```

Ensure variant renders correctly, all islands work, mobile intact.

### Step 6 — Visual Verification

Use the host agent's browser capability at 390px, 768px, and 1280px. If it is
unavailable, provide the preview URL and state that visual QA remains.

Checklist:
- [ ] The ONE change is clearly visible
- [ ] Everything else identical to control
- [ ] Mobile layout intact
- [ ] Islands hydrated correctly
- [ ] No unintended side effects (broken spacing, color bleed)

### Step 7 — Launch Experiment

```
lexsis_drafts({
  action: "experiment_create",
  args: {
    page_id: page_id,
    hypothesis: "Changing [X] will improve [metric] because [reason]",
    variants: [
      { page_id: page_id, weight: 50, name: "Control (A)" },
      { page_id: variant_page_id, weight: 50, name: "Variant (B)" }
    ],
    primary_metric: "conversion_rate",
    minimum_sample: 1000
  }
})
```

50/50 split is standard. 80/20 only for high-traffic pages testing risky changes.

### Step 8 — Monitor Results

```
lexsis_analytics({ action: "experiment", args: { experiment_id } })
```

Returns: CVR per variant with confidence intervals, statistical significance (mSPRT), sample size, winner recommendation, secondary metrics.

RULES:
- NEVER call a winner before mSPRT reports `significant: true`
- Minimum 1000 visitors per variant for evaluation
- Check device split (variant may win mobile, lose desktop)
- Monitor secondary metrics (winning CVR but tanking AOV is not a win)

### Step 9 — Scale Winner

Only when `significant: true`:
```
lexsis_live_ops({ action: "scale_winner", args: { experiment_id, variant_id: winning_variant_id } })
```

Routes 100% traffic to winner. Marks experiment complete.

If no winner after 2000+ visitors per variant: the change has no meaningful impact. Stop test, formulate bolder hypothesis.

## Decision Points

| Question | Decision |
|----------|----------|
| What to test first? | Highest impact, lowest effort: headline > CTA > hero > layout |
| Traffic split? | 50/50 default; 80/20 for high-traffic + risky changes |
| When to check? | After 500+ visitors per variant; avoid daily peeking |
| When to stop? | Significant result OR >3000 visitors/variant with no signal |
| Variant loses? | Document learning, revert to control, new hypothesis |
| Multiple tests? | Only on DIFFERENT pages; never two tests on same page |

## Quality Gates

- ONE change per test (scientific rigor -- isolate the variable)
- Hypothesis documented BEFORE variant creation
- Minimum 1000 visitors per variant before evaluating
- Statistical significance required (mSPRT p<0.05) before declaring winner
- Both variants pass `lexsis_pages` action `integrity`
- Control remains untouched for test duration
- Secondary metrics monitored alongside primary
- Learning documented regardless of outcome (losses teach as much as wins)
- Wait for mSPRT -- never call early based on gut feeling

## Optional Follow-Up

This skill can end with a documented winner or learning. `optimize` can use
that evidence for a later page improvement when the user requests one.

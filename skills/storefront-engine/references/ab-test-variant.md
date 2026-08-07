# A/B Test Variant (Hypothesis-Driven Experiment)

Clone an existing page, apply a single focused change based on a clear hypothesis, launch a controlled experiment, and monitor for statistical significance via mSPRT.

## Prerequisites

- Target page exists and is published (needs traffic)
- Sufficient traffic (minimum 200 daily visitors, recommend 500+)
- Clear metric to optimize (CVR, AOV, bounce rate, scroll depth)

## Workflow

### Step 1 — Context Gathering

```
get_workspace_details()          → workspace ID, plan tier
get_connected_stores()           → store domain, Shopify data
```

These two calls ALWAYS run first. No exceptions.

### Step 2 — Load Current Page and Baseline

```
get_page(page_id)
get_page_analytics(page_id)
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
duplicate_page(page_id)
```

Creates exact copy. Then apply the SINGLE focused change:
```
update_page_section(variant_page_id, section_id, { html, css, settings })
```

RULE: ONE change per test. Multiple changes make attribution impossible.

All styling via `--lx-*` CSS variables. Islands unchanged unless the test specifically targets island props:
```html
<div data-island="BuyBox" data-props='{"product":{"title":"...","price":"$29.99","variants":[...]}}'></div>
```

### Step 5 — Validate Variant

```
validate_vibe_page(variant_page_id)
```

Ensure variant renders correctly, all islands work, mobile intact.

### Step 6 — Visual Verification

**Claude Code (Playwright MCP):**
```
browser_navigate({ url: variant_preview_url })
browser_take_screenshot()
```

**Codex:** Use built-in browser to open variant preview.

**Other IDEs:** Provide URL: "Variant preview: {url} -- verify change is visible."

Checklist:
- [ ] The ONE change is clearly visible
- [ ] Everything else identical to control
- [ ] Mobile layout intact
- [ ] Islands hydrated correctly
- [ ] No unintended side effects (broken spacing, color bleed)

### Step 7 — Launch Experiment

```
create_ab_test({
  page_id: page_id,
  hypothesis: "Changing [X] will improve [metric] because [reason]",
  variants: [
    { page_id: page_id, weight: 50, name: "Control (A)" },
    { page_id: variant_page_id, weight: 50, name: "Variant (B)" }
  ],
  primary_metric: "conversion_rate",
  minimum_sample: 1000
})
```

50/50 split is standard. 80/20 only for high-traffic pages testing risky changes.

### Step 8 — Monitor Results

```
get_experiment_results(experiment_id)
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
scale_winner(experiment_id, winning_variant_id)
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
- Both variants pass `validate_vibe_page`
- Control remains untouched for test duration
- Secondary metrics monitored alongside primary
- Learning documented regardless of outcome (losses teach as much as wins)
- Wait for mSPRT -- never call early based on gut feeling

# Storefront Analytics & Experiments

Access page performance data and manage A/B experiments.

## Analytics Tools

### Page-Level Deep Dive
```
lexsis_analytics.page(page_id)
```
Returns: CVR, bounce rate, time on page, traffic sources, device split, top-performing sections.

### Time Series Trends
```
lexsis_analytics.timeseries({ metric: "conversions", period: "daily", range: "30d" })
```
Returns: daily/weekly trends for hits, conversions, revenue, AOV.

### Revenue Attribution
```
lexsis_analytics.attribution({ page_id? })
```
Returns: ROAS by channel, revenue per page, top campaigns driving conversions.

## A/B Testing Flow

### 1. Create Experiment
```
lexsis_drafts(action: "experiment_create", args: {
  page_id: "...",
  variants: [{ blueprint_id: "...", weight: 50 }, { blueprint_id: "...", weight: 50 }]
})
```

### 2. Monitor Results
```
lexsis_analytics.experiment(experiment_id)
```
Returns: CVR per variant, statistical significance (mSPRT), sample sizes, winner recommendation.

### 3. Scale Winner
```
lexsis_live_ops.scale_winner(experiment_id, { variant_id: "..." })
```
Scales winning variant to 100% traffic, marks experiment complete.

### Reading Section Engagement

Section rows follow page order. Views are sessions where the section was at
least half on screen; engaged is the share of viewers who stayed 3s or longer;
drop-off compares each section with the previous in-flow section; CTR is
viewers who clicked a CTA divided by views. Sticky bars, floating buttons,
sticky headers, and cart drawers are reported as persistent elements or
overlays outside page order, so they never create a drop-off. Treat pages with
fewer than 20 sessions as directional.

## Best Practices

- Wait for statistical significance before scaling winner
- Minimum ~1000 visitors per variant for reliable results
- Check device split  -  a variant may win on mobile but lose on desktop
- Use `lexsis_analytics.attribution` to understand which traffic sources convert best
- Compare page analytics before/after changes to measure impact

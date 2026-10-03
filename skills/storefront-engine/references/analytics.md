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


## Quiz journey and response evidence

`Quiz` emits consented, identifier-only `lx_quiz_*` events across exposure,
start/resume/restart, questions, committed/changed answers, branches, review,
completion, results, product interactions, cart outcomes, and explicit dismissal.
Raw answers, contact details, and question labels are excluded;
`analytics.answerAllowlist` does not permit raw values.

Response saving is a separate shopper choice. A saved response can exist without
analytics consent and without quiz events. `lx_quiz_completed` means a result was
reached; server-side `lx_quiz_submission_saved` requires persisted completion and
analytics linkage. Retries reuse event identity. Neither proves checkout or payment.

Read retained response summaries/details through `lexsis_capture.quiz_responses`
and `lexsis_capture.quiz_response`, scoped to the selected store and definition.
MCP values are redacted; use the merchant response viewer for authorized reveals.
Check pagination, status, test-mode filters, and retention before concluding that
responses are missing. Normal tests on published pages are not automatically
classified as test mode.

There is no dedicated quiz drop-off, entry/exit cohort, or paid-order attribution
report in the current tools. Missing completion is not an observed exit reason.
Follow `references/quiz-authoring.md` for policy setup and post-publication proof;
preview does not collect production responses.

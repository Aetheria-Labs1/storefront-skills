# Page Plan Contract

`/plan-page` owns the full page specification. `/visualize-page` may illustrate
it, `/plan-assets` resolves its production media, and `/design-page` implements
it. Later skills return to planning when they need to change strategy,
sections, claims, offers, or customer-facing copy.

## Required Blocks

Write these blocks in order:

1. `## Binding`
2. `## Page type`
3. `## Page strategy`
4. `## Consumer decision model`
5. `## Design direction`
6. `## Section specification`
7. `## Proof ledger`
8. `## Offer ledger` when an offer exists
9. `## Message match` for paid or campaign-led traffic
10. `## Claim gate`
11. `## Asset requirements`
12. `## Template direction`
13. `## Open decisions`
14. `## Plan status`

`none` is valid. `TBD`, placeholders, instructions to a future writer, and
unlabelled assumptions are not.

## Binding

```markdown
## Binding

| Field | Value |
|---|---|
| Workspace | <name and id> |
| Store | <name, domain, and id> |
| Theme | <name and id> |
| Plan date | <ISO date> |
| Setup refresh | <date> |
```

## Page Type

```markdown
## Page type

**Type.** <page-type id>
**Funnel stage.** tof | mof | bof | retention
**Awareness.** unaware | problem-aware | solution-aware | product-aware | most-aware
**Traffic.** <source>
**Offer.** <offer id> or none
**Campaign.** <name or evergreen>
**Copy framework.** <framework id>
**Mandatory sections omitted.** none | <section>: <reason>
**Deviations.** none | <decision>: <reason>
```

## Page Strategy

```markdown
## Page strategy

**Audience and market.** <persona, market, language>
**Traffic and message.** <source plus supplied promise or search intent>
**Goal.** <one measurable conversion action>
**Product scope.** <product/collection ids and default variant>
**Purchase model.** <one-time, subscription, pre-order, bundle, lead, quiz>
**Offer.** <summary or none>
**Primary concern.** <largest unresolved shopper question>
**Narrative.** <one sentence describing how the page earns the action>
**Section order.** 1 <id>; 2 <id>; ...
```

## Consumer Decision Model

```markdown
## Consumer decision model

**Primary visitor mode.** confirm | compare | explore | complete | replenish
**Top decision questions.**
1. <question>
2. <question>
3. <question>
**Selected behavioral patterns.** <at most three, with evidence>
**First decision area.** <facts, proof, and action shown first>
**Gallery jobs.** <covered and missing product-media jobs>
**Guided merchandising.** <relationship and products, or none>
**Risk and trust.** <proof/policy placed beside the relevant decision>
**Mobile context.** <what stays visible or repeats during long scroll>
**Hypothesis and metric.** <expected behavior change and measurement>
```

## Design Direction

```markdown
## Design direction

**Visual thesis.** <one distinctive sentence>
**Palette.** <named colors and roles from the selected theme>
**Typography.** <heading/body roles and scale>
**Layout rule.** <alignment, width, spacing, density>
**Background rule.** <one page background and any single justified exception>
**Bold moment.** <one memorable visual treatment>
**Motion intent.** none | <one purposeful moment>
**Desktop structure.** <1280 layout summary>
**Mobile structure.** <390 layout summary>
**Generic-default check.** <at least three visible differences from a generic page>
**Design-guide deviations.** none | <source line and reason>
```

The direction names visual decisions, not CSS, island props, or implementation
details.

## Section Specification

One entry per section in page order:

```markdown
## Section specification

### S1. <section id> - <consumer job>

**Decision question answered.** <question>
**Copy.**
- Eyebrow: <final text or none>
- Headline: <final text>
- Subhead: <final text or none>
- Body: <final paragraph(s)>
- Labels / bullets: <final strings or none>
- CTA: "<final label>" -> <destination/action>
- FAQ: <final question and answer pairs, or none>
**Claims.** <C# ids or none>
**Proof.** <P# ids or none>
**Offer.** <O# ids or none>
**Layout.** 1280: <structure> | 390: <stack and priority>
**Interaction intent.** none | <shopper behavior and decision inputs>
**Asset slots.** <A# ids or none with reason>
```

Copy is final and customer-facing. Every CTA has one destination. Any number,
quote, rating, timeframe, certification, guarantee, price, or policy statement
maps to a ledger or claim row.

## Proof, Offer, Message, and Claims

Proof ledger:

```markdown
## Proof ledger

| # | Type | Exact content/fact | Source | Product | Rights/date | Status | Sections |
|---|---|---|---|---|---|---|---|
```

Only verified rows may render. Quotes stay verbatim and attributed as stored.
Ratings and counts use one current source and date. Logos, certifications,
results, studies, experts, and customer imagery require source and rights.

Offer ledger:

```markdown
## Offer ledger

| # | Offer | Exact terms | Eligibility | Start/end | Mechanic | Evidence | Status |
|---|---|---|---|---|---|---|---|
```

Price, discount, gift, shipping, urgency, inventory, subscription, pre-order,
guarantee, and delivery copy must match verified merchant terms. A missing
term is not filled by inference.

For campaign-led traffic:

```markdown
## Message match

| Element | Supplied message | Page treatment | Risk |
|---|---|---|---|
| Promise | | | |
| Noun phrase | | | |
| CTA verb | | | |
| Offer | | | |
| Visual cue | | | |
```

Claim gate:

```markdown
## Claim gate

| # | Claim | Section | Status | Evidence | Final copy treatment |
|---|---|---|---|---|---|
| C1 | | | approved | P1 | ships as written |
| C2 | | | merchant evidence required | | use: "<safe final copy>" |
| C3 | | | removed | none | omitted |
```

## Asset Requirements

This block specifies production jobs. `/plan-assets` resolves them.

```markdown
## Asset requirements

| Slot | Section | Consumer job | Product/variant | Source constraint | Mobile aspect/crop/pixels | Larger-screen aspect/crop/pixels | Derivation | Composition and quiet zone | Palette/set fit | Evidence/rights | Concept ref |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | hero | establish exact product identity | product/variant ids | real-only | 4:5, 1080x1350 | 3:2, 1800x1200 | same master, art-directed crops | product left, quiet upper/right | warm neutral set | merchant catalog | none |
| A2 | story | show use context | product id | editable-real | 4:5, 1080x1350 | 3:2, 1800x1200 | extend background only if needed | real product unchanged in scene | match A1 light | merchant-owned | none |
| A3 | divider | create atmosphere | none | generation-permitted | 9:16, 1080x1920 | 16:9, 1920x1080 | separate responsive outputs | low-detail backdrop | theme palette | no third-party marks | F2 |
```

Source constraints:

- `real-only`: exact product, variant, packaging, person, customer proof,
  results, official logo, certification, press mark, or evidence image;
- `editable-real`: real authorized source may be cropped, cleaned, extended,
  background-removed, or composited without changing identity-bearing pixels;
- `generation-permitted`: background, decorative element, pattern, texture,
  or clearly synthetic editorial context allowed by policy.

Every row includes why the consumer needs it, not merely what the image looks
like. `Concept ref` remains `none` until `/visualize-page` returns an approved
frame.

## Template Direction

```markdown
## Template direction

**Mode.** page-kit | sections | custom
**Selected kit.** <slug/id or none>
**Selected sections.** <ids or none>
**Fit rationale.** <how the direction serves the planned sections>
**Required adaptations.** <layout/content changes, or none>
```

Templates are selected after sections. A missing fit results in `custom`, not
a compromised narrative.

## Open Decisions and Status

```markdown
## Open decisions

| # | Question or evidence needed | Owner | Affects | Resolution |
|---|---|---|---|---|
```

```markdown
## Plan status

**Status.** PLAN_BLOCKED | PLAN_READY_FOR_APPROVAL
**Blocking items.** none | <ids and reasons>
**Approval.** pending | PLAN_APPROVED <who> <ISO date>
```

`PLAN_BLOCKED` means a material strategy, copy, product, offer, proof, claim,
CTA, or section decision is unresolved. `PLAN_READY_FOR_APPROVAL` means every
block is complete. `PLAN_APPROVED` requires explicit approval for the exact
presented plan and authorizes neither paid generation nor page creation.

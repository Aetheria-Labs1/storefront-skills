# Page-Type Checklist Format

Every file in `references/page-types/` (except `_index.md` and this file)
describes one page type in the same shape so that `/plan-page`, `/design-page`,
`/build` and repository contract tests can read it the same way. The
heart of each file is its `## Workflow`: the ordered thinking the model follows
for that type, section by section, with the asset decision, the island
decision and the tool call that settles each. The `## Checklist` JSON is the
default anatomy the workflow produces; deviate when the context calls for it
and note the deviation in the plan. House rules in `references/design-rules.md`
still apply to every page.

## How a skill uses a page-type file

1. `/plan-page` identifies the type with `references/page-types/_index.md`,
   records the `## Page type` block in `page plan` and `page.pageType` in
   `page record`, then loads only the matching file.
2. `/plan-page` follows the file's **Workflow**: the context reads first, then
   each section in order with its media decision (search, generate, ask or
   skip), island decision and copy ceiling. The **Checklist** JSON is the
   default the workflow lands on; a deviation is written under "Deviations
   from the type default" in the plan with its reason.
3. `/design-page` re-reads the same file before writing HTML and follows the
   Workflow's island and asset decisions while composing, with **Above the
   fold**, **Proof**, **Offer and CTA**, **Imagery** and **Copy** as the
   guide. Where source and plan disagree with the checklist, it lists the
   differences in the plan and continues.
4. Review the checklist against the plan, then the persisted source and
   hosted draft. Type deviations are advisory; proof/offer violations
   block readiness. Repository fixture checks test this contract separately.

## Required prose sections, in order

```markdown
# <Page type name>

One paragraph: what the page is for, who lands on it, what they must do.

## Identify it
Signals in the brief that select this type; near neighbours and how to tell
them apart (one line each).

## Anatomy
Numbered, ordered section list using the canonical ids below. Mark each
`mandatory`, `recommended` or `conditional: <condition>`. One sentence per
section on its job.

## Workflow
The ordered thinking for this type. Three fixed sub-headings:

### Context reads
Numbered tool calls run before any section is chosen, each with what to
extract from the result (image count and which jobs they cover, variant axes
and whether colour variants have images, price and compare-at, selling plans,
inventory, review count band, theme tokens and voice, asset library inventory
by tag, ad creative for message match).

### Section by section

Link `references/workflows/_how-to-read.md` once. It supplies the shared
asset/fallback, view-and-fit, island-resolution and copy procedures.
Keep one row per Anatomy section, in order, with type-specific inputs only:

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `<section id>` | Shopper job | Needed job, tag/query, crop and specific alternative | Native content or candidate family plus decision inputs | Type-specific message or ceiling | Data that settles the decision |

Do not repeat the shared procedures or enumerate props. Planning records
functional intent; design resolves the current island schema. Default copy
ceilings remain in the copy-policy owner, with deliberate type exceptions
recorded in the plan.

### Asset budget

A table records what the catalogue and library supply, which jobs are
missing, and type-specific alternatives. Execute gaps through the shared
asset workflow rather than reproducing its question and fallback rules.
A deliberately text-only section remains valid when the type specifies it.

## Above the fold (390px)
What must be visible in the first screen on mobile, in order. What must not.

## Proof
Which proof kinds, how many modules, where they sit, minimum evidence per
kind, and what replaces them when the store has none
(`references/proof/reviews-sourcing.md`).

## Offer and CTA
CTA count, first CTA position, sticky rule, CTA copy pattern, price reveal
timing, offer types that fit and offer types that do not
(`references/offers/offer-types.md`).

## Imagery
Required image jobs, hero treatment, lifestyle vs studio balance, video rule,
slots the plan must create (`references/assets/image-jobs-by-page-type.md`).

## Copy
Framework, headline pattern, reading level, length ceiling per section,
vocabulary constraints (`references/copy/copy-frameworks.md`).

## Never
Type-specific failures, one line each, each checkable.

## Examples
Two or three real pages with URLs and one line on what they do well.

## Checklist
One fenced ```json block, schema below.

## Sources
URLs.
```

## Checklist JSON schema

```json
{
  "page_type": "advertorial",
  "aliases": ["editorial pre-sell", "native article"],
  "funnel_stage": ["tof", "mof"],
  "awareness": ["problem-aware", "solution-aware"],
  "traffic": ["meta", "tiktok", "native"],
  "sections": { "min": 8, "max": 12 },
  "mandatory_sections": ["hero", "hook", "problem", ["mechanism", "how-it-works"], "reviews", "offer-bridge", "faq", "closing-cta"],
  "recommended_sections": ["dateline", "founder-note", "guarantee"],
  "forbidden_sections": ["announcement", "header", "product-grid", "countdown", "stock-indicator"],
  "nav": "none",
  "price_above_fold": "forbidden",
  "cta": { "min": 1, "max": 3, "first_after_section": 4, "sticky": "optional", "copy_pattern": "next-step" },
  "proof": { "min_modules": 2, "max_modules": 4, "required_kinds": ["review-quote"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count"] },
  "imagery": { "required_jobs": ["identity", "in-use", "result-or-context"], "hero": "editorial-lifestyle", "video": "optional", "min_images": 4 },
  "copy_framework": ["story-lead", "pas"],
  "offer_compat": { "allowed": ["first-order", "bundle", "free-shipping"], "forbidden": ["flash-sale", "clearance", "percent-off"] },
  "urgency": "none"
}
```

Field rules:

- `mandatory_sections`, `recommended_sections`, `forbidden_sections`: canonical
  ids from the vocabulary below. An inner array means "any one of these".
  A manifest section id `x` satisfies id `y` when `x == y` or `x` starts with
  `y + "-"` (so `reviews-skin-type` satisfies `reviews`).
- `nav`: `none` (logo only, not clickable), `minimal` (logo + one utility
  link), `full`.
- `price_above_fold`: `required`, `optional`, `forbidden`.
- `cta.first_after_section`: 0 means the first CTA is in the hero.
- `cta.sticky`: `required`, `optional`, `forbidden`.
- `cta.copy_pattern`: `add-to-cart`, `claim-offer`, `next-step`,
  `start-quiz`, `join-waitlist`, `subscribe`, `shop-collection`,
  `read-results`.
- `proof.*_kinds`: from the proof vocabulary below.
- `imagery.hero`: `packshot`, `product-in-hand`, `product-in-context`,
  `editorial-lifestyle`, `video-poster`, `typographic`, `grid`,
  `ugc-screenshot`. Before/after media never leads a hero
  (`references/proof/proof-ledger.md`, display rule 9).
- `imagery.video`: `required`, `optional`, `forbidden`.
- `copy_framework`: `pas`, `aida`, `bab`, `4ps`, `fab`, `story-lead`,
  `listicle`, `comparison`, `hook-story-offer`, `answer-first`,
  `qualifier-lead`.
- `offer_compat.allowed` / `forbidden`: offer ids from
  `references/offers/offer-types.md`, exactly: `none`, `percent-off`,
  `fixed-off`, `bogo`, `gwp`, `free-shipping`, `tiered-volume`, `bundle`,
  `bundle-decoy`, `subscribe-save`, `first-order`, `referral`, `loyalty`,
  `cashback`, `bnpl`, `trial-sample`, `mystery`, `pre-order-price`,
  `price-lock`, `flash-sale`, `clearance`, `limited-edition`, `gift-card`,
  `student-military`, `charity`. Hero placement and countdown rules are not
  offer ids; they live in `price_above_fold` and `urgency`.
- Campaign ids (manifest `campaign.type`) come from
  `references/offers/campaign-calendar.md`: `evergreen`, `launch`, `restock`,
  `seasonal`, `gifting`, `flash-sale`, `clearance`, `collab-drop`,
  `anniversary`, `cause`, `back-to-school`, `bfcm`, `end-of-season`,
  `founder-sale`.
- `urgency`: `none`, `verified-only`, `encouraged` (still verified).
- Every checklist value is the type's default, not a hard limit. A plan that
  deviates records the field, the new value and the reason under
  "Deviations from the type default".
- `awareness`: `unaware`, `problem-aware`, `solution-aware`,
  `product-aware`, `most-aware`.
- `funnel_stage`: `tof`, `mof`, `bof`, `retention`.

## Canonical section id vocabulary

Use these ids (or `id-suffix`) in plans, manifests and `<!-- section: id -->`
delimiters. Add a new id only by adding it here.

| Group | Ids |
|---|---|
| Chrome | `announcement`, `header`, `footer`, `sticky-cta`, `legal` |
| Opening | `hero`, `dateline`, `hook`, `toc`, `qualifier` (who this is / is not for) |
| Trust strip | `trust-bar` (shipping, returns, guarantee facts), `press-marquee` (linked media logos), `stats` (verified numbers), `certifications` |
| Narrative | `problem`, `agitation`, `discovery`, `story`, `founder-note`, `about`, `values`, `mission` |
| Explanation | `solution`, `mechanism`, `how-it-works`, `benefits`, `features`, `ingredients`, `specs`, `materials`, `sourcing`, `science`, `methodology`, `routine`, `usage`, `results-timeline` |
| Product | `gallery`, `buy-box`, `product-hero`, `variant-picker`, `size-guide`, `product-grid`, `product-spotlight`, `list-item`, `lookbook`, `shop-the-look`, `cross-sell`, `bundle-builder`, `quantity-breaks`, `subscription-toggle`, `plan-selector` |
| Offer | `offer`, `offer-bridge` (advertorial hand-off to product), `pricing`, `savings-math`, `gift-options`, `delivery-cutoff`, `countdown`, `stock-indicator`, `bnpl-line`, `shipping-returns`, `guarantee`, `payment-options` |
| Proof | `review-summary` (stars + count), `reviews`, `testimonial-spotlight`, `ugc-grid`, `video-testimonials`, `before-after`, `expert-endorsement`, `press-quotes`, `case-study`, `awards`, `community-count` |
| Comparison | `comparison`, `us-vs-them`, `alternatives`, `verdict`, `winner` |
| Interaction | `quiz`, `quiz-results`, `product-finder`, `calculator`, `video`, `shoppable-video`, `email-capture`, `sms-capture`, `waitlist-form`, `referral-form`, `giveaway-entry` |
| Closing | `faq`, `objections`, `closing-cta`, `final-offer`, `post-purchase-next-steps`, `related-reads`, `disclaimer` |

## Proof kind vocabulary

`review-summary`, `review-quote`, `review-list`, `review-with-media`,
`external-verified-quote`, `ugc-photo`, `ugc-video`, `creator-video`, `before-after`, `expert-quote`,
`founder-note`, `press-logo-linked`, `press-quote-linked`, `certification`,
`award`, `test-data`, `customer-count`, `sales-count`, `repeat-rate`,
`guarantee`, `policy-fact`, `case-study`, `community-screenshot`,
`social-proof-popup` (never), `live-viewer-count` (never), `stock-count`
(verified only), `press-logo-unlinked` (never).

## Image job vocabulary

`identity`, `detail`, `scale`, `texture`, `in-use`, `context`, `variation`,
`included-items`, `sequence`, `result-or-context`, `ingredient-or-material`,
`packaging`, `founder-or-team`, `ugc`, `diagram`, `comparison-visual`,
`gift-presentation`, `size-reference`, `swatch`, `label-or-facts-panel`.

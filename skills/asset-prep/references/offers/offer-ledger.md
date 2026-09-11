# Offer Ledger

Any price other than the current list price, any discount, bundle saving,
gift, free shipping promise, delivery date, countdown, stock statement or
subscription term is a row in the plan's `## Offer ledger` before design.
`/design-page` renders offers only from ledger rows; `/generate` fails
production QA on an unledgered offer element; a countdown or stock indicator
without a verified row is removed. Types and legality live in
`references/offers/offer-types.md`, `references/offers/price-presentation.md`
and `references/offers/urgency-scarcity.md`.

## The block

```markdown
## Offer ledger

**Offer type.** bundle (offer-types id)
**Summary.** Starter Kit: serum + cleanser + SPF, ₹2,499 vs ₹3,297 separately
**Confirmed by.** merchant (Aditi, email 2026-09-08)

| # | Item | Value shown on page | Basis | Confirmed | Status |
|---|---|---|---|---|---|
| O1 | bundle price | ₹2,499 | Shopify bundle product gid://.../456 | catalog 2026-09-10 | verified |
| O2 | compare-at | ₹3,297 | sum of component list prices, all currently sold at list | catalog 2026-09-10 | verified |
| O3 | savings | Save ₹798 (24%) | O2 - O1 | computed | verified |
| O4 | per-day price | ₹83/day | O1 U+00F7 30-day supply on label | label photo | verified |
| O5 | end date | none | evergreen bundle | merchant | verified |
| O6 | stock statement | none | not planned |  -  |  -  |
| O7 | shipping | Free shipping over ₹999 | store policy page URL | fetched | verified |
| O8 | delivery estimate | 2-5 days, pincode-based | DeliveryEstimate island, live | live | verified |
| O9 | code | none needed | automatic bundle price | merchant | verified |
| O10 | exclusions / stacking | not with WELCOME15 | merchant | merchant | verified |
| O11 | regions | India only | store markets | catalog | verified |
| O12 | subscription terms | none |  -  |  -  |  -  |
| O13 | guarantee | 30-day returns, unopened | policy URL | fetched | verified |
| O14 | BNPL | none | store payment methods | catalog |  -  |
```

Columns:

- **Item**: one of the fixed rows above. Keep the row with ` - ` when not
  applicable; do not delete rows, so reviewers see what was considered.
- **Value shown on page**: the exact string the page will display, in the
  store currency and locale.
- **Basis**: where the number comes from (catalog price, policy URL, label,
  computation, merchant document).
- **Confirmed**: source and date. Prices and availability come from
  `lexsis_catalog.get` on the planning day and are re-read in
  `/design-page` and `/generate`.
- **Status**: `verified`, `pending` (not rendered), ` - ` (not applicable).

## Rules the ledger enforces

1. **Compare-at needs a basis.** A struck-through price is the genuine
   recent selling price (the product's Shopify compare-at with a recorded
   history, or the sum of components sold at list). No basis, no
   strike-through. Every `<s>`, `<del>` or compare-at element carries
   `data-source="compare_at_price"` or the ledger row id (`data-source="O2"`)
   so the source/hosted review O12 can trace it. Jurisdiction rules are in
   `references/offers/price-presentation.md`.
2. **Savings are computed, not typed.** Show currency first, percent only
   when the rule for the type allows (`offer-types.md`). Never a percent
   with no amount on high-ticket goods.
3. **Urgency needs a verified end or a live read.** `endsAt` is an ISO
   datetime with timezone that the merchant confirmed; countdowns bind to
   it and disappear after it. `endsAt` is the ledger's field name; the
   CountdownTimer island's required prop is `endDate`, so the ledger value is
   what you write into `endDate`. Confirm the prop name against
   `lexsis_design` action `island_schema` before authoring. Stock statements come only from a live
   inventory binding. Neither may appear in static copy.
4. **Terms travel with the offer.** Exclusions, stacking, regions, code,
   minimum spend and subscription cancellation terms are visible within one
   scroll of the offer, not only in a footer.
5. **Shipping and tax language is the store's.** Threshold, regions,
   estimate source, tax-inclusive wording (GST-inclusive for India) come
   from store settings or the policy page URL.
6. **One offer per page** unless the type is `sale-clearance-flash` or
   `seasonal-gifting`. A second offer needs its own ledger block and a
   reason.
7. **Manifest mirror.** `offer.type`, `offer.summary`, `offer.endsAt`,
   `offer.stockVerified`, `offer.compareAtBasis` in `page record`.

## Claims to confirm before design (ask once, together)

- Exact price, compare-at and its basis.
- Start and end (date, time, timezone) or "evergreen".
- Stock basis for any scarcity statement.
- Code, automatic or both; case; single use.
- Exclusions, stacking with other codes, minimum spend, quantity caps.
- Regions and currencies.
- Shipping threshold and estimate source; delivery cutoffs for occasions.
- Gift-with-purchase item, value, while-supplies-last handling.
- Subscription cadence, discount, first-order terms, cancellation path,
  renewal notice.
- BNPL providers actually enabled on the store.
- Guarantee and returns terms as written on the policy page.

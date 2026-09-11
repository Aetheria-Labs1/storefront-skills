# AOV levers

Cross-sells, upsells, quantity breaks, progress bars, bundles, subscription
toggles and instalments: where each sits, when it eats the primary
conversion, its guardrails, and how to measure it. Every lever is judged on
revenue per session and contribution margin per order, never on AOV or take
rate alone. Offer ids are from `references/offers/offer-types.md`; price
wording from `references/offers/price-presentation.md`; relationship names
from `references/consumer-behavior-cro.md` (Relationship-based
merchandising); cart placements from `references/cart-composition.md` and
`references/cart-profile-management.md`. Pre-ticked add-ons and other dark
patterns are covered in `references/anti-patterns/dark-patterns.md`.

## Benchmarks

| Touchpoint | Acceptance or effect | Caveat | Tag | Source |
|---|---|---|---|---|
| Post-purchase one-click upsell | 3 to 8% acceptance; ReConvert 2023 (16.9M offers): 4.7% average, top 5% of stores 28.3%, AOV +5.6% | Gross take rate overstates lift (see Measurement) | OPERATOR | https://www.growthsuite.net/resources/shopify-upsell-cross-sell/complete-guide/benchmarks ; https://upsell.com/blog/the-impact-of-post-purchase-upselling-2023 |
| Post-purchase, full-price offer | 17.89% acceptance, beating small-discount offers; acceptance rises at steps 2 and 3; downsells recovered $25.7M from declines (AfterSell 2026) | Self-selection; relevance beats depth | OPERATOR | https://www.aftersell.com/2026-revenue-report |
| Cart drawer upsell | 2 to 5% acceptance; the cart generates about 4x more revenue per session than checkout; single-offer placements convert 53% better (2.55% vs 1.67%) while multi-offer placements carry 58% higher AOV ($21.44 vs $13.55) | Pick one metric before choosing single or multi | OPERATOR | https://www.aftersell.com/2026-revenue-report |
| Checkout upsell (Plus) | 1 to 4% | Lowest of the touchpoints | OPERATOR | Growthsuite benchmarks above |
| PDP frequently bought together | 1 to 3%; automated recommendations 3.8% vs manual 1.56% | Manual wins only with a named relationship and verified compatibility | OPERATOR | Growthsuite benchmarks above |
| Free-shipping progress bar | AOV +3 to +11% in 9 of 14 stores; flat in 2; negative revenue per session in 3; 1.5x AOV threshold best; static banner beat animated bar in 2 of 3 arms | The lever can go negative; needs a holdout | OPERATOR | https://www.72technologies.com/blog/free-shipping-threshold-bar-ab-test-results |
| Bundles and post-purchase upsells together | "routinely add 15 to 25%" to AOV across 170+ brands (Statlas) | Directional | OPERATOR | https://www.linkedin.com/posts/taylor-holiday-a169b322_we-track-store-and-analyze-conversations-activity-7471272309199265792-Xc7H |
| Quantity break decoy | Removing the 2-pack decoy dropped 3-pack sales 15 to 25% | Single operator source | OPERATOR | https://www.acceleroi.com/blog/psychology-of-pricing |
| Subscribe and save | Subscribers place about 3x more orders than one-time buyers (Recharge, 20,000 brands) | Selection effect; measure retention at 90 days | OPERATOR | https://getrecharge.com/reports/subscription-trend-report-2026/ |
| BNPL under price | 15 to 30% higher AOV on qualifying carts; 5 to 12% checkout conversion lift; +9% instalment selection when moved from below add-to-cart to under price | Operator-reported; BNPL cohorts may repurchase 8 to 14% less (unverified) | OPERATOR | https://digitalheroesco.com/journal/shopify-afterpay-klarna-shop-pay-integration/ ; https://d2c-times.com/shopifys-shop-pay-installments-surge-is-rewriting-dtc-checkout-economics/ |

## Levers

### Frequently bought together (PDP cross-sell)

| Field | Rule |
|---|---|
| Where | `cross-sell` section below `buy-box`, never between price and add-to-cart; at most three items, each priced below the hero item |
| Name the relationship | Use a relationship from `consumer-behavior-cro.md` (Complete the Routine, Make It Work, Fit Kit, Refill the Stack) and state why each item belongs; record the relationship kind (complementary, compatible, sequential, protective, replenishing) in the plan's Guided merchandising line; never "Recommended for you" |
| Cannibalises when | It sits above the fold, competes with the hero price, or offers a cheaper substitute for the hero SKU |
| Guardrails | Nothing pre-checked (offer-types OF6); compatibility only from verified mappings (model, shade, size), never from visual similarity; inline add without leaving the page; suppress out-of-stock items |
| Measure | Attach rate and PDP add-to-cart rate side by side; a rise in attach with a fall in hero add-to-cart is cannibalisation |

### Quantity breaks

| Field | Rule |
|---|---|
| Where | `quantity-breaks` in the purchase block, 1, 2 and 3 units with per-unit price per tier (`offer-types.md` `tiered-volume`) |
| Cannibalises when | The single unit is de-emphasised or the multi-pack is default; visitors who wanted one unit leave |
| Guardrails | Single unit selected by default; at most four tiers; higher tier always cheaper per unit; the single price is the real selling price (price-presentation PP1); no "MOST POPULAR" ribbon (design-rules N9) |
| Measure | Units per order and conversion rate together; tier mix over time |

### Bundle and save

| Field | Rule |
|---|---|
| Where | On a `pdp`, a `bundle-builder` or `cross-sell` below the buy box offering the set; on `bundle-kit` pages the set is the hero with `savings-math` mandatory (offer-types OF4) |
| Cannibalises when | The bundle replaces the single-SKU buy box on a page whose traffic wanted one item; or the bundle's per-item price beats the single price by so much that single-SKU margin evaporates |
| Guardrails | Individually selectable items; "vs buying separately" line from components sold at those prices (PP1); currency saving first over $100 (OF2); no padding with low-value items; at most six slots in build-your-own |
| Measure | Bundle attach rate, AOV, first-order contribution margin, and single-SKU conversion on the same page |

### Subscribe and save toggle

| Field | Rule |
|---|---|
| Where | `subscription-toggle` inside `buy-box`: one-time and subscribe prices side by side, cadence selector, "skip, swap or cancel anytime", renewal price and cadence above the button |
| Cannibalises when | Subscribe is pre-selected (one-time buyers abandon), or the intro discount is so deep that churn follows the first renewal |
| Guardrails | One-time selected by default; separate un-ticked consent for recurring billing (ROSCA; India "subscription trap"); cancellation path stated on the page; selling plan must exist on the product in Shopify (a profile cannot make an ineligible product subscribable, `cart-composition.md`) |
| Measure | Subscription attach rate, 90-day retention, first-order margin after discount |

### Free-shipping progress bar

| Field | Rule |
|---|---|
| Where | Cart profile `Free-shipping progress` module pinned to the top of the drawer on mobile; `announcement` states the threshold sitewide; `shipping-returns` line in `buy-box` |
| Cannibalises when | The threshold sits far above AOV (1.8x raised abandonment in the 14-store test); the bar resets between pages; the animation distracts (static beat animated in 2 of 3 arms) |
| Guardrails | Threshold 1.3 to 1.5x AOV and above the margin floor (all-in shipping cost divided by gross margin); one number across page, bar and checkout (PP17); progress fill plus amount remaining, not a percent; stacked rewards (shipping, then gift, then discount) only when thresholds are about one add-on apart; disable code stacking on top of the threshold or set it so the combined offer clears margin |
| Measure | Revenue per session and contribution margin per order with a holdout; AOV alone hid the 3 negative stores |

### Cart upsell

| Field | Rule |
|---|---|
| Where | Cart profile offer slot at `after_lines` (below the progress bar, above checkout); one offer, low price point, relevant to the lines in cart; `RELATED` or `COMPLEMENTARY` intent or a manual GID |
| Cannibalises when | It sits above the lines or beside the checkout button; more than one offer when conversion is the goal; a substitute for a carted item |
| Guardrails | Un-ticked "Add" button; no modal that blocks checkout; one offer for conversion, up to three only when AOV is the stated goal and the holdout confirms revenue per session; never a discount code the visitor has not seen |
| Measure | Cart-to-checkout rate and revenue per session; attach rate is secondary |

### Post-purchase one-click upsell

| Field | Rule |
|---|---|
| Where | `thank-you-post-purchase` page, `post-purchase-next-steps` first (delivery, setup, support), then one offer and one downsell; not on the order-status page later |
| Cannibalises when | Rarely; the primary conversion is banked. It harms trust when the offer is irrelevant, pre-selected, or the decline is smaller or greyed |
| Guardrails | One offer plus one downsell, relevant to the purchased item; "No thanks" at equal visual weight (confirmshaming is a listed dark pattern); consent language "Add to my order for $X"; offer the most relevant item at full price before a discounted one (full-price offers converted at 17.89%); native Shopify Buy X Get Y does not apply here |
| Measure | Incremental AOV against a holdout that sees no offer (see Measurement); acceptance rate alone is misleading |

### BNPL line

| Field | Rule |
|---|---|
| Where | `bnpl-line` directly under the price in `buy-box`; provider logos in `payment-options` or `trust-bar` |
| Cannibalises when | The instalment figure is larger or brighter than the total (visitors anchor on the split and abandon at checkout when the total appears); shown under the provider floor; three providers create choice fatigue |
| Guardrails | Total first, then split, count, provider, interest (PP23); at most two providers (PP24); floor respected; luxury pages keep it discreet and below price or omit it (offer-types OF3) |
| Measure | Conversion on carts above the floor and AOV; repeat rate by payment cohort at 90 days |

## Measurement

Take rate and "upsell revenue" overstate lift because some accepted items
replace spend the visitor would have made anyway; a worked example showed
$2.70 true incremental AOV against $3.30 implied (Daymark). Procedure:

1. Assign visitors (or orders, for post-purchase) to treatment and holdout at the session level, 90/10 or 80/20, sticky for the session.
2. Holdout sees the page or cart with the lever removed and nothing in its place.
3. Primary metric: revenue per session (page and cart levers) or incremental revenue per order (post-purchase). Secondary: contribution margin per order, conversion rate, attach rate, refund rate at 30 days.
4. Run to the sample size the `references/ab-testing.md` procedure requires; do not stop on the first positive day.
5. Segment by device, new versus returning, and traffic source; mobile AOV runs 20 to 30% below desktop, so a threshold that works on desktop can fail on mobile.
6. Record the result in the plan's Hypothesis and metric line and in `qa-report.md`; a lever whose holdout shows flat or negative revenue per session is removed, whatever the attach rate.

## Rules

AO1. Judge every lever on revenue per session and contribution margin per order; never ship or keep a lever on AOV or take rate alone. OPERATOR.
Check: the plan's Hypothesis and metric line names revenue per session or contribution margin for any AOV lever.

AO2. Never place an upsell, cross-sell or progress bar between price and add-to-cart, in the checkout payment step before the total, or as a modal that blocks add-to-cart or checkout. HEURISTIC and RESEARCH (Baymard PDP research).
Check: in `buy-box`, no `cross-sell`, `quantity-breaks` other than the purchase quantity, or offer element appears between the price element and the add-to-cart button; no `role="dialog"` triggered on add-to-cart.

AO3. One upsell surface per stage: PDP (`cross-sell`), cart (one offer slot), post-purchase (one offer plus one downsell). Not all three on one screen. HEURISTIC.
Check: at most one of `cross-sell`, `bundle-builder`, `quantity-breaks` renders in the first viewport below the buy box; the cart profile has at most one enabled offer slot when the goal is conversion.

AO4. Name the relationship for every recommendation and record its kind; never "Recommended for you" or "You may also like". HEURISTIC (`consumer-behavior-cro.md`).
Check: `grep -ciE 'recommended for you|you may also like|customers also bought' $W/lexsis-source.html` is 0; the plan's Guided merchandising line names the relationship and kind.

AO5. Nothing is pre-selected: no default multi-pack, no default subscription, no pre-checked add-on, wrap, insurance or donation. LAW (India CCPA basket sneaking; ROSCA; EU CRD Art 22).
Check: offer-types OF6 grep; `subscription-toggle` default state is one-time; `quantity-breaks` default is one unit.

AO6. Compatibility claims come from verified mappings, never from visual similarity; incompatible or out-of-stock items are suppressed. HEURISTIC (`consumer-behavior-cro.md`, Compatibility confidence).
Check: the plan's Compatibility answer names the mapping source (catalog metafield, merchant document) or the cross-sell is limited to complementary, not compatible, items.

AO7. The free-shipping threshold is one number across the page, the cart bar and checkout, set at 1.3 to 1.5x AOV and above the margin floor, shown as fill plus amount remaining. OPERATOR and LAW (PP17).
Check: `commerce_config.free_shipping_threshold` equals the ledger `shipping` row and the store shipping rate; bar copy matches `Add [₹$£€][0-9,]+ more for free shipping`.

AO8. Cap the visible recommendation set at three on the PDP and one in the cart drawer when conversion is the goal. HEURISTIC and OPERATOR (Chernev 2003 choice overload; AfterSell single-offer data).
Check: `cross-sell` renders at most three items; cart profile offer slot `max_items` is 1 unless the plan states AOV as the goal with a holdout.

AO9. Post-purchase offers show a full-price relevant item first, one downsell on decline, and a "No thanks" of equal weight; no confirmshaming copy. OPERATOR and LAW.
Check: `grep -ciE 'no, i (like|prefer|want to)|no thanks, i' $W/lexsis-source.html` is 0; the decline control has the same font size and contrast as the accept control.

AO10. Measure every lever against a holdout before it is kept; a flat or negative revenue-per-session result removes it regardless of attach rate. OPERATOR (72technologies; Daymark).
Check: `qa-report.md` or the `/ab-test` record shows a holdout arm and revenue per session for the lever.

AO11. Subscribe-and-save shows one-time and subscription prices side by side, one-time selected, renewal terms and cancellation path above the button, and a separate un-ticked consent. LAW (ROSCA; UK DMCC subscription rules; India CCPA).
Check: `subscription-toggle` contains both prices, the cadence, and a string matching `cancel`; no `checked` attribute on the subscribe option.

AO12. Instalments follow price-presentation PP23 and PP24: total first, at most two providers, above the floor, never larger than the total. LAW and OPERATOR.
Check: PP23 and PP24 checks pass.

AO13. Disable discount-code stacking on top of the free-shipping threshold, or set the threshold so the combined offer still clears the margin floor. OPERATOR.
Check: the ledger `exclusions / stacking` row states whether codes combine with the shipping threshold; Shopify combination classes match.

## Sources

- Growthsuite upsell and cross-sell benchmarks: https://www.growthsuite.net/resources/shopify-upsell-cross-sell/complete-guide/benchmarks
- ReConvert post-purchase upsell 2023: https://upsell.com/blog/the-impact-of-post-purchase-upselling-2023
- AfterSell 2026 revenue report (cart vs checkout, single vs multi offer, full-price post-purchase, downsells): https://www.aftersell.com/2026-revenue-report
- Daymark on post-purchase incrementality and holdouts: https://www.usedaymark.io/blog/post-purchase-upsell-measurement
- 72technologies free-shipping bar 14-store test: https://www.72technologies.com/blog/free-shipping-threshold-bar-ab-test-results ; margin floor formula: https://resources.rework.com/libraries/ecommerce-growth/free-shipping-thresholds ; stacked rewards bar: https://cartylabs.com/blog/shopify-free-shipping-bar-strategy/
- Statlas AOV and bundle data (Taylor Holiday): https://www.linkedin.com/posts/taylor-holiday-a169b322_we-track-store-and-analyze-conversations-activity-7471272309199265792-Xc7H
- AccelerOI quantity-break decoy: https://www.acceleroi.com/blog/psychology-of-pricing ; Chernev 2003: https://ideas.repec.org/a/oup/jconrs/v30y2003i2p170-83.html
- Recharge subscription trend report 2026: https://getrecharge.com/reports/subscription-trend-report-2026/ ; Recharge 2022 on intro-discount churn: http://getrecharge.com/downloads/state-of-subscription-commerce-report-2022.pdf
- BNPL placement and cohort notes: https://digitalheroesco.com/journal/shopify-afterpay-klarna-shop-pay-integration/ ; https://d2c-times.com/shopifys-shop-pay-installments-surge-is-rewriting-dtc-checkout-economics/ ; https://d2c-times.com/is-shop-pay-installments-still-the-bnpl-leader-dtc-brands-trust-in-2026/
- Baymard product page and cross-sell research: https://baymard.com/research/product-page
- Shopify recommendation intents: https://shopify.dev/docs/apps/build/product-merchandising/recommendations
- India CCPA Dark Patterns 2023 (basket sneaking, confirmshaming): https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf ; FTC ROSCA guidance: https://www.ftc.gov/business-guidance/blog/2024/10/click-cancel-ftcs-amended-negative-option-rule-what-it-means-your-business

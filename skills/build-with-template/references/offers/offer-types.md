# Offer types

The canonical offer catalogue. `page-manifest.json` `offer.type` takes exactly
one id from this file; page-type checklists list the same ids under
`offer_compat`. Every offer renders only from a verified row in the plan's
`## Offer ledger` (`references/offers/offer-ledger.md`). Price display rules
live in `references/offers/price-presentation.md`, urgency rules in
`references/offers/urgency-scarcity.md`, stage rules in
`references/offers/funnel-stages.md`, dark patterns in
`references/anti-patterns/dark-patterns.md`.

Tags: LAW (statute or regulator text), RESEARCH (peer-reviewed or large
sample), OPERATOR (practitioner data, directional), HEURISTIC (rule of thumb).
Section ids come from `references/page-types/_checklist-format.md`.

## Catalogue

### `none`
- Use when: luxury or prestige positioning; launches at full price; retargeting where the objection is not price; any page whose ledger has no verified offer row.
- Anatomy delta: no `offer`, `savings-math`, `countdown`, `stock-indicator`, `final-offer`. `trust-bar` carries shipping, returns and guarantee facts only.
- Math: list price alone; unit price in `specs` where law requires it (PP8).
- LAW: general price rules only (`price-presentation.md`).
- Anti-patterns: inventing a "value" or "worth" line to fill the gap; a fake compare-at to make list price look reduced.
- Metric: conversion rate. CTA: "Add to cart" ("Add to bag" for fashion and beauty).

### `percent-off`
- Use when: unit price under about $100 or ₹8,000 (RESEARCH, Rule of 100); catalogue-wide sale; mass or mid-market positioning. OPERATOR: 20% was the redemption and AOV sweet spot in Seguno's unique-code benchmark; 10% had the worst redemption (0.20%).
- Anatomy delta: `announcement` with depth and end date; struck compare-at plus sale price on every price instance in `buy-box` and `pricing`; `savings-math` line with currency saved; `legal` offer footnote within one scroll of the first price.
- Math: compare-at, sale price, computed currency saving. EU: percent computed from the 30-day lowest prior price (PP2).
- LAW: compare-at basis required in every market (PP1 to PP5). FTC 16 CFR 233.1: a nominal reduction may not be called a sale.
- Anti-patterns: perpetual sale; stacking with the first-order code; percent alone on goods over the Rule-of-100 line; ALL-CAPS "% OFF" pills (design-rules N9); any percent on a luxury page (OF3).
- Metric: conversion rate and contribution margin per order. CTA: "Add to cart"; headline "[depth] off [scope], ends [date]".

### `fixed-off`
- Use when: unit price over about $100 or ₹8,000; win-back; when a minimum-spend threshold is wanted. OPERATOR: minimum spend on amount-off codes correlated with 2.6x AOV ($100.79 vs $39.30, Seguno).
- Anatomy delta: as `percent-off`, plus a threshold line beside the offer ("$30 off orders over $150") and a cart progress indicator toward the threshold (cart profile, `references/cart-composition.md`).
- Math: currency off beside the price; in cart, the remaining amount to unlock.
- LAW: same compare-at rules; threshold and exclusions adjacent to the offer, not in a footnote (FTC 251.1 proximity by analogy; India CCPA drip pricing).
- Anti-patterns: threshold more than 50% above AOV; amount-off on items under $30 (reads small); threshold that differs from the checkout rule.
- Metric: AOV lift against a holdout, redemption rate. CTA: "Add to cart"; headline "Save $[n] on [product] this week".

### `bogo`
- Use when: product cost is low relative to price (OPERATOR, CTC: at 13 to 18% COGS a BOGO is a better take rate than 25% off and a bigger perceived offer); moving a second SKU or slow stock; consumables.
- Anatomy delta: `offer` names both items with images; `buy-box` shows the free line at 0 with a strike; an explicit "add both to cart" instruction because native Shopify Buy X Get Y never auto-adds the get item.
- Math: present as quantity gained, not percent saved (RESEARCH, Chen et al. 2012: bonus pack beat the equivalent price cut); show effective per-unit price ("2 for $40, $20 each").
- LAW: FTC 16 CFR 251.1 treats "buy one get one" as a Free claim: the paid item at its regular price (lowest with substantial sales in the prior 30 days); no size runs a Free offer more than 6 months in any 12. Stock for the free item must exist.
- Anti-patterns: "BOGO 50%" with no per-unit price; a code required but not stated near the offer; a get item of lower quality; "BOGO" as a word for non-US audiences.
- Metric: units per order, contribution margin per order. CTA: "Add both to cart".

### `gwp`
- Use when: prestige positioning where a price cut damages equity; AOV lift via threshold; sampling a new SKU; giving categories (pets, kids, beauty). OPERATOR: three named, pictured gifts at a $60 threshold beat 15% off by +25% AOV in a five-arm popup test (Convertibles).
- Anatomy delta: `offer` shows the gift as a product image with its retail value; threshold line adjacent; cart progress to the gift; gift line auto-added at 0 by a Discount Function, never theme JavaScript (which drops at checkout).
- Math: gift retail value, never cost; threshold gap in cart.
- LAW: FTC 251.1: all conditions "at the outset, in close conjunction with the offer"; an asterisk to a footnote is not adequate; "gift", "bonus", "complimentary" carry the same rules. India CCPA: free samples are not basket sneaking, but the gift may not raise the total payable.
- Anti-patterns: "a free gift" with no name or picture; threshold below current AOV; dead-stock gift; banner still up after the gift sells out.
- Metric: AOV lift, gift redemption, second-purchase rate of gifted customers. CTA: "Add to cart" on the product; "Claim your free [gift]" only on the gift module.

### `free-shipping`
- Use when: unexpected shipping is the top addressable abandonment cause. RESEARCH, Baymard: 40% of non-browsing abandoners cite extra costs; 64% look for shipping cost on the product page and 43% of sites do not show it.
- Anatomy delta: `announcement` with the threshold; a `shipping-returns` line in `buy-box`; cart progress bar with remaining amount; optional gap-filler `cross-sell` priced to close the gap.
- Math: threshold 15 to 30% above AOV (HEURISTIC). OPERATOR, 72technologies 14-store test: 1.5x AOV was the best revenue-per-session point; the bar was negative on revenue per session in 3 of 14 stores; a static banner beat the animated bar in 2 of 3 arms. Margin floor: all-in shipping cost divided by gross margin percent.
- LAW: the page threshold and the checkout shipping rate are the same number. India: delivery charge sits inside the single-figure total (E-Commerce Rules 6(5)(b)).
- Anti-patterns: threshold hidden until checkout; bar that resets between pages; free shipping stacked with a sitewide percent code; threshold above mobile AOV.
- Metric: revenue per session and contribution margin per order, never AOV alone. CTA: none of its own; announcement copy "Free shipping on orders over $[n]" (India: "Free delivery above ₹[n]. Pay on delivery available").

### `tiered-volume`
- Use when: consumables and replenishables where shipping cost barely rises with units (OPERATOR, CTC).
- Anatomy delta: `quantity-breaks` in the purchase block with per-unit price per tier; cart shows the tier reached and the gap to the next.
- Math: per-unit price and total saving at each tier; the single unit is the reference price. OPERATOR: single, 2-pack, 3-pack beat single and 3-pack; removing the 2-pack dropped 3-pack sales 15 to 25% (AccelerOI).
- LAW: the single-unit price must be the real selling price (PP1). Needs an app or Discount Function on Shopify.
- Anti-patterns: more than four tiers (RESEARCH, Chernev 2003 on choice overload); a higher tier with a worse per-unit price; a multi-pack pre-selected; "MOST POPULAR" ribbon (N9).
- Metric: units per order, tier mix. CTA: "Add to cart" with the selected tier; headline "Buy 2, save 10%. Buy 3, save 20%." with per-unit price beneath.

### `bundle`
- Use when: AOV is below the paid-media break-even (OPERATOR, Statlas: median new-customer AOV $74; 35% of brands under $75 lose on the first order); the value is the set.
- Anatomy delta: `product-hero` or `bundle-builder` with component images and "what's inside"; `savings-math` mandatory ("$87 separately, $59 as a set, save $28"); `comparison` table when a good, better, best ladder exists.
- Math: sum of components, bundle price, currency saved; percent only under the Rule-of-100 line. Do not pad with a cheap item to inflate the "separately" figure (RESEARCH, Chernev: low-value components lower willingness to pay).
- LAW: compare-at for a bundle is the sum of component prices actually sold at those prices (UK CMA principles cover bundles).
- Anti-patterns: no "vs buying separately" line; build-your-own with more than six slots; components never sold individually; percent-only saving on a bundle over $100.
- Metric: AOV, bundle attach rate, first-order contribution margin. CTA: "Get the set" or "Add the bundle".

### `bundle-decoy`
- Use when: a three-option ladder where the target tier should win and the attributes can be compared in a visible table.
- Anatomy delta: `plan-selector` or `pricing` with three tiers plus `comparison` (the decoy effect needs visible attribute comparison); target tier in the middle or as the option that dominates the decoy.
- Math: RESEARCH, Simonson 1989 asymmetric dominance; the Economist replication moved bundle share 32% to 84%, but replications show 10 to 18 point shifts, so plan on that. Every tier shows price and per-unit or per-item value.
- LAW: the decoy must be a real purchasable option at the shown price; a tier nobody can buy is bait (UK DMCC bait advertising; FTC 16 CFR 238).
- Anti-patterns: decoy not clearly dominated; all three tiers look poor (repulsion effect); highlighted middle tier with "BEST VALUE" chrome (N9).
- Metric: target-tier share, revenue per visitor. CTA: "Choose [tier name]".

### `subscribe-save`
- Use when: replenishable category. OPERATOR, Recharge 2026: subscribers place about 3x more orders than one-time shoppers.
- Anatomy delta: `subscription-toggle` in `buy-box` with one-time and subscribe prices side by side; frequency selector; "skip, swap or cancel anytime" adjacent; renewal price and cadence stated before the buy button.
- Math: both prices and the saving per delivery; per-day framing allowed for consumables (RESEARCH, Gourville 1998: 52% vs 30% acceptance for the same annual cost framed daily).
- LAW: US ROSCA: material terms before billing details, express informed consent, simple cancellation (the 2024 FTC Negative Option Rule was vacated July 2025; ROSCA and state auto-renewal laws still apply). UK DMCC subscription rules phase in from 2026. India CCPA lists "subscription trap".
- Anti-patterns: subscribe pre-selected; intro discount so deep that churn follows expiry (OPERATOR, Recharge 2022); renewal price hidden; cancellation path missing from the page.
- Metric: subscription attach rate, 90-day retention, first-order margin after discount. CTA: "Subscribe and save [n]%" with renewal terms directly beneath.

### `first-order`
- Use when: cold or TOF acquisition where price is the stated objection. OPERATOR: popups with a discount convert 7.45% vs 4.60% without (Wisepops via Farabi Ulder); 10% and 20% first offers show near-identical repeat rate and LTV, so 10% is the margin-efficient default.
- Anatomy delta: `sticky-cta` bar or a timed `email-capture`; code shown in `buy-box` and pre-filled in cart; "first order" eligibility stated on the offer.
- Math: 10% under $50 AOV; free shipping or GWP over $80 AOV with over 55% margin (OPERATOR, Blossom).
- LAW: if email or SMS is collected, consent wording per market; never gate the code behind pre-ticked marketing consent (forced action, basket sneaking).
- Anti-patterns: code visible to returning customers (trains abandon-and-return); mobile popup that fails Google's interstitial guidance; deeper than the sitewide sale running at the same time.
- Metric: net revenue per new subscriber, not popup submit rate. CTA: "Add to cart"; offer line "10% off your first order" (never "Unlock").

### `referral`
- Use when: the visitor has already bought. OPERATOR, ReferralCandy: referred customers are 10.7x more likely to refer (3.27% vs 0.30%); 83% of advocates refer exactly once.
- Anatomy delta: `referral-form` on `thank-you-post-purchase` and `referral-loyalty-vip`; the referred friend's landing page states both rewards and who referred them.
- Math: both sides of the reward in currency ("Give $15, get $15"); expiry and minimum spend adjacent.
- LAW: the friend's reward is a discount or Free claim (FTC 251.1); incentivised reviews disclosed (UK DMCC banned practice 13; FTC Endorsement Guides).
- Anti-patterns: referral module on a cold page (nobody has bought); reward that is store credit with expiry but not labelled as such.
- Metric: referral order share, share-action rate. CTA: "Share your link".

### `loyalty`
- Use when: retention pages, account pages, early access. OPERATOR, CTC: give VIPs early access and exclusive drops, not a deeper discount.
- Anatomy delta: points-earned line in `buy-box` ("Earn 120 points"); tier badge; "members get early access" `announcement` shown only to logged-in visitors.
- Math: points value in currency where the programme defines it; expiry stated.
- LAW: expiry and redemption terms disclosed; India CCPA "interface interference" if points value is obscured.
- Anti-patterns: loyalty widget above the fold on TOF pages; points shown to visitors who cannot join.
- Metric: repeat rate, redemption rate. CTA: "Get early access", "Join [programme]".

### `cashback`
- Use when: India and marketplace-trained audiences; bank or UPI cashback is the dominant festive mechanic (Redseer festive 2025).
- Anatomy delta: `payment-options` strip near the price ("10% instant discount with [bank] cards, up to ₹1,500"); terms link adjacent.
- Math: cap, minimum order, and whether the cashback is instant or post-settlement.
- LAW: cashback conditions are material terms; "up to" must be achievable by a meaningful share of buyers (UK CAP "up to" standard; India CCPA misleading advertisement).
- Anti-patterns: store credit labelled cashback; bank list hidden; cap omitted.
- Metric: payment-method mix, prepaid share. CTA: none of its own; line "[n]% instant discount with [bank] cards, up to ₹[cap]. T&C."

### `bnpl`
- Use when: AOV $80 to $400 (₹3,000 and up) and considered purchases. OPERATOR: Shop Pay Installments 15 to 30% higher AOV on qualifying carts (Digital Heroes citing Shopify Editions); moving the callout from below add-to-cart to under the price lifted installment selection 9% for one brand (D2C Times).
- Anatomy delta: `bnpl-line` directly under the price in `buy-box`, not only at checkout; `payment-options` logos in `trust-bar`.
- Math: total price first, then the split, count and interest ("$99, or 4 payments of $24.75"); "0% APR" only if true; India "₹999/month x 6, no-cost EMI" with bank list and the note that interest is absorbed as a discount.
- LAW: US TILA / Reg Z triggering terms; UK FCA BNPL regulation from 2026; EU Consumer Credit Directive 2023; India RBI digital-lending guidelines. Full price always more prominent than the installment.
- Anti-patterns: installment larger than the total; BNPL as the only price; more than two providers; shown under the provider's eligibility floor.
- Metric: conversion on carts above the floor; repeat rate by payment cohort. CTA: none; the line sits under price.

### `trial-sample`
- Use when: high-consideration consumables (skincare, supplements) where the objection is "will it work for me".
- Anatomy delta: `product-hero` with the sample and the full-size price visible; shipping cost on the page; `post-purchase-next-steps` states what happens after the trial.
- Math: trial price, shipping, full-size price; if the trial converts to a subscription, renewal price and date.
- LAW: FTC 251.1: "Free" with a shipping charge needs the charge at the outset; conversion to paid needs ROSCA consent and cancellation; UK DMCC subscription rules; India "subscription trap".
- Anti-patterns: auto-enrol without a separate un-ticked consent; "free" in the headline with "$4.95 S&H" in the footer.
- Metric: trial-to-paid conversion. CTA: "Try it for $[n]" or "Get your sample".

### `mystery`
- Use when: clearance of mixed inventory to an engaged base; retention audiences.
- Anatomy delta: `offer` with "guaranteed value of at least $[n]"; category or size selector; "no returns on mystery items" stated before add-to-cart.
- Math: guaranteed value is a compare-at claim and needs a basis (PP1).
- LAW: returns exclusions disclosed pre-purchase (UK CRA 2015; India E-Commerce Rules 6(5)(g)); statutory withdrawal rights cannot be waived in the EU.
- Anti-patterns: on any TOF page; value guarantee built on inflated RRPs.
- Metric: sell-through, return rate. CTA: "Add the mystery box".

### `pre-order-price`
- Use when: a launch or restock where the visitor pays now (deposit or full) for a product that ships later.
- Anatomy delta: "Pre-order" state in `buy-box`; "Estimated to ship by [date]" beside the price and beside the button; deposit and full price shown separately; cancellation line in `shipping-returns`.
- Math: Shopify UX guidance: never strike the full price against a deposit. "Pre-order $89 (launch price $109)" is a future-price comparison and is fair only if the price actually rises afterwards (UK CTSI).
- LAW: FTC Mail Order Rule 16 CFR 435: reasonable basis for the ship date, 30 days if none stated, revised date plus cancel or refund right on delay. Shopify pre-order policy mirrors this.
- Anti-patterns: "ships soon" without a date; charging months ahead without saying so; countdown to a ship date the merchant cannot meet.
- Metric: pre-order conversion, cancellation rate. CTA: "Pre-order. Ships by [date]".

### `price-lock`
- Use when: a waitlist or subscription where the merchant promises to hold today's price for a stated period or cohort.
- Anatomy delta: `offer` line stating the locked price, duration and conditions; on `subscription` pages, "your price stays $[n] per delivery for 12 months" beside the toggle.
- Math: locked price, comparison price only if it is a real current or scheduled price.
- LAW: a price-lock is a contract term: state duration, what ends it, and what happens after. UK CTSI: an "after the promotion" price is fair only if it really rises.
- Anti-patterns: "prices going up soon" with no scheduled increase; lock that silently expires into a higher renewal.
- Metric: waitlist-to-order or subscription retention. CTA: "Lock in $[n]" or "Join the waitlist".

### `flash-sale`
- Use when: a genuinely short window (hours) and a list to notify. OPERATOR, Attentive: hours, not days; send SMS off the hour to avoid carrier congestion.
- Anatomy delta: `sticky-cta` or `announcement` with a server-side `countdown` to the real end; sale `product-grid`; price reverts automatically at zero. Requires the page-type checklist `urgency` to be `verified-only` or `encouraged`.
- Math: as `percent-off` or `fixed-off` on each card.
- LAW: UK DMCC Sch. 20, EU UCPD Annex I.7, India CCPA false urgency (`urgency-scarcity.md`). Never extend a "last chance" deadline.
- Anti-patterns: six-day "flash" sale; timer on any TOF page; timer without an `offer.endsAt`.
- Metric: revenue per send, cumulative revenue past the window (nets out pull-forward). CTA: "Add to cart"; headline "[depth] off [set] until [time] [tz]".

### `clearance`
- Use when: end of season or discontinued lines. OPERATOR, CTC: go deep on end-of-line stock late in season rather than a 70%-off site in March.
- Anatomy delta: separate "Last chance" `product-grid`; "Final sale, no returns" on card and `buy-box`; sizes remaining shown from live inventory via `stock-indicator`.
- Math: genuine compare-at per SKU; "up to X% off" only when a meaningful share of SKUs sit at the maximum (PP23).
- LAW: compare-at basis still required; "final sale" cannot remove statutory rights (UK CRA; EU 14-day withdrawal; India return-terms disclosure).
- Anti-patterns: clearance stock in the hero of an evergreen page; "up to 70%" where one SKU is 70%; any clearance on a luxury page.
- Metric: sell-through, margin recovered. CTA: "Add to cart"; card label "Final sale".

### `limited-edition`
- Use when: a real unit cap or collaboration. RESEARCH, Barton et al. 2022 meta-analysis (131 studies): scarcity effects roughly double for unfamiliar brands (0.41 vs 0.21) and are larger for high-involvement products.
- Anatomy delta: unit count in `product-hero` ("Edition of 500"); drop date and time; `waitlist-form` pre-drop; "sold out" state stays visible post-drop; no percent off, ever.
- Math: none beyond price; the counter binds to live inventory and stops at the cap.
- LAW: the cap must be true and not replenished under the same "limited" label (UK DMCC banned practice on availability; India CCPA false scarcity).
- Anti-patterns: "limited" with no number; restocking a "limited" SKU; discount on a drop.
- Metric: sell-out time, waitlist conversion. CTA: "Join the waitlist" pre-drop; "Add to cart" during; "Notify me" after.

### `gift-card`
- Use when: shipping cutoffs have passed; last-minute gifting; "they choose".
- Anatomy delta: denomination selector, schedule-send date, personal message field, no shipping line; becomes the hero of `seasonal-gifting` after the last cutoff.
- Math: face value only. Never show a gift card at a discount unless the merchant funds it.
- LAW: US CARD Act: no expiry under 5 years, fee limits; UK and EU: expiry and fees disclosed; India RBI PPI rules: minimum one-year validity.
- Anti-patterns: gift card as a hero before cutoffs have passed; "bonus" card value without terms.
- Metric: gift-card revenue share in the post-cutoff window. CTA: "Send a gift card".

### `student-military`
- Use when: a verification partner (SheerID, ID.me, UNiDAYS) is connected and the segment matters to the brand.
- Anatomy delta: verification-gated code in `offer` or `faq`; eligibility stated; hidden from segments known to be ineligible.
- Math: as `percent-off` or `fixed-off`, against the real selling price.
- LAW: never presented as a general sale; UK CMA: the reference price is still the real selling price.
- Anti-patterns: eligibility hidden until after the code fails; the gated code visible in the hero of a general page.
- Metric: verified redemptions. CTA: "Verify and save".

### `charity`
- Use when: a cause campaign with a named recipient; brand story pages. RESEARCH, Gneezy et al.: pay-what-you-want with half to charity reached 4.49% purchase at a $5.33 average and was profitable.
- Anatomy delta: "[n]% or $[n] of every order goes to [named charity]" adjacent to price; running total only if real; end date; any donation add-on un-ticked.
- Math: amount or percent per order, cap, period.
- LAW: name the charity, share, period and cap (UK CAP Code; FTC charitable-solicitation guidance; India CCPA "disguised advertisement"). India CCPA lists pre-ticked charity add-ons as basket sneaking.
- Anti-patterns: "a portion of proceeds"; cause badge on an unrelated product; discount stacked on a cause campaign.
- Metric: conversion versus the same page without the cause line, donation total. CTA: "Shop and give".

## Cross-cutting rules

OF1. One offer per page. `offer.type` holds one id; a second offer needs its own ledger block and a reason. Exempt page types: `sale-clearance-flash`, `seasonal-gifting` (offer-ledger rule 6).
Check: `grep -c '<!-- section: offer' $W/lexsis-source.html` is 0 or 1 unless `page.pageType` is exempt.

OF2. Rule of 100. Always show the currency saving (offer-ledger rule 2). Under $100 or ₹8,000 the percent may lead ("32% off, save $28"); above it currency leads and percent is optional ("Save $128 (18%)"); never a percent without the currency amount on high-ticket goods. RESEARCH: Berger; JBR 2015 three-study replication. The ₹8,000 crossover is HEURISTIC.
Check: every `savings-math` line contains a currency figure; the leading figure matches the side of the line the ledger price falls on.

OF3. Luxury never shows percent, a struck price, a timer, "sale" or "clearance". Allowed ids: `none`, `gwp`, `free-shipping` (phrased "complimentary shipping", no threshold), `limited-edition`, `pre-order-price`, `price-lock`, `loyalty`, `gift-card`. RESEARCH and OPERATOR: Kapferer and Bastien anti-laws; Langer on price volatility and equity decay.
Check: when the plan loads `references/vertical-luxury.md`, `offer.type` is in the allowed list and `grep -ciE 'sale|% off|save [$₹£€]' $W/lexsis-source.html` is 0.

OF4. Bundle, tiered and BOGO pages show their arithmetic. `bundle`, `bundle-decoy`, `tiered-volume`, `bogo` require a `savings-math` or `quantity-breaks` section whose figures are ledger rows.
Check: `offer.type` in that set implies `grep -cE '<!-- section: (savings-math|quantity-breaks)' $W/lexsis-source.html` is at least 1.

OF5. "Free", "gift", "bonus" and "complimentary" appear only when the buyer pays nothing extra and the conditions sit in the same section (LAW, FTC 16 CFR 251.1; UK banned practice; EU UCPD Annex I.20).
Check: every section containing `\bfree\b` also contains the threshold, shipping cost or eligibility text; no `*` after "free".

OF6. No pre-ticked add-on, subscription, gift wrap, insurance, donation or upsell (LAW, India CCPA basket sneaking; ROSCA; EU CRD Art 22). Detail in `references/anti-patterns/dark-patterns.md`.
Check: `grep -cE '<input[^>]*checked' $W/lexsis-source.html` is 0 outside variant pickers.

OF7. The offer moves down the page as awareness falls. On `tof` page types the offer section index is greater than the `mechanism`, `how-it-works` or `solution` index; on `bof` types the offer is in the hero (`funnel-stages.md` FS4).
Check: compare section order in `page-manifest.json` against `page.funnelStage`.

OF8. Retargeting never shows a deeper discount than the visitor already saw, and never the first-order code (OPERATOR: trains abandonment).
Check: `page.pageType` is `retargeting-warm` implies `offer.type` is not `first-order` and the ledger notes the prior offer depth.

OF9. Free-offer frequency. A size or SKU carries a Free or BOGO offer no more than 6 months in any 12, with 30 days between offers and at most three per year (LAW, FTC 251.1(h)).
Check: ledger row for `bogo` or `gwp` records the months this year the offer has run on that SKU.

OF10. Compare-at is struck-through text only; no pills, ribbons or caps (design-rules N9).
Check: design-rules N9 grep returns 0.

OF11. Promise only what the discount configuration can do. Native BXGY does not auto-add the get item; a GWP auto-add needs a Discount Function; tiered pricing needs an app or Function; shipping discounts never combine with each other; at most 25 active automatic discounts (Shopify Help).
Check: ledger row O9 names the mechanic (code, automatic, Function, app) and the page instruction matches it.

OF12. Terms travel with the offer: exclusions, stacking, regions, code, minimum spend and cancellation terms within one scroll of the first offer mention (offer-ledger rule 4).
Check: the `legal` or `disclaimer` text for the offer is in the same or the next section as the first `offer`, `pricing` or `buy-box`.

OF13. Unknown market means the strictest rule: EU 30-day prior price, UK duration and volume, India MRP display and single-figure total.
Check: `page-manifest.json` has a market list, or the ledger notes "strictest applied".

OF14. Never render an offer the merchant has not confirmed on the offer-ledger "Claims to confirm" list. Missing timing, compare-at basis or stock answers mean the price renders alone: no strike, no urgency, no scarcity.
Check: every offer-ledger row that the page uses has status `verified`.

## Offer by page type compatibility

Rows are the 30 page type ids from `references/page-types/_index.md`;
columns are the 25 offer ids in catalogue order. Cells: `yes` fits; `ask` fits
only under the condition named in the offer's entry above (merchant confirms
it, ledger records it); `no` never. A page-type file's `offer_compat` may
narrow this table but not widen it.

| Page type | none | percent-off | fixed-off | bogo | gwp | free-shipping | tiered-volume | bundle | bundle-decoy | subscribe-save | first-order | referral | loyalty | cashback | bnpl | trial-sample | mystery | pre-order-price | price-lock | flash-sale | clearance | limited-edition | gift-card | student-military | charity |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ad-landing-page | yes | ask | ask | ask | ask | yes | no | ask | ask | ask | yes | no | no | no | ask | yes | no | no | no | no | no | ask | no | no | ask |
| pdp | yes | ask | ask | ask | yes | yes | ask | yes | ask | yes | ask | ask | ask | ask | ask | ask | no | ask | ask | no | no | ask | ask | ask | ask |
| pdp-hybrid-landing | yes | ask | ask | ask | yes | yes | ask | yes | ask | yes | yes | no | no | ask | ask | ask | no | ask | no | no | no | ask | no | no | ask |
| advertorial | yes | ask | ask | no | ask | ask | no | ask | no | no | ask | no | no | no | no | yes | no | no | no | no | no | no | no | no | ask |
| listicle | yes | ask | ask | ask | ask | ask | no | yes | no | no | ask | no | no | no | ask | yes | no | no | no | no | no | no | no | no | no |
| seo-buyers-guide | yes | ask | ask | no | ask | yes | no | yes | no | no | ask | no | no | no | ask | ask | no | no | no | no | no | no | no | no | no |
| comparison-us-vs-them | yes | ask | ask | no | ask | yes | no | ask | no | ask | ask | no | no | no | ask | ask | no | no | no | no | no | no | no | no | no |
| quiz-funnel | yes | no | no | no | no | no | no | yes | ask | ask | ask | no | no | no | no | yes | no | no | no | no | no | no | no | no | no |
| bundle-kit | yes | no | yes | yes | yes | yes | yes | yes | yes | yes | ask | no | ask | ask | yes | no | no | no | no | no | no | ask | no | no | no |
| offer-page | yes | yes | yes | yes | yes | yes | yes | yes | ask | ask | yes | no | ask | yes | yes | ask | ask | ask | ask | ask | ask | ask | ask | ask | ask |
| sale-clearance-flash | yes | yes | yes | yes | yes | yes | ask | yes | no | no | no | no | yes | yes | yes | no | yes | no | no | yes | yes | no | no | ask | no |
| seasonal-gifting | yes | ask | yes | ask | yes | yes | no | yes | no | no | ask | no | ask | ask | yes | no | ask | no | no | ask | ask | yes | yes | no | ask |
| gift-guide | yes | ask | ask | no | yes | yes | no | yes | no | no | ask | no | no | ask | ask | no | no | no | no | no | no | yes | yes | no | ask |
| launch-waitlist-preorder | yes | no | no | no | yes | yes | no | yes | no | no | no | ask | yes | ask | ask | no | no | yes | yes | no | no | yes | no | no | ask |
| restock | yes | no | no | no | ask | yes | ask | ask | no | yes | no | no | ask | ask | ask | no | no | no | ask | no | no | ask | no | no | no |
| subscription | yes | no | no | no | yes | yes | ask | yes | yes | yes | yes | ask | yes | no | no | yes | no | no | yes | no | no | no | no | no | no |
| ugc-creator-collab | yes | ask | ask | no | yes | yes | no | yes | no | no | yes | no | no | no | ask | yes | no | ask | no | no | no | yes | no | no | no |
| video-sales-page | yes | ask | ask | no | ask | ask | no | yes | no | no | ask | no | no | no | ask | yes | no | no | no | no | no | ask | no | no | no |
| brand-story-founder | yes | no | no | no | no | ask | no | no | no | no | ask | ask | ask | no | no | no | no | no | no | no | no | ask | no | no | yes |
| ingredient-science | yes | no | no | no | no | yes | no | ask | no | ask | ask | no | no | no | no | ask | no | no | no | no | no | no | no | no | no |
| collection-landing | yes | ask | ask | ask | yes | yes | no | yes | no | no | ask | no | ask | ask | ask | no | no | no | no | ask | ask | ask | no | no | ask |
| homepage | yes | ask | ask | ask | yes | yes | no | yes | no | no | ask | ask | yes | ask | no | ask | no | ask | no | ask | ask | ask | ask | ask | ask |
| lookbook-shop-the-look | yes | no | no | no | ask | yes | no | yes | no | no | ask | no | no | no | ask | no | no | no | no | no | no | ask | no | no | no |
| lead-capture-giveaway | yes | no | no | no | ask | ask | no | no | no | no | yes | ask | no | no | no | ask | no | no | no | no | no | ask | no | no | ask |
| referral-loyalty-vip | yes | no | no | no | no | yes | no | no | no | no | no | yes | yes | no | no | no | ask | no | no | no | no | yes | ask | ask | no |
| retargeting-warm | yes | yes | yes | yes | yes | yes | yes | yes | ask | yes | no | no | yes | yes | yes | yes | ask | no | ask | ask | ask | yes | no | ask | no |
| thank-you-post-purchase | yes | no | no | no | no | no | no | no | no | ask | no | yes | yes | no | no | no | no | no | no | no | no | no | no | no | ask |
| faq-support-led | yes | no | no | no | no | yes | no | no | no | no | no | no | ask | no | ask | no | no | no | no | no | no | no | ask | ask | no |
| trial-sample | yes | no | no | no | no | yes | no | no | no | ask | no | no | no | no | no | yes | no | no | no | no | no | no | no | no | no |
| wholesale-b2b | yes | no | no | no | no | ask | yes | ask | ask | no | no | no | no | no | no | ask | no | no | ask | no | no | no | no | no | no |

Reading notes: `ask` on TOF types (`ad-landing-page`, `advertorial`,
`listicle`, `video-sales-page`) always means below the fold and after the
mechanism (OF7). `ask` for `percent-off` and `fixed-off` on `pdp`,
`seo-buyers-guide` and `collection-landing` means a verified compare-at basis
exists for every discounted entry. `ask` on `retargeting-warm` for `mystery`
and `clearance` means existing customers only. `charity` on
`thank-you-post-purchase` means a round-up that is never pre-ticked.
`wholesale-b2b` `tiered-volume` means MOQ price breaks, not a consumer promo.

## Sources

- Shopify discount types and combinations: https://help.shopify.com/en/manual/discounts/discount-types and https://help.shopify.com/en/manual/discounts/combining-discounts/discount-combinations
- Berger, Rule of 100: https://jonahberger.com/fuzzy-math-what-makes-something-seem-like-a-good-deal/ ; JBR 2015 replication: https://www.sciencedirect.com/science/article/abs/pii/S0148296315003513
- Seguno unique-code benchmarks: https://www.seguno.com/unique-discount-code-benchmarks
- Common Thread Collective BFCM offer database: https://commonthreadco.com/blogs/ecommerce-playbook/dig-in-bfcm-offer-database-2023 and https://commonthreadco.com/blogs/ecommerce-playbook/how-to-craft-the-best-bfcm-offer-this-year
- Chen, Marmorstein, Tsiros and Rao 2012 (bonus packs): https://doi.org/10.1509/jm.10.0443
- FTC 16 CFR 251.1 (Free): https://www.law.cornell.edu/cfr/text/16/251.1 ; 16 CFR 233.1 (deceptive pricing): https://www.law.cornell.edu/cfr/text/16/233.1 ; Mail Order Rule: https://www.ftc.gov/business-guidance/resources/business-guide-ftcs-mail-internet-or-telephone-order-merchandise-rule
- Convertibles GWP vs discount popup test: https://convertibles.dev/blogs/case-studies/free-gifts-vs-discounts-popup-offers-case-study
- Baymard cart abandonment and shipping-cost research: https://baymard.com/lists/cart-abandonment-rate and https://baymard.com/blog/show-shipping-costs-on-product-pages
- 72technologies free-shipping bar test: https://www.72technologies.com/blog/free-shipping-threshold-bar-ab-test-results
- AccelerOI pricing psychology (quantity breaks): https://www.acceleroi.com/blog/psychology-of-pricing
- Chernev 2003 (choice overload): https://ideas.repec.org/a/oup/jconrs/v30y2003i2p170-83.html
- Statlas AOV data (Taylor Holiday): https://www.linkedin.com/posts/taylor-holiday-a169b322_we-track-store-and-analyze-conversations-activity-7471272309199265792-Xc7H
- CXL pricing experiments (decoy, anchoring, PWYW): https://cxl.com/blog/pricing-experiments-you-might-not-know-but-can-learn-from/
- UK CMA reference-pricing principles: https://assets.publishing.service.gov.uk/media/66ab4347a3c2a28abb50db3c/Discount_and_reference_pricing_principles.pdf ; CTSI pricing guidance: https://www.businesscompanion.info/en/guidance-for-traders-on-pricing-practices
- Recharge subscription trend report 2026: https://getrecharge.com/reports/subscription-trend-report-2026/ ; Gourville 1998: https://doi.org/10.1086/209517
- FTC negative option and ROSCA: https://www.ftc.gov/business-guidance/blog/2024/10/click-cancel-ftcs-amended-negative-option-rule-what-it-means-your-business
- Welcome offer benchmarks: https://farabiulder.com/blog/welcome-offer-benchmarks and https://www.blossomecom.com/blogs/welcome-offer-optimization-ecommerce
- ReferralCandy referred-customer study: https://www.referralcandy.com/blog/referred-customers-study/
- Redseer festive 2025: https://redseer.com/articles/festive-2025-day-0-ecommerce-sales-surge-25-with-gst-boost-demand-led-by-smartphones-and-tvs/
- BNPL placement and AOV: https://digitalheroesco.com/journal/shopify-afterpay-klarna-shop-pay-integration/ and https://d2c-times.com/shopifys-shop-pay-installments-surge-is-rewriting-dtc-checkout-economics/
- Shopify pre-order UX guidelines: https://shopify.dev/docs/storefronts/themes/pricing-payments/preorder-tbyb/preorder-tbyb-ux-guidelines
- Attentive BFCM campaign guidance: https://www.attentive.com/black-friday-cyber-monday-2026/articles/bfcm-campaigns-that-convert
- Barton, Zlatevska and Oppewal 2022 scarcity meta-analysis (via Clean Commit): https://cleancommit.io/blog/do-countdown-timers-work/
- India CCPA Dark Patterns Guidelines 2023: https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf ; E-Commerce Rules 2020: https://ibclaw.in/consumer-protection-e-commerce-rules-2020/
- Luxury pricing: https://aws2.campaignasia.com/article/why-pricing-is-the-easy-growth-trap-in-luxury/482956 and https://www.vogue.com/article/should-luxury-brands-reduce-their-prices

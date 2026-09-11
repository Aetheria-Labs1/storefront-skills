# Price presentation

How a price, a compare-at, a saving, a unit price, a tax line or an
installment is written and placed. Applies to every page that shows a number
with a currency symbol. The number itself comes from the ledger
(`references/offers/offer-ledger.md`); this file decides how it is shown.
Offer mechanics are in `references/offers/offer-types.md`; deadline and stock
wording in `references/offers/urgency-scarcity.md`.

Format per rule: imperative sentence; tag; rationale; a check. Checks are
evaluated on the hosted draft; Checks use persisted MCP source and the hosted draft. Tags: LAW, RESEARCH, OPERATOR,
HEURISTIC.

## Compare-at legality by jurisdiction

| Market | Reference price rule | Duration and volume | Percent computation | Labels | Enforcement | Source |
|---|---|---|---|---|---|---|
| EU | Prior price = lowest price the trader applied in the 30 days before the reduction (Price Indication Directive Art 6a). Successive campaigns each take the lowest price of the previous 30 days including the earlier promo price. | Member states may shorten the window for goods on sale under 30 days and perishables. Netherlands ACM: discount periods may not exceed 3 months. | Any percent is computed from the 30-day prior price (CJEU, Aldi Sud, 26 Sept 2024). | "Was" price must be the 30-day low, not the list. | National authorities; fines under UCPD transposition. | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A52021XC1229%2806%29 ; https://www.lexology.com/library/detail.aspx?g=0419af35-3c0b-4820-8c6c-46150f540f75 |
| UK | Was-price offered on the same site immediately before the sale for at least as long as the sale runs (30 days "more likely" compliant; 21 days accepted for a 10-day sale). | At least 1 unit sold at the was-price for every 2 sold at the now-price. Once either test fails, the now-price is the price and the strike must go. | From the substantiated was-price. | RRP comparisons labelled "RRP" and genuine. | CMA direct fines up to 10% of global turnover since 6 April 2025 (DMCC Act). Emma Sleep trial on these principles began June 2026. | https://assets.publishing.service.gov.uk/media/66ab4347a3c2a28abb50db3c/Discount_and_reference_pricing_principles.pdf ; https://www.businesscompanion.info/en/guidance-for-traders-on-pricing-practices |
| US | Former price is "the actual, bona fide price at which the article was offered to the public on a regular basis for a reasonably substantial period of time" (16 CFR 233.1). | "Formerly sold at" needs substantial sales. Nominal reductions may not be advertised as a sale. | From the bona fide former price. | MSRP or list comparisons (233.3) need substantial sales at that price in the area. | State UDAP statutes and class actions more than FTC. | https://www.law.cornell.edu/cfr/text/16/233.1 |
| India | Compare-at is the printed MRP (inclusive of all taxes, in rupees), displayed on the listing (Legal Metrology Packaged Commodities Rule 6(10)). Selling above MRP is an offence. | A revised lower MRP sticker may not cover the original. | "X% off MRP" only against the printed MRP. | "MRP ₹X (inclusive of all taxes)". | Legal Metrology officers; CCPA for misleading discounts and "bait and switch". | https://www.legitquest.com/act/legal-metrology-packaged-commodities-rules-2011/97B4 ; https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf |
| Unknown | Apply EU 30-day low plus UK duration and volume plus India MRP display (offer-types OF13). | | | | | |

## Compare-at and anchoring

PP1. Render a struck-through price only when the ledger row records a `compare_at_basis` of `prior_30_day_low`, `regular_price_with_sales`, `mrp` or `rrp_substantiated`. No basis: show the sale price alone, no strike, no "save". LAW.
Rationale: every market above treats an unsubstantiated former price as deception.

PP2. For EU visitors, compute the percent and the "was" from the lowest price of the prior 30 days, including any earlier promotion in that window. LAW.
Rationale: Art 6a; CJEU 2024 ruled the percent must also reference the 30-day low.
Check: the ledger `compare-at` row cites the 30-day low with a date range when `EU` is in the market list.

PP3. For UK visitors, keep the strike only while the was-price ran at least as long as the sale has run and at least one unit sold at the was-price per two at the sale price; remove it the day either test fails. Label RRP comparisons "RRP". LAW.
Rationale: CMA duration and volume principles, applied generally since the mattress work.
Check: the ledger records was-price start date and units sold at each price; sale end date is not later than start date plus was-price duration.

PP4. For US visitors, never call a nominal reduction a sale, and never use a list or MSRP figure at which substantial sales did not occur. LAW.
Rationale: 16 CFR 233.1 and 233.3.
Check: ledger `compare-at` row basis is `regular_price_with_sales` or `rrp_substantiated`, not "list price in Shopify".

PP5. For India, show "MRP ₹X (inclusive of all taxes)" for packaged goods, keep the selling price at or below MRP, phrase discounts as "off MRP", and include the mandatory declarations (net quantity, manufacturer or importer, country of origin, consumer-care contact, best-before where applicable) in `specs`. LAW.
Rationale: Legal Metrology Rule 6(10); E-Commerce Rules 2020 Rule 6(5).

PP6. Place the anchor before the paid price in reading direction (above or left), at equal or smaller size and lower contrast than the paid price. RESEARCH and LAW.
Rationale: the first number seen becomes the reference (Tversky and Kahneman 1974; Ariely, Loewenstein and Prelec 2003). A compare-at larger than the paid price is "interface interference" under India CCPA.
Check (browser): for each struck element, its `getBoundingClientRect().top` is less than or equal to the sale price element's and its computed `font-size` is less than or equal to the sale price's.

PP7. Use only real anchors when there is no discount: the top tier of a good, better, best ladder, a cost-per-use comparison with a named alternative, or a real competitor price with source. HEURISTIC and RESEARCH.
Rationale: the Williams-Sonoma bread-maker pattern (a $429 model nearly doubled $279 sales) works without a fake was-price; disprovable anchors backfire.
Check: any "compare to" or "worth" string has a ledger row with a source URL or catalog id.

## Unit, per-day and percent framing

PP8. Show the unit price (per kg, per litre, per 100 ml, per serving) small in `specs` or beside the price where law requires it; never as the hero figure. LAW.
Rationale: EU Price Indication Directive requires unit price for many goods; India Legal Metrology lists "unit sale price" among mandatory declarations.
Check: ledger row `per-unit price` exists for consumables sold by weight or volume in EU or IN markets.

PP9. Use per-day or per-serving framing only for consumables, subscriptions and memberships; never for a one-time purchase over the Rule-of-100 line unless it is a real BNPL split with the total shown first. RESEARCH.
Rationale: Gourville 1998 "pennies a day" raised acceptance 52% vs 30% for the same annual cost; the frame backfires on large one-time purchases by naming the commitment (EightX).

PP10. Always show the currency saving; let percent lead only under $100 or ₹8,000, and lead with currency above it ("Save $128 (18%)"). SMS copy may lead with percent regardless (OPERATOR, Attentive: percent formats drove 10% higher SMS conversion). RESEARCH, consistent with offer-ledger rule 2.
Rationale: Rule of 100 (Berger; JBR 2015). India crossover is HEURISTIC, no replication found.
Check: as offer-types OF2.

PP11. Never show "up to X% off" unless a meaningful share of the discounted SKUs sit at X. Show the range ("20 to 50% off") or the modal depth instead. LAW.
Rationale: UK CAP and ASA "up to" standard; India CCPA misleading advertisement; FTC Section 5.
Check: the ledger row for the headline depth records the count of SKUs at the maximum against the total.

## Charm and round pricing

PP12. Use 9-endings for mass and mid-market goods in comparison contexts (collection cards, tier tables, sale tags), and round prices for premium, hedonic and luxury goods and for subscription plans. RESEARCH.
Rationale: Anderson and Simester 2003, three field experiments: $9 endings raised demand, most for new items and least when a "Sale" cue was present ($39 outsold $34). Wadhwa and Zhang 2015: round prices fit feeling-based purchases. Data Colada replication: the effect is weak on an isolated PDP for a known product.

PP13. Round Indian rupee prices to the whole rupee ("₹999", never "₹999.99"). LAW and HEURISTIC.
Rationale: Legal Metrology requires MRP to the nearest rupee or 50 paise; paise endings are not idiomatic.

## Total-cost transparency

PP14. Show a shipping estimate or the free-shipping threshold in the `buy-box` `shipping-returns` line, and the full total (items, shipping, tax, fees) before payment details are requested. RESEARCH and LAW.
Rationale: Baymard: 40% of non-browsing abandoners cite extra costs, 12% could not see the total up front, 64% look for shipping cost on the product page. UK DMCC prohibits drip pricing; India Rule 6(5)(b) requires a single-figure total with breakup; FTC treats hidden mandatory fees as bait and switch.

PP15. Include every mandatory fee (handling, COD fee, platform fee) in the displayed price or state it beside the price; taxes and shipping may follow later only if the page never calls the displayed price final. LAW.
Rationale: FTC junk-fees rule and Section 5; UK DMCC invitation to purchase; India E-Commerce Rules 6(5)(b).

PP16. Write tax status the market's way: EU and UK B2C prices VAT-inclusive with no separate VAT line; India "inclusive of all taxes" and never add GST at checkout on B2C; US ex-tax with "plus tax" or "tax calculated at checkout" beside the price. LAW.
Rationale: EU and UK consumer law; India MRP definition; US state sales-tax practice.

PP17. Match the on-page free-shipping threshold, the cart progress bar target and the checkout shipping rate to one number from store settings. LAW and OPERATOR.
Rationale: a mismatch is a misleading price claim and the most common bar complaint.
Check: ledger row `shipping` cites the store shipping profile; `commerce_config.free_shipping_threshold` in the cart profile equals it (`references/cart-profile-management.md`).

## Hiding and revealing price

PP18. Never hide the price ("see price in cart", "DM for price", "login to see price") on a B2C page. A US MAP-constrained category may use "add to cart to see price" and the plan flags it as a conversion risk; `wholesale-b2b` may gate trade prices behind login. LAW.
Rationale: UK DMCC and EU UCPD require the full price in an invitation to purchase; India Rule 6(5)(b).

PP19. Time the first price to the awareness level: unaware and problem-aware pages reveal price after the mechanism and first proof, and always before the first CTA that leads to a cart or PDP; product-aware and most-aware pages show price in the hero. HEURISTIC, consistent with `references/page-types/_index.md` section 5.
Rationale: a price before the premise reads as an ad to a cold reader; a hidden price to a hot one is friction.
Check: the page-type checklist `price_above_fold` value is satisfied; on `tof` types the first price element index is greater than the `mechanism` or `solution` index and less than or equal to the first `closing-cta` or `offer-bridge` index.

PP20. Show the shopper's currency with the ISO code whenever the symbol is ambiguous ("$" for AU, CA, NZ, SG shoppers) and never drop the symbol. OPERATOR.
Rationale: cross-border was 16% of Shopify BFCM 2025 orders; the Cornell "no symbol" finding is restaurant-specific and mixed in ecommerce tests (49% win rate, AccelerOI).

## Indian rupee formatting

PP21. Write rupees as "₹" followed by Indian digit grouping (₹1,24,999, not ₹124,999), whole rupees only, "MRP" label for the compare-at, "inclusive of all taxes" once beside the first price. LAW and HEURISTIC.
Rationale: Legal Metrology labelling; the lakh grouping is the reading convention.

PP22. Put the payment facts India shoppers decide on beside the price: "Pay on delivery via UPI or cash" or "Cash on delivery not available for this pincode", a prepaid incentive if the merchant runs one, and the pincode `delivery-estimate` returning a date, not a speed. OPERATOR.
Rationale: COD is still about 45 to 60% of D2C orders nationally and up to 75% in Tier-2 cities; COD RTO runs 20 to 30% versus 2 to 8% prepaid; Bain notes a shift to UPI-on-delivery (Financial Express, ET, Bain 2026).
Check: when `IN` is in the market list, `buy-box` contains a COD statement and a `delivery-estimate` island bound to live data.

## BNPL and cashback lines

PP23. Write the installment line as total first, then the split, count, provider and interest: "$99, or 4 payments of $24.75 with Shop Pay"; India: "₹5,999, or ₹999/month x 6, no-cost EMI on [bank] cards". The total stays larger and higher-contrast than the split. LAW and OPERATOR.
Rationale: TILA / Reg Z triggering terms; UK FCA BNPL rules from 2026; RBI disclosure for no-cost EMI; Baymard: summarise financing in plain language.
Check: `bnpl-line` text matches `^[₹$£€][0-9,]+, or ` and its computed `font-size` is less than or equal to the price's.

PP24. Show BNPL only for carts at or above the provider's floor (typically $50, ₹3,000) and for at most two providers. OPERATOR.
Rationale: Shop Pay Installments is not shown under $50; three providers create choice fatigue (Digital Heroes; EightX Plus adoption data).
Check: ledger row O14 lists the enabled providers (at most two) and the floor; `bnpl-line` is absent when the ledger price is under the floor.

PP25. Write cashback with cap, minimum order, bank list and timing in one line ("10% instant discount with HDFC cards, up to ₹1,500, on orders over ₹2,999. T&C"), and never label store credit as cashback. LAW.
Rationale: conditions are material terms; "up to" standard (PP11).
Check: any line matching `cashback|instant discount` also matches `up to` and names a bank or method.

## Pre-order and Free price lines

PP26. On pre-orders, show the deposit and the full price as two labelled figures and never strike the full price against the deposit; put "Estimated to ship by [date]" beside the price and beside the button. LAW and OPERATOR.
Rationale: Shopify pre-order UX guidelines; FTC Mail Order Rule.

PP27. Where "free" carries a shipping or handling charge, print the charge in the same phrase ("Free sample, $4.95 shipping"). LAW.
Rationale: FTC 251.1 disclosure "at the outset"; UK banned practice on "free" with costs beyond unavoidable response cost.
Check: as offer-types OF5.

## Sources

- EU Price Indication Directive Art 6a guidance: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A52021XC1229%2806%29 ; CJEU Aldi Sud 2024 summary: https://www.lexology.com/library/detail.aspx?g=0419af35-3c0b-4820-8c6c-46150f540f75
- UK CMA reference-pricing principles: https://assets.publishing.service.gov.uk/media/66ab4347a3c2a28abb50db3c/Discount_and_reference_pricing_principles.pdf ; Oxera on the Emma Sleep case and ACM: https://www.oxera.com/insights/agenda/articles/when-does-a-discount-become-deceptive/ ; CTSI pricing practices: https://www.businesscompanion.info/en/guidance-for-traders-on-pricing-practices ; CMA UCP guidance: https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices
- FTC 16 CFR 233: https://www.law.cornell.edu/cfr/text/16/233.1 ; 16 CFR 251: https://www.law.cornell.edu/cfr/text/16/251.1 ; junk-fees rule: https://www.ftc.gov/business-guidance/blog/2024/12/getting-bottom-line-ftcs-bipartisan-junk-fees-rule-your-business ; Mail Order Rule: https://www.ftc.gov/business-guidance/resources/business-guide-ftcs-mail-internet-or-telephone-order-merchandise-rule
- India Legal Metrology (Packaged Commodities) Rules: https://www.legitquest.com/act/legal-metrology-packaged-commodities-rules-2011/97B4 ; amendments: https://ssrana.in/articles/new-amendments-legal-metrology-packaged-commodities-rules-2011/ ; E-Commerce Rules 2020: https://ibclaw.in/consumer-protection-e-commerce-rules-2020/ ; CCPA Dark Patterns 2023: https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf
- Baymard cart abandonment: https://baymard.com/lists/cart-abandonment-rate ; shipping costs on PDP: https://baymard.com/blog/show-shipping-costs-on-product-pages ; payment UX: https://baymard.com/learn/payment-ux
- Berger Rule of 100: https://jonahberger.com/fuzzy-math-what-makes-something-seem-like-a-good-deal/ ; JBR 2015: https://www.sciencedirect.com/science/article/abs/pii/S0148296315003513
- Gourville 1998: https://doi.org/10.1086/209517 ; per-day boundary: https://eightx.co/blog/psychological-pricing-dtc
- Anderson and Simester 2003: https://link.springer.com/article/10.1023/A:1023581927405 ; round prices for premium: https://conversion.studio/blog/psychological-pricing ; CXL anchoring and Williams-Sonoma: https://cxl.com/blog/pricing-experiments-you-might-not-know-but-can-learn-from/ ; Growthegy on disprovable anchors: https://www.growthegy.com/2026/05/24/product-pricing-anchoring-decoy-ecommerce/
- Attentive SMS percent vs dollar: https://www.attentive.com/black-friday-cyber-monday-2026/articles/bfcm-campaign-best-practices
- Shopify BFCM 2025 cross-border share: https://www.shopify.com/news/bfcm-data-2025 ; currency symbol tests: https://www.acceleroi.com/blog/psychology-of-pricing
- India COD and UPI: https://www.financialexpress.com/business/news/upi-wins-but-cod-wont-quit/4303229/ ; https://economictimes.indiatimes.com/news/india/nearly-half-of-indias-online-orders-are-still-cod-why-cash-on-delivery-isnt-fading-in-the-upi-era/articleshow/131118821.cms ; https://www.bain.com/globalassets/noindex/2026/bain_report_how_india_shops_online_2026.pdf ; RTO rates: https://shipybox.in/resources/ecommerce-shipping-statistics-india
- BNPL placement and provider limits: https://digitalheroesco.com/journal/shopify-afterpay-klarna-shop-pay-integration/ ; https://d2c-times.com/shopifys-shop-pay-installments-surge-is-rewriting-dtc-checkout-economics/ ; https://eightx.co/blog/afterpay-vs-klarna-vs-affirm-shopify-plus
- Shopify pre-order UX: https://shopify.dev/docs/storefronts/themes/pricing-payments/preorder-tbyb/preorder-tbyb-ux-guidelines

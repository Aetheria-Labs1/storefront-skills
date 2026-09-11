# Numbers and Counts

Every numeral in a proof, trust, stats or press section is a ledger row
(`references/proof/proof-ledger.md` display rule 10; `design-rules.md` N11).
This file gives the source query, phrasing, rounding and as-of rule for each
kind of number, and the pre-render numeral checklist `/design-page` and
`/generate` run. Rule tags: LAW, RESEARCH ([H] [M] [L]), OPERATOR,
HEURISTIC. Live urgency numbers (stock, viewers, recent buys) are governed by
`references/offers/urgency-scarcity.md` and `references/anti-patterns/dark-patterns.md`;
this file only states what they may never be.

## Numeral rules by claim

| Claim | Ledger kind | Source query or document | Phrase on page | Rounding | As-of |
|---|---|---|---|---|---|
| Customers | `customer-count` | distinct customers with at least one paid, non-refunded order, all time; Shopify customers export or analytics screenshot | "Over 12,000 customers since 2022" | down to two significant figures; 12,438 becomes 12,000 | month shown when the export is older than 90 days |
| Units or orders sold | `sales-count` | sum of fulfilled units (or orders) in a stated window; never both words for one number | "Over 48,000 units shipped, Jan 2023 to Aug 2026" | down to two significant figures | window mandatory |
| Repeat rate | `repeat-rate` | customers with two or more paid orders divided by all customers, window stated | "41% of customers reorder within 90 days (Jan to Jun 2026)" | one decimal at most, or whole percent rounded down | window mandatory |
| Five-star count | `review-summary` | count of published reviews with rating 5 from `lexsis_catalog.reviews` `rating_min: 5` | "1,203 five-star reviews" | exact or down | API date |
| Star average | `review-summary` | mean of all published ratings for the exact scope, n >= 5 | "4.6/5 from 312 reviews" | one decimal, standard rounding; never two decimals; never 5.0 below n = 20 unless all are five | API date |
| Review count | `review-summary` | API total for the scope | "312 reviews" | exact | API date |
| "Sold out N times" | `sales-count` | inventory history: N distinct events where available quantity reached 0 while published | "Sold out three times since launch" | exact; N spelled out under ten | inventory log dates |
| "#1", "best-selling in <category>" | `award` or `test-data` | third-party panel (Nielsen, NielsenIQ, Mintel, Kantar) or a platform badge with dated screenshot | "Best-selling face serum on Nykaa, Beauty > Serums, 4 Sep 2026" | none | source, category and period named |
| Survey percentage | `test-data` | survey report: n, method, question wording, dates | "93% of 100 users saw visible results in 8 weeks (self-assessment)" | whole percent, rounded down | study date |
| Clinical percentage | `test-data` | study report: n, design (single-arm, controlled, blinded), duration, endpoint, lab or CRO | "In a 12-week single-arm study of 60 adults, 87% reported softer skin" | as reported; never rounded up | study date |
| Years in business | `policy-fact` | incorporation date or first order date | "Since 2019" | none | none |
| Social followers | `customer-count` | live platform count | "82,000 on Instagram" | down to two significant figures; never for a bought audience | month shown |
| Awards count | `award` | list of awards with bodies and years | "Three industry awards (2024 to 2026)" | exact | years shown |
| Countries or cities shipped to | `sales-count` | order export by country | "Shipped to 14 countries" | exact | as-of month |
| Live stock ("3 left in Olive / M") | `stock-count` | `lexsis_catalog.get` inventory read at render through the island binding | island output only | exact, variant-specific | live; hide on failure |
| Live activity ("137 bought in the last 24 hours") | never a fixed numeral | live orders query with the window stated; hide on failure | island output only | exact | live |
| "People viewing", "bought in the last hour" popups | never | | | | |

## Rounding, "over" and "+"

| Rule | Detail |
|---|---|
| Direction | always down; 12,438 is "over 12,000", never "12,500+" or "nearly 13,000" |
| Precision | two significant figures for counts above 100; exact below 100 |
| Word | "over N" in running copy; "N+" allowed inside a stats tile where the tile has no room for a word; one form per page |
| Exactness | an exact figure is allowed when the export is under 90 days old and the page states the month |
| Never | rounding up; "almost"; "nearly"; "thousands of"; "countless"; "loved by many" |
| Bundles | never sum component review counts or average component ratings into one bundle number |
| Cross-site | never add Trustpilot, Google and on-site counts into one total; show each with its source |

## Star averages and decimals

| Rule | Detail | Source |
|---|---|---|
| Pair | the average never appears without the count in the same element | Trustpilot brand rules; PowerReviews: 52% distrust a star rating without content [M] |
| Threshold | no average below n = 5; individual reviews and "4 reviews" instead | Baymard n=670 [H] https://baymard.com/blog/sort-by-customer-ratings |
| Decimals | one decimal, standard rounding, from all published ratings; two decimals never | `proof-ledger.md` display rule 3 |
| Glyphs | star glyphs match the number: 4.6 renders four full stars and one partial at 60%, never five full; glyphs are inline SVG, never emoji | `design-rules.md` N1 |
| 5.0 | only when every review is five stars and n >= 20 | `proof-ledger.md` display rule 3 |
| Distribution | at n >= 20, every bar including one-star | `references/proof/reviews-sourcing.md` RS5 |
| Static assets | "rating as of <Month Year>" on any exported image or PDF | Trustpilot brand guidelines Sep 2026 |

## Percentages from surveys and studies

| Element | Required beside the number |
|---|---|
| n | "of 100 users", "n=60" |
| Design | self-assessment, consumer perception, instrumented, single-arm, controlled; blinded if so |
| Duration | "in 8 weeks" |
| Population | "adults 25 to 48", "women with dry skin" |
| Date | study month and year in the footnote |
| Who ran it | brand, third-party CRO, lab name |
| Disclosure | if the study measured a different endpoint than the claim, the claim is downgraded to what was measured |

Pattern from the highest-tier pages: "third-party, single-arm study, 35 healthy
adults ages 25 to 48" (AG1); "ex vivo, human stool samples" (LOAM)
(internal teardown audit, 2026-09-10).

## Units, currency and locale

| Rule | Detail |
|---|---|
| One unit per number | "customers" or "orders" or "units", never interchangeably for the same figure |
| Locale grouping | use the store locale's digit grouping everywhere: en-IN "12,00,000", en-US and en-GB "1,200,000"; never both on one page |
| Lakh and crore | only when `voice_md` or the merchant uses them; then consistently; never mixed with million on one page |
| Currency | the store currency symbol from `lexsis_catalog.get`; symbol before the number, no space, for ₹, $, £, €; ISO code only when two currencies appear |
| Percent | digits then "%" with no space; whole numbers unless the source reports a decimal |
| Ratings | "4.6/5" or "4.6 out of 5"; never "4.6 stars" as text without the count |
| Dates | "Sep 2026" or "4 Sep 2026" in copy; ISO in the ledger |
| Ranges | "2 to 5 days", not a hyphen or dash |
| Large numbers | digits with grouping, never "1.2M" in proof copy; "1.2M" allowed only in a stats tile with the ledger's exact figure in the row |

## Truthful phrasing without hedging

| Instead of | Say | Why |
|---|---|---|
| "Thousands of happy customers" | "Over 12,000 customers since 2022" | hedge words are not a substitute for a source; omit or source |
| "Loved by many" | a sourced count or nothing | same |
| "Up to 40% reduction" | "Reduced by 23% on average (n=60, 12 weeks)" | "up to" hides the typical result (FTC 255.2(b)) |
| "May help improve" | "Improved <measure> by <n>% in <study>" or remove | "may help" is an unsubstantiated implication |
| "Rated 5 stars" | "4.8/5 from 212 reviews" | the true number with its count |
| "Trusted by 50,000" | "Over 50,000 customers" | "trusted" is an opinion; the count is the fact |
| "#1 serum" | "Best-selling face serum on Nykaa, Beauty > Serums, 4 Sep 2026" | source, category, period |
| "Clinically proven" | "In a 12-week study of 60 adults, 87% reported <result>" | the data, not the adjective |
| "Selling fast" | live island output or nothing | static urgency is a dark pattern |
| a number the merchant cannot document | remove the sentence | a hedge does not repair a missing source |

## Google rich results for ratings

| Rule | Detail | Source |
|---|---|---|
| Eligible types | `Product` (and other listed types) with `aggregateRating` (`ratingValue`, `ratingCount` or `reviewCount`) or `Review` with `author` name under 100 characters, `datePublished`, `reviewRating` | https://developers.google.com/search/docs/appearance/structured-data/review-snippet |
| Self-serving | `Organization` and `LocalBusiness` reviews about the site itself, including embedded third-party widgets, are ineligible since Sep 2019 | https://developers.google.com/search/blog/2019/09/making-review-rich-results-more-helpful |
| Visible parity | markup numbers equal the visible numbers on the page | same |
| Source | reviews about this specific item, collected on the site; no aggregation from other sites; no undisclosed incentivised reviews | same |
| Google Ads seller ratings | roughly 100 eligible reviews in 24 months and 3.5 average before Google issues a rating; never a Google-styled badge before then | https://support.google.com/google-ads/answer/2375474 |
| Product ratings on Shopping | 50 reviews across the catalogue | https://support.google.com/merchants/answer/14549080 |
| Google Business Profile reviews on your site | Places API with attribution; they do not earn rich-result stars on your page | https://developers.google.com/maps/documentation/places/web-service/policies |

## Pre-render numeral checklist

Run on `MCP source` before compile. Every listed numeral must map to
a ledger row id; a numeral with no row is removed from copy, not softened.

| Check | Pass |
|---|---|
| Every line of the output has a ledger row id written beside it in `QA record` | yes |
| Every count is rounded down or exact and phrased with "over" or "+" consistently | yes |
| Every time-bound count states its window or as-of month | yes |
| Every average has a count in the same element and n >= 5 | yes |
| Every percentage has n and design in the same element or a footnote on the same screen | yes |
| Every "#1" or "best-selling" names source, category and period | yes |
| No static numeral for stock, viewers or recent buys; islands only | yes |
| Structured data `aggregateRating` equals the visible numbers | yes |
| Locale grouping and currency symbol are consistent across the page | yes |

## Rules

NC1. Every numeral in a proof, trust, stats, press, guarantee or founder section maps to a ledger row; no row, no numeral. OPERATOR; LAW CAP 3.7, FTC reasonable basis, UCPD Art. 6, CCPA 2022.
Check: the checklist extraction above; each output line has a row id in `QA record`.

NC2. Round counts down to two significant figures and prefix "over" (or suffix "+" in a stats tile); never round up, never "nearly" or "almost". HEURISTIC; consistent with `proof-ledger.md` display rule 5.

NC3. Show an average only at n >= 5, one decimal, always with the count in the same element; 5.0 only when every review is five stars and n >= 20. RESEARCH [H] Baymard; LAW FTC 465.7 (a headline average that hides its base misrepresents the set).
Check: `references/proof/reviews-sourcing.md` RS3 and RS4.

NC4. Time-bound counts state the window ("Jan 2023 to Aug 2026") or the as-of month when the export is older than 90 days. LAW CAP 3.7 (claims must hold at publication); HEURISTIC.
Check: each `sales-count` and `repeat-rate` string in source contains a month name or a year.

NC5. Percentages carry n, design and duration beside the number or in a footnote visible on the same screen. LAW CAP 3.7; FTC; ASCI. RESEARCH teardown pattern 9.

NC6. "#1", "number one", "best-selling", "most popular" name the third-party source, the category and the period, or are removed. LAW ASA (Skinny Tan ruled misleading; Post Office and Vitabiotics upheld only on third-party data); FTC; CCPA.

NC7. Never mix units for one figure and never sum or average across products or sites. LAW CMA208 (misleading aggregation); Google review-snippet policy; HEURISTIC.
Check: each count row names one unit; no `review-summary` row cites more than one scope.

NC8. Live numbers (stock, recent buys, viewers) come only from island bindings with a hide-on-failure mode; a fixed numeral for any of them is removed; popups are never rendered. LAW FTC Dark Patterns report 2022; CMA Wowcher undertakings; India CCPA Dark Patterns Guidelines 2023 (false urgency, burden of proof on the seller).

NC9. Hedge words never replace a source: a number the merchant cannot document is removed from copy; "up to", "may help", "thousands of", "countless" are not softeners the page may use. LAW CAP 3.7; FTC 255.2(b) ("up to" hides the typical result).

NC10. Locale grouping, currency symbol placement and percent formatting follow the store locale and stay consistent on the page. OPERATOR (`lexsis_catalog.get` currency; store locale); HEURISTIC.

NC11. Structured data for ratings uses `Product` (or another eligible type) with numbers equal to the visible ones; no `Organization` self-serving review markup; no Google-styled seller badge before Google has issued a rating. LAW Google review-snippet policy; Google Ads seller ratings policy.

NC12. Star glyphs are inline SVG and match the decimal (partial fill), never emoji, never five full stars beside 4.x. LAW none; HEURISTIC; `design-rules.md` N1.
Check: the source/hosted review N1 passes; for each average, the SVG group renders `floor(avg)` full stars and one partial.

NC13. Every numeral row is repeated under "Claims to confirm" in `page plan` before design; the merchant confirms or the row is dropped. OPERATOR.

## Sources

- FTC Endorsement Guides 255.2(b): https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising
- FTC "Bringing Dark Patterns to Light" 2022: https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf
- CMA Wowcher: https://www.gov.uk/government/news/cma-secures-over-4-million-in-refunds-for-wowcher-customers ; CMA Emma Sleep 2026: https://www.gov.uk/government/news/court-endorses-cma-action-as-emma-sleep-agrees-to-change-sales-practices
- India CCPA Dark Patterns Guidelines 2023: https://consumeraffairs.nic.in/theconsumerprotection/guidelines-prevention-and-regulation-dark-patterns-2023
- ASA "number one" rulings: https://www.mondaq.com/uk/advertising-marketing-branding/128488/asa-adjudications-snapshot-february-2011 ; https://www.naturalproductsonline.co.uk/news/company-news/asa-satisfied-vitabiotics-is-uks-number-one-vitamin-company/ ; https://www.bbc.co.uk/news/entertainment-arts-41664183
- Baymard sort by ratings (perfect score on few ratings loses): https://baymard.com/blog/sort-by-customer-ratings
- PowerReviews 2021 (52% distrust stars without content): https://www.powerreviews.com/survey-importance-product-reviews-drive-purchase-behavior/
- Trustpilot brand guidelines (count beside rating; "as of" on static assets): https://uk.corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026 ; count lift 28% to 33% [M]: https://assets.ctfassets.net/b7g9mrbfayuu/29yz43E1wulVjHyTlJoFWJ/98e785d7ecc593531dd525feef4d7b3f/Trustpilot_Value_of_Ratings_and_Reviews_Report2023.pdf
- Google review snippet: https://developers.google.com/search/docs/appearance/structured-data/review-snippet ; 2019 self-serving change: https://developers.google.com/search/blog/2019/09/making-review-rich-results-more-helpful ; seller ratings: https://support.google.com/google-ads/answer/2375474 ; product ratings: https://support.google.com/merchants/answer/14549080
- Teardowns: study footnotes with n and design (AG1, LOAM), proof counts in headlines (HexClad "1,000,000+"), cart-velocity line (Wakefit): internal research audit (2026-09-10) Part D.1 and D.5.

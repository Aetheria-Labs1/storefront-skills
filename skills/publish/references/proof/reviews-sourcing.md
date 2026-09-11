# Reviews Sourcing

The tiered procedure that fills the review rows of the plan's `## Proof
ledger` (`references/proof/proof-ledger.md`). `/plan-page` runs tiers 0 to 3
against Lexsis before any template or asset call; tiers 4 and 5 run only when
tiers 1 to 3 return nothing usable. Output is ledger rows, never page copy.
Rule tags: LAW (statute, regulator, platform terms), RESEARCH (with [H]
academic or regulator, [M] large survey with method, [L] vendor or
practitioner), OPERATOR (Lexsis contract), HEURISTIC (house judgement).

Definitions. `n` is the count of published, product-matched reviews the API
returns for the exact product or active collection. `avg` is the arithmetic
mean of all published ratings for that scope, never of a `minRating` subset.
"Usable" means a row can reach `verified` under the ledger's per-kind table.

## Tier 0: read status

| Step | Call | Read | Then |
|---|---|---|---|
| 0.1 | `lexsis_catalog.reviews_status` | source connected (Judge.me), imported count, last sync | connected and count > 0: tier 1. Otherwise: tier 4 |
| 0.2 | write "Proof sources" line in `page plan` | source, count, sync date, tier reached | always, even when the answer is "none" |

## Tier 1: active collections

| Step | Call | Read | Then |
|---|---|---|---|
| 1.1 | `lexsis_catalog.review_collections` with `collection_status: "active"` | id, name, `item_count`, product scope | list them with counts in plan question 9 |
| 1.2 | `lexsis_catalog.review_collection_items` for the chosen collection | rating, body, author, date, media, verified flag | one `review-quote` or `review-list` row per rendered item, `collectionId` recorded |
| 1.3 | no active collection fits | | tier 2; optionally `lexsis_drafts.review_collection_create` as a draft shortlist, only when the user asks |

Only `active` collections serve on published pages. A draft the agent creates
is `pending` in the ledger until the merchant activates it in Storefront,
Reviews, Collections. If the host returns `UNKNOWN_ACTION`, ask the merchant
to paste a collection id.

## Tier 2: product reviews via the API

| Step | Call | Read | Ledger use |
|---|---|---|---|
| 2.1 | `lexsis_catalog.reviews` with `product_id`, `limit: 100` | total `n`, `avg`, newest date | `review-summary` row: avg, n, min rating present, as-of date |
| 2.2 | same with `rating_min: 5`, `4`, `3`, `2`, `1` (or read the distribution the response carries) | per-star counts | distribution for the summary; confirms no band is missing |
| 2.3 | same with `has_media: true` | count of photo or video reviews | `review-with-media` rows; UGC grid eligibility |
| 2.4 | same with `source_type` | Shop vs app vs import | verified badge semantics per source (RS10) |

### Count bands

| Band | n | Show | Do not show | Evidence |
|---|---|---|---|---|
| B0 | 0 | nothing review-shaped; go to tier 4 | stars, "loved by customers", placeholder cards | 45% will not buy with no reviews, PowerReviews 2023 n=8,153 [M] |
| B1 | 1 to 4 | individual cards, verbatim, fields present in data; "n reviews" text link | any average, star summary, distribution, carousel | 56% chose 4.5 from 12 ratings over 5.0 from 2, Baymard n=670 [H]; Baymard: hide the summary at 5 or fewer ratings [H] |
| B2 | 5 to 19 | avg to one decimal with n beside it every time; carousel of 3 to 6 cards; verified badge where data has it | distribution below 10 (optional 10 to 19); "rated 5.0" headline styling | most lift arrives by 5 reviews, Spiegel 2017 [H, single retailer, unreplicated] |
| B3 | 20 to 99 | avg + n; distribution bars as filters, expanded; sort control; at least one review of 3 stars or lower reachable without filtering when one exists | five-star-only carousel with no path to the rest | distribution used more than review text, Baymard [H]; 53% seek negative reviews, Baymard [H] |
| B4 | 100+ | everything in B3 plus media filter, attribute filters, merchant replies, corpus summary labelled as generated | aggregating other sites into the same average | conversion lift grows with displayed count to 1,000+, PowerReviews 8.8M pages [M, correlational] |

Spiegel found ratings of 4.2 to 4.7 convert better than 4.7 to 5.0
(https://spiegel.medill.northwestern.edu/how-online-reviews-influence-sales/).
That describes shopper psychology. It is never a target: removing five-star or
low-star reviews to land in the band is suppression (RS9).

### Display decision table

Module shape by band and page type (`references/page-types/_index.md`). Every
module is a ledger row; proof density stays inside the type checklist.

| Page type | B1 (1 to 4) | B2 (5 to 19) | B3 (20 to 99) | B4 (100+) |
|---|---|---|---|---|
| `ad-landing-page`, `pdp-hybrid-landing` | "n reviews" link near price; one quote beside the primary claim | avg + n near price; carousel 3 to 6; last-word quote above final CTA | as B2 plus "Read all n reviews" to a list | as B3; media filter |
| `pdp` | "n reviews" near title; cards mid-page | avg + n near title; carousel or short list | avg + n; distribution + list with filters mid or low page | full module with media and attribute filters, replies |
| `advertorial`, `video-sales-page` | one dated quote after the mechanism | two or three dated quotes inline, never a carousel | as B2 plus avg + n at the offer bridge | as B3 |
| `listicle` | one quote under the reason it matches | one quote per reason where a matching review exists; avg + n at the close | as B2 | as B2 |
| `comparison-us-vs-them` | none or one quote that names the alternative | avg + n near the verdict; quotes that name the alternative | as B2 | as B2 |
| `seo-buyers-guide` | one quote under the ranked entry it matches, labelled by product | per-entry avg + n labelled by product in the comparison table; never one guide-level average | as B2 | as B2 |
| `bundle-kit` | component quotes labelled by product | component avg + n labelled by product; no bundle average unless reviews are bundle-specific | as B2 | as B2 |
| `ugc-creator-collab` | none | `review-with-media` cards only, 3 to 6 | media grid 6 to 12 | as B3 |
| `restock`, `retargeting-warm` | one dated quote answering the objection | avg + n plus one objection quote | as B2 | as B2 |
| `launch-waitlist-preorder`, `thank-you-post-purchase`, `faq-support-led`, `lead-capture-giveaway` | none | none or a store-level avg + n labelled as store rating | as B2 | as B2 |
| luxury vertical (`references/vertical-luxury.md`) | one long-form quote | one long-form quote; no carousel, no counts | as B2 | as B2 |

### Review anatomy: field gating

Render a field only when the record contains it. Never fill a gap.

| Field | Render only if | Rendering |
|---|---|---|
| Rating | `rating` present, integer 1 to 5 from the author | as given; never recalculated (IS 19000 cl. 5.7.3) |
| Body | `body` present | verbatim; `[...]` trim only; "Read more" reveals the full text |
| Title | `title` present | verbatim |
| Name | `reviewer_name` present | first name + last initial, or as the app displays it publicly |
| Location | `location` present | city or region as stored |
| Date | `created_at` present | month and year at minimum; always shown |
| Verified badge | record links to an order, or `verified: true`, or Shop source | the app's own semantics; never on a CSV import without order linkage |
| Photo or video | media URL present and app terms cover display | native aspect; no crop that removes product or watermark |
| Variant | `variant` present | "Size M, Olive" |
| Recommends | explicit boolean present | text plus icon; never inferred from rating |
| Merchant reply | reply present | visually distinct, labelled as the store's reply |
| Incentivised | app flag present | "Incentivised review" label on the card and beside the summary |
| Source | always | "via Judge.me" or "via Shop"; third-party sources link out |

Never render: an avatar that is not the reviewer's, a stock face implied to be
the reviewer, a generated name, date or verified tick.

## Tier 3: proof-proximity candidates

| Step | Call | Read | Then |
|---|---|---|---|
| 3.1 | for each of the plan's three decision questions, `lexsis_catalog.reviews_search` with `query` = the claim in the shopper's words | candidate reviews with ids | row per candidate, status `pending`, section = the claim's section |
| 3.2 | `lexsis_catalog.reviews` by id (or the item in an active collection) | full record | confirm verbatim text, date, fields |
| 3.3 | plan question 9 lists candidates with a one-line excerpt | merchant confirms or an active collection already contains the item | status `verified`; else the row stays `pending` and does not render |

Semantic search returns candidates, not selections. A candidate that mentions
a limitation ("took two weeks", "runs small") is preferred over pure praise.

## Tier 4: zero-review playbook

Run only when tiers 1 to 3 return zero usable rows for both product and store.
Everything here produces evidence for the merchant and a consent shortlist;
only an `external-verified` row reaches the page.

```text
ZERO_REVIEW(store, product):
 1. Shop app reviews. Ask the merchant whether Shop reviews exist (Shopify admin,
    Shop, Reviews). Shop reviews are purchase-verified by construction and sync
    into Judge.me with a non-removable "Verified by Shop" badge.
    STOP if the sync brings n > 0: rerun tier 0.
 2. Brand-owned channels. Ask for: existing testimonials page (must hold evidence
    of genuineness and contact details, CAP 3.45); comments on the brand's own
    Instagram, TikTok or YouTube posts; customer emails, DMs or WhatsApp.
    The author owns each comment or message. Build a consent shortlist: post
    URL or message date, author handle, proposed quote, channels, duration.
    STOP the item until a recorded written "yes" exists (template in
    `references/proof/ugc-rights-and-display.md`).
 3. Public third-party sources. Search "<brand>" "<product>" reviews on each
    source in the table below. Record URL, date, count, rating, handle.
    Apply the per-source rule. Verify the author bought or used the product
    (EU Annex I 23b; FTC bona fide user); if unverifiable, at most a link.
 4. Decide. If at least one item has (a) platform-permitted reuse, (b) merchant
    written approval, (c) verbatim text, (d) live URL and attribution the
    platform allows: ledger row kind `external-verified`, section
    `testimonial-spotlight` captioned "What people are saying elsewhere" with
    the source named and linked. Never blended into an on-site average.
    STOP. Else tier 5.
```

| Source | May reach the page as | Evidence for the merchant only | Never |
|---|---|---|---|
| Shopify Shop app | synced reviews through tier 1 to 2 with the Shop badge | | copying Shop text outside the synced app |
| Brand site testimonials | quote with evidence of genuineness and contact details on file | | undocumented quotes |
| Brand Instagram or TikTok comments and tagged posts | quote or embed with the author's scoped written consent recorded | shortlist to request consent | a tag or hashtag treated as a licence; platform-licensed music |
| YouTube | official embed of a creator video with the creator's written permission and connection disclosed | shortlist | downloading or re-hosting; quoting comments |
| Customer emails, DMs, WhatsApp | quote with explicit consent for that quote, channel and duration; phone numbers, surnames, avatars redacted; channel and month labelled | shortlist | fabricated chat UI; screenshots without consent |
| Trustpilot | live TrustBox widget on a paid plan; free plan is a plain text link; quotes need reviewer permission or full anonymisation | aggregate and count | static star image; product-score widget on a landing page (Trustpilot brand guidelines Sep 2026) |
| Google Business Profile | Places API with author name, avatar, profile link, link to the source review, no caching, Google logo when off-map | aggregate and count | screenshots; feeding into the site average; expecting rich-result stars |
| Amazon | one dated text line "Rated 4.6/5 by 2,140 Amazon customers (as of Sep 2026)" with a link, screenshot on file | aggregate, themes, objections | verbatim review text; "Best Seller" or "Amazon's Choice" badge art (Amazon trademark licence) |
| Flipkart, Nykaa, Myntra | as Amazon (terms not fetched; applied by analogy) | aggregate, themes | verbatim text |
| Reddit | "Discussed on r/<sub>" with a link; a quote only with the author's written permission | objections, vocabulary | quoting without permission; any use in ads (Reddit Embeds Terms) |
| Creator videos (any platform) | hosted or embedded only with scoped written consent that names "website"; "Paid partnership" when paid | shortlist | organic consent stretched to ads or whitelisting |

## Tier 5: substitutes when no review row exists

Use in this order and stop at the first that verifies. Each is its own ledger
kind; none is review-shaped.

| Order | Kind | Minimum evidence | File |
|---|---|---|---|
| 1 | `guarantee`, `policy-fact` | policy page URL, exact terms (days, conditions, refund vs credit) | `references/offers/offer-ledger.md` |
| 2 | `certification` | issuer, certificate or licence number, scope, current | `references/proof/trust-badges-certifications.md` |
| 3 | `test-data` | lab or study report with method, n, date; numbers copied exactly | `references/proof/before-after-and-claims.md` |
| 4 | `founder-note` | named founder, role stated, approved text, no invented customer voices | `references/proof/before-after-and-claims.md` |
| 5 | `press-quote-linked`, `press-logo-linked` | fetched editorial URL naming the brand | `references/proof/press-and-media-mentions.md` |
| 6 | "first customers" programme | offer terms in the offer ledger; adequate stock (India CCPA bait rule); copy states reviews open after delivery | `references/offers/offer-ledger.md` |
| 7 | nothing | a page without proof is honest; a page with invented proof is a liability | |

## Rules

RS1. Never render a review element that is not a ledger row from tiers 0 to 3 or an `external-verified` row from tier 4. OPERATOR.
Check: each authored review island's `application/json` child binds the
confirmed collection or product scope using its live schema. Every static
quote id appears in the ledger. Inspect source-format JSON, not compiled
`data-props` markers in the source file.

RS2. Run tiers in order and stop at the first tier that yields usable rows; never open tier 4 while tier 1 or 2 has data. OPERATOR.
Check: the plan's "Proof sources" line names the tier reached and the calls made.

RS3. Show an average only at n >= 5, always beside n, to one decimal, computed from all published ratings for the scope. RESEARCH [H] Baymard; LAW (a headline 5.0 from two ratings is misleading by omission, FTC 465.7, CMA "publishing in a misleading way").
Check: every rating string is followed by a count in the same element (review the hits; prices also match the pattern).

RS4. Never show 5.0 unless every review is five stars and n >= 20; never show two decimals. HEURISTIC, mirrors `proof-ledger.md` display rule 3.

RS5. Show the distribution at n >= 20 (optional at 10 to 19, hidden below 10), expanded, every bar present including one-star, bars acting as mutually exclusive filters. RESEARCH [H] Baymard distribution summary.
Check: in the hosted draft the distribution element exists when the ledger's n >= 20 and lists five bars.

RS6. Recency gate: when the newest review is older than 12 months, do not place the average in the hero or buy box; render dated cards only. RESEARCH [M] PowerReviews (64% prefer fewer recent reviews), BrightLocal 2026.
Check: ledger `review-summary` row records newest date; if older than 12 months, section is not `hero`, `buy-box` or `review-summary`.

RS7. Never relabel a store-level aggregate as a product rating, never average bundle components into a bundle rating, never merge reviews across substantially different products or formulations. LAW FTC 465.3; CMA208 "porting"; FTC v. Bountiful ($600k, 2023).
Check: each `review-summary` row names the exact `product_id` or `collectionId` its numbers came from.

RS8. A `minRating` filter is allowed only on a carousel that is labelled as a selection ("Selected reviews"), links to the full list ("Read all n reviews"), and sits with an unfiltered avg + n. Never on the full list, never for `averageRating` or `totalReviews`. LAW FTC 465.7(b); DMCC banned practice 13.

RS9. Negative reviews stay reachable: at n >= 20 at least one review rated 3 or lower is visible without filtering when one exists; sort default is disclosed in one line and does not bury low ratings. LAW FTC 465.7; FTC v. Fashion Nova ($4.2M, 2022); IS 19000 (no discouraging negatives). RESEARCH [H] Baymard: presence of negatives makes positives believable.
Check: hosted draft at 1280 shows the sort label and, for B3+, at least one card with rating <= 3 in the default view.

RS10. Render each review field only when the record contains it (field-gating table). Verified badge only with order linkage or Shop source. LAW EU Annex I 23b (verification is material information); Shopify Shop badge semantics.
Check: no `verified` prop set to true on a static item whose ledger row lacks order linkage; no `avatar` URL that is not the reviewer's own media.

RS11. Quote verbatim. Trim with `[...]` only; keep the reviewer's specifics (variant, timeframe, use); prefer a quote that includes a limitation; never stitch sentences from two reviews; never fix grammar. LAW CAP 3.47; Trustpilot "quote reviews exactly as written"; IS 19000 (administrator may not edit content).
Check: each `review-quote` body is a substring of the API record with `[...]` removed.

RS12. Render merchant replies when present, visually distinct and labelled as the store's reply. RESEARCH [H] Baymard: 37% weigh the reply; 87% of sites never reply.
Check: reply markup uses a distinct class and the label "Reply from <store>".

RS13. Label incentivised reviews on the card and beside the summary when the app flags them; incentives may never be conditioned on sentiment. LAW FTC 465.4 and 465.5; CMA208; Google review-snippet policy.

RS14. Review islands take `collectionId` or `productIds`, `minRating`, `pageSize` <= 12; `averageRating` and `totalReviews` come only from the API total for the same scope; never `reviewsEndpoint`; never `SocialProofPopup`. OPERATOR.

RS15. Only `active` collections bind to `collectionId`; a draft collection is `pending` until the merchant activates it. The plan never activates a collection. OPERATOR.
Check: the `collectionId` in source matches an id returned with `collection_status: "active"` on the plan date.

RS16. `reviews_search` hits are `pending` until the merchant confirms them or an active collection contains them. OPERATOR.
Check: every row with source `reviews_search` has status `verified` only with a confirmation note (question 9 answer or collection id).

RS17. In band B0 render nothing review-shaped. An external item reaches the page only as `external-verified` with a live URL, platform-permitted reuse, merchant written approval, and verbatim text. Marketplace review text (Amazon, Flipkart, Nykaa, Myntra) is never verbatim; Reddit is never used in ads. LAW Amazon Conditions of Use; Reddit User Agreement and Embeds Terms; CAP 3.45.
Check: no `review-*` kind in the ledger when `reviews_status` count is 0; each `external-verified` row has four evidence fields.

RS18. When B0 persists after tier 4, use tier 5 substitutes in order; "nothing" is an acceptable outcome. HEURISTIC.
Check: plan records the substitute chosen and why the higher rows were unavailable.

RS19. Never write, paraphrase, summarise as if quoted, or generate a review; never present staff or founders as customers; never reuse a review for a different product. LAW FTC 16 CFR 465.2 and 465.5; FTC v. Rytr 2024; FTC v. Sunday Riley 2020; India E-Commerce Rules 2020 r.5(2).

RS20. Autoplay video reviews muted only; sound on tap; captions present. LAW WCAG 2.1 SC 1.4.2.

## Regulatory spine

| Jurisdiction | Instrument | In force | Bites on | Penalty | URL |
|---|---|---|---|---|---|
| US | FTC Consumer Reviews and Testimonials Rule, 16 CFR 465 | 21 Oct 2024 | fake or AI reviews (465.2), porting (465.3), sentiment-conditioned incentives (465.4), undisclosed insiders (465.5), suppression (465.7), bought indicators (465.8) | civil penalties per knowing violation | https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials |
| US | FTC Endorsement Guides, 16 CFR 255 | 26 Jul 2023 revision | atypical results (255.2(b)), procuring or editing reviews (255.2(d)), experts (255.3), material connections (255.5) | Section 5 FTC Act; > $50,000 per violation under penalty offence notices | https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising |
| UK | DMCC Act 2024 Sch. 20 banned practice 13; CMA208 | 6 Apr 2025 | fake or concealed incentivised reviews; publishing reviews in a misleading way; no reasonable steps to prevent them | CMA fines up to 10% of global turnover | https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices |
| UK | CAP Code 3.45 to 3.48 | current | evidence and contact details for each testimonial; permission; relates to the advertised product | ASA ruling, ad withdrawn, referral | https://www.asa.org.uk/advice-online/testimonials-and-endorsements.html |
| EU | Directive 2019/2161 amending UCPD, Annex I 23b and 23c, Art. 7(6) | 28 May 2022 | claiming reviews are from purchasers without verification; fake reviews; verification method is material information | national penalties | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32019L2161 |
| India | CPA 2019; CCPA Misleading Ads Guidelines 2022 | 9 Jun 2022 | endorsements must be genuine and current; disclaimers cannot cure | ₹10 lakh first, ₹50 lakh repeat; endorser ban 1 to 3 years | https://consumeraffairs.nic.in/theconsumerprotection/guidelines-prevention-misleading-advertisements-and-endorsements-misleading |
| India | Consumer Protection (E-Commerce) Rules 2020 r.5(2), 7(2) | 2020 | sellers may not pose as consumers and post reviews | CPA 2019 | https://taxguru.in/corporate-law/consumer-protection-e-commerce-rules-2020.html |
| India | BIS IS 19000:2022 | voluntary; QCO proposed May 2024 | no editing review content or ratings; publish moderation criteria; no discouraging negatives | certification of process | https://www.bis.gov.in/scheme-online-review-feb-26/ |

## Sources

- Spiegel Research Center 2017: https://spiegel.medill.northwestern.edu/how-online-reviews-influence-sales/ ; critique: https://cleancommit.io/blog/do-product-reviews-increase-conversion-rate/
- Baymard: https://baymard.com/blog/sort-by-customer-ratings ; https://baymard.com/blog/user-ratings-distribution-summary ; https://baymard.com/blog/respond-to-negative-user-reviews
- PowerReviews: https://www.powerreviews.com/power-of-reviews-2023/ ; https://www.powerreviews.com/right-volume-of-reviews/ ; https://www.powerreviews.com/review-volume-and-recency/
- BrightLocal 2026: https://www.brightlocal.com/research/local-consumer-review-survey/
- FTC FAQ on the reviews rule: https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers
- FTC v. Fashion Nova: https://www.ftc.gov/news-events/news/press-releases/2022/01/fashion-nova-will-pay-42-million-part-settlement-ftc-allegations-it-blocked-negative-reviews
- FTC v. Rytr: https://www.ftc.gov/news-events/news/press-releases/2024/12/ftc-approves-final-order-against-rytr-seller-ai-testimonial-review-service-providing-subscribers
- FTC v. Sunday Riley: https://www.ftc.gov/news-events/news/press-releases/2020/11/ftc-approves-final-consent-agreement-sunday-riley-modern-skincare-llc
- FTC v. Bountiful: https://techcrunch.com/2023/04/10/ftc-orders-supplement-maker-to-pay-600k-in-first-case-involving-hijacked-amazon-reviews/
- CMA208 fake reviews guidance: https://assets.publishing.service.gov.uk/media/67eeb64fe9c76fa33048c790/CMA208_-_Fake_reviews_guidance.pdf
- IS 19000:2022 text: https://www.medianama.com/wp-content/uploads/2022/12/19000_2022.pdf
- Shopify Shop reviews: https://help.shopify.com/en/manual/online-sales-channels/shop/product-reviews ; partner sync: https://help.shopify.com/en/manual/online-sales-channels/shop/product-reviews/sync-partner-apps
- Trustpilot brand guidelines: https://uk.corporate.trustpilot.com/legal/for-businesses/legal-brand-guidelines/sept-2026 ; showcasing reviews: https://help.trustpilot.com/s/article/Share-and-showcase-reviews
- Google Places policies: https://developers.google.com/maps/documentation/places/web-service/policies ; review snippet: https://developers.google.com/search/docs/appearance/structured-data/review-snippet
- Amazon Conditions of Use: https://www.amazon.com/gp/help/customer/display.html?nodeId=GLSBYFE9MGKKQXXM ; trademark licence: https://buywithprime.amazon.com/legal/trademark-license
- Reddit: https://redditinc.com/policies/user-agreement ; https://redditinc.com/policies/embeds-terms
- YouTube terms: https://www.youtube.com/static?template=terms ; Instagram terms: https://help.instagram.com/581066165581870/
- WCAG 1.4.2: https://www.w3.org/WAI/WCAG21/Understanding/audio-control.html

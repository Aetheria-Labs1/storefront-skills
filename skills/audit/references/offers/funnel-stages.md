# Funnel stages

How funnel stage (tof, mof, bof, retention) and Schwartz awareness level
(unaware, problem-aware, solution-aware, product-aware, most-aware) change
what a page may assume, how it opens, how much proof it carries, how hard the
offer pushes, and which page type fits. This file expands section 5 and
section 6 of `references/page-types/_index.md`; the type ids and the
tie-break table there are authoritative. Offer ids are from
`references/offers/offer-types.md`; urgency from
`references/offers/urgency-scarcity.md`; proof kinds from
`references/proof/proof-ledger.md`. Traffic-specific tone lives in
`references/traffic-source-meta.md`, `references/traffic-source-tiktok.md`
and `references/traffic-source-google.md`.

The governing sentence (Schwartz, Breakthrough Advertising, 1966): a headline
that works on a market in one stage of awareness will not work on a market in
another. The page never assumes more awareness than the traffic supplies.

## Stage by awareness

| Stage and awareness | Typical traffic | The page must not assume | Headline leads with | Proof density | Offer aggressiveness | CTA copy pattern | Length | First CTA position | Imagery posture |
|---|---|---|---|---|---|---|---|---|---|
| Pre-tof, unaware | broad social, viral, PR | that they feel the problem or know the category exists | identity, story, a striking fact; never the product, price or discount | low early, builds; founder or expert credibility | none above the fold; `none` or `trial-sample` late | `next-step` ("Keep reading", "See why") | long | after section 4 | editorial lifestyle, people and context; no packshot in the hero |
| tof, problem-aware | cold Meta or TikTok prospecting, native | that solutions exist or that the brand is known | the problem, named in the visitor's words (PAS) | medium; mechanism proof, ingredient or expert, first review quote after the mechanism | soft: `free-shipping`, `trial-sample`, `gwp`, `first-order`; `percent-off` only below the fold after the mechanism | `next-step` or `add-to-cart` after the mechanism ("See how it works", "Try [product]") | long | after the premise: hero for `ad-landing-page`, section 4+ for `advertorial` | in-use and result-or-context; the product appears with the mechanism |
| tof or mof, solution-aware | non-brand search, comparison intent, "best X for Y" | that they know this product or brand | the desired result plus the unique mechanism ("Who else wants ...") | high; `comparison`, `us-vs-them`, case study, review summary | moderate: `bundle`, `first-order`, `subscribe-save` | `next-step` or `shop-collection` ("Compare", "Find your fit", "Get started") | medium to long | hero, restated after the comparison | comparison-visual, detail, product-in-context |
| mof, product-aware | site retargeting, email subscribers, brand search | that desire needs creating; doubt is what needs removing | product name plus the sharpened claim, proof and the differentiator | very high; reviews with media, `before-after` where permitted, `guarantee`, `objections` | moderate, framed as risk reversal: `guarantee`, free returns, `bnpl`, `subscribe-save`; no first-order code | `add-to-cart` ("Add to cart", "Choose your [variant]") | medium | hero | packshot or product-in-hand hero; gallery covers all decision jobs |
| bof, most-aware | cart abandoners, "[brand] discount code" search, VIP list | nothing; do not re-educate | product name plus the deal plus the terms and deadline | light; one `trust-bar` row and a `review-summary` | strongest the ledger verifies: code, `free-shipping`, `gwp`, `fixed-off` | `claim-offer` or `add-to-cart` ("Complete your order", "Claim your [gift]") | short | hero, repeated at the end | packshot; the exact variant they viewed |
| retention | email or SMS to buyers, account, post-purchase | that the brand needs defending | new arrivals, replenish, VIP access, "what changed" | reviews of the new item; the visitor's own purchase history | non-price: `loyalty`, `referral`, early access; `fixed-off` with minimum spend for win-back only | `subscribe` or `add-to-cart` ("Reorder", "Get early access") | shortest | hero | packshot or lifestyle of the new item; continuity cues |

Diagnose the stage from channel, creative and query, not from the merchant's
hope: broad social is problem-aware at best (the ad already named the
problem, so fully unaware is rare); "best X for Y" search is solution-aware;
brand search and retargeting are product-aware or most-aware; "[brand]
discount code" is most-aware.

## Stage changes the page type

Read with the decision tree in `references/page-types/_index.md` section 2.
The same product and offer land on different types by stage.

| Stage and awareness | Buy on this page | First choice | Second choice | Never |
|---|---|---|---|---|
| unaware | no | `advertorial`, `brand-story-founder`, `video-sales-page` | `quiz-funnel`, `lead-capture-giveaway` | `pdp`, `offer-page`, `sale-clearance-flash`, `retargeting-warm`, `restock` |
| problem-aware, social | yes | `ad-landing-page` (single product, one CTA) | `advertorial` when the ad is a story or "I tried" hook; `listicle` when the ad is a number or "reasons" frame; `ugc-creator-collab` when creator video is the hook | `pdp` with full nav; `offer-page`; `bundle-kit` as the first page |
| problem-aware, video | yes or capture | `video-sales-page` | `ad-landing-page` | `sale-clearance-flash` |
| solution-aware, search | yes | `pdp` (search-intent variant) for product or category queries | `comparison-us-vs-them` for "vs" and "alternatives"; `seo-buyers-guide` for "best X" and "top N"; `ingredient-science` for "does X work" | `advertorial`, `listicle` (the searcher wants a ranked answer, not a story or five reasons) |
| solution-aware, social | yes | `pdp-hybrid-landing` when variants or gallery matter | `ad-landing-page`; `trial-sample` when the objection is "will it work for me" | full-nav `pdp` on paid traffic |
| product-aware | yes | `pdp` or `pdp-hybrid-landing` | `bundle-kit`, `subscription`, `retargeting-warm` when the visitor already saw the product | `advertorial`, `listicle` |
| most-aware | yes | `offer-page`, `retargeting-warm` | `sale-clearance-flash` (more than five products), `restock` | any long-read type |
| retention | reorder, refer, browse | `referral-loyalty-vip`, `restock`, `collection-landing` | `thank-you-post-purchase`, `homepage`, `lookbook-shop-the-look` | `ad-landing-page`, `advertorial` |

Silent brief: choose the type that assumes less (`advertorial` over
`ad-landing-page` for unaware audiences; `ad-landing-page` over
`retargeting-warm`), per the tie-break table.

## Bridge page

A bridge (pre-sell) page sits between the ad and the PDP to close the
awareness gap. It is not a page type of its own; it is `advertorial`,
`listicle`, `ad-landing-page`, `comparison-us-vs-them` or `ugc-creator-collab`
chosen by the table above.

| Traffic awareness | The bridge's job | Must answer, in order | Hand-off section | Evidence |
|---|---|---|---|---|
| problem-aware, solution-aware | educate and rank options before the PDP | what it is; why the brand exists; how it improves the visitor's life; why it is the best option; how fast they get it; why they should trust it (Nik Sharma's six) | `offer-bridge` then `closing-cta` to the PDP or cart | OPERATOR: cold TikTok or Meta traffic sent straight to a PDP underperforms; listicles reach 35%+ click-through to the PDP (Sharma Brands) |
| product-aware | stack proof and handle objections | the top three objections (fit, results timeline, returns); the exact variant viewed; the guarantee | `objections` then `buy-box` or `closing-cta` | OPERATOR: retargeting converts 2 to 5x cold prospecting (WordStream via Conversion Studio) |

## Retargeting rules (product-aware and most-aware)

Apply on `retargeting-warm` and on any page whose traffic is retargeting.

| Rule | Detail |
|---|---|
| Skip education | No `problem`, `agitation`, `mechanism` or `how-it-works` above the first CTA; the visitor knows the product |
| Open with proof | `review-summary` or `testimonial-spotlight` in or directly after the hero |
| Objections first | Lead body section is `objections`: the top three for the product (fit, results timeline, returns or cancellation) |
| Offer as risk reversal | `guarantee`, free returns, `bnpl`, `subscribe-save` before any price cut |
| Show what they saw | The exact product and variant viewed or carted; no generic collection |
| No first-order code | They saw it already (offer-types OF8) |
| Never deeper than before | A discount deeper than the one they abandoned on trains abandonment (offer-types OF8) |
| Deadline only if real | `offer.endsAt` bound; text end date otherwise (urgency-scarcity UR2) |

## Cold traffic rules (Meta, TikTok, native)

| Rule | Detail |
|---|---|
| Message match first | The hero repeats the ad's product, outcome, offer and visual context in the first screen (`references/consumer-behavior-cro.md`, Message match); the visitor must not reconstruct the premise |
| Problem before product | On problem-aware pages the product name appears after the problem is named; on unaware pages after the story |
| Price after mechanism | First price element after `mechanism`, `solution` or `how-it-works` and before the first cart or PDP CTA (price-presentation PP19) |
| Offer below the fold | `first-order`, `free-shipping`, `gwp` or `trial-sample` after the mechanism; `percent-off` never in the hero |
| No urgency in the hero | No `countdown`, `stock-indicator` or deadline copy in sections 0 or 1 (urgency-scarcity UR6) |
| No nav | `nav: none` per the type checklist; navigation on paid traffic leaks |
| Proof distributed | Mechanism proof (ingredient, expert, test data) beside the mechanism; the first review quote after it; `review-summary` beside the first CTA |
| Length follows the gap | As long as the awareness gap demands; a most-aware page with long education creates friction between desire and action (Schwartz via Palmer) |
| Market sophistication picks the claim | In a saturated category lead with a new mechanism, not a bigger promise (Schwartz's second axis) |
| TikTok specifics | Creator or UGC video above the fold; vertical media; `references/traffic-source-tiktok.md` |

## Search intent rules (Google)

| Query shape | Awareness | Page type | Page rules |
|---|---|---|---|
| "[brand] [product]" or "[brand]" | product-aware or most-aware | `pdp`, `homepage` | Buy box in the first viewport (design-rules A8); price above the fold; full nav |
| "[category] for [use]", "buy [category]" | solution-aware | `pdp` (search-intent variant), `collection-landing` | Answer-first copy; the product's fit for the use in the first paragraph; comparison to alternatives below |
| "[brand] vs [competitor]", "[competitor] alternative" | solution-aware, evaluative | `comparison-us-vs-them` | Attribute table with only decision-driving attributes; "best for" per option; no manufactured winner (`consumer-behavior-cro.md`, Guided comparison) |
| "best [category]", "top N [category]", "[category] buyer's guide" | problem-aware or solution-aware, exploratory | `seo-buyers-guide` | TOC, methodology, ranked entries with a comparison table; the merchant's product placed where the methodology puts it; full nav; offers only as verified per-entry prices, never a sitewide banner |
| "does [ingredient or category] work", "[ingredient] benefits" | solution-aware, informational | `ingredient-science` | Mechanism and sources first; product after; one CTA late |
| "[brand] discount code", "[brand] coupon" | most-aware | `offer-page` | The code in the hero, auto-applied where possible; terms adjacent; no education |
| "[brand] shipping", "[brand] returns", "[brand] sizing" | product-aware, support | `faq-support-led` | Answer in the first screen; policy facts from the store policy page; one CTA |
| Shopping ads (Google Shopping) | solution-aware or product-aware | `pdp-hybrid-landing` | Landed variant matches the ad's variant and price exactly (bait and switch otherwise); price above the fold |

Search traffic never gets an `advertorial`, a `listicle` or a
`video-sales-page`: the searcher asked a question and wants the answer before
the story; "best X" search goes to `seo-buyers-guide`, "N reasons" paid social
goes to `listicle` (`_index.md` tie-breaks). Tone and schema rules are in
`references/traffic-source-google.md`.

## Rules

FS1. Record `page.funnelStage` and `page.awareness` in `page record` and in the plan's `## Page type` block, diagnosed from channel, creative and query, before choosing the page type. HEURISTIC.
Check: both fields present; `awareness` is one of the five Schwartz values; `funnelStage` is one of `tof`, `mof`, `bof`, `retention`.

FS2. Never assume a higher awareness than the traffic supplies: cold social is problem-aware at best; brand search is product-aware. HEURISTIC (`_index.md` section 5).
Check: `trafficSource` in {`meta`, `tiktok`, `native`} implies `awareness` in {`unaware`, `problem-aware`, `solution-aware`}; `trafficSource: retargeting` implies `awareness` in {`product-aware`, `most-aware`}.

FS3. The chosen page type's checklist `funnel_stage` and `awareness` arrays contain the page record values. HEURISTIC.
Check: the type checklist review passes; the type file's checklist includes both values.

FS4. The offer moves down the page and up in depth as awareness rises: on `tof` types the first offer element follows `mechanism`, `solution` or `how-it-works`; on `bof` types the offer is in the hero. HEURISTIC (offer-types OF7).
Check: section index comparison in `page record` against `funnelStage`.

FS5. Headline leads with the stage's subject: problem for problem-aware, result plus mechanism for solution-aware, product plus claim for product-aware, product plus offer plus terms for most-aware, identity or story for unaware. HEURISTIC.
Check: the `<h1>` on a problem-aware page names no product or brand; on a most-aware page it names the product and the offer.

FS6. No urgency element in the hero or educational sections on `tof` types; no education above the first CTA on `bof` types. HEURISTIC and LAW (urgency-scarcity UR6).
Check: `funnelStage: tof` implies no `countdown` or `stock-indicator` at index 0 or 1; `funnelStage: bof` implies no `problem`, `mechanism` or `how-it-works` before the first `buy-box` or `offer`.

FS7. Proof density follows the table: at least two proof modules distributed through the body on `tof` and `mof` pages, at most one `trust-bar` plus one `review-summary` on `bof` pages. HEURISTIC (page-type checklists set the exact range).
Check: proof module count within the type checklist's `proof.min_modules` to `max_modules`.

FS8. Retargeting pages skip education, open with proof, lead with objections, frame the offer as risk reversal, show the viewed variant, and never show the first-order code or a deeper discount than the visitor saw. OPERATOR and HEURISTIC.
Check: `pageType: retargeting-warm` implies section order matches the table above and `offer.type` is not `first-order`.

FS9. Cold social pages match the ad's message in the first screen and hold price until after the mechanism. HEURISTIC and OPERATOR.
Check: the plan's "Message match" line identifies the supplied creative or campaign message; price-presentation PP19 check passes.

FS10. Search pages answer first and never use `advertorial`, `listicle` or `video-sales-page`; "best" and "top N" queries land on `seo-buyers-guide`. HEURISTIC.
Check: `trafficSource` in {`google-search`, `google-shopping`} implies `pageType` not in {`advertorial`, `listicle`, `video-sales-page`}; `pageType: seo-buyers-guide` implies `trafficSource` in {`google-search`, `organic`}.

FS11. CTA copy follows the stage: `next-step` on unaware and problem-aware pages, `add-to-cart` from solution-aware onward, `claim-offer` only on most-aware; "Buy now" is never the primary CTA on `tof` or `mof` pages (design-rules A12 forbids it as generic copy anyway). HEURISTIC.
Check: `cta.copy_pattern` in the type checklist matches the stage; CTA wording satisfies A12.

FS12. Length follows the awareness gap: no long-read type for most-aware traffic, no short offer page for unaware traffic. HEURISTIC.
Check: `awareness: most-aware` implies section count at or below the `offer-page` or `retargeting-warm` checklist maximum; `awareness: unaware` implies `pageType` in the unaware row of the type table.

FS13. Retention pages lead with non-price incentives (early access, points, reorder); a price cut appears only as `fixed-off` with minimum spend for a win-back segment. OPERATOR (CTC; Seguno segmented codes 1.68x AOV).
Check: `funnelStage: retention` implies `offer.type` in {`none`, `loyalty`, `referral`, `subscribe-save`, `bundle`, `fixed-off`, `gwp`, `limited-edition`, `gift-card`}.

## Sources

- Schwartz's five awareness stages, mapped to page formats (Landra): https://www.getlandra.com/blog/5-stages-of-awareness ; Rob Palmer on Breakthrough Advertising: https://robpalmer.com/blog/eugene-schwartz-breakthrough-advertising-lessons
- Nik Sharma on bridge pages and cold traffic: https://askthepods.com/episode/the-importance-and-value-of-landing-pages-nik-sharma-sharma-brands-bonus-episode ; https://sharmabrands.com/blogs/newsletter/how-to-scale-a-brand-to-5-million-in-revenue ; https://www.nik.co/you-launched-your-brand-now-wtf-do-you-do
- Retargeting versus prospecting conversion (WordStream via Conversion Studio): https://conversion.studio/blog/customer-awareness-stages
- Seguno segmented and unique code benchmarks: https://www.seguno.com/unique-discount-code-benchmarks
- Common Thread Collective on VIP incentives: https://commonthreadco.com/blogs/ecommerce-playbook/dig-in-bfcm-offer-database-2023
- Welcome-offer benchmarks and returning-visitor caps: https://farabiulder.com/blog/welcome-offer-benchmarks ; https://www.metricuno.com/exit-intent-popups
- Baymard on familiar CTA wording and PDP composition: https://baymard.com/research/product-page

# Page Types: Identification Framework

Every storefront page is one of the thirty types below. `/plan-page` picks
exactly one before it searches templates, assets or proof, records it in the
`## Page type` block and in `page.pageType`, and then loads only that type's
file. `/design-page` and `/optimize` re-read the same file. Each
type file follows `references/page-types/_checklist-format.md` and ends with
a JSON checklist shared by the workflow and repository contract tests.

## 1. Inputs to read from the brief

Extract these seven facts before choosing. Ask only for the ones that change
the answer and that the catalog, brand, campaign and analytics cannot supply.

| Input | Values | Where it usually comes from |
|---|---|---|
| Traffic source | meta, tiktok, google-search, google-shopping, email, sms, organic, direct, influencer, affiliate, retargeting, marketplace | brief, `lexsis_campaigns.creatives`, analytics |
| Funnel stage | tof (cold), mof (warm), bof (hot), retention (owned) | traffic + whether the visitor has seen the product |
| Awareness (Schwartz) | unaware, problem-aware, solution-aware, product-aware, most-aware | traffic + ad creative + audience description |
| Desired action | buy now, add to cart, start quiz, join waitlist, subscribe, capture email, read then buy, browse, refer, reorder | brief |
| Product count | 1 SKU, 1 product with variants, 2 to 5 (kit/compare), 6 to 40 (collection), whole store | catalog |
| Offer shape | an offer id from `references/offers/offer-types.md`: `none`, `first-order`, `percent-off`, `fixed-off`, `bogo`, `gwp`, `bundle`, `bundle-decoy`, `subscribe-save`, `free-shipping`, `tiered-volume`, `pre-order-price`, `trial-sample`, `flash-sale`, `clearance`, `limited-edition`, and the rest of that list | brief, merchant |
| Campaign trigger | a campaign id from `references/offers/campaign-calendar.md`: `evergreen`, `launch`, `restock`, `seasonal`, `gifting`, `flash-sale`, `clearance`, `collab-drop`, `anniversary`, `cause`, `back-to-school`, `bfcm`, `end-of-season`, `founder-sale` | brief, calendar |

## 2. Decision tree

Walk top to bottom; stop at the first leaf that fits. Tie-breaks are in
section 4.

```text
Is the visitor's job to BUY (or add to cart) on this page?
+-- no - what is the job?
|   +-- answer questions / route to the right product ........... quiz-funnel
|   +-- leave an email or phone (giveaway, waitlist, early access)
|   |   +-- product not yet purchasable ....................... launch-waitlist-preorder
|   |   +-- incentive or contest ............................... lead-capture-giveaway
|   +-- read a story, learn who we are ......................... brand-story-founder
|   +-- understand the science, ingredients, materials, method . ingredient-science
|   +-- browse many products
|   |   +-- whole store, first visit ........................... homepage
|   |   +-- one category or collection ......................... collection-landing
|   |   +-- by recipient or price for a holiday ................ gift-guide
|   |   +-- outfits, rooms, looks with shoppable items ......... lookbook-shop-the-look
|   +-- get help, policies, answers ............................ faq-support-led
|   +-- refer a friend, join a programme, see tiers ............ referral-loyalty-vip
|   +-- just paid; what next .................................... thank-you-post-purchase
|   +-- order in volume for resale ............................. wholesale-b2b
+-- yes - has the visitor already seen this product or brand?
    +-- no (cold) - what brought them?
    |   +-- a social ad with a story or problem hook (meta, tiktok, native)
    |   |   +-- long-read wanted, price hidden until late ...... advertorial
    |   |   +-- "N reasons / best X" list framing ............. listicle
    |   |   +-- creator or customer video is the hero .......... ugc-creator-collab
    |   |   +-- one long video does the selling ................ video-sales-page
    |   |   +-- direct-response, single product, single CTA .... ad-landing-page
    |   +-- a search for the product or category (google, shopping)
    |   |   +-- "X vs Y", "alternatives" ....................... comparison-us-vs-them
    |   |   +-- "best X", "top N X", buyer's guide, roundup ..... seo-buyers-guide
    |   |   +-- product or category intent ..................... pdp (search-intent variant)
    |   +-- a sample, trial or starter offer ................... trial-sample
    +-- yes (warm or hot) - what is the page selling?
        +-- one product at full price, full store context ....... pdp
        +-- one product, paid-traffic focus, no navigation ...... pdp-hybrid-landing
        +-- two or more products as a set or configurator ....... bundle-kit
        +-- a recurring plan ..................................... subscription
        +-- a specific discount, code, GWP or BOGO .............. offer-page
        +-- many products at reduced prices for a window ........ sale-clearance-flash
        +-- an occasion or holiday assortment .................... seasonal-gifting
        +-- a product that is back or newly available ............ restock
        +-- a return visit after abandonment or a prior view ..... retargeting-warm
```

## 2b. Keyword lookup

A fast first pass before the tree. The tree still decides.

| Brief says | Type |
|---|---|
| "5 reasons", "top 7", "reasons why", "things you didn't know" (paid social, one product) | `listicle` |
| "best X", "top N X for Y", "buyer's guide", "roundup" (search intent) | `seo-buyers-guide` |
| "story", "article", "editorial", "we tried it", "here's what happened", native placement | `advertorial` |
| "vs", "compared to", "alternative to", "why switch" | `comparison-us-vs-them` |
| "find your", "which one is right", "shade finder", "size finder" | `quiz-funnel` |
| "bundle", "kit", "starter set", "build your own", "routine" | `bundle-kit` |
| "% off", "BOGO", "free gift", "GWP", "code", "deal" without a hard end | `offer-page` |
| "sale", "flash", "clearance", "ends", "48 hours" | `sale-clearance-flash` |
| "BFCM", "Diwali", "Rakhi", "Valentine", "Mother's Day", "Eid", "Christmas" with a buying window | `seasonal-gifting` |
| "gift guide", "gifts for", "under ₹999" without a hard date | `gift-guide` |
| "launch", "coming soon", "waitlist", "pre-order", "drop" | `launch-waitlist-preorder` |
| "restock", "back in stock", "notify me" | `restock` |
| "subscribe", "auto-ship", "membership" | `subscription` |
| "creator", "influencer", "collab", "x [name]", "code [NAME]" | `ugc-creator-collab` |
| "video", "VSL", "watch the presentation" | `video-sales-page` |
| "about", "our story", "founder", "why we started" | `brand-story-founder` |
| "ingredients", "science", "how it works", "clinical", "studies" | `ingredient-science` |
| "shop all", "collection", "category", "browse" | `collection-landing` |
| "homepage", "home" | `homepage` |
| "lookbook", "shop the look", "outfit", "styled" | `lookbook-shop-the-look` |
| "thank you", "order confirmation", "after checkout" | `thank-you-post-purchase` |
| "giveaway", "enter to win", "newsletter", "10% for email", "text club" | `lead-capture-giveaway` |
| "refer", "rewards", "VIP", "loyalty", "points" | `referral-loyalty-vip` |
| "retarget", "came back", "visited but didn't buy", "abandoned" | `retargeting-warm` |
| "FAQ", "help", "support", "questions" | `faq-support-led` |
| "sample", "trial", "try before you buy", "home try-on" | `trial-sample` |
| "wholesale", "B2B", "stockists", "bulk" | `wholesale-b2b` |
| "landing page", "LP", "ad page", "post-click" for one product | `ad-landing-page` (or `pdp-hybrid-landing` when variants or gallery matter) |
| "product page", "PDP", brand search, Google Shopping | `pdp` |
| "microsite", "campaign hub" | the type of its main page; other pages are separate plans |
| "mobile first", "one thumb" | a modifier, not a type; every type is mobile-first already |

## 3. Type catalogue

`Length` is sections between chrome. `Proof` is the checklist's module range.
`Nav` is the checklist value.

| Type id | One line | Stage | Awareness | Typical traffic | Length | CTAs | Proof | Nav |
|---|---|---|---|---|---|---|---|---|
| `ad-landing-page` | Single product, single CTA, message-matched to a paid ad | tof/mof | problemU+2192product | meta, tiktok, google | 8-11 | 3 | 2-4 | none |
| `pdp` | Full product page inside the store; gallery, buy box, details, reviews | mof/bof | product/most | organic, search, email, nav | 7-11 | 2 | 2-4 | full |
| `pdp-hybrid-landing` | PDP anatomy with landing-page focus: no nav, ad message match, one goal | mof | solutionU+2192product | meta, google shopping | 8-11 | 2-3 | 2-4 | none |
| `advertorial` | Editorial article that sells by story; price and CTA arrive late | tof | unaware/problem | meta, native, tiktok | 8-12 | 1-3 | 2-4 | none |
| `listicle` | Numbered reasons for one product; each reason answers an objection and earns a click | tof/mof | problem/solution | meta, tiktok | 8-13 | 3-6 | 2-4 | none/minimal |
| `seo-buyers-guide` | Search-intent roundup or "best X" guide: TOC, methodology, ranked entries, comparison table | tof/mof | problem/solution | google organic, google ads | 9-14 | per entry + 1 | 2-4 | full |
| `comparison-us-vs-them` | Attribute table against named or generic alternatives | mof | solution/product | google, retargeting | 7-10 | 2-3 | 2-3 | minimal |
| `quiz-funnel` | Questions route the visitor to a recommendation | tof/mof | problem/solution | meta, tiktok, email | 4-7 | 1 + result | 1-2 | none |
| `bundle-kit` | Fixed or build-your-own set with visible savings math | mof/bof | product | email, pdp cross-link, ads | 7-10 | 2 | 2-3 | minimal/full |
| `offer-page` | One named promotion (code, GWP, BOGO, first order) | mof/bof | product/most | email, sms, retargeting | 6-9 | 2-3 | 1-3 | minimal |
| `sale-clearance-flash` | Many products, reduced prices, real window | bof | most | email, sms, social | 5-8 | per card | 1-2 | full |
| `seasonal-gifting` | Occasion assortment with delivery cutoffs and gift options | mof | solution/product | email, social, search | 7-10 | per card + 1 | 1-3 | full |
| `gift-guide` | Curated picks by recipient or price band | tof/mof | solution | organic, email, social | 6-9 | per card | 1-2 | full |
| `launch-waitlist-preorder` | Not yet buyable: capture intent or take pre-orders | tof/mof | problem/solution | email, social, PR | 6-9 | 1-2 | 1-3 | minimal |
| `restock` | Product is back; convert the demand already there | bof/retention | most | email, sms | 5-7 | 2 | 1-2 | minimal |
| `subscription` | Recurring plan; cadence, savings, cancellation clarity | mof/bof | product | pdp, email, ads | 7-10 | 2 | 2-3 | minimal/full |
| `ugc-creator-collab` | Creator or customer content is the hero and the proof | tof/mof | problem/solution | tiktok, instagram, influencer | 6-9 | 2-3 | 3-5 | none |
| `video-sales-page` | One long video, then the offer | tof/mof | problem/solution | meta, youtube, email | 5-8 | 1-2 | 1-3 | none |
| `brand-story-founder` | Who we are and why; sells belief, not a SKU | tof/retention | unaware/problem | organic, nav, PR | 6-9 | 1-2 | 1-2 | full |
| `ingredient-science` | Mechanism, ingredients, materials, studies | mof | solution/product | organic, pdp link, google | 7-10 | 1-2 | 2-4 | full |
| `collection-landing` | One category; grid with filters and a short story | mof | solution | organic, nav, google | 5-8 | per card | 1-2 | full |
| `homepage` | Store front door; route to collections, best sellers, story | tof/retention | all | direct, organic, brand search | 7-10 | 2-3 | 2-3 | full |
| `lookbook-shop-the-look` | Editorial imagery with shoppable items | tof/mof | solution | instagram, organic, email | 5-8 | per look | 1-2 | full |
| `lead-capture-giveaway` | Email or SMS in exchange for an incentive | tof | unaware/problem | social, partner, ads | 3-6 | 1 | 1-2 | none |
| `referral-loyalty-vip` | Programme rules, tiers, rewards, join | retention | most | email, account, nav | 5-8 | 1-2 | 1-2 | full |
| `retargeting-warm` | Visitor saw it already; handle objections, restate offer | bof | product/most | meta/google retargeting | 5-8 | 2-3 | 2-4 | none/minimal |
| `thank-you-post-purchase` | Order confirmed; next steps, one relevant add-on, referral | retention | most | checkout | 3-6 | 1-2 | 0-1 | minimal |
| `faq-support-led` | Answers first; policies, shipping, sizing, care | mof/retention | product | organic, nav, support links | 4-7 | 1 | 0-2 | full |
| `trial-sample` | Low-risk first purchase; what happens after is explicit | tof/mof | solution | ads, email | 6-9 | 2 | 2-3 | minimal |
| `wholesale-b2b` | MOQ, tiers, lead times, line sheet, inquiry | mof | product | organic, outreach | 5-8 | 1-2 | 1-3 | minimal |

## 4. Tie-breaks between near neighbours

| If torn between | Choose | Because |
|---|---|---|
| `ad-landing-page` vs `pdp-hybrid-landing` | hybrid when the product has 3+ variants or a gallery that matters; ad-landing otherwise | hybrid keeps PDP buy mechanics; ad-landing keeps one story |
| `ad-landing-page` vs `advertorial` | advertorial when awareness is unaware/problem-aware and the ad is a story or "I tried" hook | cold readers need the premise before the price |
| `advertorial` vs `listicle` | listicle when the ad or search phrase is a number or "best/top/reasons" | frame must match the click |
| `listicle` vs `comparison-us-vs-them` | comparison when the visitor named a competitor or searched "vs" | intent is evaluative, not exploratory |
| `listicle` vs `seo-buyers-guide` | buyer's guide when traffic is search and the query is "best/top N"; listicle when traffic is paid social and the page sells one product | search readers expect a ranked, methodical roundup; social readers expect five reasons |
| `pdp` vs `pdp-hybrid-landing` | hybrid whenever the traffic is paid and the brief wants one goal | navigation on paid traffic leaks |
| `bundle-kit` vs `offer-page` | bundle when the value is the set; offer when the value is the discount | anatomy differs: savings math vs offer terms |
| `offer-page` vs `sale-clearance-flash` | sale when more than five products are discounted | grid, not buy box |
| `seasonal-gifting` vs `gift-guide` | gifting when there is a purchase window with cutoffs and gift options; guide when it is curation without a hard date | cutoff logic vs editorial |
| `launch-waitlist-preorder` vs `restock` | restock when the product sold before and has review data | proof exists |
| `ugc-creator-collab` vs `video-sales-page` | VSL when one long video carries the pitch; UGC when many short clips do | one hero vs many proofs |
| `retargeting-warm` vs `offer-page` | retargeting when the offer is secondary to objection handling | different first screen |
| `quiz-funnel` vs `lead-capture-giveaway` | quiz when answers change the recommendation; capture when they do not | a quiz that does not route is a form |
| `homepage` vs `collection-landing` | collection when one category is named | scope |
| `brand-story-founder` vs `ingredient-science` | science when the brief names ingredients, studies or "how it works" | mechanism vs meaning |
| Brief is silent on stage | the type that assumes less (`ad-landing-page` over `retargeting-warm`, `advertorial` over `ad-landing-page` for unaware audiences) | over-assuming knowledge loses cold visitors |

## 5. Awareness level U+2192 headline and page posture

Eugene Schwartz's five stages decide how much the page may assume and what
the headline leads with.

| Awareness | Visitor knows | Headline leads with | Page posture | Types |
|---|---|---|---|---|
| unaware | nothing relevant | a story, an identity, a surprising fact; never the product | educate first, price last | advertorial, brand-story, video-sales |
| problem-aware | the pain, not the fix | the problem named in their words | agitate briefly, reveal mechanism, then product | advertorial, listicle, ad-landing, quiz |
| solution-aware | the category, not you | the mechanism or outcome and why this one | differentiate, compare, prove | ad-landing, comparison, ingredient-science, ugc |
| product-aware | your product, not enough to buy | the product name plus the strongest claim or offer | proof, price clarity, risk reversal | pdp, hybrid, bundle, subscription, retargeting |
| most-aware | wants it; needs the deal or the nudge | product plus offer plus terms | buy box first, no education | offer, sale, restock, thank-you |

Rule: a page never assumes a higher awareness than the traffic supplies. Cold
social traffic is problem-aware at best. Brand search is product-aware.

## 6. Funnel stage defaults

| Stage | Assume | Proof density | Offer aggressiveness | Copy length | First CTA |
|---|---|---|---|---|---|
| tof | nothing; explain the premise | high, early and distributed | low; `first-order` or `free-shipping` in view, `gwp` or `trial-sample` only below the fold | longest | after the premise (hero for ad-landing; section 4+ for advertorial) |
| mof | category known; brand not trusted | high, beside claims | moderate; bundle, subscribe-and-save, GWP | medium | hero |
| bof | product known; objections remain | targeted; answer the objection | highest that the ledger verifies | short | hero, repeated |
| retention | brand trusted | light; continuity cues | loyalty, referral, reorder | shortest | hero |

`references/offers/funnel-stages.md` expands this table.

## 7. Recording the choice

Plan block (`page plan`):

```markdown
## Page type

**Type.** advertorial
**Funnel stage.** tof
**Awareness.** problem-aware
**Traffic.** meta
**Offer.** first-order
**Campaign.** evergreen
**Copy framework.** story-lead
**Mandatory sections omitted.** none
```

Manifest (`page record`): `page.pageType`, `page.funnelStage`,
`page.awareness`, `page.trafficSource`, plus `offer` and `campaign` blocks
(`references/page-files.md`).

## 8. Benchmarks and what they are worth

Use benchmarks to set relative expectations (quiz > landing page > PDP for
cold traffic; PDP beats a landing page for hot and branded-search traffic),
never as promised outcomes. Print the caveat with the number.

| Metric | Value | Source | Caveat |
|---|---|---|---|
| Median landing-page conversion, all industries | 6.6% | Unbounce Conversion Benchmark Report Q4 2024, https://unbounce.com/conversion-benchmark-report/ | counts form fills and other goals, not purchases |
| Ecommerce landing-page conversion | 2.35% to 4.2% | same report; summaries of the same data disagree | quote the range, never one number |
| Ecommerce landing page by channel | email 28.6%, paid search 5.1 to 5.7%, paid social 4.8% | https://unbounce.com/conversion-benchmark-report/ecommerce-conversion-rate/ | traffic source moves conversion more than page design |
| Reading level | grade 5 to 7 pages 5.6% vs professional 1.5% | same | correlational |
| Ecommerce landing-page word count | 285 to 930 words | same | classic landing page only, not advertorial |
| Average Shopify store conversion | 1.4% (top 20% above 3.2%, top 10% above 4.7%) | Littledata, https://www.littledata.io/ecommerce-conversion-rate | average across ~2,800 stores, 2023 |
| Shopify add-to-cart rate | 4.6% of sessions (top 10% above 9.6%) | Littledata | low ATC is a product-page problem |
| Cart abandonment | 70.2% mean of 50 studies | https://baymard.com/lists/cart-abandonment-rate | 42% "just browsing" is unavoidable |
| Landing page vs PDP by traffic heat | cold LP 3.8% vs PDP 2.4%; hot (cart abandoners) LP 6.5% vs PDP 7.2%; branded search LP 5.1% vs PDP 6.8% | https://mhigrowthengine.com/blog/landing-page-vs-product-page-dtc/ | practitioner averages |
| Cold Facebook traffic straight to PDP | about 0.5%; with an advertorial in between 3 to 5% | TrueProfit via https://www.getlandra.com/blog/advertorial-listicle-conversion-statistics | vendor, directional |
| Quiz results pages | one results page 10.6% vs 7.1% with 11 or more | https://docs.revenuehunt.com/customer-success/how-to-build-successful-quiz/ | vendor data |
| Back-in-stock alerts | about 25% when sent within 15 minutes, 10% after 4 hours | Klaviyo via https://ustechautomations.com/resources/blog/ecommerce-back-in-stock-notifications-how-to-2026 | vendor |
| Post-purchase one-click upsell | 3 to 8% take rate; thank-you page upsells about 1% | https://zipify.com/blog-post-purchase-upsells-shopify-2026/ | vendor network |
| Urgency | real promo countdown +8.3%; generic timer -11.4% revenue; cart urgency flat | https://crometrics.com/blog/urgency-that-actually-works/ | agency test portfolio |
| Sticky add-to-cart | -7.7% to +26% across tests | see `references/anti-patterns/cro-anti-patterns.md` | mixed; test, do not assume |
| Reading | users read about 20 to 28% of words; paragraph 4 gets 32% of eyes | https://www.nngroup.com/articles/how-little-do-users-read/ , https://www.nngroup.com/articles/website-reading/ | subheads carry long pages |

## 9. Universal rules across every type

1. Message match: the H1 restates the promise of the ad, email or creator
   post that sent the click (`references/copy/message-match.md`).
2. One destination: on single-goal types every CTA points at the same next
   step.
3. Mobile first: hero, first proof and CTA survive the first 390px screen as
   the type file lists them.
4. Proof is specific and checkable, and comes from the Proof ledger.
5. Urgency is real, specific and server-anchored, from the Offer ledger.
6. Plain language: grade 6 to 8, short paragraphs, a subhead every 300 to 500
   words on long pages.
7. A reviews block with 5 or more reviews shows the ratings distribution and
   lets it filter; below 5 it shows the count and quotes only.
8. Hero media is compressed and preloaded (`references/assets/slot-spec.md`).
9. Advertorials carry a visible "Advertisement" or "Sponsored" label;
   health claims stay within what the ledger substantiates.
10. Never send cold prospecting traffic to the homepage.

## 10. What the type does not decide

Vertical (`references/vertical-*.md`), traffic source
(`references/traffic-source-*.md`) and brand design layer on top of the type.
The type fixes anatomy, proof density, CTA logic, price timing and imagery
jobs. The vertical fixes which modules fill those slots (ingredient explorer
for beauty, supplement-facts panel for supplements, size guide for fashion).
The traffic file fixes tone and message match. House rules
(`references/design-rules.md`) override all three.

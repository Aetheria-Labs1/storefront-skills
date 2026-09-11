# Dark patterns

Catalogue of deceptive interface practices a generated page must never
contain. Each entry gives the regulator's definition, an ecommerce example,
the page-builder rule, a severity and a check. `/plan-page` applies these when
it writes the Offer ledger; `/design-page` applies them in Compose step 6;
the source/hosted review runs the O1 to O4 checks. Offer-specific detail lives in
`references/offers/offer-ledger.md`, `references/offers/price-presentation.md`
and `references/offers/urgency-scarcity.md`; proof detail in
`references/proof/proof-ledger.md`. This file is the canonical list; the two
offer files and `references/consumer-behavior-cro.md` (Guardrails) point here.

Severity: BLOCK (legal exposure; the page does not ship), FAIL (fix before
publish), WARN (fix unless the plan records a reason). Tag: LAW (a regulator
names it), RESEARCH (usability evidence), OPERATOR (practitioner consensus),
HEURISTIC (this project's judgement).

Inspect the persisted source and hosted purchase flow.

## 1. Regulatory frame

| Regime | Scope | Status | Text |
|---|---|---|---|
| India CCPA, Guidelines for Prevention and Regulation of Dark Patterns, 2023 | 13 named patterns in Annexure 1; applies to all platforms, advertisers and sellers offering goods or services in India; list extensible | In force since 30 Nov 2023; self-audit advisory 5 Jun 2025 with notices issued | https://consumeraffairs.nic.in/theconsumerprotection/guidelines-prevention-and-regulation-dark-patterns-2023 ; https://consumeraffairs.nic.in/latestnews/ccpa-advisory-terms-consumer-protection-act-2019-self-audit-e-commerce-platforms |
| US FTC, Bringing Dark Patterns to Light (Sep 2022) | Four buckets: induce false beliefs; hide or delay material information; unauthorised charges (ROSCA); obscure privacy choices | Staff report; enforced under FTC Act s.5 and ROSCA | https://www.ftc.gov/system/files/ftc_gov/pdf/P214800%20Dark%20Patterns%20Report%209.14.2022%20-%20FINAL.pdf |
| US FTC, Rule on the Use of Consumer Reviews and Testimonials, 16 CFR 465 | Fake or AI-generated reviews, bought reviews, insider reviews, suppression of negative reviews | Final rule 14 Aug 2024; civil penalties | https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials |
| US FTC, Endorsement Guides, 16 CFR 255 (2023) | Disclosure of material connections; typicality of results claims | Guides; enforced under s.5 | https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising |
| US ROSCA (15 USC 8401) | Disclose material terms before billing information; express informed consent; simple cancellation | In force. The 2024 amended Negative Option Rule was vacated by the Eighth Circuit on 8 Jul 2025; ROSCA and state auto-renewal laws still apply | https://ecf.ca8.uscourts.gov/opndir/25/07/243137P.pdf |
| EU DSA Art. 25 | Platforms may not design interfaces that deceive, manipulate or materially distort decisions; names prominence bias, repeated prompts, harder-to-cancel | In force since 17 Feb 2024 (platforms; single-brand stores fall under UCPD) | https://www.digitalacts.eu/regulation/digital-service-act/article/25/online-interface-design-and-organisation |
| EU UCPD Annex I | Blacklist incl. false limited-availability statements (item 7), advertorial without disclosure (item 11), "free" that costs (item 20) | In force for all B2C traders | https://www.europarl.europa.eu/RegData/etudes/ATAG/2025/767191/EPRS_ATA(2025)767191_EN.pdf |
| CJEU Planet49, C-673/17 | Pre-ticked boxes are not consent | Judgment 1 Oct 2019 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A62017CJ0673 |
| UK CMA, Online Choice Architecture (Apr 2022) + DMCC Act 2024 | 21 practices; drip pricing, reference pricing, sludge, forced outcomes starred as almost always harmful; CMA direct fines up to 10 percent of global turnover from 6 Apr 2025 | Guidance + statute | https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1066524/Online_choice_architecture_discussion_paper.pdf ; https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices |
| deceptive.design (Brignull) | Reference taxonomy: sneaking, hidden costs, hidden subscription, trick wording, confirmshaming, fake scarcity, fake urgency, fake social proof, forced action, hard to cancel, preselection, obstruction, nagging, disguised ads, visual interference, comparison prevention | Taxonomy, not law | https://deceptive.design/types/ |
| EU Digital Fairness Act (proposal) | Expected to codify dark patterns and switch addictive design (infinite scroll, autoplay) off by default | Proposal expected end 2026 | https://www.dentons.com/en/insights/articles/2026/june/9/the-digital-fairness-act-dark-patterns-addictive-designs-and-influencer-marketing |

Prevalence (CMA evidence review): 75 percent of the top 200 US ecommerce sites carried at least one impulse-buying choice-architecture practice; the ICPEN/OECD 2021 sweep of 1,300 sites found over a fifth with harmful practices, led by pre-ticked defaults, scarcity claims and drip pricing. https://www.gov.uk/government/publications/online-choice-architecture-how-digital-design-can-harm-competition-and-consumers/evidence-review-of-online-choice-architecture-and-consumer-and-competition-harm

## 2. Catalogue

### DP1. False urgency (timers)  BLOCK  LAW
- Definition. CCPA Annexure 1, item 1: "falsely stating or implying the sense of urgency or scarcity so as to mislead a user into making an immediate purchase". FTC bucket I: countdown timers on offers that are not time-limited. UCPD Annex I item 7. CMA: countdown clocks that reset.
- Example. A "Sale ends in 14:59" timer that restarts on every page load; "limited time" sales where the same deal continues after the deadline (Emma Sleep undertakings, 22 May 2026: https://www.gov.uk/cma-cases/emma-group-consumer-protection-case ).
- Rule. A countdown binds to the Offer ledger's confirmed `endsAt` (ISO datetime with timezone), disappears after it, and the deal actually ends. No per-session, per-visitor or resetting timers. No "ends soon" in static copy.

### DP2. Fake scarcity (stock)  BLOCK  LAW
- Definition. CCPA item 1(ii): "stating that quantities of a particular product or service are more limited than they actually are". FTC: "almost sold out" with ample supply. UK banned practice: pretending a product is available only for a very limited time.
- Example. "Only 3 left!" hardcoded in copy on a made-to-order item; "Low stock" badge on every variant.
- Rule. Stock statements come only from a live inventory binding (`lexsis_catalog.get` at render) and read the real count. "Limited edition" states the run size from the ledger. No stock words in static copy.

### DP3. Fake popularity (viewer and purchase counts)  BLOCK  LAW
- Definition. CCPA item 1(i): "showing false popularity of a product or service". FTC bucket I: false "others are viewing" and "recently purchased" notices. deceptive.design: fake social proof.
- Example. "23 people are viewing this" from a random-number script; "Priya from Mumbai just bought" popups with no order behind them.
- Rule. No viewer counts, activity feeds or "recently bought" toasts of any kind, even if fed by analytics; the proof vocabulary lists `social-proof-popup` and `live-viewer-count` as never rendered. Aggregate counts ("over 51,000 customers") only as verified proof-ledger rows.

### DP4. Basket sneaking  BLOCK  LAW
- Definition. CCPA item 2: "inclusion of additional items such as products, services, payments to charity or donation at the time of checkout from a platform, without the consent of the user, such that the total amount payable by the user is more than the amount payable for the product(s) and/or service(s) chosen by the user". Free samples and disclosed necessary fees are exempt.
- Example. Sports Direct added a GBP 1 magazine to every basket (https://deceptive.design/types/sneaking ); shipping protection auto-added in the cart drawer.
- Rule. Nothing enters the cart that the shopper did not tap. Cart-drawer add-ons are opt-in buttons, not pre-added lines. A bundle is one product the shopper chose, not silently combined items.

### DP5. Preselection (pre-ticked paid add-ons and consent)  BLOCK  LAW
- Definition. deceptive.design "preselection"; CJEU Planet49: pre-ticked boxes are not consent; GDPR Recital 32; EU Consumer Rights Directive Art. 22: no default options that require payment; CCPA basket sneaking covers paid defaults.
- Example. Gift wrap, insurance, donation, warranty, or "Subscribe and save" ticked by default; marketing checkbox pre-checked under the email field.
- Rule. No `checked` on any checkbox or radio whose label carries a price, a cadence, or a consent verb. Purchase type defaults to one-time. Marketing and SMS consent boxes start unchecked and are never `required`.
- Check.

### DP6. Confirmshaming  BLOCK  LAW
- Definition. CCPA item 3: "using a phrase, video, audio or any other means to create a sense of fear or shame or ridicule or guilt in the mind of the user so as to nudge the user to act in a certain way". Amazon's "No, I don't want Free Shipping" decline button is now banned by court order (https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-secures-historic-25-billion-settlement-against-amazon ).
- Example. "No thanks, I like paying full price"; "I don't care about my skin".
- Rule. Decline and close labels are neutral: "No thanks", "Close", "Not now", "Continue without". No first-person self-deprecation, no consequence framing, no sarcasm.

### DP7. Forced action  BLOCK  LAW
- Definition. CCPA item 4: "forcing a user into taking an action that would require the user to buy any additional good(s) or subscribe or sign up for an unrelated service or share personal information, in order to buy or subscribe to the product or service originally intended by the user". Baymard: 18 to 19 percent of US shoppers abandoned a checkout because the site wanted an account. https://baymard.com/lists/cart-abandonment-rate
- Example. Email gate before the price is shown; "Create an account to continue"; forced app download.
- Rule. Guest checkout is the primary path. No gate on price, shipping, reviews or the CTA. Email and phone are asked once, optional unless needed for delivery, and marketing consent is separate.

### DP8. Subscription trap, hard to cancel, roach motel  BLOCK  LAW
- Definition. CCPA item 5: making cancellation "impossible or a complex and lengthy process", hiding the cancel option, forcing payment details for a free trial, or giving "ambiguous instructions for cancellation". ROSCA: simple cancellation mechanism. DSA Art. 25(3)(c): termination may not be harder than subscribing. FTC v. Amazon, Vonage (USD 100M, 2022: https://www.ftc.gov/news-events/news/press-releases/2022/11/ftc-action-against-vonage-results-100-million-customers-trapped-illegal-dark-patterns-junk-fees-when-trying-cancel-service ) and Adobe (2024: https://www.ftc.gov/news-events/news/press-releases/2024/06/ftc-takes-action-against-adobe-executives-hiding-fees-preventing-consumers-easily-cancelling ).
- Example. "Cancel anytime" in the hero, "call us Monday to Friday" in the terms.
- Rule. The cancellation path is one sentence beside the subscribe control ("Pause or cancel from your account, no call needed") and it is true for this store's subscription app. Free trials state the conversion date and price in the CTA block.

### DP9. Hidden recurring terms (SaaS billing, hidden subscription)  BLOCK  LAW
- Definition. CCPA item 12 "SaaS billing": generating and collecting recurring payments "by exploiting positive acquisition loops in recurring subscriptions ... as surreptitiously as possible", including silent trial conversion. ROSCA s.4: all material terms clearly and conspicuously before obtaining billing information. deceptive.design "hidden subscription".
- Example. "$19" in the buy box, "/month" in 10 px grey; first-charge date only in the confirmation email.
- Rule. Recurring amount, cadence, first-charge date, renewal price after any intro period and the cancel path sit in the same visual block as the price, at body size and contrast. A subscribe option never wins by default (DP5).
- Check.

### DP10. Interface interference, visual interference, false hierarchy  BLOCK  LAW
- Definition. CCPA item 6: "a design element that manipulates the user interface in ways that (a) highlights certain specific information; and (b) obscures other relevant information relative to the other information". DSA Art. 25(3)(a): giving more prominence to certain choices. FTC bucket II: un-bolded fees "sandwiched between bold paragraphs".
- Example. Bright "Yes, upgrade" button with a grey 12 px "no" text link; a close icon at 2:1 contrast; compare-at price larger than the price paid.
- Rule. In any binary choice (consent, upsell, subscription vs one-time), both options are the same element type, within 1.5x of each other's area, both at 4.5:1. Close controls meet A11's 48 x 48 CSS px floor, have 3:1 contrast and close on first tap. The price paid is never smaller than the compare-at.
- Check (browser).
```js
(() => { const d = document.querySelector('[role=dialog]'); if (!d) return 'no dialog';
  const a = d.querySelector('[data-action=accept]'), r = d.querySelector('[data-action=decline]');
  if (!a || !r) return 'FAIL missing accept/decline';
  const A = a.getBoundingClientRect(), R = r.getBoundingClientRect();
  return ((A.width*A.height)/(R.width*R.height) <= 1.5 && a.tagName === r.tagName) ? 'ok' : 'FAIL parity'; })()
```

### DP11. Bait and switch  BLOCK  LAW
- Definition. CCPA item 7: "advertising a particular outcome based on the user's action but deceptively serving an alternate outcome". UK banned practices 5 and 6 (bait advertising; bait and switch). FTC 16 CFR 238.
- Example. Ad shows the GBP 29 colourway; the page lands on a GBP 39 variant with the cheap one "unavailable"; sold-out size silently replaced.
- Rule. The SKU, variant, colour, flavour, size and price in the ad and the hero are what lands in the cart. Sold-out variants are disabled and labelled "Notify me", never swapped. See `references/copy/message-match.md` MM3.
- Check. Manifest `campaign.adVariantId`, hero `data-variant-id` and buy-box default variant are identical; the cart preload URL carries the same variant id.

### DP12. Drip pricing and hidden costs  BLOCK  LAW
- Definition. CCPA item 8: "elements of prices are not revealed upfront or are revealed surreptitiously", including revealing price "post-confirmation" and "free" that requires a paid continuation. UK DMCC: the full price belongs in the invitation to purchase. FTC fees rule (16 CFR 464 for tickets and lodging; s.5 elsewhere). CMA evidence 4/4 stars. Baymard: extra costs are the top abandonment reason at 39 to 40 percent; 64 percent of shoppers look for shipping cost on the product page. https://baymard.com/lists/cart-abandonment-rate ; https://baymard.com/blog/show-shipping-costs-on-product-pages
- Example. "$49" hero, "$8.95 handling" at payment; "Free" trial with shipping charged; tax added after the address step with no earlier signal.
- Rule. The price on the page is the price at checkout. Shipping cost or the free-shipping threshold, tax wording ("inclusive of all taxes" or "plus tax") and any mandatory fee appear within one viewport of the primary CTA. See `references/offers/price-presentation.md` PP1 and PP21.
- Check. For every `buy-box`, `pricing` or `offer` section: section text matches `shipping|delivery` and `tax|GST|inclusive`. Every `<s>`, `<del>` or compare-at element traces to an offer-ledger row with a `compare_at_basis`.

### DP13. Disguised advertisement  BLOCK  LAW
- Definition. CCPA item 9: "posing, masking advertisements as other types of content such as user generated content or new articles or false advertisements". UK banned practice 11 (advertorial without disclosure). FTC native advertising guidance; Endorsement Guides: disclosures "difficult to miss" and "unavoidable".
- Example. Fake newspaper masthead; "By our health desk" byline on a sales page; comment thread with invented commenters.
- Rule. `advertorial` and `listicle` pages carry a visible "Advertisement" or "Sponsored by [brand]" label inside the first 600 px at 390, plus the compliance line in the footer. No fake mastheads, bylines of people who do not exist, or invented comments. Paid creators say "Paid partnership".
- Check (browser, 390).
```js
(() => { if (!/advertorial|listicle/.test(document.body.dataset.pageType||'')) return 'n/a';
  return [...document.querySelectorAll('body *')].some(e => e.children.length===0 && /advertis(ement|ing)|sponsored|paid partnership/i.test(e.textContent) && e.getBoundingClientRect().top < 600) ? 'ok' : 'FAIL label'; })()
```

### DP14. Nagging  BLOCK  LAW
- Definition. CCPA item 10: "disrupted and annoyed by repeated and persistent interactions, in the form of requests, information, options, or interruptions ... unless specifically permitted by the user". DSA Art. 25(3)(b): repeatedly requesting a choice already made, especially by pop-ups. NN/g "overlay overload". https://www.nngroup.com/articles/overlay-overload/
- Example. Email popup on every page view after dismissal; notification prompt with no "No".
- Rule. One marketing popup per session, remembered for at least 7 days after dismissal and 30 days after conversion. Never two overlays at once. Consent UI first; marketing waits until it is gone.
- Check. Popup island props: `frequencyCapDays >= 7`. Browser: `[...document.querySelectorAll('[role=dialog],[data-overlay]')].filter(e => e.offsetParent !== null).length <= 1` at every scroll position.

### DP15. Trick wording, trick question  BLOCK  LAW
- Definition. CCPA item 11: "deliberate use of confusing or vague language like confusing wording, double negatives, or other similar tricks, in order to misguide or misdirect a user". CMA: complex language starred as almost always harmful.
- Example. "Uncheck to not receive no updates"; a toggle labelled "Opt out" whose on state means subscribed.
- Rule. Choice labels are affirmative, single-clause, no negation: "Email me offers" / "No thanks". Toggle labels describe the on state. No double negatives anywhere in choice UI.

### DP16. Rogue malware and fake system UI  BLOCK  LAW
- Definition. CCPA item 13: scareware and ransomware tactics.
- Rule. No fake virus warnings, fake OS dialogs, fake download buttons, fake "connection lost" banners.

### DP17. Fake reviews and undisclosed incentives  BLOCK  LAW
- Definition. FTC 16 CFR 465 bans fake, AI-generated or bought reviews, insider reviews without disclosure, and suppression of negative reviews (Fashion Nova, USD 4.2M, 2022: https://www.ftc.gov/news-events/news/press-releases/2022/01/fashion-nova-will-pay-42-million-part-settlement-ftc-allegations-it-blocked-negative-reviews-website ). UK DMCC banned practice on fake reviews. Endorsement Guides: incentivised reviews disclosed; results claims need typicality.
- Rule. Every quote, star, count and photo of a customer is a `verified` row in the proof ledger (`references/proof/proof-ledger.md`); sourcing in `references/proof/reviews-sourcing.md`. No invented names, avatars or cities. Never only five-star sets. "Results not typical" alone is not a disclosure.

### DP18. Misdirection  BLOCK  LAW
- Definition. deceptive.design: design that steers attention to the seller's preferred option and away from the shopper's. CMA "sensory manipulation" and "decoys". Overlaps DP10 but concerns steering rather than hiding.
- Example. A highlighted "MOST POPULAR" middle tier that exists only to make the top tier look cheap; a colour-only difference between "one-time" and "subscribe" that favours subscribe.
- Rule. Plan tiers are presented with the same visual weight; a recommended tier is labelled with a reason from the ledger ("Most ordered in the last 90 days" with the count), never a ribbon (design-rules N9). One-time and subscribe options are visually equal with one-time first.

### DP19. Obstruction and sludge  FAIL  LAW
- Definition. deceptive.design "obstruction"; CMA "sludge": excessive friction on the action the shopper wants (returns, cancellation, contact).
- Rule. Returns, refund, cancellation and contact information reach in at most two taps from any CTA: a one-line statement under the CTA linked to the full policy.

### DP20. Comparison prevention  WARN  LAW
- Definition. deceptive.design: making it hard to compare prices or features; CMA "partitioned pricing".
- Rule. Comparison tables use one unit per row, the same attribute set for every column, and no blank cell where the competitor actually has the feature. Per-unit price is shown wherever pack sizes differ.
- Check. In `comparison` and `us-vs-them` sections, every row has a value in every column; no cell is only a dash for a named competitor unless the plan records the source.

### DP21. Fictitious former price  BLOCK  LAW
- Definition. FTC 16 CFR 233.1; UK CMA duration and volume tests (Emma Sleep was/now judgment 30 Jul 2026); EU Price Indication Directive 30-day prior price; India MRP rules.
- Rule. A struck-through price exists only with an offer-ledger `compare_at_basis`. Detail in `references/offers/price-presentation.md` PP1 to PP5.
- Check. Every `<s>`, `<del>`, `[data-part=compare-at]` carries `data-source="compare_at_price"` or the ledger row id.

### DP22. Faux progress and fake processing  BLOCK  LAW
- Definition. FTC bucket I (induce false beliefs); CCPA interface interference. Progress indicators and "analysing your answers..." delays that do not reflect real work.
- Example. "Applying your discount... 87 percent" spinner; "Step 2 of 3" on a one-step form; quiz "Building your routine" delay with a fixed timer.
- Rule. Progress UI reflects real remaining steps from the funnel definition. No decorative delays or fake percentages.

## 3. Enforcement cases to cite when a merchant pushes back

| Case | Pattern | Outcome | URL |
|---|---|---|---|
| FTC v. Amazon (Prime), 2023 to 2025 | Subscription trap, confirmshaming decline, hidden terms | USD 2.5B (USD 1B penalty, USD 1.5B refunds); decline button must be clear and neutral | https://www.ftc.gov/news-events/news/press-releases/2025/09/ftc-secures-historic-25-billion-settlement-against-amazon |
| FTC v. Epic Games, 2022 | Dark patterns causing unwanted charges | USD 245M refunds | https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations |
| FTC v. Vonage, 2022 | Hard to cancel, junk fees | USD 100M | https://www.ftc.gov/news-events/news/press-releases/2022/11/ftc-action-against-vonage-results-100-million-customers-trapped-illegal-dark-patterns-junk-fees-when-trying-cancel-service |
| FTC v. Adobe, 2024 | Hidden early-termination fee, obstructed cancellation | Complaint filed | https://www.ftc.gov/news-events/news/press-releases/2024/06/ftc-takes-action-against-adobe-executives-hiding-fees-preventing-consumers-easily-cancelling |
| FTC v. Fashion Nova, 2022 | Suppressed negative reviews | USD 4.2M | https://www.ftc.gov/news-events/news/press-releases/2022/01/fashion-nova-will-pay-42-million-part-settlement-ftc-allegations-it-blocked-negative-reviews-website |
| CMA v. Emma Sleep, 2022 to 2026 | Countdown timers, "high demand" claims, misleading discounts; was/now pricing | Court-confirmed undertakings 22 May 2026; High Court judgment on reference pricing 30 Jul 2026 | https://www.gov.uk/cma-cases/emma-group-consumer-protection-case |
| CMA and Simba Sleep | Genuineness of "was" prices | Formal undertakings | https://www.gov.uk/government/news/cma-launches-court-action-against-emma-to-protect-uk-consumers |
| CJEU Planet49, 2019 | Pre-ticked consent | Pre-ticked boxes invalid | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A62017CJ0673 |
| India CCPA advisory, 5 Jun 2025 | All 13 patterns | Mandatory self-audit within 3 months; notices to platforms | https://consumeraffairs.nic.in/latestnews/ccpa-advisory-terms-consumer-protection-act-2019-self-audit-e-commerce-platforms |
| Sports Direct, 2015 | Basket sneaking (GBP 1 magazine) | Public backlash, practice withdrawn | https://deceptive.design/types/sneaking |

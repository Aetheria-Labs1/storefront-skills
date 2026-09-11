# Headline and CTA rules

Mechanics for the lines that carry the page: headline, subhead, bullets,
CTA label, the microcopy beside it, FAQ, price, guarantee and disclaimer
copy. `/design-page` applies them in Compose step 8; the hosted review
answers the checks. Frameworks are in `references/copy/copy-frameworks.md`;
the blacklist in `references/anti-patterns/copy-anti-patterns.md`; source
phrases in `references/copy/voice-of-customer-mining.md`. House rules A12
(sentence case, CTA names the action, no placeholder copy) and N6 (no
accent word in a headline) apply throughout.

Severity BLOCK, FAIL, WARN. Tag LAW, RESEARCH, OPERATOR, HEURISTIC. `rendered text` is
extracted text; `<headings>` is the text of `h1` to `h3`.

## 1. Headline

HC1 (FAIL, RESEARCH). The headline's job is to select the reader and pull them to the next line, not to sell (Schwartz). Lead with what the plan's awareness level allows:

| Awareness | Headline formula | Skeleton | Never |
|---|---|---|---|
| unaware | story or identity or surprising specific | Why [group] are quietly changing [habit] | product name, price, offer |
| problem-aware | the problem in the shopper's words, sharper than they say it | [symptom in their words]? Here is why [common fix] does not work | brand name first, "Introducing" |
| solution-aware | outcome plus mechanism, and why this one | [outcome in a number] without [the trade-off]. The [mechanism] way | superlatives, "best" |
| product-aware | product plus the strongest verified claim or the offer | [product]: [claim with a ledger number] | claims not in the ledger |
| most-aware | product plus offer plus terms | [product], [price], [shipping], [returns] | education, story |

HC2 (WARN, OPERATOR). Score the h1 on the 4U scale (useful, urgent, unique, ultra-specific), 1 to 4 each. Ship at 12 or more; rewrite under 8. Usefulness is mandatory; manufactured urgency scores 0. https://www.awai.com/2001/06/a-review-of-the-4-us/
Check: the score and its four numbers appear in `page plan` under the headline pattern line.

HC3 (FAIL, RESEARCH). The h1 contains at least one specific: a number, a material, a timeframe, a named mechanism, or a verbatim shopper phrase from the worksheet. Odd exact numbers read as measured; round numbers read as invented. Copyhackers: a headline lifted from a review beat the marketing headline by over 400 percent in clicks. https://copyhackers.com/2014/10/amazon-review-mining/
Check: h1 matches `\d|[a-z]+ (wool|cotton|steel|oil|acid|mg|ml|days?|weeks?|hours?|minutes?)` or the plan's "Headline VoC source" line names the worksheet row.

HC4 (FAIL, RESEARCH). Length: h1 at most 10 words and two lines at 32 px on 375 px; subhead at most 20 words.

HC5 (FAIL, RESEARCH). Sentence case for h1, h2, h3, subheads, buttons, labels. Product names keep brand casing. USAGov adopted sentence case sitewide in 2023 with no loss of trust and fewer wrapped lines. https://www.usa.gov/blog/2023/09/making-the-case-for-sentence-case
Check: CP16 regex on `<headings>` after the product-name allowlist.

HC6 (FAIL, OPERATOR). No accent word: no span, colour, italic, weight or underline on a word inside a headline (design-rules N6).
Check: lint N6.

HC7 (WARN, OPERATOR). No question in the h1 unless the framework is `qualifier-lead` and the question selects the reader. At most one question heading on the page.
Check: CP8.

HC8 (FAIL, LAW). Exactly one h1, the hero headline; no skipped heading levels; eyebrows are `<p>`, not `<h6>` (design-rules A3; WCAG 1.3.1).
Check: lint A3; `document.querySelectorAll('h1').length === 1`.

HC9 (WARN, OPERATOR). No year, month or "now" in the h1 unless the page is a dated campaign with an offer-ledger end date (CA29).
Check: CA29 regex.

HC10 (BLOCK, LAW). Every claim in the h1 or subhead is a verified proof-ledger or offer-ledger row; "clinically proven", "No.1", "doctor recommended" without a row is CP2.
Check: CP2 regex on `<headings>`.

## 2. Subhead

HC11 (FAIL, OPERATOR). The subhead has one job: resolve the headline's open loop with the mechanism, the proof or who it is for. It is not a second headline and does not restate the h1.
Check: CP20 overlap under 50 percent; the subhead contains a number, a mechanism noun or an audience noun.

## 3. Bullets

HC12 (FAIL, RESEARCH). Bullets are fascinations: specific attribute, then what it does for the shopper. Front-load the first two words (NN/g F-pattern). No adjective-only bullets. Each bullet carries a number, a material, a time or a test. At most 6 bullets per list, at most one list per section, no three consecutive bullets within 10 percent of the same length. Blind (teasing) bullets only in `advertorial`. https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ ; https://samueljwoods.com/7-formulas-for-fascination-bullets/

## 4. CTA copy

HC13 (FAIL, OPERATOR). Pattern: verb, object, then outcome or price. One to four words. Sentence case. The label names what happens on tap. Examples: "Add to cart", "Get my starter kit", "Start the hair test", "Join the waitlist", "Pre-order, ships 12 Oct".
Check: CP27 script (verb-first, 1 to 4 words) on every button and `a.btn` label.

HC14 (FAIL, OPERATOR). Banned as a primary CTA: Submit, Click here, Learn more, Read more, Get started, Continue without an object, OK, Yes, Go, Shop now, Buy now on `tof` and `mof` types. No arrows (N12), no exclamation marks, no ALL CAPS, no "MY" or "ME" in caps.
Check: lint A12 and C4 plus `STOCK_CTA_EXT`.

HC15 (WARN, RESEARCH). First person ("Get my kit") is optional; one widely cited test showed +90 percent CTR for "my" over "your" and another +14.7 percent, so the direction is worth testing and the magnitude is unreliable. Default to the checklist pattern; test first person in `/ab-test`. https://unbounce.com/a-b-testing/failed-ab-test-results/
Check: plan records the variant when used.

HC16 (FAIL, RESEARCH). On ad-driven pages the CTA verb equals the ad's CTA verb (`references/copy/message-match.md` MM7; Google Ads: mirror the call to action). https://support.google.com/google-ads/answer/7636512
Check: manifest `campaign.adCta` first word equals the primary CTA's first word.

HC17 (FAIL, OPERATOR). Every repeat of the primary CTA on the page is identical in copy and colour. Repeat about every two screens on long pages, and in the sticky bar when the checklist allows it. The sticky-bar label may append the price ("Add to cart, ₹1,299").

HC18 (FAIL, OPERATOR). Per page type, the checklist's `cta.copy_pattern` fixes the family of labels:

| copy_pattern | Approved labels | Not this |
|---|---|---|
| `add-to-cart` | Add to cart; Add to bag (fashion, beauty); Add both to cart (BOGO); Add the set | Buy now (tof/mof), Shop now |
| `claim-offer` | Get 10% off my first order; Claim the free travel kit; Apply code WELCOME | Unlock, Grab, Snag, Steal |
| `next-step` | See how it works; Read the results; Continue to the offer; See the price | Learn more, Continue |
| `start-quiz` | Start the 2-minute quiz; Find my shade; Take the hair test | Get started, Begin |
| `join-waitlist` | Join the waitlist; Reserve mine for ₹99; Get first access | Sign up, Submit |
| `subscribe` | Subscribe and save 15%; Start my monthly delivery | Subscribe (alone), Buy now |
| `shop-collection` | Shop the summer edit; See all 24 styles; Shop gifts under ₹2,000 | Shop now, View all |
| `read-results` | See the before and afters; Read 212 reviews; Watch the test | Learn more, Discover |

Check: the primary CTA label is in the approved family for the checklist pattern, or the plan records the deviation.

## 5. Microcopy beside the CTA

HC19 (FAIL, RESEARCH). Directly under every primary CTA, one or two short lines from: price with tax wording; shipping cost or threshold and delivery window; returns or guarantee with its duration; payment methods; the code as an action ("Code WELCOME applied at checkout"). Baymard: extra costs are the top abandonment reason (39 to 40 percent); 64 percent look for shipping cost on the product page; 13 to 15 percent abandon over returns. Never urgency theatre. https://baymard.com/lists/cart-abandonment-rate ; https://baymard.com/blog/show-shipping-costs-on-product-pages
Check: the element after each primary CTA matches `shipping|delivery|return|guarantee|inclusive|tax|code` and DP1 words are absent.

HC20 (FAIL, LAW). Shipping copy states the threshold and the region ("Free shipping in India on orders over ₹999"); delivery is a date range or day count, never "fast". Free means free (OF5).

## 6. FAQ

HC21 (FAIL, RESEARCH). 5 to 7 questions. Each is a real objection from the worksheet, phrased as the shopper would type it ("Will it feel heavy or cakey?", "Do I have to subscribe?", "Are these before and after photos real?"), never as marketing ("Why is our serum different?"). Baymard: FAQs that miss the real question leave shoppers stranded; 70 percent of sites fail to offer both FAQ and Q&A. Teardowns: objection-phrased FAQs on Jones Road, Seed, Hello Face, Endy. https://baymard.com/blog/product-page-faq-and-qa

HC22 (FAIL, OPERATOR). Order: shipping cost and time first, returns or refunds second, then cancellation (subscriptions), ingredients or materials or sizing, who it is not for, then the long tail.
Check: the first two FAQ questions match `ship|deliver` and `return|refund`.

HC23 (FAIL, OPERATOR). The first sentence of every answer is the answer (yes, no, a number, a date, a price); one sentence of why follows; at most 60 words per answer.
Check: CF10 first-sentence test; word count per answer at most 60.

HC24 (WARN, OPERATOR). The page as a whole answers Nik Sharma's six questions somewhere above the FAQ: what is it, why does this brand exist, why will it improve my life, why is it the best option for me, how fast do I get it, why should I trust you. https://www.nik.co/you-launched-your-brand-now-wtf-do-you-do
Check: one line per question in `QA record` naming the section that answers it.

## 7. Price copy

HC25 (BLOCK, LAW). Price copy follows `references/offers/price-presentation.md`: the full price with currency symbol first; compare-at struck through only with a ledger basis (PP1); "MRP ₹X (inclusive of all taxes)" for Indian packaged goods (PP5, PP21); unit price small and beside the price (PP8).

HC26 (FAIL, RESEARCH). Per-day or per-serving framing only for consumables, subscriptions and memberships, and only when the arithmetic is a ledger row (PP9). "₹43 a day" is allowed if true; "affordable luxury" is not.

HC27 (FAIL, LAW). "Free" states what is paid in the same line (shipping, trial conversion price and date). No asterisk on free (CP28).

## 8. Guarantee copy

HC28 (FAIL, OPERATOR). Named duration, scope and friction: "60-day money-back guarantee. Used or unused. Email us and we refund." Never "satisfaction guaranteed" alone (unfalsifiable). Linked to the policy page from the offer ledger; appears under the CTA and again in the FAQ.
Check: guarantee text matches `\d+[- ]day|\d+[- ]night|lifetime|\d+[- ]year` and contains an `<a href`.

## 9. Disclaimers

HC29 (BLOCK, LAW). A disclaimer sits in the same viewport as the claim it qualifies, at 12 px or more and 4.5:1, never only in the footer or an accordion. India CCPA and ASCI: a disclaimer may clarify but not contradict the claim. FTC: disclosures must be unavoidable. Supplements: the regulatory sentence sits beside the health claim.
Check: for each claim row in the ledger marked "needs disclaimer", the disclaimer element's `offsetTop` is within one viewport height of the claim at 390; computed `font-size >= 12px`.

## 10. Reading level and rhythm

HC30 (WARN, RESEARCH). Target Flesch-Kincaid grade 6 to 8 and reading ease 60 to 80 for body copy. Caveat: readability formulas are noisy on short marketing copy with product names and numbers; use the trend, not the decimal, and do not rewrite good specifics to hit a score. US plain-language guidance recommends grade 6 to 8 for public web content; aggregated landing-page benchmarks (secondary, unaudited) put top converters near grade 7 and 14 words per sentence. https://roast.page/stats/landing-page-copy-statistics ; https://neilpatel.com/blog/write-copy-like-apple/

HC31 (FAIL, RESEARCH). Sentences average at most 15 words, none over 25. Paragraphs at most 3 lines at 375 (about 45 words). One idea per paragraph. Apple's iPhone 5 pages averaged 10.9 to 14 words per sentence.

HC32 (WARN, OPERATOR). Fragments for rhythm are allowed once per page ("Smaller. Lighter. Same battery."); more is CP13. Delete the first sentence of every draft paragraph before shipping; it is usually throat-clearing (Shleyner). https://www.verygoodcopy.com/verygoodcopy-blogs-10/how-to-write-concisely
Check: CP13 count at most 1.

## 11. Review excerpting

HC33 (BLOCK, LAW). Quotes are verbatim ledger rows, trimmed only with "[...]", attributed exactly as stored with the date and source; at least one non-five-star quote when 20 or more reviews exist; results claims carry the generally-expected statement (CP4). Procedure in `references/proof/reviews-sourcing.md`; display rules in `references/proof/proof-ledger.md`.
Check: lint N11 and P4; every `[data-part=quote]` text equals a ledger row text after `[...]` removal.

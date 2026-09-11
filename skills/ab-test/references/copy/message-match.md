# Message match

The contract between an ad (or a search query) and the page it sends the
visitor to. `/plan-page` fills the scorecard in section 4 for every
ad-driven or search-driven page and writes the one-line "Message match"
summary the plan requires; `/design-page` re-checks the hero against it in
Compose step 8; `/optimize` runs it first on any paid-traffic page with a
high bounce. `references/traffic-source-meta.md` ("The #1 Rule: Message
Match") gives the tone guidance; this file is the checkable version and
wins where they differ. Channel specifics stay in the traffic-source files.

Severity BLOCK, FAIL, WARN. Tag LAW, RESEARCH, OPERATOR, HEURISTIC.

## 1. Evidence

- Unbounce audit of 300 paid ads: 98 percent failed message match (page headline did not match the ad headline). https://unbounce.com/ppc/poor-message-match/
- Campaign Monitor via Unbounce dynamic text replacement: mirroring the searcher's exact verb in the headline lifted trial sign-ups 31.4 percent (77 days, over 100 conversions per variant). https://unbounce.com/landing-page-examples/built-using-unbounce/dynamic-text-a-b-test/
- Moz case: matched ad and page raised conversion rate 212.74 percent and cut CPA 69.39 percent. https://moz.com/blog/message-match-conversion-rates
- Google Ads landing-page experience (a Quality Score component): relevance, transparency, ease of navigation, mobile, speed; "keep messaging consistent from ad to landing page", "mirror the call-to-action". https://support.google.com/google-ads/answer/7636512 ; https://support.google.com/google-ads/answer/6167130
- Meta: strong quality and engagement rankings with a low conversion ranking signal a post-click disconnect; Meta downgrades ads that withhold information or use sensationalised language. https://www.facebook.com/business/help/436113280262012 ; https://www.facebook.com/business/news/reducing-low-quality-ads-on-facebook
- Google: a one-second mobile delay can reduce retail conversions by up to 20 percent. https://support.google.com/google-ads/answer/7543502

## 2. The contract

Every row applies to paid social, paid search and email or SMS clicks with
a specific promise. "Ad" means the creative or the message the visitor
clicked; for search it means the query and the ad text.

| Id | Element | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| MM1 | Headline | The h1 carries the ad headline's core noun phrase and the same promise. Either identical, or a rephrase no longer than the ad with at least 60 percent content-word overlap. Never a broader or a bigger promise. | FAIL | RESEARCH |
| MM2 | Offer | Same discount depth, same gift, same bundle, same price, same code. The offer appears above the fold on `mof` and `bof` types; the code is auto-applied through the CTA href (`?discount=CODE`) and named in the microcopy. | BLOCK | LAW, OPERATOR |
| MM3 | Product and variant | The hero shows the SKU and variant (colour, flavour, size, pack) from the creative; the buy box defaults to it; the cart receives it. Sold-out variants are labelled, never swapped (DP11). | BLOCK | LAW |
| MM4 | Angle | The mechanism, claim or hook the ad leads with is the first claim on the page, in the h1 or subhead. A page that switches from the ad's "no aluminium" angle to "smells great" fails. | FAIL | RESEARCH |
| MM5 | Persona | The audience the ad addresses ("new mums", "runners over 40", "oily skin") is named in the h1, subhead or qualifier within the first screen at 390. | FAIL | OPERATOR |
| MM6 | Tone | Register matches: UGC or creator ad gets a UGC-led hero and first-person copy; clinical ad gets a clinical hero; conversational ad gets conversational copy. Recorded from `lexsis_campaigns.analyze` `tone`. | WARN | OPERATOR |
| MM7 | CTA verb | The primary CTA's first word equals the ad's CTA verb (Google: mirror the call to action). "Shop" in the ad and "Add" on the page is a mismatch; use the checklist pattern in the ad too, or match the page to it. | FAIL | RESEARCH |
| MM8 | No new claims above the fold | Every claim in the first screen at 390 is either in the ad or a verified ledger row. Nothing the visitor did not click for appears before the fold. | BLOCK | LAW |
| MM9 | Awareness | Cold social ads land on `advertorial`, `listicle`, `ad-landing-page`, `ugc-creator-collab` or `video-sales-page`; retargeting and brand search land on `pdp`, `pdp-hybrid-landing`, `offer-page` or `retargeting-warm`. Never send a most-aware click to an educational page or a cold click to a buy box with no premise. | FAIL | RESEARCH |
| MM10 | Visual continuity | The hero uses the same creative asset or the same product, variant and setting as the ad. Colour matching is done within the brand palette only: the page never adopts an ad's accent that is not in the plan's palette table (design-rules N14 and A1 win over the meta file's "extract from creative" advice). Fonts stay the brand's (N4). | FAIL | RESEARCH |
| MM11 | Speed and transparency | LCP under 2.5 s on 4G at 390; business name, contact, returns and privacy reachable from the page; no hidden fees (DP12). | FAIL | RESEARCH, LAW |
| MM12 | No sensationalism | Neither ad nor page uses "shocking", "miracle", "doctors hate", "you won't believe", stacked punctuation. Meta quality ranking penalises it; CP2 and CP21 catch it on the page. | FAIL | OPERATOR |
| MM13 | Consistency across variants | With A/B or personalisation variants, every variant keeps MM1 to MM8; only the element under test changes. | FAIL | OPERATOR |

## 3. Procedure

1. Pull the creative: `lexsis_campaigns.creatives` for the campaign, or accept the ad image, video frame and primary text from the merchant.
2. `lexsis_campaigns.analyze({ creative_id })` returns headline, claims, colours, CTA, tone and persona. Without the tool, view the creative and write the same seven fields by hand.
3. `lexsis_campaigns.match_persona({ creative_id })` returns the persona vocabulary and a rewritten headline, subhead and CTA. Use its vocabulary in the h1 and qualifier; keep every claim inside the ledger.
4. Record in `page record` under `campaign`: `adHeadline`, `adOffer`, `adVariantId`, `adAngle`, `adClaims[]`, `adCta`, `persona`, `tone`, `creativeAssetId`.
5. Fill the scorecard (section 4) in `page plan`. Any BLOCK row marked "no" stops the plan until the merchant confirms the ad change or the page change. Write the one-line summary:
   `**Message match.** h1 mirrors "<ad headline>" (overlap 0.8); offer 15% first order auto-applied; variant gid://.../456 in hero and buy box; CTA "Get 15% off my first order"; persona "night-shift nurses" in subhead; tone UGC.`
6. `/design-page` re-reads the page record before writing the hero and runs the section 6 scripts after compile.
7. For an ad claim that cannot be substantiated from the ledger (MM8): the page does not repeat it, the plan flags it under "Claims to confirm", and the merchant is told the ad itself needs the evidence or a rewrite.

## 4. Scorecard

Copy into `page plan` under `## Message match`. One row per creative element; "Match" is yes or no; a "no" on a BLOCK row stops the plan.

```markdown
## Message match

| Creative element | Value in ad | Page element | Value on page | Match | Rule |
|---|---|---|---|---|---|
| Headline | "Finally, a deodorant that lasts a 5-mile run" | h1 | "The deodorant that lasts a 5-mile run" | yes | MM1 |
| Offer | 15% off first order, code RUN15 | offer line + CTA href | "15% off your first order, code RUN15 applied" / ?discount=RUN15 | yes | MM2 |
| Product / variant | Magnesium stick, Cedar, 75 g, gid://.../456 | hero image + buy box default | same variant | yes | MM3 |
| Angle | no aluminium, 48 h | subhead | "48 hours without aluminium" (ledger P3) | yes | MM4 |
| Persona | runners | qualifier line | "Made for runners who sweat through the usual sticks" | yes | MM5 |
| Tone | UGC, first person | hero treatment | creator video poster, first-person subhead | yes | MM6 |
| CTA verb | "Get 15% off" | primary CTA | "Get 15% off my first order" | yes | MM7 |
| New claims above fold | none | first screen | none beyond ad claims + P1, O1 | yes | MM8 |
| Awareness | problem-aware (cold Meta) | page type | ad-landing-page | yes | MM9 |
| Visual | product on white, cedar tone | hero slot A1 | creative asset a_91f... | yes | MM10 |
```

## 5. Search-intent match (Google search and shopping)

| Id | Rule | Sev | Tag |
| --- | --- | --- | --- |
| MM14 | The h1 contains the query's head term (the product or category noun) and its modifier ("best", "vs", "for oily skin", "under ₹2,000") in the same sense. Use dynamic text replacement for the verb only when the ad group's verbs differ. | FAIL | RESEARCH |
| MM15 | The first screen at 390 answers the query: informational queries get the answer or the table first (`answer-first`, `comparison`, `seo-buyers-guide`); transactional queries get price, availability and CTA first (`pdp`, `pdp-hybrid-landing`). | FAIL | RESEARCH |
| MM16 | Query modifiers become sections: "vs" needs `comparison`; "best" needs `methodology` or ranking criteria; "review" needs `reviews` from the ledger; "price" or "cost" needs `pricing` above the fold; "near me" or "delivery" needs `shipping-returns` early. | FAIL | OPERATOR |
| MM17 | Shopping-ad clicks land on the exact product and variant in the feed at the feed price; a price change on the page without a feed update is a mismatch (and a Merchant Center disapproval risk). | BLOCK | LAW, OPERATOR |
| MM18 | The page title, meta description and h1 agree on the head term; the ad's display path words appear on the page. | WARN | RESEARCH |

# UGC Rights and Display

Rights and display procedure behind the `ugc-photo`, `ugc-video`,
`creator-video` and `community-screenshot` rows of the plan's `## Proof
ledger` (`references/proof/proof-ledger.md`). The creator owns the content; a
tag, a hashtag, a purchase or a public account transfers nothing. The agent
holds a recorded, scoped, written consent before an item exists in source.
Rule tags: LAW, RESEARCH ([H] [M] [L]), OPERATOR, HEURISTIC.

## What counts as UGC

| Item | Ledger kind | Who owns it | Typical rights path |
|---|---|---|---|
| Customer photo (review app upload, tagged post, email) | `ugc-photo` | the customer | review-app terms cover on-site widget display; off-widget use needs explicit consent |
| Customer video (review app, tagged Reel, TikTok) | `ugc-video` | the customer | explicit consent; audio cleared or stripped |
| Creator video (gifted, paid, affiliate) | `creator-video` | the creator | signed agreement listing channels, term, paid flag |
| Screenshot testimonial (DM, WhatsApp, email) | `community-screenshot` | the sender | written consent for that quote, channel and duration; redaction |
| Community post (Reddit, forum, Facebook group) | `community-screenshot` | the poster | poster's written permission; Reddit never in ads; else link only |
| Brand-owned content (staff shoot, product photography) | not UGC; an asset | the merchant | must not be labelled as customer content |

## Rights model

| Rule | Detail | Source |
|---|---|---|
| Ownership | copyright stays with the author; platform licences run to the platform, not to brands; Instagram grants no sublicence through its embed API | Instagram terms https://help.instagram.com/581066165581870/ ; Illinois Law Review on embed licensing https://illinoislawreview.org/wp-content/uploads/2023/01/Friedland-1.pdf [H] |
| Native reshare is the safe lane | Story reshare, collab post, official YouTube or Reddit embed for non-advertising display | platform terms [H] |
| Off-platform use needs a licence | anything hosted on a Lexsis page, in an email or an ad | platform terms [H] |
| Consent is explicit, scoped, recorded | names the exact post, lists channels (website, organic social, paid ads, email, marketplace), states duration, gets an unambiguous "yes", stored with timestamp outside the platform | CAP 3.45 (hold evidence and contact details); practitioner guides [L] https://idukki.io/blog/how-to-get-ugc-rights |
| Organic consent excludes ads | "website" consent does not cover paid or whitelisting; ask separately | practitioner guides [L]; FTC material connection rules |
| Music | platform-licensed audio is not licensed for your site; strip, replace or licence | platform terms [H] |
| Withdrawal | remove from every surface including CDN caches within 30 days (GDPR erasure) or 45 days (CCPA) | GDPR Art. 17; CCPA [H] |
| Review-platform media | Trustpilot: reviewer permission or full anonymisation; never a profile photo without documented permission. Google: Places API only, with author attribution | Trustpilot help https://help.trustpilot.com/s/article/Share-and-showcase-reviews ; Google Places policies https://developers.google.com/maps/documentation/places/web-service/policies [H] |
| Minors | a parent or guardian gives consent; no face of a minor without it | HEURISTIC; consistent with platform age rules |

### Rights request template

Public comment, then DM. The merchant sends it; the agent drafts it.

```text
Hi <handle>, we love this <post/video> of <product>. May we share it on our
website (<store domain>) and our Instagram for the next 12 months, with credit
to @<handle>? Reply "Yes, you can share" to agree. No ads or email unless we
ask separately. You can withdraw any time by messaging us.
```

The recorded "yes" must contain: post URL, handle, channels granted, start
date, duration, paid or gifted flag, screenshot of the reply, date received.
Store it with the asset in the library and cite the record in the ledger.

## Disclosure by jurisdiction

| Where | Any material connection (payment, free product, discount, affiliate) | Label rules | Source |
|---|---|---|---|
| US | disclose | "#ad" or "Paid partnership", clear and conspicuous, superimposed on visual content, same language as the content | FTC Endorsement Guides 16 CFR 255.5; FAQ https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking |
| India | disclose | one of ASCI's permitted labels: Advertisement, Ad, Sponsored, Collaboration, Partnership, Employee, Free gift, Affiliate; upfront, not buried in hashtags; on screen for 3 seconds on video up to 15 s, one third of duration for 15 s to 2 min, the entire brand segment beyond | ASCI Influencer Guidelines https://www.ascionline.in/social/wp-content/uploads/2025/04/ASCI-Influencer-Guidelines.pdf |
| UK | disclose | "Ad" per ASA and CMA | CAP Code; CMA influencer guidance |
| EU | disclose | commercial intent stated; UCPD Annex I 11 and 22 | Directive 2005/29/EC as amended |
| All | free product counts as a material connection | label as "Gifted" or the jurisdiction's term | FTC FAQ; ASCI |

When a creator video is reused on a Lexsis page, the label must be in the
frame for the whole brand segment and repeated as visible text beside the
player. A label in the original caption is not enough once the caption is gone.

## Display rules

| Element | Rule |
|---|---|
| Video aspect | native 9:16 or 1:1; never letterboxed into 16:9; poster frame from the video, not stock |
| Video playback | click to play, or muted autoplay with sound on tap; burned-in or toggleable captions; disclosure in frame |
| Photo aspect | original; no brand-added beautifying filter; no crop that removes the product or a watermark |
| Handle and attribution | creator handle or first name plus city as consented; date or month |
| Label line | product, duration of use, frequency, and where consented a verbatim caption ("Miracle Balm, 8 weeks, twice daily"); the strongest results pages label every item (Hello Face) |
| Caption text | verbatim if licensed; otherwise no caption; never a written-for-them quote |
| Grid vs carousel | 3 to 4 items: single row; 5 to 6: carousel or 2-row grid; 7 to 12: grid with click-to-expand; never a wall of 30 |
| Mixing with studio | never in the same grid; a UGC grid may sit beside a studio hero but each item carries its source label; creator content is never captioned "customer review" |
| Source labels | "Customer photo", "Creator video (paid partnership)", "via WhatsApp, Mar 2026" |
| Autoplay sound | never (WCAG 2.1 SC 1.4.2) |
| Position | beside the claim it illustrates (fit next to sizing, results next to the benefit); a shoppable strip below the hero on beauty and apparel; never above the H1 |
| Motion | no hover zoom, no shimmer (`design-rules.md` N7) |

## Quantity by page type

| Page type | Items | Shape |
|---|---|---|
| `ugc-creator-collab` | 6 to 12 | grid or shoppable strip; the hero itself is one creator video |
| `pdp`, `pdp-hybrid-landing` | 6 to 12 in a gallery or review media filter | media filter in the review module at 100+ reviews; else a `ugc-grid` after benefits |
| `ad-landing-page` | 3 to 6 | one carousel or row, below the primary claim it proves |
| `advertorial`, `listicle` | 1 to 3 | inline beside the reason or paragraph they support |
| `homepage`, `brand-story-founder` | 3 to 6 | one row low on the page |
| `bundle-kit`, `subscription` | 3 to 4 | beside the routine or the value stack |
| `comparison-us-vs-them`, `seo-buyers-guide` | 0 to 3 | only where an item shows the attribute being compared |
| `lookbook-shop-the-look` | 6 to 12 | shoppable grid |
| `launch-waitlist-preorder` | 0 to 3 early-tester items labelled "In-home tester" | never presented as customers |
| `thank-you-post-purchase`, `faq-support-led`, `lead-capture-giveaway`, `offer-page`, `sale-clearance-flash` | 0 | none |

## What may not be UGC

| Item | Why |
|---|---|
| Stock people implied to be customers | fictitious testimonial; CAP 3.45; FTC 16 CFR 465.2; ASA v. Hike Footwear 2024 |
| Generated people, generated rooms with the product, generated screenshots | fake testimonial; FTC 465.2; ASA GTMC 2013 ("illustrative" did not save invented imagery) |
| Staff, founders, relatives posing as customers | undisclosed insider; FTC 465.5; FTC v. Sunday Riley 2020 |
| Reused marketplace review photos (Amazon, Flipkart, Nykaa, Myntra) | platform terms license content to the platform; no reuse right |
| Screenshots of paid or fake accounts, bought followers or likes | FTC 465.8; EU Annex I 23c |
| A fabricated chat UI or "DM" mock-up | fictitious; CAP 3.45; India CCPA 2022 |
| Content whose consent covered only organic social | out of scope; platform terms and the consent record |
| Creator content without the paid or gifted label when a connection exists | undisclosed endorsement; FTC 255.5; ASCI |

## Evidence of lift, with caveats

| Finding | Number | Caveat | Source |
|---|---|---|---|
| UGC vs brand content on purchase decisions | 79% say UGC highly impacts decisions vs 13% branded content | 2019 survey, n about 1,590, vendor-run | Stackla/Nosto [M] https://www.nosto.com/wp-content/uploads/2019/02/Stackla-Consumer-Marketer-Data-Report-2019_FINAL.pdf |
| Reliance on UGC | 65% of shoppers; 80% of Gen Z | vendor index, n over 8,000 | Bazaarvoice SEI Vol. 18 [M] https://www.bazaarvoice.com/press/bazaarvoice-shopper-experience-index-vol-18-88-of-shoppers-want-an-omnichannel-experience-a-third-of-shoppers-say-that-includes-social/ |
| Shopper photos on a PDP | 71% of Americans say they raise purchase likelihood | vendor survey | Bazaarvoice SEI 2022 [M] https://www.bazaarvoice.com/press/sei-2022-press-release/ |
| Conversion when shoppers interact with UGC | +161% overall; apparel +207%; electronics +81% | correlational, self-selected engagers, 2018 | Yotpo [M] https://www.yotpo.com/blog/increase-conversion-rate-ecommerce/ |
| Photo or video makes a review more credible | 36% cite it | local-business survey, not ecommerce | BrightLocal 2026 [M] https://www.brightlocal.com/research/local-consumer-review-survey/ |
| Video beats photo beats text multipliers | "4.1x", "2.6x" | vendor blogs, unaudited; never quote on a page | [L] |

None of these numbers may appear on a page. They justify planning a UGC
module when rights exist; they do not justify creating content to fill one.

## Ledger row template

```markdown
| P5 | ugc-video | in-use proof | creator @<handle> | asset id <id>; post URL; consent email 2026-08-21 (website + Instagram, 12 months); gifted; audio replaced | merchant consent record | ugc-grid | verified |
| P14 | ugc-photo | "fits true to size" | customer review 9a1c<id> (Judge.me) | media URL from `lexsis_catalog.reviews` has_media; caption verbatim; "Size M" | API 2026-09-10; app terms cover widget display | reviews | verified |
| P15 | community-screenshot | "arrived in two days" | WhatsApp, 2026-03-04 | sender consent 2026-03-06 for website, 12 months; phone and surname redacted | consent record | shipping-returns | verified |
| P16 | creator-video | hero | creator @<handle> | consent covers Instagram only | none for website | — | dropped (scope) |
```

## Rules

UG1. Never render UGC without a rights record naming the item, the channels granted (including "website"), the start date, the duration and the recorded "yes". LAW platform terms (Instagram, TikTok, YouTube, Reddit); CAP 3.45.
Check: every `ugc-*`, `creator-video` and `community-screenshot` row cites a consent record id or date; no row reads "tagged us" or "public post" as its evidence.

UG2. A tag, hashtag, mention or purchase is not a licence. LAW Instagram terms; Reddit User Agreement; YouTube terms.
Check: `grep -ciE 'tagged|hashtag|public post' page-plan.md` under the ledger is 0 in the Verified column.

UG3. Paid or gifted content carries the jurisdiction's label in frame for the brand segment and as visible text beside the player; free product is a material connection. LAW FTC 16 CFR 255.5; ASCI Influencer Guidelines; ASA and CMA.
Check: each `creator-video` row with paid or gifted flag renders "Paid partnership", "Ad", "Sponsored" or "Gifted" text inside its section.
```bash
perl -0ne 'while(/<!-- section: (ugc-grid|video-testimonials)[a-z-]* -->(.*?)(?=<!-- section: |\z)/gs){my $b=$2; print "unlabelled\n" if $b=~/creator/i && $b!~/(Paid partnership|Sponsored|Gifted|\bAd\b)/}' $W/lexsis-source.html   # no output when a paid or gifted creator item exists
```

UG4. Video renders at native 9:16 or 1:1, click to play or muted autoplay, captions present, poster from the video. LAW WCAG 2.1 SC 1.4.2; HEURISTIC display table.
Check:
```bash
perl -ne 'print if /<video[^>]*autoplay(?![^>]*muted)/' $W/lexsis-source.html | wc -l   # 0
grep -c '<track[^>]*kind="captions"' $W/lexsis-source.html   # >= number of <video> with speech
```

UG5. Every item carries a source label and, where consented, handle, date and the product, duration and frequency line; creator content is never labelled as a customer review. LAW FTC 465 (a creator is not a bona fide customer unless they bought it); HEURISTIC teardown pattern 20.
Check: each item in a `ugc-grid` contains a `<figcaption>` or label element with one of "Customer photo", "Customer video", "Creator video", "via <channel>".

UG6. Never stock people, generated people, staff or relatives as customers, or reused marketplace photos. LAW FTC 465.2 and 465.5; CAP 3.45; Amazon Conditions of Use.
Check: every `ugc-*` asset in the manifest has provider = import or review-app media, never generated; no asset filename or alt contains "stock", "unsplash", "pexels", "shutterstock".
```bash
grep -ciE 'unsplash|pexels|shutterstock|istock|getty|generated' $W/lexsis-source.html   # 0 inside ugc sections
```

UG7. Strip or replace platform-licensed music before hosting a clip; record the audio status in the row. LAW platform music licences do not extend to brand sites.
Check: each `ugc-video` and `creator-video` row states "audio replaced", "audio original (creator-owned)" or "muted".

UG8. Screenshot testimonials render only with the sender's written consent, phone numbers, surnames and avatars redacted unless consented, with the channel and month labelled; never a fabricated chat UI. LAW CAP 3.45; GDPR; India CCPA 2022.
Check: `community-screenshot` assets are imports with a consent record; no CSS or component that draws a chat bubble around typed text.

UG9. Quantity stays inside the page-type table; 3 to 6 on a landing page, 6 to 12 on a PDP or UGC page; never a wall of 30. HEURISTIC; consistent with the type checklist's proof module ceilings.
Check:
```bash
perl -0ne 'while(/<!-- section: ugc-grid[a-z-]* -->(.*?)(?=<!-- section: |\z)/gs){my $b=$1; my $n=()=$b=~/<(figure|video|img)/g; print "items=$n\n"}' $W/lexsis-source.html   # within the table's range for the page type
```

UG10. Withdraw within 30 days of a creator's request across every surface, including cached renders; record the removal in the ledger row as `dropped (withdrawn <date>)`. LAW GDPR Art. 17; CCPA.
Check: the plan's ledger row and the asset library record agree.

UG11. UGC sits beside the claim it proves, never above the H1, never mixed into a studio grid, never with hover motion. HEURISTIC; `design-rules.md` N7; `references/consumer-behavior-cro.md` proof proximity.
Check: DOM order places `ugc-grid` after `hero`; no `hover:scale` inside it.

UG12. Lift statistics from the evidence table never appear on a page. HEURISTIC; RESEARCH caveats above.
Check: `grep -ciE '161%|79% of (shoppers|consumers)|2\.4x more authentic' $W/lexsis-source.html` is 0.

## Sources

- FTC Endorsement Guides 2023: https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising ; FAQ: https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking
- FTC Consumer Reviews Rule 16 CFR 465: https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials
- ASCI Influencer Guidelines: https://www.ascionline.in/social/wp-content/uploads/2025/04/ASCI-Influencer-Guidelines.pdf
- CAP testimonials advice: https://www.asa.org.uk/advice-online/testimonials-and-endorsements.html
- Instagram terms: https://help.instagram.com/581066165581870/ ; Reddit: https://redditinc.com/policies/user-agreement ; https://redditinc.com/policies/embeds-terms ; YouTube: https://www.youtube.com/static?template=terms
- Embed licensing analysis: https://illinoislawreview.org/wp-content/uploads/2023/01/Friedland-1.pdf
- Trustpilot showcasing reviews: https://help.trustpilot.com/s/article/Share-and-showcase-reviews ; Google Places policies: https://developers.google.com/maps/documentation/places/web-service/policies
- WCAG 1.4.2: https://www.w3.org/WAI/WCAG21/Understanding/audio-control.html ; Chrome autoplay: https://developer.chrome.com/blog/autoplay/
- Rights workflows [L]: https://idukki.io/blog/how-to-get-ugc-rights ; https://www.inspirefusion.com/ugc-rights-request-script/ ; https://creatorflow.so/blog/collect-user-generated-content-instagram/
- Lift evidence: Stackla/Nosto 2019; Bazaarvoice SEI Vol. 18 and 2022; Yotpo 2018; BrightLocal 2026 (URLs in the table).
- Teardowns: labelled before/afters and video grids with handles (Hello Face), reviews tagged with variant (Ridge, Endy): internal research audit (2026-09-10) Part D.5 items 20 and 21.

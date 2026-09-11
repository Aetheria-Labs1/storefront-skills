# CRO anti-patterns

Evidence table of page patterns that measurably lose conversions or trust.
`/design-page` reads it before Compose and during the hosted review;
`/optimize` uses it as the first diagnosis pass. Deceptive practices live in
`references/anti-patterns/dark-patterns.md` (DP ids); mobile-specific
failures in `references/anti-patterns/mobile-anti-patterns.md` (MA ids);
copy in `references/anti-patterns/copy-anti-patterns.md` (CP ids). House
rules N1 to N14 and A1 to A12 in `references/design-rules.md` override this
file where they overlap.

Severity: BLOCK, FAIL, WARN. Tag: LAW, RESEARCH, OPERATOR, HEURISTIC.
Vendor benchmark data (popup tools, sticky-CTA vendors) describes those
vendors' customers; rows built on it are tagged RESEARCH (vendor).

Checks use `$W` for the page workspace and `$T` for extracted text
(`perl -pe 's/<[^>]+>/ /g' $W/lexsis-source.html > $T`). Browser checks run in
the hosted draft at 390 x 844 and 1280 x 800.

## 1. Attention and layout

| Id | Anti-pattern | Evidence | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|---|
| CA1 | Hero carousel or auto-rotating slider | Notre Dame (Runyon), 3.76M visits: 1.07 percent of visitors clicked any slide; 89.1 percent of those clicks were slide 1. NN/g: users read moving panels as ads; do not auto-forward on mobile. Baymard recommends against auto-rotation on all touch devices. https://erikrunyon.com/2013/07/carousel-interaction-stats/ ; https://www.nngroup.com/articles/auto-forwarding/ ; https://baymard.com/blog/mobile-ecommerce-search-and-navigation | One static hero with one message. Stack extra messages as sections. Manual carousels only for product galleries, with arrows and dots. | FAIL | RESEARCH | `grep -ciE 'data-autoplay="?true|autorotate|swiper-autoplay' $W/lexsis-source.html` is 0; hero section contains no carousel island |
| CA2 | Autoplay video with sound | NN/g 2004: 79 percent rate auto-playing sound negatively; 2017 survey (n=452): autoplay video ads among the most hated. WCAG 1.4.2 (A): auto audio over 3 s needs a stop or volume control. https://www.nngroup.com/articles/most-hated-advertising-techniques/ ; https://www.w3.org/TR/WCAG22/#audio-control | Autoplay only muted, `playsinline`, poster, captions, visible unmute and pause. See `references/assets/video-rules.md`. | FAIL | RESEARCH, LAW | `grep -cE '<video[^>]*autoplay(?![^>]*muted)' $W/lexsis-source.html` is 0 (use `perl -ne`) |
| CA3 | Entry popup inside 10 s | NN/g: modals are the most-hated format on desktop and mobile. Google: intrusive interstitials on mobile entry from search may rank lower. Wisepops (vendor, 1B displays): immediate popups 4.16 percent vs 6.45 percent at 11 to 15 s; Omnisend (vendor): 0 to 1 s 1.9 percent vs 6 to 10 s 2.4 percent. https://www.nngroup.com/articles/most-hated-advertising-techniques/ ; https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials ; https://wisepops.com/blog/popup-stats ; https://www.omnisend.com/blog/email-popup-statistics/ | No marketing popup before 10 s and 30 percent scroll. Never while the hero is in view on paid-traffic types. Once per session, capped 7 days (DP14). | FAIL | RESEARCH (vendor), OPERATOR | Popup island props: `delayMs >= 10000` and `scrollPct >= 30`; browser at 9.5 s after load shows no `[role=dialog]` |
| CA4 | Competing CTAs | Unbounce attention ratio: homepages run about 40 links per CTA; a focused page is 1:1. Baymard: competing buttons distract from add-to-cart. https://unbounce.com/ppc/poor-message-match/ ; https://baymard.com/learn/ecommerce-ux-best-practices | One primary action per page on single-goal types. Secondary actions are text links. Never two equal-weight buttons side by side in the hero (see DA5). | FAIL | RESEARCH | `document.querySelectorAll('[data-section=hero] .btn-primary, [data-section=hero] [data-primary]').length === 1` |
| CA5 | Site navigation on a paid landing page | VWO/Yuppiechef: removing nav doubled registry sign-ups (3 to 6 percent). Unbounce case: nav removed, 3.12 to 13.64 percent (small sample). https://vwo.com/blog/a-b-testing-case-study-navigation-menu/ ; https://unbounce.com/a-b-testing/how-a-single-a-b-test-increased-conversions/ | Types with `nav: none` render the logo only, not a link; slim legal footer. Enforced by plan_lint T5. | FAIL | RESEARCH | `grep -c '<!-- section: header' $W/lexsis-source.html` is 0 when checklist `nav` is `none` |
| CA6 | Generic stock imagery, AI-rendered people | NN/g eyetracking: users ignore decorative feel-good stock photos and scrutinise product photos and real people. https://www.nngroup.com/articles/photos-as-web-content/ | Hero shows the product or a real customer using it. People shown as customers are never generated (`references/assets/generation-policy.md` NEVER list). | FAIL | RESEARCH | Every hero slot in `page-plan.md` Asset slots has source `shopify media`, `library`, `merchant` or an ALLOW purpose; none is `product_lifestyle` generated with a person |
| CA7 | Wall of text | NN/g: users read at most 28 percent of words on an average visit; F-pattern scanning dominates unformatted text. https://www.nngroup.com/articles/how-little-do-users-read/ ; https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ | Paragraph at most 45 words (3 lines at 375). Every section headline carries the message alone. Lists for 3 or more parallel items. | FAIL | RESEARCH | `perl -0ne 'while(/<p[^>]*>(.*?)<\/p>/sg){$n=()=($1=~/\S+/g); print "$n\n" if $n>45}' $W/lexsis-source.html` prints nothing |
| CA8 | Primary CTA below the first screen (single-goal types) | Baymard PDP research and design-rules A8: price and add-to-cart within the first viewport on desktop and 1.5 viewports at 390. Sticky-CTA evidence is mixed: GrowthRock +5.2 percent orders with a sticky drawer, no lift from scroll-to; CleanCommit +8.7 percent ATC but -7.7 percent CR in one test; RevenueFlows (47 stores): average +0.31 percent, only meaningful on pages over 1,200 words. https://growthrock.co/sticky-add-to-cart-button-example/ ; https://cleancommit.io/ab-tests/sticky-mobile-add-to-cart-button/ ; https://revenueflows.ai/blog/shopify-sticky-add-to-cart-button-myth | Follow the type checklist `cta.first_after_section` and `cta.sticky`. Where sticky is `optional`, add it only on pages longer than about two screens, showing price plus button, and treat it as a test. Never stack with other fixed bars (MA5). | WARN | RESEARCH (mixed) | Browser at 390: primary CTA `getBoundingClientRect().top <= 1266` when `cta.first_after_section` is 0 |
| CA9 | Dead-end page | The type checklists make `closing-cta` mandatory on selling types; conversion-psychology.md lists dead ends as a conversion killer. | The last content section before the footer is offer plus CTA plus guarantee or returns line. No trailing "related reads" after it on selling types. | FAIL | OPERATOR | Last `<!-- section:` before `footer` is `closing-cta`, `final-offer` or `buy-box` |
| CA10 | Essentials hidden in accordions | NN/g: accordions reduce discoverability; avoid hiding crucial information in collapsed panels. https://www.nngroup.com/articles/accordions-on-desktop/ | Price, shipping, guarantee, ingredients or materials, and the top three objections are visible. FAQ accordions hold the long tail only. | FAIL | RESEARCH | No `<details>` or accordion island wraps the `shipping-returns`, `guarantee`, `ingredients`, `materials` or `pricing` section |
| CA11 | Hamburger-only navigation on full-nav types | NN/g (n=179): hidden nav used 27 percent vs 48 to 50 percent visible on desktop; tasks 39 percent slower. https://www.nngroup.com/articles/hamburger-menus/ | On `nav: full` types, expose 3 to 5 top links at 1280; hamburger holds the rest. | WARN | RESEARCH | At 1280, header renders at least 3 visible `<a>` links outside the menu button |
| CA12 | Infinite scroll on a landing page | EU Digital Fairness Act fitness check lists infinite scroll and autoplay as addictive design likely to be off by default. https://www.dentons.com/en/insights/articles/2026/june/9/the-digital-fairness-act-dark-patterns-addictive-designs-and-influencer-marketing | Landing pages are finite. Product grids on `collection-landing` and `sale-clearance-flash` paginate or "Load more". | WARN | LAW (pending), OPERATOR | `grep -ciE 'infinite-?scroll|loadOnScroll' $W/lexsis-source.html` is 0 |

## 2. Price and commerce

| Id | Anti-pattern | Evidence | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|---|
| CA13 | Hidden price ("See price", "Contact us") on selling types | Baymard: 12 to 14 percent abandon because total cost was unclear. Drip pricing is DP12. https://baymard.com/lists/cart-abandonment-rate | Price visible where the checklist says `price_above_fold: required` and beside every CTA on selling types. No gates. | BLOCK | LAW, RESEARCH | plan_lint price rule; `grep -ciE 'see price|contact (us )?for (price|pricing)|request a quote' $T` is 0 except `wholesale-b2b` |
| CA14 | Hidden shipping cost or delivery time | Baymard: 64 percent of shoppers look for shipping cost on the product page; 43 percent of sites omit it; "delivery too slow" is the second abandonment reason at 20 to 21 percent. https://baymard.com/blog/show-shipping-costs-on-product-pages ; https://baymard.com/lists/cart-abandonment-rate | Shipping cost or threshold plus a delivery window within one viewport of the primary CTA, from the offer ledger. Cutoff timers only when real (DP1). | FAIL | RESEARCH | For each `buy-box`, `offer`, `pricing` section text: matches `shipping|delivery` (lint O7) |
| CA15 | Forced account creation | Baymard: 18 to 19 percent abandonment reason; 60 percent of mobile test subjects overlooked guest checkout when not primary. https://baymard.com/blog/mobile-ecommerce-checkout-forms | Guest checkout primary; account offered after purchase. DP7. | BLOCK | LAW, RESEARCH | CTA hrefs never route via `/account` or `/register` |
| CA16 | Returns policy absent near the CTA | Baymard: 13 to 15 percent abandon over an unsatisfactory returns policy; 44 percent of sites do not link the policy from the product page. https://baymard.com/blog/current-state-ecommerce-product-page-ux | One-line returns or guarantee statement under the CTA, linked to the policy URL in the offer ledger. | FAIL | RESEARCH | `buy-box` or `closing-cta` section text matches `return|refund|guarantee` and contains an `<a href` |
| CA17 | Free-shipping bar with wrong or negative math | Baymard: a free-shipping offer only in a site-wide banner is missed through banner blindness (32 percent of sites). Threshold bars that read "Add $-4 more" or exceed 100 percent break trust. https://baymard.com/blog/show-shipping-costs-on-product-pages | The threshold bar reads the live cart total, clamps at zero, states the threshold and region from the offer ledger, and repeats the threshold beside the price. | FAIL | OPERATOR | Browser: add items past the threshold; bar text never contains `-` before a currency amount and switches to a "qualifies" state |
| CA18 | Discount pills and ribbons | Design-rules N9; Baymard: show price and compare-at clearly, do not shout. | Compare-at is struck-through text only. No "31% OFF", "BEST VALUE", "MOST POPULAR". | FAIL | OPERATOR | lint N9 |
| CA19 | Urgency devices on health, supplement or medical-claim pages | India ASCI and CCPA misleading-ads guidelines require substantiation for health claims; Meta downgrades sensationalised health ads (https://www.facebook.com/business/news/reducing-low-quality-ads-on-facebook ). Timers beside "clinically proven" invite regulatory review of both. | Pages whose copy carries a health, efficacy or safety claim carry no countdown, stock indicator or "last chance" copy. Offer terms are stated plainly. | FAIL | LAW, OPERATOR | If `grep -ciE 'clinical|doctor|dermatolog|cure|treat|relie(f|ve)' $T` is at least 1, then `countdown` and `stock-indicator` sections are absent |
| CA20 | "Buy now" as the primary CTA on tof or mof types | Offers research: "Buy now" assumes a most-aware reader; Baymard and NN/g: "Add to cart" is the familiar wording. `references/copy/headline-and-cta-rules.md` HC14. | Use the checklist `cta.copy_pattern`. "Buy now" only on `offer-page`, `restock`, `sale-clearance-flash`. | WARN | OPERATOR | `grep -ciE '>\s*buy now\s*<' $W/lexsis-source.html` is 0 unless `page.funnelStage` is `bof` |
| CA21 | Faux progress bars, fake processing delays | FTC bucket I; DP22. | Progress reflects real steps; no decorative delays. | BLOCK | LAW | DP22 check |

## 3. Forms and overlays

| Id | Anti-pattern | Evidence | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|---|
| CA22 | Long forms | Baymard: ideal checkout is about 8 fields vs an average of 11.3; 17 to 18 percent abandon for "too long or complicated". Popupsmart (vendor): 1 to 2 field popups convert best. https://baymard.com/blog/checkout-flow-average-form-fields ; https://popupsmart.com/blog/popup-conversion-benchmark-report | Lead capture asks for one field (email or phone); a second field goes on step two. No coupon field above the fold; hide address line 2. | FAIL | RESEARCH | `email-capture`, `sms-capture`, `waitlist-form` sections contain at most 1 visible `<input>` not of type hidden or submit |
| CA23 | Chat launcher covering the CTA or sticky bar | CleanCommit: moving the chat bubble off the CTAs, shrinking it and auto-minimising on mobile lifted conversion across devices. https://cleancommit.io/ab-tests/repositioning-the-chat-pop-up-significantly-improves-conversion-rates-across-devices/ | Launcher at most 56 px, opposite corner from the sticky CTA, hidden until the hero scrolls out, never auto-opens. Counts against the fixed-height budget (MA5). | FAIL | RESEARCH | Browser: bounding boxes of `[data-part=chat-launcher]` and `.btn-primary, [data-sticky-cta]` do not intersect at 390 |
| CA24 | Cookie banner covering the hero | Google: legal interstitials are exempt from the penalty but should overlay, not replace, content. DSA 25(3)(a) and GDPR: no false hierarchy in consent. https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials | Where consent UI is legally required: bottom sheet at most 25 percent of viewport height, equal accept and reject buttons (DP10), no scroll lock, no marketing popup until dismissed. Where no non-essential cookies exist: no banner. | FAIL | LAW, OPERATOR | Browser at 390: consent element height at most `0.25 * innerHeight`; `document.body.style.overflow !== 'hidden'` |
| CA25 | Non-tappable phone, WhatsApp or email | Google Ads landing-page guidance: make it easy to contact you. https://support.google.com/google-ads/answer/7636512 | Every phone number is `tel:`, WhatsApp is `https://wa.me/`, email is `mailto:`. | WARN | OPERATOR | `[...document.querySelectorAll('a')].filter(a => /\+?\d[\d\s-]{8,}/.test(a.textContent)).every(a => /^(tel:|https:\/\/wa\.me)/.test(a.href))` |

## 3b. Popups and interstitials

| Id | Anti-pattern | Evidence | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|---|
| CA34 | Full-page interstitial on mobile entry | Google penalises intrusive interstitials on mobile entry from search (since 10 Jan 2017; legal, age and login gates exempt). https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials | No overlay taller than 60 percent of the viewport in the first 10 s; never a separate consent page. | BLOCK | LAW (platform) | Browser at 9.5 s: every visible `[role=dialog]` has `height / innerHeight <= 0.6` |
| CA35 | Popup without a real dismiss | Close at least 24 x 24 px (44 preferred), 3:1, Esc and backdrop close, neutral decline copy (DP6, DP10). | As stated. | BLOCK | LAW | MA21 and DP10 checks |
| CA36 | Popup asking for two fields at once | Popupsmart (vendor): one or two fields convert best; Baymard: every extra field costs mobile completion. https://popupsmart.com/blog/popup-conversion-benchmark-report | One field per step; phone on step two if wanted. Consent boxes unchecked and separate for email and SMS. | FAIL | RESEARCH (vendor) | CA22 check |
| CA37 | Exit intent faked on mobile ("Wait!" on tab switch) | No mouse on touch; back-button or scroll-up intent only. | Use click-triggered ("Get my code") or scroll-triggered popups on mobile; Wisepops (vendor) reports click-triggered at about 54 percent conversion vs 3.9 percent exit intent. https://wisepops.com/blog/popup-stats | WARN | RESEARCH (vendor) | Popup island `trigger` is not `exit` when the viewport is under 768 px |
| CA38 | Gamified popup with fake odds or fake delay | Spin-to-win is allowed only with real odds and every prize honoured; no "you almost won"; no fixed spinning delay (DP22). | As stated; odds recorded in the offer ledger. | BLOCK | LAW | Offer ledger row for each prize; `grep -ci 'almost won' $T` is 0 |

## 4. Proof and copy

| Id | Anti-pattern | Evidence | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|---|
| CA26 | Unattributed or invented testimonials | FTC Endorsement Guides: endorsements must reflect real experience; results need typicality. Baymard: 95 percent of shoppers rely on reviews; 53 percent seek negative ones. https://www.govinfo.gov/content/pkg/CFR-2023-title16-vol1/pdf/CFR-2023-title16-vol1-part255.pdf ; https://baymard.com/blog/respond-to-negative-user-reviews | Every quote is a `verified` proof-ledger row with attribution as stored, a date and a source. Include at least one non-five-star review when 20 or more exist. DP17. | BLOCK | LAW | lint N11 numerals check; every `[data-part=quote]` sits in an item with `[data-part=author]` and `data-source` |
| CA27 | Trust badges nobody recognises | Baymard surveys: Norton about 36 percent recognition, McAfee about 23 percent, SSL vendor seals about 3 percent; CXL: unaided awareness of most seals "very low"; payment brands most trusted. https://baymard.com/blog/site-seal-trust ; https://cxl.com/research-study/trust-seals/ | Show the store's real payment methods (UPI, Visa, Mastercard, PayPal, Shop Pay, Apple or Google Pay) near the CTA. No generic "100% secure" shields; no seal the merchant does not hold (`references/proof/trust-badges-certifications.md`). | WARN | RESEARCH | `grep -ciE '100% (secure|safe)|ssl secured|secure checkout badge' $T` is 0; every badge is a proof-ledger `certification` row |
| CA28 | Conflicting proof numbers on one page | Teardowns: Jones Road showed 4.88 stars in the hero and 4.61 in the module; Create showed 22,000+ and 5,000+ five-star reviews on the same URL. https://www.jonesroadbeauty.com/pages/foundation-stick-performance ; https://trycreate.co/pages/5-reasons-try-create-sub | One average, one count, one customer count per page, each from a single ledger row, repeated verbatim. | FAIL | OPERATOR | `grep -oE '[0-9]\.[0-9]{1,2} ?(stars|/ ?5|out of 5)' $T | sort -u | wc -l` is at most 1; review counts likewise |
| CA29 | Year-stamped or dated headlines | Teardowns: AG1 "5 Health Benefits of Taking AG1 in 2025" and Stars + Honey "...in 2026" need maintenance and read stale after the year turns. https://drinkag1.com/5-reasons-why-variant-a | No year in a headline unless the page is a dated campaign with an offer-ledger end date. | WARN | OPERATOR | `grep -cE '<h1[^>]*>[^<]*\b20[2-3][0-9]\b' $W/lexsis-source.html` is 0 unless the plan records an end date |
| CA30 | Stock CTA labels ("Learn more", "Submit", "Click here", "Get started") | ContentVerve/Unbounce: "Get my..." vs "Get your..." +90 percent CTR in one test (magnitude unreliable); Google Ads: mirror the ad's call to action. https://unbounce.com/a-b-testing/failed-ab-test-results/ ; https://support.google.com/google-ads/answer/7636512 | CTA is verb plus object plus outcome or price (`references/copy/headline-and-cta-rules.md` HC12). Design-rules A12 and lint C4 already fail the stock strings. | FAIL | RESEARCH, OPERATOR | lint A12 and C4 |

## 5. Performance and mobile

| Id | Anti-pattern | Evidence | Rule | Sev | Tag | Check |
|---|---|---|---|---|---|---|
| CA31 | Tap targets under 24 x 24 CSS px; primary controls under 44 | WCAG 2.2 SC 2.5.8 (AA); Shopify Theme Store requires 24 x 24 and recommends 44 x 44 for primary controls. Design-rules A11 asks 48 px for primary. https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html ; https://shopify.dev/docs/storefronts/themes/store/requirements | MA11. | BLOCK | LAW | MA11 script |
| CA32 | Slow first render | Google: a one-second mobile delay can cut retail conversions by up to 20 percent; Google Ads landing-page experience scores speed. https://support.google.com/google-ads/answer/7543502 | LCP under 2.5 s on simulated 4G at 390; hero image preloaded with `fetchpriority="high"`, everything below the fold lazy. | FAIL | RESEARCH | Lighthouse mobile LCP < 2.5 s on the hosted draft; `grep -c 'fetchpriority="high"' $W/lexsis-source.html` is 1 |
| CA33 | Stacked fixed bars | MA4 and MA5 budgets. | At most one top and one bottom fixed region; total fixed height at most 30 percent of the viewport. | FAIL | RESEARCH | MA5 script |

## 6. Diagnostic frame before shipping

Run every selling page through Fogg's B = MAP as Sarah Levinger applies it
(https://www.linkedin.com/posts/sarahlevinger_sometimes-customers-buy-sometimes-they-activity-7457081960512000000-kmqK ):

| Axis | Question | Typical failure on this page | Fix source |
|---|---|---|---|
| Motivation | Does the first screen make the shopper feel the outcome, not just read the spec? | Informative hero, no before-state, no proof beside the claim | `references/copy/copy-frameworks.md`, proof proximity rule |
| Ability | Can they buy in under a minute? | Too many SKUs unexplained, price needing justification, returns unclear, forced account | CA13 to CA16, MA rules |
| Prompt | Is the next step obvious at every scroll position? | Buried CTA, vague "Shop now", no closing CTA | CA4, CA8, CA9, CA30 |

Answer each in one line in `qa-report.md`.

## 7. Lint alignment

`design_lint.py` covers CA18 (N9), CA30 (A12, C4), CA26 partly (N11 manual, P1 to P4) and CA13/CA14 partly through O-rules. Adopt these static additions; the rest are browser checks recorded in `qa-report.md`.

```python
# CA1 NEW: auto-rotating carousels
r'data-autoplay="?true|autorotate|swiper-autoplay'                      # expect 0
# CA2 NEW: autoplay video without muted (Python: use lookahead on the tag)
r'<video(?![^>]*\bmuted\b)[^>]*\bautoplay\b'                            # expect 0
# CA7 NEW: paragraphs over 45 words (count tokens inside <p>...</p>)
# CA9 NEW: last content section id before footer in {closing-cta, final-offer, buy-box} on selling types
# CA12 NEW
r'infinite-?scroll|loadOnScroll'                                        # expect 0
# CA13 NEW
r'see price|contact (us )?for (price|pricing)|request a quote'          # expect 0 unless pageType == wholesale-b2b
# CA19 NEW: health-claim pages carry no urgency sections
# if re.search(r'clinical|doctor|dermatolog|cure|treat|relie(f|ve)', text, re.I): assert no '<!-- section: countdown' and no '<!-- section: stock-indicator'
# CA20 NEW
r'>\s*buy now\s*<'                                                       # expect 0 unless manifest page.funnelStage == 'bof'
# CA22 NEW: capture sections with more than one visible input
# CA27 NEW
r'100% (secure|safe)|ssl secured'                                        # expect 0
# CA28 NEW: distinct star averages / review counts on the page <= 1 each
r'\b[0-9]\.[0-9]{1,2} ?(stars|/ ?5|out of 5)\b'
# CA29 NEW
r'<h1[^>]*>[^<]*\b20[2-3][0-9]\b'                                        # expect 0 unless plan has an end date
# CA32 NEW
'fetchpriority="high"'                                                   # expect exactly 1
```

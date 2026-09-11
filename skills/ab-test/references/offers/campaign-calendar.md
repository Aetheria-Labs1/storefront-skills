# Campaign calendar

Campaign types, the occasions they attach to, and what each changes about the
hero, urgency, proof and offer. `page record` `campaign.type` takes one
id from the table below. The brief's campaign trigger vocabulary in
`references/page-types/_index.md` section 1 maps as: seasonal/holiday to
`seasonal` or `gifting`; sale window to `flash-sale`, `clearance`, `bfcm`,
`end-of-season` or `founder-sale`; collab/drop to `collab-drop`. Offer ids are
from `references/offers/offer-types.md`; urgency bases from
`references/offers/urgency-scarcity.md`; delivery-date rows go in the offer
ledger (`references/offers/offer-ledger.md`).

Dates below are for the 2026 and 2027 cycles. Fixed-calendar dates are
computed. Lunar and Hindu-calendar dates are tagged `confirm` and must be
checked against an almanac each year before a ship-by line is written.

## Campaign types

| Id | Lead time (page live before) | Hero treatment | Urgency treatment | Proof treatment | Offer treatment | Page-type fit |
|---|---|---|---|---|---|---|
| `evergreen` | none; always on | Product benefit; offer sits in `announcement` and `buy-box`, never in the headline | Dispatch cutoff only | Full proof ledger; reviews beside claims | `free-shipping`, `subscribe-save`, `bundle`, `first-order`; never called a sale; no permanent strike (PP3) | pdp, pdp-hybrid-landing, bundle-kit, subscription, collection-landing, homepage, advertorial, listicle, seo-buyers-guide |
| `launch` | waitlist page 4 to 8 weeks; launch page 1 week; proof refresh at +2 weeks | Pre-launch: mechanism teaser and "join the waitlist"; no price unless final ("from $X" only if true). Launch: product, price, ship date, founder note | Real drop time; real edition size; pre-order ship date | Pre-launch: founder credibility, ingredient or spec proof, press. Launch: early reviews and UGC as they arrive. Post-launch: verified counts | `none`, `gwp` or `price-lock` for the waitlist, `pre-order-price`, `limited-edition`; no percent at launch (sets the anchor low forever) | launch-waitlist-preorder, pdp-hybrid-landing, ugc-creator-collab |
| `restock` | back-in-stock list captured during stock-out; page live the hour stock lands | "Back in stock", the SKU, the true reason it sold out, variant availability grid | Live stock read; prior sell-out date as fact | Reviews accumulated during stock-out; waitlist size if real | `none`; back-in-stock SMS or email converts 12 to 20% without a discount (OPERATOR) | restock, pdp |
| `seasonal` | 4 to 6 weeks for search; 2 weeks for owned channels | Seasonal use case in the hero image and headline | Dispatch cutoff; season end date only if the price changes at season end | Season-specific reviews ("kept me warm at -5") | `bundle`, `free-shipping`, `gwp`; compare-at only if the was-price ran through the season | seasonal-gifting, collection-landing, ad-landing-page, homepage |
| `gifting` | gift guide 6 weeks out; cutoff banner 3 weeks out | Recipient framing ("for the runner in your life"), price bands, curated sets | Delivery cutoff per shipping speed, sitewide; ships-by on each card | Reviews that mention gifting; gift-presentation imagery | `gwp`, `bundle`, `free-shipping`, `gift-card` after cutoffs; modest `percent-off` for early planners only | seasonal-gifting, gift-guide, bundle-kit, homepage |
| `flash-sale` | 48 hours with a warmed SMS or email list | One product or collection, price, server-side clock | `countdown` bound to `endsAt`, hours not days; final-hours send | Bestseller badge from sales data; review count | `flash-sale` with `percent-off` or `fixed-off` on a narrow set; deepest of the year | sale-clearance-flash, offer-page, retargeting-warm |
| `clearance` | end of season; 1 week | "Final sale" grid; sizes remaining; honest depth | Live stock per variant | Ratings on cards | `clearance`; deep percent or fixed price points ("Everything $29"); "final sale, no returns" stated before add-to-cart | sale-clearance-flash, collection-landing |
| `collab-drop` | teaser 1 to 2 weeks; waitlist before drop | Creator plus product; creator's own words; real edition size | Drop time; unit cap with stopping counter | Creator's usage, not reviews; paid-partnership disclosure | `limited-edition`, `none`; creator code only if disclosed; never percent off | ugc-creator-collab, launch-waitlist-preorder, pdp-hybrid-landing |
| `anniversary` | 3 to 4 weeks | The story and one clear offer; founder letter section | Real campaign dates; text end date | Years in business, customer count, milestones, all verified in the proof ledger | `gwp` or sitewide `percent-off` or `fixed-off`; the "reason why" prevents training discounting | offer-page, homepage, brand-story-founder |
| `cause` | 2 to 3 weeks | Cause plus product; named charity | Campaign end date as text | Named charity, prior-year total if documented | `charity`; donation per order, not a discount; no stacking | brand-story-founder, offer-page, pdp, homepage |
| `back-to-school` | US: page live early July for Jul to Aug; India: early June for Jun to Jul | Bundles by grade or need; budget filters | "Delivery before first day" cutoff | Parent reviews | `bundle`, `free-shipping`, `tiered-volume` | bundle-kit, collection-landing, gift-guide |
| `bfcm` | list growth from September; segments by October; teaser Nov 1 to 20; early access Tue to Thu before Black Friday | One offer, one sentence ("30% off sitewide, ends Monday"), code auto-applied; category shortcuts; shipping cutoff strip | Real weekend end; final-hours SMS Monday evening; countdown only inside 48 hours | Bestseller badges, review counts, "N sold" only if true | `percent-off`, `fixed-off`, `gwp`, `bundle`; `loyalty` early access; segmented plus-ups by email or SMS, not deeper sitewide | sale-clearance-flash, offer-page, homepage, collection-landing |
| `end-of-season` | 2 weeks before the season turns | Last of the season's line; next-season teaser | Live stock; text end date | Ratings on cards | `clearance` or `percent-off` with a was-price that ran through the season; deepest discounts belong here, not mid-season | sale-clearance-flash, collection-landing |
| `founder-sale` | 3 to 4 weeks | Founder letter with the reason for the sale; one offer | Real dates | Founder note, verified milestones | `percent-off`, `fixed-off` or `gwp`; one depth, no tiers of codes | offer-page, homepage |

## Occasion calendar

| Occasion | Markets | 2026 | 2027 | Typical buying window | Delivery cutoff logic | Notes and typical offer |
|---|---|---|---|---|---|---|
| New Year | global | Jan 1 | Jan 1 | Dec 26 to Jan 15 | none (digital and resolution goods) | Wellness, fitness, planners; `subscribe-save`, `bundle` |
| Republic Day sale | India | Jan 26 | Jan 26 | Jan 17 to 26 | none | Marketplace-led sale week; bank `cashback` strips; electronics and fashion |
| Lunar New Year | China, SEA, diaspora | Feb 17 (confirm) | Feb 6 (confirm) | 3 weeks before | ship-by about 10 days before for cross-border | Red and gold gifting; `gift-card`; factories close 1 to 2 weeks, so restock dates slip |
| Valentine's Day | US, UK, EU, India metros | Feb 14 | Feb 14 | Feb 1 to 13 | standard ship-by about Feb 9; express to Feb 12 | Couples gifting; `gwp`, `bundle`; gift note mandatory |
| Holi | India | Mar 4 (confirm) | Mar 22 (confirm) | 10 days before | ship-by 5 days before | Colour, sweets, ethnic wear; modest offers |
| Eid al-Fitr | Middle East, South Asia, diaspora | about Mar 20 (confirm) | about Mar 9 (confirm) | Ramadan month before | ship-by 7 days before Eid | Gifting, fashion, food; `gift-card` |
| Akshaya Tritiya | India | Apr 19 (confirm) | about May 9 (confirm) | 1 week before | same-day or 2-day; jewellery insured shipping | Gold, silver, lab-grown jewellery; BIS hallmark proof; prepaid 82% of jewellery orders; EMI-on-UPI and BNPL 2.5x (GoKwik) |
| Mother's Day | US, India, most of world | May 10 | May 9 | Apr 25 to May 8 | standard ship-by about May 4; express to May 7 | Gifting; `gwp`, `bundle`; recipient framing |
| Eid al-Adha | Middle East, South Asia | about May 27 (confirm) | about May 16 (confirm) | 2 weeks before | ship-by 7 days before | Food, fashion, gifting |
| Father's Day | US, UK (Jun 21 2026, Jun 20 2027), India | Jun 21 | Jun 20 | Jun 5 to 19 | standard ship-by about Jun 15 | Gifting; tools, grooming, tech |
| Back to school | US Jul to Aug; India Jun to Jul | Jul 1 to Aug 31 | Jul 1 to Aug 31 | 6 weeks | "before first day" per district or state | `bundle`, `tiered-volume` |
| July 4 | US | Jul 4 (Sat) | Jul 4 (Sun) | Jun 25 to Jul 4 | not gifting; no cutoff | Summer and outdoor; `percent-off` sale weekend |
| Raksha Bandhan | India | Aug 28 (confirm) | about Aug 17 (confirm) | 2 weeks before | ship-by 5 to 7 days before; cross-city sibling gifting | Gifting to siblings; rakhi add-on; `gwp`; pincode estimate mandatory |
| Labor Day | US | Sep 7 | Sep 6 | Sep 3 to 7 | none | End-of-summer sale; `end-of-season` |
| Ganesh Chaturthi | India (Maharashtra, south, west) | Sep 14 (confirm) | about Sep 4 (confirm) | 1 week before | regional 2-day delivery | Decor, sweets, ethnic wear |
| Navratri and Durga Puja | India | Oct 11 to 19; Puja Oct 16 to 20 (confirm) | about Sep 30 to Oct 9 (confirm) | opens the festive season; marketplaces open sale about a week before | ship-by for Puja pandal dates in the east | Ethnic wear, festive fashion; marketplace sale opening is the first festive peak (Redseer) |
| Dussehra | India | Oct 20 (confirm) | about Oct 9 (confirm) | with Navratri | ship-by 3 days before | Appliances, vehicles, big-ticket |
| Halloween | US, UK | Oct 31 | Oct 31 | Oct 1 to 28 | ship-by about Oct 25 for costumes | Costumes, decor, candy; hard date |
| Dhanteras | India | Nov 6 (confirm) | about Oct 27 (confirm) | 3 days | same-day or next-day in metros | Gold, silver, utensils, appliances; the second festive peak (Redseer); jewellery about INR 85,000 crore in two days in 2025 |
| Diwali | India | Nov 8 (confirm) | about Oct 29 (confirm) | 3 weeks before; gifting has a hard date | ship-by 5 to 7 days before with festive carrier load; quick commerce takes the last 48 hours | Gifting, sweets, decor, apparel; bank `cashback`, no-cost EMI strips; member early access; "Diwali delivery by [date]" pincode check |
| Bhai Dooj | India | Nov 10 (confirm) | about Oct 31 (confirm) | with Diwali | as Diwali | Sibling gifting |
| Singles' Day | China, SEA | Nov 11 | Nov 11 | Nov 1 to 11 | none for domestic | Deep marketplace discounting; cross-border brands only |
| Thanksgiving, Black Friday, Cyber Monday | US, UK, EU, India (BF), global | Nov 26, 27, 30 | Nov 25, 26, 29 | teaser Nov 1 to 20; early access Nov 24 to 26 (2026); weekend; Cyber Monday | none for the sale; Christmas cutoffs start after | Shopify BFCM 2025: $14.6B, average cart $114.70, peak 12:01pm EST Black Friday; over 80% of offers at 25% off or deeper (CTC) |
| Green Monday, Super Saturday | US | about Dec 14; Dec 19 | about Dec 13; Dec 18 | Dec 11 to 20 | express only | Deadline-driven shoppers pay for express and need no discount |
| Christmas | US, UK, EU, India metros | Dec 25 | Dec 25 | three waves: Dec 1 to 10 planners, Dec 11 to 20 deadline-driven, Dec 21 to 25 rescuers | see procedure below; 2025 US carrier table: USPS Ground Dec 17, Priority Dec 18, Express Dec 20; UPS 3 Day Dec 19, 2nd Day Dec 22, Next Day Dec 23; FedEx 2Day Dec 22, Overnight Dec 23 | Gift guides, gift wrap, `gift-card` after cutoffs; deepest discounts after Dec 26 |
| Boxing Day | UK, AU, CA, NZ | Dec 26 | Dec 26 | Dec 26 to Jan 5 | none | Clearance opens; `end-of-season`, `clearance` |

## Delivery cutoff procedure for an occasion

1. Take the occasion date from the table and confirm any `confirm` date against an almanac; record the source in the ledger `delivery estimate` row.
2. Take the carrier last-ship date for each shipping speed the store offers (Shopify holiday shipping guide, or the carrier's published table for the year).
3. Subtract processing time from store settings and a 1 to 2 day buffer; the earlier of the resulting dates is the published cutoff for that speed.
4. Publish conservative dates and phrase them "Order by Dec 18 for expected delivery by Dec 24 with standard shipping". Never "guaranteed" (urgency-scarcity UR5).
5. International destinations get separate, earlier rows (US to UK about Dec 12, US to AU about Dec 10 in 2025 tables).
6. India: the pincode `delivery-estimate` island returns a date that accounts for festive carrier load; show COD availability with it (price-presentation PP22).
7. Schedule the hero switch: after the standard cutoff, express; after the express cutoff, `gift-card`. The passed cutoff text is removed by the island, not by hand.

## Gifting anatomy deltas

Apply on `seasonal-gifting`, `gift-guide` and any page whose campaign is
`gifting`:

| Element | Section id | Rule |
|---|---|---|
| Recipient framing | `hero`, `qualifier` | Headline addresses the giver about the recipient ("for the one who runs before sunrise"); collections by recipient, budget band ("Under ₹1,000", "Under $50") or interest, four to six of them |
| Ships-by line | `product-grid` cards, `buy-box` | Per product, from the cutoff procedure; absent if the product cannot arrive in time (hide the card or mark "arrives after [occasion]") |
| Sitewide cutoff | `delivery-cutoff` near the top; `announcement` | Standard and express dates with timezone; rolls automatically |
| Gift note | `gift-options` | Free text field, character limit stated, previewed |
| Gift wrap | `gift-options` | Priced add-on, un-ticked, price beside it ($3 to $5 typical); never pre-selected (offer-types OF6) |
| Gift receipt | `gift-options`, `shipping-returns` | "Gift receipt hides prices" stated; returns window for gifts stated (extended if the store extends it) |
| Gift-presentation imagery | `gallery`, `hero` | Image job `gift-presentation` and `included-items` from `references/assets/image-jobs-by-page-type.md`; the box, the wrap, the note in the shot |
| Fallback after cutoff | `hero`, `offer` | `gift-card` with schedule-send and message, "instant delivery, they choose" |
| Discount depth by wave | `offer` | Planners: modest `percent-off` or free standard shipping; deadline-driven: none needed, sell speed; rescuers: none, sell certainty; post-occasion: deepest |

## Rules

CC1. Set exactly one `campaign.type` from the table and record it in the plan's `## Page type` block under "Campaign"; a page serving two campaigns is two pages. HEURISTIC.
Check: `campaign.type` in `page record` is one of the 14 ids.

CC2. Honour the lead time. If the page cannot be live by the lead time, downgrade: a BFCM page with no list built becomes an `offer-page` with `campaign.type: evergreen`; a launch with no waitlist window becomes a launch-day `pdp-hybrid-landing`. OPERATOR (Klaviyo, Gosh Digital BFCM playbooks).
Check: the plan records the go-live date and the campaign's lead time; live date is on or before the deadline or the downgrade is written down.

CC3. Confirm every `confirm` date against an almanac for the year in question before writing a ship-by or "delivery by" line, and cite the source in the ledger. LAW (a wrong date is a false delivery claim).
Check: ledger `delivery estimate` row names the almanac or calendar source for lunar and Hindu dates.

CC4. Compute occasion cutoffs by the procedure above, never by copying last year's date. LAW and OPERATOR.
Check: the ledger row lists the carrier table URL, processing days and buffer used.

CC5. After a cutoff passes, the hero changes (express, then gift card); the page never keeps a passed cutoff and never goes quiet. OPERATOR (Glaze Digital last-orders guidance).
Check: `delivery-cutoff` is an island bound to dates, not static copy; the plan names the post-cutoff hero.

CC6. One offer per campaign page; segment-specific plus-ups (VIP drops every 4 to 8 hours during BFCM) go to email and SMS, not to a deeper sitewide figure on the page. OPERATOR (Klaviyo, CTC), consistent with offer-ledger rule 6.
Check: offer-types OF1.

CC7. Never discount at launch or on a collab drop; use early access, `gwp`, `price-lock` or `limited-edition` instead. OPERATOR (CTC: launch discounts set the anchor low forever).
Check: `campaign.type` in {`launch`, `collab-drop`} implies `offer.type` not in {`percent-off`, `fixed-off`, `bogo`, `flash-sale`, `clearance`}.

CC8. A seasonal or end-of-season strike-through needs a was-price that ran through the season for at least as long as the sale and met the volume test (price-presentation PP3). LAW.
Check: ledger `compare-at` row shows the was-price start date before the season start.

CC9. Evergreen offers are never called a sale and never carry a permanent compare-at. LAW (UK duration rule) and OPERATOR (perpetual discounting trains waiting; AccelerOI reports 30%+ AOV drops six months after perpetual-discount tests).

CC10. Model BFCM depth against margin first. Shoppers expect about 30% sitewide or "up to" with SKU-variable depth; 10 to 15% reads as no offer. If margin cannot support 25%+, use `gwp` or `bundle` instead of a shallow percent. OPERATOR (CTC 3,000-brand database).
Check: the plan records the contribution margin at the chosen depth and the ROAS target adjusted for it.

CC11. Put the deepest December discounts after Dec 26, not before; deadline-driven shoppers (Dec 11 to 20) pay for express and rescuers (Dec 21 to 25) pay for certainty. OPERATOR (Growthsuite).
Check: a `percent-off` or `fixed-off` on a gifting page dated Dec 11 to 25 is flagged in the plan with the merchant's reason.

CC12. Gifting pages carry gift note, un-ticked wrap, gift receipt wording, per-product ships-by and a sitewide cutoff. HEURISTIC and LAW (pre-ticked wrap is basket sneaking).

CC13. India festive pages show the bank `cashback` strip, no-cost EMI line for items over ₹3,000, COD or UPI-on-delivery statement, "inclusive of all taxes", a pincode delivery date, and member early access mirroring BFCM VIP. OPERATOR and LAW (Redseer, GoKwik, Legal Metrology).
Check: when `IN` is in markets and `campaign.type` in {`seasonal`, `gifting`, `bfcm`}, `payment-options`, `delivery-estimate` and the tax line are present.

CC14. Collab and creator campaigns disclose the paid partnership on the page and never show a percent. LAW (FTC Endorsement Guides; UK DMCC banned practices 12 and 13; India ASCI influencer guidelines).

CC15. Anniversary and founder-sale milestones ("10 years", "1 million customers") are proof-ledger rows with documents before they appear. LAW (design-rules N11).
Check: every numeral in `founder-note`, `stats` or `story` maps to a proof-ledger row with status `verified`.

CC16. Cause campaigns name the charity, the amount or percent per order, the period and any cap beside the price, and never stack a discount on the donation. LAW (UK CAP Code; FTC charitable-solicitation guidance; India CCPA).
Check: `campaign.type: cause` implies `offer.type: charity` and the `offer` text matches a named organisation and a figure.

## Sources

- Shopify BFCM 2025 data: https://www.shopify.com/news/bfcm-data-2025 ; Shopify holiday shipping guide (carrier cutoffs): https://www.shopify.com/blog/holiday-shipping-guide
- Adobe US holiday 2025: https://news.adobe.com/news/2026/01/adobe-holiday-shopping-season
- Klaviyo BFCM timing: https://www.klaviyo.com/blog/when-to-send-black-friday-emails ; Klaviyo BFCM checklist (VIP early access): https://www.klaviyo.com/blog/bfcm-checklist-guide ; Gosh Digital Klaviyo BFCM playbook 2026: https://www.goshdigital.co/blog/klaviyo-bfcm-playbook-2026
- Common Thread Collective BFCM offer depth: https://commonthreadco.com/blogs/ecommerce-playbook/how-to-craft-the-best-bfcm-offer-this-year ; offer database: https://commonthreadco.com/blogs/ecommerce-playbook/dig-in-bfcm-offer-database-2023
- Attentive BFCM campaigns and timing: https://www.attentive.com/black-friday-cyber-monday-2026/articles/bfcm-campaigns-that-convert ; https://www.attentive.com/black-friday-cyber-monday-2025/bfcm25-resources/timing
- December waves and gift-guide anatomy (Growthsuite): https://www.growthsuite.net/resources/shopify-holiday-campaigns/christmas-holiday-season ; last-orders messaging (Glaze Digital): https://glazedigital.com/blogs/news/guide-to-last-orders-messaging-for-christmas ; holiday deadlines (Attribute): https://www.getattribute.com/blog/holiday-shipping-deadlines
- Redseer India festive 2025: https://redseer.com/articles/e-commerce-festive-1st-leg-11-day/ ; Day 0: https://redseer.com/articles/festive-2025-day-0-ecommerce-sales-surge-25-with-gst-boost-demand-led-by-smartphones-and-tvs/ ; Datum festive first week: https://www.datumintell.in/festive-sales-reached-60-000-crore-in-the-first-week/ ; Dhanteras jewellery and GST 2.0 effects: https://www.firstresort.in/blogs/research/india-festive-retail-economy-2026
- Akshaya Tritiya 2026 (GoKwik via ET and Mediabrief): https://economictimes.indiatimes.com/industry/cons-products/fashion-/-cosmetics-/-jewellery/akshaya-tritiya-jewellery-buying-turns-more-prepaid-and-offer-led-led-by-tier-2-and-tier-3-demand/articleshow/130417402.cms ; https://mediabrief.com/akshaya-tritiya-2026-sees-3x-gmv-growth-from-smaller-cities-says-gokwik-report/ ; Fortune India: https://www.fortuneindia.com/business-news/akshaya-tritiya-2026-rising-gold-prices-digital-buying-reshape-jewellery-demand/132948
- Back-in-stock and SMS win-back benchmarks: https://conversion.studio/blog/sms-marketing-benchmarks
- Perpetual discounting effects (AccelerOI): https://www.acceleroi.com/blog/psychology-of-pricing
- UK CMA reference-pricing principles (seasonal was-price duration): https://assets.publishing.service.gov.uk/media/66ab4347a3c2a28abb50db3c/Discount_and_reference_pricing_principles.pdf
- India CCPA Dark Patterns (basket sneaking, charity add-ons): https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf

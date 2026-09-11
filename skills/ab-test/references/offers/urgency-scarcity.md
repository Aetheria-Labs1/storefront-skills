# Urgency and scarcity

What may be shown as a deadline, a stock level or a cohort limit, how it is
worded, where it sits, and when it is removed. Every urgency element is a row
in the offer ledger (`references/offers/offer-ledger.md`, rule 3) and binds to
`offer.endsAt` or `offer.stockVerified` in `page record`. The page-type
checklist's `urgency` field (`none`, `verified-only`, `encouraged`) caps what
this file allows; `encouraged` still means verified. Fake urgency as a dark
pattern is treated in depth in `references/anti-patterns/dark-patterns.md`;
this file covers only offer-specific rules.

## Legitimate bases

Only these four sources of urgency exist. Anything else is removed at design.

| Basis | Data binding | Display | Removal trigger | Preferred for |
|---|---|---|---|---|
| Real end date and time | `offer.endsAt` ISO datetime with timezone, confirmed by the merchant; server-side price revert at that instant | "Sale ends Sunday 11:59pm IST" in `announcement` or `sticky-cta`; `countdown` island bound to `endsAt` only in the final 24 to 48 hours | At `endsAt`; banner, timer and "last chance" copy share the field | `flash-sale`, `sale-clearance-flash`, BFCM |
| Live stock read | `stock-indicator` island bound to `lexsis_catalog.get` inventory at render; conservative threshold (show at or below 10 units or 10% of initial, whichever is lower) | "12 left in size M" beside the variant picker | Disappears when stock rises above the threshold or the SKU is replenished | `restock`, `clearance`, `limited-edition` |
| Cohort or edition cap | Counter bound to units sold or orders, stopping at the cap the merchant documented | "Edition of 500", "First 200 orders include the travel case" | Counter freezes at cap; "sold out" state persists | `launch-waitlist-preorder`, `limited-edition`, collab drops |
| Dispatch or delivery cutoff | Store dispatch schedule or carrier last-ship table plus processing time plus buffer; `delivery-cutoff` or `delivery-estimate` island | "Order by 2pm for dispatch today", "Order by Dec 18 for expected delivery by Dec 24" | Rolls to the next cutoff automatically; occasion cutoff disappears after the date | Every page type that sells; the default urgency |

## Evidence and its caveats

| Finding | Effect | Caveat | Tag | Source |
|---|---|---|---|---|
| Meta-analysis of 6,700 A/B tests | scarcity +2.9% RPV, social proof +2.3%, urgency and countdowns +1.5% | Most UI changes are within plus or minus 1%; plan on 0 to 5% | RESEARCH | https://gwern.net/doc/economics/advertising/2017-browne.pdf |
| Luguri and Strahilevitz (n=3,777, census-weighted) | Countdown timers did not significantly increase purchases | Timers were tested as a pressure tactic, not as information | RESEARCH | via https://cleancommit.io/blog/do-countdown-timers-work/ |
| Tiemessen et al., CHI 2023 (n=245) | Deceptive timers shifted choice about as much as a plain discount; rated manipulative; over 80% reported moderate to high regret on learning a deadline was fake | Study calls for a ban; regret is the cost the A/B test never measures | RESEARCH | https://gunesacar.net/assets/CHI-EA-23-Time-is-Ticking-Deceptive-Countdown-Timers.pdf |
| Prevalence of fake timers | 27 of 60 live timers deceptive (Tiemessen); 157 of 393 (Princeton 11k-site crawl) | Regulators cite these counts | RESEARCH | https://cleancommit.io/blog/do-countdown-timers-work/ |
| Hmurovic, Lamberton and Goldsmith (JMR) | Offline time-scarcity effects did not reliably appear online | Do not import retail-floor intuitions | RESEARCH | via https://cleancommit.io/blog/do-countdown-timers-work/ |
| Bob and Lush dispatch-cutoff line (CXL) | One line, "Free next business day delivery if you order before 4 PM", +27.1% revenue at 95% confidence | Single test, one store; the mechanism is information, not a clock | OPERATOR | https://cleancommit.io/blog/do-countdown-timers-work/ |
| Barton, Zlatevska and Oppewal 2022 (131 studies) | Scarcity effects roughly double for unfamiliar brands (0.41 vs 0.21); larger for high-involvement goods | Applies to true limited supply, not manufactured stock counts | RESEARCH | via https://cleancommit.io/blog/do-countdown-timers-work/ |
| Vendor claims ("+14% per Baymard", "+332%") | Unsupported | Treat as fabricated | HEURISTIC | https://cleancommit.io/blog/do-countdown-timers-work/ |

## Regulator wording

| Jurisdiction | Text | Penalty | Source |
|---|---|---|---|
| UK, DMCC Act 2024 Schedule 20 (in force 6 April 2025) | Banned practice: "pretend that a special offer will finish soon ... when this is not true"; banned practice 20: materially inaccurate information about market conditions or availability to induce purchase. CMA mattress work named "countdown clocks and other urgency claims". | CMA direct fines up to 10% of global turnover | https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices ; https://www.lewissilkin.com/insights/2024/08/28/pricing-and-discount-claims-was-misleading-now-compliant |
| EU, UCPD Annex I point 7 | Unfair in all circumstances: "Falsely stating that a product will only be available for a very limited time, or that it will only be available on particular terms for a very limited time, in order to elicit an immediate decision." 2021 guidance section 4.2.7 names countdown timers and fake stock as dark patterns. | National fines; up to 4% of turnover under the Omnibus Directive | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32005L0029 ; https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A52021XC1229%2805%29 |
| India, CCPA Dark Patterns Guidelines 2023, Annexure 1(1) "False Urgency" | "falsely stating or implying the sense of urgency or scarcity so as to mislead a user into making an immediate purchase ... including (i) showing false popularity of a product or service to manipulate user decision; (ii) stating that quantities of a particular product or service are more limited than they actually are." Applies to all platforms, advertisers and sellers offering in India. | CCPA penalties under Consumer Protection Act 2019 | https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf |
| US, FTC Act Section 5 | Fake deadlines and fake stock are false claims about availability or terms; deceptive practices. | Civil penalties via consent orders; state UDAP suits | https://www.ftc.gov/business-guidance |

## Rules

UR1. Show urgency only from one of the four bases above, each with the named data binding. Static copy never carries a deadline, a count or a viewer number. LAW.
Rationale: the three regulators above penalise the claim, not the intent; a hard-coded number is unverifiable by definition.

UR2. Bind every countdown to `offer.endsAt`, an ISO 8601 datetime with timezone that the merchant confirmed, and confirm the price reverts server-side at that instant. LAW.
Rationale: a timer that resets on reload or outlives the sale is the UK banned practice verbatim.
Check: `offer.endsAt` matches `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?([+-]\d{2}:\d{2}|Z)$`; ledger row `end date` is `verified`; no `countdown` island exists without it (type review T10).

UR3. Render stock statements only from a live inventory binding, with a conservative threshold, and let them disappear when stock is replenished. Never show a count on a made-to-order or unlimited SKU. LAW.
Rationale: India CCPA 1(ii) and UK banned practice 20 both target overstated scarcity.
Check: `offer.stockVerified` is true for any `stock-indicator`; the island reads `lexsis_catalog.get` at render (proof-ledger kind `stock-count`).

UR4. Make edition and cohort counters stop at the documented cap and keep the "sold out" state visible afterwards; never replenish under the same "limited" label. LAW.
Rationale: a limited edition that restocks is a false availability claim.
Check: ledger row records the cap and its source document; `limited-edition` pages include a post-cap state in the design.

UR5. Prefer the dispatch or delivery cutoff over any other urgency. Compute it from the store dispatch schedule or the carrier last-ship date plus processing time plus a 1 to 2 day buffer; phrase as expected, not guaranteed. OPERATOR and LAW.
Rationale: the only urgency form with a clean positive test (+27.1% revenue, Bob and Lush); also the only one that is pure information. "Guaranteed by Christmas" is a liability the merchant cannot control.

UR6. Keep urgency out of the hero on `tof` page types and out of educational content everywhere: no timers or counts in `advertorial`, `listicle`, `video-sales-page`, `ingredient-science`, `brand-story-founder`, `faq-support-led`, `quiz-funnel`, or inside `mechanism`, `how-it-works`, `size-guide`, `faq` sections on any page. HEURISTIC, consistent with `references/page-types/_index.md` and `funnel-stages.md` FS6.
Rationale: a cold reader has no desire yet; pressure before desire reads as an ad and is skipped (banner blindness). The checklist for those types sets `urgency: none` and lists `countdown` under `forbidden_sections`.
Check: `page.funnelStage` is `tof` implies no `countdown` or `stock-indicator` section index is 0 or 1; none of the named sections contains a timer or count.

UR7. Run a sale countdown only in the final 24 to 48 hours of the window; before that, show the end date as text. OPERATOR.
Rationale: a six-day countdown communicates nothing on day six and trains the visitor to ignore it.
Check: the `countdown` island's `show-when-within` (or equivalent) is at most 48 hours, or the plan schedules the island's publish for `endsAt` minus 48 hours.

UR8. Show no timers, counts or "last chance" on luxury pages or on goods over about $500, except a genuine seasonal event window or a real edition cap phrased as exclusivity ("Edition of 50"). HEURISTIC and OPERATOR, consistent with `references/vertical-luxury.md` and offer-types OF3.
Rationale: urgency implies the product might not sell otherwise; exclusivity implies the opposite.
Check: when the plan loads `vertical-luxury.md`, no `countdown` or `stock-indicator` section exists; edition counts are phrased without "only" or "left".

UR9. Phrase urgency as information, never as pressure: state the fact, the time and the timezone. Forbidden words and forms: "Hurry", "Don't miss out", "Selling fast", "Almost gone", "Only N left" without binding, "N people are viewing", "Limited time" without a date, exclamation marks, ALL CAPS. HEURISTIC and LAW.
Rationale: India CCPA names "false popularity"; design-rules N9 forbids ALL-CAPS status pills; plain statements tested better in SMS (Attentive: plain verbs +9%).

UR10. Bind the banner, the timer, the "last chance" copy and the price to the same `endsAt` so all four disappear or revert together. LAW.
Rationale: a banner that outlives the sale by a day is the UK banned practice.
Check: every string containing "ends", "last chance" or "until" on the page is inside an island that reads `offer.endsAt`; none is in static copy.

UR11. Never render a cart reservation timer ("items reserved for 10:00"). LAW.
Rationale: Shopify does not reserve inventory at add-to-cart; the claim is false on its face.

UR12. Never render live viewer counts, "N bought in the last hour" toasts or social-proof popups. LAW and HEURISTIC.
Rationale: proof-ledger lists `social-proof-popup` and `live-viewer-count` as never verified; India CCPA "false popularity".
Check: proof vocabulary kinds `social-proof-popup` and `live-viewer-count` are absent from the proof ledger and the source.

UR13. Never extend a deadline that the page called final; if the merchant extends, the new window is a new campaign with new copy and no "extended" framing on the same page. OPERATOR and LAW.
Rationale: "an honored deadline this year is what makes next year's urgency work" (Attentive); an extended "last chance" is a false statement about the earlier deadline.

UR14. Place sitewide deadlines in `announcement` or `sticky-cta`, product-specific cutoffs between price and add-to-cart in `buy-box`, and occasion cutoffs in a `delivery-cutoff` section near the top of `seasonal-gifting` pages. Never place urgency in `faq`, `size-guide`, `mechanism`, `how-it-works` or `footer`. HEURISTIC and OPERATOR.
Rationale: urgency belongs at the decision point it informs; anywhere else it is noise or pressure.
Check: `countdown`, `stock-indicator` and `delivery-cutoff` sections appear only in the named positions; no `data-behavior="countdown"` inside those forbidden sections.

UR15. Fold the offer end date into the offer ledger before design and record the merchant's answer to "will this deadline be honoured with no extension?"; a "no" or "unsure" means text end date only, no countdown. LAW.
Rationale: offer-ledger rule 3 and the "Claims to confirm" list.
Check: ledger row `end date` has a `Confirmed` value naming the merchant and date.

UR16. Set `urgency` in the page-type checklist as the ceiling: `none` allows no urgency element; `verified-only` allows any of the four bases with bindings; `encouraged` means the type benefits from a dispatch cutoff and a real end date, still verified. LAW.
Rationale: the checklist is machine-enforced by the type checklist review T10.
Check: the type checklist review passes; no `countdown` or `stock-indicator` section on a type whose checklist says `urgency: none`.

## Dispatch cutoff pattern

The default urgency for every buying page. Procedure:

1. Read the store's dispatch schedule (cutoff time, timezone, dispatch days) and the carrier last-ship table for the occasion, if any.
2. Compute: cutoff = carrier last-ship date minus processing days minus buffer (1 to 2 days). For same-day dispatch, cutoff = store cutoff time in store timezone.
3. Write the line as fact plus consequence: "Order by 2pm IST, Monday to Saturday, for same-day dispatch" or "Order by Dec 18 for expected delivery by Dec 24 with standard shipping". Use "expected", never "guaranteed" (UR5).
4. Bind it: `delivery-cutoff` or `delivery-estimate` island reading the schedule so the line rolls over automatically; on India pages, the pincode estimate returns a date (`price-presentation.md` PP22).
5. Ledger it: row `delivery estimate` with the source (store settings, carrier table URL) and the buffer used. International cutoffs are earlier (US to UK about Dec 12, US to AU about Dec 10 in the 2025 tables) and need their own rows.
6. After the last cutoff: switch the hero to express shipping, then to `gift-card`; never leave a passed cutoff on the page (`campaign-calendar.md` CC8).

## When the merchant wants urgency and has no basis

Ask once, in this order, and stop at the first yes:

| Question | If yes | Ledger row |
|---|---|---|
| Is there a real end date and time for this price, and will it be honoured? | Text end date in `announcement`; `countdown` only inside 48 hours | end date |
| Does the store dispatch on a fixed schedule, or is there an occasion delivery date? | `delivery-cutoff` line (UR5) | delivery estimate |
| Is any variant genuinely low in stock, and is inventory tracked in Shopify? | `stock-indicator` bound to live inventory with a conservative threshold | stock statement |
| Is the run capped at a documented number of units? | Edition count with a stopping counter, no "only" or "left" | stock statement (cap) |
| None of the above | No urgency element. Offer the merchant the alternatives that do not need a basis: a verified review count beside the CTA (proof-ledger), a guarantee line (`guarantee`), the free-shipping threshold, or a real launch date for the next drop. Record the request and the refusal in `page plan` under "Claims confirmed". | none |

The agent never invents a deadline "to test". A test of fake urgency is a
test of a banned practice; the measured lift includes the regret and refund
cost the test does not capture (Tiemessen 2023).

## Sources

- Browne and Swarbrick Jones 2017 meta-analysis: https://gwern.net/doc/economics/advertising/2017-browne.pdf
- Tiemessen et al., CHI 2023, deceptive countdown timers: https://gunesacar.net/assets/CHI-EA-23-Time-is-Ticking-Deceptive-Countdown-Timers.pdf
- Clean Commit review of countdown evidence (Luguri and Strahilevitz, Princeton crawl, Bob and Lush, Barton et al., vendor claims): https://cleancommit.io/blog/do-countdown-timers-work/
- UK CMA unfair commercial practices guidance (CMA207): https://www.gov.uk/government/publications/unfair-commercial-practices-cma207/unfair-commercial-practices ; business summary: https://www.gov.uk/government/publications/what-businesses-need-to-know-about-unfair-commercial-practices/what-businesses-need-to-know-about-unfair-commercial-practices ; Lewis Silkin on CMA urgency findings: https://www.lewissilkin.com/insights/2024/08/28/pricing-and-discount-claims-was-misleading-now-compliant
- EU UCPD text: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32005L0029 ; 2021 UCPD guidance: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A52021XC1229%2805%29
- India CCPA Dark Patterns Guidelines 2023: https://www.nls.ac.in/wp-content/uploads/2021/04/Dark-Patterns.pdf ; summary: https://www.scconline.com/blog/post/2023/12/04/ccpa-notifies-guidelines-for-prevention-and-regulation-of-dark-patterns-2023-legal-news/
- Attentive on honoured deadlines and flash-sale timing: https://www.attentive.com/black-friday-cyber-monday-2026/articles/bfcm-campaigns-that-convert ; plain-verb SMS copy: https://www.attentive.com/black-friday-cyber-monday-2026/articles/bfcm-campaign-best-practices
- Countdown placement data (Liquidboost): https://liquidboost.app/blog/countdown-timer-conversion-data
- Shopify holiday shipping guide (carrier cutoffs): https://www.shopify.com/blog/holiday-shipping-guide ; Attribute holiday deadlines: https://www.getattribute.com/blog/holiday-shipping-deadlines ; last-orders messaging: https://glazedigital.com/blogs/news/guide-to-last-orders-messaging-for-christmas

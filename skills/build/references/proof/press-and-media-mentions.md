# Press and Media Mentions

Sourcing and verification behind the `press-logo-linked`, `press-quote-linked`
and `award` rows of the plan's `## Proof ledger`
(`references/proof/proof-ledger.md`). A logo is a claim that an outlet chose,
on its own editorial judgement, to feature this brand. The agent proves that
claim before the logo exists in source. `press-logo-unlinked` is never
rendered. Rule tags: LAW, RESEARCH ([H] [M] [L]), OPERATOR, HEURISTIC.

## Eligibility test

All four must pass for a logo. A quote needs the same four plus verbatim text.

| Test | Pass | Fail |
|---|---|---|
| Editorial decision | the outlet's staff or a named contributor chose to cover the brand | paid placement, advertorial, affiliate commission without disclosure, wire release |
| Identifiable brand or product | brand or product named, pictured with visible branding, or linked | unbranded prop in a photo shoot; "a serum like this one" |
| Recency | published within 24 months; within 12 months for any "as seen" or "featured" caption | older coverage without a year label (ASA Lifes2good: a 2009 appearance did not support a 2013 claim) |
| Live URL | fetched on the plan date, brand text confirmed in the body | 404, paywall the agent could not read, archive-only, screenshot supplied by the merchant |

## Verification procedure

Run once per outlet, before any logo or quote enters source. Record the
result in the ledger row. No record, no logo.

| Step | Action | Record |
|---|---|---|
| 1 | host web search: `"<brand>" site:<outlet-domain>`; also `"<brand>" "<outlet name>"` | result URLs |
| 2 | fetch the article; confirm the brand or product name appears in body text, not only in a comment or ad slot | URL, headline, author, date |
| 3 | classify: editorial, advertorial or sponsored, wire release, affiliate roundup, podcast episode, award | class |
| 4 | for affiliate or sponsored: check for "affiliate", "sponsored", "paid", "partner", "we may earn a commission" on the page | disclosure text |
| 5 | for awards: fetch the awarding body's own page listing the winner and year | body URL |
| 6 | write the row; status `verified` only for class editorial, podcast episode or award; `pending` for affiliate or sponsored until the caption carries the disclosure; `dropped` for wire | row |

## What counts and what does not

| Item | Counts as press | Ledger kind | Caption |
|---|---|---|---|
| Staff-written feature, review, or interview naming the brand | yes | `press-logo-linked` or `press-quote-linked` | "In the press" or "Featured in" |
| Named contributor column that chose the product | yes | same | same |
| Podcast episode where the host discusses the brand editorially, with an episode URL | yes | `press-quote-linked` (episode link) | "Discussed on <show>" |
| Award from a body with a public winners page (Allure Best of Beauty, Good Housekeeping, Red Dot) | yes | `award` | "Winner, <award> <year>" |
| Best-of listicle with affiliate links, brand pays commission | only with disclosure | `press-logo-linked`, status `pending` until captioned | "Named in <outlet>'s best-of list (affiliate)" or omit |
| Paid placement, sponsored content, host-read ad, advertorial | not press | `press-logo-linked` only with the paid caption | "As advertised in <outlet>" or "Sponsored feature" |
| Wire release (PRNewswire, BusinessWire, PTI, ANI) and syndicated copies on Yahoo Finance, MarketWatch, AP "press release" sections | never | `dropped` | none; at most "Press release" text link in the footer |
| Listicle or directory that merely links to the store | never | `dropped` | none |
| Coverage where the product is an unbranded prop | never | `dropped` | none |
| TV or video appearance where the product was placed for a fee | not press | paid caption only | "As advertised on" |

## Logo treatment

| Property | Rule |
|---|---|
| Colour | monochrome, one neutral from the page palette; never the outlet's brand colour, never a gradient |
| Size | one cap height for the row; equal optical weight; no outlet enlarged |
| Count | three to six; fewer than three: render quotes instead of a logo row |
| Link | each logo is inside `<a href="<article URL>" rel="noopener">` |
| Accessible name | `alt` or `aria-label` is the publication name plus "article" ("Vogue India article") |
| Format | inline SVG or SVG file; never a raster screenshot of a masthead; never generated art |
| Alteration | scale and single-colour fill only; never redraw, crop or retype the wordmark |
| Motion | static; no marquee unless the announcement island supplies it (`design-rules.md` N10) |

## Placement by page type

| Page type | Position | Never |
|---|---|---|
| `ad-landing-page`, `pdp-hybrid-landing` | directly below the hero (`press-marquee`) or beside the review module | inside the hero headline block |
| `pdp` | beside or below `review-summary`; or in `press-quotes` near reviews | above the buy box |
| `advertorial`, `listicle`, `video-sales-page` | one quote inline where it supports a reason; logos after the article body, before the offer bridge | in the hero; before the "Advertisement" disclosure |
| `homepage`, `brand-story-founder` | trust row below the first screen | as the first thing on the page |
| `comparison-us-vs-them` | near the verdict as `press-quotes` | inside the comparison table cells |
| `seo-buyers-guide` | one `press-quote-linked` per ranked entry where an outlet reviewed that product; methodology section may cite sources | logo row in the hero or table |
| luxury vertical | editorial quotes only, one to three, no logo row | logo marquee |
| `thank-you-post-purchase`, `faq-support-led`, `lead-capture-giveaway` | none | any |

## Caption rules

| Caption | Allowed when |
|---|---|
| "In the press", "Press" | every logo in the row is editorial |
| "Featured in" | editorial and the product itself was covered |
| "As seen in" | editorial, the product is pictured or named, within 12 months |
| "As advertised in", "Sponsored feature" | paid placement; mandatory wording for paid |
| "Named in <outlet>'s best-of list (affiliate)" | affiliate roundup; disclosure must be on this page, not only on the outlet's |
| "Recommended by <outlet>", "Endorsed by" | only if the article literally recommends the product in those words |
| "Award-winning" | only beside the award name, body and year |

## Press quotes

| Rule | Detail |
|---|---|
| Verbatim | exact words; `[…]` trim only; never stitch two paragraphs |
| Attribution | outlet, author where bylined, month and year, link |
| Scope | the quote is about this brand or product, not the category |
| Permission | CAP 3.48 allows accurate published quotes without express permission; still record the URL and date |
| Quantity | one to three on a page; a quote replaces a logo, it does not duplicate it |

## Ledger row template

```markdown
| P3 | press-logo-linked | credibility | Vogue India | https://www.vogue.in/<path> ; headline "<headline>"; author; 2026-03-14; class editorial | fetched 2026-09-10, brand named in body | press-marquee | verified |
| P8 | press-quote-linked | "melts in seconds" | Mint Lounge | https://lifestyle.livemint.com/<path> ; quote verbatim; author; 2025-11-02 | fetched 2026-09-10 | benefits | verified |
| P9 | award | quality | Allure Best of Beauty 2025 | https://www.allure.com/<winners page> ; category; year | fetched 2026-09-10 | awards | verified |
| P10 | press-logo-linked | credibility | Yahoo Finance | PRNewswire syndication of the brand's own release | wire | — | dropped (wire release) |
```

## Rules

PM1. Never render a press logo or quote whose ledger row lacks a fetched URL that names the brand or product. LAW CAP 3.7 and 3.1 (ASA v. MPJ Invest 2023: "as seen in" with no evidence upheld); FTC Endorsement Guides (a publication name is an endorsement).
Check:
```bash
perl -0ne 'while(/<!-- section: (press[a-z-]*|awards) -->(.*?)(?=<!-- section: |\z)/gs){my $b=$2; my $imgs=()=$b=~/<img/g; my $links=()=$b=~/<a [^>]*href="https?:/g; print "imgs=$imgs links=$links\n"}' $W/lexsis-source.html   # links >= imgs in every press section
```

PM2. Only editorial coverage earns a logo without a paid caption; paid, sponsored and host-read placements carry "As advertised in" or "Sponsored feature" in the same visual field. LAW ASA v. Ergoflex 2012 ("as seen in" implies an editorial decision); NAD LegalZoom (paid or affiliate "As Seen In" needs on-page disclosure).
Check: for each row of class paid, the section text contains "advertised" or "Sponsored".

PM3. Wire releases and their syndicated copies never earn an outlet's logo or a "featured" caption. LAW ASA "As seen on TV" guidance; CAP 3.7.
Check: no ledger press row has source domain in the wire list (prnewswire, businesswire, globenewswire, ptinews, aninews) or a syndication path containing `/news/press-release` or `/prnewswire/`.

PM4. Affiliate roundups render only with an on-page affiliate disclosure, or are omitted; omission is preferred. LAW FTC 16 CFR 255.5; NAD LegalZoom.
Check: rows of class affiliate have status `pending` unless the caption contains "affiliate".

PM5. Coverage must be within 24 months; any "as seen" or "featured" caption within 12 months; older coverage carries the year in the caption or is dropped. LAW ASA v. Lifes2good (stale coverage).
Check: ledger date fields; `date >= plan date minus 730 days`, or the caption contains the year.

PM6. Three to six logos in one row at one cap height, monochrome, each an `<a>` to its article with the publication as accessible name; fewer than three verified outlets renders quotes, not logos. HEURISTIC; consistent with `proof-ledger.md` display rule 6.
Check:
```bash
perl -0ne 'while(/<!-- section: press-marquee[a-z-]* -->(.*?)(?=<!-- section: |\z)/gs){my $b=$1; my $n=()=$b=~/<a [^>]*href/g; print "logos=$n\n"; print "missing-name\n" if $b=~/<img(?![^>]*(alt="[^"]+"|aria-label="[^"]+"))/}' $W/lexsis-source.html   # 3 <= logos <= 6, no missing-name
```

PM7. Never place press in the hero headline block; on advertorials never before the "Advertisement" disclosure. RESEARCH [M] Trustpilot: media mentions weigh most during initial research, so they belong after the premise; HEURISTIC placement table above.
Check: the `hero` section contains no `press` markup; on `advertorial` the disclosure section precedes any press row in DOM order.

PM8. Never write "Recommended by", "Endorsed by", "Loved by <outlet>" unless the fetched article uses that verb about this product. LAW CAP 3.7; CCPA 2022 (no unjustified reference to an institution).
Check:
```bash
grep -ciE '(recommended|endorsed|loved|approved) by (vogue|elle|forbes|mint|the hindu|times|wired|gq|allure|cosmopolitan|nykaa|amazon)' $W/lexsis-source.html   # 0 unless the ledger quote contains the verb
```

PM9. Quote press verbatim with outlet, author, date and link; never stitch sentences from different paragraphs. LAW CAP 3.48.
Check: each `press-quote-linked` body appears contiguously in the fetched article text.

PM10. Podcasts count only with an episode URL where the host names the brand editorially; paid host-read ads take the "As advertised on" caption. HEURISTIC; consistent with the ledger's "podcast without episode link" exclusion.
Check: podcast rows carry an episode URL, not a show homepage.

PM11. Awards need the awarding body's own page, the category and the year; "award-winning" appears only beside those three. LAW CAP 3.7 substantiation; FTC reasonable basis.
Check: `grep -ci 'award-winning' $W/lexsis-source.html` is 0, or each hit's section contains a year and a link to the body.

PM12. Logos are trademarks: single-colour scaling only, never redrawn or retyped; remove a logo on any outlet request and record the removal. HEURISTIC [L] PR-agency guidance on logo use.
Check: press SVGs are the outlet's own files, filled with one `currentColor`; no `<text>` element that spells an outlet name inside a logo `<svg>`.

PM13. Every press row appears in `page-plan.md` under "Claims to confirm" so the merchant can object before design. OPERATOR.
Check: `grep -c 'press-' page-plan.md` under the ledger equals the count under "Claims to confirm".

## Jurisdiction notes

| Where | Rule that bites |
|---|---|
| UK | CAP 3.7 substantiation; ASA treats "as seen in" as an implied independent endorsement (Ergoflex 2012, MPJ Invest 2023) |
| US | FTC Act s.5 and Endorsement Guides: an organisation's name or seal is an endorsement; NAD LegalZoom on affiliate "As Seen In" boxes |
| EU | UCPD misleading action, Art. 6; Annex I 4 (false approval or endorsement) |
| India | CCPA 2022 Guidelines cl. 4: no unjustified reference to a person, institution or publication |

## Sources

- ASA "As seen on TV" advice (Ergoflex, Lifes2good): https://www.asa.org.uk/advice-online/as-seen-on-tv.html
- ASA v. MPJ Invest 2023: https://www.asa.org.uk/rulings/mpj-invest-ltd-a22-1164599-mpj-invest-ltd.html
- NAD LegalZoom "As Seen In" decision: https://www.jdsupra.com/legalnews/nad-decision-considers-as-seen-in-claims-1309590/
- CAP Code 3.45 to 3.48: https://www.asa.org.uk/type/capcode/code%5Frule/3.45.html ; testimonials advice: https://www.asa.org.uk/advice-online/testimonials-and-endorsements.html
- FTC Endorsement Guides 2023: https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising
- CCPA Misleading Ads Guidelines 2022: https://consumeraffairs.nic.in/theconsumerprotection/guidelines-prevention-misleading-advertisements-and-endorsements-misleading
- Trustpilot social proof survey (media mentions 52% during research): https://uk.business.trustpilot.com/guides-reports/build-trusted-brand/why-and-how-social-proof-influences-consumers
- Logo permission heuristics [L]: https://www.jwcpr.com/do-i-need-permission-for-using-logos-on-my-website/

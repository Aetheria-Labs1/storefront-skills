# Lead capture and giveaway page

The page trades an incentive for an email address or phone number. The
visitor is cold: they came from a social ad, a creator post, a partner
giveaway or an affiliate link, and they are not shopping yet. Their one job
is to submit a single-field form. The page states the incentive and its
exact value, shows the terms and the consent language in the open, and
sends nothing else competing for the click. Its metric is opt-in rate and
cost per consented contact, followed by the welcome flow's revenue.

## Identify it

- The brief asks for emails or phone numbers rather than sales: "giveaway",
  "enter to win", "get 10% off", "download the guide", "early access list",
  "build the list before BFCM or Diwali", cold TikTok traffic with
  entertainment intent.
- Near neighbours: `quiz-funnel` when the answers change the recommendation;
  a form with a prize does not route, so it is capture.
  `launch-waitlist-preorder` when the product is not yet purchasable and the
  incentive is access, not a prize. `offer-page` when the visitor can buy on
  the page. A popup on another page is not a page type; this file is for the
  dedicated URL.

## Variants

- Discount for email or phone: incentive is `first-order`; the code is
  delivered by message, never shown on the page.
- Giveaway or contest: incentive is a prize with a stated value, entry
  window, draw date, eligibility and official rules.
- Lead magnet: incentive is a guide, checklist or sample offer; PAS headline.

## Anatomy

1. `hero` mandatory: headline names the incentive and its exact value, one
   sentence on what the messages will contain and how often, the prize or
   product image.
2. `giveaway-entry`, `email-capture` or `sms-capture` mandatory: one form,
   one field by default (email or phone), never more than three fields;
   unticked, separate consent boxes for email and SMS; button text states
   what happens ("Send my code", "Enter the giveaway"); confirmation state
   tells the visitor where the code or entry confirmation arrives and when.
   Schema comes from `lexsis_capture.form_schemas`.
3. `offer-prize` conditional: the incentive is a prize or gift; image, retail
   value, number of winners, what is included, substitution policy
   (satisfies `offer`).
4. `how-it-works` conditional: giveaway or contest; three steps, entry open
   and close datetime with timezone, draw date, how winners are notified and
   by when, eligibility (age, countries), bonus entries if any.
5. `trust-bar` or `review-summary` recommended: one verified proof line:
   subscriber count from an export, rating with count, past winner names
   with consent, or the privacy fact ("One message a week. Unsubscribe in
   one tap.").
6. `legal-terms` mandatory: on-page block directly under the form, not only
   in the footer: link to official rules or offer terms, sponsor name,
   eligibility, free entry method where sweepstakes law requires one,
   privacy policy link, how to opt out (satisfies `legal`).
7. `countdown` conditional: the entry close datetime is verified in the
   offer ledger; it counts to the draw close and disappears afterwards.

A discount-for-email page is sections 1, 2, 5 and 6. A giveaway adds 3 and 4.

## Workflow

### Context reads
1. `lexsis_catalog.get` for the prize, or the product the code applies to:
   media position one as the `identity` packshot (viewed), a `packaging` or
   included-items shot when the prize is a physical gift, the retail price
   (only to state the prize value in the ledger), the exact variant that will
   ship. Jobs per `references/assets/image-jobs-by-page-type.md`.
2. `lexsis_capture.form_schemas` for the email, phone or giveaway schema:
   field ids, the consent field, required flags, the confirmation text.
   Confirm at most three fields (one on cold paid traffic). SMS needs the
   registered consent template (India DLT) or the TCPA disclosure in the
   schema; without it SMS is not captured on this page.
3. `lexsis_brand.context` and `lexsis_brand.brand_kit` for `theme_id`, the
   logo asset (rendered non-clickable), palette hexes for any backdrop, voice
   and banned phrases. Skip `lexsis_brand.navigation`: nav is `none`.
4. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`:
   `product-shot`, then `hero`, then `flat-lay`; then semantic "<prize>
   packshot"; view with `lexsis_assets.view`. One image, two at most.
5. Proof source, one of: `lexsis_catalog.reviews_status` (a `review-summary`
   needs 5 or more reviews), a subscriber count export (rounded down, dated),
   or past winners with written consent. Each is a proof ledger row; the
   message-frequency fact (`policy-fact`) is always a row.
6. Merchant-confirmed offer ledger rows: the incentive and its exact value,
   how and when it is delivered (code by message, never on the page), entry
   open and close datetime with timezone, draw date, winner notification
   method and deadline, eligibility, official rules URL, sponsor, free entry
   method where required, privacy URL, opt-out path, message frequency as a
   number; counsel confirmation per market for a sweepstakes. Consent and
   form rules: `references/anti-patterns/dark-patterns.md` (DP5, DP6, DP7,
   DP14, DP15).
7. `lexsis_design.islands`, then `lexsis_design.island_schema` for
   `EmailCapture`, `FunnelRuntime` and, only with a verified end datetime,
   `CountdownTimer`. `Modal` is read only for pages that link here; it never
   mounts on this page.

### Section by section
Media lines follow `references/workflows/section-asset-workflow.md` and
`references/assets/asset-sourcing-sequence.md`; aspects from
`references/assets/slot-spec.md`. When every step finds nothing: tell the
merchant what is missing (job, aspect, count), offer upload via
`lexsis_asset_upload.upload` or generation when the purpose is feasible
under `references/assets/generation-policy.md`, and skip or merge the section
only if the merchant chooses; in fast-draft, proceed with the closest
existing asset or leave the slot `planned` and list it in the plan and draft
summary. Island lines name the island and the decision inputs; variants and
props are resolved live from `lexsis_design.island_schema`
(`references/workflows/island-selection-workflow.md`). Copy ceilings follow
this file's Copy section and `references/anti-patterns/copy-anti-patterns.md`. No asset is
used sight unseen: every candidate is opened with `lexsis_assets.view` and
judged against its section with the fit review in section 1b of
`references/workflows/section-asset-workflow.md` (the subject does the job,
it crops to the slot aspect without losing the subject, a quiet area holds
the copy, lighting and palette match the neighbouring slots, no baked-in
text, watermark or promo overlay); a generated backdrop or texture is viewed
the same way when it returns.

**`hero`**
- Purpose: name the incentive and its exact value, say what the messages
  contain and how often, show the prize or product.
- Media: yes. Job `identity` as a `packshot` hero; `product-in-context` is
  the alternate for a lifestyle prize using a photo the merchant or partner
  owns with a licence on record. Catalog media position one, then library tag
  `product-shot`, then `hero`, then merchant or partner upload; view with
  `lexsis_assets.view` and confirm the prize as it ships, a portrait crop
  that keeps it and a quiet area for the headline and form. Gap: ask the
  merchant (prize packshot, portrait crop, one image); upload, or `hero_bg`
  as a plain backdrop behind a real cut-out; the prize is never generated
  (GN1, GN2). A lead magnet with no physical prize is typographic, or shows
  the real cover file of the guide if the merchant supplies it. No-go: stock
  people celebrating, confetti or gift-box art, a drawn gift card, text baked
  into the image, a hero with no image when a physical prize exists.
- Island: `none`. Logo as a plain `<img>` or text wordmark without a link;
  one static `<picture>` whose portrait crop leaves the whole form visible
  above the fold at 390 (media at most 60% of the viewport height).
- Copy: headline 10 words with the value; one sentence, 20 words, with the
  frequency as a number.
- Decide with: prize type from the brief; the image inventory from reads 1
  and 4.

**`giveaway-entry`**, **`email-capture`** or **`sms-capture`**
- Purpose: the one form and the one CTA of the page.
- Media: no. The form is the object; it sits directly under the hero image
  with its consent text and button visible without scrolling.
- Island: `EmailCapture` for a single email field; `FunnelRuntime` inline for
  two or three fields (name plus email, or a phone step) with steps built from
  the read-2 schema via `lexsis_drafts.funnel_create` and checked with
  `lexsis_capture.validate_funnel`. Inputs: field count, channel, market.
  Resolve props from `lexsis_design.island_schema`; no discount line on the
  page (the code travels by message); the unticked consent checkbox with full
  disclosure is authored in HTML beneath the island, never `required`,
  separate boxes for email and SMS (DP5); any celebratory motion off (N10).
  No `Modal` on this page; on pages that link here, `Modal` as exit intent
  only, once per session, with `EmailCapture` as its only child, resolved
  from the schema.
- Copy: button names the delivery; consent text in full for the market;
  confirmation state names the channel and the wait.
- Decide with: the schema in read 2; the consent template for the market
  from read 6.

**`offer-prize`** (conditional)
- Purpose: what the prize is, its retail value, winners, what is included,
  substitution policy.
- Media: yes when the prize is physical. Jobs `packaging` or
  `included-items` (flat lay of everything the winner receives). Catalog
  media, then library tag `product-shot` or `flat-lay`, then merchant or
  partner upload with licence; view with `lexsis_assets.view` and confirm
  every item shown is something the winner receives. Gap: ask the merchant
  (flat lay of the
  contents, square, one image); never generated, nothing shown that does not
  ship (GN13); running the section as a text list under the form is the
  merchant's call. No-go: a gift-box render, a value badge inside the image, a
  duplicate of the hero image.
- Island: `none`.
- Copy: 60 words: value, number of winners, contents, substitution line.
- Decide with: the prize ledger row and the merchant's answer on the image.

**`how-it-works`** (conditional)
- Purpose: three steps with the entry window, draw date, notification and
  eligibility.
- Media: no. Dated facts, rendered as a numbered list or a two-column table
  beside the prize image, not as icon tiles (N3, N12).
- Island: `none`.
- Copy: one sentence per step with the datetime and timezone written out.
- Decide with: the offer ledger rows for open, close and draw.

**`trust-bar`** or **`review-summary`** (recommended)
- Purpose: one verified proof line.
- Media: no.
- Island: `none`; a `review-summary` is a text line with average and count
  from `lexsis_catalog.reviews`.
- Copy: one line: the frequency and opt-out fact, or "over N subscribers,
  as of <month>", or the average and count.
- Decide with: the proof ledger; when only the policy fact is verified, the
  policy fact is the whole module.

**`legal-terms`**
- Purpose: rules, sponsor, eligibility, free entry method, privacy, opt-out,
  directly under the form.
- Media: no. Island: `none`.
- Copy: links and one-line facts; a single plain text link to the store is
  allowed here for visitors who would rather buy.
- Decide with: counsel-confirmed rules per market from read 6.

**`countdown`** (conditional)
- Purpose: count to the verified entry close.
- Media: no.
- Island: `CountdownTimer` bound to the ledger's ISO end datetime with
  timezone, hidden after it (DP1); resolve style from
  `lexsis_design.island_schema`. No per-session or resetting timer.
- Copy: the close date written in text beside the timer.
- Decide with: an offer ledger `endsAt` row marked verified; no row, no
  section.

### Asset budget
| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | the prize or product `identity` packshot | `packaging` or included-items flat lay for a gift; any image for a non-catalog prize (trip, gift card, guide) | reuse the hero packshot in the prize section only if it is a different crop; ask the merchant or partner to upload a licensed photo; gift card or guide: the real file or a typographic hero on the merchant's call; never a drawn prize |
| asset library | a prior packshot or hero of the same product | a lifestyle prize photo | ask the merchant to upload; `hero_bg` backdrop generation behind a real cut-out is the only generated option; drop the second image only if they choose |
| generation | backdrops only (`hero_bg` behind a real cut-out) | product, prize, people, gift art, badges, text | never |

With minimal assets the page is a packshot hero from catalog media, the form
with its consent text, the frequency fact and the terms block; a lead magnet
with no physical prize is typographic. Generated assets on this type are zero
or one backdrop; the house cap is four per page. Every asset placed, generated ones included, was
opened with `lexsis_assets.view` and passed the fit review before use.

## Above the fold (390px)

In order: logo (not clickable); headline with the incentive and value;
one-line reason to receive messages; the prize or product image; the form
field and button; the consent checkbox with its full text; one privacy or
proof line. The whole form, including the consent text and the button, is
visible without scrolling on a 390 by 844 screen.

Must not appear: navigation, a product price, a second CTA, a countdown
without a ledger row, a popup of any kind, a pre-ticked box, "spam-free"
promises in place of the actual frequency.

## Proof

One or two modules. `policy-fact` is required and is usually the minimum
module: the message frequency and opt-out fact stated as the store's own
policy. Optional second module: `customer-count` (subscriber count from a
platform export, rounded down, "over N", dated), `review-summary` (store
average and count), or named past winners with consent. Nothing else. A
giveaway page that stacks review carousels is selling the wrong thing.
When the store has none of these, the privacy fact alone is the proof
section (`references/proof/reviews-sourcing.md`, Tier 5).

## Offer and CTA

Exactly one CTA: the form button, in the hero. No sticky bar, no secondary
"or shop bestsellers" button; a plain text link to the store in `legal` is
acceptable for visitors who would rather buy. Copy pattern: claim-offer
("Send my 10% code", "Enter the giveaway", "Send the guide"); the button
names the delivery, never "Submit" or "Sign up".

Incentive rules:

- State the exact value and mechanism: "10% off your first order. Code
  arrives by email within a minute." Discount popups converted 7.45%
  against 4.60% without an incentive (OPERATOR, Wisepops via Klaviyo,
  https://www.klaviyo.com/blog/ecommerce-email-popup).
- One field: single-field forms converted 4.30% against 2.61% to 3.45% for
  multi-field (OPERATOR, Wisepops via Klaviyo, same URL). Ask for email and
  phone in two steps, email first.
- Dedicated capture pages opt in at roughly 6 to 7% against 3 to 5% for
  popups (OPERATOR, Opensend,
  https://www.opensend.com/post/email-opt-in-rate-statistics-ecommerce).
- Giveaway entrants convert to buyers less than discount subscribers; tag
  them separately so later flows do not treat them as buyers (OPERATOR,
  Klaviyo, https://www.klaviyo.com/blog/sign-up-form-best-practices).
- Gamified entry (spin-to-win) is allowed only with real odds, every prize
  honoured, no fake spin delay and no "you almost won" (LAW, dark patterns;
  OPERATOR, Klaviyo, https://www.klaviyo.com/blog/spin-to-win-opt-in-forms).
- Offers that fit: `none`, `first-order`; `gwp`, `free-shipping`,
  `referral` (bonus entries), `trial-sample`, `gift-card` (as the prize) and
  `charity` only when the merchant confirms terms. Offers that do not fit:
  `percent-off` and `fixed-off` as sitewide sales, `bogo`, `flash-sale`,
  `clearance`, `subscribe-save`, `bnpl`, `mystery`.
- The code is never printed on the page; it arrives in the first message,
  which is what makes the consent worth something.

Consent language (LAW), written in full beside the checkbox and matching
the registered template where one exists:

- US SMS (TCPA): prior express written consent by an affirmative act;
  disclosure names the business, purpose, message frequency, "Msg & data
  rates may apply", STOP and HELP instructions, links to terms and privacy;
  consent is specific to this seller. The FCC one-to-one consent rule was
  litigated in 2025; write seller-specific consent regardless and verify
  the current status before relying on any shared-consent flow
  (https://www.moengage.com/blog/new-tcpa-rules/).
- India SMS (TRAI TCCCPR 2018 as amended February 2025): the brand is a
  registered Principal Entity on DLT with registered headers, content
  templates and a consent template; the checkbox text on the page must match
  the registered consent template; promotional SMS only 9 am to 9 pm IST;
  every message carries an opt-out honoured within 7 days
  (https://www.trai.gov.in/sites/default/files/2025-02/Regulation_12022025.pdf,
  https://www.techtonetworks.com/post/sms-consent-templates-in-india).
- India data (DPDP Act 2023): consent is free, specific, informed,
  unconditional and unambiguous, given by clear affirmative action for a
  stated purpose, and as easy to withdraw as to give
  (https://www.meity.gov.in/content/digital-personal-data-protection-act-2023).
- EU and UK (GDPR, PECR): no pre-ticked boxes (CJEU Planet49, C-673/17,
  https://curia.europa.eu/juris/liste.jsf?num=C-673/17; Recital 32,
  https://gdpr-info.eu/recitals/no-32/); separate consent for email and SMS;
  double opt-in required for Germany and enabled for all EU traffic.
- Sweepstakes: official rules exist and are linked; a free entry method is
  offered where consideration would make the promotion a lottery; the
  merchant's counsel confirms the rules for each market before publish.

Popup and overlay rules on this page and on any page that links here
(`references/island-patterns.md`, Modal exit-intent; LAW and OPERATOR,
https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials,
https://wisepops.com/blog/popup-stats):

- No entry popup: the form is the page. Any marketing overlay anywhere in
  the store waits for at least 10 seconds and 30% scroll, and never shows
  while a paid landing hero is in view.
- Exit intent only as a Modal, once per session, remembered 7 days after
  dismissal and 30 days after conversion, never on the page where the
  visitor just converted; on mobile use scroll-up or back intent, and cap
  the sheet at 60% of viewport height.
- Close control at least 44 px, top right or a visible "No thanks" of equal
  weight; Esc and backdrop close; no confirmshaming decline copy.
- No full-page interstitial on mobile entry from search or ads.

## Imagery

Required job: `identity` of the prize or the product the code applies to,
as a `packshot`; `product-in-context` is the alternative when the incentive
is a lifestyle prize. Minimum one image, maximum two; no gallery, no
carousel (HEURISTIC, `references/assets/image-jobs-by-page-type.md`).
`packaging` is recommended for a physical gift. `typographic` hero only when
there is no physical prize. Video optional and only a short clip that shows
the prize; never autoplay with sound. Slots the plan must create: one hero
prize or product image; one optional secondary image for the prize section.

## Copy

Framework: PAS for lead magnets (name the problem the guide solves, then
the offer); AIDA compressed to headline, one sentence, form for discounts
and giveaways. Headline pattern: incentive plus exact value plus who it is
for ("Win a year of coffee. Two winners, drawn 30 Sept."); never "Join our
newsletter". Reading level grade 6. Ceilings: headline 10 words, subhead
20 words, whole page 80 to 250 words excluding the terms block. Consent
copy is written in the brand's voice but never shortened below what the law
requires; frequency is a number ("about one message a week"). Email and
SMS copy are not identical. Copy rules in `references/copy/copy-frameworks.md`.

## Never

- Never more than three fields; never more than one on cold paid traffic.
- Never pre-tick or bundle consent; email and SMS are separate unticked
  boxes.
- Never show the discount code on the page.
- Never show a countdown without a verified entry-close datetime.
- Never trigger a popup on this page; the form is the page.
- Never write a decline label that shames ("No, I like paying full price").
- Never run a giveaway without linked official rules, sponsor, eligibility,
  draw date and winner notification method visible on the page.
- Never state a subscriber count or winner without a ledger row.
- Never place navigation, a product grid or a second CTA on the page.
- Never treat giveaway entrants as buyers in later flows; tag the source.

## Examples

- Jones Road Beauty quiz landing,
  https://www.jonesroadbeauty.com/pages/quiz-landing: capture via a routing
  quiz, one action above the fold, no navigation; shows where the boundary
  with `quiz-funnel` sits (answers change the result).
- Klaviyo sign-up form guidance with the MERIT Beauty example (product image
  plus "ships free" as the incentive, single field),
  https://www.klaviyo.com/blog/sign-up-form-best-practices.
- Wisepops popup benchmark set (timing, field count, incentive effects) used
  to set the rules above, https://wisepops.com/blog/popup-stats. Giveaway
  pages are short-lived, so documented patterns stand in for live URLs.

## Checklist

```json
{
  "page_type": "lead-capture-giveaway",
  "aliases": ["opt-in page", "squeeze page", "giveaway page", "contest page", "sweepstakes page", "discount-for-email page", "lead magnet page"],
  "funnel_stage": ["tof"],
  "awareness": ["unaware", "problem-aware"],
  "traffic": ["meta", "tiktok", "influencer", "affiliate"],
  "sections": { "min": 3, "max": 6 },
  "mandatory_sections": ["hero", ["giveaway-entry", "email-capture", "sms-capture"], "legal"],
  "recommended_sections": ["offer", "how-it-works", ["trust-bar", "review-summary"]],
  "forbidden_sections": ["header", "buy-box", "product-grid", "sticky-cta", "quiz", "cross-sell", "pricing", "offer-bridge"],
  "nav": "none",
  "price_above_fold": "forbidden",
  "cta": { "min": 1, "max": 1, "first_after_section": 0, "sticky": "forbidden", "copy_pattern": "claim-offer" },
  "proof": { "min_modules": 1, "max_modules": 2, "required_kinds": ["policy-fact"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked", "stock-count"] },
  "imagery": { "required_jobs": ["identity"], "hero": "packshot", "video": "optional", "min_images": 1 },
  "copy_framework": ["pas", "aida"],
  "offer_compat": { "allowed": ["none", "first-order", "gwp", "free-shipping", "referral", "trial-sample", "gift-card", "charity"], "forbidden": ["percent-off", "fixed-off", "bogo", "flash-sale", "clearance", "subscribe-save", "bnpl", "mystery"] },
  "urgency": "verified-only"
}
```

## Sources

- Klaviyo sign-up form best practices: https://www.klaviyo.com/blog/sign-up-form-best-practices
- Klaviyo ecommerce email popup benchmarks (Wisepops data): https://www.klaviyo.com/blog/ecommerce-email-popup
- Klaviyo spin-to-win forms: https://www.klaviyo.com/blog/spin-to-win-opt-in-forms
- Wisepops popup statistics: https://wisepops.com/blog/popup-stats
- Opensend opt-in rate statistics: https://www.opensend.com/post/email-opt-in-rate-statistics-ecommerce
- Google, avoid intrusive interstitials: https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials
- TCPA consent rules summary: https://www.moengage.com/blog/new-tcpa-rules/
- TRAI TCCCPR amendment, February 2025: https://www.trai.gov.in/sites/default/files/2025-02/Regulation_12022025.pdf
- India DLT consent templates: https://www.techtonetworks.com/post/sms-consent-templates-in-india
- Digital Personal Data Protection Act 2023: https://www.meity.gov.in/content/digital-personal-data-protection-act-2023
- CJEU Planet49 (pre-ticked consent): https://curia.europa.eu/juris/liste.jsf?num=C-673/17
- GDPR Recital 32: https://gdpr-info.eu/recitals/no-32/
- Jones Road quiz landing: https://www.jonesroadbeauty.com/pages/quiz-landing
- Research notes: internal research audit (2026-09-10) block 25; internal research audit (2026-09-10) sections 10 and 11; `references/conversion-psychology.md` Recipe 1.

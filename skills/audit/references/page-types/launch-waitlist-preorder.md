# Launch, waitlist and pre-order

A page for a product that cannot ship yet. Before launch it captures intent
with a one-field waitlist; at launch it takes pre-orders or first orders
against a stated ship date; in launch week it keeps selling without review
data. Visitors arrive from teaser ads, the existing list, PR and creator
seeding, problem- to product-aware but with no way to verify the product from
other buyers. The page must state the date, the price basis and the terms,
and substitute founder credibility, test data and a roadmap for the reviews
it cannot have. Once the product has shipped and holds review data, it stops
being this type and becomes `pdp` or `restock` (index tie-break).

## Identify it

Signals in the brief: "launch", "coming soon", "drop", "pre-order",
"reserve", "early access", "waitlist"; a launch date or window; the product
is not yet shippable; a wish to validate demand or fund production.

Near neighbours:

- `restock`: the product sold before and has reviews; use it.
- `lead-capture-giveaway`: an incentive or contest for an email; a waitlist
  is for a product the visitor wants, not a prize.
- `pdp-hybrid-landing`: the product is live and buyable with reviews; a
  launch-day page with no waitlist window and no pre-order terms downgrades
  to it (campaign-calendar CC2).
- `ugc-creator-collab`: a collab drop where the creator's content is the
  proof; that type carries the paid-partnership disclosure.

## Variants

- **Pre-launch waitlist** (4 to 8 weeks out). `waitlist-form` in the hero,
  one field, launch window stated, what joining earns (first access, launch
  price, founder tier), referral loop, teaser visuals, FAQ. 6 to 7 sections,
  150 to 400 words. OPERATOR: waitlist pages typically convert 2%, the best
  about 20%, with referral loops the single biggest lever
  (https://leadpages.com/blog/the-launch-page-sequence-before-during-after-launch).
- **Launch or pre-order live** (from launch day). `buy-box` labelled
  "Pre-order" with estimated ship-by date, charge timing (deposit, full,
  or at ship), cancellation and refund terms, all within one scroll of the
  CTA; roadmap timeline; early-tester quotes with disclosed connection. 8
  to 9 sections, 500 to 900 words. OPERATOR: 10 to 20% pre-order conversion
  from a warm list is strong
  (https://preorder.page/how-to-build-a-preorder-waitlist-that-actually-converts-ince).
- **Post-launch week** (shipping started, no reviews yet). Same anatomy as
  launch with the ship-by replaced by a dispatch estimate and first
  verified customer media as it arrives; retype to `pdp` when 5 or more
  reviews exist.

## Anatomy

Sections between chrome: 6 to 9.

1. `header` (mandatory). Minimal: logo plus one utility link (account or
   help); no category navigation on a launch page.
2. `hero` (mandatory). One-line value proposition, the launch date or
   window, and the primary action: the `waitlist-form` (pre-launch) or the
   `buy-box` (pre-order). Price shown only when final; "from $X" only if it
   will be true.
3. `waitlist-form` (conditional: pre-launch variant; then mandatory). One
   field (email or phone, not both), consent unchecked, what happens next
   in one line. In the hero or directly below it.
4. `buy-box` (conditional: pre-order live; then mandatory). "Pre-order"
   label, "Estimated to ship by [date]" beside the price and beside the
   button, deposit and full price shown separately without striking the
   full price against the deposit, cancellation and refund line. LAW:
   Shopify pre-order requirements mirror the FTC Mail Order Rule, a
   reasonable basis for the ship date, 30 days if none is stated, revised
   date plus cancel or refund right on delay
   (https://help.shopify.com/en/manual/products/purchase-options/pre-orders/setup ;
   https://www.ftc.gov/business-guidance/resources/business-guide-ftcs-mail-internet-or-telephone-order-merchandise-rule ;
   https://shopify.dev/docs/storefronts/themes/pricing-payments/preorder-tbyb/preorder-tbyb-ux-guidelines).
5. `offer` (recommended). What early action earns: launch price versus the
   confirmed public price, founder tier, GWP; a future-price comparison is
   fair only if the price actually rises afterwards (LAW: UK CTSI pricing
   guidance, https://www.businesscompanion.info/en/guidance-for-traders-on-pricing-practices).
6. `benefits` (recommended). Three to five "why reserve early" or
   "what it does" bullets with a number, material or test in each.
7. `founder-note` (mandatory). Named founder with title and photo, why the
   product exists, signed. Observed at the commitment point on Klassy Pet
   (internal teardown audit, 2026-09-10).
8. `specs` (recommended; conditional: prototype test data exists). What was
   tested, on how many units, when, with what result; a document or URL in
   the proof ledger.
9. `how-it-works` roadmap (recommended; mandatory in the pre-order variant).
   Development timeline (design, tooling, production, ship) with status and
   a plain-English "what this means" line per stage, and the launch
   schedule with the public price and its date. Observed: 3 of 3 launch
   teardowns carry a roadmap or launch schedule.
10. `testimonial-spotlight` (conditional: named early testers with written
    approval and their connection disclosed, "In-home tester", "Early
    access partner"). Two quotes, never styled as customer reviews.
11. `referral-form` (recommended in pre-launch). "Refer two friends, move up
    the list"; the mechanic stated exactly.
12. `press-marquee` or `expert-endorsement` (conditional: verified, linked).
13. `countdown` (conditional: a merchant-confirmed drop datetime in the
    offer ledger; final 48 hours only). Bound to `endsAt`; disappears at
    zero.
14. `stock-indicator` (conditional: a real edition size read live). "Edition
    of 500, 212 reserved" from a live binding.
15. `faq` (mandatory). When it ships, what the price will be, how and when
    the card is charged, how to cancel, what happens on delay, why the
    deposit or the lower price. Observed on 1 of 1 full launch teardown.
16. `closing-cta` (recommended). Repeat of the form or the pre-order button
    with the ship-by line.
17. `sticky-cta` (conditional: pre-order variant). Label carries the action
    and date: "Pre-order, ships by Nov 12".
18. `footer` (mandatory). Legal entity, contact, refund policy link.

## Workflow

Apply `references/workflows/_how-to-read.md` to these type-specific
decisions. It links the shared asset/fallback, fit, live-island and
copy procedures; this table supplies their inputs, not another policy.

### Context reads

1. Merchant facts into the offer ledger before anything else: variant (pre-launch, pre-order live, post-launch week), launch date or window, estimated ship-by date and its basis, public price and launch price, charge timing (deposit, full, at ship), cancellation and refund terms, edition size and whether it is read live, drop datetime for a countdown (`references/offers/campaign-calendar.md`, `launch` row and CC7).
2. `lexsis_catalog.get` for the product: does real prototype or production media exist (footnote f in `references/assets/image-jobs-by-page-type.md`); price; a pre-order purchase option or selling plan; inventory tracking. No pre-order option in Shopify means no buy box: the page runs the waitlist variant.
3. `lexsis_capture.form_schemas` for the one-field waitlist form and its consent text; the referral mechanic if the form supports one.
4. Founder facts: full name, title, the photo the merchant approves in writing, the note text; test data documents (method, units, date); roadmap stages with status (`references/proof/proof-ledger.md` rows). `lexsis_brand.brand_kit` for tokens, voice and banned phrases; `lexsis_brand.context` for the `theme_id`; `lexsis_brand.navigation` only for the one utility link.
5. When teaser ads run, read the supplied campaign message and frame: the hero must match them (`references/copy/message-match.md`).
6. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`, one call each for `product-shot`, `hero`, `lifestyle`, `logo`, `social-proof`; then semantic "<product> prototype" and "<founder name>" with `lexsis_assets.view`. Press rows fetched and verified per `references/proof/press-and-media-mentions.md`.
7. `lexsis_catalog.reviews_status` is read only to confirm the count is zero for this product; nothing review-shaped is planned (`references/proof/reviews-sourcing.md`, zero-review playbook).
8. `lexsis_design.islands` for the active catalog; `lexsis_workspace.credits` is read; generation here is limited to a `hero_bg` behind a typographic hero at most (`references/assets/generation-policy.md`, GN2).

### Section by section

| Section | Purpose | Media job and source | Interactive decision | Copy constraints | Decision evidence |
|---|---|---|---|---|---|
| `header` | logo plus one utility link; no category navigation. | logo from the brand kit; a text wordmark when none. | SiteHeader in its minimal treatment (not sticky, one link, cart hidden pre-launch, CTA to the form or buy box). | one link label. | the variant. |
| `hero` | one-line value proposition, the date or window, and the primary action inline. | job `identity` packshot of the real prototype or production unit when it exists (catalog media, then library `product-shot`, then merchant upload; ad-matched frame when creatives exist), treatment `packshot`. Otherwise `typographic` with no product slot. Generation: `hero_bg` behind the type only; never a product render (GN2); a merchant's own render only captioned "Rendering; final packaging may vary". Missing media: (a real prototype photo, 4:5 and 16:9, one image) and; the page ships typographic in the meantime and the plan records it. No-go: stars, a review count, a discount pill, "coming soon" without a date. | none for the image (static `<picture>`); HeroMedia only when a real photo is the full-bleed bold moment, image mode, autoplay off | H1 10 words or fewer stating the outcome; subhead names the date or window and who it is for. | `lexsis_catalog.get` media count viewed; the ledger date row. |
| `waitlist-form` (conditional: pre-launch; then mandatory) | one field, consent unchecked, what happens next in one line. | the prototype identity image beside the form when one exists; otherwise the form alone is the object (N8). | EmailCapture, one per page; decide the incentive line from a `gwp` or `price-lock` ledger row; consent text is HTML beside the form naming brand, purpose and frequency | one line after the button; pattern `join-waitlist`. | `lexsis_capture.form_schemas` (one field, email or phone). |
| `buy-box` (conditional: pre-order live; then mandatory) | "Pre-order" with the ship-by date, price basis and terms within one scroll. | yes; job `identity` of the real unit beside the box from catalog media. Missing means no pre-order page: run the waitlist variant until a real photo arrives. | BuyBox; decide the compact or default treatment from the variant count; ship-by, charge timing and refund line as HTML under the button; public price and launch price as separate text, never a strike-through against a deposit (`references/offers/price-presentation.md`). | "Estimated to ship by <date>", "We charge when it ships" or the deposit amount, "Cancel any time before dispatch for a full refund". | the Shopify pre-order option in `lexsis_catalog.get` and the ledger terms rows. |
| `offer` (recommended) | what early action earns. | a `gwp` wants the gift's `identity` image from catalog media; a `price-lock` or founder tier is text and merges into the hero price block rather than standing alone. Missing gift image:; if skipped, the offer is a line in the price block. | none. | one sentence; a future-price comparison only when the price will rise on the stated date. | the offer-ledger row and the gift's image. |
| `benefits` (recommended) | three to five bullets each with a number, material or test. | yes; one real prototype photo per bullet (`detail`, `scale`, `in-use` with the prototype) from merchant upload or library, or one authored inline SVG `diagram` anchoring the list. Generation: none (GP14). Missing media: (one photo per bullet, 4:5, count) and; if skipped, the three strongest facts fold into the hero subhead and the section leaves. view the benefit images together so lighting, backgrounds and crops agree. | none. | bullets 15 words each, one fact per bullet. | count of viewed prototype photos. |
| `founder-note` | named founder with title and photo, why the product exists, signed. | yes; job `founder-or-team`, real photo (4:5, in context) from library `lifestyle` or merchant upload with written approval in the ledger; never stock or generated (GN3). Missing media: (a real photo of the founder, 4:5, one image) ; the signed text stands on its own in the meantime (allowed by the asset workflow) and plan approval waits for the photo. | none. | first person, under 120 words, name and title as the signature. | the `founder-note` ledger row (approval recorded). |
| `specs` (conditional: prototype test data exists) | what was tested, on how many units, when, with what result. | an HTML facts table is the object; a real photo of the test rig or the merchant's document photo may sit beside it; an authored inline SVG `diagram` for a measured curve. Generation: never a lab, chart or result image (GN4). Missing photo: the table stands alone; the merchant is told a rig photo could be uploaded. | none. | numbers copied exactly from the `test-data` ledger row; method and date in one line. | the document or URL in the ledger. |
| `how-it-works` roadmap (recommended; mandatory for pre-order) | design, tooling, production, ship with status and a plain "what this means" line per stage; the launch schedule with the public price date. | yes; job `diagram` as an authored inline SVG timeline with every label and date in HTML text, plus real `sequence` photos of the process (tooling, factory, samples) from merchant upload where they exist. Generation: none. Missing process photos:; the SVG timeline carries the section meanwhile; never icon tiles per stage. | none. | one noun phrase and one "this means" sentence per stage. | the roadmap stages the merchant confirmed. |
| `testimonial-spotlight` (conditional: named early testers with written | two quotes styled as tester quotes, never as customer reviews. | quotes are the artefact; real photos only with consent; never generated people. | none; static blockquotes with the connection line ("In-home tester"). ReviewCarousel is not used: these are not reviews. | verbatim, two quotes, 60 words each. | `expert-quote` ledger rows. |
| `referral-form` (recommended in pre-launch) | "Refer two friends, move up the list", stated exactly. | no. | none; the mechanic is text with the post-signup share link from the capture form's schema; a second EmailCapture is not mounted. | the mechanic in one sentence. | `lexsis_capture.form_schemas` exposing a referral link. |
| `press-marquee` or `expert-endorsement` (conditional: verified, | three to six linked editorial logos, or one expert quote with a credential line. | outlet SVGs from library `logo`, each linked (`references/proof/press-and-media-mentions.md`); the expert's real photo only with consent. Generation: never (GN5). Missing logo files: ask the merchant; fewer than three rows renders quotes. | none; a static linked row (the Marquee island is deprecated). | caption "In the press"; credential line under the quote. | count of `verified` press rows. |
| `countdown` (conditional: ledger `endsAt`, final 48 hours only) | the drop time. | no. | CountdownTimer (the Countdown island is deprecated) bound to the ledger `endsAt`, with the expired state naming what is live next | one line naming what happens at zero. | the ledger row and the current time being inside 48 hours (`references/offers/urgency-scarcity.md`). |
| `stock-indicator` (conditional: a real edition size read live) | "Edition of 500, 212 reserved". | no. | InventoryIndicator only when the edition is tracked as live inventory on a buyable product; the island's own guidance excludes pre-order and made-to-order items, so the reserved count on a pre-order page is an HTML line bound to a live orders query (`sales-count` ledger row) or it is omitted. | one line, numbers from the live read, rounded down. | inventory tracking in `lexsis_catalog.get` and the ledger. |
| `faq` | ship date, price, charge timing, cancellation, delay handling, why the deposit. | no. | none; native `<details>` and `<summary>`. | five to seven questions, the fact first, 60 words each. | the ledger terms rows. |
| `closing-cta` (recommended) | the action repeated with the ship-by line. | the real product image again when one exists; otherwise the button and line alone. | none; an anchor button to the hero form or buy box (a second EmailCapture or BuyBox is not mounted). | the CTA label plus "Estimated to ship by <date>". | the variant. |
| `sticky-cta` (conditional: pre-order variant) | keep the pre-order action available below the fold. | the product image inside the bar from catalog media. | StickyBar in product mode, appearing after the hero; decide from page length in 390px screens. | the label carries the action and the date. | the variant and the BuyBox being present. |
| `footer` | legal entity, contact, refund policy link. | logo only. | Footer with links from `lexsis_brand.navigation`. | Use the shared procedure. | the navigation result. |

### Asset budget

| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | a prototype or production packshot when the product is set up | `detail`, `scale`, `in-use` with the prototype, `packaging` | ask the merchant to upload prototype photos ("needs a real photo"); typographic hero and no product slot meanwhile; `benefits` leaves only on the merchant's call |
| asset library | `logo` SVGs for press, sometimes a founder portrait | the founder photo with approval, process photos for the roadmap | ask the merchant to upload with written approval; the authored SVG timeline carries the roadmap; nothing is generated in their place |
| generation | backdrops, textures, composites only | product, people, results, logos, text | never; `hero_bg` (ALLOW) behind a typographic hero is the only feasible purpose, and `product_composite` needs a real cut-out a pre-launch product usually lacks |

With minimal assets the page is a minimal header, a typographic hero with the one-field form, a signed founder note, an authored SVG roadmap, an FAQ and a footer; at most one generated asset (`hero_bg`), never more than four per page, and every missing photo (prototype, founder, process) listed in the plan and the draft summary with upload or skip.

## Above the fold (390px)

Pre-launch: compact header; one-line value proposition; launch window; the
one-field form with its button; one line on what joining earns. Nothing
else. Pre-order: header; value proposition; price block with public price
and pre-order price stated separately; "Estimated to ship by [date]";
deposit or charge timing; the pre-order button; refund line under it.
Observed recipe: outcome H1, future versus launch price, deposit mechanic,
capture (internal teardown audit, 2026-09-10).

Must not appear: stars or a rating, a review count, a multi-field form, a
countdown more than 48 hours out, "coming soon" with no date, a discount
pill, a popup.

## Proof

Modules: 1 to 3. Not-yet-buyable rule: a product with no shipped units has
no reviews, so nothing review-shaped is rendered (LAW: FTC 16 CFR 465 and
design-rules N11; `references/proof/reviews-sourcing.md` zero-review
playbook).

- `founder-note` (required): real name, title, photo, written approval.
- `test-data` (recommended): prototype or lab results with method, sample
  size and date; numbers copied exactly.
- `customer-count` as a waitlist count (conditional: live read from the ESP,
  rounded down, "over 2,300 waiting").
- `sales-count` of pre-orders placed (conditional: live orders query).
- `expert-quote` or `press-quote-linked` (conditional: verified and linked;
  no wire releases).
- Early-tester quotes as `expert-quote` rows with the connection disclosed;
  never as `review-quote`.
- Never: `review-summary`, `review-quote`, `review-list`,
  `review-with-media`, `repeat-rate`, `social-proof-popup`,
  `live-viewer-count`, `press-logo-unlinked`, "limited run" for a product
  that restocks quarterly.

## Offer and CTA

- CTAs: one on a waitlist page (the form, repeated once at the end at
  most); two on a pre-order page (buy box and closing, plus the optional
  sticky). Pattern `join-waitlist` ("Join the waitlist", "Reserve my
  spot"); the pre-order variant uses verb plus object with the date
  ("Pre-order, ships by Nov 12").
- First CTA in the hero. Sticky optional, pre-order only.
- Price reveal: pre-launch only when final; pre-order in the hero with the
  public price and its start date as text, never a strike-through of the
  full price against a deposit.
- Terms within one scroll of the CTA: ship date, charge timing,
  cancellation, refund, delay handling (`references/offers/offer-ledger.md`
  rule 4).
- Urgency: verified only. A real drop time or a real edition size read live;
  no fake "limited".
- Offer types that fit: `none` (full price at launch), `pre-order-price`,
  `price-lock`, `gwp` for the waitlist, `limited-edition` with a real size,
  `loyalty` early access, `referral` loop, `free-shipping`, `bnpl` on the
  full price, `bundle` launch set, `cashback` for India.
- Offer types that do not fit: `percent-off`, `fixed-off`, `bogo`,
  `flash-sale`, `clearance`, `subscribe-save`, `tiered-volume`,
  `bundle-decoy`, `mystery`, `trial-sample`, `student-military`,
  `first-order`. OPERATOR: a launch discount sets the anchor low forever;
  use early access, GWP or price-lock instead (campaign-calendar CC7;
  https://commonthreadco.com/blogs/ecommerce-playbook/how-to-craft-the-best-bfcm-offer-this-year).
- Deposits: refundable micro-deposits work as commitment devices (Klassy Pet
  $3, fully refundable); state refundability beside the button.

## Imagery

Required job: `founder-or-team` (real, named). `identity` is required when
real prototype or production media exists; when it does not, the hero is
typographic and no product slot is created (matrix footnote f,
`references/assets/image-jobs-by-page-type.md`). Recommended: `detail`,
`scale`, `in-use` with a prototype, `ingredient-or-material`, `packaging`,
`diagram` for the roadmap (numbers in HTML).

Hero treatment: `packshot` of the prototype or production unit on a plain
background when real media exists; otherwise `typographic`. Never a
generated product image standing in for an unshipped product. Video
optional: a short teaser or prototype demo with a poster. Three to six assets
before launch; minimum 3 image slots.

## Copy

Framework: AIDA for a cold teaser (curiosity headline, then the mechanism),
BAB for the product story; direct offer language for pre-order to a warm
list.

- H1 10 words or fewer stating the outcome, not "coming soon".
- Subhead names the date or window and who it is for.
- Form microcopy: what happens after joining, in one line; consent text
  names brand, purpose and frequency.
- Roadmap stages: one noun phrase plus one "this means" sentence each.
- FAQ answers start with the fact (date, amount, yes or no).
- Reading level grade 6 to 8; "you" outnumbers the brand name.
- Vocabulary: "estimated to ship by", "fully refundable", "we charge when it
  ships"; never "guaranteed", "revolutionary", "the future of".

## Never

- Never show reviews, stars, a rating or a review count for a product that
  has not shipped.
- Never ask for more than one field on a waitlist form.
- Never publish "coming soon" without a date or window and a stated benefit.
- Never run a pre-order without an explicit ship-by date and refund and
  cancellation terms within one scroll of the button.
- Never strike the full price against a deposit.
- Never call a run "limited" when it restocks.
- Never show a countdown more than 48 hours before the drop or without a
  ledger `endsAt`.
- Never charge the card months before shipping without saying so beside the
  button.
- Never invent a waitlist count; read it live and round down.
- Never keep this type once 5 or more verified reviews exist; retype to
  `pdp` or `restock`.
- Never let a launch page carry a percent-off.

## Examples

- Klassy Pet VIP reservation,
  https://klassypet.com/products/klassy-vip-reservation: outcome headline,
  public price versus launch price, $3 refundable deposit, founder note with
  name and title, early-tester quotes with roles, development timeline with
  "what this means" lines, launch schedule, FAQ explaining the fee and the
  lower price. Weak on product imagery.
- Weighted Hoodie early access, https://www.weightedhoodie.com/: colourway
  preview and a quarter-dated roadmap on the capture page.
- Rize pouches launch, https://getrizepouches.com/: a stated edition size
  per flavour ("150 tins per flavor") as the scarcity basis; verify the
  count is live before copying the pattern.

## Checklist

```json
{
  "page_type": "launch-waitlist-preorder",
  "aliases": ["coming soon page", "waitlist page", "early access page", "pre-launch page", "pre-order page", "drop page", "launch hub"],
  "funnel_stage": ["tof", "mof"],
  "awareness": ["problem-aware", "solution-aware"],
  "traffic": ["email", "meta", "organic", "influencer"],
  "sections": { "min": 6, "max": 9 },
  "mandatory_sections": ["header", "hero", ["waitlist-form", "buy-box"], "founder-note", "faq", "footer"],
  "recommended_sections": ["offer", "benefits", "how-it-works", "specs", "referral-form", "closing-cta"],
  "forbidden_sections": ["reviews", "review-summary", "ugc-grid", "video-testimonials", "before-after", "product-grid", "dateline", "hook", "agitation", "offer-bridge", "quantity-breaks", "subscription-toggle"],
  "nav": "minimal",
  "price_above_fold": "optional",
  "cta": { "min": 1, "max": 2, "first_after_section": 0, "sticky": "optional", "copy_pattern": "join-waitlist" },
  "proof": { "min_modules": 1, "max_modules": 3, "required_kinds": ["founder-note"], "forbidden_kinds": ["review-summary", "review-quote", "review-list", "review-with-media", "repeat-rate", "social-proof-popup", "live-viewer-count", "press-logo-unlinked"] },
  "imagery": { "required_jobs": ["founder-or-team"], "hero": "packshot", "video": "optional", "min_images": 3 },
  "copy_framework": ["aida", "bab"],
  "offer_compat": { "allowed": ["none", "pre-order-price", "price-lock", "gwp", "limited-edition", "loyalty", "referral", "free-shipping", "bnpl", "bundle", "cashback"], "forbidden": ["percent-off", "fixed-off", "bogo", "flash-sale", "clearance", "subscribe-save", "tiered-volume", "bundle-decoy", "mystery", "trial-sample", "student-military", "first-order"] },
  "urgency": "verified-only"
}
```

## Sources

- internal research audit (2026-09-10) section 5 block 11; section 2 row 11.
- internal research audit (2026-09-10) teardown 37, partials (Weighted Hoodie, Rize) and Part D.
- internal research audit (2026-09-10) sections 1.16, 4.1, 7.
- internal research audit (2026-09-10) sections 4, 13 (zero-review row).
- internal research audit (2026-09-10) section 10 (form rules).
- `references/offers/campaign-calendar.md` CC2, CC7; `references/proof/reviews-sourcing.md`; `references/assets/image-jobs-by-page-type.md` footnote f.
- Leadpages launch sequence: https://leadpages.com/blog/the-launch-page-sequence-before-during-after-launch
- preorder.page waitlist and anatomy: https://preorder.page/how-to-build-a-preorder-waitlist-that-actually-converts-ince ; https://preorder.page/the-anatomy-of-a-high-converting-preorder-page-templates-cop
- PreProduct campaign guide: https://preproduct.io/how-to-run-a-pre-order-campaign-complete-guide-for-ecommerce-brands/
- Threshline waitlist: https://threshline.com/blog/build-pre-launch-waitlist/
- Shopify coming-soon pages: https://www.shopify.com/blog/coming-soon-page
- Shopify pre-order setup: https://help.shopify.com/en/manual/products/purchase-options/pre-orders/setup
- Shopify pre-order UX guidelines: https://shopify.dev/docs/storefronts/themes/pricing-payments/preorder-tbyb/preorder-tbyb-ux-guidelines
- FTC Mail Order Rule: https://www.ftc.gov/business-guidance/resources/business-guide-ftcs-mail-internet-or-telephone-order-merchandise-rule
- UK CTSI pricing practices: https://www.businesscompanion.info/en/guidance-for-traders-on-pricing-practices
- CTC on launch anchors: https://commonthreadco.com/blogs/ecommerce-playbook/how-to-craft-the-best-bfcm-offer-this-year

# Referral, loyalty and VIP programme page

The page explains a programme to people who already buy: how to earn, what
a point or a referral is worth, what the tiers unlock, and how to join or
share. The visitor is most-aware and arrives from an email, the account
page, a footer link or a post-purchase prompt. Their job is to join (or log
in) and, if the programme has referral, to share their link. The page is
short, table-driven and free of persuasion; its metrics are enrolment rate,
share-action rate and referred-friend conversion.

## Identify it

- The brief mentions "rewards", "points", "VIP", "tiers", "members",
  "refer a friend", "loyalty", "early access for members".
- Near neighbours: `thank-you-post-purchase` carries a referral module but
  is owned by the order confirmation. `offer-page` sells one promotion to
  everyone; a loyalty page sells continued membership. `brand-story-founder`
  sells belief; this page sells arithmetic. The referred friend's landing is
  an `offer-page` (`first-order` or the friend reward), not this page.

## Variants

- Referral only: two-sided reward, share tools, terms; no points.
- Points programme: earn table, redeem table, expiry, optional referral.
- Tiered VIP: points programme plus a tier table with thresholds and perks
  (access and service first, discounts last).

## Anatomy

1. `hero` mandatory: programme name, one-line benefit stated in currency or
   a concrete perk ("Earn 5 points per ₹100. 100 points is ₹100 off."), two
   states: guest sees "Join", member sees "Log in" or their balance.
2. `how-it-works` mandatory: three steps, earn then redeem then refer, one
   line each; passes a three-second read.
3. `benefits-earn` mandatory: ways-to-earn table generated from the
   programme configuration (create account, place an order, birthday,
   review with a photo, follow), each with its point value (satisfies
   `benefits`).
4. `offer-rewards` mandatory: redemption table with point cost and reward
   value, the conversion rule shown as arithmetic, expiry and exclusions on
   the same screen with a link to the full terms (satisfies `offer`).
5. `comparison-tiers` conditional: the programme has tiers; a table with
   threshold, qualifying period, perks per tier, and what happens on
   downgrade; perks lead with early access, exclusive drops and service, not
   deeper discounts (satisfies `comparison`).
6. `referral-form` mandatory: both sides of the reward in currency ("Give
   ₹500, get ₹500"), email share as the primary action, copy-link second,
   social third; states minimum spend and expiry for the friend's reward;
   uses the email capture form schema from `lexsis_capture.form_schemas`.
7. `faq` recommended: expiry, combining with codes, returns and refunded
   points, tier downgrade, who is eligible.
8. `closing-cta` recommended: repeat Join or Log in.

Terms travel with the value: the expiry and exclusion line sits inside
`offer-rewards` and `comparison-tiers`, and the footer `legal` links the
full terms page.

## Workflow

### Context reads
1. The programme configuration from the merchant (loyalty or referral app
   export, or the terms document): earn actions with point values, the
   redemption table with point cost and reward value, the conversion rule,
   expiry, exclusions, tier thresholds with qualifying period, perks per tier,
   downgrade rule, both sides of the referral reward in currency, the
   friend's minimum spend and expiry, early-access windows with start and end
   datetimes. Every value becomes an offer ledger row (`policy-fact`) before
   any table is written; interface-interference and preselection rules in
   `references/anti-patterns/dark-patterns.md` (DP5, DP10).
2. `lexsis_catalog.get` for any physical reward or member-only product:
   `identity` packshot at position one (viewed), price for the reward value
   line, availability so a sold-out reward is not listed
   (`references/assets/image-jobs-by-page-type.md`, type row: rewards
   identity optional).
3. `lexsis_brand.context` and `lexsis_brand.brand_kit` for `theme_id`, the
   programme name and voice, palette hexes; `lexsis_brand.navigation` for
   the full header and footer and the account or login URL that drives the
   guest and member states.
4. `lexsis_capture.form_schemas` for the referral share schema (the friend's
   email field, an optional advocate email field) and the join form when the
   programme app exposes one.
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`:
   `product-shot` for reward items; `lifestyle` only for a member event the
   merchant photographed; then semantic "<reward> packshot"; view with
   `lexsis_assets.view`. No people presented as members.
6. Proof: a member count export (rounded down, dated) or a member review
   that names the programme from `lexsis_catalog.reviews_search`; each a
   proof ledger row or it does not render. A new programme shows nothing.
7. `lexsis_design.islands`, then `lexsis_design.island_schema` for
   `EmailCapture` and `FunnelRuntime`; deprecated entries take their
   replacement per `references/workflows/island-selection-workflow.md`.

### Section by section
Media lines follow `references/workflows/section-asset-workflow.md` and
`references/assets/asset-sourcing-sequence.md`. When every step finds
nothing: tell the merchant what is missing (job, aspect, count), offer upload
via `lexsis_asset_upload.upload` or generation when the purpose is feasible
under `references/assets/generation-policy.md`, and skip or merge the section
only if the merchant chooses; in fast-draft, proceed with the closest
existing asset or leave the slot `planned` and list it in the plan and draft
summary. Island lines name the island and the decision inputs; variants and
props are resolved live from `lexsis_design.island_schema`. Copy ceilings
follow this file's Copy section and
`references/anti-patterns/copy-anti-patterns.md`. No asset is
used sight unseen: every candidate is opened with `lexsis_assets.view` and
judged against its section with the fit review in section 1b of
`references/workflows/section-asset-workflow.md` (the subject does the job,
it crops to the slot aspect without losing the subject, a quiet area holds
the copy, lighting and palette match the neighbouring slots, no baked-in
text, watermark or promo overlay); a generated backdrop or texture is viewed
the same way when it returns.

**`hero`**
- Purpose: programme name and the value sentence in currency; Join for
  guests, Log in or balance for members.
- Media: optional. Default `typographic`. When rewards are physical, one
  `identity` or `product-in-context` image of a reward: catalog media, then
  library tag `product-shot`, then merchant upload; view with
  `lexsis_assets.view` and confirm the reward as redeemed and a palette fit.
  Gap: ask the merchant (reward packshot, portrait or square, one); upload, or `hero_bg` as a
  backdrop behind the typographic hero when the plan names it the bold
  moment; never generated rewards, membership cards, coins, ribbons or tier
  badges. No-go: stock people as members, a "VIP card" render, a lifestyle
  band.
- Island: `none`. Header `SiteHeader` or `Navbar` from
  `lexsis_brand.navigation`; preset `siteheader/sticky-light` or
  `navbar/sticky-light` when it fits. Guest and member states come from the
  storefront customer object in HTML, not from an island.
- Copy: programme name plus the arithmetic, 14 words; one line beneath.
- Decide with: whether a physical reward with a real image exists (read 2);
  whether the customer login state is available on the surface (read 3).

**`how-it-works`**
- Purpose: earn, redeem, refer in three lines.
- Media: no photographs. Icons only as one inline SVG set with visible
  labels (N3) or none; no tiles, no colour blocks.
- Island: `none`.
- Copy: one line per step, verb first.
- Decide with: the programme configuration from read 1.

**`benefits-earn`**
- Purpose: the ways-to-earn table with a point value per action.
- Media: no; the table is the object.
- Island: `none` (HTML `<table>`).
- Copy: action and points per row; nothing else.
- Decide with: read 1; an action not in the configuration is not listed.

**`offer-rewards`**
- Purpose: redemption table with point cost, reward value, the conversion
  shown as arithmetic, expiry and exclusions on the same screen.
- Media: yes when rewards are physical products: an `identity` thumbnail per
  reward from catalog media (viewed with `lexsis_assets.view`: the reward
  exactly as redeemed, one background across the set) in the row; credit or discount rewards are text rows. Gap: ask the merchant for
  the missing reward packshots (square, count); never generic gift or coupon
  icons, never a generated product; a text row is the merchant's call.
- Island: `none` (HTML table with an image cell).
- Copy: arithmetic line ("100 points is ₹100 off"), expiry and exclusions
  under the table, link to the full terms.
- Decide with: read 1 for values; read 2 for reward images.

**`comparison-tiers`** (conditional)
- Purpose: threshold, qualifying period, perks per tier, downgrade rule.
- Media: no; when a tier perk is a physical gift its `identity` image sits
  in the cell from catalog media, viewed the same way. No tier badge art.
- Island: `none` (HTML table; on mobile a horizontally scrolling table or
  CSS-only tabs with radio inputs per tier).
- Copy: perks lead with access and service; each early-access window has
  its start and end datetime.
- Decide with: read 1; a tier without threshold and qualifying period is not
  shown.

**`referral-form`**
- Purpose: both sides of the reward in currency, email share first.
- Media: no.
- Island: `EmailCapture` when the share is a single friend-email field;
  `FunnelRuntime` inline when the referral app needs a logged-in advocate or
  a generated link (steps from the read-4 schema via
  `lexsis_drafts.funnel_create` and `lexsis_capture.validate_funnel`), or a
  link to the app's portal. Inputs: the schema in read 4, the app's share
  endpoint. Resolve props from `lexsis_design.island_schema`; the reward
  maths live in HTML beside the form, not in a discount line. Copy-link
  second and social third as plain HTML buttons after the email form.
- Copy: 25 words plus the terms line (friend's minimum spend, expiry).
- Decide with: the schema in read 4; no schema and no portal URL means the
  section is a link to the account page and the share tools wait.

**`faq`** (recommended)
- Purpose: expiry, combining with codes, refunded points, downgrade,
  eligibility.
- Media: no.
- Island: `none`; native `<details>` and `<summary>`, all collapsed.
- Copy: five to eight questions, answer first, 60 words each.
- Decide with: read 1 and the merchant's support questions.

**`closing-cta`** (recommended)
- Purpose: repeat Join or Log in.
- Media: no. Island: `none`.
- Copy: the same imperative as the hero.
- Decide with: page length; on a five-section page the hero CTA is enough.

### Asset budget
| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | `identity` packshots of physical rewards | nothing required; a reward image when rewards are credit only | rows stay text; ask the merchant to upload a packshot for any physical reward without one; no gift icons |
| asset library | a prior packshot; a merchant-owned event photo | member imagery | ask the merchant for consented member or event photos; never stock or generated people; the page has no lifestyle band |
| generation | backdrops and textures only (`hero_bg` behind the typographic hero, `texture_fill` at 8% or less page-wide) | rewards, cards, coins, badges, people, text | never |

With minimal assets the page is a typographic hero, three text steps, three
HTML tables, the email share form and native `<details>` FAQs; it needs no
image to be complete. Generated assets on this type are usually zero and at
most one backdrop; the house cap is four per page. Every asset placed, generated ones included, was
opened with `lexsis_assets.view` and passed the fit review before use.

## Above the fold (390px)

In order: full header; programme name; the one-line value in currency or
the top perk; the Join button (member state: Log in or balance); the first
row of the how-it-works steps. A `typographic` hero is the default; a
rewards product image is optional.

Must not appear: a paragraph of prose, a member count without a ledger row,
a countdown, star glyphs, a product grid, a discount pill.

## Proof

One or two modules. `policy-fact` is required: the reward maths, expiry and
exclusions rendered exactly as the programme terms state them. Optional
second module: `customer-count` for members ("over 12,000 members", from a
platform export, rounded down, dated) or `review-quote` from a member that
mentions the programme (verbatim, attributed as stored). No press, no UGC
grid, no expert. When there is no verified count, the page shows none; a
new programme says "new" rather than inventing a community
(`references/proof/reviews-sourcing.md`, Tier 5).

Legal edges: points expiry and redemption terms are material and must be
visible next to the value; obscuring the point value is "interface
interference" under India's CCPA dark-pattern guidelines (LAW,
https://consumeraffairs.nic.in/theconsumerprotection/guidelines-prevention-and-regulation-dark-patterns-2023).
The referred friend's reward is a discount or "free" claim and follows FTC
16 CFR 251.1 proximity rules (LAW, https://www.law.cornell.edu/cfr/text/16/251.1).
Rewards for reviews are allowed only when not conditioned on sentiment and
are disclosed beside the review summary (LAW, FTC 16 CFR 465;
`references/proof/reviews-sourcing.md`).

## Offer and CTA

One or two CTAs: Join (or Log in) in the hero and repeated at the close;
the referral share button belongs to the referral form and is the action
of that section, not a third page CTA. Sticky forbidden. Copy pattern:
next-step ("Join [programme]", "Log in to see your points", "Share your
link"); never "Unlock rewards".

Reward maths shown, never implied: points per currency unit, points per
reward, the resulting percentage back, expiry. Two-sided referral rewards
in currency; cash or credit rewards reached meaningful revenue share 2.2 to
3.7 times more often than coupon-only rewards, referred customers were
10.7 times more likely to refer again (3.27% against 0.30%), and 83% of
advocates refer exactly once, so the share step must be effortless
(OPERATOR, ReferralCandy,
https://www.referralcandy.com/blog/referred-customers-study/). Email shares
convert better than social shares, so email leads the referral form
(OPERATOR, Yotpo, https://support.yotpo.com/docs/referral-program-how-it-works).
VIP perks are access and exclusivity, not a deeper discount (OPERATOR,
Common Thread Collective,
https://commonthreadco.com/blogs/ecommerce-playbook/dig-in-bfcm-offer-database-2023);
early-access windows have real start and end datetimes in the offer ledger.

Offers that fit: `none`, `referral`, `loyalty`, `free-shipping` as a tier
perk, `limited-edition` as member-only drops; `mystery`, `gift-card` and
`student-military` when the merchant confirms them as perks. Offers that do
not fit: `percent-off`, `fixed-off`, `first-order`, `bogo`, `flash-sale`,
`clearance`, `subscribe-save`, `cashback`. Free shipping open to everyone
is not a VIP perk and may not be listed as one.

## Imagery

No required job; zero to one image (HEURISTIC,
`references/assets/image-jobs-by-page-type.md`). Hero `typographic` by
default; `product-in-context` or `packshot` of a reward item when the
rewards are physical. Icons for the three steps follow design-rules N3 (one
inline SVG set, one stroke, visible labels) or are omitted. No lifestyle
band, no stock people as members. Video optional and rarely useful. Slots
the plan must create: none by default; one reward `identity` slot when a
physical reward exists.

## Copy

Framework: FAB for each perk (what it is, what it gives, why it matters) in
answer-first sentences. Headline pattern: programme name plus the value
sentence ("Copper Rewards. Every ₹100 earns 5 points."). Reading level
grade 6; whole page 200 to 400 words excluding tables; no paragraph longer
than 40 words; tables carry the detail. Vocabulary: "points", "credit",
"early access" with their exact conversion; never "exclusive" without
naming what is excluded from whom, never "family" or "tribe". CTA verbs are
imperative and literal. Copy rules in `references/copy/copy-frameworks.md`.

## Never

- Never state a member count without an export-backed ledger row.
- Never omit expiry or exclusions from the screen where a reward value is
  shown.
- Never render referral by social share alone; email share is primary.
- Never list a perk that every shopper already receives.
- Never explain the programme in paragraphs where a table would do.
- Never show a Join CTA to a logged-in member or a balance to a guest.
- Never place this module above the fold on a cold-traffic page.
- Never show tiers without the threshold and the qualifying period.
- Never reward reviews conditioned on rating, and never hide that reviews
  were rewarded.

## Examples

- Copper Cow Coffee rewards, https://coppercowcoffee.com/pages/rewards:
  guest and returning-customer states in the hero, "How to earn" and "How
  to cash in" as two short lists, FAQ, no prose.
- Sephora Beauty Insider, https://www.sephora.com/beauty/beauty-insider:
  three-tier table with spend thresholds and perks per tier, what the
  member is working toward made visible.
- Smile.io loyalty page round-up (Blume, Buttercloth, Goose & Gander),
  https://blog.smile.io/favorite-ecommerce-loyalty-pages/: Join at top and
  bottom, three-icon how-it-works, tiers shown as aspiration.

## Checklist

```json
{
  "page_type": "referral-loyalty-vip",
  "aliases": ["rewards page", "loyalty explainer", "refer a friend page", "VIP tiers page", "members page", "points page"],
  "funnel_stage": ["retention"],
  "awareness": ["most-aware"],
  "traffic": ["email", "direct", "sms"],
  "sections": { "min": 5, "max": 8 },
  "mandatory_sections": ["hero", "how-it-works", "benefits", "offer", "referral-form"],
  "recommended_sections": ["comparison", "faq", "closing-cta"],
  "forbidden_sections": ["buy-box", "product-grid", "countdown", "stock-indicator", "sticky-cta", "problem", "agitation"],
  "nav": "full",
  "price_above_fold": "optional",
  "cta": { "min": 1, "max": 2, "first_after_section": 0, "sticky": "forbidden", "copy_pattern": "next-step" },
  "proof": { "min_modules": 1, "max_modules": 2, "required_kinds": ["policy-fact"], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked", "stock-count"] },
  "imagery": { "required_jobs": [], "hero": "typographic", "video": "optional", "min_images": 0 },
  "copy_framework": ["fab", "answer-first"],
  "offer_compat": { "allowed": ["none", "referral", "loyalty", "free-shipping", "limited-edition", "mystery", "gift-card", "student-military"], "forbidden": ["percent-off", "fixed-off", "first-order", "bogo", "flash-sale", "clearance", "subscribe-save", "cashback"] },
  "urgency": "verified-only"
}
```

## Sources

- ReferralCandy referred-customers study: https://www.referralcandy.com/blog/referred-customers-study/
- ReferralCandy referral benchmarks 2025: https://www.referralcandy.com/blog/referral-program-benchmarks-whats-a-good-conversion-rate-in-2025/
- Yotpo referral program how it works: https://support.yotpo.com/docs/referral-program-how-it-works
- Yotpo rewards page guide: https://support.yotpo.com/docs/creating-a-rewards-page
- Smile.io loyalty landing page guide: https://help.smile.io/en/articles/8174498-create-a-loyalty-landing-page
- Smile.io favourite loyalty pages: https://blog.smile.io/favorite-ecommerce-loyalty-pages/
- Common Thread Collective BFCM offer database (VIP early access): https://commonthreadco.com/blogs/ecommerce-playbook/dig-in-bfcm-offer-database-2023
- India CCPA dark-pattern guidelines 2023: https://consumeraffairs.nic.in/theconsumerprotection/guidelines-prevention-and-regulation-dark-patterns-2023
- FTC "Free" guide, 16 CFR 251.1: https://www.law.cornell.edu/cfr/text/16/251.1
- Copper Cow Coffee rewards: https://coppercowcoffee.com/pages/rewards
- Research notes: internal research audit (2026-09-10) block 26; internal research audit (2026-09-10) sections 1.10, 1.11, 5.

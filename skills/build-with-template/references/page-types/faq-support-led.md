# FAQ and support-led page

The page answers questions before they become abandoned carts or support
tickets: shipping, returns, sizing or fit, care, then the objections that
stop a product-aware shopper from buying. Visitors arrive from navigation,
a footer or PDP link, a support reply, or a search like "does X work with
Y". Their job is to find the answer in one scan and go back to the product
or to a human. The page is answer-first, lightly sold, and measured by exit
rate, click-through to the product, and support contacts per order.

## Identify it

- The brief says "FAQ", "help page", "customers keep asking", "reduce
  tickets", "questions before you buy", or the product is high-consideration
  with fit, value, proof or risk doubts.
- Near neighbours: `comparison-us-vs-them` when the question is "which one";
  `ingredient-science` when the question is "why does it work";
  `pdp` when the answers belong beside the buy box. Most shoppers never
  open a standalone FAQ (67%, Hotjar via WebMedic, OPERATOR,
  https://webmedic.com/ecommerce-faq-page-guide), so the same answers also
  ship as a five-to-eight-item `faq` block on the PDP and landing pages.

## Variants

- Dedicated help page: 15 to 25 questions in four to six groups, category
  index, one light CTA.
- FAQ-first landing page: five objection questions plus one CTA, used when
  the traffic is product-aware and copy has stalled (OPERATOR,
  https://www.landandconvert.com/blog/landing-page-faq-method).

## Anatomy

1. `hero` mandatory: question-led headline ("Questions before you order"),
   one sentence, optional in-page search field when the page holds ten or
   more questions; no product pitch.
2. `toc` conditional: ten or more questions; category index with anchors in
   this order: shipping, returns, sizing or fit, care or usage, product,
   account and payment.
3. `faq` mandatory: grouped questions, all collapsed, a `<details>` and
   `<summary>` accordion is acceptable; shipping and returns first, then
   sizing, care, product, account; 15 to 25 questions on a dedicated page,
   no more than 40.
4. `objections` mandatory: fit, value, proof and risk questions phrased as
   the shopper would type them ("Will it feel heavy?", "Why is it ₹2,000
   more than the other brand?", "Are the reviews real?", "What if it does
   not work for me?"), each dissolved with a verified fact.
5. `size-guide` conditional: sized goods; measurements table, how to
   measure, model reference.
6. `usage` conditional: care or setup that generates tickets; three
   photographed steps.
7. `closing-cta` mandatory: "Still unsure?" with the contact channel and
   hours, and one link to the product or bestsellers; the single CTA of the
   page.

## Workflow

### Context reads
1. Policy facts from the store's policy pages (URLs): shipping cost, time
   and free threshold; returns and refunds including who pays return
   shipping; cancellation path; warranty; the grievance contact for India.
   Each is a proof ledger `policy-fact` row; an answer must match the policy
   text word for word.
2. The question list: merchant support tickets, `lexsis_catalog.reviews_search`
   for recurring questions and complaints, ad comments. Group them in the
   fixed order (shipping, returns, sizing or fit, care or usage, product,
   account and payment) and add the four objection families (fit, value,
   proof, risk). Target 15 to 25 questions on a dedicated page, never more
   than 40; five on a FAQ-first landing variant.
3. `lexsis_catalog.get` for the product or line the page supports: media
   that answers a question faster than words (a `detail` macro for "will it
   feel heavy", a `scale` shot, a `size-reference` on a model with stated
   size, `packaging` for "how do I return it"), the `identity` packshot for
   the closing link, variants for the size table
   (`references/assets/image-jobs-by-page-type.md`).
4. `lexsis_brand.context`, `lexsis_brand.brand_kit` and
   `lexsis_brand.navigation` for `theme_id`, voice, the support channel and
   hours, and the full header and footer (nav is `full`).
5. `lexsis_asset_library.search` with `theme_id`, `mode: "tags"`:
   `lifestyle` and `product-shot`; then semantic "how to measure", "size
   chart", "care <product>", "washing", "assembly" for `sequence`,
   `size-reference` and `diagram` material; view with `lexsis_assets.view`.
6. `lexsis_catalog.reviews_status` and `lexsis_catalog.reviews` for the
   "Are the reviews real?" answer: average, count, source and the
   verification method; below 5 reviews the answer states the count only.
7. `lexsis_design.islands`, then `lexsis_design.island_schema` for
   `SizeGuide`, `DeliveryEstimate` and `VideoPlayer`; the accordion, the
   topic tabs and the back-to-top control are native HTML per
   `references/workflows/island-selection-workflow.md`.

### Section by section
Media lines follow `references/workflows/section-asset-workflow.md` and
`references/assets/asset-sourcing-sequence.md`; video per
`references/assets/video-rules.md`. When every step finds nothing: tell the
merchant what is missing (job, aspect, count), offer upload via
`lexsis_asset_upload.upload` or generation when the purpose is feasible
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
- Purpose: question-led headline, one sentence, the search field when the
  page holds ten or more questions; no pitch.
- Media: no by default. The type's hero is `typographic` and section 5 of
  `references/assets/image-jobs-by-page-type.md` rules out a photo hero here.
  When the page supports a single product, a `detail` macro of it from
  catalog media (viewed with `lexsis_assets.view`: the supported product,
  legible at inset size) may sit as a small inset beside the headline on desktop
  only (hidden at 390 so the mobile fold stays text only), never as a
  background, never full-bleed, never generated. No-go: a lifestyle photo, a
  stock support agent, an illustration of a question mark, a `hero_bg`
  backdrop.
- Island: `none`. Header `SiteHeader` or `Navbar` from
  `lexsis_brand.navigation`; preset `siteheader/sticky-light` or
  `navbar/sticky-light` when it fits. The search field is a plain
  `<input type="search">` that filters the `<details>` list.
- Copy: a question or "Questions before you order", 8 words; one sentence.
- Decide with: question count from read 2; single-product scope from read 3.

**`toc`** (conditional)
- Purpose: category index with anchors in the fixed order.
- Media: no.
- Island: `none`. Anchor links to each group heading. With three or more
  groups on a long page, CSS-only tabs with radio inputs by topic are an
  alternative, each panel holding that group's `<details>`; the anchor index
  stays the default because hidden panels defeat find-in-page.
- Copy: the group names only.
- Decide with: ten or more questions in read 2.

**`faq`**
- Purpose: grouped questions, all collapsed, shipping and returns first.
- Media: yes where a picture answers faster than a sentence, one per topic
  at most: an inline SVG `diagram` of the return process or delivery
  regions; a real `packaging` photo for "what do I send back"; a care
  `sequence`. Catalog media, then library tag `lifestyle` or `product-shot`,
  then merchant upload, then an authored SVG for diagrams; view each with
  `lexsis_assets.view` and confirm the packaging is the merchant's own box
  and each sequence frame shows its step. Gap: ask the merchant (which
  topic, job, count); upload only, since generation has no
  feasible purpose on a support page; the answer stays text if they choose.
  No-go: an icon tile per category, a stock "customer service" photo, a
  colour band per group, all answers expanded.
- Island: `none`. Each question is a `<details>` with a `<summary>` under an
  `<h2>` per group; answers stay in the HTML for indexing. `DeliveryEstimate`
  inside the shipping answer only when the store ships to one country with a
  fixed estimate (inputs: the shipping row), cutoff countdown off; India
  pincode copy is static HTML.
- Copy: answer in the first sentence, one sentence of why, the next-step
  link; 60 words per answer.
- Decide with: the grouped list from read 2 and the policy rows from read 1.

**`objections`**
- Purpose: fit, value, proof and risk questions as the shopper types them,
  each dissolved with a verified fact.
- Media: yes when the fact is visual: a `scale` or `detail` image from
  catalog media beside "Will it feel heavy?", the issuer mark beside a safety
  question (`references/proof/trust-badges-certifications.md`), the review
  average and count beside "Are the reviews real?". Catalog media, then
  library, then merchant upload; view with `lexsis_assets.view` and confirm
  the image answers the question asked and any issuer mark matches its
  ledger row. Gap: ask the merchant for the scale or detail shot; never a before/after pair, never a generated badge or result
  (`references/proof/before-after-and-claims.md`).
- Island: `none`.
- Copy: as typed ("Why is it ₹2,000 more than the other brand?"); the answer
  is a number, a policy term or a study line with n, then the link.
- Decide with: proof ledger rows (`policy-fact`, `review-summary`,
  `certification`, `test-data`); an objection with no verified fact is
  answered with the guarantee or not asked.

**`size-guide`** (conditional)
- Purpose: measurements table, how to measure, model reference.
- Media: yes. Jobs `size-reference` (model with stated height and size worn)
  from catalog media, then library, then merchant upload; a how-to-measure
  `diagram` as an authored inline SVG; the measurements as an HTML `<table>`.
  A merchant chart image only when it cannot be transcribed, with the table
  repeated in HTML. View with `lexsis_assets.view`: the model photo shows
  the stated size and fit, and any chart image is legible at 390px. Gap: ask
  the merchant for the on-model photo (4:5, one
  per fit); never generated; the table alone is their call.
- Island: `none` by default (inline HTML table with units). `SizeGuide` when
  the merchant wants a unit toggle (inputs: measurement source, fits); it
  opens from a trigger, so keep the inline table as well so the answer is
  visible without a tap. Resolve props from `lexsis_design.island_schema`.
- Copy: how to measure in 40 words; the model line ("Model is 178 cm and
  wears M").
- Decide with: sized goods and the measurement source from read 3.

**`usage`** (conditional)
- Purpose: care or setup that generates tickets, in three photographed
  steps.
- Media: yes. Job `sequence` (three real step photos) or one captioned
  how-to video under 60 seconds: catalog media, then library semantic "care
  <product>", "assembly", then merchant upload; view each step with
  `lexsis_assets.view` and confirm the action is legible at 390px. Gap: ask
  the merchant for step photos (three, square); never generated; keeping the steps as a text
  answer inside `faq` is their call. No icon tiles.
- Island: `VideoPlayer` when a real video exists; otherwise `none`.
- Copy: one sentence per step; step text in HTML.
- Decide with: the ticket-generating topics in read 2, `sequence` coverage
  from reads 3 and 5, and the merchant's answer.

**`closing-cta`**
- Purpose: "Still unsure?" with the contact channel and hours, and one link
  back to the product or bestsellers.
- Media: yes, optional: the `identity` packshot of the linked product from
  catalog media, viewed with `lexsis_assets.view` to confirm the exact
  product, so the return path is visual. Gap: ask the merchant for the
  packshot; the link runs as text meanwhile. No-go: a product grid, an
  offer, a countdown.
- Island: `none`. On pages taller than two screens add a "Back to top"
  anchor link at the end of each group with CSS `scroll-behavior: smooth`
  under `prefers-reduced-motion: no-preference`.
- Copy: channel and hours ("Chat with us, 9 am to 6 pm IST"); one link
  ("Back to the product").
- Decide with: the support channel from read 4 and the product from the
  brief.

### Asset budget
| Source | Usually supplies | Usually missing | Per gap |
|---|---|---|---|
| catalog media | `identity` packshot, sometimes a `size-reference` or `detail` shot | care `sequence`, how-to video, a measuring diagram, a packaging photo for returns | ask the merchant to upload step photos or the video; author the diagram as inline SVG; the answer stays text only if they choose |
| asset library | prior lifestyle or product shots | topic imagery for shipping and returns | inline SVG diagram; ask the merchant for a real packaging photo; never stock agents or parcels |
| generation | nothing on this page (typographic hero, no bold moment) | product, people, results, badges, text, diagrams | never |

With minimal assets the page is a typographic hero, an anchor index, grouped
native `<details>` answers, objection answers with policy facts, and a
closing contact block; a single packshot at the close is the only image.
Generated assets on this type are zero; the house cap of four per page is
never approached. Every asset placed, generated ones included, was
opened with `lexsis_assets.view` and passed the fit review before use.

## Above the fold (390px)

In order: full header; the question-led headline; the search field when
present or the first three category links; the first group heading
("Shipping") with its first two questions collapsed. Text only; a
`typographic` hero.

Must not appear: a product price, a discount, a countdown, a review
carousel, an expanded wall of answers, a chat widget covering the search
field.

## Proof

Zero to two modules, and both live inside answers rather than as standalone
blocks: `policy-fact` (return window, shipping threshold, warranty term
copied from the policy page and linked), `review-summary` beside "Are the
reviews real?" (average, count, source, and the verification method as the
EU Omnibus requires), `certification` or `test-data` beside a safety or
efficacy question. No testimonial block, no UGC grid, no press row. When
the store has none, the answers cite policy only
(`references/proof/reviews-sourcing.md`).

Answer rules (OPERATOR unless tagged):

- First sentence is the answer (yes, no, a number, a date). Then one
  sentence of why. Then the next-step link. Under 60 words
  (internal teardown audit, 2026-09-10).
- Questions are mined from support tickets, reviews and ad comments; FAQs
  that miss the real question ("how do I clean it?") strand the shopper,
  and 70% of sites offer neither FAQ nor Q&A well (Baymard,
  https://baymard.com/blog/product-page-faq-and-qa).
- Logistics questions come first; the four objection families (fit, value,
  proof, risk) follow and are answered with proof or a guarantee, not
  reassurance (BrandRocket,
  https://www.brandrocket.net/resources/your-faq-is-answering-the-wrong-questions).
- Mandatory questions on every store: shipping cost and time, returns and
  refunds including who pays return shipping, how to cancel a subscription,
  ingredients or materials or sizing, who the product is not for.
- India: return, refund and exchange terms including the cost of return
  shipping, and the grievance contact, are required disclosures under the
  Consumer Protection (E-Commerce) Rules 2020 (LAW,
  https://ibclaw.in/consumer-protection-e-commerce-rules-2020/).
- Legal disclaimers sit in the same viewport as the claim they qualify,
  at 12 px or larger, not inside a collapsed answer alone (LAW, FTC
  "unavoidable" disclosures; India CCPA misleading-ads guidelines).

Structured data: FAQPage JSON-LD may be emitted, but Google shows FAQ rich
results only for well-known authoritative government and health sites since
August 2023, so a store should not expect rich results from it
(https://developers.google.com/search/blog/2023/08/howto-faq-changes).
Collapsed `<details>` content is still indexed; keep answers in the HTML,
not loaded on click.

## Offer and CTA

One CTA, in the closing section after the objection answers. A secondary
text link to the product at the end of a risk answer ("See the 60-day
returns policy") is a link, not a CTA. Sticky forbidden. Copy pattern:
next-step ("Chat with us, 9 am to 6 pm IST", "Back to the product"). Price
does not appear above the fold and appears in answers only as a fact
("Shipping is free over ₹999").

Offers that fit: `none`, `free-shipping` stated as the threshold fact;
`loyalty`, `bnpl`, `gift-card` and `student-military` only as answers to
"do you offer" questions with the terms, when the merchant confirms them.
Offers that do not fit: `percent-off`, `fixed-off`, `first-order`, `bogo`,
`gwp`, `flash-sale`, `clearance`, `mystery`. No urgency of any kind: a
support page with a countdown reads as a trap.

## Imagery

No required job; zero to two images (HEURISTIC,
`references/assets/image-jobs-by-page-type.md`). Hero `typographic`. When
used: `sequence` for a care or setup answer, `diagram` for a shipping map
or return process, `size-reference` for the size guide. Video optional:
one captioned how-to under 60 seconds inside the relevant answer. Icons per
category follow design-rules N3 or are omitted. Slots the plan must create:
none by default; one per conditional `size-guide` or `usage` section.

## Copy

Framework: answer-first throughout. Headline pattern: a question or
"Questions before you order"; never "Help Center" alone. Question pattern:
first person or second person, as typed ("Can I return it if the size is
wrong?"), never marketing questions ("Why is our serum different?").
Reading level grade 5 to 6; answer ceiling 60 words; page total 800 to
1,500 words across 15 to 25 questions. Vocabulary: exact numbers, dates,
currencies and policy terms; "you" outnumbers the brand name. No legal
jargon in answers; link to the policy for the legal text. Copy rules in
`references/copy/copy-frameworks.md`.

## Never

- Never answer with "it depends" or "shipping times may vary" without the
  range and the source.
- Never phrase a question as marketing.
- Never expand all answers by default.
- Never exceed 40 questions on one page.
- Never place a buy box, product grid, offer or countdown on the page.
- Never leave the page without a human contact path with hours.
- Never let a policy answer differ from the policy page text.
- Never skip the objection questions; a logistics-only FAQ is the most
  common failure.
- Never bury the page more than one click from the footer and the PDP.
- Never leave promo-period answers (cutoffs, codes) live after the period.

## Examples

- Huel FAQs, https://huel.com/pages/faq: "Popular questions" first
  (subscription, delivery, returns, cancel), then product groups; "Not sure
  which product is right for you?" as the single soft CTA.
- Seed DS-01 FAQ block, https://seed.com/daily-synbiotic: objection-phrased
  questions answered in the first sentence ("Do I have to sign up for a
  subscription? Yes."), eleven questions in JSON-LD, three shown.
- Sleepy Owl Coffee FAQs, https://sleepyowl.co/pages/faq: questions grouped
  by product and phrased as shoppers ask them ("How many cups does one
  brew pack make?"); what it lacks is a shipping and returns group first.

## Checklist

```json
{
  "page_type": "faq-support-led",
  "aliases": ["FAQ page", "help page", "questions before you buy", "objections page", "support page"],
  "funnel_stage": ["mof", "retention"],
  "awareness": ["product-aware"],
  "traffic": ["organic", "direct", "google-search"],
  "sections": { "min": 4, "max": 7 },
  "mandatory_sections": ["hero", "faq", "objections", "closing-cta"],
  "recommended_sections": ["toc", "size-guide", "usage"],
  "forbidden_sections": ["buy-box", "product-grid", "offer", "final-offer", "countdown", "stock-indicator", "sticky-cta", "us-vs-them", "agitation"],
  "nav": "full",
  "price_above_fold": "forbidden",
  "cta": { "min": 1, "max": 1, "first_after_section": 3, "sticky": "forbidden", "copy_pattern": "next-step" },
  "proof": { "min_modules": 0, "max_modules": 2, "required_kinds": [], "forbidden_kinds": ["social-proof-popup", "live-viewer-count", "press-logo-unlinked", "stock-count"] },
  "imagery": { "required_jobs": [], "hero": "typographic", "video": "optional", "min_images": 0 },
  "copy_framework": ["answer-first"],
  "offer_compat": { "allowed": ["none", "free-shipping", "loyalty", "bnpl", "gift-card", "student-military"], "forbidden": ["percent-off", "fixed-off", "first-order", "bogo", "gwp", "flash-sale", "clearance", "mystery"] },
  "urgency": "none"
}
```

## Sources

- WebMedic ecommerce FAQ page guide: https://webmedic.com/ecommerce-faq-page-guide
- Baymard, product page FAQ and Q&A: https://baymard.com/blog/product-page-faq-and-qa
- BrandRocket, four objection families: https://www.brandrocket.net/resources/your-faq-is-answering-the-wrong-questions
- Land and Convert, FAQ-first landing pages: https://www.landandconvert.com/blog/landing-page-faq-method
- Ecom Design Pro, PDP FAQ UX: https://ecomdesignpro.com/product-page-faq-ux/
- Google, changes to HowTo and FAQ rich results: https://developers.google.com/search/blog/2023/08/howto-faq-changes
- India Consumer Protection (E-Commerce) Rules 2020: https://ibclaw.in/consumer-protection-e-commerce-rules-2020/
- Huel FAQs: https://huel.com/pages/faq
- Sleepy Owl Coffee FAQs: https://sleepyowl.co/pages/faq
- Research notes: internal research audit (2026-09-10) block 29; internal research audit (2026-09-10) sections 7.7 and 7.12; internal research audit (2026-09-10) Part D pattern 10.

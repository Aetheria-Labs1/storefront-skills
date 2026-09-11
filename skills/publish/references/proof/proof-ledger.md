# Proof Ledger

Every trust element a page shows (a star, a count, a quote, a logo, a badge,
a photo of a customer, a "clinically tested" line) is a row in the plan's
`## Proof ledger` before design begins. `/design-page` renders only ledger
rows; `/generate` fails production QA on any proof element that is not in the
ledger; `/optimize` may add proof only by adding a row first. This file
defines the block, the verification each kind needs, and the display rules.
Sourcing procedures live in `references/proof/reviews-sourcing.md` and the
sibling files.

## The block

```markdown
## Proof ledger

| # | Kind | Supports claim | Source | Evidence | Verified | Section | Status |
|---|---|---|---|---|---|---|---|
| P1 | review-summary | overall quality | lexsis_catalog.reviews product gid://.../123 | 4.6 avg, 212 reviews, min rating 1 | API 2026-09-10 | review-summary | verified |
| P2 | review-quote | "no more 3pm crash" | collection 7f2e... item 9a1c... | verbatim text, name initial + city as stored, 2026-04-02 | API | benefits | verified |
| P3 | press-logo-linked | credibility | Vogue India | https://www.vogue.in/... (article names the brand) | fetched 2026-09-10 | press-marquee | verified |
| P4 | certification | "FSSAI licensed" | merchant | licence no. 1001...; issuer FSSAI | merchant doc | trust-bar | verified |
| P5 | ugc-video | in-use proof | creator @..., rights email 2026-08-21 | asset id ... | merchant consent | ugc-grid | verified |
| P6 | customer-count | "50,000+ customers" | merchant | Shopify orders export, 51,204 unique customers to 2026-08-31 | merchant doc | stats | pending |
| P7 | before-after | "visible in 4 weeks" | merchant | none supplied | none |  -  | dropped |
```

Columns:

- **Kind**: one id from the proof kind vocabulary in
  `references/page-types/_checklist-format.md`.
- **Supports claim**: the exact page claim this proof stands beside. Proof
  without a claim is decoration; drop it.
- **Source**: the system, person or publication that holds the evidence.
- **Evidence**: the id, URL, count, document, or verbatim text.
- **Verified**: how and when (API date, fetched URL, merchant document,
  consent record). "Merchant says" is `pending` until a document or written
  confirmation exists.
- **Section**: the canonical section id where it renders.
- **Status**: `verified`, `pending` (may not render), `dropped` (with reason
  in the row).

## Verification required per kind

| Kind | Minimum evidence before `verified` | Never |
|---|---|---|
| review-summary | `lexsis_catalog.reviews` total and average for the exact product or collection; count >= 5 to show an average, >= 1 to show a count | rounding 4.3 to 5.0; "5.0" with under 20 reviews; stars without a count |
| review-quote / review-list / review-with-media | row exists in `lexsis_catalog.reviews` or `review_collection_items`; text verbatim; attribution exactly as stored; date present | edited wording beyond `[...]` trimming; invented names, cities, photos; five identical five-star quotes |
| external-verified-quote | public URL, platform terms allow reuse, merchant written approval, verbatim text, attribution the platform allows; manifest `reviews.source: external-verified` | marketplace text that the platform's terms forbid copying; quotes from DMs without consent |
| ugc-photo / ugc-video / creator-video | asset id in the library, rights record (email, contract, platform rights request), creator handle, paid disclosure flag when paid | stock people as customers; generated people; content without rights |
| before-after | merchant-supplied, same subject, same framing and lighting, unretouched, timeframe stated, consent, category permitted (`references/proof/before-after-and-claims.md`) | generated, composite, or "illustrative" results; medical outcomes without substantiation |
| expert-quote / founder-note | named person, credential verifiable, written approval, material connection disclosed | anonymous "doctors recommend"; invented titles |
| press-logo-linked / press-quote-linked | fetched article URL that names the brand or product; not a press release wire; paid placements disclosed as such | logos without a URL; "as seen in" for a wire release; podcast without episode link |
| certification / award | issuer, certificate or licence number, scope, current date; exact issuer wording (`references/proof/trust-badges-certifications.md`) | "FDA approved" for anything FDA does not approve; "dermatologist tested" without a test report; generated badge art |
| test-data / case-study | document or URL with method, sample, date; numbers copied exactly; disclaimer where required | "clinically proven" from an ingredient supplier's study applied to the product |
| customer-count / sales-count / repeat-rate | merchant export or analytics screenshot with date; rounded down; phrase "over N" | invented, rounded up, or extrapolated numbers |
| guarantee / policy-fact | store policy page URL or merchant confirmation; exact terms | "free returns" when returns cost; "lifetime" without terms |
| community-screenshot | platform, date, consent from the poster (or public brand-owned content) | screenshots of paid or fake accounts |
| stock-count | live `lexsis_catalog.get` inventory read at render time via island binding | fixed numbers in copy |
| social-proof-popup, live-viewer-count, press-logo-unlinked | never verified; never rendered |  -  |

## Display rules

1. **Proof proximity.** A quote or number sits beside the claim it supports,
   not pooled in one "testimonials" block. A standalone reviews section holds
   the breadth (list or carousel); claim-specific rows go inline.
2. **Density.** Modules within the type checklist's `proof.min_modules` and
   `max_modules`. A module is one section or one inline element; the same
   ledger row may render once.
3. **Stars.** Show stars only next to a numeric average and count (count of
   5 or more for an average). Distribution (or "n% recommend"): hidden below
   10 reviews, optional from 10 to 19, required and click-to-filter at 20 or
   more. Use the real average to one decimal; do not show 5.0 unless every
   review is five stars and there are at least 20. No average in the hero or
   buy box when the newest review is older than 12 months (recency gate).
   A filtered carousel (`minRating`) is labelled as a selection, links to the
   full unfiltered list, and sits beside the unfiltered average and count;
   `averageRating` and `totalReviews` are never computed from a filtered set.
4. **Quotes.** Verbatim. Trim with `[...]` only. Keep the reviewer's own
   specifics (product variant, timeframe, use). Attribution exactly as
   stored plus the date. Prefer reviews that mention the claim and, where
   possible, a limitation.
5. **Counts.** Round down, prefix "over", include the as-of month when older
   than 90 days. Never mix units ("customers" vs "orders").
6. **Press.** Monochrome logos at one height, each an `<a>` to the ledger
   URL with the publication as accessible name; three to six logos; caption
   "Press" or "In the press", never "As seen in" unless the outlet actually
   featured the product. Paid placements say "Sponsored feature". Mentions
   older than 24 months drop out (12 months for "as seen in" or "featured").
7. **Badges.** Issuer text next to the mark; monochrome; no generated art;
   one row, three to five badges, never repeated per section.
8. **UGC.** Native aspect (9:16 or 1:1), captions on video, click to play,
   creator handle, "Paid partnership" when paid, rights recorded.
9. **Before/after.** Same crop, labels "Before" and "After" with the
   interval, "Individual results vary" where the category requires it,
   never in the hero, never generated.
10. **Numbers in copy.** Every numeral inside a proof, trust, stats or press
    section appears in the ledger. the source/hosted review lists them; the review
    checks each.

## Fallback order when the ledger is thin

1. Guarantee and policy facts (returns, shipping, warranty) with exact terms.
2. Certifications and licences with issuer.
3. Product evidence: test data, ingredient sourcing, materials, process
   photos.
4. A founder note with a real name and signature.
5. Verified press with links.
6. A "first customers" programme: an honest invitation (early access,
   founder contact, review request) that says the product is new.
7. Nothing. A page with no proof section is honest; a page with invented
   proof is a liability.

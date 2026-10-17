# Hosted Design Review

The hosted renderer is the acceptance surface. Compile success is necessary,
not sufficient.

## Evidence

Review the exact hosted page id and version at:

- 390px mobile;
- 768px tablet;
- 1280px desktop.

Record the hosted URL, tested version, viewport, result, finding, and evidence.
Do not claim a browser, hydration, or commerce pass from source inspection.

## Visual and Responsive Review

At every viewport confirm:

- first attention lands on the plan's intended decision and bold moment;
- section order, hierarchy, copy, CTA, and asset crop match the approved plan;
- optional visual decisions are visibly represented without using concept
  images as media;
- typography, spacing, alignment, backgrounds, and density feel intentional;
- there is no horizontal overflow, clipped text, hidden content, accidental
  overlap, or broken image;
- product identity, variant, label, shade, packaging, and proof imagery remain
  accurate;
- focus states, keyboard access, contrast, alt text, reduced motion, and tap
  targets are usable;
- mobile does not stack multiple fixed regions or hide the primary action;
- motion pauses or respects reduced motion;
- header, navigation, announcement, and footer appear exactly once.

Remove decorative elements that do not support hierarchy or comprehension.
Check for generic repeated cards, excessive pills, uniform radii, icon grids,
and section bands used only to create variety.

## Copy, Proof, and Offer Review

Compare rendered text with the approved plan:

- all required copy is present and wording is unchanged;
- every numeral, quote, rating, count, result, logo, certification, policy,
  urgency statement, price, and offer traces to an approved row;
- live prices, variants, availability, review totals, and offer mechanics
  still match;
- unsupported proof, fake activity, reset timers, fabricated scarcity, and
  unapproved claims are absent.

## Interaction and Commerce Review

Exercise every planned interaction. For commerce pages verify:

- expected product and variant enter the cart;
- sold-out variants are disabled and not silently swapped;
- variant media and price remain synchronized;
- cart opens in the intended responsive form;
- quantity, line totals, subtotal, selling plan, discount, and checkout path
  update correctly;
- Quick Add and sticky purchase controls, when present, target the correct product state;
- disclosures, details, forms, quiz/funnel steps, video, galleries, and review
  controls respond;
- hydration does not blank, flicker, duplicate, or shift content;
- no console errors occur.

## Collection review

For CollectionGrid and CollectionSwipe pages, verify on the hosted page:

- the grid loads the planned collection with live prices, stock and the
  result count;
- applying a filter or sort updates the URL (`filter.*`, `sort_by`), and
  reloading that URL restores the same filters, sort and results;
- clearing filters returns the full collection; a filter with no results
  says so;
- "Load more" appends the next page, updates `page` in the URL, and is a
  link to that page;
- Quick Add adds the correct product and variant; multi-variant products
  open the picker; sold-out variants are disabled; the cart opens or stays
  closed as `openCartOnAdd` intends;
- when paired, the swipe deck appears only below 768px and the grid only at
  768px and wider (check 390px and 1280px); swipe right adds, swipe left
  passes, photo taps step through images, undo restores the last card.

## Template review

For a product or collection template, open the preview at two or three
different handles from the plan
(`<renderer>/v/<template slug>?preview=1&resource=product:<handle>` or
`resource=collection:<handle>`). At each, confirm every bound island and
text shows that resource, no other product's name, image, claim or offer
leaks into shared copy, and the layout holds for the longest title, the
fewest images and a sold-out or small resource. After routing, confirm
`lexsis_pages.resolve_resource` returns the template for those handles.

## Quiz review

Use `references/quiz-authoring.md` for path, fallback, product/variant, and capture
checks. Test forward/back/review/result transitions, focus after state changes,
reduced motion, and saving/error states. Apply checks only to controls present;
a Quiz does not need a duplicate Quick Add, BuyBox, or sticky control to pass.

Preview does not collect production responses. Keep live saving/analytics checks
pending until authorized activation and publication, then verify on the returned
published URL. Do not infer saving from a result screen or purchase from cart
success. Reuse existing MCP QA evidence and operation notes; do not save local
JSON or screenshot reports.

## Record and Repair

Read `lexsis_pages.integrity` and `lexsis_pages.qa`; save supported results with
`lexsis_drafts.page_record_qa`.

For a finding:

1. Read current edit context and editable source.
2. Stop on unexpected version drift.
3. Edit the smallest intended source area.
4. Compile the complete changed inputs.
5. Write with `expected_version`.
6. Read back, inspect `lexsis_pages.diff`, and rerun integrity.
7. Rerun the affected viewport and interaction checks.

Never create a replacement draft for a design fix. Any visible edit resets
user approval for that version.

When browser access is unavailable, return the hosted preview as
`DRAFT_CREATED` with QA pending. `DESIGN_APPROVED` requires passed hosted
evidence and explicit user approval for the tested page version.

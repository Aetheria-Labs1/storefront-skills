# Page planning contract

`/plan-page` produces the complete specification `/design-page` builds from;
`/optimize` produces the same blocks for an existing page. Choose the type in
`references/page-types/_index.md`, plan with
`references/workflows/_how-to-read.md`, and keep the house rules in
`references/design-rules.md`. The plan records copy, assets, evidence and
tasks; schema-level island choices happen in design.

## Blocks, in order

Page type; Page strategy; Consumer decision model; Design direction (with the
Imagery and background plan); Section specification; Asset slots; User
selection (when a role has several candidates); Generation briefs (when a slot
is generate-required or composite-required); Generation record (filled after
generation); Proof ledger; Offer ledger (when an offer exists); Message match
(ad or paid-search traffic); Claim gate; Work queue; Plan status.

## Section specification

One entry per section: purpose; eyebrow, headline, subhead, body, labels, CTA
with destination, FAQ answers; claim ids; 1280 and 390 layout; interaction
behaviour without island names or props; asset decision. Copy is final
customer-facing text in sentence case: h1 at most 10 words, subhead at most
20, paragraph at most 45, FAQ answer at most 60.

## Asset slots

| Slot | Section | Role/purpose | Aspect | Decision | Source decision | Id / URL | Status |

Decision is one of: none-required (section line only), reuse-selected,
shopify-product-media, user-selection-required, user-upload-required,
generate-required, composite-required. reference-only marks a baked creative
that is never placed and names its replacement slot. Status stays verified or
planned: verified only with reuse-selected or shopify-product-media. A
generate-required or composite-required slot carries a brief: aspect and
crops, subject, composition, wardrobe, palette, lighting, mood, exclusions,
composite source, alt intent, estimated credits, approval. Purposes and the
ALLOW / ASK / NEVER lists follow `references/assets/generation-policy.md`.
Every asset is viewed before it fills a slot
(`references/workflows/section-asset-workflow.md` section 2).

## User selection

| Role | Section / slot | Candidates (asset id - one-line description - fit note) | Why the choice matters |

Offered only for roles with more than one fit-reviewed candidate (hero
editorial visual, formula or detail visual, social-proof or results visual,
closing CTA visual). Never assume a selection when the visual decision
materially affects the page.

## Claim gate

| # | Claim (verbatim) | Where | Gate | Evidence | V1 copy if not approved |

Gate is one of: approved evidence available (a verified P or O ledger row in
that section), merchant evidence required, remove from V1. No clinical badge,
before/after image, rating, review count, results timeline or efficacy claim
without an evidence row assigned to that exact section.

## Work queue

| # | Task | Owner | Section / slot | Unblocks | Status |

Owner is one of: user, agent, merchant, blocked-by-evidence. Status is open
or done. Every plan carries build, crop verification and claim/asset/CTA QA
tasks plus one per open claim, pending slot and unconfirmed offer item.

## Plan status

BLOCKED - evidence required when any open task is blocked-by-evidence;
PLAN_COMPLETE - asset tasks pending when any open task is owned by user or
merchant; otherwise PLAN_READY_FOR_DESIGN. PLAN_APPROVED is recorded only
after the user's explicit approval and never while blocked. `/optimize`
returns OPTIMIZATION_PLAN_READY in place of PLAN_READY_FOR_DESIGN.

`/design-page` refuses a blocked or unapproved plan, executes the agent tasks
and asks for the user and merchant tasks before composing, places the section
copy verbatim (recording any fit edit), renders only approved claims, and
returns DESIGN_APPROVED after the hosted review at 390, 768 and 1280.

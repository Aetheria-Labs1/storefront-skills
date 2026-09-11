---
name: page-builder
description: |
  Build a Shopify storefront page through the Lexsis setup, planning, design,
  generation, and draft-QA workflow. Never publishes without separate
  explicit approval.

  <example>
  Context: User wants a new landing page
  user: "Build a landing page for our vitamin C serum"
  assistant: "I'll use the page-builder workflow and stop at an approved draft."
  </example>
model: sonnet
color: green
---

# Lexsis Page Builder

Use the public commands as distinct stages:

```text
/setup U+2192 /plan-page U+2192 /design-page U+2192 /generate
```

`/publish` remains a separate explicit action.

For the fastest unpublished draft, use `/build`; use
`/build-with-template` when the user already supplied a page-kit or section
template. These routes return `DRAFT_CREATED` before deeper QA. When the user
wants to approve the appearance first, `/design-page` may generate a
mobile-first visual concept with the existing Lexsis image tools.

Infer whether the user wants a quick reversible draft or production-ready
verification from the complete request. Do not require a magic phrase.
Reversible ambiguity defaults to a fast unpublished draft; publishing remains
a separate explicit operation.

## MCP Gate

Use the exact router/action pairs declared by each stage. Call
`lexsis_discover` only for an unfamiliar argument schema, passing structured
`router` and `action` fields. Never use a prose query for a known action. A
zero-result directory lookup is not an MCP outage; report failures from the
actual domain call. Do not replace a failed Lexsis operation with static HTML
unless the user explicitly requests a separate offline prototype.

## Setup

Read `work/storefront/setup/setup.json` and select one saved store/theme pair.
If it is missing, tell the user to run `/setup`; do not invoke it
automatically. Reuse saved brand design and theme CSS, while reading current
products, prices, assets, schemas, permissions, credits, and page versions
live.

## Plan

Identify exactly one page type first with the plan skill's packaged
`references/page-types/_index.md` (traffic, funnel stage, awareness, offer
shape, product count, campaign trigger, desired action), record it in the
`## Page type` block and `page.pageType`, and load only that type's file. Follow its `## Workflow`: context reads, then each section's media, island and
copy decision; its checklist is the default anatomy and deviations are noted.
Fill the Proof ledger with the tiered review procedure
(`references/proof/reviews-sourcing.md`: connected reviews, collections,
intent search, the zero-review playbook, then legitimate substitutes) and the
Offer ledger when any discount, bundle, urgency or delivery promise exists.
Review the type checklist before presenting the plan.

Create or consume a concise one-page `page plan`. Ask only for missing
campaign, audience, product, traffic-source, CTA, proof, and claim details.
Use the packaged consumer-behavior reference to classify visitor mode, write
the top three shopper decision questions, and select at most three relevant
patterns. Inspect gallery coverage before asking about custom imagery; name
the exact missing image jobs and placements.
Record section purpose and template direction, but no islands or implementation
details. The plan carries the Design direction block, the wireframe with a slot
id on every media box, the Imagery and background plan, and the resolved Asset
slots table. Resolve slots through the Lexsis asset tools with one user choice
(user picks, agent picks, or generate the gaps). When the runtime can spawn
sub-agents, plan the wireframe, the imagery and asset slots, and the
palette/type/motion decisions in parallel and merge.

## Design

Re-read the plan's page-type file and compare its checklist with the
plan's deviation list, and an unexplained deviation is a question, not a stop. Render proof only
from the Proof ledger (linked press logos, real counts, verbatim quotes) and
offers only from the Offer ledger. Generate imagery only for ALLOW purposes in
`references/assets/generation-policy.md`. Copy follows the plan's framework
and `references/anti-patterns/copy-anti-patterns.md`; review the persisted
source and hosted page against those requirements.

Read the design skill's packaged `references/design-rules.md`; house rules
override generated brand guidance and preview blueprints. Apply the plan's
Design direction and any `Preset:` ids from its packaged
`references/island-presets.md`. Confirm only the asset
slots the plan left `planned`; verified slots are final. Prefer Lexsis
generation; offer other available image tools before using them. Create the
hosted draft first. For production-ready approval, inspect hosted
screenshots at 390 and 1280 and record the result in `QA record`.

If the user asked for a visual concept, follow the design skill's
`design-concepts.md`: generate mobile first, show it for approval, adapt it to
desktop, and then generate only the real production asset gaps. Never use the
concept image itself as page media.

Load the selected theme, adapt template source, choose and resolve islands,
use LX tokens and compile-time Tailwind utilities, and write
`MCP source` plus `theme_css`. Compile once and create one
unpublished hosted draft. Do not create a local renderer or use placeholder
assets.

## Generate

Reuse the draft created by design when its page ID is present. Otherwise
compile the current source values once and create with `publish:false`.
Surface `DRAFT_CREATED` immediately, then run deeper synchronization and
hosted QA when the inferred intent calls for production readiness.

Record page ID, version, preview URL, bundle hash, and section hashes. Verify
390px, 768px, and 1280px layouts plus the expected variant, cart opening,
quantity, and subtotal before returning `DRAFT_READY`.

## Fast Build

Resolve a supplied page kit or choose a coherent kit from intent, hydrate its
sections, adapt current products and brand tokens, compile once with at most
one targeted repair, and create with `publish:false`. Return the preview as
`DRAFT_CREATED` without blocking on critique, screenshots, commerce QA, or hash
reconciliation.

## Editing

Change editable source first. Stop on version drift, compile the complete page,
patch only changed sections with `expected_version`, and update recorded version
and hashes only after success.

Never patch compiled output in place of editable source and never publish without the
user's separate approval for the identified page version.

---
name: plan-page
description: "Plan one storefront page from strategy through final copy, section order, proof, offers, template direction, responsive layout, and production asset requirements. Stops at an approved execution-ready specification."
---

# Plan a Storefront Page

Produce the complete specification that later skills visualize, resource, and
design. Finalize the strategy and customer-facing copy here. Do not choose
islands, author code, create drafts, or produce assets.

## Read Only What Applies

Always read:

- `work/storefront/setup.md`;
- the selected store's `brand.md`, `design.md`, `products.md`, `persona.md`,
  `rules.md`, and default theme CSS;
- `references/plan-page.md`;
- `references/page-type-guide.md`;
- `references/planning-rules.md`.

These three references are the complete planning packet. General setup
context is a map, not live commerce authority.

Use:

- `lexsis_catalog.list` and `lexsis_catalog.get` to refresh selected products;
- `lexsis_catalog.reviews_status`, `lexsis_catalog.review_collections`,
  `lexsis_catalog.reviews`, and `lexsis_catalog.reviews_search` for proof;
- `lexsis_template_library.search_page_kits`,
  `lexsis_template_library.search_sections`, and
  `lexsis_template_library.get_kit` after sections are planned;
- `lexsis_capture.funnel_templates` and
  `lexsis_capture.funnel_template` for quiz or lead-capture structures.

Resolve unfamiliar schemas through exact router/action discovery. Use
authoritative web research for public facts and ask the user about private
merchant decisions, unclear positioning, intended campaign messaging, or
conflicting evidence. Record the source and date for researched facts.

## 1. Establish the Brief

Identify:

- workspace, store, and default working theme;
- requested page and page type;
- product, collection, or whole-store scope;
- target market and persona;
- traffic source and supplied campaign message;
- funnel stage and awareness;
- conversion goal and CTA destination;
- offer, purchase model, dates, and regions;
- proof, claims, legal constraints, and mandatory sections.

If the request is empty or incomplete, ask every material question needed to
make these decisions. There is no fixed question limit. Group related
questions so the user can answer efficiently. Do not ask for facts already
available in setup, the catalog, or reliable public sources.

Stop with `PLAN_BLOCKED` when a missing choice or evidence would materially
change the page. Lesser uncertainties remain labelled in `## Open decisions`.

## 2. Refresh Live Context

Find likely products in `products.md`, then refresh every selected product
with the live catalog. Capture exact ids, variants, options, prices,
availability, selling plans, descriptions, and product-media jobs.

Read review availability before planning proof. Verify public policy,
occasion, certification, shipping, returns, and claim facts from authoritative
sources when they are not available through Lexsis. Merchant-controlled
conflicts return to the user.

For a supplied campaign message or creative, extract its promise, nouns, CTA,
tone, claims, and visual cues from the material the user supplied. Do not
invent a campaign context.

## 3. Identify One Page Type

Walk `references/page-type-guide.md` before template search. Select exactly
one type using traffic, stage, awareness, desired action, product count,
offer, and campaign trigger.

Use the guide's default anatomy as the starting point. Record every mandatory section
omitted and every deviation with a reason. Review the checklist before
presenting the plan.

## 4. Build the Consumer Narrative

Use the Consumer decision model to list the shopper's top decision questions,
concerns, objections, proof needs, and mobile context. Turn them into an
ordered section narrative:

1. establish relevance and message match;
2. explain the product or mechanism;
3. resolve the largest objections;
4. place proof beside the claim it supports;
5. present the offer and risk reversal;
6. close with one clear action.

Sections are decided before templates. Each section must have a distinct
consumer job; merge or remove sections that repeat the same job.

## 5. Finalize Copy, Proof, and Layout

Write the final customer-facing content for every section:

- eyebrow, headline, subhead, body, labels, bullets, CTA, and destination;
- FAQ questions and complete answers where applicable;
- exact offer terms and policy language;
- proof and claim ids;
- desktop and mobile layout intent;
- interaction intent described as shopper behaviour, never implementation.

No placeholders, writing instructions, draft options, or `TBD` values may
remain. Every number, timeframe, quote, badge, certification, price, or
guarantee must resolve through the Proof ledger, Offer ledger, or Claim gate.

## 6. Define Production Asset Requirements

Define what each section needs; leave sourcing and production to
`/plan-assets`.

For every slot specify:

- section and consumer job;
- product or variant identity;
- real-only, editable-real, or generation-permitted status;
- mobile aspect ratio, crop, focal point, and minimum pixel dimensions first;
- larger-screen aspect ratio, crop, minimum pixel dimensions, and whether it
  derives from the same master;
- subject, composition, focal point, quiet zone, palette, and neighbouring
  section fit;
- evidence, rights, or provenance requirements;
- optional concept-frame reference when `/visualize-page` is later used.

Requirements may cite real Shopify media already identified through the
catalog, but they do not select library assets, upload files, import URLs,
generate images, spend credits, or declare production assets ready.

Official marks, certifications, press logos, customer proof, results imagery,
packaging identity, and exact product appearance always require genuine
authorized media.

## 7. Choose Template Direction

Search templates only after the section requirements are complete.

1. Search page kits for the selected type, vertical, mood, and objective.
2. When selection UI is available, let the user select and wait for the
   selection response.
3. Without selection UI, follow the user's delegation:
   - present the strongest candidates when they want to choose;
   - choose the best fit and explain why when they delegate the choice.
4. Resolve a selected kit with `lexsis_template_library.get_kit`.
5. If no page kit fits, search sections only for the specific planned
   sections that need a reusable direction.
6. If the shelf is empty or every candidate conflicts with the plan, record a
   custom layout direction. `/design-page` will author it.

Template direction never changes the consumer narrative merely to fit an
available template.

## 8. Produce and Approve the Plan

Write every block in `references/plan-page.md` in its defined order. The
result contains:

- complete strategy and consumer decisions;
- final copy;
- ordered sections and responsive layout;
- proof, offer, message-match, and claim decisions;
- template or custom direction;
- production asset requirements;
- open decisions and status.

Present a compact summary with page type, audience, goal, offer, section
count, asset-requirement count, proof/claim risks, and template direction.
Revise until the user approves.

Status rules:

- `PLAN_BLOCKED`: a material strategy, copy, offer, proof, claim, product, or
  CTA decision is unresolved;
- `PLAN_READY_FOR_APPROVAL`: the specification is complete and awaits the
  user's explicit approval;
- `PLAN_APPROVED <who> <date>`: the user explicitly approved this exact plan.

Plan approval does not authorize asset spending, draft creation, or
publication.

## Return

Return the complete plan, binding, status, and next route:

- optional `/visualize-page` when the user wants concept approval;
- `/plan-assets` to resolve production media;
- back to `/plan-page` whenever a visual or asset decision changes strategy,
  sections, claims, or final copy.

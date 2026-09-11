---
name: generate
description: Create an unpublished Lexsis storefront draft early, then synchronize and QA it to production readiness when the user's intent calls for deeper verification.
---

# Generate the Draft

Create a remote draft directly from editable source. Draft creation is
reversible; publishing remains a separate explicit action.

Read:

- `references/workflow-intent.md`
- `references/source-and-sync.md`
- `references/animation-system.md` when source contains or requires motion
- `references/consumer-behavior-cro.md` when planning or design was skipped
- `references/page-editing.md` only for an existing page
- `references/merchant-templates.md` only when reusing a merchant template
- `references/qa-recipe.md` for production-ready QA
- `references/authoring/css-and-styling.md` and
  `references/authoring/source-authoring.md` when repairing source
- the plan's `references/page-types/<type>.md` and
  `references/proof/proof-ledger.md` for the production gate
- `references/anti-patterns/copy-anti-patterns.md`,
  `references/anti-patterns/dark-patterns.md` and
  `references/anti-patterns/mobile-anti-patterns.md` for hosted QA

Use `lexsis_catalog.get`, `lexsis_design.island_schema`,
`lexsis_pages.compile`, `lexsis_pages.edit_context`,
`lexsis_pages.source`, `lexsis_pages.integrity`, and
`lexsis_page_create.create`.

## Infer the Outcome

Infer intent from the whole request and conversation using
`references/workflow-intent.md`; do not require a trigger phrase.

- `fast-draft` is the default for reversible ambiguity and requests to create,
  try, preview, explore, or iterate.
- `production-ready` applies when the user asks for final polish, exhaustive
  QA, campaign handoff, or launch preparation.
- `publish` routes to `/publish`; this skill never infers live-release
  approval.

State the inferred mode briefly and record compact evidence in `workflow`.
A request to create a draft authorizes one page-creation credit for the named
page. Intent inference never authorizes a duplicate page, paid asset
generation, publication, deletion, or destructive replacement.

## Inputs and Setup Reuse

Follow `references/source-artifact-workflow.md`: source and optional
`theme_css` are direct MCP values; editable source files are not required.
Reuse the confirmed workspace, store and theme binding in the page record
or current MCP context. Saved setup and campaign records are useful when
available. Do not call setup again when the binding is valid, and never switch
workspace, store or theme for an existing page.

Refresh only volatile creation data: selected products and variants, prices,
availability, permissions, active island schemas, and an existing page's
version. Never preserve a stale hardcoded Shopify variant ID when current
catalog data or a dynamic product binding can resolve it.

If `/plan-page` or `/design-page` was intentionally skipped, create the minimum
missing planning/evidence record, record the skip, and continue. Use
`references/consumer-behavior-cro.md` to record a minimum visitor mode, top
decision questions, at most two relevant patterns, gallery gaps, and primary
metric. Do not claim design approval that did not happen.

## Draft-Creation Gate

Before the first remote draft, require only:

- a valid saved store/theme binding and draft-write permission
- non-empty editable source, title and page handle; any required theme values
- current product/variant bindings with no known invalid hardcoded variant
- permanent assets rather than local URLs
- custom fonts backed by full HTTPS stylesheet URLs in `head.fonts`, or an
  intentional system-font stack
- a clean compiler result

Do not block first draft creation on critique screenshots, exhaustive hashes,
hosted responsive QA, commerce QA, or a `DRAFT_READY` validator result.

Optional design or QA guidance that cannot be read produces one warning and
does not block the draft. Missing source-format, binding or compile-contract
inputs remain blocking.

## Compile Directly

Pass the exact source, head, optional theme CSS and scripts to
`lexsis_pages.compile`. Use summary mode; do not request or echo the full
compiled bundle merely to inspect it. No workspace adapter, source file or
local QA step is part of this workflow.

If `remote.pageId`, `remote.lastKnownVersion`, and `remote.previewUrl` already
exist, fetch the current edit context and reuse that draft. Do not call
`lexsis_page_create.create` again. Compile only when inputs changed, then
patch the existing draft with expected-version protection.

When no remote draft exists, compile once from the current source values.
Immediately pass the returned `compile_id` and creation metadata to
`lexsis_page_create.create` with `publish:false`.

If a compile ID expires before creation, recompile the same verified inputs
once. If the client cannot reuse the ID, create with the exact source, head,
optional theme CSS and scripts. Never send source fields alongside a
`compile_id`. Expiry is not a reason to repeat
planning, critique, asset search, or approval.

## Return or Reuse the Reversible Draft

As soon as creation succeeds, or after an existing draft is confirmed current:

1. Record page ID, version, preview URL, input hashes and compile bundle hash.
2. Set manifest `status` to `draft_created` and QA to `pending`.
3. Confirm the returned binding, page id, version and preview URL.
4. Surface the preview immediately as `DRAFT_CREATED`.

Do not delete, replace, or conceal a working draft because later QA finds an
issue.

## Production-Ready Follow-Through

After the preview exists, continue best-effort verification unless the user
asked to stop at a first draft.

For `production-ready`, or when upgrading an existing `DRAFT_CREATED`:

1. Fetch persisted source, bundle, and version evidence.
2. Reject drift between the reviewed source/bundle and persisted version;
   reconcile from current MCP source before repairing.
3. Review the page's imagery as one campaign, not merely as individually valid
   assets.
4. Run hosted QA at 390px, 768px, and 1280px.
5. Verify typography, media, hydration, overflow, responsive geometry,
   expected Shopify variant, cart opening, quantity, subtotal, Quick Add,
   product-grid stability, thumbnails, and authored header/footer order.
6. Review the type checklist, proof/offer ledgers and house rules against
   the persisted source and hosted draft under `references/qa-recipe.md`.
   Proof and offer findings (a proof element outside the Proof ledger, an
   offer element outside the Offer ledger, a dark-pattern hit) block; type
   deviations and copy findings are review notes unless the plan did not
   record them. Check the 390px first screen against the type file's
   "Above the fold" list and every numeral in proof sections against the
   ledger.
7. Record evidence and blockers with the tested page id and version.
8. Set `status: qa_passed` only when all blocking checks pass for the same
   live version and hashes. Read/write supported QA evidence through MCP.

Return `DRAFT_READY` only after synchronization and every blocking QA check
passes. Otherwise return the existing `DRAFT_CREATED` with specific blockers
and the next repair action.

## Later Edits

Fetch edit context and stop on unexpected version drift. Change editable source
first, compile changed inputs once, patch only changed sections with
`expected_version`, and update synchronization state only after success.

## Return

Always return page ID, version, preview URL, inferred intent mode and current
state: `DRAFT_CREATED` or `DRAFT_READY`. Include hosted QA evidence when attempted.

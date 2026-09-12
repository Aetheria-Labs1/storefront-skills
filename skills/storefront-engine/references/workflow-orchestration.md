# Storefront Workflow

Use one owning command at a time.

## Normal Page Journey

```text
/setup
  U+2192 /plan-page
  U+2192 /design-page
  U+2192 /publish
```

- Setup is normally run once and refreshed only for changed stores/themes.
- Plan produces the complete page specification: strategy, final section
  copy, an asset decision for every section, claim gate, work queue and plan
  status, without islands. It waits for explicit approval.
- Design builds the approved plan: selects islands, resolves the plan's asset
  decisions, compiles source, creates one unpublished hosted draft, runs
  hosted QA at 390, 768 and 1280 with commerce checks, applies later edits
  with version protection, and returns `DESIGN_APPROVED`.
- Publish is a separate explicit release that gates on `DESIGN_APPROVED` for
  the same version.

Commands do not silently invoke one another. When a user intentionally starts
later, recover the minimum missing decision evidence and record the skipped command.

Infer question depth and publish intent from the user's complete request and
current conversation. Approval before design and before publish is never
inferred. Intent inference never authorizes publishing, paid generation, or
deletion.

## Optional Routes

- Use `/design-page` concept-first when the user wants a mobile-first mockup
  approved before source authoring.
- Use `/optimize` for an existing page and a specific outcome: it scores the
  page, proposes a plan with the same blocks, and applies approved changes.
- Use `/ab-test` to inspect a live Lexsis URL, build controlled variants, and
  create or evaluate an experiment.
- Use `/cart` for cart profile configuration.

## Shared Safety

- Identify one page type (`references/page-types/_index.md`) before templates,
  assets or proof; its `## Workflow` guides every later stage and its checklist
  is the default anatomy.
- Render proof only from the plan's Proof ledger and offers only from its
  Offer ledger; never invent reviews, counts, logos, badges or urgency.
- Generate imagery only for ALLOW purposes in
  `references/assets/generation-policy.md`; never the product, people as
  customers, results, badges or text in images.
- Bind every page to one saved store/theme pair.
- Read changing product, price, asset, schema, permission, analytics, and
  version data live.
- Search existing assets before paid generation.
- Resolve island schemas before authoring.
- Keep production changes in source-based MCP operations and stop on version drift.
- Create drafts with `publish:false`.
- Keep concept images out of production source and asset slots.
- Publish only after current QA and explicit approval.

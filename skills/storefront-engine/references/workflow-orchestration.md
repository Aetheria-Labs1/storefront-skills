# Storefront Workflow

Use one owning command at a time.

## Normal Page Journey

```text
/setup
  → /plan-page
  → /design-page
  → /generate
  → /publish
```

- Setup is normally run once and refreshed only for changed stores/themes.
- Plan defines a concise campaign and section strategy without islands.
- Design selects islands, resolves page assets, compiles source, and creates
  one unpublished hosted draft.
- Generate reuses that draft when present, then owns synchronization and
  production-ready hosted QA.
- Publish is a separate explicit release.

Commands do not silently invoke one another. When a user intentionally starts
later, create the minimum missing artifact and record the skipped command.

Infer `fast-draft`, `production-ready`, or `publish` from the user's complete
request and current conversation. Reversible ambiguity defaults to
`fast-draft`; consequential ambiguity still requires clarification. Intent
inference never authorizes publishing, paid generation, or deletion.

## Optional Routes

- Use `/analyze-page` before planning when a URL, screenshot, or ad matters.
- Use `/asset-prep` independently for standalone or replacement asset work.
- Use `/design-page` concept-first when the user wants a mobile-first mockup
  approved before source authoring.
- Use `/build` for the fastest unpublished draft from a prompt or an
  automatically selected page kit.
- Use `/build-with-template` when the user already supplied the page-kit or
  section-template URL.
- Use `/optimize` for an existing page and a specific outcome.
- Use `/ab-test` to inspect a live Lexsis URL, build controlled variants, and
  create or evaluate an experiment.
- Use `/cart` for cart profile configuration.

## Shared Safety

- Bind every page to one saved store/theme pair.
- Read changing product, price, asset, schema, permission, analytics, and
  version data live.
- Search existing assets before paid generation.
- Resolve island schemas before authoring.
- Keep production changes local-first and stop on version drift.
- Create drafts with `publish:false`.
- Keep concept images out of production source and asset slots.
- Limit fast-build compilation to one initial attempt and one targeted repair.
- Publish only after current QA and explicit approval.

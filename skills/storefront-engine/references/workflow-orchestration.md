# Storefront Workflow

Use one owning command at a time.

## Normal Page Journey

```text
/setup
  → /plan-page
  → /visual-page
  → /asset-prep
  → /generate
  → /publish
```

- Setup is normally run once and refreshed only for changed stores/themes.
- Plan defines the campaign and page strategy.
- Visual creates the responsive mockup and interactive island preview.
- Asset prep replaces all temporary media.
- Generate owns production source, draft creation, and hosted QA.
- Publish is a separate explicit release.

Commands do not silently invoke one another. When a user intentionally starts
later, create the minimum missing artifact and record the skipped command.

## Optional Routes

- Use `/analyze-page` before planning when a URL, screenshot, or ad matters.
- Use `/optimize` for an existing page and a specific outcome.
- Use `/experiment` for a measurable hypothesis.
- Use `/cart` for cart profile configuration.

## Shared Safety

- Bind every page to one saved store/theme pair.
- Read changing product, price, asset, schema, permission, analytics, and
  version data live.
- Search existing assets before paid generation.
- Resolve island schemas before authoring.
- Keep production changes local-first and stop on version drift.
- Create drafts with `publish:false`.
- Publish only after current QA and explicit approval.

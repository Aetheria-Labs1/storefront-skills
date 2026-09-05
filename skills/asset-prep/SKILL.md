---
name: asset-prep
description: Independently search, generate, import, or replace storefront media. Works from an asset brief or an existing page workspace and is not a required page-generation stage.
---

# Prepare Assets

Use this skill for asset-only work. It does not require `/plan-page` or
`/design-page`, and other skills must not invoke it automatically.

Use `lexsis_asset_library.search`, `lexsis_catalog.list`,
`lexsis_catalog.get`, `lexsis_workspace.credits`,
`lexsis_drafts.asset_generate`, `lexsis_asset_upload.import`, and
`lexsis_assets.view`.

## Choose a Mode

### Standalone

Accept an asset brief containing the brand/store, roles, dimensions, crops,
style, and intended use. Search, generate, import, and verify the requested
media. Save results under `work/storefront-assets/<brief-name>/asset-manifest.json`.

### Existing Page

Read the page source and compact manifest. Work only on the requested missing,
placeholder, or replacement roles. Do not redesign unrelated sections.

## Source Order

For each role:

1. Search existing Lexsis assets.
2. Use real Shopify product media for product identity.
3. Ask before spending generation credits.
4. Prefer Lexsis generation. If another image-generation tool is available,
   offer it as an explicit provider choice.
5. Import external-tool results into Lexsis.
6. Inspect the final asset and verify identity-sensitive imagery.

Use supported icons, SVG, or CSS for ordinary interface icons. Do not generate
raster UI icons unless the brief explicitly requires custom artwork.

## Page Updates

When working on a page:

- replace the asset in `lexsis-source.html`
- store only the final binding in `page-manifest.json`
- recompile once after all requested assets are updated
- regenerate `page-preview.html`
- set `design.status` to `changes-pending-approval` for visible changes

Do not create a second HTML source. Placeholders may remain for local preview,
but `/generate` rejects them.

## Asset Record

Keep the machine record compact:

```json
{
  "role": "hero",
  "sectionId": "hero",
  "sourceType": "lexsis",
  "assetId": "...",
  "url": "https://...",
  "status": "verified"
}
```

Shopify media uses `productId` and `mediaId`. Put crop guidance, alt-text
intent, prompt history, and creative reasoning in the brief or plan, not the
page manifest.

## Return

Return the final asset paths or bindings, provider used, verification result,
and any unresolved roles.

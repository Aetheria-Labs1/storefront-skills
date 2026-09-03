---
name: asset-prep
description: Replace visual-page placeholders with verified production images and video. Searches Lexsis and Shopify first, then generates or imports only what is still missing.
---

# Prepare Page Assets

Use the approved plan and visual mockup to finalize media. Do not author the
production page or create a draft.

Read the page's saved store/theme binding. Stop if it does not match
`work/storefront/setup/setup.json`; never run setup automatically.

## Source Order

For each asset role:

1. Search `lexsis_asset_library`.
2. For product media, use the real Shopify media from `lexsis_catalog`.
3. If a non-product image is still missing, check credits and use
   `lexsis_drafts` action `asset_generate`.
4. If an external tool supplies media, persist it through
   `lexsis_asset_upload` action `import`.
5. Inspect the final asset with `lexsis_assets` action `view`.

Pass the selected workspace and theme IDs whenever the current action schema
supports them. Never generate product pack shots or infer identity from a file
name. Creator and product imagery must be visually verified.

## Update the Mockup

Replace every `preview-placeholder` asset in the page workspace and manifest
with a permanent Lexsis or Shopify asset. Regenerate `visual-preview.html` so
the approved composition can be checked with final media.

Every manifest asset records:

```json
{
  "role": "hero",
  "sectionId": "hero",
  "sourceType": "lexsis",
  "assetId": "...",
  "url": "https://...",
  "width": 1600,
  "height": 1200,
  "desktopCrop": "center",
  "mobileCrop": "center top",
  "altTextIntent": "Product beside a glass",
  "verificationStatus": "verified"
}
```

Shopify media uses `productId` and `mediaId` instead of `assetId`.

## Gate

Before completion, confirm:

- no bundled placeholder remains
- every URL is permanent
- desktop and mobile crops work
- identity-sensitive media was visually verified
- generated media does not make unsupported product claims

## Return

Update `page-manifest.json` and return `ASSETS_READY` with the verified roles,
IDs, URLs, dimensions, crops, and alt-text intent. The next normal command is
`/generate`.

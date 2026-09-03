---
name: setup
description: Connect a Lexsis storefront workspace and save reusable brand and theme design context. Run once initially, then only to add or refresh a store or theme.
---

# Set Up Lexsis

Run this once after installing the Lexsis MCP and skills. It saves the
slow-changing context that page skills reuse; it does not create or edit pages.

## What to Save

1. Use `lexsis_discover` for unfamiliar setup actions and their current
   arguments.
2. Resolve the authorized workspace and connected stores.
3. When several stores or themes exist, ask the user which ones to save and
   which store/theme should be the default. Show names, not raw IDs.
4. For each selected store, read the brand kit, design guide, voice, and
   navigation. For each selected theme, read its exact theme CSS.
5. Write:

```text
work/storefront/setup/
├── setup.json
└── stores/
    └── <store-id>/
        ├── brand-design.md
        └── themes/
            └── <theme-id>.css
```

`setup.json` indexes every saved store/theme pair and identifies one default:

```json
{
  "schemaVersion": 1,
  "workspaceId": "...",
  "defaultStoreId": "...",
  "defaultThemeId": "...",
  "stores": [
    {
      "storeId": "...",
      "storeName": "Main Store",
      "brandDesignPath": "stores/<store-id>/brand-design.md",
      "themes": [
        {
          "themeId": "...",
          "themeName": "Light",
          "themeCssPath": "stores/<store-id>/themes/<theme-id>.css"
        }
      ]
    }
  ]
}
```

The default theme must belong to the default store. Adding a theme must not
replace another theme's CSS or another store's design file.

## Reuse

If a requested store/theme is already saved, reuse it. Refresh only when the
user asks, adds a store/theme, or Lexsis reports that the saved binding is no
longer valid.

Do not cache changing commerce or operational data. Page skills still read
current products, variants, prices, assets, island schemas, permissions,
credits, analytics, and remote page versions from Lexsis.

Never save credentials, cookies, authorization headers, or tokens.

## Return

Return the setup path, saved store/theme names, and default selection. Other
skills read this setup independently and never invoke `/setup` automatically.

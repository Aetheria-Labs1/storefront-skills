---
name: setup
description: Connect one or more Lexsis storefront workspaces and save reusable brand and theme design context per workspace, store and theme. Run once initially, then to add, switch or refresh a workspace, store or theme.
---

# Set Up Lexsis

Run this once after installing the Lexsis MCP and skills. It saves the
slow-changing context that page skills reuse; it does not create or edit pages.

Use exact action slots for setup: `lexsis_workspace.list`,
`lexsis_workspace.stores`, `lexsis_brand.context`,
`lexsis_brand.brand_kit`, `lexsis_brand.list_themes`,
`lexsis_brand.get_theme`, `lexsis_brand.navigation`, and
`lexsis_design.guide`. When an input schema is unfamiliar, call
`lexsis_discover` with its exact `router` and `action`. Never use a prose query
for these known actions. An empty discovery result is not a connection
failure; the real domain call determines whether the operation is available.

## What to Save

1. Resolve only unfamiliar schemas through exact router/action discovery.
2. Call `lexsis_workspace.list` for every authorized workspace, then
   `lexsis_workspace.stores` per workspace for its connected stores, then
   `lexsis_brand.list_themes` per store. An agency or multi-brand account
   commonly has several workspaces, each with its own stores and themes.
3. Show the tree by name, never raw ids, and ask which workspaces, stores and
   themes to save and which of each should be the default. Saving one
   workspace now does not prevent adding another later. When only one
   workspace, store or theme exists, save it and say so instead of asking.
4. For each selected store, read the brand kit, design guide, voice, and
   navigation. For each selected theme, read its exact theme CSS.
5. Write one file per saved artefact, namespaced by workspace so two
   workspaces can hold a store with the same name:

```text
work/storefront/setup/
+-- setup.json
+-- workspaces/
    +-- <workspace-id>/
        +-- stores/
            +-- <store-id>/
                +-- brand-design.md
                +-- themes/
                    +-- <theme-id>.css
```

`setup.json` indexes every saved workspace, store and theme, and names one
default at each level:

```json
{
  "schemaVersion": 2,
  "defaultWorkspaceId": "...",
  "workspaces": [
    {
      "workspaceId": "...",
      "workspaceName": "Acme Brands",
      "defaultStoreId": "...",
      "defaultThemeId": "...",
      "stores": [
        {
          "storeId": "...",
          "storeName": "Main Store",
          "storeDomain": "acme.myshopify.com",
          "brandDesignPath": "workspaces/<workspace-id>/stores/<store-id>/brand-design.md",
          "themes": [
            {
              "themeId": "...",
              "themeName": "Light",
              "themeCssPath": "workspaces/<workspace-id>/stores/<store-id>/themes/<theme-id>.css"
            }
          ]
        }
      ]
    }
  ]
}
```

Rules for the index:

- `defaultWorkspaceId` names a saved workspace; each workspace's
  `defaultStoreId` names one of its own stores and `defaultThemeId` one of
  that store's themes. A default never points across workspaces.
- Paths are relative to `setup.json` and unique per workspace, store and
  theme. Adding a theme never overwrites another theme's CSS, another store's
  design file, or another workspace's tree.
- Schema 1 (a single flat `workspaceId` with `stores[]` at the root) is still
  readable. When a schema-1 file is found and the user adds a second
  workspace, migrate it: move `stores/` under
  `workspaces/<workspace-id>/stores/`, wrap the existing entry in
  `workspaces[]`, set `schemaVersion: 2` and `defaultWorkspaceId`, and update
  every `brandDesignPath` and `themeCssPath`. Say that the migration happened.

## Switching Workspace, Store or Theme

A page binds exactly one workspace, store and theme, recorded in its manifest
as `workspaceId`, `storeId` and `themeId`, and it never silently changes.

- When the user names a workspace, store or theme, resolve it by name from
  `setup.json` and use it. An ambiguous name (the same store name in two
  workspaces) is disambiguated by asking, showing the workspace for each.
- When the user names nothing, use the defaults, and state which workspace,
  store and theme are in effect in one line so a wrong default is visible
  immediately.
- Switching mid-campaign is a new binding, not an edit: a page already bound
  to one store keeps that binding, and a page for the other store belongs to
  its own campaign/page decision record. Never combine design
  files or theme CSS from two themes, stores or workspaces on one page.
- `/setup` can be re-run to add a workspace, store or theme, or to change a
  default, without touching what is already saved.

## Reuse

If a requested workspace, store or theme is already saved, reuse it. Refresh
only when the user asks, adds one, or Lexsis reports that the saved binding is
no longer valid.

Do not cache changing commerce or operational data. Page skills still read
current products, variants, prices, assets, island schemas, permissions,
credits, analytics, and remote page versions from Lexsis.

Never save credentials, cookies, authorization headers, or tokens.

## Return

Return the setup path, the saved tree as workspace then store then theme names,
the default at each level, MCP status, discovered capabilities, actions called,
fallbacks, and blockers. Say whether a schema-1 file was migrated. Other skills
read this setup independently and never invoke `/setup` automatically.

# Storefront Publishing & Lifecycle

Manage page publishing, previews, and lifecycle.

## Publish Flow

1. `compile_page_source` — compile and validate the generated source
2. `create_page_from_source` — persist the initial draft
   - `publish: false` → preview URL only (not live on store)
3. `publish_page` — go live only after explicit approval

## Operations

### Create Draft (New Page)
```
compile_page_source({ source, head, theme_css, scripts })
create_page_from_source({ source, head, theme_css, scripts, slug, publish: false })
```
Returns: page_id, page_url, preview_url

### Preview (Draft)
```
create_page_from_source({ source, head, theme_css, scripts, slug, publish: false })
```
Returns: preview_url (not visible to store visitors)

### Publish Existing Page
```
publish_page(page_id)
```
Makes a draft page live.

### Unpublish
```
unpublish_page(page_id)
```
Takes page offline but preserves it in DB.

### Duplicate
```
duplicate_page(page_id, { title: "New Title" })
```
Creates a copy — useful for A/B test variants.

### Create Experiment Variant
```
create_page_variation(page_id, { changes: {...} })
```
Creates variant for A/B testing.

## Prerequisites

- Store must be connected (`get_connected_stores`)
- Brand kit should exist for proper theming

## Post-Publish

After publishing, the page is served via:
- Shopify store (native page)
- pages.lexsis.app (standalone via edge worker)
- Custom domain (if tracking domain configured)

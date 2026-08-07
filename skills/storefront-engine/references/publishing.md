# Storefront Publishing & Lifecycle

Manage page publishing, previews, and lifecycle.

## Publish Flow

1. `validate_vibe_page` — always validate before publishing
2. `publish_vibe_page` — persist to DB + storage
   - `draft: true` → preview URL only (not live on store)
   - `draft: false` → live on Shopify store

## Operations

### Publish (New Page)
```
validate_vibe_page(page_data)
publish_vibe_page(page_data, { draft: false })
```
Returns: page_id, page_url, preview_url

### Preview (Draft)
```
publish_vibe_page(page_data, { draft: true })
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

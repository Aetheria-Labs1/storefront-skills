---
name: publish
description: QA a storefront page, create a draft preview, and publish live only after explicit user approval.
---

# Publish Storefront Page

QA a storefront page, validate structure and rendering, create a draft preview, and publish live only after explicit user approval.

## Context

- **qa-recipe**: 1. **Validate structure** — call `validate_vibe_page` on the generated JSON

## Workflow

# Storefront Publishing & Lifecycle

Manage page publishing, previews, and lifecycle.

## Publish Flow

1. `validate_vibe_page` — always validate before publishing
2. `publish_vibe_page` — create a draft preview first
   - `draft: true` → preview URL only (not live on store)
3. Confirm the user explicitly wants a live publish before any `draft: false` or `publish_page` call.

## Operations

### Draft Preview (New Page)
```
validate_vibe_page(page_data)
publish_vibe_page(page_data, { draft: true })
```
Returns: page_id and preview_url

### Preview (Draft)
```
publish_vibe_page(page_data, { draft: true })
```
Returns: preview_url (not visible to store visitors)

### Publish Live (Explicit Approval Required)
```
publish_page(page_id)
```
Only call this after the user explicitly says to publish live. Makes a draft page live.

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

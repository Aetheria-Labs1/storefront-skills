---
name: publish
description: QA a storefront page, create a draft preview, and publish live only after explicit user approval.
---

# Publish Storefront Page

QA a storefront page, validate structure and rendering, create a draft preview, and publish live only after explicit user approval.

## Context

- **qa-recipe**: compile source, create a draft, run integrity checks, then verify in a browser

## Workflow

# Storefront Publishing & Lifecycle

Manage page publishing, previews, and lifecycle.

## Publish Flow

1. `compile_page_source` — compile and validate the generated source
2. `create_page_from_source` — create a draft preview first
   - `publish: false` → preview URL only (not live on store)
3. Confirm the user explicitly wants a live publish before `publish_page`.

## Operations

### Draft Preview (New Page)
```
compile_page_source({ source, head, theme_css, scripts })
create_page_from_source({ source, head, theme_css, scripts, slug, publish: false })
```
Returns: page_id and preview_url

### Preview (Draft)
```
create_page_from_source({ source, head, theme_css, scripts, slug, publish: false })
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

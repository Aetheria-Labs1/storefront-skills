# Storefront Publishing & Lifecycle

Manage page publishing, previews, and lifecycle.

## Publish Flow

1. `lexsis_pages` action `compile`
2. `lexsis_page_create` action `create` with `publish:false`
3. `lexsis_pages` action `integrity`
4. Host-agent browser QA at 390px, 768px, and 1280px
5. `lexsis_live_ops` action `publish` after explicit approval

## Operations

### Create Draft (New Page)
```
lexsis_pages({ action: "compile", args: { source, head, theme_css, scripts } })
lexsis_page_create({ action: "create", args: { source, head, theme_css, scripts, slug, publish: false } })
```
Returns: page_id, page_url, preview_url

### Preview (Draft)
```
lexsis_page_create({ action: "create", args: { source, head, theme_css, scripts, slug, publish: false } })
```
Returns: preview_url (not visible to store visitors)

### Publish Existing Page
```
lexsis_live_ops({ action: "publish", args: { page_id } })
```
Promotes the exact reviewed version to `published_version_id`.

### Unpublish
```
lexsis_live_ops({ action: "unpublish", args: { page_id } })
```
Takes page offline but preserves it in DB.

### Duplicate
```
lexsis_drafts({ action: "page_duplicate", args: { page_id, title: "New Title" } })
```
Creates a copy — useful for A/B test variants.

### Create Experiment Variant
```
lexsis_drafts({ action: "page_variation", args: { page_id, changes: {...} } })
```
Creates variant for A/B testing.

## Prerequisites

- Resolve a connected store with `lexsis_workspace` action `stores`
- Require a valid selected/default theme from `lexsis_brand`

Edits to a published page remain draft-only until publish succeeds. A failed
republish keeps the prior public version live.

## Post-Publish

After publishing, the page is served via:
- Shopify store (native page)
- pages.lexsis.app (standalone via edge worker)
- Custom domain (if tracking domain configured)

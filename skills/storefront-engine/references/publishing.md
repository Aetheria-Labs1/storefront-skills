# Storefront Publishing & Lifecycle

Manage page publishing, previews, and lifecycle.

## Publish Flow

1. Require local artifacts from `source-artifact-workflow.md`
2. Confirm the page's saved store/theme binding
3. `lexsis_pages` action `compile`
4. `lexsis_page_create` action `create` with `publish:false`
5. Fetch persisted source/content and record matching local and remote hashes
6. `lexsis_pages` action `integrity`
7. Compare the compiled local preview and hosted draft at 390px, 768px, and
   1280px, then run commerce QA
8. Recheck remote version and local synchronization
9. `lexsis_live_ops` action `publish` after explicit approval

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

Use the experiment workflow for duplication and variants so each remote page
has its own local source and manifest first.

## Prerequisites

- The manifest's store and theme exist in the saved one-time setup
- Current permissions and store entitlement are read live
- Require `qa-report.md` with no blocking failures
- Require local source, page theme, remote bundle, and remote version to match
  the manifest baseline

Edits to a published page remain draft-only until publish succeeds. A failed
republish keeps the prior public version live.

## Post-Publish

After publishing, the page is served via:
- Shopify store (native page)
- pages.lexsis.app (standalone via edge worker)
- Custom domain (if tracking domain configured)

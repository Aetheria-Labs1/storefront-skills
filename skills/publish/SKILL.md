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

1. Require a `DRAFT_READY` page from `generate` or a validated update from
   `optimize`.
2. Read `lexsis_pages` action `edit_context` and confirm
   `has_unpublished_changes` when promoting an edited published page.
3. Confirm the preview has passed QA at 390px, 768px, and 1280px using the host
   agent's browser capability.
4. Confirm the user explicitly wants a live release.

## Operations

### Ready Draft Requirement

`generate` creates and validates draft previews. Do not recreate source or
compile it here. Require the page ID, preview URL, and completed visual QA
before release.

### Publish Live (Explicit Approval Required)
```json
{
  "name": "lexsis_live_ops",
  "arguments": {
    "action": "publish",
    "args": { "page_id": "page-uuid" }
  }
}
```
Only call this after explicit approval. A successful publish promotes the
reviewed current version to the immutable public `published_version_id`.
Failure preserves the previous live version.

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

- Resolve the store with `lexsis_workspace` action `stores`
- `lexsis_brand` action `list_themes` must return a valid selected/default theme
- Run `lexsis_pages` action `integrity` before publishing

## Post-Publish

After publishing, the page is served via:
- Shopify store (native page)
- pages.lexsis.app (standalone via edge worker)
- Custom domain (if tracking domain configured)

## Optional Follow-Up

This skill ends after release. Later, `experiment` can test a focused variant
or `optimize` can address performance evidence when the user requests it.

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
2. Confirm the preview has passed desktop and mobile QA.
3. Confirm the user explicitly wants a live release before `publish_page`.

## Operations

### Ready Draft Requirement

`generate` creates and validates draft previews. Do not recreate source or
compile it here. Require the page ID, preview URL, and completed visual QA
before release.

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

## Optional Follow-Up

This skill ends after release. Later, `experiment` can test a focused variant
or `optimize` can address performance evidence when the user requests it.

# Before Showing Draft to Merchant — QA Recipe

## Pre-flight Checklist

1. **Validate local artifacts** — run the shared page workspace validator
2. **Compile complete source** — `lexsis_pages` action `compile`
3. **Save as draft** — `lexsis_page_create` action `create` with `publish:false`
4. **Fetch and compare persisted source/content** — reject hash drift
5. **Check integrity** — `lexsis_pages` action `integrity`

## Browser QA (if available)

### Viewports to test:
- Mobile: 390px
- Tablet: 768px
- Desktop: 1280px

### Check for:
- [ ] No horizontal overflow at any viewport
- [ ] All images load (no broken/gray placeholders)
- [ ] Hero section visible above fold on both viewports
- [ ] Text readable without zooming on mobile
- [ ] Interactive islands respond to clicks (FAQ accordion, BuyBox variant selection)
- [ ] Expected Shopify variant enters the cart
- [ ] Cart opens and quantity/subtotal update
- [ ] Inherited header and footer are correct
- [ ] Full-page hosted screenshots match `visual-preview.html` at all three
      viewports
- [ ] Dynamic island regions preserve the approved container geometry and
      placement
- [ ] No console errors blocking render

Write the result to `qa-report.md`, including source hash, remote version, copy
lint, claims review, asset verification, blockers, and publish readiness.

## Common Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| Gray product cards | Missing `image`/`media` in product data | Add image URLs or use `productIds` for auto-fetch |
| FAQ items don't toggle | Missing island hydration script | Ensure page includes island runtime |
| 401 on publish | OAuth session expired or revoked | Reconnect the MCP and complete browser OAuth |
| Insufficient scope on publish | Connection has Read or Build access | Reauthorize with Publish access after user approval |
| Images too large/slow | Using original Shopify CDN URLs | Append `&width=800` to resize |

## Draft vs Live

- `publish: false` → draft at `/v/{slug}?shop={domain}&preview=1`
- `lexsis_page_create` is draft-only and rejects `publish:true`
- Publish later with `lexsis_live_ops` action `publish` after explicit approval
- Draft edits do not replace the public `published_version_id`

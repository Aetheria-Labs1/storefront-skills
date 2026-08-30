# Before Showing Draft to Merchant — QA Recipe

## Pre-flight Checklist

1. **Compile and validate source** — `lexsis_pages` action `compile`
2. **Save as draft** — `lexsis_page_create` action `create` with `publish:false`
3. **Check integrity** — `lexsis_pages` action `integrity`

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
- [ ] No console errors blocking render

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

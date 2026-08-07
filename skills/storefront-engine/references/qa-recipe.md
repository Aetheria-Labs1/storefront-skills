# Before Showing Draft to Merchant — QA Recipe

## Pre-flight Checklist

1. **Validate structure** — call `validate_vibe_page` on the generated JSON
2. **Save as draft** — call `publish_vibe_page` with `publish: false`
3. **Check integrity** — call `check_page_integrity` with the page's archetype

## Browser QA (if available)

### Viewports to test:
- Mobile: 390×844 (iPhone 14)
- Desktop: 1440×900

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
| 401 on publish | Using API key auth | Endpoint supports X-API-Key — ensure key is valid |
| Images too large/slow | Using original Shopify CDN URLs | Append `&width=800` to resize |

## Draft vs Live

- `publish: false` → draft at `/v/{slug}?shop={domain}&preview=1`
- `publish: true` → live page, edge-cached, visible to shoppers
- Always draft first, QA, then publish

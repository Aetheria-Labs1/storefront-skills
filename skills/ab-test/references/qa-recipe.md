# Hosted draft verification

Run by `/design-page`, `/quiz`, and `/optimize` Apply.

## Evidence gate

Follow `references/source-artifact-workflow.md`. There are no local QA steps,
page decision records or source-file prerequisites.

1. Check compiler results for the exact submitted inputs.
2. Reuse the existing unpublished draft, or create it once with `publish:false`.
3. Read persisted source, bundle and version through MCP; reconcile drift.
4. Run `lexsis_pages.integrity` and read `lexsis_pages.qa`.
5. Check the page-type contract, house rules and proof/offer evidence against
   that persisted source and the hosted draft. Type and copy findings are
   review notes; unsupported proof/offer content blocks readiness.

First drafts may be returned with QA pending. Production readiness requires
the hosted checks below; no browser access means no claimed visual pass.

## Browser QA (if available)

### Viewports to test:
- Mobile: 390px
- Tablet: 768px
- Desktop: 1280px

### Check for:

Apply commerce and component checks to controls actually present. A quiz does
not require a separate Quick Add drawer, sticky control, or product grid.

- [ ] No horizontal overflow at any viewport
- [ ] All images load (no broken/gray placeholders)
- [ ] Hero section visible above fold on both viewports
- [ ] Text readable without zooming on mobile
- [ ] Native disclosures and interactive islands respond to clicks (details, BuyBox selection)
- [ ] Expected Shopify variant enters the cart
- [ ] Cart opens and quantity/subtotal update
- [ ] Authored header and footer appear exactly once and in source order
- [ ] No renderer-injected shell or duplicate navigation is present
- [ ] Full-page hosted screenshots preserve the approved hierarchy and
      composition at all three viewports
- [ ] Dynamic island regions preserve the approved container geometry and
      placement
- [ ] Collection cards keep titles, prices, media, options, variants, and
      availability after hydration
- [ ] Quick Add is anchored to media top-right
- [ ] Desktop opens a right drawer and mobile opens a bottom sheet
- [ ] Sold-out variants are disabled; the chosen available variant is added
- [ ] Focus trap, Escape, and focus restoration work
- [ ] Product grids do not blank, flicker, restart media, or shift on hydration
- [ ] Asset thumbnails show visible media or actionable retry/unavailable state
- [ ] Functional-looking filter/sort controls work or are absent
- [ ] No console errors blocking render

Keep results with the hosted URL, source/bundle hash and tested version.
Record claims review, asset verification, screenshots, interaction evidence,
blockers and readiness. Save supported evidence with
`lexsis_drafts.page_record_qa` using its current schema; reread the QA record.

## Quiz checks

Follow `references/quiz-authoring.md` for reachable paths, ties/fallbacks,
unavailable variants, back/review/restart, keyboard focus, transitions, and
reduced motion. Preview is the design surface, not production capture proof.
After authorized activation and publication, verify saving/analytics consent
combinations, confirmed saving, edit/reload/retry, and retained Forms responses.
Record explicit pending checks when live proof is not yet available.

Use screenshots only as hosted review evidence or transient browser inspection;
do not create local JSON dumps, screenshot bundles, or ad hoc QA reports.

## Common Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| Gray product cards | Missing `image`/`media` in product data | Add image URLs or use `productIds` for auto-fetch |
| Native disclosure does not toggle | Broken details/summary markup or blocked input | Repair source and test keyboard/pointer input on the hosted draft |
| 401 on publish | OAuth session expired or revoked | Reconnect the MCP and complete browser OAuth |
| Insufficient scope on publish | Connection has Read or Build access | Reauthorize with Publish access after user approval |
| Images too large/slow | Using original Shopify CDN URLs | Use the supported image transformation for that URL; preserve its query parameters |

## Draft vs Live

- `publish: false` returns a draft `preview_url`; use that exact URL
- `lexsis_page_create` is draft-only and rejects `publish:true`
- Publish later with `lexsis_live_ops` action `publish` after explicit approval
- Draft edits do not replace the public `published_version_id`

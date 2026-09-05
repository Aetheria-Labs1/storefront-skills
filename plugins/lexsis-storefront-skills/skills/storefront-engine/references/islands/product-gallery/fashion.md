# ProductGallery — Fashion/Apparel

## Tone

- Show the garment on a model (not flat lay alone)
- Multiple angles: front, back, side, close-up fabric, styled outfit
- Include a "worn" context shot (street, studio, lifestyle)

## Layout Selection

- Default: `hero-thumbnails.json` (large main + vertical strip)
- For lookbooks: `editorial-asymmetric.json`
- Mobile: always horizontal scroll (swipe natural for fashion shoppers)

## Image Requirements

- Min 4 images per product: front, back, detail, model full-length
- Consistent model pose across color variants (compare easily)
- Aspect ratio: 3/4 (portrait, shows full outfit)
- Background: consistent (white studio OR contextual, never mixed)

## Prop Overrides

| Prop | Value | Why |
|------|-------|-----|
| layout | "vertical" (desktop) | Thumbnail strip for quick angle switching |
| enableZoom | true | Fabric detail inspection |
| aspectRatio | "3/4" | Portrait orientation for full-body |
| enableVideo | true | Show movement, drape, fit in motion |

## Companion Context

- Below gallery on mobile: "Model is 5'9\" wearing size M"
- Fabric zoom callout: "Pinch to zoom on fabric detail"
- Color variant: gallery updates when color swatch selected (island handles)

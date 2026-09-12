# Production Asset Guide

`/plan-assets` uses this guide to turn planned media jobs into permanent,
verified production assets. Search real sources first, choose capabilities
dynamically, preserve identity and rights, and persist every external output
in Lexsis before use.

## Capability Discovery

Inspect the current client's installed generation and editing tools. Build an
internal matrix for:

- text and reference-image generation;
- transparent output and background removal;
- inpainting, outpainting, cleanup, and upscaling;
- identity-preserving compositing;
- supported aspects, resolution, cost, and persistence.

Do not assume a provider exists because an example mentioned it. Honor the
user's available preferred capability; otherwise select by job. Lexsis
fallback uses `lexsis_assets.capabilities`, `lexsis_workspace.credits`, and
`lexsis_drafts.asset_generate`.

State the slots, operation count, and known cost before every paid batch and
obtain explicit approval.

## Source Order

1. Exact Shopify product and variant media.
2. Existing Lexsis library assets.
3. Merchant upload or supplied attachment/URL.
4. Authorized supplier or manufacturer source.
5. Licensed stock for eligible background/context jobs.
6. Policy-permitted generation or editing.

Every candidate is viewed in its intended mobile crop first and its
larger-screen crop second. Confirm identity, resolution, focal point, quiet
zone, palette, neighbouring-set fit, rights, watermarks, baked-in text, and
whether it truly performs the slot's consumer job before binding it.

## Responsive Output Order

1. Resolve the 390 mobile composition and crop.
2. Record the mobile aspect and minimum pixel dimensions.
3. Select, edit, or generate the mobile output first.
4. Derive the 768/1280 output from the same approved direction.
5. Reuse one master when art-directed crops are sufficient; otherwise produce
   a separate larger-screen output with the same subject, identity, scene,
   lighting, palette, and focal intent.

Full-width mobile imagery should normally be at least 1080px wide. Other
mobile slots should target roughly 2x their maximum rendered CSS dimensions.
Full-width desktop imagery should be at least 1600px wide and preferably
1920px when the source supports it. These are source-quality targets, not
instructions to render images at those CSS dimensions.

## Import and Upload

| Operation | Use |
|---|---|
| `lexsis_asset_library.search` | Search existing assets by theme, role, tags, semantics, filename, OCR, or similarity |
| `lexsis_assets.view` | Inspect a candidate or output |
| `lexsis_asset_import.import` | Import exactly one supplied source: URL, image data with MIME type, or conversation attachments |
| `lexsis_asset_upload.upload` | Open the local image/video upload UI |

Import never opens upload UI. Upload is complete only after the user's
uploaded-asset response. Without inline upload UI, request a URL or
conversation attachment and import it.

External outputs must be imported before binding. Use the returned permanent
Lexsis asset id and URL, not a transient output URL.

Permanent Shopify media may use `https://cdn.shopify.com/`; persisted Lexsis
assets may use `https://cdn.trylexsis.com/`. Treat other remote output URLs as
transient until import returns a permanent Lexsis asset.

## Production Recipes

### Transparent Product Cutout

- Start with real, identity-confirmed product media.
- Remove only the background.
- Preserve label, color, proportions, texture, edges, shadows intrinsic to the
  product, and all packaging details.
- Require true alpha transparency when the slot calls for it.
- Compare the output beside the source at full size.

### Background or Backdrop

- Generate or edit only the environment, surface, texture, or abstract field.
- Name the mobile aspect, pixel target, and focal point first; then name the
  larger-screen aspect, pixel target, and derivation.
- Reserve the planned quiet zone for HTML copy.
- Keep detail and contrast low beneath text.
- Exclude products, people, text, logos, badges, prices, and watermarks unless
  a separate approved real source is composited later.

### Real-Product Composite

- Use an approved real cutout as the identity layer.
- Generate or edit the scene separately.
- Composite without repainting identity-bearing product pixels.
- Match contact shadow, perspective, scale, and color temperature.
- Never add accessories, gifts, ingredients, or included items that could
  imply they ship with the product.

### Decorative Elements, Textures, and Patterns

- Use transparent or seamless output as required.
- Limit colors to the plan palette.
- Keep elements non-informational and `aria-hidden` in implementation.
- Avoid letters, marks, product silhouettes, and culturally specific symbols
  unless they are intentionally sourced and approved.

### Campaign or Editorial Imagery

- Follow the plan's persona, market, message, and visual direction.
- Use real product references whenever the product appears.
- Keep synthetic scenes clearly separate from customer proof or results.
- Record any required disclosure from the generation policy.

### Extension, Cleanup, and Upscaling

- Extension may add background around a real subject but not alter the
  subject.
- Cleanup removes dust, compression artifacts, or unwanted background items;
  it does not change product features.
- Upscaling must retain label legibility and edge fidelity.
- View the original and output together before acceptance.

## Real-Only and Official Media

Never generate or fabricate:

- exact products, variants, packaging, labels, shades, fit, texture, scale, or
  included items;
- customers, reviewers, results, before/after evidence, founders, staff, or
  experts;
- press, payment, certification, trust, award, regulatory, or partner marks;
- quotations, ratings, counts, claims, signatures, or documents.

Official marks require issuer or publication artwork and a verified source.
Proof imagery requires the applicable evidence and rights record.

## Verification and Repair

Verify:

- identity and source integrity;
- mobile crop and pixels first, then larger-screen crop and pixels;
- dimensions, alpha, format, and resolution;
- palette and neighbouring-set consistency;
- quiet zone and text legibility;
- rights, provenance, and disclosure;
- absence of unintended text, marks, watermarks, or fabricated evidence.

One bounded repair is allowed when the defect and correction are specific.
After that, switch source/capability, request user input, revise the plan, or
mark the slot blocked.

## Record

Use the plan-assets binding and production tables. Do not create a separate
JSON manifest. A final binding records slot, source, permanent id/URL, crops,
rights, operation history, and verification status.

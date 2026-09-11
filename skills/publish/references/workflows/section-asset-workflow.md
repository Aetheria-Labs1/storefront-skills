# Section asset workflow

This is the single execution procedure for sourcing, missing-slot handling,
and visual fit. Type files provide jobs, tags, crops and budgets; policy
lives in `references/assets/asset-sourcing-sequence.md`,
`references/assets/generation-policy.md`, `references/assets/slot-spec.md`,
`references/assets/video-rules.md` and the relevant proof ledger.

## 1. Acquisition and missing-slot handling

1. Read the type's section job and budget. Decide whether imagery is needed;
   a native disclosure or factual table does not need a decorative image.
2. Inventory real catalogue media, the merchant's selections, and existing
   library assets before planning new media. Assign each candidate its actual
   job, product/variant, dimensions and rights evidence.
3. Follow the source eligibility order in
   `references/assets/asset-sourcing-sequence.md`. Use the type's search tags
   and queries. A missing tag is not proof that the library is empty.
4. Run the fit review in section 2 before binding a candidate. Retain rejection
   reasons so the same unsuitable image is not proposed repeatedly.
5. For a remaining slot, consult `references/assets/generation-policy.md`.
   That file owns ALLOW / ASK / NEVER, credit approval, identity protection,
   prompts and generation records. Do not infer permission from a page type.
6. Tell the merchant what is missing: section, job, aspect, count and why it
   matters. Offer **upload**, **generate** only where that policy permits it,
   or **skip/merge** with an explanation of what the page loses. Group gaps
   into one useful message, not a question for each section.
7. A fast draft may use the closest existing asset that honestly performs a
   suitable job, or leave the slot `planned`. Record all unresolved slots in
   the plan and draft summary. Do not silently remove a required section.
   Production readiness requires resolution of its required slots; an
   explicit type deviation still needs a reason and appropriate evidence.
8. Skip or merge a section only on the merchant's decision. A generation ban
   is not permission to invent media, substitute irrelevant stock, or hide
   the missing job behind a decorative band.

### Import, upload and selection

- `lexsis_asset_library.search` selects existing assets. With an empty query,
  wait for the `Design asset selection:` message when inline selection UI is
  available; map its selection order to the named slots.
- `lexsis_asset_import.import` persists an available URL, image base64 with
  MIME type, or conversation attachments. Supply exactly one source.
- `lexsis_asset_upload.upload` opens the local-file UI. Scope it to the
  selected workspace/theme and wait for the user's uploaded-asset message.
  Without inline UI, ask for a URL or conversation attachment and import it.
  Opening a panel is not an upload. The exact argument contract is in
  `references/lexsis-mcp-contract.md`.

### Search efficiently

Use the current search schema. Tags such as `hero`, `lifestyle`,
`product-shot`, `social-proof` and `logo` are conventions, not a closed enum.
Try semantic queries for missing jobs and filename lookup for a supplied
filename. Where supported, OCR search helps identify baked-in overlays and
similarity search around a verified seed helps maintain a coherent set.
Result geometry screens candidates before the visual review; metadata never
replaces inspection. Keep the selected workspace and theme binding explicit.

## 2. View and fit review

Nothing is used sight unseen. Open each candidate with `lexsis_assets.view`;
if the host cannot display it, inspect the returned permanent URL with the
available image viewer. Judge the asset **in its intended section**:

| Check | Required decision |
|---|---|
| Identity and job | Correct product/variant; the image actually demonstrates the assigned job |
| Crop | Desktop and mobile crops preserve the subject and required detail |
| Text placement | Copy has an appropriate quiet region, or moves outside the image; A7 still governs contrast |
| Set consistency | View adjacent/grid candidates together; they should read as one shoot rather than unrelated finds |
| Palette | The image works with the plan's visual direction without falsifying product appearance |
| Resolution | Detail survives at the actual mobile and desktop rendered sizes |
| Source integrity | Rights are recorded; no misleading overlay, watermark or competitor branding; genuine product labels remain readable where the job requires them |

A near-uniform preview can be a failed preview. Inspect the original URL
before rejecting the asset or spending credits on a replacement. Apply this
same review after generation; payment is not evidence of suitability. A
rejected generation returns to the policy's bounded repair/fallback route.

## 3. Asset budget and record

The type's budget records supplied jobs, missing jobs and type-specific
alternatives. It does not redefine source permissions. Assign each slot a
source decision, rights basis, final asset or Shopify media id, and status.
Use the workspace record defined in `references/page-files.md`; generation
records follow the generation-policy owner. Mark rejected or unresolved jobs
accurately even when a different verified image allows a reversible draft.

Example merchant message: "The kit has a packaging image but no image of
all included items. Supply one overhead kit photo, or choose to omit the
optional unboxing section; the included-items job is still pending."

## 4. Write to the resolved job

After the media decision, execute `references/workflows/copy-workflow.md`.
Do not invent benefit imagery or pad the copy because a requested image is
missing. A deliberately text-only section follows its type contract.

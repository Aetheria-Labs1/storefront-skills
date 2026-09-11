# Standalone asset operations

For page assets, execute `references/workflows/section-asset-workflow.md`.
For an asset-only request, accept the brand/store/theme binding, intended
role and delivery requirements without invoking page planning or design.
Eligibility and rights come from `references/assets/asset-sourcing-sequence.md`;
generation permissions come from `references/assets/generation-policy.md`.

## Import and upload mechanics

| Operation | Use |
|---|---|
| `lexsis_asset_library.search` | Find existing library assets; an empty query lets the user browse |
| `lexsis_assets.capabilities` | Discover current generation providers and capabilities |
| `lexsis_asset_import.import` | Import exactly one supplied source: URL, image base64 with MIME type, or conversation attachments |
| `lexsis_asset_upload.upload` | Open the local image/video upload UI |
| `lexsis_drafts.asset_generate` | Execute an approved generation request |
| `lexsis_assets.view` | Inspect the returned asset through the shared fit procedure |

Import arguments are exactly one of `url`, image `data` + `mime_type`, or
non-empty `attachments` with `attachment_id` per entry. Import never opens UI.
Upload arguments contain only the selected `workspace_id` and `theme_id`.
Wait for the user's uploaded-asset message; opening the panel is not a
completed upload. Without inline UI, request a URL or conversation attachment
and import it instead. `references/lexsis-mcp-contract.md` owns this contract.

## External-provider handoff

When the merchant chooses an available external provider, retain that provider
and its credit/approval evidence. Persist its output with
`lexsis_asset_import.import` before binding it to a page; use the returned
permanent asset URL, not a transient provider URL. Inspect it through the
shared asset workflow. Do not imply a provider exists merely because an old
example named it.

## Result record

Save the final bindings in
`work/storefront-assets/<brief-name>/asset-manifest.json`: role, source type,
asset id, permanent URL, and verification status. Shopify media retains its
product and media ids. Prompt history and rights evidence stay in the brief.
For an existing page, update only the requested slots and recompile once;
visible changes return to design approval. No page publication is implied.

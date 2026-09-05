# Island Preview

Use this during `/design-page`.

1. Resolve the selected island's active schema.
2. Author readable `<lx-island>` source with safe preview data.
3. Compile the complete canonical page.
4. Save the response and input hashes in `compile-artifact.json`.
5. Run `design-page/scripts/build_page_preview.py`.
6. Save `page-preview.html`.
7. Confirm every required island hydrates before design approval.

The preview uses compiled renderer markup and the exported Lexsis island
runtime. Never hand-author `data-island` or `data-props`.

Fallback HTML may keep an isolated component visible while iterating, but a
required production island in fallback mode blocks approval. Real product
resolution and cart behavior are verified on the hosted draft.

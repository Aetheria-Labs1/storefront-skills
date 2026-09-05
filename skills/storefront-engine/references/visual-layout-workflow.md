# Visual Layout Workflow

`/visual-page` turns an approved plan into a browser-reviewable mockup. It does
not create the production draft.

## Design Decisions

The visual stage approves:

- hierarchy and section proportions
- image placement and crop direction
- typography and color balance
- desktop composition and mobile stacking
- CTA placement
- island choice and presentation

Use placeholder copy where final copy is not approved. A composition image may
support art direction, but it must never become the page itself.

## Files

Write:

- `lexsis-source.html` — canonical readable authoring source
- `page-theme.css` — global page CSS passed to the compiler
- `compile-artifact.json` — compile response plus exact input hashes
- `visual-preview.html` — generated local browser preview

Static content stays ordinary HTML. Supported interactions use
schema-validated `<lx-island>` source and a static
`data-lx-island-fallback` child. Read `island-preview.md` for the runtime
contract.

Use existing store and product assets first. Copy bundled placeholders into
the page's `assets/` directory only when an image is still missing. Record each
one as `sourceType: "preview-placeholder"` so `/asset-prep` can replace it.

## Approval Gate

Review at 390px, 768px, and 1280px. Show which islands are hydrated, which use
fallback HTML, and which assets are temporary.

After approval, preserve the source and CSS exactly. `/asset-prep` replaces
temporary media in the canonical source and requires reapproval of visible
changes. `/generate` promotes the approved bundle instead of rebuilding it.

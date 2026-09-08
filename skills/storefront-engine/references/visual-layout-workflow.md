# Design Page Workflow

`/design-page` turns an approved one-page section plan into canonical Lexsis
source and one unpublished hosted draft.

It owns:

- existing-asset inventory and the single generation decision
- responsive layout and copy composition
- island selection and schema resolution
- `lexsis-source.html` and `page-theme.css`
- one clean compile artifact and hosted preview URL
- hosted 390px and 1280px approval

The plan supplies section intent, not islands. `/generate` supplies tablet and
full real-commerce QA.

Local and temporary placeholder assets are not allowed. Source must use
permanent Lexsis or Shopify media before draft creation.

An optional `/asset-prep` run may replace or improve media, but it is not a
required handoff. Any visible replacement returns the design to
`changes-pending-approval`.

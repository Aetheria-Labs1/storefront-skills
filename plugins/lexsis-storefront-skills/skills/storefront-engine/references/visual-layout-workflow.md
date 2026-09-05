# Design Page Workflow

`/design-page` turns an approved one-page section plan into canonical Lexsis
source and an interactive local preview.

It owns:

- existing-asset inventory and the single generation decision
- responsive layout and copy composition
- island selection and schema resolution
- `lexsis-source.html` and `page-theme.css`
- one clean compile artifact and `page-preview.html`
- 390px and 1280px approval

The plan supplies section intent, not islands. `/generate` supplies tablet,
hosted-fidelity, and real-commerce QA.

Placeholders are allowed while reviewing the local design. They are recorded
as `sourceType: "preview-placeholder"` and cannot pass production validation.

An optional `/asset-prep` run may replace or improve media, but it is not a
required handoff. Any visible replacement returns the design to
`changes-pending-approval`.

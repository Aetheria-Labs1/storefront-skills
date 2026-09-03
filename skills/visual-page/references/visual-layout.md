# Visual Layout

The visual stage approves hierarchy, section proportions, image placement,
typography, color balance, desktop composition, mobile stacking, CTA
placement, and island presentation.

Write:

- `visual-source.html` — readable design-stage authoring source
- `visual-preview.html` — generated browser preview

Use ordinary HTML for static content and active Lexsis islands only for useful
interaction previews. A supporting composition image may guide art direction,
but it must never become the page.

Search existing store and product assets first. When media is still missing,
copy a bundled placeholder into the page workspace and record it as
`sourceType: "preview-placeholder"`.

Review at 390px, 768px, and 1280px. Show which islands use the runtime, which
use static fallbacks, and which assets remain temporary.

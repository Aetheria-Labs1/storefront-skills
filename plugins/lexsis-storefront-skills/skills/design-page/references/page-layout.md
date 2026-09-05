# Page Layout

The design stage approves hierarchy, section proportions, image placement,
typography, color balance, desktop composition, mobile stacking, CTA
placement, and island presentation.

Write:

- `lexsis-source.html` — the canonical readable page source
- `page-theme.css` — global theme tokens and page-wide custom CSS
- `compile-artifact.json` — exact compile response and input hashes
- `page-preview.html` — generated browser preview; never edit it directly

Use ordinary HTML for static content and active Lexsis islands only for useful
interaction previews. A supporting composition image may guide art direction,
but it must never become the page.

Start from the selected page kit or section templates. Use the selected
theme's `--lx-*` tokens and Tailwind utilities rather than rebuilding the
brand system inside each section. Record one coherent style treatment in the
manifest.

Search existing store and product assets first, show one combined asset
summary, and ask once before generating missing or optional media. When
generation is postponed, copy a bundled placeholder into the page workspace
and record it as `sourceType: "preview-placeholder"`.

Review at 390px and 1280px. `/generate` owns tablet and hosted-draft QA.

Approval hashes the exact source, page theme, head, scripts, structure, and
compiled bundle. `/generate` promotes this source instead of recreating it.

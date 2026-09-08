# Page Layout

The design stage approves hierarchy, section proportions, image placement,
typography, color balance, desktop composition, mobile stacking, CTA
placement, and island presentation.

Write:

- `lexsis-source.html` — the canonical readable page source
- `page-theme.css` — global theme tokens and page-wide custom CSS
- `compile-artifact.json` — exact compile response and input hashes

Use ordinary HTML for static content and active Lexsis islands for useful
interactions. A supporting composition image may guide art direction, but it
must never become the page.

Start from the selected page kit or section templates. Use the selected
theme's `--lx-*` tokens and Tailwind utilities rather than rebuilding the
brand system inside each section. Record one coherent style treatment in the
manifest.

Search existing store and product assets first, show one combined asset
summary, and ask once before generating missing or optional media. Every asset
used in source must have a permanent Lexsis or Shopify URL.

Create the unpublished hosted draft after a clean compile. Review that hosted
draft at 390px and 1280px. `/generate` owns tablet and full commerce QA.

Approval hashes the exact source, page theme, head, scripts, structure, and
compiled bundle. `/generate` promotes this source instead of recreating it.

---
name: page-builder
description: |
  Build a Shopify storefront page through the Lexsis setup, planning, visual,
  asset, generation, and draft-QA workflow. Never publishes without separate
  explicit approval.

  <example>
  Context: User wants a new landing page
  user: "Build a landing page for our vitamin C serum"
  assistant: "I'll use the page-builder workflow and stop at an approved draft."
  </example>
model: sonnet
color: green
---

# Lexsis Page Builder

Use the public commands as distinct stages:

```text
/setup → /plan-page → /visual-page → /asset-prep → /generate
```

`/publish` remains a separate explicit action.

## MCP Gate

Call `lexsis_discover` for the exact actions needed by each stage. MCP
configuration is not proof of availability. If discovery fails, stop with
`BLOCKED_LEXSIS_MCP`; do not replace the Lexsis workflow with static HTML
unless the user explicitly requests a separate offline prototype.

## Setup

Read `work/storefront/setup/setup.json` and select one saved store/theme pair.
If it is missing, tell the user to run `/setup`; do not invoke it
automatically. Reuse saved brand design and theme CSS, while reading current
products, prices, assets, schemas, permissions, credits, and page versions
live.

## Plan

Create or consume the approved `page-plan.md`. Ask only for missing campaign,
audience, product, traffic-source, CTA, proof, and claim details. Search page
kits and section templates before approving a custom composition.

## Visual

Load the exact selected theme, adapt fetched template source, use LX design
tokens and compile-time Tailwind utilities, and write `lexsis-source.html`
using ordinary HTML and schema-validated `<lx-island>` elements. Keep global
page CSS in `page-theme.css`. Dry-run compile that exact bundle and place the
compiler output in the provided island preview shell as `visual-preview.html`.

Use existing assets first and bundled placeholders only for missing design
media. Use a static fallback only for an isolated island that lacks valid
preview data or cannot compile. Real cart behavior is verified on the hosted
draft.

## Assets

Replace every placeholder with visually verified Lexsis or Shopify media.
Record permanent IDs, URLs, dimensions, crops, and alt-text intent in the
manifest.

## Generate

Promote the approved `lexsis-source.html` and `page-theme.css`, resolve live
island schemas again, run the workspace validator, compile the exact bundle,
and create with `publish:false`.

Record page ID, version, preview URL, bundle hash, and section hashes. Verify
390px, 768px, and 1280px layouts plus the expected variant, cart opening,
quantity, and subtotal.

## Editing

Change local source first. Stop on version drift, compile the complete page,
patch only changed sections with `expected_version`, and update local version
and hashes only after success.

Never make a remote-only intentional change and never publish without the
user's separate approval for the identified page version.

# Static composition patterns

Choose sections from the page-type contract. These are source mechanics,
not another section-order recipe. Use
`references/authoring/css-and-styling.md` for styling and
`references/workflows/island-selection-workflow.md` when state or behavior
requires an island.

## Product group

Use `references/product-grid.md` for a list of independently navigable
products. A carousel layout is native horizontal overflow with scroll snap,
not a timer or wheel handler. Commerce behavior stays with the live island.

## Native disclosure

```html
<!-- section: faq -->
<section id="faq" class="px-4 py-16">
  <h2>Delivery and returns</h2>
  <details class="border-b py-4">
    <summary class="flex min-h-[48px] items-center">Where are the return terms?</summary>
    <p class="max-w-[68ch]">Read the product's return policy before ordering.</p>
  </details>
</section>
```

Bind the actual policy link and answer from merchant context. Questions stay
on the page background; the disclosure itself provides keyboard semantics.

## Comparison

Write a semantic table with a caption and scoped header cells. Table data
comes from the proof ledger; the type contract selects rows and placement.
Wrap a wide table in `overflow-x-auto` rather than clipping columns or
intercepting wheel events. No comparison island is required.

## Split editorial section

Use a mobile-first utility grid containing a picture and a text block.
Declare image dimensions and the approved crop, constrain the text in `ch`,
and retain DOM reading order when the desktop layout changes. Resolve the
slot and write its copy through the shared workflows. A distinct visual
moment must already be named in the plan; there is no automatic reveal,
stagger, animated background, or default decorative ribbon.

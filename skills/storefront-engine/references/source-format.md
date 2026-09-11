# HTML-native source format

House rules in `storefront-engine/references/design-rules.md` govern the
page. `references/authoring/source-authoring.md` is the authoring contract;
`references/authoring/css-and-styling.md` owns CSS. This entry point covers
only the input shape passed to the compiler.

## Page structure

Author a source string with one delimiter and matching section id per section:

```html
<!-- section: faq -->
<section id="faq" class="px-4 py-16">
  <h2>Ordering questions</h2>
  <details>
    <summary class="flex min-h-[48px] items-center">Where are the shipping terms?</summary>
    <p>Read the product's shipping policy before ordering.</p>
  </details>
</section>
```

Use actual merchant policy copy and links. An interactive section contains
`<lx-island>` with one `application/json` child copied from the schema fetched
for that decision. `hydrate` is an authored attribute; generated
`data-island` and `data-props` markers are renderer output, not source.
Supported headless hooks and fallback markup are resolved through the same
live schema, not a static hook or prop table.

## Tool inputs

Pass `source`, structured `head`, optional `scripts` and any page-wide
`theme_css` directly to `lexsis_pages.compile`; no local files are created. Follow `references/source-artifact-workflow.md`. Templates come from
`lexsis_design.get_section` as editable `source`; compiled references are
inspection artifacts only. `references/generation-protocol.md` owns repairs,
draft creation and subsequent versioned edits.

The compiler escapes storage representations. Do not escape a whole section
or construct JSON strings of HTML manually. Valid HTML entities in authored
text or attribute values remain normal HTML; they are not an escaped page.
Motion, if the plan requires it, follows `references/animation-system.md`.

# Editable section templates

Templates are reusable source, not a page-type or island authority. The
selected contract in `references/page-types/_index.md` determines which jobs
the page needs; the plan determines their order and merchant evidence.

## Search and fetch

1. Search `lexsis_template_library.search_sections` for the section job and
   intended visual direction. Search `search_page_kits` and read `get_kit`
   only when the whole-page direction needs a starting kit.
2. Fetch selected section ids through `lexsis_design.get_section` and use
   its editable `source` response. Keep the response's source and stable
   section identity; compiled output is for inspection only.
3. Replace template content with the approved merchant data. Resolve media
   through `references/workflows/section-asset-workflow.md` and interactive
   choices through `references/workflows/island-selection-workflow.md`.
4. Scope styling through `references/authoring/css-and-styling.md`, compile,
   then create or patch the draft through `references/generation-protocol.md`.

## Merchant-owned sections

Use `lexsis_template_library.list_mine` and `get_mine` for saved merchant
sections. Creation, update and application follow
`references/merchant-templates.md`; publishing a reusable section remains an
explicit live operation. A source section is not a hidden renderer shell.

Keep one section per semantic job. Inserting a template is not permission to
add unrelated navigation, urgency, capture, proof, or another purchase form.

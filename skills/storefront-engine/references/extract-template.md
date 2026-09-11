# Extract reusable source

Use a merchant-authorized page or reference to identify a reusable section.
The reusable object is editable source, not compiled DOM or a screenshot.

## Workflow

1. Capture the source URL and the intended reusable job. Preserve provenance
   and distinguish observed behavior from behavior actually tested.
2. For a Lexsis page, use `lexsis_pages.source` or
   `lexsis_pages.section_source`. For a reference, author the equivalent job
   through `references/authoring/source-authoring.md`; do not paste compiled
   island markers or another site's application code.
3. Separate structure from merchant bindings. Resolve the current schema for
   interactive requirements and keep required product/evidence bindings
   explicit. Compile the source before saving it as reusable material.
4. Create or update the merchant section through
   `references/merchant-templates.md`. Record the returned id and version.
   Applying the section to a page still needs that page's bindings and QA.

A template may change content and layout; it may not override house rules,
create a second renderer shell, or smuggle a publication step into saving.

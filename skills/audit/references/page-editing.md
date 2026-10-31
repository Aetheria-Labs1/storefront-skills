# Storefront Page Editing

Run by `/design-page` (Existing Page Edits) and `/optimize` Apply.

Edit existing pages through canonical editable source and section-level remote
operations. Read `source-artifact-workflow.md` first.

## Edit Flow

1. Read `lexsis_pages.edit_context` and `lexsis_pages.source`.
2. Compare the current version with the last recorded version; reconcile drift.
3. Edit the returned source value and compile the complete changed inputs.
4. Compare section changes with the persisted baseline.
5. Patch only changed sections with `expected_version`,
   `expected_source_sha256` and an idempotency key where supported.
6. Update recorded version/hashes after success, then run `diff`, `integrity`
   and the affected checks on the hosted draft.

For existing pages, `page_id` is authoritative. Do not require the user to
reselect a workspace or pass `store_id`; an optional store ID is only an
assertion. Service-token store/workspace scopes remain authorization boundaries.

## Operations

Every section write below loads `edit_context`, applies the change to the
page source, recompiles the whole page and commits exactly one new version.
Pass `expected_version` (and `expected_source_sha256` when you have it): a
stale value is rejected with `version_conflict` and nothing is written.

### Batch changes: `page_patch` (preferred)

Several operations in one call apply in order and commit one version, or
nothing if any step fails. Use it for any edit touching more than one section.

```json lexsis-args=patch_page
{
  "page_id": "00000000-0000-4000-8000-000000000001",
  "expected_version": 7,
  "idempotency_key": "indimums-hero-copy-1",
  "changes": [
    {
      "operation": "upsert_section",
      "source": "<!-- section: hero -->\n<section id=\"hero\" class=\"px-4 py-16\"><h1>Gentle care for new skin</h1></section>"
    },
    { "operation": "move_section", "section_id": "reviews", "position": { "after": "hero" } },
    { "operation": "remove_section", "section_id": "old-banner" }
  ]
}
```

### Position semantics (`upsert_section`, `move_section`, `page_update_section`, `page_move_section`)

| `position` | Result |
| --- | --- |
| omitted on an existing section | replaced in place |
| omitted on a new section | appended last |
| `"first"` / `"last"` | moved/inserted there |
| number `n` | final index `n`, counted after the section is taken out |
| `{ "before": "id" }` / `{ "after": "id" }` | next to that section |

A `position` on an existing section replaces **and** moves it. An unknown or
self-referencing anchor id is rejected instead of silently appending.

### Update, add or move one section

```json lexsis-args=update_section_from_source
{
  "page_id": "00000000-0000-4000-8000-000000000001",
  "expected_version": 7,
  "source": "<!-- section: faq -->\n<section id=\"faq\" class=\"px-4 py-16\"><h2>Questions</h2></section>",
  "position": { "before": "footer" }
}
```

```json lexsis-args=move_page_section
{
  "page_id": "00000000-0000-4000-8000-000000000001",
  "section_id": "reviews",
  "position": "first",
  "expected_version": 8
}
```

`page_remove_section` takes `page_id`, `section_id` and `expected_version`
and follows the same version protection.

### Update page CSS (`page_update_head`)

`theme_css` **replaces** the page's stylesheet wholesale; it is never merged.
Read the current value from `lexsis_pages.content`, edit that full string and
send all of it back. Section `<style>` blocks travel with their section and are
replaced only when that section is upserted. `page_patch` never changes
`theme_css`.

```json lexsis-args=update_page_head
{
  "page_id": "00000000-0000-4000-8000-000000000001",
  "expected_version": 9,
  "theme_css": ":root { --lx-bg-color: #fffaf5; }\n.offer-note { color: var(--lx-text-muted, #555); }"
}
```

A class the compiler reports as `missing_tailwind_utility` must become a real
Tailwind utility, a rule that actually styles it, or a data attribute if it
only marks an element for script. Never add an empty rule to pass.

## Best Practices

- Retain the intended change and returned version in the task handoff
- Always call `lexsis_pages` action `edit_context` before a write
- Stop on unexpected version drift
- Re-read source and reconcile against the current version when an edit returns `version_conflict`
- Reference section IDs from the page data (don't guess)
- Compile the complete editable source before section patching
- After editing, run `diff` and `integrity`
- Use explicit remove operations for absent properties. `null` remains a JSON
  value and is not deletion.
- When changing a collection binding, setting `products` removes `productIds`
  and setting `productIds` removes `products`; never send both.
- Reusing an idempotency key with the same request returns the original result.
  Reusing it with different content is an error.
- Update input hashes and manifests only after a successful remote write.
- Preserve existing CSS variables and island configurations
- Don't break mobile responsiveness when editing desktop layout

Minor edits do not repeat planning or create page files. Resolve the saved
binding or current MCP context; keep the existing page id authoritative.

For published pages, `current_version` can advance while the live renderer
remains pinned to `published_version_id`. Publish only after QA.

## Applying Reusable Sections

Read `merchant-templates.md`. `template_apply` follows the same edit
preconditions and materializes source into the page. After success, fetch edit
context, read back the persisted source and hashes, then run `diff` and `integrity`.

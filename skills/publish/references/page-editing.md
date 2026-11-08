# Storefront Page Editing

Run by `/design-page` (Existing Page Edits) and `/optimize` Apply.

Edit existing pages through canonical editable source and section-level remote
operations. Read `source-artifact-workflow.md` first.

## New Page (files, `lexsis_build`)

Create a draft with `lexsis_build` action `commit` and no `page_id`:

- `create`: `slug`, `title`, `theme_id`, optional `archetype`,
  `product_binding`, `resource_type`. Always a draft; it never publishes.
- `files`: the page as files, in the same layout as editing below.
- `from` (optional): `{page_id, version?}` seeds the tree from an existing
  page, so only new or changed files are sent. `null` drops a seeded file.
- `shared_sections` (optional): shared section ids (store header, footer).
  Each is added as `sections/<section_id>.html` and linked to the new page.
  If `lexsis.json` doesn't list it, the first id goes on top and the rest at
  the bottom.
- `dry_run: true` returns every diagnostic with file and line and creates
  nothing. Run it first, fix everything, then commit once.

An existing slug returns `PAGE_EXISTS` with that page's id: edit it instead.
The result carries `page_id`, `version` and `preview_url`; every later change
uses the Edit Flow below.

## Edit Flow (files, `lexsis_build`)

An existing page is a tree of files: `lexsis.json` (section order and `head`),
`sections/<id>.html` (each starts with its own `<!-- section: id -->` line,
markup, `<style>` and `<script>` together) and optional `styles/*.css` for
classes shared across sections. Unchanged files are never resent.

1. `lexsis_build` action `get` with `page_id`: returns `version` and the tree
   (path to hash, sizes). Ask for contents only of the files you will change
   (`files: ["sections/hero.html"]`). Do not read the whole page to edit one part.
2. Pick the smallest write:
   - **Under about 20 changed lines: `patch`.** `replace_text`
     (`file`, `find`, `replace`, optional `all`), `upsert_css_rule`
     (`file`, `selector`, `decl`), `remove_css_rule`. Never resend a file to
     change a word, a price or one CSS rule.
   - **New or heavily changed sections: `commit`** with only the changed
     paths in `files`. `null` deletes a file.
   - **Reorder or remove sections:** `commit` a new `lexsis.json` with the
     `sections` order changed, plus `null` for a removed section's file.
3. Always pass `base_version` (the version from step 1). Run `dry_run: true`
   first when the change is large or risky; it compiles and validates without
   saving.
4. One compile returns **every** diagnostic with `file`, `line` and `code`.
   Fix them all in one pass, then commit once. Do not fix one error per call.
5. `noop: true` means nothing changed and no version was made.
6. After success, record the new `version` and `preview_url`, run
   `lexsis_build` action `diff` (`from`, `to`) to confirm only the intended
   lines changed, then `lexsis_pages.integrity` and the affected hosted checks.

A class used by more than one section belongs in `styles/base.css`, not in
one section's `<style>`; this is what stops a cross-section class from failing
the compile.

On `version_conflict` (stale `base_version`), call `get` again, re-apply the
change to the current files and retry. Never overwrite blindly.

For existing pages, `page_id` is authoritative. Do not require the user to
reselect a workspace or pass `store_id`; an optional store ID is only an
assertion. Service-token store/workspace scopes remain authorization boundaries.

```json lexsis-args=build_get
{
  "page_id": "00000000-0000-4000-8000-000000000001",
  "files": ["sections/hero.html"]
}
```

```json lexsis-args=build_patch
{
  "page_id": "00000000-0000-4000-8000-000000000001",
  "base_version": 7,
  "ops": [
    { "op": "replace_text", "file": "sections/hero.html", "find": "Gentle care", "replace": "Gentle daily care" },
    { "op": "upsert_css_rule", "file": "sections/hero.html", "selector": ".hero h1", "decl": "font-size:44px" }
  ]
}
```

```json lexsis-args=build_commit
{
  "page_id": "00000000-0000-4000-8000-000000000001",
  "base_version": 7,
  "message": "add FAQ before footer",
  "files": {
    "sections/faq.html": "<!-- section: faq -->\n<section id=\"faq\" class=\"px-4 py-16\"><h2>Questions</h2></section>\n",
    "lexsis.json": "{\n  \"schema\": \"lexsis.page/2\",\n  \"sections\": [\"hero\", \"faq\", \"footer\"]\n}\n"
  }
}
```

## V1 section actions (fallback only)

Use `lexsis_drafts` `page_patch`, `page_update_section`, `page_move_section`,
`page_remove_section` and `page_replace` only when `lexsis_build` is not
available on the connected server (it is missing from `lexsis_discover`).
They resend whole sections and recompile the whole page on every call. Each
takes `expected_version`; a stale value is rejected with `version_conflict`.

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
- Always read the current version (`lexsis_build` `get`) before a write
- Stop on unexpected version drift
- Re-read source and reconcile against the current version when an edit returns `version_conflict`
- Reference section IDs from the page data (don't guess)
- Send only changed files; patch small edits instead of resending sections
- After editing, run `lexsis_build` `diff` and `lexsis_pages` `integrity`
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

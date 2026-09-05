# Production Source and Synchronization

## Page Files

The page workspace contains:

```text
page-plan.md
page-manifest.json
lexsis-source.html
page-theme.css
compile-artifact.json
visual-preview.html
qa-report.md
assets/
```

`lexsis-source.html` and `page-theme.css` are the only editable visual and
production inputs. `compile-artifact.json` and `visual-preview.html` are
generated from them.

For a schema-v1 workspace, run
`scripts/migrate_page_workspace_v2.py <working-directory>`. The migration
stops when the old visual and production source differ; those workspaces need
an explicit source choice and renewed visual approval.

## Source Format

Use one stable delimiter and matching section ID:

```html
<!-- section: hero -->
<section id="hero">
  <lx-island name="BuyBox" hydrate="immediate">
    <script type="application/json">
      {
        "product": {
          "title": "Product name",
          "variants": []
        }
      }
    </script>
  </lx-island>
</section>
```

Keep HTML and island JSON readable. Section IDs are unique. Production source
contains no temporary asset paths, preview placeholders, inline event handlers,
unsupported scripts, internal notes, or hand-authored runtime island markup.

Resolve the current schema before every island. Prefer native presentation and
use headless variants only when their required hooks are fully implemented.

## Compile and Create

Validate locally, compile the complete source without saving, fix every
blocking issue including missing Tailwind candidates, then create with
`publish:false`.

Save the returned page ID, version, preview URL, bundle hash, persisted source
hash, remote bundle hash, and per-section hashes. Save the returned style
manifest under `design.compiledStyleManifest`. The bundle hash covers
`lexsis-source.html`, `page-theme.css`, head, page scripts, and every
non-file compiler value recorded in `compileInputs`.

### Creation Example

1. Discover the exact `lexsis_pages.compile` and
   `lexsis_page_create.create` schemas.
2. Compile the complete local source with `page-theme.css`, selected head,
   theme ID, scripts, and product binding.
3. Fix every blocking issue without saving remotely.
4. Create the page as a draft with `publish:false`. Use a discovered
   `compile_id` when supported; otherwise resubmit the exact compiled bytes.
5. Fetch the persisted source and page content and reject any source or bundle
   hash mismatch.
6. Save the returned page ID, version, preview URL, hashes, section hashes,
   and style manifest.

## Edits

1. Fetch the remote version and compare it with the manifest.
2. Stop on drift.
3. Change local source.
4. Validate and compile the complete page.
5. Read `changedSections` from the validator.
6. Patch only those sections with `expected_version`.
7. Update local hashes and version only after success.

Remote content must never be the only copy of an intentional change.

### One-Section Edit Example

For a hero-only change:

1. Fetch the current remote version and stop if it differs from the manifest.
2. Edit only the hero block in `lexsis-source.html`.
3. Compile the complete local page.
4. Confirm the validator reports only `hero` in `changedSections`.
5. Patch the hero source with the discovered section-update action and
   `expected_version`.
6. Save the returned version and new hashes only after the patch succeeds.
7. Repeat responsive, asset, copy, and affected interaction checks.

## QA

Record MCP status, capabilities, actions, template decision, live bindings,
fallbacks, compilation, local bundle, remote version, 390px/768px/1280px
results, local-versus-hosted visual regression, commerce interaction, copy,
claims, assets, integrity, blockers, and publish readiness in `qa-report.md`.

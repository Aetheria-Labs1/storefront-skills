# Production Source and Synchronization

## Page Files

The page workspace contains:

```text
page-plan.md
page-manifest.json
visual-source.html
visual-preview.html
lexsis-source.html
qa-report.md
assets/
```

Visual files may be absent only when the user explicitly skipped the visual
stage.

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
blocking issue, then create with `publish:false`.

Save the returned page ID, version, preview URL, bundle hash, and per-section
hashes. The bundle hash covers source, head, theme CSS, and page scripts.

## Edits

1. Fetch the remote version and compare it with the manifest.
2. Stop on drift.
3. Change local source.
4. Validate and compile the complete page.
5. Read `changedSections` from the validator.
6. Patch only those sections with `expected_version`.
7. Update local hashes and version only after success.

Remote content must never be the only copy of an intentional change.

## QA

Record compilation, local bundle, remote version, 390px/768px/1280px results,
commerce interaction, copy, claims, assets, integrity, blockers, and publish
readiness in `qa-report.md`.

# Storefront Page Files

Use these files to pass work between the public storefront commands without
requiring one command to invoke another.

## Setup Context

`/setup` creates:

```text
work/storefront/setup/
├── setup.json
└── stores/
    └── <store-id>/
        ├── brand-design.md
        └── themes/
            └── <theme-id>.css
```

A page binds exactly one saved store and theme. Several themes may be saved,
but a page must not mix their design files.

Setup is reused for slow-changing design context. Products, prices, variants,
assets, island schemas, permissions, analytics, and page versions remain live
reads.

## Page Workspace

```text
work/visual-pages/<page-handle>/
├── page-plan.md
├── page-manifest.json
├── visual-source.html
├── visual-preview.html
├── lexsis-source.html
├── qa-report.md
└── assets/
```

- `page-plan.md` is the approved strategy and section blueprint.
- `visual-source.html` is readable design-stage HTML and may use preview data.
- `visual-preview.html` is generated from a dry-run compile and the Lexsis
  island preview shell.
- `lexsis-source.html` is the canonical editable production source.
- `qa-report.md` records draft and interaction verification.

Visual files are optional only when the user explicitly skips `/visual-page`.
Production source is never optional once a draft exists.

## Manifest

Use `schemaVersion: 1`:

```json
{
  "schemaVersion": 1,
  "status": "planned",
  "workflow": {
    "skippedSkills": []
  },
  "mcp": {
    "status": "connected",
    "checkedAt": "2026-09-04T12:00:00Z",
    "surfaceVersion": "3.0",
    "capabilities": [
      {
        "router": "lexsis_pages",
        "actions": ["compile"]
      }
    ]
  },
  "page": {
    "title": "SuperYou Pro Creatine",
    "handle": "superyou-pro-creatine",
    "archetype": "landing"
  },
  "workspaceId": "...",
  "storeId": "...",
  "themeId": "...",
  "template": {
    "mode": "page-kit",
    "pageKitId": "kit-slug",
    "sectionTemplateIds": ["hero-slug", "buy-box-slug"],
    "evaluatedTemplates": [],
    "selectionReason": "Matches the approved PDP structure",
    "selectedAt": "2026-09-04T12:00:00Z"
  },
  "design": {
    "themeId": "...",
    "themeSource": "saved-and-verified",
    "stylePack": "editorial",
    "compiledStyleManifest": null
  },
  "setupPath": "work/storefront/setup/setup.json",
  "brandDesignPath": "work/storefront/setup/stores/<store-id>/brand-design.md",
  "themeCssPath": "work/storefront/setup/stores/<store-id>/themes/<theme-id>.css",
  "pageConfig": {
    "head": {},
    "themeCss": "",
    "scripts": []
  },
  "productBindings": [],
  "assets": [],
  "sections": ["announcement", "hero", "benefits", "faq"],
  "islands": [
    {
      "sectionId": "hero",
      "name": "BuyBox",
      "schema": {
        "version": "5.0.0",
        "lifecycleStatus": "active",
        "resolvedAt": "2026-09-04T12:00:00Z"
      },
      "productionMode": "native",
      "previewMode": "hydrated",
      "previewData": true
    }
  ],
  "visual": {
    "status": "pending",
    "sourcePath": "visual-source.html",
    "previewPath": "visual-preview.html"
  },
  "sourceSync": {
    "lastCompiledBundleHash": null,
    "lastSyncedBundleHash": null,
    "lastSyncedSectionHashes": {},
    "lastChangedSections": []
  },
  "qa": {
    "status": "pending",
    "checkedVersion": null,
    "checkedBundleHash": null,
    "responsive": false,
    "commerce": false,
    "copy": false,
    "claims": false,
    "assets": false,
    "integrity": false
  },
  "remote": {
    "pageId": null,
    "lastKnownVersion": null,
    "previewUrl": null
  }
}
```

`previewMode` is `hydrated` when the real exported island runs locally and
`fallback` when the mockup shows static fallback HTML.

`template.mode` is `page-kit`, `sections`, or `custom`. A custom composition
records evaluated templates and why they were rejected. The current template
API does not guarantee a version field, so preserve selected IDs rather than
inventing one.

After a successful production compile, save the compiler's returned
`style_manifest` under `design.compiledStyleManifest`.

## Skill Skips

Commands are independently invokable and never run another command
automatically.

- Skipping planning requires a short replacement `page-plan.md`.
- Skipping visual design sets `visual.status: "skipped"`.
- Skipping asset preparation requires `/generate` to create the same verified
  asset records.

Record each explicit skip in `workflow.skippedSkills`.

## Source Rules

Both visual and production source use stable boundaries:

```html
<!-- section: hero -->
<section id="hero">
  ...
</section>
```

Section delimiters and IDs match, IDs are unique, JSON is valid, and source is
normally formatted.

Visual source may use preview copy, bundled assets, and schema-valid island
preview data. Production source may not contain any preview placeholder,
temporary URL, local path, unsupported script, internal note, or unverified
asset.

## Synchronization

The production bundle hash covers `lexsis-source.html` plus page head, theme
CSS, and scripts.

For creation:

1. Validate local files.
2. Compile the complete source without saving.
3. Create the draft with `publish: false`.
4. Save page ID, version, preview URL, bundle hash, and section hashes.

For editing:

1. Fetch the current remote version.
2. Stop when it differs from `remote.lastKnownVersion`.
3. Change local source first.
4. Validate and compile the complete source.
5. Compare section hashes.
6. Patch only changed sections with `expected_version`.
7. Update the manifest only after a successful write.

Remote content must never be the only copy of an intentional change.

## QA Report

```markdown
# QA Report

- MCP status: connected/blocked
- MCP surface version: <version>
- Capabilities used: <routers/actions>
- Lexsis actions called: <ordered summary>
- Template: <kit/sections/custom reason>
- Live bindings: <products/assets>
- Fallbacks: none or list
- Compilation: pass/fail
- Source bundle: <hash>
- Remote version: <version>
- Desktop 1280px: pass/fail
- Tablet 768px: pass/fail
- Mobile 390px: pass/fail
- Commerce: pass/fail
- Copy: pass/fail
- Claims: pass/fail
- Assets: pass/fail
- Integrity: pass/fail
- Blockers: none or list
- Publish readiness: ready/not ready
```

Publishing requires matching local and remote versions, current passing QA,
the required entitlement, and explicit approval.

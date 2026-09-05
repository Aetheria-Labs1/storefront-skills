# Initial Page Files

Create:

```text
work/visual-pages/<page-handle>/
├── page-plan.md
├── page-manifest.json
├── qa-report.md
└── assets/
```

Start the manifest with:

```json
{
  "schemaVersion": 2,
  "status": "planned",
  "workflow": { "skippedSkills": [] },
  "mcp": {
    "status": "connected",
    "checkedAt": "2026-09-04T12:00:00Z",
    "surfaceVersion": "3.0",
    "capabilities": [
      {
        "router": "lexsis_catalog",
        "actions": ["get"]
      }
    ]
  },
  "page": {
    "title": "...",
    "handle": "...",
    "archetype": "landing"
  },
  "workspaceId": "...",
  "storeId": "...",
  "themeId": "...",
  "template": {
    "mode": "page-kit",
    "pageKitId": "...",
    "sectionTemplateIds": ["..."],
    "evaluatedTemplates": [],
    "selectionReason": "...",
    "selectedAt": "2026-09-04T12:00:00Z"
  },
  "design": {
    "themeId": "...",
    "themeSource": "saved-and-verified",
    "stylePack": null,
    "compiledStyleManifest": null
  },
  "setupPath": "work/storefront/setup/setup.json",
  "brandDesignPath": "...",
  "themeCssPath": "...",
  "pageThemeCssPath": "page-theme.css",
  "pageConfig": {
    "head": {},
    "scripts": []
  },
  "compileInputs": {
    "productBinding": {},
    "commerceConfig": {}
  },
  "productBindings": [],
  "assets": [],
  "sections": [],
  "islands": [],
  "visual": {
    "status": "pending",
    "sourcePath": "lexsis-source.html",
    "themeCssPath": "page-theme.css",
    "previewPath": "visual-preview.html",
    "compileArtifactPath": "compile-artifact.json",
    "approvedSourceHash": null,
    "approvedThemeCssHash": null,
    "approvedConfigHash": null,
    "approvedStructureHash": null,
    "approvedBundleHash": null,
    "approvedCompileBundleHash": null,
    "hydrationStatus": "pending",
    "hydrationEvidence": null
  },
  "fidelity": {
    "status": "pending",
    "productionBundleHash": null,
    "remoteSourceHash": null,
    "remoteBundleHash": null,
    "changedBindingPaths": [],
    "approvedExceptions": []
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
    "visualRegression": false,
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

The page binds one saved store/theme pair. Do not write visual or production
source during planning. `template.mode` is `page-kit`, `sections`, or `custom`.
Custom composition requires recorded template evaluation and a
`selectionReason`. Do not invent a template version when Lexsis does not
return one.

`themeCssPath` points to the reusable theme saved by `/setup`.
`pageThemeCssPath` points to the page-local `page-theme.css` passed as
`theme_css` to the compiler. `/visual-page` creates that page-local file from
the selected theme and any approved page-wide additions.

`compileInputs` stores every non-file value passed to compilation or page
creation. It is included in approval and synchronization hashes.

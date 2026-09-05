# Initial Page Files

Create:

```text
work/visual-pages/<page-handle>/
├── page-plan.md
├── page-manifest.json
└── assets/
```

Start with a compact progressive manifest:

```json
{
  "schemaVersion": 3,
  "status": "planned",
  "workflow": {
    "skippedSkills": []
  },
  "page": {
    "title": "...",
    "handle": "...",
    "archetype": "landing"
  },
  "workspaceId": "...",
  "storeId": "...",
  "themeId": "...",
  "setupPath": "work/storefront/setup/setup.json",
  "template": {
    "mode": "page-kit",
    "pageKitId": "...",
    "sectionTemplateIds": ["..."]
  },
  "sections": [
    "hero",
    "benefits",
    "closing-cta"
  ],
  "products": [
    {
      "productId": "...",
      "variantIds": ["..."]
    }
  ],
  "assets": [
    {
      "slotId": "A1",
      "role": "hero_bg",
      "sectionId": "hero",
      "sourceType": "lexsis",
      "assetId": "...",
      "url": "https://...",
      "status": "verified"
    },
    {
      "slotId": "A2",
      "role": "product_lifestyle",
      "sectionId": "benefits",
      "sourceType": "pending",
      "status": "planned"
    }
  ],
  "reviews": {
    "source": "collection",
    "collectionId": "...",
    "productIds": [],
    "minRating": 4,
    "available": 37
  }
}
```

`template.mode` is `page-kit`, `sections`, or `custom`. For custom
composition, keep the rationale in `page-plan.md`; do not store template
search transcripts in JSON.

`assets[]` holds one entry per asset slot in the plan. `sourceType` is
`lexsis` (with `assetId`), `shopify` (with `productId` and `mediaId`),
`preview-placeholder`, or `pending` while the slot is still `planned`.
`status` is `verified` or `planned`.

`reviews` records the plan's Proof sources line: `source` is `collection`,
`products`, or `none`; `collectionId` or `productIds` name the real source;
`available` is the count returned by the reviews API. Omit the block when the
page has no review section.

The manifest grows only when later stages have real state to record:

- `/plan-page` writes `assets[]` (verified or planned) and `reviews`.
- `/design-page` adds compact `config`, `islands`, and `design` records,
  resolves `planned` assets, and records `islands[].preset` and
  `islands[].presetOverrides` when a preset is applied.
- `/generate` adds `sync`, `remote`, and `qa`.

Do not prefill null production, approval, hash, QA, or remote fields. Do not
store copy intent, claims, occasion research, omitted components, or creative
notes in the manifest.

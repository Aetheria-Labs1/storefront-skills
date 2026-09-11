# Initial Page Files

Every page lives inside a campaign folder, so the pages of one push sit
together with the brief and the shared media that serve them.

```text
work/campaigns/<campaign-slug>/
├── campaign.json          the binding and the campaign facts
├── campaign.md            one-page brief: objective, occasion, dates, audience, offer
├── assets/                media shared by several pages in this campaign
└── pages/
    └── <page-handle>/
        ├── page-plan.md
        ├── page-manifest.json
        └── assets/        media used only by this page
```

`$W`, the page workspace every script and check refers to, is
`work/campaigns/<campaign-slug>/pages/<page-handle>/`.

## Naming the campaign folder

Infer `<campaign-slug>` from the request rather than asking, and say which
folder is in use in one line. Lower-case kebab-case, no dates inside the words:

| The request is about | Slug pattern | Example |
|---|---|---|
| An occasion or holiday push | `<occasion>-<year>` | `diwali-2026`, `bfcm-2026` |
| A named sale or promotion | `<name>-<year>` | `founders-sale-2026` |
| A product launch | `<product>-launch` | `vitamin-c-serum-launch` |
| An always-on funnel for one product | `<product>-evergreen` | `creatine-evergreen` |
| A channel or creative test | `<channel>-<theme>` | `meta-problem-hook` |
| A creator or partner collaboration | `<partner>-collab` | `ananya-collab` |
| Nothing campaign-like in the request | `adhoc-<yyyy-mm>` | `adhoc-2026-09` |

Reuse an existing folder when the request continues that campaign (another
page, a variant, an edit). Open a new one when the occasion, offer or product
changes. Two stores never share a campaign folder: the binding lives in
`campaign.json` and a second store means a second folder, suffixed with the
store name when the campaigns are otherwise the same (`diwali-2026-uk`).

## campaign.json

```json
{
  "schemaVersion": 1,
  "campaignSlug": "diwali-2026",
  "campaignType": "seasonal",
  "occasion": "Diwali",
  "startsAt": "2026-10-25",
  "endsAt": "2026-11-08",
  "workspaceId": "...",
  "storeId": "...",
  "themeId": "...",
  "setupPath": "work/storefront/setup/setup.json",
  "campaignSlug": "diwali-2026",
  "campaignPath": "work/campaigns/diwali-2026",
  "pages": ["diwali-gift-sets", "diwali-gift-sets-variant-b"]
}
```

`campaignType` is an id from `references/offers/campaign-calendar.md`.
`startsAt` and `endsAt` are set only when the merchant confirmed them, and an
`endsAt` here is what an offer ledger row and any countdown bind to. The
workspace, store and theme come from `setup.json`
(`references/page-types/_index.md` names the page type; the campaign names the
binding). Every page in `pages[]` inherits that binding and repeats it in its
own manifest, so a page is still readable on its own.

Legacy `work/visual-pages/<page-handle>/` workspaces stay readable. Do not
move them unless the user asks; new pages go in a campaign folder.

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
    "archetype": "landing",
    "pageType": "ad-landing-page",
    "funnelStage": "tof",
    "awareness": "problem-aware",
    "trafficSource": "meta"
  },
  "offer": {
    "type": "first-order",
    "summary": "15% off first order with code WELCOME15",
    "endsAt": null,
    "stockVerified": false,
    "compareAtBasis": "none"
  },
  "campaign": {
    "type": "evergreen",
    "occasion": null
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

`campaignSlug` and `campaignPath` point at the owning campaign folder;
`workspaceId`, `storeId` and `themeId` repeat the campaign binding so the page
validates without reading `campaign.json`. They must match it.

`page.pageType` is a file name from `references/page-types/` (without
`.md`), chosen with `references/page-types/_index.md`. `funnelStage`,
`awareness` and `trafficSource` use the vocabularies in
`references/page-types/_checklist-format.md`.

`offer.type` is an id from `references/offers/offer-types.md` or `none`.
`endsAt` is an ISO date only when the merchant confirmed it; `stockVerified`
is true only when live inventory was read. Omit `offer` when the page has no
offer. `campaign.type` is an id from `references/offers/campaign-calendar.md`.

`assets[]` holds one entry per asset slot in the plan. `sourceType` is
`lexsis` (with `assetId`), `shopify` (with `productId` and `mediaId`), or
`pending` while the slot is still `planned`. A generated slot is imported into
Lexsis (`sourceType: lexsis`) and also carries `"generated": true` and
`"provider": "<provider>"`; its `role` must be an ALLOW purpose from
`references/assets/generation-policy.md`, or the ASK purpose
`product_lifestyle` together with `"askApproved": true` and the merchant's
approval quoted in the plan's Generation record.
`status` is `verified` or `planned`.

`reviews` records the plan's Proof ledger review row: `source` is
`collection`, `products`, `external-verified` (a merchant-approved quote
imported with its source URL, see `references/proof/reviews-sourcing.md`), or
`none`; `collectionId` or `productIds` name the real source; `available` is
the count returned by the reviews API (or the number of approved external
quotes). Omit the block when the page has no review section.

The manifest grows only when later stages have real state to record:

- `/plan-page` writes `assets[]` (verified or planned) and `reviews`.
- `/design-page` resolves `planned` assets and adds compact `config`,
  `islands`, `design`, `sync`, `remote`, and pending `qa` records.
- `/generate` creates a draft only when none exists; otherwise it updates
  synchronization and QA state.

Do not prefill null production, approval, hash, QA, or remote fields. Do not
store copy intent, claims, occasion research, omitted components, or creative
notes in the manifest.

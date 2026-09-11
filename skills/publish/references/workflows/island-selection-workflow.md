# Live island selection

This is the single procedure for choosing interactive components. A page
contract names candidate families and decision inputs, not a prop schema.
Planning records functional intent; design resolves implementation.
`references/authoring/source-authoring.md` owns markup, and
`references/authoring/css-and-styling.md` owns styling.

## 1. Decide whether behavior is required

Use static HTML for factual text, comparisons, native disclosures, linked
logos, tables, navigation anchors and simple product lists. Add an island
only for required state, catalogue binding, media behavior, capture,
subscription/variant selection or an overlay. Do not create an island merely
because a legacy file named one.

## 2. Resolve the current catalog and schema

1. Read the type's decision inputs: product and media count, variant axes,
   selling plans, review availability, capture purpose and page length.
2. Call `lexsis_design.islands` for the compact current catalog. Exclude
   entries marked deprecated and entries disallowed by domain policy.
3. Call `lexsis_design.island_schema` for the selected candidate. Read its
   supported variants, required props, defaults, authoring examples,
   hydration mode, parts, CSS variables and headless support.
4. Select only a variant and props justified by the actual page decision.
   Bind real catalogue/ledger ids. Do not infer a field from a sibling
   island, old prose example, intent label or bundled prop map.
5. Check defaults against the house requirements. Disable incidental motion
   when the plan does not authorize it; a schema default is not a policy
   exemption. Do not hide data with filters when the section claims to show
   the full distribution.
6. Use source-format examples from that live schema and compile. Revisit the
   schema when an error or an unmet behavior requires it; never fetch every
   full schema without a decision that needs it.

## 3. Candidate families

| Job | Candidate direction | Decision inputs |
|---|---|---|
| Purchase | BuyBox | Actual product, variants, selling plans and approved design |
| Gallery | ProductGallery, ProductHero, ImageZoom | Image count/jobs, aspect, variant images and inspection needs |
| Linked purchase bar | StickyBar | Page length and the live purchase synchronization contract |
| Product browsing | QuickAdd, ProductCarousel, FeaturedCollectionStage | Need for commerce behavior beyond native product links |
| Reviews | ReviewCarousel, ReviewList | Eligibility and scope from `references/proof/reviews-sourcing.md` |
| Product explanation | IngredientExplorer, BeforeAfter | Verified product/evidence requirements, not decorative proof |
| Media | VideoPlayer, MediaCarousel, ShoppableVideoFeed | User-controlled behavior required by the type |
| Capture | EmailCapture, FunnelRuntime | Real form schema and the type's authorized goal |
| Availability or deadline | InventoryIndicator, CountdownTimer | Verified offer-ledger basis and type permission |
| Navigation/overlay | SiteHeader, Navbar, Footer, MobileMenu, Modal | Required navigation or interaction, with one owner per role |

These are candidate names, not a frozen catalog or prop map. Re-check the
current catalog before use. Policy owners decide whether a candidate's job
is allowed; an available component is not permission to deploy it.

## 4. Purchase state and styling

Keep one owner for purchase state. When the live schemas support linked
BuyBox and StickyBar controls, use their matching synchronization key and
complete variant catalog so variant, quantity, effective price, selling plan,
availability and cart-pending state remain consistent. External selectors
must use the group's supported scoped-event contract. Never replace this
with two independent cart handlers. If the current schemas cannot express
the intended linkage, route the secondary control back to the main form.

Record actual variant/props and schema evidence in the page decision record. A
`Preset: <island>/<intent>-<tone>` label describes the desired appearance; it
is not executable configuration. Resolve its intent now and record deviations.
Use only live schema parts/CSS variables, scoped by section id.

## 5. Retired jobs

| Retired component name | Current implementation |
|---|---|
| FAQ | Native `details` and `summary` |
| Tabs | Native radio controls with labels or disclosures |
| Marquee | Static linked logo/list markup; no ticker by default |
| StatCards | Static semantic figures with sourced values |
| BackToTop | Native anchor to a stable page id |
| Carousel | Native scroll snap or a justified active specialist |
| CartDrawer | Cart V2 through `head.use_cart_v2` |
| Countdown | CountdownTimer, only after ledger and live-schema checks |

Retained schema files for older pages are compatibility artifacts. They do
not authorize using retired components in new source. Non-existent names
have no schema to resolve; use the native job or an active catalog candidate.

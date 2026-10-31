# Consumer Behavior and CRO Decision Framework

Use this reference to turn shopper behavior into page decisions. It is a
hypothesis library, not a checklist. A page should usually activate two or
three relevant patterns, not every pattern below.

## Decision Protocol

Before asking the merchant or choosing a module:

1. Read the product, variants, price, inventory, existing media, reviews,
   policies, audience, traffic source, and available analytics.
2. Classify the visitor's likely primary mode:
   - **confirm**  -  knows the product and wants confidence to buy;
   - **compare**  -  deciding between options or alternatives;
   - **explore**  -  needs inspiration or use-case education;
   - **complete**  -  wants the full solution, routine, or setup;
   - **replenish**  -  returning for a refill, replacement, or repeat order.
3. Write the three most important questions the shopper must answer before
   buying.
4. Select at most three behavioral patterns that answer those questions.
5. Map each selected pattern to evidence, one page response, any required
   asset, and one primary metric.

Do not add a carousel, bundle, urgency treatment, sticky CTA, quiz, or proof
module merely because the pattern exists. Every module must reduce a named
uncertainty or decision cost.

## Merchant Questions

Inspect available evidence first. Ask only when the answer changes the page,
requires unavailable business knowledge, or spends credits. Group no more than
three questions in one turn.

Useful conditional questions include:

- **Gallery gap:** "The current media shows the pack and texture, but not scale
  or in-use context. Can you supply the real scale and
  in-use photos, or should those jobs remain pending?"
- **Relationship:** "Should the recommendation help shoppers complete the
  routine, compare alternatives, replenish later, or should this page avoid
  recommendations?"
- **Compatibility:** "Do you have a verified model, size, shade, ingredient,
  room-dimension, or usage mapping for these add-ons?"
- **Risk:** "Which verified shipping, returns, trial, warranty, cancellation,
  or guarantee terms can appear beside the purchase decision?"
- **Audience state:** "Is this primarily a first purchase, an experienced
  buyer, or a returning/replenishment visit?"
- **Traffic context:** "Which promise or creative brought this traffic here,
  if the page must preserve message match?"

Never ask "Do you want custom images?" without first identifying the missing
decision job, proposed image count, purpose, and likely placement. Paid image
generation remains separately credit-gated.

## Behavioral Pattern Library

| Pattern | Shopper signal or uncertainty | Page response | Primary measurement |
|---|---|---|---|
| Scan-first decision packet | High-intent visitor wants to verify and act quickly | Make product identity, promise, price, variants, availability, delivery/returns cue, proof summary, and primary CTA scannable in the first decision area | Add-to-cart rate, time to CTA |
| Visual investigation | Product appearance materially affects choice | Give the gallery clear next-image cues and cover product, detail, in-use, scale, variation, included items, and result/proof jobs where relevant | Gallery engagement, conversion |
| Scale, fit, and sensory confidence | Size, fit, texture, finish, shade, or quantity is hard to judge | Add dimension diagrams, familiar-object scale, model measurements, texture close-ups, swatches, or use-context imagery | Returns, fit questions, conversion |
| Information scent | Shoppers need detail but will not parse a wall of copy | Lead with benefit and decision fact, then expose specifications, ingredients, care, or methodology through clear progressive disclosure | Detail interaction, conversion |
| Choice reduction | Too many variants, bundles, or recommendations compete | Prioritize the likely default, explain differences, and keep the first recommendation set to two or three choices | Variant completion, conversion |
| Guided comparison | Visitor is deciding between products or tiers | Compare only decision-driving attributes; state "best for" and meaningful trade-offs without manufacturing a winner | Comparison interaction, product selection |
| Compatibility confidence | Add-on usefulness depends on model, shade, size, ingredient, room, or regimen fit | Show the verified fit reason beside each recommendation and suppress incompatible or unavailable items | Attach rate, support questions, returns |
| Solution completeness | The hero SKU is only one part of the shopper's job | Present the minimum complete outfit, routine, stack, recipe, room, setup, care kit, or commissioning kit with individually selectable items | Attach rate, AOV, revenue per visitor |
| Sequence and next step | Products are understood as stages or order of use | Show when, how, and in what order products are used; distinguish morning/evening, setup/use/care, or beginner/advanced | Bundle attach rate, education engagement |
| Context and mental simulation | Shopper cannot picture ownership or final use | Show the product in the actual scene, occasion, room, routine, task, or before/after context using truthful media | Context-image engagement, conversion |
| Replenishment and continuity | Consumable, maintenance item, size progression, or replacement cycle exists | Explain serving/use count, refill timing, cadence, compatible replacement, or easy reorder without inventing depletion dates | Repeat purchase, subscription opt-in |
| Returning-customer shortcut | Existing buyers need less education and more continuity | Prefer refill, reorder, saved configuration, compatible replacement, or "what changed" paths when reliable customer context exists | Repeat conversion, time to purchase |
| Proof proximity | A claim creates doubt at a specific decision point | Place sourced review excerpts, customer media, certification, test evidence, or expert proof beside the claim it supports | Proof interaction, conversion |
| Risk reversal | Delivery, fit, efficacy expectations, warranty, returns, or subscription cancellation creates hesitation | Put verified policy and guarantee language beside the relevant CTA or choice; make conditions legible | Checkout progression, support contacts |
| Price comprehension | Shopper cannot understand total value or recurring cost | Show current price, factual compare-at price, unit/cost-per-use where accurate, bundle contents, cadence, and savings calculation without deceptive anchoring | Conversion, AOV, margin |
| Effort reduction | Selecting an add-on or completing the setup requires navigation and rework | Allow inline selection, preserve the primary product choice, and avoid forcing page exits for two or three simple additions | Attach rate, abandonment |
| Commitment and ownership | Configuration increases relevance but can also create work | Use short builders, quizzes, or progress only when answers materially change the recommendation; show editable selections and a clear result | Builder completion, conversion |
| Mobile context preservation | Long scrolling hides product identity and purchase state | Keep gallery cues visible, repeat concise product context at major decision points, use short sections, and use a non-obstructive sticky CTA only when helpful | Mobile conversion, CTA usage |
| Message match | Visitor arrives from a specific ad, search, creator, or campaign promise | Repeat the same product, outcome, offer, and visual context early; do not make cold traffic reconstruct the premise | Bounce, conversion by source |
| Ethical urgency | Real stock, cutoff, launch, or event timing matters | Show only verified availability or deadlines, explain the consequence plainly, and remove stale urgency automatically | Conversion, cancellations, trust |
| Post-purchase clarity | Shopper worries about what happens after payment | Explain delivery, setup, first use, support, returns, warranty, subscription management, or expected next step | Checkout completion, support questions |
| Cognitive and performance ease | Heavy media or many modules slow comprehension or rendering | Keep one primary action per decision area, remove duplicate modules, optimize media, and preserve fast visual stability | Core Web Vitals, bounce, conversion |

## Relationship-Based Merchandising

Name the customer's job instead of using a generic "Recommended for You."
Start with two or three relevant products and show why each belongs.

| Vertical | Useful relationship names and jobs |
|---|---|
| Fashion | Complete the Look, Shop the Occasion, Three Ways to Wear It, Fit Kit, Care for This |
| Beauty | Complete Your Routine, Morning vs Evening, Solve the Concern, Shade Companion, Starter vs Refill |
| Supplements | Build Your Stack, Goal Protocol, Time-of-Day Stack, 30-Day Start, Refill the Stack |
| Food | Pair It With, Shop the Recipe, Make It a Meal, Flavor Flight, Occasion Box |
| Home | Complete the Room, Shop the Scene, Finish the Surface, Install and Protect, Match the Finish |
| Electronics | Make It Work, Compatibility Check, Protect It, Creator Kit, Replace the Consumable |
| Pet | Complete Their Care Routine, Life-Stage Bundle, Enrichment Set, Refill Reminder |
| Baby | Set Up the Station, Feeding Stage Kit, Size-Up Reminder, Daycare Pack |
| Travel | Complete the Packing System, Trip Type Kit, Destination Weather Kit, Carry-On Kit |
| B2B | Commissioning Kit, Compatible Parts, Maintenance Kit, Reorder This Set, Job-Specific Kit |

The relationship may be complementary, compatible, sequential, protective,
replenishing, substitutive, occasion-based, or an upgrade. Record which one it
is. Do not infer medical compatibility, technical compatibility, shade match,
or safety from visual similarity.

## Gallery Job Coverage

Treat the gallery as decision support. Check only jobs relevant to the product:

- identity and every included item;
- multiple angles and important detail;
- scale, dimensions, fit, or model reference;
- texture, material, finish, shade, or consistency;
- in-use context and the intended environment;
- variation across color, size, flavor, or configuration;
- installation, sequence, routine, or setup;
- sourced result, proof, or customer media.

Use `references/workflows/section-asset-workflow.md` for unresolved gallery
jobs and inspection. That procedure applies the source/generation policies;
a behavioral hypothesis does not authorize synthetic product or result media.

## Plan Handoff

Add this compact block to `page plan`:

```markdown
## Consumer decision model

**Primary visitor mode.** confirm | compare | explore | complete | replenish
**Top decision questions.** Three shopper questions this page must answer.
**Selected behavioral patterns.** At most three, each with observed evidence.
**First decision area.** Facts, proof, and action visible before deeper detail.
**Gallery jobs.** covered; missing; asset slots created for missing jobs.
**Guided merchandising.** relationship name, reason, 2-3 products or none.
**Risk and trust.** sourced proof/policy placed beside the relevant decision.
**Mobile context.** what remains visible or is repeated during long scroll.
**Hypothesis and metric.** one primary behavior change and measurement.
```

`/design-page` implements this block without reopening settled choices.
`/optimize` and `/ab-test` use it to form one controlled, measurable
hypothesis.

## Guardrails

- Treat every pattern as a testable hypothesis, not a guaranteed lift.
- Protect primary-product conversion when introducing cross-sells.
- Measure attach rate, AOV or revenue per visitor, conversion, margin,
  returns/refunds, and support questions as appropriate.
- Segment meaningful results by device, traffic source, new/returning status,
  and product family when data supports it.
- Never fabricate reviews, customer counts, scarcity, compatibility, savings,
  clinical outcomes, delivery promises, or personalization.
- Avoid dark patterns: preselected paid add-ons, hidden recurring terms,
  obstructive sticky controls, fake countdowns, confirmshaming, or difficult
  opt-out.

## Evidence Foundation

This framework synthesizes merchant-provided Shopify CRO research with:

- Baymard product-page, image-gallery, description, cross-sell, and mobile UX
  research: `https://baymard.com/research/product-page`
- Shopify related and complementary recommendation guidance:
  `https://shopify.dev/docs/apps/build/product-merchandising/recommendations`
- Shopify Search & Discovery recommendation guidance:
  `https://help.shopify.com/en/manual/online-store/search-and-discovery/product-recommendations`
- Nielsen Norman Group progressive-disclosure guidance:
  `https://www.nngroup.com/articles/progressive-disclosure/`
- UK Competition and Markets Authority guidance on urgency and price-reduction
  claims: `https://www.gov.uk/government/publications/online-choice-architecture-how-digital-design-can-harm-competition-and-consumers`

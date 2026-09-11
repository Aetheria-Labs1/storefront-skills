# Copy frameworks

The eleven copy frameworks the page-type checklists name in
`copy_framework`, with the same ids: `pas`, `aida`, `bab`, `4ps`, `fab`,
`story-lead`, `listicle`, `comparison`, `hook-story-offer`, `answer-first`,
`qualifier-lead`. `/plan-page` records one in the Page type block
(`**Copy framework.**`) and the headline pattern; `/design-page` Compose
step 8 writes every section to that skeleton. Word ceilings here are the
defaults; a page-type file may tighten them, never loosen them. Vocabulary
limits are in `references/anti-patterns/copy-anti-patterns.md`; headline
and CTA mechanics in `references/copy/headline-and-cta-rules.md`; source
language in `references/copy/voice-of-customer-mining.md`.

Skeleton conventions: square brackets are slots the writer fills from the
worksheet or a ledger row (`[shopper phrase]`, `[ledger number]`,
`[product]`). A bracket left in rendered copy is CP29 BLOCK. Every skeleton
below is written in sentence case, without the blacklist, without
exclamation marks or em dashes; copy that leaves the skeleton keeps those
properties.

Severity BLOCK, FAIL, WARN. Tag LAW, RESEARCH, OPERATOR, HEURISTIC.

## 1. Rules

| Id | Rule | Sev | Tag |
| --- | --- | --- | --- |
| CF1 | One primary framework per page, chosen from the type checklist's `copy_framework` list and recorded in the plan. | FAIL | OPERATOR |
| CF2 | The framework matches the plan's awareness level (section 4). Cold traffic never gets `fab` or `answer-first` as the primary frame; most-aware never gets `story-lead` or `aida`. Schwartz, Breakthrough Advertising. https://sorinadumitru.com/breakthrough-advertising-by-eugene-schwartz/ | FAIL | RESEARCH |
| CF3 | Stacking: the primary framework fixes section order; sections may use a secondary frame (pas hero, fab product body, bab proof, 4ps close). Record secondaries as "sections: fab (features), bab (reviews)". | WARN | OPERATOR |
| CF4 | Stage names never appear in copy ("Problem:", "Proof:", "Call to action"). | FAIL | OPERATOR |
| CF5 | Ceilings: h1 at most 10 words, subhead at most 20, paragraph at most 45 words, section body inside the ceiling in section 2, whole page inside the type's `sections.max`. | FAIL | RESEARCH |
| CF6 | Every slot that is a number, name, quote, study, count or price resolves to a `verified` proof-ledger or offer-ledger row before render. An unresolved slot is deleted with its sentence, never estimated. | BLOCK | LAW |
| CF7 | `listicle`: 5 to 7 items; item 1 answers the category's main objection; the product is named by item 2; a CTA after every 2 to 3 items and after the last; the last item is the guarantee, the offer or an identity line; every item carries one specific (number, material, time, test); at most one fear-framed item; each item 40 to 120 words. Teardowns, Part D section 1. | FAIL | RESEARCH |
| CF8 | `comparison`: same attribute set and units in every column; no blank competitor cell without a sourced reason; a "not for you if" line; named competitors only with a public source per cell (DP20). | FAIL | LAW |
| CF9 | `story-lead` and `hook-story-offer` on `advertorial`, `video-sales-page` or `listicle`: the narrator is a real named person from the proof ledger (founder-note, expert-quote, review-with-media) or the brand in first person; never an invented journalist, patient or "our editor". The page carries the Advertisement label (DP13). | BLOCK | LAW |
| CF10 | `answer-first`: the first sentence of every section, and of every FAQ answer, is the answer (a number, a yes or no, a date, a price). | FAIL | OPERATOR |
| CF11 | `qualifier-lead`: the first two sections name who the page is for and who it is not for, in the shopper's words. | FAIL | OPERATOR |
| CF12 | `aida` is never the primary frame on `bof` or most-aware types; it educates people who already know. | WARN | RESEARCH |
| CF13 | Second person carries the page: "you" and "your" outnumber the brand name in body copy. | WARN | RESEARCH |

## 2. The frameworks

### pas (Problem, Agitate, Solve)
- Structure: name the problem in the shopper's words; make its cost concrete (time, money, embarrassment, a scene); present the product as the mechanism that removes it.
- Sections: `hero` (problem), `problem` or `agitation`, `solution` or `mechanism`, `benefits`, proof beside the mechanism, `offer`, `faq`, `closing-cta`.
- Fits: problem-aware; `ad-landing-page`, `advertorial` (hero and first third), `listicle` item 1, `quiz-funnel` intro, `lead-capture-giveaway`, popups.
- Ceilings: problem 60 words, agitation 90, solution 90; one agitation section only.
- Skeleton:
```text
h1: [problem in the shopper's words, no product name]           e.g. Still awake at 2am after the third cup
sub: [what the shopper has tried and why it fails, one sentence]
problem: [the scene] [what it costs, one number from a ledger row or none]
solution: [product] [mechanism in plain words]. [what changes, with the timeframe the reviews report]
proof beside it: [verbatim ledger quote that mentions the mechanism]
cta: [verb + object + price or outcome]
```
- Failure modes: agitation that shames the shopper (DP6 adjacent); a solution that restates the problem; inventing the cost number; more than one agitation section.

### aida (Attention, Interest, Desire, Action)
- Structure: earn the stop with one specific; hold attention with the mechanism or a demonstration; build wanting with proof and the outcome scene; ask once.
- Sections: `hero`, `how-it-works` or `mechanism`, `benefits` with proof, `reviews`, `offer`, `closing-cta`.
- Fits: unaware to solution-aware; `homepage`, `lookbook-shop-the-look`, `seasonal-gifting`, `lead-capture-giveaway`; whole-page arc for cold traffic when no story or list frame fits.
- Ceilings: hero 45 words total; interest 120; desire 120; one closing ask plus the checklist's repeats.
- Skeleton:
```text
h1: [one specific about the outcome or the product, no adjective]   e.g. Sheets that stay cool past 3am
sub: [who it is for] [the mechanism in five words]
interest: [how it works, 2 to 3 sentences with one number]
desire: [the outcome scene in second person] + [ledger quote]
action: [verb + object] with [price, shipping, guarantee line]
```
- Failure modes: attention bought with a rhetorical question or "Imagine"; desire written as adjectives instead of proof; the ask before interest on cold traffic.

### bab (Before, After, Bridge)
- Structure: the before state in the shopper's words; the after state as observed by real customers; the product as the bridge with the mechanism and timeframe.
- Sections: `problem` (before), `results-timeline` or `before-after` or `reviews` (after), `mechanism` (bridge), `routine`, `offer`.
- Fits: solution-aware; `ugc-creator-collab`, `trial-sample`, `subscription` value section, proof sections on any type; `before-after` islands where the category permits (`references/proof/before-after-and-claims.md`).
- Ceilings: before 60 words, after 90, bridge 90.
- Skeleton:
```text
before: [the shopper's own description of the current state, from the worksheet]
after: [what customers report, verbatim ledger quotes with timeframe]   e.g. "by week three the itching stopped" (ledger P4)
bridge: [product] does this by [mechanism]. Most people use it [cadence from usage instructions].
cta: [verb + object]
```
- Failure modes: an after state the merchant asserts rather than a customer reports; results without the FTC typicality line (CP4); before/after imagery in the hero (proof-ledger rule 9).

### 4ps (Promise, Picture, Proof, Push)
- Structure: one measurable promise; the picture of life with it; stacked proof that the promise is kept; the push as offer plus risk reversal.
- Sections: `hero` (promise), `benefits` or `usage` (picture), `reviews`, `stats`, `certifications`, `case-study` (proof), `offer`, `guarantee`, `closing-cta` (push).
- Fits: product-aware, higher ticket or higher scepticism; `pdp-hybrid-landing`, `bundle-kit`, `subscription`, `offer-page`, `retargeting-warm`, high-AOV `pdp`.
- Ceilings: promise 25 words; picture 90; proof modules inside the checklist range; push 60 words.
- Skeleton:
```text
h1: [product] + [strongest verified claim or offer]   e.g. The 40-litre cabin bag that fits every Indian carrier's sizer
sub: [who it is for] [the one spec that makes the claim true]
picture: [two sentences of use, second person, one number]
proof: [review-summary row] + [two ledger quotes of different length] + [certification or test-data row]
push: [offer ledger terms in one line] + [guarantee sentence] + cta [verb + object + price]
```
- Failure modes: a promise with no unit; proof pooled in one block instead of beside the claim; a push that adds urgency the ledger does not hold (DP1).

### fab (Feature, Advantage, Benefit)
- Structure: for each feature, what it does, then what that means for the shopper; publish the benefit, keep the feature as the evidence.
- Sections: `features`, `specs`, `materials`, `ingredients`, `science`, `comparison` rows, PDP description accordions.
- Fits: product-aware, spec-heavy goods; `pdp`, `ingredient-science`, `wholesale-b2b`, `comparison-us-vs-them` rows; the product body on any type.
- Ceilings: one feature per paragraph, 35 words; 4 to 6 features; specs as a table, not prose.
- Skeleton:
```text
h2: [benefit in the shopper's words]                  e.g. Warm without the itch
p:  [feature: material, number, standard], so [advantage], so [benefit with a situation].
    e.g. 18.5 micron merino (ledger), so it does not prickle, so you can wear it on skin on a nine-hour flight.
table: [spec] | [value from catalog] | [what it means]
```
- Failure modes: feature lists with no "so that"; adjective-only bullets; hidden specs in accordions on decision items (CA10); numbers not traceable to the catalog.

### story-lead
- Structure: a person, a situation, a failed alternative, a discovery, the mechanism, proof, a soft hand-off, then the offer. Editorial voice, price late.
- Sections: `dateline`, `hook`, `story`, `discovery`, `mechanism`, `reviews`, `offer-bridge`, `faq`, `closing-cta`.
- Fits: unaware and problem-aware; `advertorial`, `brand-story-founder`, `video-sales-page` companion text.
- Ceilings: hook 60 words; story 250 total across `story` and `discovery`; mechanism 120; the first CTA after section 4 as the checklist requires.
- Skeleton:
```text
label: Advertisement
h1: [news or identity framing, no product name]      e.g. Why nurses on night shift are switching how they wash their hair
hook: [one sentence that states the situation the reader recognises]
story: [narrator, a real person from the ledger, first person or reported] tried [alternatives] and [what happened].
discovery: [how the mechanism was found or explained], [one number]
mechanism: [how the product does it, plain]
proof: [ledger quotes], [expert-quote row if any]
offer-bridge: [what the product is, the price, the guarantee], cta [next-step verb + object]
```
- Failure modes: an invented narrator; a fake masthead or byline (DP13); price or "sale" language in the first third; more than 250 words before the mechanism.

### listicle
- Structure: a numbered headline with the audience or a verified count; 5 to 7 numbered items that each answer an objection or state a mechanism with one specific; CTAs interleaved; quotes after the list; guarantee, offer or identity as the last item.
- Sections: `hero`, optional `trust-bar`, `list-item-1` to `list-item-n`, `reviews`, `offer` or `buy-box`, `guarantee`, `closing-cta`; optional `faq`.
- Fits: problem-aware to solution-aware; `listicle`, `gift-guide` (by recipient), `seo-buyers-guide` (with `toc`, `methodology` and a `comparison` table added).
- Ceilings: CF7 items 40 to 120 words; headline 10 words.
- Skeleton:
```text
h1: [N] reasons [audience] are switching to [product or category]      (N from the item count; audience from the persona)
sub: [proof-strip: ledger rating and count, or the one-line premise]
1. [heading answering the category objection]  [specific]  [one sentence of why]
2. [product named; the mechanism]
3. [benefit with a number]         cta after item 3
4. [comparison or third-party fact with source]
5. [guarantee or offer or identity line]      cta
quotes: [two to three ledger quotes, varied length]
```
- Failure modes: a year in the headline (CA29); "reason" items that are adjectives; every item the same length; an offer item that invents urgency; conflicting counts (CA28).

### comparison
- Structure: a decision headline; a table with the same rows for every column; a fair "in focus" paragraph on the main rival; the verdict as a conditional ("choose them if, choose us if"); proof; CTA.
- Sections: `hero`, `comparison` or `us-vs-them`, `alternatives`, `verdict`, `reviews`, `faq` as decision questions, `closing-cta`.
- Fits: solution-aware and product-aware; `comparison-us-vs-them`, `seo-buyers-guide` table, intra-range `pdp` tables, `bundle-kit` tier tables.
- Ceilings: 5 to 8 rows, 3 columns at most (us, named rival, others); verdict 60 words.
- Skeleton:
```text
h1: [product] or [rival]: which [job] is right for you
table rows: [price per unit] | [material or dose] | [warranty or returns] | [delivery] | [what reviewers say, count]
in focus: [rival] does [thing] well. It [the honest trade-off, sourced].
verdict: Choose [rival] if [condition]. Choose [product] if [condition].
faq: [decision questions in the shopper's words]
```
- Failure modes: blank rival cells; units that differ per column; superlatives in the verdict (CP2); rival facts without a public URL in the ledger.

### hook-story-offer
- Structure: a scroll-stopping specific (the hook); a founder or customer story that explains the mechanism; the offer stacked with its terms and guarantee.
- Sections: `hook` or `hero`, `founder-note` or `story`, `mechanism`, `reviews`, `offer` with `savings-math` if a bundle, `guarantee`, `closing-cta`.
- Fits: unaware to solution-aware in sophisticated categories (supplements, skincare, sleep) where a named mechanism beats a bigger promise; `video-sales-page`, `launch-waitlist-preorder`, `advertorial`.
- Ceilings: hook 25 words; story 200; offer block 80.
- Skeleton:
```text
hook: [one falsifiable specific from the worksheet]          e.g. 3,000 mg of magnesium glycinate in one scoop, no sugar
story: [founder name and title from the ledger] made this because [the real reason, one paragraph].
mechanism: [why it works, two sentences, one number]
offer: [ledger price], [what is included], [savings math if any], [guarantee], [shipping]
cta: [verb + object + price]
```
- Failure modes: a hook that is a question or "Imagine"; a story with no named person; an offer with terms hidden below the CTA (OF12).

### answer-first
- Structure: the answer in the first sentence of every unit; then the one-line reason; then the detail for those who scroll.
- Sections: `faq`, `shipping-returns`, `pricing`, `offer`, `restock` hero, `thank-you-post-purchase` steps, `referral-loyalty-vip` rules, `collection-landing` intro.
- Fits: most-aware and support intent; `faq-support-led`, `offer-page`, `sale-clearance-flash`, `restock`, `thank-you-post-purchase`, `referral-loyalty-vip`, `retargeting-warm`, `collection-landing`; the FAQ on every type.
- Ceilings: first sentence 12 words; unit 60 words; FAQ 5 to 7 items.
- Skeleton:
```text
h1: [the thing the shopper came for, stated]        e.g. Back in stock: the 750 ml bottle, ₹1,299, ships tomorrow
unit: [answer]. [reason]. [detail or link]
faq q: [objection as the shopper types it]     a: [yes or no or number]. [one sentence why].
cta: [verb + object]
```
- Failure modes: answers that start with context; marketing questions in the FAQ (CP26); burying shipping and returns below product questions (HC22).

### qualifier-lead
- Structure: the headline or first section selects the reader (who this is for, who it is not for); then the diagnosis or routing; then the recommendation with its reason.
- Sections: `qualifier`, `quiz` or `product-finder`, `results-timeline`, `plan-selector`, `benefits`, `faq`, `closing-cta`.
- Fits: any awareness when there are many SKUs or a narrow fit; `quiz-funnel`, `trial-sample`, `subscription` plan selection, `wholesale-b2b`, `size-guide` sections, intra-range comparisons.
- Ceilings: qualifier 60 words; each routing question 12 words; result page recommendation 90 words with the reason.
- Skeleton:
```text
h1: [for whom] [the outcome]                          e.g. For hair that sheds in the shower: a routine by stage
qualifier: This is for you if [three concrete conditions]. It is not for you if [two conditions]; try [alternative] instead.
routing: [one question per screen, plain words, real progress count]
result: [product] because [the answers that led here]. [what to expect and when, from usage and reviews].
cta: [verb + object]
```
- Failure modes: a question headline that does not actually select (CP8); fake "analysing" delays (DP22); a result that ignores the answers.

## 3. Page type to default framework

| Type id | Primary | Secondary by section | Headline pattern |
|---|---|---|---|
| `ad-landing-page` | `pas` (problem-aware) or `4ps` (product-aware) | fab body, bab proof | problem in their words, or product + claim |
| `pdp` | `fab` | answer-first faq | product name + one specific |
| `pdp-hybrid-landing` | `4ps` | fab body | product + strongest claim |
| `advertorial` | `story-lead` | pas hook | news or identity, no product |
| `listicle` | `listicle` | pas item 1 | N reasons [audience] ... |
| `seo-buyers-guide` | `listicle` | comparison table, answer-first intro | best [category] for [use], ranked |
| `comparison-us-vs-them` | `comparison` | fab rows | [A] or [B]: which [job] |
| `quiz-funnel` | `qualifier-lead` | pas intro | for whom + outcome |
| `bundle-kit` | `4ps` | fab per item | the set + what it does |
| `offer-page` | `answer-first` | 4ps push | product + offer + terms |
| `sale-clearance-flash` | `answer-first` | none | what is reduced, until when |
| `seasonal-gifting` | `aida` | answer-first cutoffs | occasion + cutoff date |
| `gift-guide` | `listicle` (by recipient) | none | gifts for [recipient] under [price] |
| `launch-waitlist-preorder` | `hook-story-offer` | answer-first terms | outcome + ship date |
| `restock` | `answer-first` | none | it is back + price + ships |
| `subscription` | `4ps` | qualifier-lead plan pick, answer-first terms | product + cadence + savings |
| `ugc-creator-collab` | `bab` | none | creator's own claim |
| `video-sales-page` | `hook-story-offer` | none | the hook |
| `brand-story-founder` | `story-lead` | none | why we exist, specific |
| `ingredient-science` | `fab` | comparison | ingredient + what it does |
| `collection-landing` | `answer-first` | fab cards | category + for whom |
| `homepage` | `aida` | answer-first trust line | outcome + who for |
| `lookbook-shop-the-look` | `aida` (minimal copy) | none | the look, named |
| `lead-capture-giveaway` | `pas` or `aida` | none | the incentive, exact |
| `referral-loyalty-vip` | `answer-first` | none | give X, get Y |
| `retargeting-warm` | `answer-first` (objections) | 4ps push | still deciding + the objection answered |
| `thank-you-post-purchase` | `answer-first` | none | what happens next |
| `faq-support-led` | `answer-first` | none | the question itself |
| `trial-sample` | `bab` | answer-first what-happens-after | try it for [price] |
| `wholesale-b2b` | `fab` | answer-first terms | MOQ, lead time, margin |

## 4. Awareness to framework

| Awareness | Allowed primary | Never primary | Headline leads with |
|---|---|---|---|
| unaware | `story-lead`, `hook-story-offer`, `aida` | `fab`, `answer-first`, `4ps` | a story, an identity, a surprising specific |
| problem-aware | `pas`, `story-lead`, `listicle`, `qualifier-lead` | `fab`, `answer-first` | the problem in their words |
| solution-aware | `listicle`, `comparison`, `bab`, `aida`, `qualifier-lead` | `story-lead` alone | mechanism or outcome and why this one |
| product-aware | `fab`, `4ps`, `comparison`, `qualifier-lead` | `story-lead`, `aida` | product + strongest claim or offer |
| most-aware | `answer-first`, `4ps` | `story-lead`, `aida`, `pas` | product + offer + terms |

## Sources

- Schwartz, Breakthrough Advertising (awareness and sophistication): https://sorinadumitru.com/breakthrough-advertising-by-eugene-schwartz/ ; https://www.getlandra.com/blog/5-stages-of-awareness
- Framework catalogues: https://thrivethemes.com/copywriting-formulas/ ; https://www.articos.com/blog/copywriting-frameworks ; https://scalegrowth.digital/resources/content/copywriting-formulas/
- Listicle structure and mid-list CTAs: Nik Sharma, https://sharmabrands.com/blogs/newsletter/how-to-scale-a-brand-to-5-million-in-revenue ; teardowns in internal research audit (2026-09-10) Part D
- Fascination bullets: https://www.breakthroughmarketingsecrets.com/blog/writing-powerful-bullets-and-fascinations-core-copywriting-skill/
- Second person and sentence length (Apple): https://neilpatel.com/blog/write-copy-like-apple/

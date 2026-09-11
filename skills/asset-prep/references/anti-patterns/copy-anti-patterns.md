# Copy anti-patterns

The canonical vocabulary and structure blacklist for generated page copy.
`/design-page` applies it in Compose step 8; `brand_kit.banned_phrases`
is merged in at run time. Positive rules for headlines, CTAs, FAQs and
microcopy are in `references/copy/headline-and-cta-rules.md`; frameworks in
`references/copy/copy-frameworks.md`; sourcing real language in
`references/copy/voice-of-customer-mining.md`.

Scope of a hit. FAIL when the word or structure appears in an `h1`, `h2`,
`h3`, subhead, button, link label, CTA microcopy or announcement bar. WARN
when it appears in body text fewer than two times; FAIL at two or more body
hits. Text inside `<blockquote>` and review islands is exempt: reviews are
verbatim (`references/proof/proof-ledger.md` rule 4).

Severity BLOCK, FAIL, WARN describes the editorial rule, not permission to
invent claims. Review authored copy outside verbatim quotes against this list
on the persisted source and hosted page; no local extraction script is used.

## 1. Evidence

- Kobak et al., Science Advances 2024/25, 15M PubMed abstracts: after ChatGPT, 379 style words spiked; "delves" 28x, "underscores" 13.8x, "showcasing" 10.7x; 66 percent of excess style words are verbs. https://arxiv.org/html/2406.07016v5
- Pangram (vendor, per 10k words, AI vs human): em dashes 17 vs 2 (10x), triads 19 vs 5 (4x), "not just X but Y" 3 vs 1 (3x), "delve into" class phrases 30 vs 3, bullet lists 9x, emoji 2x. https://www.pangram.com/signs-of-ai-writing
- Community catalogues derived from Wikipedia "Signs of AI writing": antithesis cadence, "from X to Y" sweeps, colon reveals, fragment punchlines. https://github.com/crypdick/unslop/blob/main/skills/unslop/references/ai-writing-patterns.md
- Copyhackers/Beachway: a headline lifted from a real review beat the marketing-written one by over 400 percent in clicks. Real language wins; generic language loses. https://copyhackers.com/2014/10/amazon-review-mining/

## 2. Vocabulary blacklist

CP1 (FAIL in headings and controls; WARN then FAIL in body; RESEARCH, OPERATOR). None of the following appears outside verbatim quotes. The lint list is the union of the three blocks plus `brand_kit.banned_phrases`.

Verbs and verb phrases:
```text
elevate, unleash, unlock (except a literal gate: "Unlock free shipping at ₹999" is allowed), delve, embrace, indulge,
discover (as an imperative opener), experience (as an imperative opener), transform your, revolutionize, revolutionise,
empower, harness, leverage, supercharge, streamline, optimize (consumer copy), reimagine, redefine, showcase, foster,
navigate (metaphorical), dive into, take ... to the next level, say goodbye to, say hello to, look no further, treat yourself
```

Adjectives and nouns:
```text
seamless, effortless, game-changer, game-changing, revolutionary, cutting-edge, next-level, next-generation, state-of-the-art,
world-class, best-in-class, innovative, unparalleled, unmatched, unrivalled, ultimate, premium (unqualified; allowed inside a tier or product name),
luxurious (unqualified), exquisite, meticulous, meticulously, intricate, curated, bespoke (unless made to order), artisanal (unless hand-made),
holistic, synergy, robust, tapestry, realm, journey (metaphorical), landscape (metaphorical), testament, beacon, pivotal, crucial,
vibrant, dynamic, must-have, perfect for, stunning, breathtaking, elevated, sleek, effortlessly chic
```

Phrases and openers:
```text
elevate your routine, in today's fast-paced world, whether you're X or Y, it's not just X, it's Y, not just ... but (also), more than just,
Imagine ... (opener), Picture this, Introducing (headline), crafted with care, crafted with love, premium quality, designed with you in mind,
the perfect blend of, at its finest, like never before, you deserve, the secret to, your go-to, made for modern life, we've got you covered,
sit back and relax, the best part?, here's the thing, let's face it, in a world where, gone are the days, nestled, boasts, a testament to,
from X to Y and everything in between, welcome to, at [Brand], we believe, discover the difference, experience the difference, the ultimate,
your journey, level up, game on, ready to ..., unlock your potential, step into, dive in
```

Allowlist handling. `brand_kit.allowlist` (or the plan's "Copy allowlist" line) removes a term when it is literal: a brand named "Elevate", a tier named "Premium", a hair oil that is literally "curated" by a named person. Every allowlisted hit is recorded in `page plan` with the reason.

## 3. Claims

| Id | Tell | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| CP2 | Superlatives and objective claims without substantiation: best, #1, No.1, most trusted, most advanced, clinically proven, doctor recommended, dermatologist tested, award-winning, 100% natural, chemical-free, toxin-free, guaranteed results, proven to | FTC: objective claims need a reasonable basis before publication; "clinically proven" needs that evidence. India ASCI/CCPA: "No.1" only with market-share data; disclaimers may not contradict the claim. Each hit must map to a proof-ledger row (`test-data`, `award`, `certification`, `customer-count`). https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business ; https://www.ascionline.in/wp-content/uploads/2022/09/asci_june_july_2020_ccc_pr.pdf | BLOCK | LAW |
| CP3 | Hedged non-claims: may help support, can help promote, is believed to, designed to help, supports healthy ... | Either a substantiated fact with a number, or cut the sentence. Where regulation mandates a hedge (supplement structure/function claims), keep the mandated wording and pair it with dose, ingredient or study n. | WARN | OPERATOR |
| CP4 | "Results not typical" or "results may vary" as the only qualifier beside a results testimonial | FTC Endorsement Guides: disclose the generally expected result in the same block; the bare disclaimer does not comply. https://www.govinfo.gov/content/pkg/CFR-2023-title16-vol1/pdf/CFR-2023-title16-vol1-part255.pdf | BLOCK | LAW |

## 4. Structure tells

| Id | Tell | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| CP5 | Em-dash chains | At most one em dash per 150 words; none in headings, buttons or subheads. Prefer a full stop. Pangram: 10x more em dashes in AI text. | FAIL | RESEARCH |
| CP6 | Rule of three everywhere ("soft, breathable, and durable") | At most one adjective triad per section. Lists of specifics beat adjective triads. | WARN | RESEARCH |
| CP7 | Antithesis: "not just X, it's Y", "isn't just ... it's", "more than just" | Zero. | FAIL | RESEARCH |
| CP8 | Rhetorical-question openers ("Tired of ...?", "Ever wondered ...?") | At most one question heading per page; never the h1 unless the type uses `qualifier-lead` and the question genuinely selects the reader. | WARN | OPERATOR |
| CP9 | "Imagine ..." or "Picture this" | Zero. | FAIL | RESEARCH |
| CP10 | Exclamation marks | Zero outside verbatim reviews. | FAIL | OPERATOR |
| CP11 | Uniform sentence and paragraph length | Standard deviation of sentence length at least 4 words per section; no three consecutive paragraphs within 10 percent of the same word count. | WARN | HEURISTIC |
| CP12 | Identical section rhythm (headline, subhead, three bullets, CTA, repeated) | Adjacent sections never share the same layout skeleton (`references/anti-patterns/design-anti-patterns.md` DA14). | FAIL | OPERATOR |
| CP13 | Alliterative or fragment triad headlines ("Pure. Potent. Proven.") | At most one fragment-triad heading per page. | FAIL | RESEARCH |
| CP14 | Summary and conclusion language ("In conclusion", "Ultimately", "Overall", "To sum up") | Zero. A landing page asks; it does not conclude. | FAIL | OPERATOR |
| CP15 | Colon reveal in headings ("The result: skin that ...") | At most one per page. | WARN | RESEARCH |
| CP16 | Title Case Headings | Sentence case for headings, subheads, buttons, labels; product names keep brand casing. USAGov moved to sentence case sitewide in 2023 with no trust drop. https://www.usa.gov/blog/2023/09/making-the-case-for-sentence-case | FAIL | RESEARCH |
| CP17 | Bold-label bullets ("**Fast:** ...", "**Simple:** ...") | Zero. Write the specific. | FAIL | RESEARCH |
| CP18 | False ranges ("from busy parents to pro athletes") | Only when X and Y are real endpoints of one scale the merchant serves. | WARN | RESEARCH |
| CP19 | Generic openers ("Welcome to ...", "At [Brand], we believe ...", "We are passionate about") | Zero. Lead with the shopper's problem or a specific. | FAIL | OPERATOR |
| CP20 | Subhead restates the headline | The subhead resolves the headline (mechanism, proof or who it is for); token overlap with the h1 under 50 percent. | FAIL | OPERATOR |

## 5. Punctuation and case

| Id | Tell | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| CP21 | Hype punctuation: "!!", "?!", "..." trails in headings | Zero. | FAIL | OPERATOR |
| CP22 | ALL-CAPS words of six or more letters | None outside a `CAPS_ALLOWLIST` of acronyms and registered marks (GST, FSSAI, UPI, MRP, BIS, ISO, NSF, USDA, SPF, COD, EMI, BNPL). Labels of three words or fewer may be caps only under a merchant-stated rule (design-rules N5). | FAIL | RESEARCH |
| CP23 | Arrow glyphs or "->" in link and button text | Design-rules N12. | FAIL | OPERATOR |
| CP24 | Emoji anywhere in copy | Design-rules N1. | FAIL | OPERATOR |
| CP25 | Middle dots (U+00B7) joining meta strings ("Free shipping", dot, "30-day returns", dot, "Made in India") | Use a full stop or separate lines; N12 names middle-dot joins as chrome. | WARN | OPERATOR |

## 6. CTA and control copy

| Id | Tell | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| CP26 | Stock CTA labels: Shop Now, Get Started, Learn More, Buy Now (tof/mof), Submit, Click here, Continue (no object), OK, Yes, Go, Read more | Design-rules A12; `references/copy/headline-and-cta-rules.md` HC12 to HC14. The CTA is verb plus object plus outcome or price, at most four words, sentence case. | FAIL | OPERATOR |
| CP27 | CTA that does not start with a verb, or exceeds four words | HC12. | FAIL | OPERATOR |
| CP28 | "Free" with an asterisk or a later condition | Offers OF5: the condition sits in the same line. | BLOCK | LAW |

## 7. Placeholder and model leakage

| Id | Tell | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| CP29 | Placeholder text: lorem ipsum, TODO, TBD, [brand], [product], {{ }}, "Your headline here", "Insert ...", "Product name", "Lorem" | Zero. A12 already forbids placeholder copy. | BLOCK | OPERATOR |
| CP30 | Framework labels leaking into copy ("Problem:", "Agitate:", "Solution:", "Benefit:", "Call to action") | Zero. Frameworks shape the order, never the words. | FAIL | OPERATOR |
| CP31 | Assistant voice leaking ("As an AI", "Certainly", "Here's a", "I hope this helps", "Feel free to") | Zero. | BLOCK | OPERATOR |

## 8. Brand voice

| Id | Tell | Rule | Sev | Tag |
| --- | --- | --- | --- | --- |
| CP32 | A `brand_kit.banned_phrases` entry appears | BLOCK in any position, including body. Merged into the lint list at run time; the plan's "Copy allowlist" cannot override a merchant ban. | BLOCK | OPERATOR |
| CP33 | Register mismatch with `voice_md` (jokey copy for a clinical brand; clinical copy for a playful brand) | Reviewed by an LLM pass against the voice adjectives and "we say / we don't say" pairs; not regex. | WARN | OPERATOR |
| CP34 | Brand name outnumbers "you/your" | Second person leads; Apple's iPhone 5 copy used "you/your" more than "iPhone" and "Apple" combined. https://neilpatel.com/blog/write-copy-like-apple/ | WARN | RESEARCH |
| CP35 | Spelling locale drift (color and colour on one page) | One locale from `brand_kit` or the store market. | WARN | OPERATOR |

## 10. Rewrite procedure for a hit

1. Ask Harry Dry's three questions of the sentence: can the reader visualise it, can it be falsified, could no competitor say it. A line failing all three is deleted, not rephrased. https://www.demandcurve.com/lessons/fundamental-rules-of-good-copy
2. Replace the banned word with what specifically happens: "seamless" becomes "arrives assembled, no tools"; "premium quality" becomes the material, weight or test.
3. Pull the replacement from the voice-of-customer worksheet (`references/copy/voice-of-customer-mining.md`) before inventing one.
4. Re-run the section checks; a heading hit blocks compile, a body hit produces a rewrite note in `QA record` with the span and the rule id.

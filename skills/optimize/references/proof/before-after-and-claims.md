# Before/After and Claims

Substantiation procedure behind the `before-after`, `test-data`,
`case-study`, `expert-quote` and `founder-note` rows of the plan's `## Proof
ledger` (`references/proof/proof-ledger.md`), plus the wording table for
every efficacy or superlative claim a page makes. An image that implies a
result is a performance claim; the advertiser must be able to substantiate it
as if it had stated the result in words. Rule tags: LAW, RESEARCH ([H] [M]
[L]), OPERATOR, HEURISTIC.

## Before/after protocol

All rows must hold before a `before-after` row reaches `verified`.

| Requirement | Detail | Why |
|---|---|---|
| Genuine | real customer or study participant; not a supplier, stock or generated image | ASA v. Laser Treatment Clinic 2018 (supplier stock images failed) |
| Same subject | one person, one product, one regimen | ASA "genuine and representative" |
| Same framing | same camera distance, angle, lens, lighting, background, expression; same makeup or hair state | ASA v. BetterMe 2024 |
| Unretouched | no retouching, filters, colour grading or smoothing beyond identical global adjustments applied to both; original files with EXIF retained | EU Reg. 655/2013 honesty criterion |
| Interval stated | elapsed time and regimen on the image ("8 weeks, twice daily") | FTC 255.2; EU 655/2013 |
| Consent | written consent naming this surface (website) and duration | CAP 3.45; GDPR |
| Typical result | the generally expected result from a study or customer data, in the same visual field | FTC 16 CFR 255.2(b) |
| Category permitted | see the verticals table | drug and medical claim regimes |
| Dated | capture dates for both frames | ASA recency and genuineness |

## Law and rulings

| Jurisdiction | Rule | Effect on the page | Source |
|---|---|---|---|
| US | 16 CFR 255.2(a): a testimonial or image implying a result is a claim the advertiser must substantiate | study or customer data on file before the image renders | https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising |
| US | 16 CFR 255.2(b): if the result is not typical, disclose the generally expected result clearly and conspicuously; "results may vary" and "results not typical" are inadequate | a typicality sentence with the number, not a hedge | FTC small-business FAQ https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business |
| UK | ASA requires before/after images to be genuine and representative; supplier stock fails; an "illustrative" caption cannot save an invented image; a small "actor portrayal" caption cannot contradict the impression a real user got the result | protocol table above, no fictitious imagery | Laser Treatment Clinic https://www.asa.org.uk/rulings/the-laser-treatment-clinic-ltd-a18-447095.html ; GTMC https://www.asa.org.uk/rulings/gtmc-inc-a13-225085.html ; BetterMe https://www.asa.org.uk/rulings/betterme-ltd-a24-1238625-betterme-ltd.html |
| EU | Reg. (EU) 655/2013 common criteria for cosmetic claims: truthfulness, evidential support, honesty (no embellishment by selective presentation or misleading imagery), no results achievable only under exceptional conditions | same as UK plus claim wording | summary https://care-europe.com/blog/eu-cosmetic-claims-regulation-655-2013-marketing-compliance/ |
| India | CCPA 2022 Guidelines: claims substantiated; disclaimers cannot correct a misleading claim and must be prominent and in the ad's language; ASCI Code chapter I | typicality text in the ad's language, not a footnote | https://consumeraffairs.nic.in/theconsumerprotection/guidelines-prevention-misleading-advertisements-and-endorsements-misleading |
| India | Drugs and Magic Remedies (Objectionable Advertisements) Act 1954 schedule and Schedule J of the Drugs and Cosmetics Rules 1945: no advertising that a product cures or treats listed conditions (includes baldness, obesity, premature greying, height increase) | no "treats", "cures", "regrows" framing for listed conditions; verify the schedule before any health framing | verify issuer text before relying |

## Which verticals may use before/after

| Status | Verticals and claims | Extra condition |
|---|---|---|
| Allowed | cosmetics and skincare (appearance: hydration, radiance, texture, tone), haircare (shine, frizz, manageability), oral care appearance (surface whitening), home cleaning (stain, grime, limescale), fitness apparel and equipment (with the programme disclosed), pet grooming, furniture and home restoration | protocol table plus typicality sentence |
| Restricted (study on file with matching endpoints, medical or regulatory sign-off recorded) | weight loss, supplements with body-composition claims, hair regrowth, acne, rosacea or eczema "improvement", dark-circle or pigmentation "reduction", posture or pain devices | never in the hero; study citation beside the image; India: check the DMR schedule |
| Prohibited | anything implying treatment, cure, prevention or diagnosis of a medical condition; anything for a listed DMR Act condition in India; any image of a minor's body | drop the row; tell the merchant why |

## Placement and labels

| Property | Rule |
|---|---|
| Section | `before-after` inside benefits or evidence, after the mechanism explanation |
| Never | in the hero (`imagery.hero: before-after` in a type checklist still requires the protocol and is forbidden for restricted verticals); never generated, composite or "illustrative" |
| Crop | identical crop for both frames; one slider or a side-by-side pair; labels "Before" and "After <interval>" |
| Typicality | one sentence in the same visual field: "In our 8-week study of 60 participants, average improvement was 23%; this participant saw 41%." |
| Disclaimer | "Individual results vary" only in addition to the typicality sentence, where the category requires it; never alone |
| Consent line | "Shared with permission" where the subject consented to naming; otherwise no name |
| Count | one pair per claim; a results page (`ugc-creator-collab` results variant) may carry 4 to 8 labelled pairs with product, duration and frequency on each (Hello Face pattern) |
| Motion | slider answers a drag only; no auto-wipe (`design-rules.md` N10) |

## Claims substantiation table

Every claim below is a `test-data`, `certification`, `award`, `case-study`
or `customer-count` row before design. `#1` and count claims also follow
`references/proof/numbers-and-counts.md`.

| Claim | Evidence required | Regulator | Permitted phrasing | Never |
|---|---|---|---|---|
| Efficacy ("reduces frizz", "removes limescale") | product test with method, n, date; endpoints match the claim | FTC reasonable basis; CAP 3.7; EU 655/2013; CCPA 2022 | "Reduced frizz by 36% in a 4-week consumer test (n=52)" | the adjective alone |
| Clinical ("clinically tested", "clinically proven") | tested: a clinical study exists on this formulation; proven: endpoints and population match the claim | same; FTC "competent and reliable scientific evidence" for health | "In a 12-week clinical study of 60 women, 87% reported <result>" | "clinically proven" from a supplier study of a different formulation or dose |
| Consumer-perception percentages ("93% saw results") | survey with n, design, duration, question wording | CAP 3.7; FTC; ASCI | "93% of 100 users saw visible results in 8 weeks (self-assessment)" | the percentage without n and design |
| "#1", "number one", "best-selling" | third-party panel data (Nielsen, NielsenIQ, Mintel, Kantar) covering the stated market and period, or a platform's badge with a dated screenshot | ASA (Post Office, Vitabiotics upheld; Skinny Tan ruled misleading); FTC; CCPA | "Best-selling face serum on Nykaa, Beauty > Serums, 4 Sep 2026" | "#1 in India" without source, category and period |
| "Award-winning" | award name, body, year, body's own URL | CAP 3.7; FTC | "Winner, Allure Best of Beauty 2025" | "award-winning" alone; awards older than 24 months without the year |
| "As recommended by", "doctors recommend" | a survey of the profession with n and method, or a named expert with the endorsement rules below | FTC "two out of three doctors" rule; CCPA | "Recommended by 82% of 100 dermatologists surveyed, Mar 2026" | "dermatologist recommended" without a survey |
| "Doctor-formulated", "developed with dermatologists" | the named professional's role, credential, registration number, involvement documented | FTC 255.3; CCPA; ASCI health addendum | "Formulated with Dr. <name>, MD, dermatologist (reg. no.)" | an unnamed "team of doctors" |
| "Dermatologist tested" | tolerance study report with dermatologist, n, protocol | FTC; EU 655/2013 | "Dermatologist-tested (RIPT, n=52, 2025)" | as an outcome claim |
| Sustainability ("sustainable", "eco-friendly", "carbon neutral") | third-party scheme or public-authority label; life-cycle data for any specific claim | EU Dir. 2024/825 from 27 Sep 2026; CMA Green Claims Code; FTC Green Guides | "Packaging is 80% post-consumer recycled PET (GRS cert no.)" | "eco-friendly"; offset-based "carbon neutral" (EU) |
| "Natural", "100% natural" | ingredient list; definition used; percentage by weight where "100%" or "natural origin" is claimed | FTC; EU 655/2013; ISO 16128 as a reference standard | "97% ingredients of natural origin (ISO 16128)" | "100% natural" with any synthetic ingredient |
| "Clean" | the brand's published exclusion list | FTC (must not imply competitors are unsafe) | "Formulated without <listed ingredients>" with the list linked | "clean" as a safety claim |
| "Non-toxic", "chemical-free", "safe" | absolute safety claims are rarely substantiable; ASA has upheld against "chemical-free" | CAP 3.7; FTC; EU 655/2013 (denigrating "free from" claims) | "Formulated without parabens and phthalates" | "non-toxic", "chemical-free", "100% safe" |
| "Hypoallergenic" | patch or RIPT study | FTC; EU Technical Document on claims | "Fragrance-free; patch-tested on 50 subjects" | as a badge |
| "Results in N days" | study or customer data showing the result at N days for the typical user | FTC 255.2(b); ASA; ASCI | "Most users reported softer skin by day 14 in our 60-person study" | "Visible results in 7 days" with no data |
| Guarantee ("money-back", "lifetime") | policy page with exact terms | CAP 3.1; CCPA; `references/offers/offer-ledger.md` | "30-day money-back guarantee (full refund, unopened or opened)" | "money-back" for store credit; "lifetime" undefined |
| Comparative ("2x longer lasting than <rival>") | head-to-head test with method and date; rival identified truthfully | CAP 3.33 to 3.40; FTC; India ASCI chapter IV | "Lasted 2.1x longer than <rival> in our lab wear test, Jun 2026" | "than other brands" without data |

## Expert, doctor and founder endorsements

| Endorser | Agent may render | Agent may write | Must hold |
|---|---|---|---|
| External expert (dermatologist, nutritionist, engineer, chef) | verbatim quote with name, credential line, registration number where the profession has one, date, connection label ("Paid advisor", "Received free product", "No compensation") | nothing; no paraphrase, no "based on Dr X's review" | written approval; evidence the expert examined the product; expertise in the thing endorsed (16 CFR 255.3) |
| Certifying organisation | logo or statement per `references/proof/trust-badges-certifications.md` | nothing | authorisation |
| Founder | first-person note signed with name and role ("Priya M., Founder"), drawn from the merchant's brief | a draft from the brief for the founder's approval; no invented customer stories or numbers | approved text; role stated (insider testimonial, FTC 465.5) |
| Employee | quote only with the role in the attribution | nothing | disclosure |
| Celebrity or influencer | only with a signed agreement, disclosure label, current usage term | nothing | agreement on file; India: ASCI celebrity due diligence (₹40 lakh or 500k followers) |
| Health or finance influencer (India) | quote only with qualification stated upfront | nothing | ASCI addendum Aug 2023 |

A credential line, not a logo: the strongest pages name the person and role
("Dr. Lindsey Zubritsky, dermatologist (@dermguru)"; "Dr. Matt Feder, PT,
DPT, CSCS") and put them in the top fifth of the page. Zero of fifteen PDPs
in the teardown sample carried an expert quote; homepages and bundles did
(internal teardown audit, 2026-09-10).

## Ledger row templates

```markdown
| P7 | before-after | "visible in 8 weeks" | study participant 14 | asset ids <before>, <after>; captured 2026-01-10 and 2026-03-07; same lens, light, angle; EXIF kept; regimen twice daily; consent 2026-03-20 (website, 24 months); typical result 23% (study S-02) | merchant study file S-02 | before-after | verified |
| P17 | test-data | "87% reported softer skin" | merchant | study S-02: 60 participants, 12 weeks, self-assessment, Jan 2026, CRO <lab> | PDF on file | benefits | verified |
| P18 | expert-quote | "the barrier repair is real" | Dr. <name>, MD, dermatologist, reg. no. | verbatim text; approval email 2026-07-02; "Paid advisor" | merchant record | expert-endorsement | verified |
| P19 | founder-note | trust | <founder>, Founder | approved text 2026-09-01 | merchant approval | founder-note | verified |
| P20 | before-after | "reverses hair loss" | merchant | supplier image; no subject data | none | — | dropped (supplier image; restricted claim) |
```

## Rules

BA1. Never render a before/after pair without the full protocol: genuine, same subject, same framing and lighting, unretouched originals with EXIF, interval and regimen on the image, consent for this surface, dates. LAW ASA Laser Treatment Clinic 2018, BetterMe 2024; EU 655/2013.
Check: the ledger row lists all nine protocol fields; a missing field makes the row `dropped`.

BA2. State the generally expected result in the same visual field; "results may vary" or "results not typical" never stands alone. LAW 16 CFR 255.2(b); India CCPA 2022 (disclaimers cannot cure).
Check:
```bash
perl -0ne 'while(/<!-- section: before-after[a-z-]* -->(.*?)(?=<!-- section: |\z)/gs){my $b=$1; print "hedge-only\n" if $b=~/results (may|will) vary|results not typical/i && $b!~/\d+%|\d+ (of|out of) \d+|average/i}' $W/lexsis-source.html   # no output
```

BA3. Never a supplier, stock, generated, composite or "illustrative" before/after image; a caption does not cure it. LAW ASA GTMC 2013; FTC 465.2; OPERATOR (no generated result imagery, `references/assets/generation-policy.md`).
Check: both assets are imports with capture dates; provider is never generated; `grep -ciE 'illustrative|actor portrayal|dramatisation' $W/lexsis-source.html` is 0.

BA4. Restricted verticals render before/after only with a study on file whose endpoints match the depicted result and with the study cited beside the image; prohibited claims are dropped and the merchant told why. LAW FTC health substantiation; DMR Act 1954 and Schedule J (India); EU 655/2013.
Check: for restricted rows, the `test-data` row id is cited in the `before-after` row; for any "treat", "cure", "regrow", "heal" verb in source, the plan records regulatory sign-off or the verb is absent.
```bash
grep -ciE '\b(cures?|treats?|heals?|regrows?|reverses?|eliminates?) (acne|eczema|psoriasis|hair loss|baldness|obesity|wrinkles|greying)' $W/lexsis-source.html   # 0
```

BA5. Before/after never sits in the hero and never autoplays a wipe; labels "Before" and "After <interval>" on identical crops. HEURISTIC; consistent with `proof-ledger.md` display rule 9; `design-rules.md` N10.
Check: DOM order places `before-after` after `mechanism`, `how-it-works` or `benefits`; `grep -c '@keyframes' $W/page-theme.css` unchanged by the section.

BA6. Every efficacy, clinical, comparative, superlative and sustainability claim maps to a `test-data`, `certification`, `award` or `customer-count` row with method, n, date and source; the permitted phrasing carries the parameters. LAW CAP 3.7; FTC reasonable basis; EU 655/2013; CCPA 2022; Dir. 2024/825.
Check:
```bash
grep -ciE 'clinically (proven|tested)|dermatologist (tested|recommended)|#1|number one|best[- ]selling|award[- ]winning|eco[- ]friendly|non[- ]toxic|chemical[- ]free|100% (natural|safe)|doctor[- ]formulated' $W/lexsis-source.html   # each hit maps to a ledger row id and carries n, date or issuer in the same element
```

BA7. "Clinically proven" is used only when the study's endpoints, population and formulation match the claim; otherwise "clinically tested" with the parameters, or nothing. LAW FTC; EU 655/2013.
Check: the `test-data` row states formulation, endpoint and population; a mismatch downgrades the wording.

BA8. Percentages from surveys or studies carry n, design and duration in the same element or a numbered footnote visible on the same screen. LAW CAP 3.7; ASCI; RESEARCH teardown pattern 9 (AG1, LOAM disclose design and n).
Check: every `\d+%` in a proof, benefits or stats section has `n=`, `of \d+`, or a footnote marker within the same element.

BA9. Expert quotes render only as verbatim approved text with name, credential line, registration number where applicable, date and connection label; the agent writes none of it. LAW 16 CFR 255.3 and 255.5; CCPA 2022; ASCI health addendum.
Check: each `expert-quote` row has approval date and connection label; the rendered attribution contains a credential, not a logo.
```bash
grep -ciE '(doctors|dermatologists|experts|nutritionists) (recommend|agree|love|trust)' $W/lexsis-source.html   # 0 unless a survey row exists
```

BA10. Founder notes are signed with name and role, drafted only from the merchant's brief, approved before render, and contain no customer stories or numbers that lack their own rows. LAW FTC 465.5 (insider testimonial disclosed by role); HEURISTIC teardown pattern 22.
Check: `founder-note` section contains a name and a role word ("Founder", "Co-founder"); every numeral inside it has a ledger row.

BA11. Absolute safety words ("non-toxic", "chemical-free", "100% safe", "no side effects") are replaced by the specific fact or removed. LAW CAP 3.7 (ASA upheld against "chemical-free"); FTC; EU 655/2013 "free from" criteria.
Check: `grep -ciE 'non[- ]toxic|chemical[- ]free|100% safe|no side effects|zero side effects' $W/lexsis-source.html` is 0.

BA12. Comparative claims name the comparator truthfully and hold a head-to-head test with method and date; "vs other brands" without data is removed. LAW CAP 3.33 to 3.40; FTC; ASCI chapter IV.
Check: each `\d+x` or "than" comparison in source cites a `test-data` row; no "leading brands" or "other serums" comparator without a named panel.

BA13. Every claim row appears under "Claims to confirm" in `page-plan.md`; a claim the merchant cannot document is removed from copy, not softened with "up to" or "may help". LAW hedge words do not substitute for evidence (CAP 3.7; FTC). HEURISTIC `references/proof/numbers-and-counts.md`.
Check: `grep -ciE 'up to \d+%|may help|can help (reduce|improve)|helps? support' $W/lexsis-source.html` is 0 in proof and benefits sections unless the row's evidence states a range.

## Sources

- FTC Endorsement Guides 2023 (255.2, 255.3, 255.5): https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising ; 255.3 text: https://www.law.cornell.edu/cfr/text/16/255.3
- FTC advertising FAQs (typicality, doctor claims): https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business ; FTC 2009 revision speech: https://www.ftc.gov/sites/default/files/documents/public_statements/look-forward-ftc-advertising-and-marketing-enforcement-challenges/100203eraspeech.pdf
- ASA rulings: Laser Treatment Clinic https://www.asa.org.uk/rulings/the-laser-treatment-clinic-ltd-a18-447095.html ; GTMC https://www.asa.org.uk/rulings/gtmc-inc-a13-225085.html ; BetterMe https://www.asa.org.uk/rulings/betterme-ltd-a24-1238625-betterme-ltd.html
- "Number one" rulings: Post Office https://www.mondaq.com/uk/advertising-marketing-branding/128488/asa-adjudications-snapshot-february-2011 ; Vitabiotics https://www.naturalproductsonline.co.uk/news/company-news/asa-satisfied-vitabiotics-is-uks-number-one-vitamin-company/ ; Skinny Tan https://www.bbc.co.uk/news/entertainment-arts-41664183
- EU Reg. 655/2013 summary: https://care-europe.com/blog/eu-cosmetic-claims-regulation-655-2013-marketing-compliance/ ; Directive 2024/825: https://eur-lex.europa.eu/eli/dir/2024/825/oj
- India CCPA 2022 Guidelines: https://consumeraffairs.nic.in/theconsumerprotection/guidelines-prevention-misleading-advertisements-and-endorsements-misleading ; ASCI Influencer Guidelines and health addendum: https://www.ascionline.in/social/wp-content/uploads/2025/04/ASCI-Influencer-Guidelines.pdf ; ASCI celebrity guidelines: https://www.ascionline.in/wp-content/uploads/2023/08/guidelines-for-celebrities-in-advertising.pdf
- FTC consumer alert on AI-doctored endorsements: https://consumer.ftc.gov/consumer-alerts/2024/04/did-celebrity-really-endorse-maybe-not
- Teardowns: labelled before/afters (Hello Face), study footnotes with n and design (AG1, LOAM), credential lines: internal research audit (2026-09-10) Part D.5 items 8, 9, 20.

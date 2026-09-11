# Trust Badges and Certifications

Sourcing, wording and display rules behind the `certification`, `guarantee`,
`policy-fact` and payment-badge rows of the plan's `## Proof ledger`
(`references/proof/proof-ledger.md`). A badge is a claim that a named issuer
vouched for this product or facility; the agent holds the issuer, the
certificate or licence id and the scope before the mark exists in source.
Rule tags: LAW, RESEARCH ([H] [M] [L]), OPERATOR, HEURISTIC. Rows marked
"verify issuer" were not in the research corpus; read the issuer's own rules
before first use.

## What moves conversion, and where

| Element | Finding | Where it belongs | Source |
|---|---|---|---|
| Payment method logos | familiar consumer brands (Visa, Mastercard, PayPal, Google, UPI) score highest for perceived security; 49% had no seal preference | beside the primary CTA and at checkout, only methods the store has enabled | CXL trust seals study [M] https://cxl.com/research-study/trust-seals/ |
| Guarantee or returns line | approved-seller and safe-checkout badges raised stated purchase likelihood 77% and 76% | beside the CTA, mirrored from the policy page | Trustpilot survey n=1,697 [M] https://uk.business.trustpilot.com/guides-reports/build-trusted-brand/why-and-how-social-proof-influences-consumers |
| SSL and security vendor seals | shoppers judge perceived, not technical, security from cues around card fields; a homemade "secure checkout" badge outperformed every SSL seal except Norton | checkout card fields only; landing-page noise elsewhere | Baymard 2013 to 2023 [H] https://baymard.com/blog/perceived-security-of-payment-form |
| Self-drawn padlock or "Secure checkout" | acceptable UI decoration at checkout | checkout only; never labelled a certification, never naming a vendor | Baymard, same |
| Third-party review platform badge | Trustpilot logo plus stars raised trust 8% and conversion propensity 9% | near reviews as the platform's live widget, count shown | London Research UK 2026 [M] https://business.trustpilot.com/guides-reports/build-trusted-brand/the-impact-of-trustpilot-through-the-retail-customer-journey |
| Certification marks | authorisation required to display any trust or quality mark | product benefits or `certifications` section with issuer text | CAP 3.46 [H] https://www.asa.org.uk/type/capcode/code%5Frule/3.46.html ; UCPD Annex I points 2 and 4 |

Teardown evidence: 13 of 15 PDPs put shipping, returns and warranty chips
directly under the CTA; certification badges sat in a benefits or footer row,
never in the hero (internal teardown audit, 2026-09-10).

## Badge placement by type

| Badge type | Section | Condition to render | Wording constraint |
|---|---|---|---|
| Payment logos | `buy-box`, `payment-options`, `sticky-cta` | method enabled in store payment settings (`lexsis_catalog.get` or merchant confirmation) | logos only; no "100% secure" adjectives |
| Guarantee or returns | `trust-bar`, beside CTA | policy page states the exact term | mirror policy text; "money-back" only when refunds are cash, not store credit; link the policy |
| Warranty | `trust-bar`, `guarantee` | warranty terms document | duration and what is covered; "lifetime" only with the policy's definition |
| Security seals (Norton, McAfee) | checkout only | live subscription; vendor's own live seal | never a painted vendor logo |
| Review platform badge | `review-summary`, `reviews` | live widget from the platform; paid plan where the platform requires it | count shown; static assets carry "rating as of <Month Year>" |
| Certification marks | `certifications`, `ingredients`, `materials` | certificate id, issuer, scope, expiry on file; product in scope | exact issuer wording (table below) |
| Origin statement | `sourcing`, `legal` | supply-chain documentation | plain "Made in India"; government "Make in India" lion logo needs permission |

## Certification wording by mark

| Mark or phrase | What it means | Render only if | Say | Never say |
|---|---|---|---|---|
| FDA approved | premarket approval for drugs, some devices, colour additives; FDA does not approve cosmetics, supplements, foods or facilities | approved NDA, ANDA or PMA exists | "FDA-approved <drug or device>, application no." | "FDA approved" on any cosmetic, supplement, food or packaging |
| FDA registered facility | a facility filed registration; not approval; FDA warning letters call it misbranding on consumer copy (Jul 2025) | avoid on pages | nothing | "Made in an FDA registered facility" as a badge |
| FDA compliant, structure/function disclaimer | US supplement claims need the DSHEA disclaimer ("This statement has not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.") | US traffic and a structure/function claim | the DSHEA disclaimer verbatim beside the claim | "FDA compliant" as a badge |
| GMP or cGMP | manufacturing under GMP regulation; "certified" implies a third-party certificate | certifier (NSF, UL, SGS), certificate id, date | "Made in a facility certified to NSF/ANSI 455-2 GMP by <certifier>, cert no." | "GMP certified" without certifier; "FDA GMP certified" |
| USDA Organic | 95%+ organic ingredients, accredited certifier; seal is a protected trademark | certificate and product listed | seal per 7 CFR 205.311; "Certified organic by <certifier>" | seal on "made with organic" products; "organic" without certification in the US |
| India Organic (Jaivik Bharat, NPOP) | FSSAI organic logo for certified organic food in India | NPOP or PGS certificate; verify issuer | logo plus certifier | "organic" on uncertified food (FSSAI Organic Foods Regulations 2017) |
| FSSAI | mandatory licence and logo on food labels in India | 14-digit licence number | "FSSAI Lic. No. <14 digits>" with logo | "FSSAI approved", "FSSAI certified" |
| AYUSH licence | state manufacturing licence for Ayurvedic, Siddha, Unani products | licence number; verify issuer | "Manufactured under AYUSH licence no." | "AYUSH approved", "AYUSH certified" |
| CDSCO cosmetics licence (India) | state manufacturing licence under Cosmetics Rules 2020; imports need CDSCO registration | licence or registration number; verify issuer | in the `legal` block only | "CDSCO approved" as a badge |
| ISO 9001, 14001, 22000 | the management system is certified, not the product; the ISO logo may never be used | certificate id, certifier, scope | "Manufactured by <Co.> whose quality management system is certified to ISO 9001:2015 by <certifier>" | "ISO certified product", ISO logo, "ISO 9000 certification" |
| BIS ISI mark | product certification with a CM/L licence; mandatory for QCO categories (toys since 1 Jan 2021) | CM/L number; product in scope; verify issuer | ISI mark with "CM/L-<number>" | ISI mark on out-of-scope goods; "BIS approved" |
| BIS CRS (electronics, India) | compulsory registration for listed electronics | "R-<number>" on file; verify issuer | "BIS R-<number>" in specs or legal | "BIS certified quality" |
| CE | manufacturer's self-declaration for products in scope of EU directives | Declaration of Conformity; category in scope | mark on product or packaging as required | "CE certified", "CE approved", CE on cosmetics or textiles |
| UL Listed | UL tested the product to a safety standard; file number | UL file number; verify issuer | "UL Listed, file no." | "UL approved"; "UL certified" for a Recognized component |
| FCC | equipment authorisation; FCC ID for certified radios | FCC ID or SDoC on file; verify issuer | "FCC ID: <id>" | "FCC approved" |
| Energy Star, BEE star label | listed model on the programme's register | model listed; verify issuer | programme label as issued | star graphics the programme did not issue |
| Leaping Bunny | cruelty-free certification licensed to certified brands only | brand on leapingbunny.org and holds a logo licence | logo per brand guidelines | resellers displaying it for brands they carry |
| PETA cruelty-free or vegan | listed in PETA's programme; logo licensed | brand listed; verify issuer | "PETA-certified cruelty-free" | "PETA approved" for unlisted brands |
| Vegan Society trademark | product registered with a licence number | registration; verify issuer | trademark with registration | generic "vegan certified" without a certifier |
| COSMOS, ECOCERT | organic or natural cosmetic certification by a named body | certificate; verify issuer | "COSMOS ORGANIC certified by Ecocert" | "ECOCERT approved" |
| Made Safe | ingredient screening certification | certificate; verify issuer | "MADE SAFE certified" | "toxin-free" as the badge |
| Non-GMO Project Verified | product-specific verification with a seal licence | listing; verify issuer | "Non-GMO Project Verified" | "GMO-free" as a badge |
| NSF Certified for Sport, Informed Sport, USP Verified | product or lot listed by the programme | listing URL; verify issuer | programme name and listing | "third-party tested" without the lab, report id and date |
| Gluten-free (US) | FDA definition under 20 ppm; GFCO certifies at 10 ppm | test report or GFCO certificate; verify issuer | "Gluten-free (tested below 20 ppm, <lab>, <date>)" | "gluten-free certified" without certifier |
| Halal, Kosher | certifier-issued marks | certifier and certificate; verify issuer | certifier's mark with name | generic crescent or "kosher style" badge |
| OEKO-TEX Standard 100 | textile tested for harmful substances; certificate and institute | certificate number verifiable at oeko-tex.com; verify issuer | label with certificate number and institute | "OEKO-TEX approved fabric" without number |
| GOTS, GRS, RWS, Fairtrade, FSC, bluesign | supply-chain certifications with licence numbers | licence number and certified supply chain; verify issuer | mark with licence number | mark on uncertified products; "eco-friendly" as a substitute |
| CertiPUR-US, GREENGUARD Gold | foam certification; UL low-emission certification | product listed; verify issuer | "CertiPUR-US certified foam" | "certified mattress" |
| CPSIA, ASTM F963, EN 71 (toys, baby) | US Children's Product Certificate; EU toy standard under CE | CPC or test report; verify issuer | "Tested to ASTM F963 by <lab>" | "child-safe certified" |
| AAFCO (pet food, US) | AAFCO publishes profiles; it does not certify or approve | nutritional adequacy statement on label; verify issuer | "Formulated to meet AAFCO <profile>" | "AAFCO approved", "AAFCO certified" |
| Dermatologist tested | a dermatologist was involved in a tolerance study; no outcome implied | study report: dermatologist, n, protocol, date | "Dermatologist-tested (RIPT, n=52, 2025)" | "dermatologist approved or recommended" without a survey of dermatologists (FTC two-thirds rule) |
| Clinically tested vs proven | tested: a study exists; proven: endpoints match the claim | study on file with matching endpoints | "In a 4-week study of 60 women, 87% reported <result>" | "clinically proven" from a supplier study of a different formulation |
| Hypoallergenic, natural, non-comedogenic | no legal definition in the US or EU; still must not mislead | documented test or ingredient basis | the specific fact: "fragrance-free; patch-tested on 50 subjects" | a standalone badge |
| Cruelty-free, vegan (words) | unregulated words; EU common criteria bar claims that restate a legal minimum | supplier declarations on file; verify for EU pages | "No animal testing by us or our suppliers" with the policy linked | "cruelty-free certified" without a certifier |
| Made in India, country of origin | Legal Metrology rules require origin on listings | supply-chain documents | "Made in India" | "Make in India" lion logo without permission; "Made in India" for imports packed in India |
| Sustainability labels (EU traffic) | Directive 2024/825 bans labels not based on a third-party scheme or public authority from 27 Sep 2026; offset-based carbon-neutral claims banned | scheme name and certificate | official scheme logo | self-designed "eco", "green", "planet-friendly" badges; "eco-friendly" |
| B Corp, 1% for the Planet | company-level membership or certification | current certification; verify issuer | "Certified B Corporation" | "B Corp certified product" |

## Vertical badge sets

Payment logos and the guarantee line sit beside the CTA on every vertical.
The set below is what may fill `certifications` when the ledger verifies it.

| Vertical | Typical verifiable set | Never |
|---|---|---|
| Beauty and skincare | dermatologist-tested with report; Leaping Bunny or PETA when licensed; COSMOS or ECOCERT; Made Safe; Vegan Society; CDSCO licence in `legal` | FDA approved; FDA registered facility; "chemical-free" |
| Supplements | GMP certifier and cert id; NSF Certified for Sport, Informed Sport or USP Verified when listed; third-party lab with COA id; FSSAI nutraceutical licence (India); DSHEA disclaimer (US) | FDA approved; "clinically proven" without matching study |
| Food and beverage | FSSAI licence; USDA Organic or India Organic; Non-GMO Project; gluten-free with test; Halal or Kosher certifier; FSSC 22000 as a system statement | "FSSAI approved"; "organic" without certificate; ISO logo |
| Fashion and textiles | OEKO-TEX with number; GOTS, GRS, RWS licence; Fairtrade; bluesign | "eco-friendly" badge; "sustainable" without scheme (EU) |
| Home and sleep | CertiPUR-US foam; GREENGUARD Gold; OEKO-TEX; FSC licence; warranty and trial nights from policy | "certified mattress"; "non-toxic" as a badge |
| Electronics | BIS CRS R-number (India); CE; FCC ID; UL Listed file; Energy Star or BEE label; warranty terms | "BIS certified quality"; "CE certified" |
| Baby and kids | BIS ISI (toys, India); ASTM F963 or EN 71 test report; OEKO-TEX; BPA-free with material declaration | "paediatrician recommended" without survey; "child-safe certified" |
| Pet | AAFCO statement (US); FSSAI or state licence where applicable; ingredient sourcing documents | "vet recommended" without survey; "AAFCO approved" |

## Visual rules

| Property | Rule |
|---|---|
| Mark | the issuer's own SVG, or a monochrome SVG redrawn to the issuer's brand rules where they permit it; never generated art, never a raster screenshot |
| Colour | monochrome in the page's neutral unless the issuer's rules require its colours |
| Issuer text | visible text beside the mark: issuer, and certificate or licence number where the issuer requires it on consumer surfaces |
| Count | three to five per row; fewer is fine |
| Layout | one row, one height, one section; never repeated per section, never in the hero |
| Size | one cap height; 24 to 40px tall at 1280 |
| Link | to the issuer's register entry when a public register exists |
| Icons | no emoji, no icon-tile stack (`design-rules.md` N1, N3, N12) |

## Ledger row template

```markdown
| P4 | certification | "FSSAI licensed" | merchant | licence no. 10012345678901; issuer FSSAI; scope: manufacturing unit, Pune; valid to 2027-03-31 | merchant document 2026-09-08 | trust-bar | verified |
| P11 | certification | "GMP facility" | merchant | NSF/ANSI 455-2 certificate C0123456 to <manufacturer>; issuer NSF; expiry 2027-01-15 | PDF on file; NSF listing URL | certifications | verified |
| P12 | policy-fact | "30-day returns" | store policy | https://<store>/policies/refund-policy ; "30 days, unopened" | fetched 2026-09-10 | trust-bar | verified |
| P13 | certification | "dermatologist tested" | merchant | none supplied | none | — | dropped (no test report) |
```

## Rules

TB1. Render a certification mark only when the ledger row holds issuer, certificate or licence id, scope and expiry, and the product or facility is in scope. LAW CAP 3.46 (no trust mark without authorisation); UCPD Annex I 2 and 4.
Check: every `certification` row has four evidence fields; rows with "none" are `dropped`.

TB2. Use the issuer's permitted wording from the table; never "approved", "certified" or "registered" for an issuer that does not approve, certify or register that thing. LAW FDA (cosmetics, supplements and foods are not FDA approved); ISO and IAF rules; FSSAI licensing; AAFCO.
Check:
```bash
grep -ciE 'FDA[- ]approved|FDA[- ]registered|FSSAI[- ](approved|certified)|ISO[- ]certified product|AAFCO[- ](approved|certified)|CE[- ](certified|approved)|UL[- ]approved|AYUSH[- ](approved|certified)|BIS[- ]approved' $W/lexsis-source.html   # 0
```

TB3. Never render the ISO logo, the government "Make in India" lion, an Amazon badge, or any issuer's mark for which the merchant holds no logo licence. LAW ISO logo policy; Legal Metrology and DPIIT logo permission; Amazon trademark licence.
Check: `grep -ciE 'iso\.org|make-in-india|amazon.?s choice|best seller badge' $W/lexsis-source.html` is 0 in `<img` and `<svg` contexts.

TB4. Payment logos show only methods enabled in the store; security seals appear at checkout only; a self-drawn padlock is never labelled a certification or given a vendor name. RESEARCH [H] Baymard perceived security; OPERATOR (payment methods from the catalogue or merchant).
Check: each payment logo in source matches the store's enabled methods list recorded in the plan; `grep -ciE 'norton|mcafee|ssl secured|256-bit' $W/lexsis-source.html` is 0 on non-checkout pages.

TB5. Guarantee and returns badges mirror the policy page text and link to it; "money-back" only for cash refunds; "free returns" only when the shopper pays nothing. LAW CAP 3.1; CCPA 2022; consistent with `references/offers/offer-ledger.md`.
Check: each guarantee string in source is a substring of the fetched policy page or the merchant's written confirmation; the element is inside `<a href="<policy URL>">` or adjacent to one.

TB6. For EU-facing pages after 27 Sep 2026, a sustainability label renders only when based on a third-party certification scheme or set by a public authority; generic environmental claims and offset-based carbon-neutral claims are removed. LAW Directive (EU) 2024/825 Annex I 2a, 4a, 4c.
Check:
```bash
grep -ciE 'eco[- ]friendly|planet[- ]friendly|earth[- ]friendly|carbon[- ]neutral|climate[- ]neutral|100% sustainable|green product' $W/lexsis-source.html   # 0 unless the ledger names a recognised scheme for that exact claim
```

TB7. "Dermatologist tested", "clinically tested", "hypoallergenic", "non-comedogenic" render only as the specific fact with the study parameters, never as a standalone badge. LAW FTC substantiation; EU Reg. 655/2013 common criteria; `references/proof/before-after-and-claims.md`.
Check: each such phrase in source is followed within the same element by a parenthetical or footnote carrying n and date, or the ledger `test-data` row id.

TB8. Third-party review platform badges are the platform's live widget on the plan the platform requires; never a static star image; static exports carry "rating as of <Month Year>". LAW Trustpilot brand guidelines Sep 2026; Google Places policies.
Check: no `<img` whose `alt` or filename contains "trustpilot", "google reviews" or "stars"; widgets are the platform's script or iframe.

TB9. Three to five marks per row, one height, monochrome unless the issuer requires colour, issuer text beside each, one section, never in the hero, never repeated. HEURISTIC; consistent with `proof-ledger.md` display rule 7.
Check:
```bash
perl -0ne 'my $n=()=/<!-- section: certifications/g; print "sections=$n\n"; while(/<!-- section: certifications[a-z-]* -->(.*?)(?=<!-- section: |\z)/gs){my $b=$1; my $m=()=$b=~/<(svg|img)/g; print "marks=$m\n"}' $W/lexsis-source.html   # sections <= 1, 3 <= marks <= 5
```

TB10. No generated badge art: a badge asset never comes from `lexsis_drafts.asset_generate`; only issuer files or a monochrome SVG redraw the issuer permits. OPERATOR; consistent with `references/assets/generation-policy.md`.
Check: no asset with purpose `badge`, `seal` or `certification` has provider = generated in the manifest.

TB11. Never a percentage or superlative inside a badge ("100% safe", "clinically proven", "#1 dermatologist choice"); badges carry facts and issuers. LAW CAP 3.7; FTC reasonable basis; `design-rules.md` N9 forbids ALL-CAPS pills.
Check: `grep -ciE '100% (safe|natural|pure|secure)|#1 ' $W/lexsis-source.html` is 0 within `certifications` and `trust-bar` sections.

TB12. India `legal` block carries what the law requires (marketed by, country of origin, licence numbers, customer care) as text, not badges; nine of nine Indian PDPs in the teardown sample do this. LAW Legal Metrology (Packaged Commodities) Rules; FSSAI labelling. RESEARCH teardowns Part D.1.
Check: for `en-IN` stores, the `legal` section exists and contains "Marketed by" and "Country of origin".

TB13. Every badge row appears under "Claims to confirm" in `page-plan.md`; a badge the merchant cannot document by design time is `dropped`, not "pending in place". OPERATOR.
Check: no `certification` row with status `pending` has a section assigned.

## Sources

- Baymard perceived security: https://baymard.com/blog/perceived-security-of-payment-form ; site seals: https://baymard.com/blog/site-seal-trust
- CXL trust seals: https://cxl.com/research-study/trust-seals/
- Trustpilot social proof survey: https://uk.business.trustpilot.com/guides-reports/build-trusted-brand/why-and-how-social-proof-influences-consumers ; UK 2026: https://business.trustpilot.com/guides-reports/build-trusted-brand/the-impact-of-trustpilot-through-the-retail-customer-journey
- CAP 3.46: https://www.asa.org.uk/type/capcode/code%5Frule/3.46.html
- FDA "Is it really FDA approved": https://www.fda.gov/consumers/consumer-updates/it-really-fda-approved ; cosmetics authority: https://www.fda.gov/cosmetics/cosmetics-laws-regulations/fda-authority-over-cosmetics-how-cosmetics-are-not-fda-approved-are-fda-regulated ; 2025 warning letter on "FDA registered facility": https://www.einpresswire.com/article/858156475/health-and-natural-beauty-usa-corp-700187-07-28-2025
- USDA organic seal: https://www.ams.usda.gov/rules-regulations/organic/organic-seal
- FSSAI labelling compendium: https://www.fssai.gov.in/upload/uploadfiles/files/Comp_Labelling.pdf
- ISO/IAF packaging statement rules: https://committee.iso.org/files/live/sites/tc176/files/documents/Accreditation%20Auditing%20Practices%20Group%20docs/AAPG-Packaging_or_Accompanying_Information.pdf ; BIS mark rules: https://www.bis.gov.in/wp-content/uploads/2020/04/Chapter-30-BIS-Mark-and-Accreditation-Mark.pdf
- Leaping Bunny FAQ (resellers): https://www.leapingbunny.org/frequently-asked-questions
- Legal Metrology country of origin: https://www.medianama.com/2020/07/223-country-of-origin-e-commerce/
- Directive (EU) 2024/825: https://eur-lex.europa.eu/eli/dir/2024/825/oj ; Commission FAQ: https://commission.europa.eu/document/download/3c257883-bb2a-4dd9-a6dc-501d587bb34f_en?filename=ECGT+Directive+FAQ_20260518.pdf
- FTC advertising FAQs (doctor claims, substantiation): https://www.ftc.gov/business-guidance/resources/advertising-faqs-guide-small-business
- Dermatologist-tested wording [L]: https://laeyolabs.com/dermatologist-tested-mens-care-testing-scope-documentation-and-claim-wording/ ; claims overview [L]: https://www.spscommerce.com/community/articles/navigating-claims-natural-organic-clinically-proven-and-more
- Issuer registers to verify before first use: https://www.oeko-tex.com ; https://global-standard.org ; https://fsc.org ; https://www.nsfsport.com ; https://www.usp.org ; https://www.nongmoproject.org ; https://www.leapingbunny.org ; https://crueltyfree.peta.org ; https://www.bis.gov.in ; https://www.certipur.us ; https://www.aafco.org

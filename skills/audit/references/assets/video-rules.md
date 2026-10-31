# Video rules

When a storefront page gets video, where it goes, how it plays, and how the
plan records it. `/plan-page` decides whether a video slot exists;
`/design-page` writes the markup. The page type's `imagery.video` value
(`required`, `optional`, `forbidden`) in its checklist is the first gate.
Generated video follows `references/assets/generation-policy.md`; poster and
weight thresholds extend `references/assets/slot-spec.md`; UGC rights follow
`references/proof/ugc-rights-and-display.md`. Where `references/asset-prep.md`
says "never autoplay" this file is the rule: click to play by default, a
muted loop only under section 4.

Tags: LAW, RESEARCH, OPERATOR, HEURISTIC as defined in
`references/assets/image-jobs-by-page-type.md`.

## 1. What the evidence says

| Finding | Evidence | Rule it produces |
|---|---|---|
| Landing pages with video convert the same or worse than pages without, across goals, industries, channels and devices | Unbounce analysis of customer pages https://unbounce.com/landing-pages/video-on-landing-pages-means-more-conversions-right-wrong-heres-why/ | No video by default; a slot exists only for a named job |
| 59% of users skip product-page videos; 83% never try 360 views | Baymard https://baymard.com/ecommerce-design-examples/video-and-360-views | Video supplements a complete image set; it never replaces a gallery job |
| 35% of sites put video where users do not find it; tabs hide it from about a third | Baymard https://baymard.com/blog/embedding-product-page-videos | Embed in the gallery as a thumbnail with a play badge, or beside the objection it answers; never in a tab |
| 69% watch video with the sound off in public | Verizon Media and Publicis via Forbes https://www.forbes.com/sites/tjmccue/2019/07/31/verizon-media-says-69-percent-of-consumers-watching-video-with-sound-off/ | Every speech video has captions; nothing depends on audio |
| Viewers are 80% more likely to finish a video with captions | same study via MarketingCharts https://www.marketingcharts.com/digital/video-108656 | Captions always |
| Videos under one minute hold 50 to 52% average engagement; one to three minutes 46%; how-to holds attention best | Wistia https://wistia.com/blog/optimal-video-length | Length ceilings in section 3 |
| Food and beverage videos under one minute have the highest engagement of any category | Wistia 2026 report https://downloads.ctfassets.net/j7pfe8y48ry3/5tOf2aVNOvk9CValTgj83h/f577dc1aebb439a6904c253b9f80c23c/Wistia-2026-State-Of-Video-Report.pdf | Food pages may use a short muted pour or sizzle loop |
| Background video "can distract from the CTA" and must be muted | Unbounce https://unbounce.com/landing-pages/do-video-backgrounds-help-or-hurt-conversions/ | Hero loop only as the plan's single motion moment |
| Self-reported: 85% say a brand video convinced them to buy; 63% prefer a short video to learn about a product | Wyzowl 2026 (self-reported survey, weight accordingly) https://wyzowl.com/video-marketing-statistics/ | Demo video is a mid-page objection tool, not a hero |
| Autoplay with sound fails WCAG 1.4.2 (F93) and browsers block it | W3C https://www.w3.org/WAI/WCAG22/Techniques/failures/F93.html ; Chrome autoplay policy https://developer.chrome.com/blog/autoplay | Never autoplay with sound |
| Moving content over five seconds needs a pause, stop or hide control | WCAG 2.2.2 https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide | Pause control on every loop |

## 2. Does this page get video

| Condition | Decision |
|---|---|
| Checklist `imagery.video: forbidden` | No video slot |
| Checklist `imagery.video: required` (`video-sales-page`, `ugc-creator-collab`) | Hero is `video-poster`; the video is the page's main proof or pitch |
| Checklist `imagery.video: optional` and a real product video exists in Shopify media or the library | One gallery video slot (thumbnail with play badge) |
| `optional` and a decision question in the Consumer decision model is answered best by seeing motion (assembly, texture, pour, fit in movement) | One mid-page video slot beside that section, named after the objection |
| `optional` and rights-cleared UGC clips exist | UGC grid of one to three 9:16 clips beside testimonials |
| Traffic is TikTok or Reels and the ad was a video | Hero `ugc-screenshot` or `video-poster` from the same creative concept (`references/copy/message-match.md`) |
| No real video exists | No video slot. Generated video of the product or of people is NEVER (`generation-policy.md`); an abstract or backdrop loop is ASK and rarely worth it |

## 3. Placement, length and mode

| Placement | Section ids | Length | Play mode | Aspect | Poster | Captions |
|---|---|---|---|---|---|---|
| Hero loop | `hero` | 6 to 15 s, no speech | Muted autoplay loop only when named as the plan's one motion moment (N10); otherwise click to play | 16:9 desktop, 9:16 or 4:5 mobile | Required; the poster is the LCP candidate | n/a (no speech) |
| Gallery video | `gallery` | 20 to 60 s | Click to play from a thumbnail with a play badge | 1:1 or 4:5 to match the gallery | Required | Required if speech |
| Demo or how-to | `how-it-works`, `usage`, `routine`, `features`, `video` | 45 to 90 s; key claim in the first 5 s | Click to play | 16:9 or 1:1 | Required | Required |
| UGC or testimonial clip | `ugc-grid`, `video-testimonials`, `reviews` | 20 to 40 s | Click to play; grid, not carousel | 9:16 native | Required, a real frame | Required; paid disclosure when applicable |
| Founder story | `founder-note`, `story`, `about` | 60 to 120 s | Click to play | 16:9 | Required | Required |
| Video sales letter | `video` on `video-sales-page` | as the pitch requires; state duration in HTML | Click to play; progress visible | 16:9 | Required | Required, plus transcript |
| Shoppable video | `shoppable-video` | 15 to 45 s per clip | Click to play | 9:16 | Required | Required |

Lengths are HEURISTIC anchored to Wistia (above) and to Reels guidance of 5
to 15 s for loops (secondary source) https://www.mbadv.agency/meta-ads/meta-ads-formats-and-creative .

## 4. Click to play versus muted loop

| Attribute | Click to play (default) | Muted loop (exception) |
|---|---|---|
| When | Any video with speech; any demo, UGC, founder or VSL | A silent 6 to 15 s hero or texture loop that the plan names under "Motion" as the single moment (N10 in `references/design-rules.md`) |
| Markup | `<video controls playsinline preload="none" poster="...">` | `<video autoplay muted loop playsinline preload="metadata" poster="...">` plus a visible pause button |
| Audio | User-initiated | None; `muted` attribute present; no audio track preferred |
| Reduced motion | n/a | Do not autoplay when `prefers-reduced-motion: reduce`; show the poster |
| Save data | n/a | Do not autoplay on `navigator.connection.saveData`; show the poster |
| LCP | Poster is the LCP candidate; video never fetched before interaction | Poster is the LCP candidate; the first frame of an autoplaying video is also an LCP candidate https://web.dev/articles/lcp , so keep the poster present and the file small |
| Weight | Demo up to 15 MB; UGC clip up to 8 MB | Up to 1.5 MB |
| Count per page | As the placement table allows | At most one |

## 5. Technical spec

| Item | Rule | Source |
|---|---|---|
| Container and codec | H.264 MP4 always; WebM (VP9) or AV1 as an additional `<source>` when available | https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video |
| Resolution | 1080p ceiling for demos; 1080 x 1920 for UGC; never upscale a phone clip | HEURISTIC |
| `preload` | `none` for click to play; `metadata` at most for loops | https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video |
| `playsinline` | Always, so iOS does not force full screen | same |
| `poster` | Always; a real frame with the product and, where present, a face or hands; the play control drawn in HTML over it | Baymard embedding research (section 1) |
| Captions | `<track kind="captions" srclang="..." default>` WebVTT, or burned-in when the host cannot serve the track; required for any speech | WCAG 1.2.2 https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded |
| Transcript | A text transcript or media alternative in HTML below or linked, for any video that carries information not in the page copy | WCAG 1.2.1 and 1.2.3 https://www.w3.org/WAI/WCAG22/Understanding/audio-only-and-video-only-prerecorded , https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded |
| Pause control | Present for any motion over 5 s, including loops | WCAG 2.2.2 (section 1) |
| Music | Rights cleared for web commercial use; recorded in the plan | `references/proof/ugc-rights-and-display.md` |
| Hosting | Imported through `lexsis_asset_import.import` or served from Shopify product media; no third-party hotlinks; no third-party players that inject their own autoplay or cookies without consent | `references/assets/asset-sourcing-sequence.md` |
| Island | `HeroMedia` with `"autoplay": false` for click to play (`references/asset-prep.md`); a plain `<video>` for simple playback | house |

## 6. Poster and thumbnail rules

1. A real frame from the supplied video, chosen by viewing candidate frames,
   never the auto-selected first or black frame.
2. Shows the product and, where present, a face or hands; the same subject
   the video opens with, so the click is not a bait.
3. Meets the `hero-video-poster` or `ugc-tile-vertical` row in
   `references/assets/slot-spec.md`.
4. The play control is HTML over the poster, one style across the page, at
   least 48 px tap target (A11), never baked into the image.
5. Gallery video thumbnails carry the same play badge and sit in the
   thumbnail strip, not in a separate tab.
6. Alt on the poster describes the video's subject in the slot template
   form; duration is stated in adjacent HTML ("0:42").

## 7. Recording a video slot

Plan (`page plan`, "## Asset slots"): one row for the video and one for its
poster. Aspect names the video ratio; Source decision names the origin step,
the rights basis, the duration, and whether captions are burned in or a
track. UGC rows cite the proof-ledger id.

```markdown
| A5 | how-it-works | product_media (sequence, video 0:48) | 16:9 | shopify media video, captions: track, viewed | gid://shopify/Video/456 | verified |
| A6 | how-it-works | product_media (poster for A5) | 16:9 | derived frame 00:03, viewed | asset 4b7e... | verified |
| A9 | ugc-grid | proof (ugc video 0:31, ledger P5, paid: no) | 9:16 | library, rights record P5, captions: burned in | asset 71bb... | verified |
| A10 | ugc-grid | proof (poster for A9) | 9:16 | derived frame, viewed | asset 71bc... | verified |
```

Manifest (`page record`): one `assets[]` entry per row. A Shopify video
uses `sourceType: shopify` with `productId` and `mediaId`; an imported clip
uses `sourceType: lexsis` with `assetId`. The poster is its own entry. Caption
files and transcripts are not manifest entries; the plan row records how
captions ship. The plan's "Motion" line names the muted loop when one exists;
the Consumer decision model names the objection a demo video answers.

## 8. Rules

Checks use persisted MCP source and the hosted draft.

VR1. Plan a video slot only when the checklist requires it or the plan names the decision question the video answers. RESEARCH.
Rationale: video pages did not out-convert non-video pages https://unbounce.com/landing-pages/video-on-landing-pages-means-more-conversions-right-wrong-heres-why/ ; 59% skip product videos https://baymard.com/ecommerce-design-examples/video-and-360-views .
Check: every slot row containing "video" names a section and, unless `imagery.video: required`, the Consumer decision model lists the question it answers.

VR2. Never autoplay with sound; autoplay only muted, looped, silent, 6 to 15 s, and only as the plan's single motion moment. LAW.
Rationale: WCAG 1.4.2 and F93 https://www.w3.org/WAI/WCAG22/Techniques/failures/F93.html ; N10 in `references/design-rules.md`.

VR3. Give every video a `poster` that is a real frame showing the product. RESEARCH.
Rationale: auto-selected black frames read as broken; users must see what they get https://baymard.com/blog/embedding-product-page-videos .

VR4. Caption every video that has speech and provide a transcript or media alternative for information not in the page copy. LAW.
Rationale: WCAG 1.2.2 https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded ; 69% watch with sound off (section 1).
Check: each speech video has `<track kind="captions"` or its plan row says "captions: burned in"; a transcript block or link exists for VSL and demo videos.

VR5. Default to click to play with `preload="none"`; nothing but the poster is fetched before interaction. RESEARCH.
Rationale: video bytes compete with the LCP image https://web.dev/articles/optimize-lcp .

VR6. Keep the video file out of the LCP path; the poster carries the LCP role on video-led pages with `fetchpriority="high"` on the poster image. RESEARCH.
Rationale: LCP candidates include the poster and the first frame of autoplaying video https://web.dev/articles/lcp .
Check: in the hosted draft, `new PerformanceObserver(l => console.log(l.getEntries().at(-1).element)).observe({type:'largest-contentful-paint', buffered:true})` reports an `IMG` (the poster), not `VIDEO`.

VR7. Place demo video in the gallery thumbnail strip or beside the objection it answers; never inside a tab or accordion. RESEARCH.
Rationale: about a third of users miss tabbed content https://baymard.com/blog/embedding-product-page-videos .
Check: no `<video` or video island sits inside an element with `role="tabpanel"` or inside a collapsed accordion; gallery video thumbs appear in the same strip as image thumbs.

VR8. Respect the length ceilings by placement and put the key claim in the first five seconds. RESEARCH.
Rationale: engagement falls past one minute https://wistia.com/blog/optimal-video-length .
Check: the plan row's duration is inside the section 3 range for its placement.

VR9. Keep the native aspect: 9:16 for UGC and shoppable clips, 16:9 or 1:1 for demos; never letterbox one into the other. OPERATOR.
Rationale: letterboxing shrinks the product and reads as repurposed content; Meta's 9:16 for Reels and Stories https://www.facebook.com/business/help/103816146375741 .
Check: each `<video>` `width`/`height` ratio matches the source file's ratio (from the import response).

VR10. Provide a pause control for any motion over five seconds and disable autoplay under `prefers-reduced-motion` and `saveData`. LAW.
Rationale: WCAG 2.2.2 https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide .

VR11. Stay inside the weight ceilings: loop 1.5 MB, UGC clip 8 MB, demo 15 MB; H.264 MP4 always. HEURISTIC.
Rationale: video is the heaviest asset class on the page; the loop competes with the hero image.
Check: the hosted response's Content-Length or measured transfer size per file is at or under the ceiling.

VR12. Show UGC video only with a `verified` proof-ledger row that records rights, consent and paid disclosure. LAW.
Rationale: creator copyright and 16 CFR 465 material-connection rules https://later.com/blog/user-generated-content-rules/ ; `references/proof/proof-ledger.md`.
Check: every `proof (ugc video ...)` slot row cites a `P[0-9]+` id whose status is `verified`.

VR13. Never generate video of the product, of people or of results; an abstract backdrop loop is ASK and counts as the page's single motion moment. LAW, OPERATOR.
Rationale: `references/assets/generation-policy.md` section 2; N10.
Check: no manifest entry with `generated: true` has a video URL unless its plan row shows an ASK approval and the Motion line names it.

VR14. Draw the play control in HTML at 48 px or larger, one style per page; never bake it into the poster. OPERATOR.
Rationale: A11 tap targets in `references/design-rules.md`; a baked-in control cannot be focused or styled.
Check: view each poster; no play glyph in the pixels; the button element has `min-width` and `min-height` of 48 px.

## Sources

- Unbounce video on landing pages https://unbounce.com/landing-pages/video-on-landing-pages-means-more-conversions-right-wrong-heres-why/ ; video backgrounds https://unbounce.com/landing-pages/do-video-backgrounds-help-or-hurt-conversions/
- Baymard video and 360 https://baymard.com/ecommerce-design-examples/video-and-360-views ; embedding product videos https://baymard.com/blog/embedding-product-page-videos
- Verizon Media and Publicis via Forbes https://www.forbes.com/sites/tjmccue/2019/07/31/verizon-media-says-69-percent-of-consumers-watching-video-with-sound-off/ ; MarketingCharts https://www.marketingcharts.com/digital/video-108656
- Wistia optimal length https://wistia.com/blog/optimal-video-length ; 2026 State of Video https://downloads.ctfassets.net/j7pfe8y48ry3/5tOf2aVNOvk9CValTgj83h/f577dc1aebb439a6904c253b9f80c23c/Wistia-2026-State-Of-Video-Report.pdf ; Wyzowl 2026 https://wyzowl.com/video-marketing-statistics/
- W3C: F93 https://www.w3.org/WAI/WCAG22/Techniques/failures/F93.html ; 1.4.2 https://www.w3.org/WAI/WCAG22/Understanding/audio-control ; 2.2.2 https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide ; 1.2.1 https://www.w3.org/WAI/WCAG22/Understanding/audio-only-and-video-only-prerecorded ; 1.2.2 https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded ; 1.2.3 https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded
- Chrome autoplay policy https://developer.chrome.com/blog/autoplay ; web.dev LCP https://web.dev/articles/lcp ; optimize LCP https://web.dev/articles/optimize-lcp
- MDN video element https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video
- Meta aspect ratios https://www.facebook.com/business/help/103816146375741 ; Reels length (secondary) https://www.mbadv.agency/meta-ads/meta-ads-formats-and-creative
- UGC rights: Later https://later.com/blog/user-generated-content-rules/

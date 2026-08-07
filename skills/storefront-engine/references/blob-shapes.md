# SVG Blob Shapes Reference

Organic blob/wave shapes for hero sections using SVG `<clipPath>` with `clipPathUnits="objectBoundingBox"`.

## How It Works

All coordinates are normalized 0–1 (fraction of container width/height). Scales to any container size automatically.

```html
<!-- 1. Define the clipPath (hidden SVG) -->
<svg width="0" height="0" aria-hidden="true">
  <defs>
    <clipPath id="my-blob" clipPathUnits="objectBoundingBox">
      <path d="M0.575,1 H0.37 C0.368,0.999 ..."></path>
    </clipPath>
  </defs>
</svg>

<!-- 2. Apply to container -->
<div style="clip-path: url(#my-blob); -webkit-clip-path: url(#my-blob);">
  <img src="..." style="width:100%;height:100%;object-fit:cover">
</div>
```

## Shape Catalog

### Shape 1: Soft Rounded Blob (Hero default)
**Mood:** Clean, premium, minimal
**Best for:** Product heroes, lifestyle brands

```svg
<clipPath id="blob-soft-rounded" clipPathUnits="objectBoundingBox">
  <path d="M0.875,1 H0.124 C0.121,0.999,0.119,0.998,0.116,0.997 C0.07,0.979,0.036,0.933,0.015,0.858 C0.007,0.832,0.003,0.804,0,0.775 C0,0.753,0,0.731,0,0.708 C0,0.706,0.001,0.705,0.001,0.702 C0.006,0.649,0.018,0.603,0.038,0.563 C0.047,0.546,0.05,0.526,0.051,0.502 C0.051,0.473,0.045,0.45,0.035,0.429 C0.022,0.403,0.013,0.373,0.007,0.34 C0.004,0.325,0.002,0.308,0,0.292 C0,0.262,0.003,0.232,0.01,0.204 C0.02,0.163,0.038,0.126,0.064,0.096 C0.086,0.071,0.113,0.052,0.143,0.038 C0.176,0.022,0.212,0.012,0.249,0.007 C0.29,0.002,0.331,0,0.372,0.001 C0.427,0.003,0.482,0.007,0.537,0.005 C0.586,0.003,0.634,0,0.683,0.003 C0.72,0.005,0.757,0.012,0.793,0.026 C0.83,0.041,0.862,0.064,0.889,0.098 C0.92,0.136,0.941,0.184,0.955,0.238 C0.973,0.306,0.982,0.378,0.987,0.452 C0.992,0.528,0.994,0.604,0.997,0.68 C0.998,0.72,1,0.76,1,0.8 C1,0.837,0.996,0.873,0.985,0.907 C0.975,0.937,0.96,0.963,0.938,0.982 C0.924,0.993,0.908,0.999,0.891,1 H0.875"></path>
</clipPath>
```

### Shape 2: Asymmetric Organic (Wide)
**Mood:** Editorial, artistic, fashion
**Best for:** Full-width lifestyle heroes, lookbooks

```svg
<clipPath id="blob-asymmetric" clipPathUnits="objectBoundingBox">
  <path d="M0.575,1 H0.37 C0.368,0.999,0.367,0.998,0.365,0.998 C0.345,0.998,0.324,0.996,0.304,0.994 C0.281,0.992,0.259,0.989,0.236,0.986 C0.201,0.98,0.166,0.972,0.131,0.958 C0.104,0.947,0.077,0.933,0.052,0.904 C0.04,0.891,0.03,0.876,0.022,0.851 C0.012,0.822,0.008,0.786,0.006,0.749 C0,0.65,-0.001,0.551,0.001,0.451 C0.002,0.387,0.006,0.324,0.012,0.262 C0.019,0.199,0.029,0.139,0.048,0.092 C0.057,0.069,0.067,0.05,0.08,0.036 C0.108,0.006,0.145,-0.001,0.187,0.001 C0.219,0.002,0.251,0.007,0.284,0.01 C0.32,0.014,0.357,0.013,0.393,0.011 C0.435,0.008,0.476,0.003,0.518,0.001 C0.556,-0.001,0.594,0,0.632,0.005 C0.665,0.009,0.697,0.016,0.728,0.03 C0.764,0.046,0.795,0.072,0.82,0.112 C0.845,0.152,0.862,0.2,0.874,0.253 C0.898,0.358,0.907,0.468,0.912,0.578 C0.916,0.667,0.917,0.756,0.928,0.844 C0.933,0.882,0.94,0.919,0.953,0.952 C0.959,0.966,0.966,0.978,0.975,0.988 C0.982,0.995,0.991,0.999,1,1 H0.575"></path>
</clipPath>
```

### Shape 3: Bubble Top (Inflated)
**Mood:** Playful, fun, DTC
**Best for:** Product launches, subscription boxes, food brands

```svg
<clipPath id="blob-bubble-top" clipPathUnits="objectBoundingBox">
  <path d="M0,0.002 C0,0.002,0.008,-0.002,0.017,0.002 C0.027,0.007,0.037,0.009,0.046,0.016 C0.06,0.027,0.072,0.042,0.083,0.06 C0.095,0.082,0.111,0.084,0.124,0.062 C0.135,0.046,0.145,0.029,0.159,0.019 C0.169,0.011,0.183,0.005,0.191,0.002 C0.199,-0.001,0.205,0,0.213,0.002 C0.221,0.004,0.24,0.012,0.252,0.024 C0.261,0.033,0.269,0.043,0.276,0.055 C0.283,0.068,0.291,0.08,0.303,0.085 C0.318,0.092,0.334,0.082,0.347,0.068 C0.358,0.056,0.368,0.042,0.381,0.032 C0.397,0.02,0.416,0.016,0.435,0.017 C0.453,0.018,0.469,0.026,0.484,0.037 C0.501,0.05,0.516,0.066,0.534,0.075 C0.551,0.083,0.57,0.082,0.587,0.073 C0.607,0.063,0.623,0.045,0.641,0.032 C0.66,0.019,0.683,0.01,0.706,0.005 C0.735,0,0.765,-0.001,0.795,0.003 C0.823,0.007,0.85,0.014,0.875,0.029 C0.905,0.046,0.93,0.072,0.95,0.108 C0.968,0.14,0.98,0.178,0.988,0.22 C0.995,0.263,0.998,0.308,1,0.354 C1,0.454,0.998,0.554,0.999,0.654 C1,0.722,0.999,0.789,0.996,0.855 C0.994,0.892,0.99,0.928,0.983,0.958 C0.977,0.978,0.969,0.993,0.958,1 H0.042 C0.031,0.993,0.023,0.978,0.017,0.958 C0.01,0.928,0.006,0.892,0.004,0.855 C0.001,0.789,0,0.722,0,0.654 C0.001,0.554,0,0.454,0,0.354 C0.002,0.308,0.005,0.263,0.012,0.22 C0.02,0.178,0.032,0.14,0.05,0.108 L0,0.002"></path>
</clipPath>
```

### Shape 4: Wavy Edges (Subtle)
**Mood:** Organic, natural, wellness
**Best for:** Supplements, beauty, organic food

```svg
<clipPath id="blob-wavy-subtle" clipPathUnits="objectBoundingBox">
  <path d="M0.27,1 C0.248,1,0.225,0.997,0.204,0.985 C0.191,0.978,0.179,0.971,0.167,0.963 C0.142,0.949,0.116,0.945,0.091,0.961 C0.084,0.965,0.077,0.968,0.07,0.97 C0.049,0.975,0.033,0.962,0.024,0.931 C0.018,0.911,0.016,0.89,0.014,0.869 C0.008,0.801,0.007,0.734,0.005,0.666 C0.003,0.593,0.001,0.519,0.001,0.446 C0.001,0.442,0,0.438,0,0.433 C0,0.377,0,0.321,0,0.265 C0,0.223,0.004,0.182,0.015,0.144 C0.024,0.112,0.038,0.084,0.059,0.06 C0.078,0.04,0.101,0.024,0.128,0.014 C0.158,0.003,0.191,-0.001,0.225,0.001 C0.262,0.003,0.298,0.01,0.334,0.013 C0.371,0.017,0.408,0.015,0.445,0.011 C0.484,0.006,0.524,0.001,0.563,0 C0.601,-0.001,0.639,0.002,0.676,0.009 C0.713,0.016,0.749,0.028,0.781,0.049 C0.816,0.072,0.845,0.104,0.866,0.146 C0.889,0.192,0.903,0.245,0.911,0.302 C0.921,0.369,0.925,0.438,0.928,0.507 C0.931,0.579,0.932,0.651,0.936,0.723 C0.939,0.772,0.944,0.821,0.956,0.867 C0.964,0.899,0.974,0.928,0.991,0.95 C1,0.963,0.997,0.981,0.984,0.993 C0.97,1,0.954,1,0.938,1 H0.27"></path>
</clipPath>
```

### Shape 5: Tight Pill (Rounded Rectangle)
**Mood:** Modern, tech, SaaS
**Best for:** Tech products, app screenshots, minimal brands

```svg
<clipPath id="blob-tight-pill" clipPathUnits="objectBoundingBox">
  <path d="M0.06,0 H0.94 C0.97,0,1,0.04,1,0.08 V0.92 C1,0.96,0.97,1,0.94,1 H0.06 C0.03,1,0,0.96,0,0.92 V0.08 C0,0.04,0.03,0,0.06,0"></path>
</clipPath>
```

### Shape 6: Speech Bubble
**Mood:** Conversational, testimonial, social
**Best for:** Review sections, testimonial highlights

```svg
<clipPath id="blob-speech" clipPathUnits="objectBoundingBox">
  <path d="M0.06,0 H0.94 C0.97,0,1,0.03,1,0.06 V0.78 C1,0.81,0.97,0.84,0.94,0.84 H0.55 L0.45,1 L0.4,0.84 H0.06 C0.03,0.84,0,0.81,0,0.78 V0.06 C0,0.03,0.03,0,0.06,0"></path>
</clipPath>
```

## Wavy Section Dividers

For top/bottom wave borders between sections:

```html
<div class="wave-top">
  <svg viewBox="0 0 1200 40" preserveAspectRatio="none" style="width:100%;height:40px;display:block">
    <path d="M0,40 C150,0 350,0 600,20 C850,40 1050,0 1200,10 L1200,0 L0,0 Z" fill="#ffffff"></path>
  </svg>
</div>
```

Variants:
- **Gentle wave:** `M0,40 C300,10 600,30 900,10 C1050,0 1150,15 1200,5 L1200,0 L0,0 Z`
- **Sharp peaks:** `M0,40 L100,5 L200,35 L300,0 L400,40 L500,5 L600,30 L700,0 L800,40 L900,10 L1000,35 L1100,0 L1200,30 L1200,0 L0,0 Z`
- **Organic bumps:** `M0,40 C100,35 200,10 350,25 C500,40 600,5 750,20 C900,35 1000,10 1200,30 L1200,0 L0,0 Z`

## Converting Pixel Paths to ObjectBoundingBox

Formula:
```
normalizedX = pixelX / viewBoxWidth
normalizedY = pixelY / viewBoxHeight
```

Example: If viewBox is `0 0 800 600` and point is `(400, 300)`:
- normalizedX = 400/800 = 0.5
- normalizedY = 300/600 = 0.5

## Generation Tools

- **Blobmaker** (blobmaker.app): Quick organic blobs → export SVG → normalize
- **Haikei** (haikei.app): Waves, blobs, stacked shapes → SVG
- **Figma**: Draw with pen tool → Flatten → Export SVG → normalize coords
- **Manual**: Modify existing shapes by tweaking control points (C values)

## Usage in Templates

```json
{
  "section": {
    "html": "<section><svg width='0' height='0' aria-hidden='true'><defs><clipPath id='my-shape' clipPathUnits='objectBoundingBox'><path d='...'></path></clipPath></defs></svg><div class='clipped'><img src='...'></div></section>",
    "css": ".clipped{clip-path:url(#my-shape);-webkit-clip-path:url(#my-shape);min-height:95vh}"
  }
}
```

## Anti-patterns

- Don't use objectBoundingBox on elements with 0 width or height (breaks)
- Don't nest clip-paths (performance + browser inconsistency)
- Always include `-webkit-clip-path` for Safari
- Keep path complexity reasonable (<100 control points) for performance
- Avoid thin slivers in the shape (content becomes unreadable)

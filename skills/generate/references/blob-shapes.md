# Static SVG clipping

Use an organic image crop only when it is the plan's named visual moment.
The image, its subject and its usable mobile crop are resolved through
`references/workflows/section-asset-workflow.md`; clipping is not an asset
fallback or a section divider.

## Geometry

An SVG `clipPath` with `clipPathUnits="objectBoundingBox"` uses coordinates
between zero and one. Normalize a source path by dividing its x coordinates
by the source width and its y coordinates by the source height. Preserve the
path's shape and inspect the crop at both review widths.

Give the clip path a unique page id, apply it only to the intended image,
and keep its geometry static. `references/authoring/css-and-styling.md` owns
the scoped CSS. The unclipped image remains the fallback where clipping is
unsupported; do not hide content while waiting for script execution.

Avoid clipped product labels, cut-off faces, decorative section boundaries,
an animated blob, or repeating the same unusual shape across the page.

# Style direction

A style direction translates the merchant's palette, typography, imagery and
object-radius scale into one coherent page. It does not override
`references/design-rules.md` or supply island props.

| Direction | Deliberate choice |
|---|---|
| Editorial | Strong image hierarchy, readable measure, restrained supporting type |
| Soft luxury | Quiet geometry, craftsmanship imagery, generous pacing |
| Brutalist | Firm alignment, explicit hierarchy, minimal ornament |
| Playful | Merchant-approved palette and composition, not decorative UI effects |
| Minimal | Sparse hierarchy with enough detail to make the purchase decision |

## Applying a direction

Record it in the plan. Apply tokens in `theme_css`; keep section
geometry in utilities unless the styling contract permits custom CSS.
`references/authoring/css-and-styling.md` owns scope, contrast, radii and
parts. After the live schema confirms a part, a visual override can be:

```css
#buy-box [data-part="cta"] { border-radius: var(--r-control); }
```

Do not add global part selectors, accent-tinted shadows, word accents,
background bands or motion to make a direction recognizable. Its identity
must survive without those effects. A saved island intent label is resolved
against the live schema, not copied as a prop bundle.

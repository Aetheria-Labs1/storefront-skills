# CartProgressBar — Island Knowledge

Shows progress toward free shipping or tiered rewards. Subscribes to shared cart state and store config. Self-hides when no threshold is configured or cart is empty.

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `threshold` | number | From config | Target amount in cents (e.g., 7500 = $75) |
| `message` | string | "{remaining} away from free shipping!" | Template with `{remaining}`, `{total}`, `{threshold}` |
| `completedMessage` | string | "Free shipping unlocked!" | Shown when threshold met |
| `tiers` | Array<{threshold, label}> | None | Multi-tier milestones |
| `currency` | string | From config | ISO currency code (USD, EUR, etc.) |

## Config Source

Falls back to `commerce_config` if props omitted:
- `free_shipping_threshold` → used as threshold
- `currency` → used for formatting

## Self-Managing Behavior

- Hides when: `threshold` is 0 or unset
- Hides when: cart is empty (0 items)
- Shows automatically when cart has items and threshold > 0

## Multi-Tier Support

```json
{
  "tiers": [
    {"threshold": 5000, "label": "Free sample added!"},
    {"threshold": 10000, "label": "Free shipping unlocked!"},
    {"threshold": 20000, "label": "15% off your order!"}
  ]
}
```

Finds the next unmet tier, shows progress toward it. When all tiers met, shows the highest tier's label.

## Message Template Variables

| Variable | Description |
|----------|-------------|
| `{remaining}` | Amount left to reach threshold (formatted with currency) |
| `{total}` | Current cart subtotal (formatted) |
| `{threshold}` | Target threshold (formatted) |

## Example HTML

```html
<!-- Default — reads threshold from commerce_config -->
<div data-island="CartProgressBar" data-props='{}'></div>

<!-- With explicit threshold -->
<div data-island="CartProgressBar" data-props='{"threshold":7500,"message":"Add {remaining} more for free shipping!","completedMessage":"🎉 Free shipping!"}'></div>

<!-- Multi-tier -->
<div data-island="CartProgressBar" data-props='{"tiers":[{"threshold":5000,"label":"Free sample!"},{"threshold":10000,"label":"Free shipping!"}]}'></div>
```

## data-part Attributes

| Part | Element | Purpose |
|------|---------|---------|
| `root` | Outer container | CSS targeting root |
| `track` | Progress track | Background bar |
| `bar` | Fill bar | Animated progress fill |
| `message` | Message text | Status/template text |

## CSS Custom Properties

| Property | Default | Purpose |
|----------|---------|---------|
| `--progress-bg` | #f3f4f6 | Track background |
| `--progress-color` | var(--lx-accent-color, #5055aa) | Bar fill color |
| `--progress-complete-color` | #16a34a | Text color when completed |
| `--progress-text-color` | #6b7280 | Text color when in progress |

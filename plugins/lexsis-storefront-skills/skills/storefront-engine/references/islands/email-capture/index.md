# EmailCapture — Island Directory

Lead capture form for newsletter signups, discount offers, and list building.

## Files

| File | Purpose |
|------|---------|
| `layouts/full-width-banner.json` | Full-width accent bg section, centered headline + form |
| `layouts/inline-minimal.json` | Simple inline form, transparent bg, max-w-xl |
| `layouts/popup.json` | Modal overlay card with close button |

## Quick Reference

- **Variants**: default, compact
- **Schema**: `vibe://schema/island/EmailCapture`
- **Layouts**: `vibe://islands/email-capture/layouts/{name}`
- **Contract**: follows `_contract.md` rules

## Composition

- Place after value-establishing content (post-hero, post-testimonials, pre-footer)
- Pair with: TrustBadgeBar (below form), CountdownTimer (urgency)
- Full-width banner works as page-break CTA between content sections
- Popup variant renders visible in gallery but ships as triggered overlay
- Never place two EmailCapture islands on the same page
- Provider prop connects to Klaviyo or Mailchimp for list sync

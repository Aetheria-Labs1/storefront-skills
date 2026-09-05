# EmailCapture — Island Directory

Lead capture form for newsletter signups, discount offers, and list building.

## Quick Reference

- **Variants**: default, compact
- **Schema**: `vibe://schema/island/EmailCapture`
- **Contract**: follows `_contract.md` rules

## Composition

- Place after value-establishing content (post-hero, post-testimonials, pre-footer)
- Pair with: TrustBadgeBar (below form), CountdownTimer (urgency)
- Full-width banner works as page-break CTA between content sections
- Popup variant renders visible in gallery but ships as triggered overlay
- Never place two EmailCapture islands on the same page
- Provider prop connects to Klaviyo or Mailchimp for list sync

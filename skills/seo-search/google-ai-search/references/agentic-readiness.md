# Agentic Readiness

Use this only when the business has a realistic reason to support browser
agents, shopping agents, booking agents, or emerging Google merchant
experiences. Do not make this a default scope for simple brochure sites.

## What Agents Need

Browser and commerce agents may inspect rendered pages, DOM structure, forms,
accessibility trees, product details, policies, and screenshots. They need the
same clarity that helps users:

- visible product/service facts
- stable labels and form controls
- accessible names and semantic structure
- clear prices, availability, locations, and policies
- reliable buttons and links
- no anti-automation traps on public discovery paths

## Readiness Checklist

- [ ] Product/service names are visible and unambiguous.
- [ ] Prices, availability, service areas, and constraints are explicit.
- [ ] CTAs have descriptive accessible names.
- [ ] Forms have labels, validation messages, and success/error states.
- [ ] Tables use real table markup where tabular comparison is intended.
- [ ] Policies are linked near relevant decisions: returns, cancellation,
  privacy, security, shipping, booking, eligibility.
- [ ] Product feeds or booking data match visible pages.
- [ ] Important workflows can be completed with keyboard navigation.
- [ ] Screenshots are visually clear at mobile and desktop sizes.
- [ ] Analytics can distinguish agent-assisted journeys where possible.

## Ecommerce And Local Additions

- Maintain Merchant Center feed quality.
- Keep Google Business Profile data current.
- Use structured data for products, offers, shipping, return policy, local
  business, and reviews only where it matches visible content.
- Consider Business Agent only when the business can maintain response quality,
  escalation, and policy accuracy.

## Anti-Patterns

- Hiding prices, availability, or policies until late in the journey.
- Using unlabeled icon-only controls for core actions.
- Rendering critical facts only inside images.
- Blocking all automation on public product discovery pages without a reason.
- Publishing feeds that disagree with visible pages.

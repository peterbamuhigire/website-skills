---
name: ecommerce
description: E-commerce website design and consumer psychology. Use when building online shops, product catalogues, or any site where visitors buy products or services online. Covers the CLICK system (Convenient, Likeable, Informative, Customized, Knowledgeable), product page design, cart abandonment prevention, trust signals, pricing psychology, and social proof integration.
---

# E-Commerce Website Skill

Design and build e-commerce websites that convert browsers into buyers by applying consumer psychology principles.

## The CLICK System

Every e-commerce site must satisfy five psychological needs. Use this as an audit checklist for every page:

### C — Convenient

People shop online for control and ease. Friction kills sales.

**Rules:**
- Make it obvious what you sell within 3 seconds of landing on any page
- Search must be prominent — top of page, always visible, with autocomplete
- Navigation categories must use the words customers use (not internal jargon). Do keyword research to find the right terms.
- Filtering: let customers narrow by price, size, colour, rating, availability
- Guest checkout MUST be available — never force account creation to buy
- Checkout in 3 steps or fewer (cart → shipping/payment → confirmation)
- Show delivery costs and timeframes BEFORE checkout (hidden costs are the #1 reason for cart abandonment)
- Mobile checkout must work with thumb-only navigation — large tap targets, no tiny dropdowns

### L — Likeable

Customers buy from shops they like. Shops that like their customers back.

**Rules:**
- Build the site from the customer's perspective, not the retailer's
- Navigation, layout, and content must feel effortless — never make the customer think
- Returns policy must be visible, generous, and clearly explained on every product page (not buried in footer links)
- Customer service contact (phone, email, chat) visible on every page — top right corner for phone, footer for full details
- Personalisation: "Recently viewed", "Customers also bought", "Based on your browsing"
- Social sharing: let customers share purchases and wishlists (taps into desire to be liked)
- Thank-you page after purchase: don't waste it. Ask for a review, suggest a complementary product, or invite to follow on social

### I — Informative

Customers want depth. They may not read everything, but seeing lots of information builds confidence.

**Rules:**
- Product descriptions: write for humans first, SEO second. Cover what it is, what it does, who it's for, and why it's better.
- Multiple product images (minimum 4): front, back, detail, in-use. Zoomable.
- Product videos increase conversion — embed where possible (YouTube, lazy-loaded)
- Specifications in a structured table (not buried in prose)
- Size guides, compatibility charts, ingredient lists — anything that reduces returns
- Blog/content section: informational shoppers browse content before buying. Guide them from article to product naturally.
- FAQ on product pages, not just a standalone FAQ page

### C — Customized

Every customer has different needs. One-size-fits-all feels impersonal.

**Rules:**
- Show customers that you know their situation (segment by use case, not just demographics)
- Product recommendations based on browsing/purchase history
- Allow wishlists and saved items
- Email: segment by purchase history, browsing behaviour, or stated preferences
- Product pages should address different buyer types (features for technical buyers, benefits for emotional buyers, reviews for social buyers)
- Currency and language: detect location and offer appropriate defaults (with easy override)

### K — Knowledgeable

Customers want to buy from experts who know their domain.

**Rules:**
- Demonstrate expertise through content (buying guides, how-to articles, comparison posts)
- Staff picks and expert recommendations build trust
- Answer the question "Why should I buy from you?" prominently — not just price, but knowledge, curation, service
- Product knowledge in descriptions: explain why this product exists, what problem it solves, how it compares to alternatives
- Include "About Us" story that shows domain expertise (not generic corporate boilerplate)

---

## Trust Signals (MANDATORY for e-commerce)

Online shoppers can't touch products or look the shopkeeper in the eye. Trust must be built deliberately.

### On Every Page
- **Phone number** visible in header (top right) — even if you prefer email, showing a phone number proves you're real
- **Physical address** in footer — a real address (not just a PO box) signals legitimacy
- **SSL certificate** — HTTPS everywhere (non-negotiable)
- **Payment method logos** in footer — Visa, Mastercard, PayPal, M-Pesa (whatever is relevant)

### On Product Pages
- **Customer reviews and ratings** — at least 3 reviews per product. Star ratings summarised at top.
- **Review authenticity signals** — verified buyer badge, review date, reviewer location
- **Stock status** — "In stock", "Only 3 left", "Ships in 2-3 days" (honest scarcity, never fake urgency)
- **Returns policy snippet** — "Free returns within 30 days" visible near the Add to Cart button

### On Checkout Pages
- **Security badges** — SSL, secure payment icons
- **Order summary** visible at all times during checkout
- **No surprise costs** — total including delivery must be clear before payment step
- **Multiple payment methods** — credit card, mobile money, bank transfer (region-appropriate)

---

## Cart Abandonment Prevention

60-74% of online shopping carts are abandoned. The primary causes are preventable.

### Top Causes and Fixes

| Cause | Fix |
|-------|-----|
| Unexpected delivery costs | Show delivery estimate on product page, before checkout |
| Forced account creation | Offer guest checkout (always) |
| Too many checkout steps | Maximum 3 steps: cart → details → payment |
| Security concerns | Show security badges, SSL, payment logos prominently |
| Complex forms | Autofill support, minimal required fields, inline validation |
| No price clarity | Show total (with tax + delivery) in the cart, not just at payment |
| Slow site | Performance budget: under 3s page load, under 1s interaction response |

### Recovery Strategies
- **Persistent cart** — cart survives browser close and return visits (localStorage or account)
- **Cart reminder** — if user leaves with items in cart, show a gentle notification on return
- **Exit-intent** — subtle (not popup-aggressive): "Your cart has 3 items" reminder in a corner toast

---

## Product Page Design

The product page is where buying decisions happen. Every element must reduce uncertainty and build desire.

### Required Elements (in order of importance)

1. **Product images** — large, high-quality, zoomable. Hero image above fold. Gallery below.
2. **Product name** — clear, descriptive, includes key attributes (size, colour, material)
3. **Price** — prominent, honest. Show original price + discount only if the discount is real.
4. **Add to Cart button** — highest-contrast element on the page. Large, obvious, sticky on mobile.
5. **Short description** — 2-3 sentences answering "What is this and why should I care?"
6. **Customer reviews summary** — star rating + review count near the top
7. **Availability** — in stock / limited / out of stock
8. **Delivery information** — estimated delivery date and cost
9. **Full description** — detailed, benefit-oriented copy
10. **Specifications** — structured table
11. **Customer reviews** — full reviews below the fold
12. **Related products** — "You might also like" or "Customers also bought"

### Pricing Psychology

- **Price anchoring:** Show the higher original price next to the sale price (only if genuine)
- **Visual price cues:** Premium products need premium design (lots of white space, minimal colours, elegant typography). Discount products need busy, value-signalling design (bright badges, comparison prices).
- **Don't devalue with excessive freebies:** "Buy one, get seven free bonus items" makes customers question the real value. One compelling bonus is better than seven weak ones.
- **Charm pricing:** Prices ending in .99 or .97 signal value. Round numbers (100, 50) signal quality. Choose based on positioning.
- **Bundle pricing:** "Save 15% when you buy the set" works better than discounting individual items

---

## Social Proof Integration

People look at what others do before deciding. This is the most powerful conversion tool in e-commerce.

### Types of Social Proof (ranked by effectiveness)

1. **Customer reviews with photos** — real people showing real results
2. **Star ratings with count** — "4.7 stars from 238 reviews" (include the count — 5 stars from 2 reviews isn't convincing)
3. **Bestseller / Most Popular badges** — signals social validation
4. **Recently purchased notifications** — "Sarah from Kampala bought this 2 hours ago" (only if real data, never fake)
5. **Social sharing counts** — if genuinely high
6. **Expert endorsements** — industry awards, press mentions, certifications
7. **Client logos** — for B2B, show recognisable brand logos (static, never in a carousel)

### Social Proof Rules
- Never fake reviews, purchase notifications, or social counts. Customers detect deception, and the trust damage is permanent.
- Place reviews near the purchase decision point (not just at page bottom)
- Show negative reviews too — a 4.7 rating with some 3-star reviews is more credible than a perfect 5.0
- Feature reviews that mention specific benefits or use cases, not just "Great product!"

---

## Product Structured Data (JSON-LD)

Every product page MUST include Product schema:

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "image": ["url1.jpg", "url2.jpg"],
  "description": "Product description",
  "brand": { "@type": "Brand", "name": "Brand Name" },
  "offers": {
    "@type": "Offer",
    "price": "29.99",
    "priceCurrency": "GBP",
    "availability": "https://schema.org/InStock",
    "seller": { "@type": "Organization", "name": "Shop Name" }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.7",
    "reviewCount": "238"
  }
}
```

This enables rich snippets in Google search results (star ratings, price, availability).

---

## Mobile Commerce Rules

Over 60% of e-commerce traffic is mobile. Mobile is not an afterthought — it's the primary platform.

- **Thumb zone:** Primary actions (Add to Cart, Checkout) in the bottom half of the screen
- **Sticky Add to Cart:** On product pages, the Add to Cart button should follow the user as they scroll
- **Large tap targets:** Minimum 44x44px for all interactive elements
- **Simplified navigation:** Category list, not multi-level menus. Search prominent.
- **Mobile payment:** Support Apple Pay, Google Pay, mobile money where relevant
- **Image galleries:** Swipeable, not thumbnail-clickable
- **Forms:** Use appropriate input types (tel, email, number) for mobile keyboards

---

## Integration with Other Skills

This skill works alongside:

- **page-builder** — implements product pages, category pages, cart, and checkout layouts
- **seo** — Product JSON-LD, breadcrumbs, category page meta tags
- **design-system** — visual design must match price positioning (premium vs value)
- **content-writing** — product descriptions, buying guides, blog content
- **sales-copywriting** — product page copy, CTA wording, urgency (ethical only)
- **photo-manager** — product photography handling
- **i18n** — multi-language product content, currency display, locale-specific payment methods

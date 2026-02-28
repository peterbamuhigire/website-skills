# SEO Audit Checklist — Detailed Reference

## Technical SEO

### Sitemap
- XML sitemap must list every indexable page
- Sitemap index used for multi-language sites
- Submit sitemap to Google Search Console and Bing Webmaster Tools
- Sitemap referenced in robots.txt

### Robots.txt
- Must allow all important pages
- Block admin, staging, and duplicate paths
- Include Sitemap directive
- Do not block CSS/JS files (Googlebot needs them for rendering)

### Canonical URLs
- Every page must have a self-referencing canonical
- Canonical URL must be absolute (include domain)
- Avoid conflicting canonical signals

### Hreflang
- Required for multi-language sites
- Must include x-default pointing to default language
- Reciprocal — if page A points to page B, page B must point to page A
- Use correct language-region codes (en-UG, fr-UG, sw)

## On-Page SEO

### Title Tags
- Include primary keyword near the beginning
- Keep under 60 characters (Google truncates at ~580px)
- Make each title unique across the site
- Include brand name (usually at the end after pipe)
- Front-load important keywords

### Meta Descriptions
- Include primary keyword and geo-target
- Keep under 160 characters
- Include a call to action where natural
- Make each description unique
- Describe what the user will find on the page

### Heading Hierarchy
- One H1 per page — must contain primary keyword
- H2s for major sections
- H3s for subsections within H2s
- Never skip levels (H1 > H3 without H2)
- Use headings for structure, not styling

## Content Quality

### Word Count Guidelines
- Homepage: 500-1000 words minimum
- Service pages: 800-1500 words
- About page: 500-1000 words
- Contact page: 200-400 words (plus form)
- Blog posts: 1000-2000 words

### E-E-A-T Signals
- **Experience**: Show work examples, case studies, portfolio
- **Expertise**: Credentials, certifications, team qualifications
- **Authoritativeness**: Industry associations, partnerships, media mentions
- **Trustworthiness**: Physical address, registration details, testimonials, privacy policy

## Local SEO for African Businesses

### NAP Consistency
- Name, Address, Phone must be identical everywhere
- Use consistent formatting across all pages
- Include country (Uganda), city (Kampala)

### Geo Meta Tags
- `geo.region` — ISO 3166-2 code (UG-102 for Kampala)
- `geo.placename` — City name
- `geo.position` — Latitude;Longitude
- `ICBM` — Latitude, Longitude

### Target Keywords with Location
- Include city + country in page titles: "Website Design in Kampala, Uganda"
- Include region in descriptions: "serving East Africa"
- Use local language variants: "website designers Uganda" not just "website designers"

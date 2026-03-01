# Local SEO Guide for African Businesses

## Why Local SEO Matters in Africa

Internet penetration is growing rapidly across East Africa. More businesses and consumers search online for local services. Ranking for "[service] + [location]" queries captures high-intent traffic from people ready to buy.

## Google Business Profile

### Setup
1. Claim or create Google Business Profile at business.google.com
2. Verify via postcard, phone, or email
3. Complete all fields: name, address, phone, website, hours, categories
4. Add photos of office, team, work samples

### Categories
Primary: "Information Technology Company" or "Software Company"
Secondary: "Web Designer", "Business Consultant", "Security System Supplier"

### Posts
- Share updates, offers, and news weekly
- Include photos with every post
- Link to relevant website pages

## NAP Consistency

Name, Address, Phone must be identical across:
- Website (header, footer, contact page)
- Google Business Profile
- Social media profiles
- Online directories
- Structured data (JSON-LD)

## Citation Building for East Africa

### Key Directories
- Google Business Profile (essential)
- Bing Places for Business
- Yellow Pages Uganda
- Uganda Business Directory
- LinkedIn Company Page
- Facebook Business Page

### Industry Directories
- Clutch.co (software development)
- GoodFirms (IT services)
- TopDevelopers.co

## Schema Markup for Local SEO

### LocalBusiness/ProfessionalService Schema
```json
{
  "@type": "ProfessionalService",
  "name": "Company Name",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Kampala",
    "addressCountry": "UG"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 0.3476,
    "longitude": 32.5825
  },
  "areaServed": [
    { "@type": "Country", "name": "Uganda" },
    { "@type": "Country", "name": "Kenya" }
  ]
}
```

## Content Strategy for Local Ranking

1. **Location pages** — dedicated pages for each city/region served
2. **Service + location titles** — "Website Design in Kampala, Uganda"
3. **Local case studies** — mention client locations and local context
4. **Local testimonials** — include client names and companies with locations
5. **Community involvement** — highlight local partnerships and events

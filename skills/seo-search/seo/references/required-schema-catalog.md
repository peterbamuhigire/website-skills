# Evidence-Matched Schema.org JSON-LD Catalogue

Illustrative patterns for JSON-LD blocks this skill may use. Never copy example
facts into a project. Replace or remove every property based on visible,
verified page evidence and current consumer support.

Use schema only where the visible page supports it. Common types include **Organization**, **WebSite**, **BreadcrumbList**, the most specific applicable **LocalBusiness** subtype, **Product** + **Offer**, **Service**, **Person** for named authors, and **Article** on editorial pages. Software products add **SoftwareApplication**. No type is mandatory merely because it exists in this catalogue.

All `@id` URLs must be stable, absolute and unique per entity. Cross-reference entities with `@id`, never duplicate them.

---

## Organization (site entity where applicable)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "Legal Company Name",
  "alternateName": "Trading name",
  "url": "https://example.com",
  "logo": {
    "@type": "ImageObject",
    "url": "https://example.com/logo-512.png",
    "width": 512,
    "height": 512
  },
  "foundingDate": "2024-01-01",
  "founders": [{ "@type": "Person", "@id": "https://example.com/#founder" }],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Sserumaga Road, Bukoto",
    "addressLocality": "Kampala",
    "addressCountry": "UG"
  },
  "contactPoint": [{
    "@type": "ContactPoint",
    "telephone": "+256784464178",
    "contactType": "sales",
    "areaServed": ["UG", "KE", "TZ", "RW", "CD", "NG"],
    "availableLanguage": ["en", "fr", "sw"]
  }],
  "sameAs": [
    "https://www.linkedin.com/company/...",
    "https://twitter.com/..."
  ]
}
```

---

## LocalBusiness / industry subtype (genuine customer-serving locations)

Pick the narrowest subtype:

- Healthcare → `MedicalBusiness`, `MedicalClinic`, `Hospital`, `Pharmacy`, `Dentist`, `Physician`
- Software vendor → `Organization` + `SoftwareApplication` (LocalBusiness only if there is a physical office serving customers)
- Legal → `LegalService`, `Attorney`
- Hospitality → `LodgingBusiness`, `Hotel`, `BedAndBreakfast`, `Restaurant`
- Retail → `Store`, `ClothingStore`, `ElectronicsStore`
- Education → `EducationalOrganization`, `School`, `CollegeOrUniversity`
- Finance → `FinancialService`, `BankOrCreditUnion`

```json
{
  "@context": "https://schema.org",
  "@type": "MedicalBusiness",
  "@id": "https://example.com/#localbusiness",
  "name": "Trading name",
  "image": "https://example.com/og-default.png",
  "url": "https://example.com",
  "telephone": "+256784464178",
  "email": "info@example.com",
  "priceRange": "UGX 150,000 – 700,000 / month",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Sserumaga Road, Bukoto",
    "addressLocality": "Kampala",
    "addressRegion": "Central",
    "postalCode": "",
    "addressCountry": "UG"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 0.3476,
    "longitude": 32.5825
  },
  "areaServed": [
    { "@type": "Country", "name": "Uganda" },
    { "@type": "Country", "name": "Kenya" },
    { "@type": "Country", "name": "Tanzania" },
    { "@type": "Country", "name": "Rwanda" },
    { "@type": "Country", "name": "Democratic Republic of the Congo" },
    { "@type": "Country", "name": "Nigeria" }
  ],
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "08:00",
    "closes": "18:00"
  }],
  "sameAs": ["https://www.linkedin.com/company/..."],
  "parentOrganization": { "@id": "https://example.com/#organization" }
}
```

---

## Product + Offer / AggregateOffer (matching product and offer pages)

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "@id": "https://example.com/pricing/#product",
  "name": "Medic8",
  "description": "Cloud-based healthcare management SaaS for African clinics, hospitals and NGO programmes.",
  "image": "https://example.com/og-default.png",
  "brand": { "@type": "Brand", "name": "Medic8" },
  "manufacturer": { "@id": "https://example.com/#organization" },
  "category": "Healthcare Information Management Software",
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "UGX",
    "lowPrice": "150000",
    "highPrice": "700000",
    "offerCount": "4",
    "availability": "https://schema.org/InStock",
    "url": "https://example.com/pricing/",
    "offers": [
      {
        "@type": "Offer",
        "name": "Starter",
        "price": "150000",
        "priceCurrency": "UGX",
        "availability": "https://schema.org/InStock",
        "url": "https://example.com/pricing/#starter"
      },
      {
        "@type": "Offer",
        "name": "Growth",
        "price": "350000",
        "priceCurrency": "UGX",
        "availability": "https://schema.org/InStock",
        "url": "https://example.com/pricing/#growth"
      }
    ]
  }
}
```

---

## Service (matching service pages)

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "https://example.com/services/emr/#service",
  "name": "Electronic Medical Records (EMR)",
  "serviceType": "Healthcare Information Management",
  "provider": { "@id": "https://example.com/#organization" },
  "areaServed": [
    { "@type": "Country", "name": "Uganda" },
    { "@type": "Country", "name": "Kenya" }
  ],
  "audience": {
    "@type": "BusinessAudience",
    "audienceType": "Private clinics, mission hospitals, NGO health programmes"
  },
  "description": "Offline-first electronic medical records purpose-built for African healthcare facilities.",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "EMR sub-services",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": { "@type": "Service", "name": "OPD clinical documentation" }
      },
      {
        "@type": "Offer",
        "itemOffered": { "@type": "Service", "name": "Laboratory management" }
      }
    ]
  }
}
```

---

## SoftwareApplication / WebApplication / MobileApplication

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "@id": "https://example.com/#software",
  "name": "Medic8",
  "applicationCategory": "HealthApplication",
  "applicationSubCategory": "Healthcare Information Management",
  "operatingSystem": "Web, Android, iOS",
  "browserRequirements": "Requires modern browser; works offline via service worker",
  "softwareVersion": "current",
  "datePublished": "2024-01-01",
  "publisher": { "@id": "https://example.com/#organization" },
  "offers": { "@id": "https://example.com/pricing/#product" },
  "featureList": [
    "Offline-first architecture",
    "FHIR R4 + DHIS2 interoperability",
    "MTN Mobile Money + Airtel Money integration",
    "Uganda HMIS 105/108 reporting",
    "Multi-language: English, French, Kiswahili"
  ],
  "inLanguage": ["en", "fr", "sw"]
}
```

---

## FAQPage (not a Google rich-result requirement)

Google stopped showing FAQ rich results on 7 May 2026. Do not add this markup to
promise Google visibility or require a minimum question count. Retain it only
when a documented non-Google consumer needs it and the questions and answers are
visible on the page.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "https://example.com/faq/#faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does Medic8 work offline?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Medic8 is offline-first..."
      }
    }
  ]
}
```

There is no engine minimum. Content quality and visible-content alignment govern use.

---

## Article / BlogPosting / NewsArticle (matching editorial pages)

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "https://example.com/blog/post-slug/#article",
  "headline": "Article title (≤110 characters)",
  "description": "Meta description text (140–160 characters).",
  "image": "https://example.com/blog/post-slug/og.png",
  "datePublished": "2026-04-29",
  "dateModified": "2026-04-29",
  "author": { "@id": "https://example.com/team/peter-bamuhigire/#person" },
  "publisher": { "@id": "https://example.com/#organization" },
  "mainEntityOfPage": "https://example.com/blog/post-slug/",
  "inLanguage": "en"
}
```

---

## Person (verified people represented on the page)

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://example.com/team/peter-bamuhigire/#person",
  "name": "Peter Bamuhigire",
  "jobTitle": "Lead Engineer, Chwezi Core Systems",
  "image": "https://example.com/images/peter.jpg",
  "url": "https://techguypeter.com",
  "worksFor": { "@id": "https://example.com/#organization" },
  "alumniOf": "Makerere University",
  "knowsAbout": [
    "Healthcare information management",
    "Offline-first software architecture",
    "FHIR interoperability"
  ],
  "sameAs": [
    "https://www.linkedin.com/in/peter-bamuhigire",
    "https://github.com/peterbamuhigire",
    "https://techguypeter.com"
  ]
}
```

---

## BreadcrumbList (every non-home page)

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com/" },
    { "@type": "ListItem", "position": 2, "name": "Pricing", "item": "https://example.com/pricing/" }
  ]
}
```

---

## WebSite (root entity)

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://example.com/#website",
  "name": "Medic8",
  "url": "https://example.com",
  "publisher": { "@id": "https://example.com/#organization" },
  "inLanguage": ["en", "fr", "sw"]
}
```

---

## Multi-language notes

- Set `inLanguage` on every JSON-LD block that has one.
- Use one `Organization` block for the whole site, not per language.
- Issue `Article` / `BlogPosting` per language version (each with its own `@id`).
- `Product`, `Service`, `SoftwareApplication` are usually language-neutral — issue once, with `inLanguage` listing all versions.

---

## Validation

Before sign-off:

1. Validate Schema.org syntax and vocabulary with the Schema Markup Validator
   (`https://validator.schema.org/`).
2. For types currently supported by Google Search, test eligible pages with the
   Rich Results Test (`https://search.google.com/test/rich-results`).
3. Verify rendered visible content, entity IDs, canonical URLs, dates, prices,
   availability, and relationships against the approved fact source.
4. Record unsupported types, consumer-specific warnings, and unavailable live
   tests as `NOT_ASSESSED`.

Syntax errors and misleading or unverified properties block release. Warnings
are triaged by consumer and page context; a warning is neither an automatic fail
nor permission to invent a property.

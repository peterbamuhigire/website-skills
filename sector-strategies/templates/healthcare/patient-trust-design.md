---
title: Patient Trust & Appointment Conversion Design
sector: healthcare
---

# Patient Trust & Appointment Conversion

Patients choosing a healthcare provider make one of their most personal decisions online. 77% of patients use search engines before booking. The website must answer three questions instantly: "Can they help me?", "Can I trust them?", "How do I book?"

## The Trust-First Test

A patient visiting a healthcare website decides within 5 seconds:

- **"Do they treat my condition?"**: Specialty/service list visible immediately
- **"Are they qualified?"**: Doctor credentials, accreditation badges in view
- **"Can I book easily?"**: Appointment button prominent, phone number visible
- **"Are they nearby?"**: Location, hours, and contact info above the fold

## The Patient Conversion Funnel

```
[Symptom Search]    →  [Provider Research] →  [Trust Building]    →  [Book]
Google symptom        Specialty pages        Doctor profiles       Online booking
Referral              Service descriptions   Reviews/ratings       Phone call
Insurance search      Facility info          Accreditation badges  Walk-in info
```

### Page Flow
1. **Homepage**: Hero + appointment CTA → Specialties grid → Doctor highlights → Hours/location → Insurance → Testimonials
2. **Specialties**: Condition list → Treatment descriptions → Doctor matches → FAQ → Book appointment
3. **Doctor Profiles**: Photo + credentials → Bio → Specialties → Availability → Reviews → Book with this doctor
4. **Contact/Book**: Online booking widget → Phone number (click-to-call) → Walk-in hours → Map → Insurance info

## Trust Architecture

### Tier 1: Must-Have (Every Page)
- **Appointment button**: Prominent in header, fixed on mobile
- **Phone number**: Click-to-call, visible on every page
- **Hours of operation**: Current day highlighted
- **Physical address**: With map link
- **Emergency info**: "For emergencies, call..." banner

### Tier 2: High-Impact (Homepage + Specialties)
- **Doctor credentials**: MD, board certifications, fellowships
- **Accreditation badges**: JCI, national medical board, ISO
- **Patient reviews**: Star ratings + written reviews
- **Insurance accepted**: Logos of accepted insurance providers
- **Wait time/availability**: "Next available: Today at 2:30 PM"
- **Years of practice**: "Serving the community since 2005"

### Tier 3: Depth (About + Resources)
- **Facility tour**: Photos/video of clean, modern facilities
- **Technology showcase**: Modern equipment, certifications
- **Patient education**: Health articles, condition guides
- **Privacy compliance**: HIPAA/data protection visible
- **Community involvement**: Health drives, outreach, education
- **Awards/rankings**: "Top Hospital 2025", accreditation displays

## Doctor Profile Design

Doctor profiles are the #1 page patients visit. Pattern:

```
[Professional Photo — warm, approachable]
Dr. Jane Namukasa, MD, FRCS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Specialist in: Cardiology, Internal Medicine
Board Certified | 15+ Years Experience
Languages: English, Luganda, Swahili

"I believe in treating the whole person, not just symptoms."

Education & Training:
• MD — Makerere University, 2008
• Fellowship — Johns Hopkins, 2012

[Book with Dr. Namukasa]  [View Reviews (47)]
```

## Appointment Booking Design

- **One-click booking**: Minimum steps from any page to appointment
- **Online scheduling**: Calendar with available slots, real-time updates
- **Phone booking**: Click-to-call (prominently displayed)
- **Walk-in hours**: Clearly listed for urgent needs
- **Confirmation**: Immediate email/SMS with appointment details, what to bring

## Accessibility Requirements (Mandatory)

Healthcare websites MUST exceed standard accessibility:

- **Font size**: 18px minimum body text (patients include elderly/low-vision)
- **Contrast**: 7:1 for body text (WCAG AAA), 4.5:1 for UI elements
- **Colour independence**: Never use colour alone for information
- **Screen reader**: Full semantic HTML, ARIA labels
- **Keyboard navigation**: Complete tab navigation support
- **Touch targets**: 48px minimum (larger than standard 44px)
- **Language**: Plain language (no medical jargon without explanation)
- **Reading level**: Target 8th-grade reading level for patient content

## Common Mistakes
1. **Medical jargon** — "Otolaryngology" vs "Ear, Nose & Throat Specialist"
2. **Hidden booking** — appointment button must be 1 click from any page
3. **No phone number** — older patients prefer calling, make it prominent
4. **Generic stock photos** — "smiling doctor" stock photos destroy trust
5. **Missing insurance info** — patients need this before booking
6. **Small text** — 14px body text is unacceptable in healthcare
7. **No emergency info** — "For emergencies" must be visible on every page
8. **Outdated doctor list** — departed doctors still showing destroys trust

---

## Related References

- **healthcare-branding.md** — Color psychology, typography, photography, brand voice
- **healthcare-type-patterns.md** — Design patterns for 7 facility types
- **design-tokens.md** — Reference palettes, component specs

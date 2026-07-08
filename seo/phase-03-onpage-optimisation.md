# Phase 03 — On-Page Optimisation for primeturf.co.za
> Technical SEO Implementation | Generated 2026-06-11

---

## 1. Schema Markup — Implemented

All four JSON-LD blocks are deployed in `index.html` (before `</head>`) as a single `@graph` array.

### 1.1 LocalBusiness Schema
- `@type`: `["LocalBusiness", "HomeAndConstructionBusiness"]`
- `@id`: `https://primeturf.co.za/#business` (persistent identifier for cross-page reference)
- `areaServed`: Gauteng (Johannesburg, Pretoria, Sandton, Midrand, Centurion, Fourways, Bryanston) + Cape Town (Stellenbosch, Somerset West, Constantia)
- `hasOfferCatalog`: 5 services (Residential, Commercial, Pool Surround, Rooftop, Sports)
- `contactPoint`: `+27768048868`, English + Afrikaans

### 1.2 Service Schema
- References `#business` via `provider`
- Includes `WarrantyPromise`: 6 years, `LabourAndParts`
- `UnitPriceSpecification`: ZAR per m²
- `availability`: InStock

### 1.3 FAQPage Schema — 5 Questions
| Question | Target Long-Tail |
|---|---|
| Cost per m² in South Africa | "artificial grass cost per m2 south africa" |
| Can it go on concrete? | "can you put artificial grass on concrete" |
| What warranty? | "artificial grass 6 year warranty south africa" |
| Is it pet-safe? | "best artificial grass for dogs south africa" |
| How long does installation take? | purchase-intent qualifier |

**Expected result**: Google "People Also Ask" box appearances within 4–8 weeks of indexing.

### 1.4 BreadcrumbList Schema
Home → Services → Gallery → Contact — matches actual nav link structure.

### Validate
Test all schemas at: https://search.google.com/test/rich-results

---

## 2. Meta Tag Templates

### Homepage (`index.html`)
- **Title**: `Artificial Grass Gauteng | Premium Installation | PrimeTurf` (59 chars ✓)
- **Description**: `Premium artificial grass installation across Gauteng & Cape Town. 6-year warranty · Free site consultation · Trusted by Gauteng's finest estates. Call PrimeTurf today.` (170 chars — slightly long, Google trims at ~155; monitor CTR)

*Previously*: "PrimeTurf | Professional Artificial Grass Solutions · Gauteng" — brand-first, less keyword signal

### Johannesburg Landing Page (`artificial-grass-johannesburg.html`)
- **Title**: `Artificial Grass Johannesburg | Supply & Installation | PrimeTurf` (65 chars — trim to `Artificial Grass Johannesburg | Installation | PrimeTurf` if needed = 56 chars)
- **Description**: `Premium artificial grass installation across Johannesburg — Sandton, Midrand, Fourways, Bryanston & beyond. 6-year warranty · Free site consultation. Call PrimeTurf today.` (172 chars — suburb-rich for CTR)

### Cape Town Landing Page (`artificial-grass-cape-town.html`)
- **Title**: `Artificial Grass Cape Town | Water-Wise Installation | PrimeTurf` (64 chars ✓)
- **Description**: `Drought-resistant artificial grass installation across Cape Town, Stellenbosch & the Winelands. Beat water restrictions permanently. 6-year warranty · Free quote from PrimeTurf.` (180 chars — trim if Google truncates)

### Contact Page (`contact.html`) — existing, retained
- **Title**: `PrimeTurf | Request a Free Quote — Gauteng` (42 chars ✓)
- **Description**: `Request a free site consultation from PrimeTurf — Gauteng's premium artificial grass specialists. 6-year warranty, professional installation.` (143 chars ✓)

### Commercial/Architect Page (`commercial-artificial-turf-specification.html`) — Phase 03 Priority 1 (not yet created)
- **Title**: `Commercial Artificial Turf Specification | Architects | PrimeTurf` (66 chars — acceptable)
- **Description**: `Artificial grass specification support for architects and developers in South Africa. Technical data sheets, supply & install, commercial projects across Gauteng & Cape Town.` (174 chars)

---

## 3. City Landing Page Structure

### 3.1 Johannesburg (`/artificial-grass-johannesburg.html`) — LIVE
**H1**: Artificial Grass Johannesburg

**H2 Structure**:
- Why PrimeTurf Johannesburg / Gauteng's Premium Turf Specialists
- Applications: Where We Install (6 use-cases)
- Johannesburg Projects (gallery)
- We Cover All of Johannesburg (suburb tags)
- Frequently Asked Questions
- Ready for a Lush Johannesburg Lawn? (CTA)

**Local Signals**:
- 18 suburb tags: Sandton, Midrand, Fourways, Bryanston, Morningside, Rivonia, Sunninghill, Waterfall Estate, Centurion, Pretoria East, Kyalami, Steyn City, etc.
- WhatsApp pre-populated message references "Johannesburg"
- Features section references "Gauteng's high-altitude UV intensity"

**Internal Links**: Homepage, Cape Town page, Architect spec page, Contact

### 3.2 Cape Town (`/artificial-grass-cape-town.html`) — LIVE
**H1**: Artificial Grass Cape Town

**H2 Structure**:
- Why PrimeTurf Cape Town / The Water-Wise Lawn Solution
- Natural vs Artificial comparison table (Cape Town water restrictions angle)
- Applications: Where We Install — Cape Town specific
- Cape Town Projects (gallery)
- Covering All of Cape Town (suburb tags)
- Frequently Asked Questions
- Never Worry About Water Restrictions Again (CTA)

**Local Signals**:
- 18 suburb tags: Constantia, Bishopscourt, Camps Bay, Clifton, Hout Bay, Stellenbosch, Franschhoek, Paarl, Somerset West, Gordon's Bay, Bloubergstrand, etc.
- Water restriction angle appears in hero, CTA band, and FAQ
- FAQ includes coastal/salt-air question for Seaboard properties
- References Cape Winelands estates
- Afrikaans: mention `kunsmatige gras Kaapstad` in alt text candidates (not added yet)

---

## 4. Internal Link Audit

### http:// references in public pages
No `http://primeturf` links found in live pages (`index.html`, `contact.html`, `wa.html`).  
Only `http://` references are in internal tool pages (SEO dashboard display data, SEO engine prompt text) — not live public links.

### Recommended Internal Link Anchors (top 10)
| From | To | Anchor Text |
|---|---|---|
| `index.html` footer/nav | `/artificial-grass-johannesburg.html` | "Johannesburg" or "Artificial Grass Johannesburg" |
| `index.html` footer/nav | `/artificial-grass-cape-town.html` | "Cape Town" or "Artificial Grass Cape Town" |
| `artificial-grass-johannesburg.html` | `artificial-grass-cape-town.html` | "Cape Town" (bottom of suburb section) |
| `artificial-grass-cape-town.html` | `artificial-grass-johannesburg.html` | "Johannesburg" (bottom of suburb section) |
| Both city pages | `/commercial-artificial-turf-specification.html` | "Architect & Developer Specification" |
| Both city pages | `/contact.html` | "Free Site Consultation" |
| `contact.html` | `/` | "PrimeTurf homepage" (logo link) |
| `index.html` brand-statement section | `/contact.html` | "Book a free consultation" |
| `index.html` gauteng-band section | `/artificial-grass-johannesburg.html` | "Johannesburg" |
| All pages | `tel:+27768048868` | "076 804 8868" |

### Action required on homepage
Add city page links to `index.html` footer nav and Gauteng Region Band section.  
Current footer nav links to: Services / Gallery / Testimonials / Contact — add Johannesburg and Cape Town.

---

## 5. Next Priority: Architect Specification Page

From the Phase 02 priority matrix, the Spec-Layer cluster (Cluster C) was rated the #1 priority.  
`/commercial-artificial-turf-specification.html` still needs to be created.

Content requirements:
- Target keyword: "artificial grass specification architect South Africa"
- Downloadable spec sheet PDF (even a simple one)
- Product data tables (pile height, density, UV rating, drainage rate)
- LocalBusiness schema with architect/commercial `serviceType`
- Internal links from both city pages already point to it

---

*Next: Phase 04 — Content Engine (editorial calendar, blog briefs, GBP posts)*

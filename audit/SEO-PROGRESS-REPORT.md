# PrimeTurf SEO Migration Progress Report

**Date**: 2026-08-17
**Previous audit**: 2026-08-16
**Site**: www.primeturf.co.za (Wix site ID: 9e5c1b74-f699-4def-ae95-5a8a8664880d)

---

## What Changed (Owner browser work, 2026-08-16 to 2026-08-17)

Custom SEO coverage went from **4 of 15 pages** to **12 of 15 pages**. The site owner added custom titles and meta descriptions to 8 pages via the Wix Editor and also enhanced the 4 pages that already had custom SEO.

### Pages Fixed (8 new custom SEO overrides)

| Page | URL | Old Title | New Title | Description Added |
|------|-----|-----------|-----------|-------------------|
| Home | `/` | Home \| Prime Turf SA | PrimeTurf \| Premium Artificial Grass Solutions | Yes |
| Services | `/services` | Services (List) \| Prime Turf SA | Our Services \| PrimeTurf Artificial Grass Installation | Yes |
| Quote | `/quote` | Get a Quote \| Prime Turf SA | Instant Artificial Grass Quote \| PrimeTurf SA | Yes |
| Blog | `/blog` | Blog \| Prime Turf SA | Artificial Grass Blog & Guides -- South Africa | Yes |
| About Us | `/about-us` | About Us \| Prime Turf SA | About Us \| PrimeTurf Artificial Grass Specialists | Yes |
| Product Catalogue | `/services-5` | **Poduct** Catalogue \| Prime Turf SA | Product Catalogue \| PrimeTurf Artificial Grass Ranges | Yes |
| Portfolio | `/gallery` | Portfolio \| Prime Turf SA | Portfolio \| PrimeTurf Artificial Grass Projects | Yes |
| Contact | `/contact` | Contact \| Prime Turf SA | PrimeTurf \| Request a Free Quote -- Gauteng | Yes |

### Pages Enhanced (4 already had custom SEO)

| Page | URL | Title Change |
|------|-----|-------------|
| Sandton | `/artificial-grass-sandton` | Added "\| PrimeTurf" suffix, updated description |
| Johannesburg | `/artificial-grass-johannesburg` | Added "\| PrimeTurf" suffix, updated description |
| Hyde Park | `/artificial-grass-hyde-park` | Added "\| PrimeTurf" suffix, updated description |
| Edenvale | `/artificial-grass-edenvale` | Added "\| PrimeTurf" suffix, updated description |

### Issues Resolved

- **"Poduct" typo** (page ggwix): Fixed to "Product Catalogue"
- **Homepage generic title**: "Home | Prime Turf SA" replaced with keyword-rich "PrimeTurf | Premium Artificial Grass Solutions"
- **Missing meta descriptions**: All 12 active pages now have custom descriptions
- **OG/Twitter titles**: Wix auto-inherits custom titles to OG and Twitter tags

### Pages Without Custom SEO (3 -- all expected)

| Page | URL | Reason |
|------|-----|--------|
| Accessibility Statement | `/accessibility-statement` | Wix default page, no SEO value |
| Preparation | `/about-6` | Wix-only page, no GitHub equivalent, low priority |
| Privacy Policy | `/english-privacy-policy` | Legal page, redirect target only |

---

## Remaining Open Issues

### CRITICAL: Google-Indexed 404s (unchanged)

4 old GitHub URLs confirmed indexed by Google, returning 404 on Wix:

1. `/artificial-grass-cape-town.html` -- page does not exist on Wix yet
2. `/artificial-grass-johannesburg.html` -- Wix page exists at `/artificial-grass-johannesburg`, needs 301 redirect
3. `/quote-calculator.html` -- Wix page exists at `/quote`, needs 301 redirect
4. `/page-boksburg.html` -- page does not exist on Wix yet

**Action required**: Create missing pages, then configure 301 redirects via Wix URL Redirect Manager (dashboard only).

### HIGH: 15 Missing Suburb/City Pages (1 city + 14 suburbs)

These pages existed on the original GitHub site and drove location-specific organic traffic. Content files are ready in `migration/content/*.md`. An additional legal page (terms-of-service) is also missing, bringing the total to 16.

| Priority | Page | Wix Slug | Content File |
|----------|------|----------|-------------|
| P0 | Cape Town | `/artificial-grass-cape-town` | `migration/content/artificial-grass-cape-town.md` |
| P0 | Pretoria East | `/artificial-grass-pretoria-east` | `migration/content/artificial-grass-pretoria-east.md` |
| P1 | Centurion | `/artificial-grass-centurion` | `migration/content/artificial-grass-centurion.md` |
| P1 | Steyn City | `/artificial-grass-steyn-city` | `migration/content/artificial-grass-steyn-city.md` |
| P1 | Midrand | `/artificial-grass-midrand` | `migration/content/artificial-grass-midrand.md` |
| P1 | Fourways | `/artificial-grass-fourways` | `migration/content/artificial-grass-fourways.md` |
| P1 | Bryanston | `/artificial-grass-bryanston` | `migration/content/artificial-grass-bryanston.md` |
| P1 | Boksburg | `/artificial-grass-boksburg` | `migration/content/artificial-grass-boksburg.md` |
| P2 | Bedfordview | `/artificial-grass-bedfordview` | `migration/content/artificial-grass-bedfordview.md` |
| P2 | Houghton | `/artificial-grass-houghton` | `migration/content/artificial-grass-houghton.md` |
| P2 | Mooikloof | `/artificial-grass-mooikloof` | `migration/content/artificial-grass-mooikloof.md` |
| P2 | Randburg | `/artificial-grass-randburg` | `migration/content/artificial-grass-randburg.md` |
| P2 | Roodepoort | `/artificial-grass-roodepoort` | `migration/content/artificial-grass-roodepoort.md` |
| P2 | Silver Lakes | `/artificial-grass-silver-lakes` | `migration/content/artificial-grass-silver-lakes.md` |
| P2 | Waterfall City | `/artificial-grass-waterfall-city` | `migration/content/artificial-grass-waterfall-city.md` |

**Action required**: Create these pages in Wix Editor (Classic Editor does not support page creation via API). SEO metadata specs are in `audit/missing-pages-spec.json`.

### HIGH: 22+ 301 Redirects Not Configured

No redirects have been set up yet. The complete redirect map is in `audit/redirect-spec.csv`.

- 10 redirects are **ready** (target page exists on Wix)
- 13 redirects are **blocked** (target page needs creation first)

**Action required**: Configure via Wix site dashboard > SEO Tools > URL Redirect Manager. No REST API available.

### MEDIUM: No JSON-LD Structured Data

No pages currently have JSON-LD schema markup. The GitHub site had schemas on several pages:

| Schema Type | Recommended Pages |
|-------------|-------------------|
| LocalBusiness | Homepage, Johannesburg, Cape Town, all suburb pages |
| Service | All suburb pages |
| FAQPage | Johannesburg (3 Qs), Cape Town (3 Qs) |
| BreadcrumbList | All suburb pages |
| Blog | Blog index |
| Article | Blog posts |

**Action required**: Add via Wix Velo custom code or Editor code injection.

### LOW: All Pages Share Same OG Image

Every page uses the same default Wix site OG image. Page-specific images would improve social sharing CTR.

---

## Scorecard

| Category | Before (Aug 16) | After (Aug 17) | Target |
|----------|-----------------|----------------|--------|
| Pages with custom title | 4 / 15 | **12 / 15** | 12 / 15 |
| Pages with meta description | 4 / 15 | **12 / 15** | 12 / 15 |
| Location pages on Wix (city+suburb) | 4 / 19 | 4 / 19 | **19 / 19** |
| 301 redirects configured | 0 / 22 | 0 / 22 | **22 / 22** |
| Pages with JSON-LD schema | 0 / 15 | 0 / 15 | **6+ / 15** |
| Google-indexed 404s | 4 | 4 | **0** |
| Typos in titles | 1 | **0** | 0 |

---

## Next Steps (Priority Order)

1. **Create Cape Town page** on Wix (P0 -- Google is indexing a 404 for this URL)
2. **Create Boksburg page** on Wix (P0 -- Google is indexing a 404 for this URL)
3. **Configure 10 ready redirects** in Wix URL Redirect Manager
4. **Create remaining 11 suburb pages** in build order from `audit/missing-pages-spec.json`
5. **Configure remaining redirects** as pages are created
6. **Add JSON-LD structured data** to Homepage, Johannesburg, and suburb pages
7. **Submit updated sitemap** to Google Search Console
8. **Request indexing** for newly created pages in GSC

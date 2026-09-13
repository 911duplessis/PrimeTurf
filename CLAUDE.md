# PrimeTurf -- Project Memory

## What This Project Is

PrimeTurf's website migrated from GitHub Pages to Wix (Classic Editor) around 2026-07-17. The CNAME was deleted and `www.primeturf.co.za` now points to a Wix site (ID: `9e5c1b74-f699-4def-ae95-5a8a8664880d`). Google still indexes old `.html` URLs that now 404 on Wix. This repo contains the original GitHub site, migration content files, audit data, and automation scripts for **forensic SEO migration recovery** -- restoring missing pages and SEO architecture around the existing Wix site.

## Hard Constraints (DO NOT violate)

1. DO NOT significantly edit existing content on the current Wix website
2. DO NOT delete anything on the Wix site
3. DO NOT publish changes without explicit owner approval
4. DO NOT create redirects without explicit owner approval
5. Approach is **ADD + CONNECT + OPTIMIZE** -- not REBUILD

## Resolved Decisions (DO NOT re-ask these)

- **Warranty**: 6-year (NOT 8-year -- the old homepage's "8 Year Manufacturers Warranty" was wrong)
- **Contact email**: `leon@primeturf.co.za` (NOT `social@primeturf.co.za`)
- **Phone**: 076 804 8868
- `/primeturf-vs-easigrass.html`: DO NOT republish -- redirect to homepage (stakeholder decision)
- **Wix Editor type**: Classic Editor (not Studio) -- no API for page creation
- **Redirects method**: Wix SEO Redirects REST API (bulk create confirmed working 2026-08-18)
- `/about-6` page: **Keep** and rename to "Site Preparation" (owner decision 2026-08-20)
- **Approved location pages**: 9 Gauteng suburbs (Pretoria East, Moreleta Park, Silver Lakes, Faerie Glen, Waterkloof, Mooikloof, Lynnwood, Garsfontein, Centurion & Midrand) + 1 Western Cape regional page (owner decision 2026-09-12)
- **Western Cape**: Regional page only -- do NOT invent suburbs, branches, offices, projects, or testimonials
- **Brand positioning**: "Luxury Artificial Turf Specialists, Serving Gauteng & Western Cape"
- **Navigation**: Home, About, Services, Portfolio, Preparation, Service Areas, Blog, Contact
- **Page structure**: Hero → Solutions → Why PrimeTurf → Applications → Portfolio → Service Area → CTA
- **Colour palette**: Deep Forest / Harvest Gold / Warm Ivory / Cream

## Open Decisions (ASK the user)

- Site name shows "Prime Turf  SA" (double space) in Wix -- has this been corrected?

## Current State (as of 2026-09-13)

| Metric | Count |
|--------|-------|
| Wix pages published | 17 |
| Pages in editor (draft/unpublished) | ~13 |
| Pages with custom SEO | 15 / 17 |
| Missing legal pages | 1 (terms-of-service) |
| 301 redirects configured | 10 / 27 |
| JSON-LD schemas added | 3 (LocalBusiness, BreadcrumbList, Service) via Velo (not yet synced) |
| Contact form upgraded | Yes -- "Request a Quote" (8 fields, 2 dropdowns) |
| Google-indexed 404s | 4 |
| Site businessName | "Service Map" (should be "PrimeTurf") |
| Site displayName | "Prime Turf SA" (verify double-space) |

### Published pages (in sitemap as of 2026-09-13)

/, /services, /services-5, /about-us, /about-6, /blog, /contact, /quote, /gallery, /accessibility-statement, /english-privacy-policy, /artificial-grass-johannesburg, /artificial-grass-sandton, /artificial-grass-hyde-park, /artificial-grass-edenvale, /artificial-grass-boksburg, /artificial-grass-cape-town

### Draft pages (created in editor, NOT published)

All new location pages are built in Wix Editor but not yet published. Includes: Pretoria East, Moreleta Park, Silver Lakes, Faerie Glen, Waterkloof, Mooikloof, Lynnwood, Garsfontein, Centurion (separate), Midrand (separate), Western Cape, Artificial Turf Gauteng, Service Areas landing.

**Note**: The spec had Centurion & Midrand as one combined page (`/artificial-grass-centurion-midrand`). Owner created them as two separate pages. Boksburg and Artificial Turf Gauteng were added beyond the original approved list.

### Known SEO issues

- **Garsfontein**: Meta description contains Boksburg/East Rand content instead of Garsfontein (copy-paste error)
- **Boksburg, Cape Town**: Need custom SEO titles/descriptions set (currently default)

### Completed via API (2026-09-12)

- **Contact form upgraded** to "Request a Quote" (form ID: `e04a7a22-2e2d-4c5e-b1a9-1cf20b99f79a`, revision 2)
  - Fields: First Name, Last Name, Email, WhatsApp/Phone, Suburb/Area (required), Service Interest (dropdown, 10 options), Approximate Project Size (dropdown, 6 options), Message
  - Submit button: "Request a Quote"
  - Thank-you message updated with WhatsApp number
  - Contact mapping: First Name → FIRST_NAME, Last Name → LAST_NAME, Email → EMAIL, Phone → PHONE
- **JSON-LD structured data** added via Velo in `masterPage.js` (my-site-4 repo)
  - LocalBusiness schema on all pages
  - BreadcrumbList with dynamic breadcrumbs
  - Service schema on location pages (artificial-grass-* URLs)
- **FLAG**: Verify notification email is set to leon@primeturf.co.za in Wix Dashboard → Settings → Notifications

## Implementation Files (2026-09-12)

Production-ready content and specs for the full migration. Pages must be created manually in Wix Classic Editor.

| File | Purpose |
|------|---------|
| `implementation/pages/pretoria-east.md` | Pretoria East location page content |
| `implementation/pages/moreleta-park.md` | Moreleta Park location page content |
| `implementation/pages/silver-lakes.md` | Silver Lakes location page content |
| `implementation/pages/faerie-glen.md` | Faerie Glen location page content |
| `implementation/pages/waterkloof.md` | Waterkloof location page content |
| `implementation/pages/mooikloof.md` | Mooikloof location page content |
| `implementation/pages/lynnwood.md` | Lynnwood location page content |
| `implementation/pages/garsfontein.md` | Garsfontein location page content |
| `implementation/pages/centurion-midrand.md` | Centurion & Midrand location page content |
| `implementation/pages/western-cape.md` | Western Cape regional page content |
| `implementation/pages/service-areas.md` | Service Areas landing page content |
| `implementation/specs/seo-specification.md` | SEO titles, meta descriptions, H1s, canonicals for all pages |
| `implementation/specs/navigation.md` | Navigation structure and Service Areas dropdown spec |
| `implementation/specs/contact-form.md` | Contact form fields, options, and submission behaviour |
| `implementation/guide/wix-editor-guide.md` | Step-by-step guide for building pages in Wix Classic Editor |

## Audit & Migration Files (earlier work)

| File | Purpose |
|------|---------|
| `audit/wix-seo-current-state.json` | Latest snapshot of all 15 Wix pages' SEO metadata |
| `audit/wix-seo-gaps.json` | Gap analysis with severity ratings |
| `audit/SEO-PROGRESS-REPORT.md` | Delta report showing what changed since initial audit |
| `audit/url-migration-matrix.csv` | Master URL mapping: GitHub URL -> Wix URL -> status |
| `audit/missing-pages-spec.json` | Specs for all 16 missing pages (SEO, schema, links) |
| `audit/redirect-spec.csv` | Complete 301 redirect map |
| `migration/content/*.md` | Original migration content files |
| `prompts/wix-page-builder.md` | Prompt for Claude browser extension in Wix Editor |

## Remaining Work (priority order, updated 2026-09-13)

1. ~~Create new pages in Wix Editor~~ **DONE** — all location pages created in editor (not yet published)
2. **Publish all draft pages** — ~13 pages need to be published in Wix Editor
3. **Add content to pages** using `implementation/pages/*.md` files and `implementation/guide/wix-editor-guide.md`
4. **Set SEO metadata on new pages** via Wix SEO API (I'll do this after pages are published)
5. **Fix Garsfontein meta description** — currently shows Boksburg content (API fix)
6. **Configure remaining 17 301 redirects** via Wix SEO Redirects API (2 ready now, 5 after publishing, 8 redirect to nearest, 1 needs terms page)
7. **Configure navigation** per `implementation/specs/navigation.md` — rename "Locations" to "Service Areas", optionally group by region
8. ~~Upgrade contact form~~ **DONE** — "Request a Quote" form live (8 fields, 2 dropdowns, revision 2)
9. **Verify notification email** is set to leon@primeturf.co.za in Wix Dashboard → Settings → Notifications
10. **Fix business name** — currently "Service Map", should be "PrimeTurf" (Dashboard → Settings → Business Info)
11. **Sync Velo code** — run `wix dev` in `/my-site-4` to push JSON-LD structured data to live site
12. **Create terms-of-service page** on Wix (noindex OK)
13. ~~Add JSON-LD structured data~~ **DONE** — LocalBusiness, BreadcrumbList, Service schemas in masterPage.js
14. **Submit updated sitemap** to Google Search Console
15. **Request indexing** for new pages in GSC

## Business Details

- **Company**: PrimeTurf
- **Domain**: www.primeturf.co.za
- **Phone**: 076 804 8868
- **Email**: leon@primeturf.co.za
- **WhatsApp**: wa.me/27768048868
- **Service areas**: Gauteng (primary), Western Cape (secondary)
- **Warranty**: 6-year on all installations
- **Google Analytics**: G-3Z5G37WW47
- **Google Search Console**: Verified (meta tag)

## Branch

Development branch: `claude/youthful-lovelace-4q68qp` on `911duplessis/PrimeTurf`

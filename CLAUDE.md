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

## Current State (as of 2026-09-12)

| Metric | Count |
|--------|-------|
| Wix pages live | 15 |
| Pages with custom SEO | 15 / 15 |
| New location pages to create | 10 (9 Gauteng + 1 Western Cape) |
| Service Areas landing page | 1 (to create) |
| Missing legal pages | 1 (terms-of-service) |
| 301 redirects configured | 10 / 27 |
| JSON-LD schemas added | 0 |
| Google-indexed 404s | 4 |

The 4 existing location pages on Wix (Johannesburg, Sandton, Hyde Park, Edenvale) have custom SEO with enhanced titles and descriptions.

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

## Remaining Work (priority order)

1. **Create 11 new pages in Wix Editor** using content from `implementation/pages/*.md` and SEO from `implementation/specs/seo-specification.md`. Follow `implementation/guide/wix-editor-guide.md`. Build order: Service Areas landing → Pretoria East → Centurion & Midrand → Silver Lakes → Waterkloof → Mooikloof → Moreleta Park → Faerie Glen → Lynnwood → Garsfontein → Western Cape
2. **Configure navigation** per `implementation/specs/navigation.md` — Service Areas dropdown with Gauteng/Western Cape grouping
3. **Upgrade contact form** per `implementation/specs/contact-form.md` — verify notification email set to leon@primeturf.co.za
4. **Create terms-of-service page** on Wix (noindex OK)
5. **Configure remaining 17 301 redirects** via Wix SEO Redirects API (blocked until pages created)
6. **Add JSON-LD structured data** (LocalBusiness, Service, FAQ, BreadcrumbList) via Wix Velo or code injection
7. **Submit updated sitemap** to Google Search Console
8. **Request indexing** for new pages in GSC

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

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

## Open Decisions (ASK the user)

- Site name shows "Prime Turf  SA" (double space) in Wix -- has this been corrected?

## Current State (as of 2026-08-20)

| Metric | Count |
|--------|-------|
| Wix pages live | 15 |
| Pages with custom SEO | 15 / 15 |
| Missing location pages | 15 (1 city + 14 suburbs) |
| Missing legal pages | 1 (terms-of-service) |
| 301 redirects configured | 10 / 27 |
| JSON-LD schemas added | 0 |
| Google-indexed 404s | 4 |

The 4 existing location pages on Wix (Johannesburg, Sandton, Hyde Park, Edenvale) have custom SEO with enhanced titles and descriptions.

## Key Files

| File | Purpose |
|------|---------|
| `audit/wix-seo-current-state.json` | Latest snapshot of all 15 Wix pages' SEO metadata |
| `audit/wix-seo-gaps.json` | Gap analysis with severity ratings |
| `audit/SEO-PROGRESS-REPORT.md` | Delta report showing what changed since initial audit |
| `audit/url-migration-matrix.csv` | Master URL mapping: GitHub URL -> Wix URL -> status |
| `audit/missing-pages-spec.json` | Specs for all 16 missing pages (SEO, schema, links) |
| `audit/redirect-spec.csv` | Complete 301 redirect map |
| `migration/content/*.md` | Ready-to-use content for all missing pages |
| `prompts/wix-page-builder.md` | Prompt for Claude browser extension in Wix Editor |

## Remaining Work (priority order)

1. **Create 15 missing location pages** in Wix Editor using content from `migration/content/artificial-grass-*.md` and SEO specs from `audit/missing-pages-spec.json`. Build order: Cape Town (P0) -> Pretoria East, Centurion, Fourways, Bryanston, Boksburg (batch 2) -> remaining 9 suburbs (batch 3)
2. **Create terms-of-service page** on Wix (noindex OK)
3. **Configure remaining 17 301 redirects** via Wix SEO Redirects API (blocked until pages created)
4. **Add JSON-LD structured data** (LocalBusiness, Service, FAQ, BreadcrumbList) via Wix Velo or code injection
5. **Submit updated sitemap** to Google Search Console
6. **Request indexing** for new pages in GSC

## Business Details

- **Company**: PrimeTurf
- **Domain**: www.primeturf.co.za
- **Phone**: 076 804 8868
- **Email**: leon@primeturf.co.za
- **WhatsApp**: wa.me/27768048868
- **Service areas**: Gauteng (primary), Cape Town (secondary)
- **Warranty**: 6-year on all installations
- **Google Analytics**: G-3Z5G37WW47
- **Google Search Console**: Verified (meta tag)

## Branch

Development branch: `claude/primeturf-github-wix-seo-6bbzmb` on `911duplessis/PrimeTurf`

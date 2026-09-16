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

## Current State (as of 2026-09-15, updated)

| Metric | Count |
|--------|-------|
| Wix pages live | 30 (15 original + 13 new location + 2 utility) |
| Pages with custom SEO | 28 / 30 |
| Pages without custom SEO | 2 (o6srm /blank-3, tiwvv /service-area) |
| Missing from original spec | 8 (Fourways, Bryanston, Steyn City, Bedfordview, Houghton, Randburg, Waterfall City, terms-of-service) |
| Deleted ghost pages | 2 (zqx03 + xtajx, both Roodepoort) |
| 301 redirects configured | 10 / 27 |
| 301 redirects ready (need approval) | 7 |
| 301 redirects still blocked | 10 |
| JSON-LD schemas added | 5 pages (13 schemas) |
| Custom embeds (CSS) | 1 (layout fix, rev 2) |

### New pages created by owner (13 location + 2 utility)

| Page ID | URL | SEO Status |
|---------|-----|------------|
| u6lo4 | /artificial-grass-cape-town | Enhanced (matches spec) |
| y43rr | /artificial-grass-pretoria-east | Enhanced 2026-09-15 |
| d9iwr | /artificial-grass-centurion | Enhanced 2026-09-15 |
| qquc7 | /artificial-grass-midrand | Enhanced 2026-09-15 |
| weuso | /artificial-grass-boksburg | Enhanced (matches spec) |
| nqcvo | /artificial-grass-mooikloof | Enhanced 2026-09-15 |
| ju2o2 | /artificial-grass-silver-lakes | Enhanced 2026-09-15 |
| fkibf | /artificial-grass-garsfontein | Fixed 2026-09-15 (had wrong desc) |
| gykvx | /artificial-grass-faerie-glen | Enhanced 2026-09-15 |
| helb4 | /artificial-grass-lynnwood | Enhanced 2026-09-15 |
| kqqlm | /artificial-grass-waterkloof | Enhanced 2026-09-15 |
| wcv50 | /artificial-grass-moreleta-park | Enhanced 2026-09-15 |
| nz9gr | /artificial-grass-western-cape | Enhanced 2026-09-15 |
| tdhd8 | /service-areas | Hub page (has SEO) |
| tiwvv | /service-area | Unconfigured list page |

### Layout fix (CSS Custom Embed)

Embed `24fc0b9c-96fe-4550-a8c2-8e9be1a997ba` (rev 2):
- Widens site from 980px to 1200px with responsive gutters
- Constrains hero strip height to 500px max
- Tightens hero padding (60px top, 40px bottom)
- Header z-index fix

### JSON-LD structured data (deployed via Velo 2026-09-16)

All location pages now have page-specific structured data via Wix Velo code:
- Each location page: LocalBusiness + BreadcrumbList + Service + FAQPage (real Q&A)
- Homepage (bqvuq): LocalBusiness + WebSite
- Contact (m80pg): ContactPage
- Get a Quote (evnw7): WebPage
- masterPage.js: Site-wide fallback schemas (LocalBusiness, WebSite, BreadcrumbList, Service)

### Wix Velo Architecture (PrimeTurf-Wix repo)

Branch: `claude/velo-page-content-setup` on `911duplessis/PrimeTurf-Wix`
- `src/public/siteConfig.js` -- Business constants (phone, email, warranty, URLs)
- `src/public/schemas.js` -- JSON-LD schema builders (buildLocationSchemas, buildServiceAreaSchemas)
- `src/public/pageSetup.js` -- Element binding (bindContent) and CTA wiring (setupCTAs)
- Each page file: imports shared modules, defines PAGE config + content, sets structured data, binds elements
- Element IDs convention: `#heroTitle`, `#heroSubtitle`, `#heroDesc`, `#introTitle`, `#introText`, `#areasTitle`, `#areasText`, `#ctaTitle`, `#ctaDesc`, `#ctaWhatsapp`, `#ctaCall`, `#heroQuoteBtn`, `#ctaQuote`

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

1. **Merge Velo branch** -- `claude/velo-page-content-setup` on PrimeTurf-Wix. Adds structured data + content binding to all pages. Owner should review and merge to main.
2. **Build visual content in Wix Editor** -- 13 new location pages have Velo code but need visual elements added in Classic Editor. Use element IDs from the Velo convention (see architecture above) so content auto-populates.
3. **Create 7 remaining location pages** still missing from original spec: Fourways, Bryanston, Steyn City, Bedfordview, Houghton, Randburg, Waterfall City. Also re-create Roodepoort (was deleted).
4. **Create terms-of-service page** on Wix (noindex OK)
5. **Configure 7 ready 301 redirects** (Cape Town, Pretoria East, Centurion, Midrand, Boksburg, Mooikloof, Silver Lakes) -- pages exist, needs owner approval
6. **Configure remaining 10 blocked redirects** -- waiting for pages to be created
7. **Submit updated sitemap** to Google Search Console
8. **Request indexing** for new pages in GSC
9. **Clean up** blank page (o6srm /blank-3) and unconfigured list page (tiwvv /service-area)

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

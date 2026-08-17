# PrimeTurf: Forensic SEO Migration Report

**Generated**: 2026-08-16  
**Domain**: www.primeturf.co.za  
**Migration**: GitHub Pages → Wix (Classic Editor)  
**Wix Site ID**: 9e5c1b74-f699-4def-ae95-5a8a8664880d

---

## Executive Summary

PrimeTurf's site migrated from GitHub Pages to Wix around 2026-07-17. The original site had **27 public pages**; the current Wix site has **15 static pages**, with only **4 suburb pages** carrying custom SEO metadata. Google is still indexing old `.html` URLs that now return 404 on Wix, causing **active SEO equity loss**.

The gap is a **content gap**, not a redirect problem — domain-level redirects (http/https, bare/www) are healthy. The fix is to recreate the 13 missing suburb/city pages on Wix, set proper SEO metadata on all 15 existing pages, then configure 22+ 301 redirects from old `.html` URLs.

### Key Numbers

| Metric | Count |
|--------|-------|
| GitHub public pages | 27 |
| Wix static pages | 15 |
| Wix pages with custom SEO | 4 |
| Missing suburb/city pages | 13 |
| Google-indexed 404s (confirmed) | 4 |
| 301 redirects needed | 22 |
| Wix pages needing SEO improvement | 11 |

---

## 1. GitHub SEO Baseline

### 1.1 Page Inventory (27 public pages)

| URL | Title | Schema | Priority |
|-----|-------|--------|----------|
| `/` | PrimeTurf \| Premium Artificial Grass Solutions | none | 1.0 |
| `/artificial-grass-johannesburg.html` | Artificial Grass Johannesburg \| 6-Year Warranty | none | 0.8 |
| `/artificial-grass-cape-town.html` | Artificial Grass Cape Town \| Water-Wise Installation | none | 0.8 |
| `/page-sandton.html` | Artificial Grass Sandton \| Premium Installation | Service | 0.9 |
| `/page-pretoria-east.html` | Artificial Grass Pretoria East \| Waterkloof... | Service | 0.9 |
| `/page-centurion.html` | Artificial Grass Centurion \| Golf Estate Specialists | none | 0.9 |
| `/page-fourways.html` | Artificial Grass Fourways \| Dainfern, Lonehill... | none | 0.8 |
| `/page-bryanston.html` | Artificial Grass Bryanston \| Luxury Residential | none | 0.8 |
| `/page-bedfordview.html` | Artificial Grass Bedfordview \| East Rand Luxury | none | 0.8 |
| `/page-boksburg.html` | Artificial Grass Boksburg \| East Rand Residential | none | 0.8 |
| `/page-edenvale.html` | Artificial Grass Edenvale \| East Rand Specialists | none | 0.8 |
| `/page-houghton.html` | Artificial Grass Houghton \| Luxury Estate | none | 0.8 |
| `/page-hyde-park.html` | Artificial Grass Hyde Park \| Ultra-Luxury Estate | none | 0.8 |
| `/page-midrand.html` | Artificial Grass Midrand \| Secure Estate | none | 0.8 |
| `/page-mooikloof.html` | Artificial Grass Mooikloof \| Country Estate | none | 0.8 |
| `/page-randburg.html` | Artificial Grass Randburg \| North Johannesburg | none | 0.8 |
| `/page-roodepoort.html` | Artificial Grass Roodepoort \| West Johannesburg | none | 0.8 |
| `/page-silver-lakes.html` | Artificial Grass Silver Lakes \| Pretoria East | none | 0.8 |
| `/page-steyn-city.html` | Artificial Grass Steyn City \| Luxury Estate | Service | 0.8 |
| `/page-waterfall-city.html` | Artificial Grass Waterfall City \| Luxury Estate | Service | 0.8 |
| `/quote-calculator.html` | Artificial Grass Quote Calculator South Africa | none | 0.7 |
| `/quote/` | Instant Artificial Grass Quote \| PrimeTurf SA | none | 0.9 |
| `/contact.html` | PrimeTurf \| Request a Free Quote — Gauteng | none | 0.6 |
| `/blog/` | Artificial Grass Blog & Guides — South Africa | Blog | 0.6 |
| `/blog/artificial-grass-cost-guide-south-africa.html` | Artificial Grass Cost Per m2 South Africa — 2026 | Article, FAQPage | 0.6 |
| `/blog/drought-proof-garden-cape-town.html` | Drought-Proof Your Cape Town Garden | Article, FAQPage | 0.6 |
| `/primeturf-vs-easigrass.html` | PrimeTurf vs Easigrass SA \| Compare Installers | Service | DO NOT PUBLISH |

### 1.2 GitHub Sitemap

The GitHub `sitemap.xml` contains 27 URLs with priorities from 0.6 to 1.0. Last modification dates range from 2026-07-07 to 2026-07-15. The sitemap was auto-maintained by a GitHub Actions workflow (`.github/workflows/update-sitemap.yml`).

### 1.3 Noindex Pages (not part of SEO recovery)

- `/privacy-policy.html` — `noindex, follow`
- `/terms-of-service.html` — `noindex, follow`
- `/wa.html` — WhatsApp utility redirect
- `/indexMaster.html` — unlinked draft homepage

---

## 2. Current Wix Site State

### 2.1 Site Configuration

- **Platform**: Wix Classic Editor, Premium plan
- **Velo**: Enabled
- **Apps installed**: Promote SEO, Wix Blog, Wix Forms, Wix Portfolio, Wix Invoices
- **Google Verification**: Active (meta tag `dz5Y4cIXi1isX3TD0Vt4TLgf54KDsF9l2qZYBcUtI70`)
- **Domain**: `www.primeturf.co.za` — all four variants (http/https x bare/www) 301 to `https://www.primeturf.co.za/`

### 2.2 Wix Page Inventory (15 static pages)

| Page ID | Title | URL | Custom SEO | GitHub Equivalent |
|---------|-------|-----|------------|-------------------|
| bqvuq | Home | `/` | NO | `/` |
| fw9ji | About Us | `/about-us` | NO | none (new) |
| uay3e | Preparation | `/about-6` | NO | none (new) |
| cjh26 | Services (List) | `/services` | NO | none (new) |
| ggwix | **Poduct** Catalogue (TYPO) | `/services-5` | NO | none (new) |
| evnw7 | Get a Quote | `/quote` | NO | `/quote-calculator.html` |
| l7zij | Portfolio | `/gallery` | NO | none (new) |
| m80pg | Contact | `/contact` | NO | `/contact.html` |
| fuh2w | Blog | `/blog` | NO | `/blog/` |
| avhi7 | Artificial Grass Sandton | `/artificial-grass-sandton` | **YES** | `/page-sandton.html` |
| jhk27 | Artificial Grass Johannesburg | `/artificial-grass-johannesburg` | **YES** | `/artificial-grass-johannesburg.html` |
| kgiig | Artificial Grass Hyde Park | `/artificial-grass-hyde-park` | **YES** | `/page-hyde-park.html` |
| q46e6 | Artificial Grass Edenvale | `/artificial-grass-edenvale` | **YES** | `/page-edenvale.html` |
| ll72v | Accessibility Statement | `/accessibility-statement` | NO | none (Wix default) |
| uuztp | Privacy Policy | `/english-privacy-policy` | NO | `/privacy-policy.html` |

### 2.3 Blog Posts (live via Blog API)

- `/post/how-much-does-artificial-grass-cost-per-m-in-south-africa-2026` — live, indexed
- `/post/drought-proof-your-cape-town-garden-artificial-grass-and-water-restrictions` — live, indexed

### 2.4 Wix Sitemap (`pages-sitemap.xml`)

Currently lists 8 pages: `/`, `/contact`, `/gallery`, `/blog`, `/english-privacy-policy`, `/accessibility-statement`, `/about-6`, `/about-us`. None of the 13 missing suburb pages appear.

---

## 3. Google Index Evidence

### 3.1 Confirmed Indexed URLs (via web search, 2026-08-16)

| URL | Status | Impact |
|-----|--------|--------|
| `www.primeturf.co.za/` | INDEXED (Wix homepage) | OK but generic title |
| `www.primeturf.co.za/quote-calculator.html` | INDEXED → **404** | Users hit dead page |
| `www.primeturf.co.za/artificial-grass-cape-town.html` | INDEXED → **404** | Users hit dead page |
| `www.primeturf.co.za/artificial-grass-johannesburg.html` | INDEXED → **404** | Users hit dead page (Wix equivalent exists) |
| `www.primeturf.co.za/page-boksburg.html` | INDEXED → **404** | Users hit dead page |
| `www.primeturf.co.za/post/how-much-does-artificial-grass-cost-per-m-in-south-africa-2026` | INDEXED (live) | OK |

### 3.2 Google Search Console

GSC verification is active. Coverage exports (dated 2026-07-26) showed 22-25 pages "not indexed" — consistent with the content gap diagnosis. The GSC "not indexed" number is not a redirect problem; it's because those pages don't exist on Wix yet.

### 3.3 Ahrefs / Semrush

Ahrefs data unavailable (account plan limitation). Semrush not queried. External SEO tool data is a gap in this report.

---

## 4. Three-Way Reconciliation: GitHub → Google → Wix

### 4.1 Complete URL Migration Matrix

See `audit/url-migration-matrix.csv` for the full 29-row matrix.

**Summary of actions required:**

| Action | Count |
|--------|-------|
| RECREATE (missing pages) | 15 (13 suburbs + Cape Town city + terms of service) |
| REDIRECT (old .html → new) | 22+ |
| IMPROVE (existing pages missing SEO) | 11 |
| PROTECT (already migrated with SEO) | 4 (Sandton, Johannesburg, Hyde Park, Edenvale) |

### 4.2 Pages Already Successfully Migrated

These 4 suburb pages exist on Wix with custom SEO metadata:
1. `/artificial-grass-sandton` (avhi7) — from `/page-sandton.html`
2. `/artificial-grass-johannesburg` (jhk27) — from `/artificial-grass-johannesburg.html`
3. `/artificial-grass-hyde-park` (kgiig) — from `/page-hyde-park.html`
4. `/artificial-grass-edenvale` (q46e6) — from `/page-edenvale.html`

**Action**: Protect these. Add JSON-LD schema. Verify title/description match originals.

### 4.3 Pages Existing on Wix But Missing SEO

11 pages exist but have only default Wix titles/descriptions:
- Homepage (`/`) — "Home | Prime Turf SA"
- Contact (`/contact`)
- Blog (`/blog`)
- About Us (`/about-us`)
- Services (`/services`)
- Quote (`/quote`)
- Portfolio (`/gallery`)
- Preparation (`/about-6`)
- Product Catalogue (`/services-5`) — also has "Poduct" typo
- Accessibility Statement (`/accessibility-statement`)
- Privacy Policy (`/english-privacy-policy`)

**Action**: Set custom title, meta description, and OG tags via Wix Item SEO Tags API.

### 4.4 Completely Missing Pages (13 suburbs + 2 others)

These GitHub pages have no Wix equivalent yet:

| Missing Page | Old GitHub URL | Priority |
|-------------|---------------|----------|
| Artificial Grass Cape Town | `/artificial-grass-cape-town.html` | P0 |
| Artificial Grass Pretoria East | `/page-pretoria-east.html` | P0 |
| Artificial Grass Centurion | `/page-centurion.html` | P1 |
| Artificial Grass Steyn City | `/page-steyn-city.html` | P1 |
| Artificial Grass Midrand | `/page-midrand.html` | P1 |
| Artificial Grass Fourways | `/page-fourways.html` | P1 |
| Artificial Grass Bryanston | `/page-bryanston.html` | P1 |
| Artificial Grass Boksburg | `/page-boksburg.html` | P1 |
| Artificial Grass Bedfordview | `/page-bedfordview.html` | P2 |
| Artificial Grass Houghton | `/page-houghton.html` | P2 |
| Artificial Grass Mooikloof | `/page-mooikloof.html` | P2 |
| Artificial Grass Randburg | `/page-randburg.html` | P2 |
| Artificial Grass Roodepoort | `/page-roodepoort.html` | P2 |
| Artificial Grass Silver Lakes | `/page-silver-lakes.html` | P2 |
| Artificial Grass Waterfall City | `/page-waterfall-city.html` | P2 |
| Terms of Service | `/terms-of-service.html` | P3 |

Content for all pages is ready in `migration/content/*.md`.

**Action**: Create each page on Wix, port content from the `.md` files, set SEO metadata, then configure 301 redirects.

---

## 5. Redirect Map

### 5.1 Redirects Ready to Configure (page exists on Wix)

| Old URL | New Wix URL |
|---------|-------------|
| `/artificial-grass-johannesburg.html` | `/artificial-grass-johannesburg` |
| `/page-sandton.html` | `/artificial-grass-sandton` |
| `/page-edenvale.html` | `/artificial-grass-edenvale` |
| `/page-hyde-park.html` | `/artificial-grass-hyde-park` |
| `/quote-calculator.html` | `/quote` |
| `/contact.html` | `/contact` |
| `/blog/artificial-grass-cost-guide-south-africa.html` | `/post/how-much-does-artificial-grass-cost-per-m-in-south-africa-2026` |
| `/blog/drought-proof-garden-cape-town.html` | `/post/drought-proof-your-cape-town-garden-artificial-grass-and-water-restrictions` |
| `/privacy-policy.html` | `/english-privacy-policy` |
| `/primeturf-vs-easigrass.html` | `/` |

### 5.2 Redirects Blocked (page needs creation first)

13 suburb/city redirects + terms of service — see `audit/redirect-spec.csv`.

### 5.3 How to Configure

Wix URL Redirect Manager has no REST API. All redirects must be set manually:
**Site Settings → SEO Tools → URL Redirect Manager → Add New Redirect**

---

## 6. SEO Metadata Improvement Specs

### 6.1 Homepage (bqvuq)

| Field | Current | Recommended |
|-------|---------|-------------|
| Title | Home \| Prime Turf SA | PrimeTurf \| Premium Artificial Grass Solutions in South Africa |
| Description | (none) | Professional artificial grass installation across Gauteng & Cape Town. 6-year warranty, free quotes, premium 40mm turf. |
| Schema | (none) | LocalBusiness + HomeAndConstructionBusiness |

### 6.2 All Page Recommendations

See `audit/wix-seo-gaps.json` for the complete per-page specification with recommended titles, descriptions, and schema types.

---

## 7. Structured Data Plan

| Schema Type | Pages |
|-------------|-------|
| LocalBusiness + HomeAndConstructionBusiness | Homepage, Johannesburg, Cape Town |
| Service + LocalBusiness | All 17 suburb pages |
| FAQPage | Cape Town (3 Qs), Johannesburg (3 Qs) |
| BreadcrumbList | All city + suburb pages |
| Article + FAQPage | Blog posts (already have this on GitHub) |
| Blog | Blog index |

---

## 8. Internal Link Recovery

The GitHub site had a significant internal linking structure: homepage linked to all suburb pages, suburb pages cross-linked to neighbors, all pages linked to contact and quote. The current Wix site has minimal internal linking.

**Required link structure** (per page in `audit/missing-pages-spec.json`):
- Homepage → all suburb/city pages
- Each suburb → 3-4 neighboring suburbs + homepage + contact + quote
- Blog posts → relevant suburb pages
- Footer → terms, privacy, contact on all pages

---

## 9. Safety Classification

| Action | Safety | Method |
|--------|--------|--------|
| Generate audit reports (this document) | SAFE | Read-only analysis |
| Run automation scripts | SAFE | Read-only validation |
| Set SEO metadata via API | REVIEW | Wix BulkSetItemSeoTags — reversible |
| Create missing Wix pages | REVIEW | Wix Editor — new pages only |
| Configure 301 redirects | REVIEW | Wix dashboard — manual |
| Delete Wix pages | BLOCKED | Requires explicit approval |
| Modify existing Wix content | BLOCKED | Existing content protected |

---

## 10. Automation Tools

Four automation scripts are provided in `automation/`:

| Script | Purpose |
|--------|---------|
| `github-seo-extractor.py` | Parse all GitHub HTML files, extract SEO metadata to JSON |
| `sitemap-comparator.py` | Compare GitHub vs Wix sitemaps, identify gaps |
| `redirect-validator.py` | Test all 301 redirects work correctly |
| `seo-health-monitor.py` | Ongoing health check: page status, noindex, title regression |

---

## 11. Pending Decisions

1. **`/about-6` ("Preparation" page)** — Originally assumed to be a duplicate of `/about-us`. Actually titled "Preparation" on the live site. Needs human review before any merge/delete.
2. **Warranty duration** — GitHub site mentions both 6-year and 8-year warranties in different places. The live Wix site uses 6-year. Confirm which is correct before propagating to new pages.
3. **Site name double space** — "Prime Turf  SA" has two spaces. Should be fixed in Wix site settings.

---

## 12. Artifacts Generated

| File | Description |
|------|-------------|
| `audit/FORENSIC-MIGRATION-REPORT.md` | This report |
| `audit/url-migration-matrix.csv` | Complete 29-row GitHub → Google → Wix mapping |
| `audit/redirect-spec.csv` | All 22 redirect specifications with status |
| `audit/missing-pages-spec.json` | Reconstruction specs for 15 missing pages |
| `audit/wix-seo-gaps.json` | SEO gaps on all 15 existing Wix pages |
| `audit/github-seo-baseline.json` | Complete SEO metadata from all GitHub HTML files |
| `automation/github-seo-extractor.py` | GitHub metadata extraction script |
| `automation/sitemap-comparator.py` | Sitemap comparison script |
| `automation/redirect-validator.py` | Redirect validation script |
| `automation/seo-health-monitor.py` | Ongoing SEO health monitor |

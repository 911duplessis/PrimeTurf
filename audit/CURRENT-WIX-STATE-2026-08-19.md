# CURRENT WIX STATE — 19 AUGUST 2026

This section reflects the Wix site state as directly verified in the Wix Editor and via live-URL checks on 2026-08-19. It reconciles against, and supersedes where it conflicts with, the historical audit files in this directory (wix-seo-gaps.json, missing-pages-spec.json, redirect-spec.csv, url-migration-matrix.csv, SEO-PROGRESS-REPORT.md — all dated 2026-08-16/17). Those files are preserved unchanged and remain useful for historical context, migration content-file mapping, and SEO specs. Do not delete them. Where a conflict exists, THIS file is current ground truth for page existence/status as of 2026-08-19.

## What changed since the 2026-08-17 audit

- Total Wix pages: 17 (was 15). Two pages were added since the last audit: "Artificial Grass Cape Town" and "Artificial Grass Boksburg".
- Both new pages exist in the Wix Editor as DRAFT / UNPUBLISHED. Live checks on 2026-08-19 confirm both https://www.primeturf.co.za/artificial-grass-cape-town and https://www.primeturf.co.za/artificial-grass-boksburg return 404 on the live site — i.e. built but not yet published to production.
- Cape Town: SEO metadata VERIFIED against migration/content/artificial-grass-cape-town.md (slug, title tag, and meta description match spec). Body content VERIFIED correct against the same file.
- Boksburg: SEO metadata VERIFIED against migration/content/artificial-grass-boksburg.md (slug, title tag, and meta description match spec). Body content: the "Where We Install" and FAQ sections have been CORRECTED using migration/content/artificial-grass-boksburg.md (previously they contained Johannesburg copy, apparently duplicated from another page). The Hero section still displays shared/Cape-Town-style copy and was intentionally left untouched on explicit instruction, because a reproducible Wix Editor canvas-rendering anomaly made direct verification/editing of that section unreliable. Hero is classified REVIEW REQUIRED, not yet fixed.
- IMPORTANT CORRECTION: the historical "13 missing suburb pages" / "15 total missing" framing in the files below is now STALE with respect to Cape Town and Boksburg specifically. Do NOT recreate either page — both already exist in Wix. Do not treat them as missing in any future pass.

## Current definitive page matrix (locations/suburbs only; see url-migration-matrix.csv for full 27-URL GitHub mapping)

| Page | Wix Exists | URL | SEO | Body | Draft/Published | Google Evidence | Redirect | Action |
|---|---|---|---|---|---|---|---|---|
| Cape Town | YES | /artificial-grass-cape-town | VERIFIED | VERIFIED | DRAFT (unpublished, live=404) | Indexed 404 (artificial-grass-cape-town.html) | REVIEW (blocked on publish) | PUBLISH (needs separate approval) |
| Boksburg | YES | /artificial-grass-boksburg | VERIFIED | BODY REVIEW (Hero pending) | DRAFT (unpublished, live=404) | Indexed 404 (page-boksburg.html) | REVIEW (blocked on publish + hero decision) | RESOLVE HERO, then PUBLISH (needs separate approval) |
| Johannesburg | YES | /artificial-grass-johannesburg | VERIFIED | Not re-verified this pass (previously PROTECTED+ENHANCED) | Published | Indexed 404 (old .html) | READY | CONFIGURE REDIRECT |
| Sandton | YES | /artificial-grass-sandton | VERIFIED | Not re-verified this pass | Published | INFERRED | READY | CONFIGURE REDIRECT |
| Hyde Park | YES | /artificial-grass-hyde-park | VERIFIED | Not re-verified this pass | Published | INFERRED | READY | CONFIGURE REDIRECT |
| Edenvale | YES | /artificial-grass-edenvale | VERIFIED | Not re-verified this pass | Published | INFERRED | READY | CONFIGURE REDIRECT |
| Pretoria East | NO | /artificial-grass-pretoria-east | n/a | n/a | MISSING | INFERRED 404 | BLOCKED | CREATE (P0) |
| Centurion | NO | /artificial-grass-centurion | n/a | n/a | MISSING | INFERRED | BLOCKED | CREATE (P1) |
| Steyn City | NO | /artificial-grass-steyn-city | n/a | n/a | MISSING | INFERRED | BLOCKED | CREATE (P1) |
| Midrand | NO | /artificial-grass-midrand | n/a | n/a | MISSING | INFERRED | BLOCKED | CREATE (P1) |
| Fourways | NO | /artificial-grass-fourways | n/a | n/a | MISSING | INFERRED | BLOCKED | CREATE (P1) |
| Bryanston | NO | /artificial-grass-bryanston | n/a | n/a | MISSING | INFERRED | BLOCKED | CREATE (P1) |
| Bedfordview | NO | /artificial-grass-bedfordview | n/a | n/a | MISSING | INFERRED | BLOCKED | CREATE (P2) |
| Houghton | NO | /artificial-grass-houghton | n/a | n/a | MISSING | INFERRED | BLOCKED | CREATE (P2) |
| Mooikloof | NO | /artificial-grass-mooikloof | n/a | n/a | MISSING | INFERRED | BLOCKED | CREATE (P2) |
| Randburg | NO | /artificial-grass-randburg | n/a | n/a | MISSING | INFERRED | BLOCKED | CREATE (P2) |
| Roodepoort | NO | /artificial-grass-roodepoort | n/a | n/a | MISSING | INFERRED | BLOCKED | CREATE (P2) |
| Silver Lakes | NO | /artificial-grass-silver-lakes | n/a | n/a | MISSING | INFERRED | BLOCKED | CREATE (P2) |
| Waterfall City | NO | /artificial-grass-waterfall-city | n/a | n/a | MISSING | INFERRED | BLOCKED | CREATE (P2) |
| Terms of Service | NO | /terms-of-service | n/a | n/a | MISSING | UNKNOWN | BLOCKED | CREATE (P3, noindex) |

Non-location pages (Home, Get a Quote, Contact, About Us, Preparation, Product Catalogue, Portfolio, Privacy Policy, Accessibility Statement, Blog, Services) are unchanged from the 2026-08-17 audit and are not re-verified in this pass; see wix-seo-gaps.json for their individual status.

## True missing-page count

**14 pages** genuinely still require creation: 13 suburb pages (Pretoria East, Centurion, Steyn City, Midrand, Fourways, Bryanston, Bedfordview, Houghton, Mooikloof, Randburg, Roodepoort, Silver Lakes, Waterfall City) + 1 legal page (Terms of Service, P3/noindex).

This replaces the historical "13 missing suburb pages" / "15 total missing" figures. Those figures included Cape Town and Boksburg, which now exist in Wix (draft/unpublished) and must not be recreated.

## Google-indexed 404 reconciliation

| Old URL | Current Wix Destination | Status | Redirect Required? |
|---|---|---|---|
| /artificial-grass-cape-town.html | /artificial-grass-cape-town | Destination exists but UNPUBLISHED (404 live) | YES, once page is published |
| /artificial-grass-johannesburg.html | /artificial-grass-johannesburg | Destination exists and is PUBLISHED | YES, ready to configure now |
| /quote-calculator.html | /quote | Destination exists and is PUBLISHED | YES, ready to configure now |
| /page-boksburg.html | /artificial-grass-boksburg | Destination exists but UNPUBLISHED (404 live); Hero content still under review | YES, once page is published and Hero resolved |

## Redirect reconciliation (26 total mappings in redirect-spec.csv)

- READY (10, unchanged from prior audit): artificial-grass-johannesburg.html, page-sandton.html, page-edenvale.html, page-hyde-park.html, quote-calculator.html, contact.html, both blog post redirects, privacy-policy.html, primeturf-vs-easigrass.html→homepage.
- REVIEW (2, reclassified from BLOCKED — destination pages now exist in Wix but remain unpublished, so the redirect cannot be functionally activated yet, and Boksburg additionally needs its Hero resolved): artificial-grass-cape-town.html, page-boksburg.html.
- BLOCKED (14, unchanged — destination page does not exist yet): page-pretoria-east.html, page-centurion.html, page-steyn-city.html, page-midrand.html, page-fourways.html, page-bryanston.html, page-bedfordview.html, page-houghton.html, page-mooikloof.html, page-randburg.html, page-roodepoort.html, page-silver-lakes.html, page-waterfall-city.html, terms-of-service.html.
- OBSOLETE: none identified.

No redirects have been configured during this reconciliation pass, per instruction.

## Remaining location migration queue (pages genuinely requiring creation)

| Priority | Page | URL | Content File | SEO Spec |
|---|---|---|---|---|
| P0 | Pretoria East | /artificial-grass-pretoria-east | migration/content/artificial-grass-pretoria-east.md | missing-pages-spec.json |
| P1 | Centurion | /artificial-grass-centurion | migration/content/artificial-grass-centurion.md | missing-pages-spec.json |
| P1 | Steyn City | /artificial-grass-steyn-city | migration/content/artificial-grass-steyn-city.md | missing-pages-spec.json |
| P1 | Midrand | /artificial-grass-midrand | migration/content/artificial-grass-midrand.md | missing-pages-spec.json |
| P1 | Fourways | /artificial-grass-fourways | migration/content/artificial-grass-fourways.md | missing-pages-spec.json |
| P1 | Bryanston | /artificial-grass-bryanston | migration/content/artificial-grass-bryanston.md | missing-pages-spec.json |
| P2 | Bedfordview | /artificial-grass-bedfordview | migration/content/artificial-grass-bedfordview.md | missing-pages-spec.json |
| P2 | Houghton | /artificial-grass-houghton | migration/content/artificial-grass-houghton.md | missing-pages-spec.json |
| P2 | Mooikloof | /artificial-grass-mooikloof | migration/content/artificial-grass-mooikloof.md | missing-pages-spec.json |
| P2 | Randburg | /artificial-grass-randburg | migration/content/artificial-grass-randburg.md | missing-pages-spec.json |
| P2 | Roodepoort | /artificial-grass-roodepoort | migration/content/artificial-grass-roodepoort.md | missing-pages-spec.json |
| P2 | Silver Lakes | /artificial-grass-silver-lakes | migration/content/artificial-grass-silver-lakes.md | missing-pages-spec.json |
| P2 | Waterfall City | /artificial-grass-waterfall-city | migration/content/artificial-grass-waterfall-city.md | missing-pages-spec.json |
| P3 | Terms of Service | /terms-of-service | migration/content/terms-of-service.md | missing-pages-spec.json (noindex) |

## Boksburg Hero — REVIEW REQUIRED

The Boksburg page Hero section was NOT modified during this or the prior reconciliation pass. It currently displays shared/Cape-Town-style copy. It was deliberately left untouched per explicit instruction, because the Wix Editor exhibited a reproducible canvas-rendering anomaly when this page was selected (the canvas would display other pages' content regardless of Page-dropdown selection), making direct in-place editing risky without further human input. This is flagged for a human decision before any further action is taken on it.

## JSON-LD status

Unchanged: 0 of 17 pages have JSON-LD structured data. Deferred until URL architecture and page creation are stable, per standing instruction.

## Cross-reference note

The following historical files are retained unchanged below/alongside this one and remain the source for migration content-file paths and original SEO specs: wix-seo-gaps.json, missing-pages-spec.json, redirect-spec.csv, url-migration-matrix.csv, SEO-PROGRESS-REPORT.md. Future agents should treat THIS file as authoritative for current page existence/publish status, and those files as historical/spec reference only.

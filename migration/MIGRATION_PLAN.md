# PrimeTurf: GitHub → Wix Migration Plan

## The problem, in one paragraph

PrimeTurf's site moved from GitHub Pages (`www.primeturf.co.za`, served from this repo) to Wix. The repo's `CNAME` file was deleted on 2026-07-17, and the Wix site shows the custom domain as connected and published — so the domain has likely been pointing at the (nearly empty) Wix site for about 5 days already. Checking both sides directly: the old GitHub site had **29 real public pages** (homepage, contact, quote calculator, a comparison page, 2 city pages, 17 suburb pages, a 3-post blog with 2 published posts, privacy policy, terms of service). The live Wix site today has only **~7 pages** (homepage, `/about-us`, a stray duplicate `/about-6`, `/gallery`, `/english-privacy-policy`, `/accessibility-statement`, one portfolio item). None of the suburb/service pages exist yet. That's the real cause of the lost indexed pages — not a redirect gap, a content gap.

## What's in this `migration/` folder

- **`redirect-map.csv`** — every old public URL, its proposed new Wix URL, a `status`, a `priority` tier, and notes. 46 rows: 27 need a page built before they can redirect, 16 are internal/admin tooling explicitly excluded from rebuild, and 3 are special-cased (a duplicate quote tool, a WhatsApp utility page, and the privacy policy which already has a Wix home).
- **`content/*.md`** — one file per page that needs rebuilding, with the actual title/meta description/H1/body copy pulled straight from the old HTML. This is a porting job, not a copywriting job — use these files directly in the Wix Editor rather than writing new copy from scratch.

## Build order (highest-recovery-value first)

1. **Homepage parity** — `content/homepage.md`. Reconcile against the current Wix homepage; don't blind-overwrite. Resolve the two content flags in that file first (6-year vs 8-year warranty; `social@` vs `leon@` contact email) — pick the correct number/inbox before it goes live anywhere.
2. **Contact** — `content/contact.md`. Rebuild as a native Wix Forms form (already installed on the site) instead of re-wiring the old Web3Forms integration.
3. **Quote calculator** — `content/quote-calculator.md`. This is the one page here that isn't a copy-paste job — it's a 4-step interactive pricing wizard that needs Velo custom code (Velo is already enabled on the site). Budget real dev time. Once it's live, redirect `/quote/` straight to it rather than rebuilding a second calculator.
4. **2 city pages** — Cape Town, Johannesburg. These use a richer template than the suburb pages (water-stats band, FAQ schema, suburb-tag grid) — don't try to reuse the suburb-page template for these two.
5. **Top 5 suburbs** — Sandton, Centurion, Fourways, Bryanston, Pretoria East. Highest population/estate density, likely the biggest share of current lead volume.
6. **Remaining 12 suburbs** — Bedfordview, Boksburg, Edenvale, Houghton, Hyde Park, Midrand, Mooikloof, Randburg, Roodepoort, Silver Lakes, Steyn City, Waterfall City. All share one template — content is ready in `content/`, this is the most mechanical batch.
7. ~~Comparison page~~ — **Skipped by stakeholder decision (2026-07-22).** `primeturf-vs-easigrass.html` will not be republished; marked `do-not-publish` in the redirect map.
8. **Blog** — index + 2 real posts. Low urgency; only 2 posts exist despite the blog index displaying 4 more "coming soon" placeholders that were never built.
9. **Terms of service** — needed for legal completeness, but the old page had `noindex` set, so it's not part of the SEO recovery — no rush.

## Cleanup items on the Wix side (not content, but flagged)

- **Delete or merge `/about-6`** — looks like a leftover duplicate of `/about-us` from site setup. Two near-identical pages is a duplicate-content risk.
- **Re-verify Google Search Console domain ownership under Wix.** The old GSC verification was two static HTML stub files (`google2bbf502f984c3743.html`, `google57c2ac6f73edc94d.html`) that don't exist on Wix. Re-verify via Wix's Site Settings → SEO Tools (meta tag or DNS method) so Search Console access isn't silently broken.
- **`connection-network.html`, `vendor-signup.html`, `partner-agreement.html`, `tcn-dashboard.html`, `tcn-whatsapp-flow.html`** — a separate "The Connection Network" referral-partner side-project, not PrimeTurf's core turf-installation content. **Stakeholder decision (2026-07-22): excluded from this migration entirely.**

## Redirect setup (do this last, per page, as each goes live)

Wix's URL Redirect Manager (Site Settings → SEO Tools → URL Redirect Manager) **has no public REST API** — it's a dashboard-only feature, so this step is manual, not scriptable. As each page in `redirect-map.csv` goes from `needs-rebuild` to live:
1. Add the 301 in the Redirect Manager: old URL → new URL from the CSV.
2. Flip that row's `status` to `done` in `redirect-map.csv` and commit the change, so the CSV stays the single source of truth for what's left.
3. Resubmit the Wix sitemap to Google Search Console and use "Request Indexing" on that URL.

Leave GitHub Pages content in this repo untouched until the corresponding Wix page is live and redirected — it's the only remaining copy of the original copy during the rebuild window.

## Verification

- `curl -I https://www.primeturf.co.za/page-boksburg.html` (and the other old URLs) should return a **301** to the new URL once its redirect is configured — not a 404.
- Re-fetch `https://www.primeturf.co.za/pages-sitemap.xml` periodically and confirm new URLs appear as pages go live.
- Check Google Search Console's Pages report a few weeks after each redirect batch to confirm re-indexing, rather than assuming it worked.

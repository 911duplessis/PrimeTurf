# PrimeTurf: Full SEO & Indexing Report (2026-09-24)

**Scope:** the live Wix site (www.primeturf.co.za), repo `911duplessis/PrimeTurf` (the old GitHub site plus migration tooling), and repo `911duplessis/PrimeTurf-SA` (the static rebuild).

**Method:** live HTTP crawl of 19 sitemap URLs and 38 legacy URLs, a read-only Wix SEO Redirects API pull, on-page parsing of 47 + 63 repo HTML files, Semrush ZA domain rank, and web `site:` checks. Ahrefs isn't available on the current plan, and GSC figures come from the 2026-09-17 export summarised in `PrimeTurf-SA/github.md`.

---

## Bottom line

**The site is losing equity every day through 14 dead-end legacy URLs.** 5 are 301 redirects that land on unpublished pages (404), and 9 have no redirect at all (Wix returns 400). These are the old URLs that Google still ranks. Organic visibility is close to nothing: Semrush ZA shows **1 ranking keyword and 0 estimated traffic**.

**Highest-probability fix:** publish the 5 draft location pages that the redirects already point to. That turns 5 dead redirects into working ones with no new redirect work, and it needs owner approval under the Hard Constraints. Expected result: those URLs recover indexing in 2–6 weeks (about 70% probability, assuming the pages carry the content in `implementation/pages/*.md`).

---

## 1. Indexing status (live)

| Signal | Status |
|---|---|
| Canonical host | OK. `http://` and non-www both 301 to `https://www.` |
| robots.txt | OK. Wix default, no harmful disallows |
| Sitemap index | OK. 6 child sitemaps, **17 pages + 2 blog posts** (pages-sitemap lastmod 2026-09-20) |
| GSC verification | OK. Meta tag `dz5Y4c…` present on live HTML |
| GA4 `G-3Z5G37WW47` | **Not found in the server-rendered HTML** of any page. It may be injected at runtime, so check Wix Dashboard → Marketing Integrations |
| Published location pages | 6 (Johannesburg, Sandton, Hyde Park, Edenvale, Boksburg, Cape Town) |
| Draft (unpublished) location pages | ~13, and all of them return **404** |
| Search index freshness | **Stale.** `site:` results still show old `.html` URLs, old titles ("Luxury Artificial Grass Gauteng…") and `social@primeturf.co.za` in snippets |
| Brand SERP | GitHub repo pages (`github.com/911duplessis/PrimeTurf`, `-SA`) rank **above** primeturf.co.za for "PrimeTurf artificial grass Pretoria East" |

### GSC (2026-09-17 export, 90 days)
- Demand is mostly **Cape Town + cost**. "artificial grass cape town" has 120 impressions, and Gauteng queries are marginal.
- `/post/how-much-does-artificial-grass-cost-per-m-in-south-africa-2026` has 1,055 impressions, position 14.8 and 9 clicks, making it **the #1 asset**. It **has no meta description** (see §3).
- `/artificial-grass-cape-town.html` has 566 impressions and **0 clicks** at position 33.9.
- 13 clean-slug URLs are "Crawled – currently not indexed", 11 are 404s, and 4 are "Blocked due to other 4xx".

---

## 2. Redirect audit: 17 configured (CLAUDE.md says 10, which is out of date)

### 🔴 Redirects that land on 404 (5): critical
| From | To | Target status |
|---|---|---|
| /page-pretoria-east.html | /artificial-grass-pretoria-east | **404 (draft)** |
| /page-centurion.html | /artificial-grass-centurion | **404 (draft)** |
| /page-midrand.html | /artificial-grass-midrand | **404 (draft)** |
| /page-silver-lakes.html | /artificial-grass-silver-lakes | **404 (draft)** |
| /page-mooikloof.html | /artificial-grass-mooikloof | **404 (draft)** |

Pretoria East, Centurion and Midrand were priority-0.9 pages on the old site. Google is currently being told "moved permanently → gone".

**Fix A (recommended):** publish these 5 drafts, which needs owner approval.
**Fix B (stop-gap, if publishing slips more than 7 days):** repoint them to `/artificial-grass-johannesburg`. This is weak on relevance but stops the 404 signal. It needs owner approval.

### 🔴 Legacy URLs with no redirect: Wix returns 400 (10)
`/page-houghton.html`, `/page-fourways.html`, `/page-bryanston.html`, `/page-bedfordview.html`, `/page-randburg.html`, `/page-roodepoort.html`, `/page-steyn-city.html`, `/page-waterfall-city.html`, `/terms-of-service.html`, `/index.html`

Proposed map (needs owner approval):
| From | To |
|---|---|
| /index.html | / |
| /page-houghton.html, /page-bryanston.html, /page-fourways.html, /page-randburg.html, /page-steyn-city.html, /page-waterfall-city.html | /artificial-grass-sandton |
| /page-roodepoort.html | /artificial-grass-johannesburg |
| /page-bedfordview.html | /artificial-grass-edenvale |
| /terms-of-service.html | /terms-of-service (once that page exists) |

### 🟡 Other 404s picked up by crawl/GSC
- `/residential-artificial-grass-gauteng/` → 301 → 404
- `/blog/how-to-maintain-artificial-grass-south-africa/` → 301 → 404
- `/privacy-policy` → 404. Suggested redirect: `/english-privacy-policy`
- `/terms-of-service` → 404, because the page doesn't exist yet

### ✅ Working (12)
Cape Town, Johannesburg, Sandton, Hyde Park, Edenvale and Boksburg `.html` → clean slugs; `/quote-calculator.html` and `/quote/` → `/quote`; `/contact.html`; `/privacy-policy.html`; `/primeturf-vs-easigrass.html` → `/`; the 2 old blog `.html` URLs → `/post/…`. Trailing slashes are handled (`/artificial-grass-sandton/` → 301).

---

## 3. On-page audit: live Wix (19 URLs)

| Issue | Pages affected | Severity | Fix |
|---|---|---|---|
| **Sitewide H1 in header**: "Why PrimeTurf Gauteng & Cape Town?" is the first H1 on **every page** | 19/19 | 🔴 | Change that header text from Heading 1 to a paragraph or H2 in the master header. **One edit fixes all pages** |
| No page-specific H1 at all | /quote, /about-us, /services | 🔴 | Add an H1 (see the spec in `implementation/specs/seo-specification.md`) |
| Blog posts render the post title as H1 twice | 2 posts | 🟡 | Wix blog template issue. Low priority once the header H1 is fixed |
| **No meta description** | both blog posts (incl. the #1 cost post), /about-6, /english-privacy-policy, /accessibility-statement | 🔴 for the blog posts, 🟢 for the rest | Set via Wix SEO API or the Blog SEO panel |
| **No LocalBusiness / Breadcrumb / Service schema** on any page | 17/17 pages. Only Home has `WebSite`, and the blog posts have `BlogPosting` + `FAQPage` | 🔴 | Velo `masterPage.js` code has not been synced or published (CLAUDE.md task 11) |
| Homepage title is generic: "PrimeTurf \| Premium Artificial Grass Solutions" (no geo, no "installation") | / | 🟡 | → "Artificial Grass Installation Gauteng & Cape Town \| PrimeTurf" (54 chars) |
| Cape Town title isn't price-led even though it has 566 impressions and 0 clicks | /artificial-grass-cape-town | 🟡 | → "Artificial Grass Cape Town — Prices From R350/m² \| PrimeTurf" (already written in PrimeTurf-SA) |
| Weak title: "Preparation \| PrimeTurf SA" | /about-6 | 🟡 | → "Artificial Grass Site Preparation Process \| PrimeTurf" |
| Thin pages (~340 words) | /services, /quote | 🟢 | Merge /services with /services-5 or expand it |
| Images without alt text | 9–11 per page, mostly repeated header/footer images | 🟢 | Add alt text to the global header/footer images once |
| Title length > 60 | Hyde Park (72), blog post (76) | 🟢 | Trim |

---

## 4. Repo: `911duplessis/PrimeTurf`

| Finding | Severity | Detail |
|---|---|---|
| **GitHub Pages is still live** at `911duplessis.github.io/PrimeTurf/` | 🔴 | It serves the full old site plus internal tooling (`seo-dashboard.html` returns 200, along with `tcn-dashboard`, `partner-agreement`, reports). The repo `robots.txt` **has no effect** because robots rules are only read at the host root, and `911duplessis.github.io/robots.txt` returns 404. The old pages' canonicals point at `www.primeturf.co.za/*.html` URLs that now return 301 or 400, so Google may choose the github.io copy as canonical. |
| Stale contact and warranty data on that public copy | 🟡 | `social@primeturf.co.za` on 30+ pages; "8 Year" warranty on `primeturf-vs-easigrass.html` and `indexwix Temp.html` |
| Repo `sitemap.xml` lists the old `.html` URLs + easigrass page | 🟢 | Not served on the live domain, so no impact unless someone resubmits it |
| `google*.html` verification files | 🟢 | Dead on Wix. GSC now verifies through the meta tag, which is fine |

**Fix:** Settings → Pages → **Unpublish** for this repo. This is the highest-leverage zero-risk action in the report, and it takes 1 minute.

---

## 5. Repo: `911duplessis/PrimeTurf-SA` (static rebuild)

**Strengths:** the content is the best SEO material across all three sources. Every page has a unique title and description, a single H1, LocalBusiness + BreadcrumbList schema, and OG/Twitter tags. It includes a FAQPage cost page, price-led Cape Town and Western Cape titles, no fabricated reviews or ratings, and the email is corrected to leon@.

| Finding | Severity | Detail |
|---|---|---|
| **Also live on GitHub Pages** (`911duplessis.github.io/PrimeTurf-SA/`) | 🔴 | Same duplicate-content risk as §4, and worse, because this copy is richer than the live Wix pages. Its canonicals point at www URLs that mostly **don't exist** on Wix (see next row), and Google ignores canonicals that point to non-200 URLs. Unpublish Pages, or add `noindex` until cutover |
| **URL strategy contradicts the live site** | 🔴 | PrimeTurf-SA self-canonicalises `page-*.html` and lists 21 of them in its `sitemap.xml`. Wix currently **301s** those same URLs to clean slugs (or returns 400). Shipping this sitemap today would submit ~24 non-200 URLs. **Pick one architecture.** Recommendation: clean slugs, because Google has already seen the 301s and reversing them creates chains or loops |
| Canonical targets that exist nowhere | 🟡 | `/about` (About.dc), `/portfolio`, `/get-a-quote`, `/artificial-grass-cost` (.dc) vs `/post/…` (exported .html), `/artificial-grass-products`, `/before-and-after`, `/service-areas`, `/artificial-grass-western-cape`, `/artificial-turf-gauteng` |
| Duplicate page pairs | 🟡 | 26 `*.dc.html` sources + their lowercase exports; `quote.html` + `quote-calculator.html`; `gallery.html` vs `Portfolio.dc.html`. If both sets were served, each page would exist twice |
| **No analytics** | 🟡 | 0 of 37 exported pages load GA4 |
| Blog post title is 88 characters and its description is 47 | 🟢 | `post-drought-proof-cape-town.html` |
| Location titles are short (36–42 chars) | 🟢 | "Artificial Grass Sandton \| PrimeTurf" leaves ~20 characters unused (for example "— Installed From R200/m²") |

**Best use of this repo right now:** use it as the **content source** to port into Wix through the SEO API and the editor (titles, descriptions, the cost FAQ, the Cape Town price angle), not as a second live site.

---

## 6. Action plan (ranked by impact ÷ effort)

| # | Action | Where | Owner approval? | Est. impact | Confidence |
|---|---|---|---|---|---|
| 1 | Publish the 5 drafts that redirects point to (Pretoria East, Centurion, Midrand, Silver Lakes, Mooikloof), then the other ~8 drafts | Wix Editor | **Yes** | Stops the 404 leak on the highest-value legacy URLs | 70% |
| 2 | Unpublish GitHub Pages on **both** repos | GitHub Settings | No (repo setting) | Removes duplicate-index and brand-SERP risk | 90% |
| 3 | Change the header "Why PrimeTurf…" from H1 to H2/paragraph | Wix Editor (master) | Yes (minor edit) | Fixes the H1 on all 19 pages | 85% |
| 4 | Add meta descriptions to both blog posts (the cost post first) + retitle Home, Cape Town, /about-6 | Wix SEO API (I can do this) | Yes | CTR lift on the 1,055- and 566-impression pages | 60% |
| 5 | Create the 10 legacy redirects in §2 + `/privacy-policy` → `/english-privacy-policy` | Wix Redirects API (I can do this) | **Yes** | Recovers 4xx URLs in GSC | 80% |
| 6 | Sync the Velo JSON-LD (`wix dev` / publish in `my-site-4`) | Wix Velo | Yes | LocalBusiness/Service rich-result eligibility | 50% |
| 7 | Create /terms-of-service | Wix Editor | Yes | Closes 2 GSC 404s | 95% |
| 8 | Confirm GA4 is firing (Dashboard → Marketing Integrations) | Wix Dashboard | No | Measurement | n/a |
| 9 | Resubmit the sitemap + request indexing for the cost post, Cape Town and newly published pages | GSC | No | Speeds up the stale-index refresh | 70% |
| 10 | Decide the long-term URL architecture before any PrimeTurf-SA cutover (clean slugs recommended) | Decision | **Yes** | Avoids a second migration loss | n/a |

### Risk notes
- Doing #5 before #1 creates more redirect-to-404 chains. **Order matters: publish first, then redirect.**
- Repointing redirects to Johannesburg (Fix B) is a stop-gap. Google may treat irrelevant redirects as soft 404s (about 40% chance), so replace them as soon as the real pages are live.
- Recovery after these fixes is typically 4–12 weeks. The site has almost no authority (Semrush ZA: 1 keyword), so content on the Cape Town and cost cluster is where near-term clicks will come from.

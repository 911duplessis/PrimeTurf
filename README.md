# PrimeTurf

> Artificial Grass Supply & Installation — Gauteng, Cape Town, Pretoria  
> Live at [primeturf.co.za](https://primeturf.co.za/)

[![Website](https://img.shields.io/badge/Website-primeturf.co.za-2D6A4F?style=flat-square)](https://primeturf.co.za/)
[![GitHub Pages](https://img.shields.io/badge/Hosted-GitHub%20Pages-222?style=flat-square)](https://911duplessis.github.io/PrimeTurf/)

---

## Site Structure

| File | URL | Status |
|---|---|---|
| `index.html` | `/` | Live — homepage |
| `artificial-grass-johannesburg.html` | `/artificial-grass-johannesburg.html` | Live |
| `artificial-grass-cape-town.html` | `/artificial-grass-cape-town.html` | Live |
| `artificial-grass-pretoria.html` | `/artificial-grass-pretoria.html` | Live |
| `contact.html` | `/contact.html` | Live |
| `quote-calculator.html` | `/quote-calculator.html` | Live |
| `privacy-policy.html` | `/privacy-policy.html` | Live |
| `blog/index.html` | `/blog/` | Live |
| `blog/artificial-grass-cost-guide-south-africa.html` | `/blog/artificial-grass-cost-guide-south-africa.html` | Live |
| `blog/drought-proof-garden-cape-town.html` | `/blog/drought-proof-garden-cape-town.html` | Live |

---

## SEO

- `sitemap.xml` — 9 URLs, all pages indexed
- `robots.txt` — crawlable, sitemap declared
- JSON-LD schema on every page: `LocalBusiness`, `FAQPage`, `BreadcrumbList`
- GA4 property `G-3Z5G37WW47` with custom events (`whatsapp_click`, `phone_call_click`)
- Keyword architecture documented in `seo/phase-02-keyword-architecture.md`

**Priority terms targeted:**

| Cluster | Primary keyword | Page |
|---|---|---|
| Location — JHB | artificial grass Johannesburg | `/artificial-grass-johannesburg.html` |
| Location — CPT | artificial turf Cape Town | `/artificial-grass-cape-town.html` |
| Location — PTA | artificial grass Pretoria | `/artificial-grass-pretoria.html` |
| Problem-aware | drought-resistant lawn South Africa | blog |
| Product | artificial grass South Africa | homepage |

**Pages not yet built (planned):**
- `/commercial-artificial-turf-specification.html` — architect/developer spec-layer page (highest revenue potential per keyword architecture)
- `/water-saving-artificial-grass.html` — problem-aware landing page
- Suburb-level pages (Sandton, Midrand, Centurion, Waterfall City, etc.)

---

## Design

- `design/PrimeTurf_Layout_Analysis.md` — structural audit of `index.html` with recommendations
- `design/layout-map.html` — visual wireframe: current vs. proposed layout (open in browser)
- Palette: Emerald `#1A3A2A` / Gold `#B8922A` / Cream `#F5F2EC`
- Fonts: Cormorant Garamond (headings), Lato (body)

---

## Tech

- Pure HTML/CSS/JS — no framework, no build step
- Hosted on GitHub Pages with custom domain `primeturf.co.za`
- DNS: CNAME → `911duplessis.github.io`

---

## Related

- **Connection Network** (`911duplessis/Connection-Network`) — Next.js / Supabase referral platform, live at connection-network.vercel.app. Planned integration: quote leads from this site routed through Connection Network.

---

## Drafts / Archive

The following files are **not live** and not linked from any page. Do not publish without review:

| File | Notes |
|---|---|
| `index-54.html` | Advanced design draft — 12yr/8yr warranty conflict unresolved, ~44 broken nav links |
| `indexh-2.html` | Later iteration of above — hero badges corrected to 8yr, body copy still says 12yr |
| `index1.html`, `index2.html`, `index3.html` | Earlier design iterations |
| `indexh-2.html` | Side-developed redesign — good SEO copy depth, needs broken-link audit before use |
| `PrimeTurf_*.html` | Brand system and master blueprint files — reference only |
| `tcn-*.html`, `vendor-signup.html`, `partner-agreement.html`, `connection-network.html` | Superseded by live Connection Network Next.js app |

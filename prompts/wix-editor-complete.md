# PrimeTurf — Wix Editor Completion Prompt

You are helping complete the PrimeTurf Wix site (www.primeturf.co.za) in the Wix Classic Editor. All location pages have been created as drafts. Your job is to populate content, fix the hero layout, update the Service Areas page, and publish.

---

## CONSTRAINTS (NEVER violate)

- Warranty is **6 years** (NOT 8)
- Contact email: **leon@primeturf.co.za** (NOT social@)
- Phone: **076 804 8868**
- WhatsApp: **wa.me/27768048868**
- Do NOT invent Western Cape suburbs, branches, offices, projects, or testimonials
- Do NOT delete any existing pages or content
- Match the existing colour palette: Deep Forest / Harvest Gold / Warm Ivory / Cream

---

## TASK 1: Fix the Hero Section (ALL pages)

The current hero/heading section is too tall, static, and identical across every page. Fix it to be compact and page-specific.

### What's wrong:
- Hero strip takes up the entire viewport (100vh or close to it)
- Same layout/size on every page regardless of content
- Feels like a generic template, not a professional service site

### How to fix each hero:
1. **Reduce height**: The hero should be roughly 40–50% of viewport height, not 100%. In the strip settings, change from "Full Screen" or "Large" to a fixed pixel height (~400–500px desktop, auto on mobile) or choose the "Medium" strip size option.
2. **Remove excessive whitespace**: Tighten the padding above and below the heading text. Top padding ~60px, bottom ~40px is sufficient.
3. **Make it page-specific**: Each page hero MUST have:
   - A unique **H1 heading** (from the content files below)
   - A unique **subtitle/description** (1–2 sentences specific to that location)
   - A **CTA button** ("Request a Free Quote" → links to /contact)
4. **Professional styling**:
   - H1: Large but not overwhelming. ~36–44px on desktop.
   - Subtitle: Regular weight, ~16–18px, lighter colour than the heading
   - CTA button: Harvest Gold background, dark text, adequate padding
   - Consider adding a subtle overlay gradient if using a background image
5. **Mobile**: Hero should stack vertically, H1 drops to ~28px, full-width CTA button

### Hero content per page (H1 + subtitle):

**Pretoria East**
- H1: Luxury Artificial Turf in Pretoria East
- Subtitle: PrimeTurf delivers precision-installed artificial turf across Pretoria East's most prestigious addresses. From Waterkloof Ridge to Mooikloof Country Estate, we bring professional preparation, premium materials, and a refined finish to every installation.

**Moreleta Park**
- H1: Luxury Artificial Turf in Moreleta Park
- Subtitle: Premium artificial turf installation in Moreleta Park and surrounding suburbs. Residential gardens, townhouse complexes, and family outdoor spaces transformed with precision-installed synthetic turf. 6-year warranty.

**Silver Lakes**
- H1: Luxury Artificial Turf in Silver Lakes
- Subtitle: Premium artificial turf installation in Silver Lakes Golf Estate and surrounds. Estate-grade product, HOA submission support, and precision installation — backed by a 6-year warranty.

**Faerie Glen**
- H1: Luxury Artificial Turf in Faerie Glen
- Subtitle: Premium artificial turf installation in Faerie Glen. Family gardens, residential properties, and outdoor living spaces transformed with professionally installed synthetic turf. 6-year warranty.

**Waterkloof**
- H1: Luxury Artificial Turf in Waterkloof
- Subtitle: Premium artificial turf for Waterkloof and Waterkloof Ridge. Diplomatic quarter aesthetics, estate-grade materials, and precision installation — backed by a 6-year warranty.

**Mooikloof**
- H1: Luxury Artificial Turf in Mooikloof
- Subtitle: Premium artificial turf installation in Mooikloof Country Estate and surrounds. Large-scale estate installations with HOA submission support and precision finish. 6-year warranty.

**Lynnwood**
- H1: Luxury Artificial Turf in Lynnwood
- Subtitle: Premium artificial turf installation in Lynnwood, Pretoria. Residential gardens, townhouse developments, and commercial properties near Lynnwood Bridge. 6-year warranty.

**Garsfontein**
- H1: Luxury Artificial Turf in Garsfontein
- Subtitle: Premium artificial turf installation in Garsfontein, Pretoria East. Residential gardens, schools, and commercial properties professionally installed with a 6-year warranty.

**Centurion**
- H1: Luxury Artificial Turf in Centurion
- Subtitle: Premium artificial turf installation across Centurion. Residential, estate, and commercial installations along the Centurion corridor. 6-year warranty. Free consultation.

**Midrand**
- H1: Luxury Artificial Turf in Midrand
- Subtitle: Premium artificial turf installation in Midrand. Residential estates, commercial properties, and outdoor transformations between Johannesburg and Pretoria. 6-year warranty.

**Western Cape**
- H1: Luxury Artificial Turf in the Western Cape
- Subtitle: PrimeTurf brings the same premium artificial turf and professional installation standard trusted across Gauteng to the Western Cape. Water-wise, UV-stable, and engineered for the coastal climate.

**Cape Town** (already published — just fix the hero size)
- H1: Artificial Grass Cape Town
- Subtitle: Beat water restrictions permanently. PrimeTurf installs premium synthetic turf across Cape Town, Stellenbosch, and the Winelands — staying lush and green through every drought and restriction level.

**Service Areas**
- H1: PrimeTurf Service Areas
- Subtitle: Premium artificial turf installation across Gauteng and the Western Cape. Every installation receives the same quality materials, professional preparation, and precision finish — backed by a 6-year warranty.

**Boksburg** (already published — just fix the hero size)
- H1: Luxury Artificial Turf in Boksburg
- Keep existing subtitle

**Artificial Turf Gauteng** (bonus page — fix the hero size)
- Keep existing H1 and subtitle

---

## TASK 2: Add Body Content to Each Location Page

For each new location page, add these sections below the hero. Use the content from the files listed. If the page is already populated, skip it.

### Section order (top to bottom):

1. **Artificial Turf Solutions** (H2)
   - 6–7 service cards in a 2- or 3-column grid
   - Each card: H3 heading + paragraph
   - Services: Premium Artificial Turf, Residential Turf, Estate Installations, Commercial Turf, Putting Greens, Pet-Friendly Turf, Outdoor Transformation

2. **Why PrimeTurf** (H2)
   - 6 value-prop cards in a 2- or 3-column grid
   - Cards: Premium Materials, Professional Preparation, Precision Installation, Quality Workmanship, Refined Finish / Long-Term Value, Low-Maintenance Living

3. **Applications** (H2)
   - Bulleted list with bold lead text
   - 6 application types specific to the location

4. **Portfolio** (H2)
   - Short paragraph + link to /gallery
   - Use genuine PrimeTurf imagery only

5. **Service Area** (H2)
   - Paragraph listing suburbs covered
   - Links to 2–3 adjacent location pages
   - Link to /service-areas

6. **CTA Strip** (full-width)
   - Heading: "Request a Free Quote"
   - Text: "Get a no-obligation consultation and quotation for your [Location] property. We respond within 2 hours during business hours."
   - Button: "Request a Free Quote" → /contact
   - Phone: 076 804 8868
   - WhatsApp: wa.me/27768048868

### Content source files (in the GitHub repo at `PrimeTurf/implementation/pages/`):
- `pretoria-east.md` — Pretoria East
- `moreleta-park.md` — Moreleta Park
- `silver-lakes.md` — Silver Lakes
- `faerie-glen.md` — Faerie Glen
- `waterkloof.md` — Waterkloof
- `mooikloof.md` — Mooikloof
- `lynnwood.md` — Lynnwood
- `garsfontein.md` — Garsfontein
- `centurion-midrand.md` — Split between Centurion and Midrand pages
- `western-cape.md` — Western Cape
- `service-areas.md` — Service Areas landing

---

## TASK 3: Update the Service Areas Page

The Service Areas landing page needs Cape Town listed under Western Cape with suburb areas.

### Current structure to build:

**Gauteng** (H2)

Under Gauteng, list these areas with a short description and link:

- **Pretoria East** — Waterkloof, Silver Lakes, Mooikloof, Faerie Glen, and surrounding estates → /artificial-grass-pretoria-east
- **Moreleta Park** — Residential gardens, townhouse complexes → /artificial-grass-moreleta-park
- **Silver Lakes** — Silver Lakes Golf Estate and surrounds → /artificial-grass-silver-lakes
- **Faerie Glen** — Family gardens, residential properties → /artificial-grass-faerie-glen
- **Waterkloof** — Waterkloof and Waterkloof Ridge → /artificial-grass-waterkloof
- **Mooikloof** — Mooikloof Country Estate and surrounds → /artificial-grass-mooikloof
- **Lynnwood** — Residential and commercial properties → /artificial-grass-lynnwood
- **Garsfontein** — Residential, schools, commercial → /artificial-grass-garsfontein
- **Centurion** — Residential and commercial across Centurion → /artificial-grass-centurion
- **Midrand** — Estates and commercial between JHB and PTA → /artificial-grass-midrand
- **Johannesburg** — Greater Johannesburg installations → /artificial-grass-johannesburg
- **Sandton** — Residential and commercial → /artificial-grass-sandton
- **Hyde Park** — Premium residential → /artificial-grass-hyde-park
- **Edenvale** — Residential and commercial → /artificial-grass-edenvale
- **Boksburg** — East Rand installations → /artificial-grass-boksburg

**Western Cape** (H2)

Under Western Cape, list these:

- **Cape Town** — Cape Town CBD, Southern Suburbs, Atlantic Seaboard, Northern Suburbs. Constantia, Bishopscourt, Camps Bay, Clifton, Hout Bay, Tokai, Newlands, Rondebosch, Bloubergstrand, Durbanville, Bellville. → /artificial-grass-cape-town
- **Stellenbosch & Winelands** — Stellenbosch, Franschhoek, Paarl, Somerset West → /artificial-grass-cape-town (same page)
- **Western Cape Regional** — Broader Western Cape coverage → /artificial-grass-western-cape

---

## TASK 4: Navigation

Restructure the navigation menu:

1. Rename **"Locations"** to **"Service Areas"**
2. Ideal dropdown structure:
   - **Gauteng** (header/folder)
     - Pretoria East
     - Johannesburg
     - Sandton
     - Centurion
     - Midrand
     - View All → /service-areas
   - **Western Cape** (header/folder)
     - Cape Town
     - Western Cape
3. If grouped dropdowns aren't possible in Classic Editor, keep a flat list but add "— All Service Areas" at the top linking to /service-areas
4. Rename the **"/about-6"** page label to **"Site Preparation"** in the menu

Full main menu order: Home, About, Services, Portfolio, Site Preparation, Service Areas, Blog, Contact

---

## TASK 5: Footer Links

Add these links in the site footer for SEO crawl depth:

**Service Areas:**
- Pretoria East
- Johannesburg
- Sandton
- Cape Town
- Centurion & Midrand
- Western Cape
- All Service Areas → /service-areas

**Quick Links:**
- Services → /services
- Portfolio → /gallery
- Request a Quote → /contact
- Blog → /blog

---

## TASK 6: Publish All Pages

After all content is added:

1. Preview each page on desktop AND mobile
2. Verify:
   - [ ] Hero is compact (not full-screen) with correct H1
   - [ ] All body sections present with correct content
   - [ ] CTA buttons link to /contact
   - [ ] Phone number: 076 804 8868
   - [ ] WhatsApp links work (wa.me/27768048868)
   - [ ] Internal links to adjacent location pages work
   - [ ] Mobile layout stacks correctly
3. Publish the site (this publishes all draft pages)

---

## TASK 7: Quick Fixes on Existing Published Pages

These published pages need their hero section reduced too:
- /artificial-grass-johannesburg
- /artificial-grass-sandton
- /artificial-grass-hyde-park
- /artificial-grass-edenvale
- /artificial-grass-boksburg
- /artificial-grass-cape-town

For each: reduce hero strip height, tighten padding, keep existing content.

---

## Internal Linking Reference

Every location page should link to:
- Homepage (/)
- Services (/services)
- Portfolio (/gallery)
- Contact (/contact)
- Service Areas (/service-areas)
- 2–3 geographically adjacent pages:

| Page | Link to these neighbours |
|------|--------------------------|
| Pretoria East | Silver Lakes, Waterkloof, Mooikloof |
| Moreleta Park | Faerie Glen, Garsfontein, Pretoria East |
| Silver Lakes | Pretoria East, Mooikloof |
| Faerie Glen | Moreleta Park, Lynnwood, Garsfontein |
| Waterkloof | Pretoria East, Lynnwood |
| Mooikloof | Silver Lakes, Pretoria East |
| Lynnwood | Faerie Glen, Garsfontein, Waterkloof |
| Garsfontein | Moreleta Park, Faerie Glen, Lynnwood |
| Centurion | Midrand, Pretoria East |
| Midrand | Centurion, Johannesburg, Sandton |
| Cape Town | Western Cape |
| Western Cape | Cape Town |
| Boksburg | Edenvale, Johannesburg |

---

## Checklist (verify before publishing)

- [ ] All ~13 draft pages have content populated
- [ ] Every hero is compact (40–50% viewport, not full-screen)
- [ ] Every page has a unique H1 and subtitle
- [ ] Service Areas page lists all locations with links
- [ ] Cape Town suburbs listed under Western Cape on Service Areas page
- [ ] Navigation renamed to "Service Areas" with dropdown
- [ ] Footer links added
- [ ] CTA buttons work on every page
- [ ] Mobile layout verified on all new pages
- [ ] /about-6 labelled as "Site Preparation" in menu

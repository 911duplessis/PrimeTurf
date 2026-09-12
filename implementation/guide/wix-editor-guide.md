# Wix Classic Editor — Implementation Guide

This guide covers creating the 10 new location pages + 1 Service Areas landing page in the Wix Classic Editor. Since Classic Editor has no page-creation API, each page must be built manually.

---

## Build Order

| Priority | Page | Content File |
|----------|------|-------------|
| 1 | Service Areas Landing | `pages/service-areas.md` |
| 2 | Pretoria East | `pages/pretoria-east.md` |
| 3 | Centurion & Midrand | `pages/centurion-midrand.md` |
| 4 | Silver Lakes | `pages/silver-lakes.md` |
| 5 | Waterkloof | `pages/waterkloof.md` |
| 6 | Mooikloof | `pages/mooikloof.md` |
| 7 | Moreleta Park | `pages/moreleta-park.md` |
| 8 | Faerie Glen | `pages/faerie-glen.md` |
| 9 | Lynnwood | `pages/lynnwood.md` |
| 10 | Garsfontein | `pages/garsfontein.md` |
| 11 | Western Cape | `pages/western-cape.md` |

---

## Step 1: Create a Location Page Template

Build one location page first (Pretoria East recommended), then duplicate it for the remaining 9 suburbs. This ensures consistent layout and styling.

### In the Wix Editor:

1. Click **Site Menu** (left panel) → **Add Page**
2. Choose **Blank Page**
3. Name it using the SEO slug (e.g., "Artificial Grass Pretoria East")
4. Set the URL slug in Page Settings (see Step 3)

### Page Layout (Top to Bottom):

Each location page follows this structure. Use the content from the corresponding `pages/*.md` file.

| Section | Element Type | Notes |
|---------|-------------|-------|
| **Hero** | Strip with heading + paragraph + button | H1 heading (one per page). CTA button links to /contact. Match existing hero styling. |
| **Artificial Turf Solutions** | H2 heading + repeating cards/columns | 6-7 service cards. Each has H3 heading + paragraph. Use 2 or 3 columns per row. |
| **Why PrimeTurf** | H2 heading + repeating cards/columns | 6 value-prop cards. Each has H3 heading + paragraph. Icon or checkmark optional. |
| **Applications** | H2 heading + bulleted list or cards | Bulleted list with bold lead text. |
| **Portfolio** | H2 heading + paragraph | Text referencing portfolio. Link to /portfolio. |
| **Service Area** | H2 heading + paragraph | Lists suburbs served. Links to adjacent location pages. |
| **CTA** | Strip with heading + paragraph + button(s) | CTA button to /contact. Phone and WhatsApp links. |

### Styling Rules:

- **Headings**: Match existing Wix site heading fonts and sizes
- **Colours**: Deep Forest / Harvest Gold / Warm Ivory / Cream — match existing palette
- **Buttons**: Match existing CTA button style (likely Harvest Gold background, dark text)
- **Spacing**: Generous padding between sections. Single column on mobile.
- **Images**: Use only genuine PrimeTurf portfolio images. Set alt text per the convention: `[Description] - PrimeTurf artificial turf installation in [Location]`

---

## Step 2: Duplicate for Remaining Pages

After the first page is complete:

1. In **Site Menu**, right-click the completed page → **Duplicate**
2. Rename the duplicate
3. Update all content from the corresponding `pages/*.md` file
4. Update the URL slug (Step 3)
5. Update internal links in the Service Area section to point to adjacent locations
6. Repeat for all 10 pages

---

## Step 3: Set Page URL Slugs

For each page:

1. Click **Site Menu** → hover over page name → click **⋯** → **Page Settings**
2. Go to **SEO (Google)** tab
3. Under **What's the page's URL?**, set the custom slug:

| Page | Slug |
|------|------|
| Pretoria East | `artificial-grass-pretoria-east` |
| Moreleta Park | `artificial-grass-moreleta-park` |
| Silver Lakes | `artificial-grass-silver-lakes` |
| Faerie Glen | `artificial-grass-faerie-glen` |
| Waterkloof | `artificial-grass-waterkloof` |
| Mooikloof | `artificial-grass-mooikloof` |
| Lynnwood | `artificial-grass-lynnwood` |
| Garsfontein | `artificial-grass-garsfontein` |
| Centurion & Midrand | `artificial-grass-centurion-midrand` |
| Western Cape | `artificial-grass-western-cape` |
| Service Areas | `service-areas` |

---

## Step 4: Configure SEO Per Page

For each page in **Page Settings → SEO (Google)**:

1. **SEO Title**: Copy from `specs/seo-specification.md`
2. **Meta Description**: Copy from `specs/seo-specification.md`
3. **Advanced SEO** → Add canonical URL tag pointing to `https://www.primeturf.co.za/[slug]`

Alternatively, SEO tags can be set via the Wix Item SEO Tags API after pages are created (see "API Operations" below).

---

## Step 5: Set Up Navigation

### Primary Menu:

1. Click **Site Menu** (left panel)
2. Arrange pages in this order: Home, About, Services, Portfolio, Preparation, Service Areas, Blog, Contact
3. Rename the `/about-6` page label to "Preparation" (or "Site Preparation")

### Service Areas Dropdown:

1. In **Site Menu**, click **⋯** next to "Service Areas" → **Add Submenu**
2. Create a "Gauteng" folder containing:
   - Pretoria East
   - Silver Lakes
   - Mooikloof
   - Centurion & Midrand
   - Johannesburg (existing)
   - View All → links to /service-areas
3. Create a "Western Cape" folder containing:
   - Western Cape

Note: Not all location pages need to be in the dropdown. The Service Areas landing page provides full discoverability. Keep the dropdown clean.

---

## Step 6: Update Contact Form

### If using Wix Forms:

1. Go to the **/contact** page in the Editor
2. Click the existing form → **Manage Form**
3. Add/edit fields to match the spec in `specs/contact-form.md`:
   - First Name (text, required)
   - Last Name (text, required)
   - Email (email, required)
   - WhatsApp / Phone (phone, required)
   - Suburb / Area (text, required)
   - Service Interest (dropdown, required — 10 options from spec)
   - Approximate Project Size (dropdown, optional — 6 options from spec)
   - Message (textarea, optional)
4. Set the submit confirmation message:
   > "Thank you for your enquiry. PrimeTurf will respond within 2 hours during business hours. For immediate assistance, WhatsApp us at 076 804 8868."
5. **Verify notification email**: Go to Wix Dashboard → Settings → Notifications → Form Submissions → Confirm email is set to `leon@primeturf.co.za`

---

## Step 7: Footer Links

Add links to major location pages in the site footer for SEO crawl depth:

- Pretoria East
- Silver Lakes
- Waterkloof
- Centurion & Midrand
- Johannesburg
- Western Cape
- Service Areas (landing)

---

## Step 8: Publish

1. Preview all new pages on desktop and mobile
2. Check all internal links work correctly
3. Verify CTA buttons link to /contact
4. Publish the site

---

## API Operations (Post-Page Creation)

These operations can be executed via the Wix REST API once pages exist:

### SEO Tags (via Item SEO Tags API)

SEO titles, meta descriptions, and canonical URLs can also be set programmatically. See `specs/seo-specification.md` for values.

### 301 Redirects (via Wix SEO Redirects API)

Once new pages are live, configure redirects from old GitHub URLs to new Wix pages. Key redirects:

| Old URL | New URL |
|---------|---------|
| /artificial-grass-pretoria-east.html | /artificial-grass-pretoria-east |
| /artificial-turf-pretoria.html | /artificial-grass-pretoria-east |
| /artificial-grass-centurion.html | /artificial-grass-centurion-midrand |
| /artificial-grass-silver-lakes.html | /artificial-grass-silver-lakes |
| /artificial-grass-mooikloof.html | /artificial-grass-mooikloof |
| /artificial-grass-cape-town.html | /artificial-grass-western-cape |
| /primeturf-vs-easigrass.html | / |

Full redirect map: `audit/redirect-spec.csv`

### JSON-LD Structured Data

Add via Wix Velo (code injection) or Wix Dashboard → Settings → Custom Code:

- **LocalBusiness** schema on homepage
- **Service** schema on service pages
- **BreadcrumbList** on all pages
- See `audit/missing-pages-spec.json` for schema definitions

# Wix Page Builder -- PrimeTurf Location Pages

You are helping create a missing location page on the PrimeTurf Wix site. This is a forensic SEO migration recovery task -- we are restoring pages that existed on the original GitHub Pages site.

## Before You Start

1. Which page are you creating? Pick from the build order below.
2. The content source file is at `migration/content/artificial-grass-{suburb}.md` in the GitHub repo.
3. The SEO specs are in `audit/missing-pages-spec.json` under the matching `wix_slug`.

## Build Order (by priority)

| Batch | Pages |
|-------|-------|
| 1 (P0) | Cape Town |
| 2 (P1) | Pretoria East, Centurion, Fourways, Bryanston, Boksburg |
| 3 (P2) | Steyn City, Midrand, Bedfordview, Houghton, Mooikloof, Randburg, Roodepoort, Silver Lakes, Waterfall City |
| 4 (P3) | Terms of Service |

## Step-by-Step Process

### 1. Create the Page
- In Wix Editor, go to Pages > Add Page > Blank Page
- Set the page name to match the content file's H1 (e.g., "Artificial Grass Boksburg")

### 2. Set the URL Slug
- Go to Page Settings > SEO (Google)
- Set the URL slug exactly as specified (e.g., `artificial-grass-boksburg`)
- The canonical URL should be `https://www.primeturf.co.za/artificial-grass-{suburb}`

### 3. Add Page Content
Copy content sections from the `.md` file in order:
- **Hero section**: Eyebrow text (suburb list), H1 heading, description paragraph, CTA buttons
- **Body content**: H2/H3 sections with paragraph text
- **What We Install**: Checklist items
- **The PrimeTurf Standard**: Warranty and service guarantees
- **Areas Covered**: Suburb pill/tag list
- **Why Choose PrimeTurf**: Value proposition paragraph
- **FAQ section**: Question + answer pairs (H3 for questions)
- **CTA band**: "Get a Free Quote" with WhatsApp and phone buttons

### 4. Set SEO Metadata
In Page Settings > SEO (Google):
- **Title tag**: Copy from `missing-pages-spec.json` > `seo.title`
- **Meta description**: Copy from `missing-pages-spec.json` > `seo.meta_description`
- **OG title**: Same as title tag (Wix auto-inherits)

### 5. Add Internal Links
From `missing-pages-spec.json` > `internal_links.to`:
- Link "Get a Quote" buttons to `/quote`
- Link "Contact" references to `/contact`
- Link to related suburb pages where specified
- Link to homepage

### 6. CTA Details
- WhatsApp link: `https://wa.me/27768048868?text=Hi%20PrimeTurf%2C%20I%20need%20a%20quote%20in%20{Suburb}.`
- Phone: `tel:+27768048868` (display as 076 804 8868)
- Email: `leon@primeturf.co.za`

### 7. Save (DO NOT Publish)
- Save the page as draft
- DO NOT publish without owner approval

## Constraints

- DO NOT edit any existing pages
- DO NOT change the site navigation
- DO NOT publish without explicit owner approval
- Use **6-year warranty** everywhere (not 8-year)
- Use **leon@primeturf.co.za** for contact email (not social@)
- Phone: **076 804 8868**
- Match the content from the `.md` file accurately -- do not improvise content

## SEO Checklist (verify before saving)

- [ ] URL slug matches spec exactly
- [ ] Custom title tag set (from spec)
- [ ] Meta description set (from spec)
- [ ] H1 matches spec
- [ ] All content sections from .md file present
- [ ] WhatsApp CTA links correctly with suburb name
- [ ] Phone number correct (076 804 8868)
- [ ] Internal links added (homepage, /quote, /contact, related suburbs)
- [ ] Page saved as draft (NOT published)

## Reference: Existing Pages to Match Style

Look at these existing Wix pages for visual style reference:
- `/artificial-grass-sandton` (suburb page)
- `/artificial-grass-johannesburg` (city page with richer content)
- `/artificial-grass-hyde-park` (suburb page)
- `/artificial-grass-edenvale` (suburb page)

## After Creating Each Page

Report back with:
1. Page name and URL slug
2. Confirmation all checklist items are done
3. Any content sections that couldn't be added (e.g., images not available)

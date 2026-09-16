# Create 8 Missing Location Pages in Wix Editor

**Why this is manual**: Wix Classic Editor has no API for creating pages. These must be added through the Wix Editor UI. Once created, all SEO metadata, structured data, and 301 redirects will be configured automatically via API.

**Estimated time**: ~15 minutes total (2 min per page)

## Quick Steps (repeat for each page)

1. Open the Wix Editor: https://editor.wix.com
2. Click **Add Page** (+ icon in the Pages panel on the left)
3. Select **Blank Page**
4. Name the page (use the Page Name from the table below)
5. Click the page name in the Pages panel → **SEO (Google)** → Set the **URL slug** (from table below)
6. **Save** and move to the next page

## Pages to Create

| # | Page Name | URL Slug | Old URL |
|---|-----------|----------|---------|
| 1 | Artificial Grass Fourways | artificial-grass-fourways | /page-fourways.html |
| 2 | Artificial Grass Bryanston | artificial-grass-bryanston | /page-bryanston.html |
| 3 | Artificial Grass Steyn City | artificial-grass-steyn-city | /page-steyn-city.html |
| 4 | Artificial Grass Bedfordview | artificial-grass-bedfordview | /page-bedfordview.html |
| 5 | Artificial Grass Houghton | artificial-grass-houghton | /page-houghton.html |
| 6 | Artificial Grass Randburg | artificial-grass-randburg | /page-randburg.html |
| 7 | Artificial Grass Waterfall City | artificial-grass-waterfall-city | /page-waterfall-city.html |
| 8 | Artificial Grass Roodepoort | artificial-grass-roodepoort | /page-roodepoort.html |

## Menu Setup

After creating all 8 pages:

1. In the Editor, click the **Menu** element in the header
2. Click **Manage Menu**
3. Create a submenu called **Service Areas** (or **Locations**)
4. Drag all location pages under the Service Areas submenu
5. Organize them alphabetically or by region:
   - **Gauteng**: Bedfordview, Boksburg, Bryanston, Centurion, Edenvale, Fourways, Houghton, Hyde Park, Johannesburg, Midrand, Mooikloof, Pretoria East, Randburg, Roodepoort, Sandton, Silver Lakes, Steyn City, Waterfall City
   - **Western Cape**: Cape Town

## After Creating Pages

Once the pages exist and the site is published:
1. Tell Claude the pages are created
2. Claude will automatically:
   - Configure SEO title, description, and OG tags for all 8 pages
   - Set up the 8 blocked 301 redirects
   - Deploy Velo structured data (JSON-LD schemas)
   - Update the Service Areas hub page links

## Header / Site Name

The site display name has been updated from "Prime Turf  SA" to "PrimeTurf" via the Site Properties API. This change will reflect across the site after the next publish.

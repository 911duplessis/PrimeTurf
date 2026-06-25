# Phase 06 — CRO, Retargeting & Conversion Architecture for primeturf.co.za
> Conversion Rate Optimisation | POPIA-Compliant | Mobile-First | Generated 2026-06-11

---

## 1. Quote Calculator

A fully interactive calculator widget is live at `/quote-calculator.html`.

**Inputs:** Surface type · Area (m²) · Location · Grade
**Output:** Estimated ZAR price range · Estimated installation time · Personalised CTA

See `/quote-calculator.html` for the complete implementation.

---

## 2. WhatsApp Integration

The floating WhatsApp button is already implemented on all pages with pre-populated messages contextualised per page:

| Page | Pre-populated Message |
|---|---|
| Homepage | "Hi PrimeTurf, I would like to enquire about your services." |
| JHB page | "Hi PrimeTurf, I need artificial grass installed in Johannesburg and would like a free quote." |
| CPT page | "Hi PrimeTurf, I need artificial grass installed in Cape Town and would like a free quote." |
| Cost guide | "Hi PrimeTurf, I read your cost guide and would like a free site consultation and quote." |
| Cape Town guide | "Hi PrimeTurf, I read your Cape Town guide and would like a free site consultation." |
| Quote calculator | "Hi PrimeTurf, I used your quote calculator and would like to confirm my estimate and book a site visit." |

**WhatsApp Business API checklist** (to complete manually):
- [ ] Apply for WhatsApp Business API at business.whatsapp.com
- [ ] Verify business (requires business registration document + utility bill)
- [ ] Set up automated welcome message (responds within 60 seconds when unavailable)
- [ ] Create quick reply templates for: "Quote Request", "Book Site Visit", "Request Spec Sheet"
- [ ] Set business hours in WhatsApp Business profile
- [ ] Add business description, address, website, and category

---

## 3. GA4 Conversion Tracking

### GA4 Event Tracking Code

Add to `index.html`, `contact.html`, and both city pages. Already present as a `<script>` block; add the event calls below alongside the existing gtag config.

**WhatsApp button click:**
```html
<script>
document.querySelectorAll('a[href*="wa.me"], a[href*="whatsapp.com"]').forEach(function(el) {
  el.addEventListener('click', function() {
    gtag('event', 'whatsapp_click', {
      'event_category': 'engagement',
      'event_label': document.title,
      'value': 1
    });
  });
});
</script>
```

**Phone number click:**
```html
<script>
document.querySelectorAll('a[href^="tel:"]').forEach(function(el) {
  el.addEventListener('click', function() {
    gtag('event', 'phone_click', {
      'event_category': 'engagement',
      'event_label': el.href,
      'value': 1
    });
  });
});
</script>
```

**Contact form submission (Web3Forms):**
Add to the success handler in `contact.html` after `data.success` check:
```javascript
gtag('event', 'form_submit', {
  'event_category': 'conversion',
  'event_label': 'contact_form',
  'value': 5
});
```

**Quote calculator submission:**
```javascript
// Add inside the showResult() function in quote-calculator.html
gtag('event', 'quote_calculated', {
  'event_category': 'conversion',
  'event_label': surfaceType + '_' + grade,
  'surface_type': surfaceType,
  'grade': grade,
  'area_m2': area,
  'location': location,
  'value': 3
});
```

### Google Tag Manager trigger configurations (alternative to direct gtag)

If migrating to GTM later:

| Trigger Name | Trigger Type | Condition |
|---|---|---|
| WhatsApp Click | Click — Just Links | Link URL contains "wa.me" OR "whatsapp.com" |
| Phone Click | Click — Just Links | Link URL starts with "tel:" |
| Contact Form Submit | Form Submission | Form ID = "contact-form" |
| Quote Calculated | Custom Event | Event name = "quote_calculated" |
| Blog Scroll 75% | Scroll Depth | Vertical scroll threshold = 75% |

**GA4 Conversions to mark:**
- `form_submit` → mark as conversion
- `whatsapp_click` → mark as conversion
- `quote_calculated` → mark as conversion (micro-conversion)

---

## 4. Retargeting Audience Segments

### Meta Ads Audiences

| # | Audience Name | Description | Inclusion Rules | Exclusion Rules | Ad Creative Angle | Budget % |
|---|---|---|---|---|---|---|
| 1 | Homepage Visitors — No Quote | Visited site, didn't convert | Visited primeturf.co.za in last 30 days | Completed contact form OR clicked WhatsApp | "Still thinking about it? Book a free site visit." + before/after image | 30% |
| 2 | Blog Readers | High-intent research phase | Visited /blog/ or specific blog posts in last 14 days | Completed contact form | "You read the guide — now get the exact quote for your property." | 20% |
| 3 | City Page Visitors — JHB | Johannesburg-intent visitors | Visited artificial-grass-johannesburg.html | Completed contact form | Sandton/Midrand transformation image + "Johannesburg quote in 24 hours" | 20% |
| 4 | City Page Visitors — CPT | Cape Town-intent visitors | Visited artificial-grass-cape-town.html | Completed contact form | Water restriction angle + "Never worry about restrictions again" | 20% |
| 5 | Calculator Users — No Booking | Used quote calculator but didn't WhatsApp/call | Triggered quote_calculated event in last 7 days | WhatsApp click or form submit | "Your estimate is ready. Book the site visit to confirm your price." | 10% |

### Google Ads Audiences (RLSA — Remarketing Lists for Search Ads)

Use these to increase bids when past visitors search relevant keywords:

| Audience | Bid Adjustment | Search Keywords to Boost |
|---|---|---|
| All site visitors (30 days) | +30% | artificial grass [city], synthetic turf [city] |
| Blog readers | +50% | artificial grass cost, how much artificial grass |
| City page visitors — JHB | +75% | artificial grass johannesburg, artificial turf sandton |
| City page visitors — CPT | +75% | artificial grass cape town, fake lawn cape town |
| Calculator users | +100% | artificial grass installation, quote artificial grass |

---

## 5. A/B Test Roadmap (Months 4–5)

| # | Hypothesis | Variant A (Control) | Variant B (Test) | Success Metric | Min. Sample Size | Priority |
|---|---|---|---|---|---|---|
| 1 | A WhatsApp CTA is a lower-friction conversion than a form CTA on mobile | Primary CTA = "Complete Our Form" | Primary CTA = "WhatsApp for Free Quote" | WhatsApp click rate on mobile | 300 mobile sessions per variant | High |
| 2 | Showing a price range increases quote request rate by qualifying intent | Hero has no price reference | Hero adds "From R350/m² installed" chip | Contact form submissions + WhatsApp clicks | 500 sessions per variant | High |
| 3 | A sticky bottom CTA bar on mobile increases conversion | No sticky mobile CTA | Fixed bottom bar: WhatsApp button + "Free Quote" text | Mobile WhatsApp click rate | 400 mobile sessions per variant | Medium |
| 4 | Blog posts with an in-article calculator link increase bounce-to-conversion rate | Blog CTAs link to contact form | Blog CTAs link to quote calculator | Click-through rate on article CTAs | 600 blog sessions per variant | Medium |

**A/B testing tool recommendation**: Google Optimize sunset in 2023 — use **VWO** (cheapest paid option for SA market) or **Optimizely** for statistical significance. For a lower-cost approach, manually alternate CTAs by week and compare GA4 event data.

---

## 6. POPIA Compliance Checklist

PrimeTurf collects: name, email, phone, message (via Web3Forms contact form) and phone/WhatsApp identifiers (via click events).

| Requirement | Status | Action |
|---|---|---|
| Privacy policy page | ❌ Missing | Create `/privacy-policy.html` — see template below |
| Cookie consent notice | ❌ Missing | Add lightweight cookie notice (GA4 sets cookies) |
| Data processor agreement with Web3Forms | ❓ Check | Review Web3Forms POPI/GDPR terms |
| Form disclosure | ❌ Missing | Add "Your details are used only to respond to your enquiry" note to contact form |
| Opt-out mechanism | ❌ Missing | Add "Reply STOP to unsubscribe" to any WhatsApp follow-up messages |

**Minimal privacy policy content required:**
```
PrimeTurf collects contact information (name, email, phone number) submitted via 
our enquiry form. This information is used solely to respond to your enquiry and 
schedule site consultations. We do not sell, share, or rent your data to third parties.
You may request deletion of your data at any time by emailing [email] or calling 
076 804 8868. Website analytics are collected via Google Analytics 4 (GA4) — 
you may opt out at any time using the Google Analytics Opt-out Add-on.
```

---

*All 6 SEO phases are now complete. Live assets deployed:*

| Phase | Deliverable | Status |
|---|---|---|
| 01 | HTTP→HTTPS, canonical tags, sitemap, robots.txt | ✅ Live |
| 02 | Keyword architecture (5 clusters, landing page map, priority matrix) | ✅ Documented |
| 03 | JSON-LD schemas (4 types), city landing pages (JHB + CPT), meta tags | ✅ Live |
| 04 | Blog infrastructure, 2 published articles, editorial calendar, GBP posts | ✅ Live |
| 05 | 20 SA directories, 8 associations, 10 media targets, 3 outreach templates | ✅ Documented |
| 06 | Quote calculator, GA4 tracking code, 5 retargeting audiences, 4 A/B tests, POPIA checklist | ✅ Calculator live + this doc |

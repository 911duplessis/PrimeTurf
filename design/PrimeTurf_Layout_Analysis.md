# PrimeTurf — Homepage Layout Map & Structural Recommendations

> Scope: **layout/structure only** — no copy or content changes proposed. All references point at `index.html` (the live site's single page) as it stands on the `claude/primeturf-layout-redesign-AHyWQ` branch.

---

## 1. Current Layout Map (top → bottom)

The site is a single-page layout with smooth-scroll anchor navigation, fixed navbar, and a consistent emerald/gold/cream design system defined via CSS custom properties (`index.html:18-41`). Sections run in this order:

| # | Section | Structure | Key CSS |
|---|---------|-----------|---------|
| — | **Navbar** (fixed, 92px) | logo + 5 links + phone + CTA + hamburger | `:158-221` |
| 1 | **Hero** `#home` | Centered single-column stack: watermark "PT" → decorative rings → logo mark → eyebrow line → micro-label ("Professional Outdoor Excellence") → H1 → italic subtitle → 8 application chips → 3 CTAs (WhatsApp / phone / Explore) → 4 proof points separated by gold dividers → scroll hint | `:247-430`, markup `:1212-1278` |
| 2 | **Positioning Band** | 4-column horizontal row of short trust statements | `:435-460`, markup `:1281-1296` |
| 3 | **Brand Statement** | 2-col grid `1fr 1fr`: **left** = label + headline + 5-item feature grid + 2 CTAs; **right** = trust copy + 2 warranty blocks (8-yr / 24-month) + tagline | `:462-579`, markup `:1299-1362` |
| 4 | **Services** `#services` | Section intro (centered) + `.services-layout` container styled as a **3-column bordered grid** containing a single consolidated panel ("01 — Luxury Turf Installation") | `:584-632`, markup `:1365-1394` |
| 5 | **Estates Marquee** | Horizontal auto-scrolling band of 12 estate names (looped ×2) | `:637-666`, markup `:1397-1424` |
| 6 | **Gallery** `#gallery` | Section intro + draggable before/after comparison slider + 5-item asymmetric photo mosaic (3-col grid, 2 items spanning 2 columns) | `:668-777`, markup `:1426-1513` |
| 7 | **Process** | Section intro + 4-step horizontal row (numbered circles connected by a horizontal rule) | `:783-810`, markup `:1515-1545` |
| 8 | **Gauteng Region Band** | 2-col grid `1fr 1fr`: **left** = label + headline + body copy + CTA; **right** = stylised SVG province map with estate dots | `:815-880`, markup `:1547-1598` |
| 9 | **CTA Band** (dark emerald) | Centered headline + sub + 2 CTAs — the page's one strong contrast moment | `:935-961`, markup `:1600-1610` |
| 10 | **Contact** `#contact` | 2-col grid `1fr 1.4fr`: **left** = contact info + WhatsApp link; **right** = enquiry form (Web3Forms) | `:963-1040`, markup `:1612-1704` |
| 11 | **Footer** | 4-col grid `2fr 1fr 1fr 1fr` (brand / nav / services / contact) + tagline band + bottom bar | `:1037-1093`, markup `:1706-1770` |
| — | **Floating elements** | WhatsApp bubble (bottom-right) + "back to top" (appears after 400px scroll) | `:1098-1137` |

**Responsive behaviour** (`:1142-1168`): all 2-column grids collapse to `1fr` at ≤768px, the services/testimonial/footer grids step down in stages, and the process steps go from 4 → 2 → (visually) stacked. This collapse system is solid and consistent — worth preserving as-is.

---

## 2. Structural Issues Found

### 2.1 Services section: grid/content mismatch (most visible structural bug)
`index.html:585-588` defines:
```css
.services-layout { display:grid; grid-template-columns:repeat(3,1fr); border:1px solid var(--border-gold); }
```
…but the markup (`:1374-1393`) contains **only one** `.service-panel`. The result: a gold-bordered container spanning the full 1140px content width, with the single panel occupying the **left third** and roughly **two-thirds of the box rendering as empty bordered space**. This reads as an unfinished layout rather than an intentional design — almost certainly a leftover from an earlier 3-service version that was consolidated into one panel without updating the container grid.

### 2.2 Dead "Testimonials" navigation links *(flagged only — not actioned per your instruction)*
`#testimonials` is linked from three places:
- Desktop nav — `index.html:1186`
- Mobile nav — `index.html:1206`
- Footer nav — `index.html:1729`

A complete, already-styled testimonial system exists in CSS (`.testi-grid`, `.testi-card`, `.testi-mark`, `.testi-stars`, etc. — `index.html:885-930`), but **no `<section id="testimonials">` exists in the page markup**. Clicking any of these three links currently does nothing (no matching anchor to scroll to). This is a pure structural gap — the styling investment is already there, just not wired to a section. Documented here for you to action later (either remove the three links, or repopulate the section using the existing `.testi-grid` system).

### 2.3 Hero is a long, fully-centered vertical stack
The hero (`#home`, `:1212-1278`) stacks **eight** distinct focal elements in a single centered column: watermark → decorative rings → logo mark (400px) → eyebrow rule+label → micro-label → H1 → italic subtitle → 8 application chips → 3 CTA buttons → 4 proof points (with dividers) → scroll hint. Each element competes for attention in sequence, and the cumulative vertical space pushes the next section further down the scroll — a visitor has to process a long chain before reaching any proof-of-work content.

### 2.4 Repetitive two-column rhythm down the page
Three separate bands all use a near-identical **copy-block-left / visual-or-info-block-right** layout at similar visual weight:
- Brand Statement — `1fr 1fr` (`:475`)
- Gauteng Region Band — `1fr 1fr` (`:824`)
- Contact — `1fr 1.4fr` (`:964`)

Stacked across the page in sequence (with only the Services/Estates/Gallery/Process bands between the first two), this creates a "sameness" in the scroll rhythm — the eye keeps landing on the same left-text/right-visual pattern rather than experiencing intentional variation.

### 2.5 Estates Marquee placement breaks the proof-of-work flow
The scrolling estates band (`:1397-1424`) currently sits **between Services and Gallery** — i.e., between "what we offer" and "see our transformations." It doesn't reinforce either neighbour. Thematically, it's about *where* PrimeTurf operates, which is exactly the subject of the **Gauteng Region Band** later in the page (`:1547-1598`) — placing them adjacently would let the marquee visually reinforce the region message instead of interrupting the services→gallery proof sequence.

---

## 3. What's Already Working Well (preserve these)
- **Consistent design-token system** — all colour, type, spacing decisions flow from the `:root` custom properties (`:18-41`), making future structural edits low-risk.
- **Typography hierarchy** — `.t-display` / `.t-heading` / `.t-label` / `.t-body` give the page a coherent voice.
- **Responsive collapse rules** are already in place and sensible (`:1142-1168`).
- **Scroll-reveal system** (`.reveal` / `.reveal-d1-3`, `:113-117`) gives the page gentle motion without being distracting.
- **Before/after slider** and **asymmetric gallery mosaic** are the strongest visual moments on the page — they should anchor the proof section, which they currently do.
- **Floating WhatsApp + back-to-top** are well-placed conversion aids that don't crowd the layout.

---

## 4. Proposed Structural Improvements (no copy changes — reuses existing classes, tokens, and text)

### 4.1 Fix the Services section imbalance
Replace the `repeat(3,1fr)` bordered grid with a layout sized to match the single consolidated panel — for example, an **asymmetric split** where the existing service copy/list occupies one side and a **supporting value strip** built from content that already exists elsewhere on the page (e.g., the warranty figures from the Brand Statement, or the 5 feature icons) occupies the other. This makes the bordered container read as an intentional, balanced composition instead of a 3-slot grid with 2 empty slots.

### 4.2 Alternate the two-column sections to build rhythm
Keep Brand Statement as **copy-left / visual-right** (as-is), but **mirror the Gauteng Region Band to visual-left / copy-right** (a simple grid-order flip — `order` or column-order swap, no markup rewrite needed). Contact stays info/form. The result is a left → right → left visual cadence as the user scrolls, instead of three same-direction stacks.

### 4.3 Shorten and regroup the hero stack
- Combine the eyebrow rule+label and the micro-label ("Professional Outdoor Excellence") into a **single line** rather than two stacked label rows.
- Tighten the vertical spacing scale between logo → headline → subtitle → chip row → CTA row → proof strip (the current `margin-bottom` values in `:341-408` step down from 52px → 24px → 16px → 48px → 72px in a way that could be made more consistent and compact).
- On large viewports, consider an **asymmetric hero** (visual anchor on one side, headline/CTA block on the other) rather than a fully centered stack — this shortens the scroll distance to the first content section while keeping every existing line of copy intact.

### 4.4 Relocate the Estates Marquee
Move the marquee block (`:1397-1424`) to sit **directly beneath the Gauteng Region Band** (after `:1598`, before the CTA Band), where "areas we serve" is the active theme — turning it into a visual reinforcement of that message rather than an interruption between Services and Gallery.

### 4.5 Leave the Testimonials links as documented above
No action taken in this pass per your instruction — see §2.2 for the two remediation paths available when you're ready.

---

## 5. Companion Visual Map
A side-by-side wireframe comparing the **current flow** to the **proposed flow** is provided at [`design/layout-map.html`](./layout-map.html) — open it directly in a browser to see the section stack, column structures, and the repositioning/rhythm changes represented as labelled blocks in the site's own palette.

---
title: Artificial Grass Quote Calculator South Africa | PrimeTurf
meta_description: Get an instant artificial grass price estimate for your South African property. Select surface type, area, location, and grade — free site consultation to confirm.
old_url: /quote-calculator.html
proposed_new_url: /quote-calculator
priority: 2-top-suburb
---

## Hero

**Instant Estimate**

# Artificial Grass Quote Calculator

Get an indicative price range for your project in under 60 seconds. A free site consultation confirms your exact, fixed price.

## Interactive Calculator — 4-Step Wizard

**Step 1 — What surface are you installing on?**
- 🌿 Garden Lawn — Front or back garden, typically over soil
- 💧 Pool Surround — Around pool, paving, or entertainment area
- 🏢 Rooftop / Balcony — Concrete rooftop deck or apartment balcony
- ⚽ Sports / Play — Putting green, cricket, multi-sport, or play area

**Step 2 — Approximate area (m²)**
Numeric input, 10–5000 range. Hint: "Not sure? Measure length × width. Include only the turf area, not paving or beds."

**Step 3 — Where is the property?**
- 🏙️ Gauteng — Johannesburg, Pretoria, Sandton, Midrand, Centurion
- 🌊 Cape Town / Winelands — Cape Town, Stellenbosch, Somerset West, Franschhoek

**Step 4 — What grade suits your project?**
- ✅ Standard — 25–30mm · Pet runs, play areas, balconies · Best value
- ⭐ Premium — 30–37mm · Residential lawns, pool surrounds · Most popular
- 💎 Luxury — 37–45mm · Estates, show homes, architect spec

CTA: "Calculate My Estimate →" — produces a price-range result panel.

**Implementation note:** this is a real interactive tool, not static copy — the pricing formula lives in the inline JS in this file (search for `function calculate()` in `quote-calculator.html`) and a near-duplicate simpler version exists at `/quote/` (shares `quote/engine/calc.js`, `state.js`, `form.js`, etc.). Rebuilding this on Wix requires **Velo custom code** (the Wix site already has Velo enabled) to reproduce the step wizard and pricing logic — this is not a copy-paste page, budget dev time for it. Recommend consolidating to ONE quote tool on Wix rather than porting both `/quote-calculator.html` and `/quote/` separately, since they serve the same purpose.

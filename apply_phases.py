#!/usr/bin/env python3
"""
apply_phases.py — Applies all 15 phases of changes to index.html
"""

import re

INPUT_FILE = '/home/user/PrimeTurf/index.html'
OUTPUT_FILE = '/home/user/PrimeTurf/index.html'

changes_log = []

def log(msg):
    changes_log.append(msg)
    print(f"  [OK] {msg}")

print("Reading file...")
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
print(f"Loaded {len(lines)} lines, {len(content)} bytes")

# ─────────────────────────────────────────────
# PHASE 1 — Logo replacements (line-index based)
# ─────────────────────────────────────────────
print("\nPhase 1: Logo replacements...")

def replace_src_on_line(lines_list, zero_based_idx, new_src):
    """Replace src="data:image/jpeg;base64,..." on a specific line index."""
    line = lines_list[zero_based_idx]
    new_line = re.sub(r'src="data:image/jpeg;base64,[^"]+"', f'src="{new_src}"', line)
    if new_line != line:
        lines_list[zero_based_idx] = new_line
        return True
    return False

if replace_src_on_line(lines, 1064, '/assets/logo/pt-monogram.png'):
    log("Line 1065 (idx 1064): nav logo src replaced with /assets/logo/pt-monogram.png")
else:
    print("  [WARN] Line 1065 nav logo: no change made")

if replace_src_on_line(lines, 1108, '/assets/logo/pt-monogram.png'):
    log("Line 1109 (idx 1108): hero logo src replaced with /assets/logo/pt-monogram.png")
else:
    print("  [WARN] Line 1109 hero logo: no change made")

if replace_src_on_line(lines, 1690, '/assets/logo/pt-monogram-gold.jpg'):
    log("Line 1691 (idx 1690): footer logo src replaced with /assets/logo/pt-monogram-gold.jpg")
else:
    print("  [WARN] Line 1691 footer logo: no change made")

content = '\n'.join(lines)

# ─────────────────────────────────────────────
# PHASE 2 — CSS variable colour corrections
# ─────────────────────────────────────────────
print("\nPhase 2: CSS variable colour corrections...")

css_replacements = [
    ('--emerald:      #1B4332;', '--emerald:      #1A3A2A;'),
    ('--emerald-mid:  #204D30;', '--emerald-mid:  #1C4A2A;'),
    ('--emerald-deep: #0F2B1E;', '--emerald-deep: #1A3A2A;'),
    ('--parchment:    #FAF6ED;', '--parchment:    #FFFFFF;'),
    ('--parchment-mid:#F5EFE0;', '--parchment-mid:#F5F2EC;'),
    ('--cream:        #F7F0DF;', '--cream:        #FFFFFF;'),
    ('--cream-mid:    #F0E8CE;', '--cream-mid:    #F5F2EC;'),
]

for old, new in css_replacements:
    if old in content:
        content = content.replace(old, new, 1)
        log(f"CSS: '{old.strip()}' → '{new.strip()}'")
    else:
        print(f"  [WARN] CSS var not found: {old.strip()}")

# ─────────────────────────────────────────────
# PHASE 3 — Remove ALL emoji occurrences
# ─────────────────────────────────────────────
print("\nPhase 3: Remove emoji occurrences...")

# Delete entire lines that are just emoji div/span elements
line_deletions = [
    '<div class="pos-icon">🏛</div>',
    '<div class="pos-icon">🌿</div>',
    '<div class="pos-icon">🏆</div>',
    '<div class="pos-icon">💎</div>',
    '<div class="svc-icon">🌱</div>',
    '<div class="svc-icon">💧</div>',
    '<div class="svc-icon">✨</div>',
]

for pattern in line_deletions:
    # Remove line (including newline) from content
    # Match the line with optional leading whitespace
    regex = r'[ \t]*' + re.escape(pattern) + r'\n?'
    new_content = re.sub(regex, '', content)
    if new_content != content:
        content = new_content
        log(f"Deleted line containing: {pattern}")
    else:
        print(f"  [WARN] Could not find: {pattern}")

# Delete span cd-icon elements (keep surrounding content on same line)
span_deletions = [
    '<span class="cd-icon">📞</span>',
    '<span class="cd-icon">📧</span>',
    '<span class="cd-icon">🌐</span>',
    '<span class="cd-icon">📍</span>',
]

for pattern in span_deletions:
    if pattern in content:
        content = content.replace(pattern, '')
        log(f"Deleted span: {pattern}")
    else:
        print(f"  [WARN] Span not found: {pattern}")

# Remove ☎ prefix from phone links
if '☎ 076 804 8868' in content:
    content = content.replace('☎ 076 804 8868', '076 804 8868')
    log("Removed ☎ prefix from phone number links")
else:
    print("  [WARN] ☎ phone pattern not found")

# Remove emoji from footer social links
footer_social_replacements = [
    ('>📸</a>', '></a>'),
    ('>👍</a>', '></a>'),
    ('>💬</a>', '></a>'),
]

for old, new in footer_social_replacements:
    if old in content:
        content = content.replace(old, new)
        log(f"Footer social: '{old}' → '{new}'")
    else:
        print(f"  [WARN] Footer social not found: {old}")

# Remove decorative SVG star ornaments (multiline)
ornament_pattern = re.compile(
    r'[ \t]*<div class="ornament">\s*'
    r'<div class="ornament-line"></div>\s*'
    r'<svg[^>]*viewBox="0 0 18 18"[^>]*>\s*'
    r'<path[^/]*/>\s*'
    r'</svg>\s*'
    r'<div class="ornament-line rev"></div>\s*'
    r'</div>\n?',
    re.DOTALL
)

ornament_matches = ornament_pattern.findall(content)
count_ornaments = len(ornament_matches)
content = ornament_pattern.sub('', content)
log(f"Removed {count_ornaments} decorative SVG star ornament block(s)")

# ─────────────────────────────────────────────
# PHASE 4 — Hero heading + list
# ─────────────────────────────────────────────
print("\nPhase 4: Hero heading + list...")

old_hero_block = '''    <h1 class="hero-title">
      Prime<span class="hero-title-italic">Turf</span>
    </h1>
    <p class="hero-subtitle">Crafting the Future of Greenspace Design</p>
    <p class="hero-subtext">Serving the Entire Gauteng Region — From Estate Lawns to Architectural Landscapes.</p>'''

new_hero_block = '''    <h1 class="hero-title">Premium Artificial Grass Solutions</h1>
    <ul class="hero-list">
      <li>Estate Lawns</li>
      <li>School Grounds</li>
      <li>Play Areas</li>
      <li>Restaurant Play Areas</li>
      <li>Residential</li>
      <li>Commercial</li>
      <li>Patios</li>
      <li>Putting Greens</li>
    </ul>'''

if old_hero_block in content:
    content = content.replace(old_hero_block, new_hero_block)
    log("Hero heading replaced with 'Premium Artificial Grass Solutions' + list")
else:
    print("  [WARN] Hero block not found — trying flexible match")
    # Try flexible whitespace match
    flex_pattern = re.compile(
        r'<h1 class="hero-title">\s*Prime<span class="hero-title-italic">Turf</span>\s*</h1>\s*'
        r'<p class="hero-subtitle">Crafting the Future of Greenspace Design</p>\s*'
        r'<p class="hero-subtext">Serving the Entire Gauteng Region[^<]*</p>',
        re.DOTALL
    )
    if flex_pattern.search(content):
        content = flex_pattern.sub(new_hero_block, content)
        log("Hero heading replaced (flexible match)")
    else:
        print("  [ERROR] Hero block not found at all!")

# ─────────────────────────────────────────────
# PHASE 5 — Signature Turf / Brand Statement section
# ─────────────────────────────────────────────
print("\nPhase 5: Brand statement section...")

# Replace h2 in brand statement
old_bs_h2 = 'Where <em>Design</em> Meets the<br>Engineering of Nature'
new_bs_h2 = 'Premium Artificial Grass For Every Space'
if old_bs_h2 in content:
    content = content.replace(old_bs_h2, new_bs_h2)
    log(f"Brand statement h2 replaced")
else:
    print("  [WARN] Brand statement h2 not found")

# Replace the TWO <p> tags inside <div class="bs-body">
old_bs_body = '''        <p>PrimeTurf is Gauteng's architectural authority in luxury artificial grass. We don't simply install turf — we engineer outdoor environments that reflect the standard of the properties we serve.</p>
        <p>Led personally by Managing Director Leon van Eeden, every project undergoes a rigorous design process: site analysis, drainage engineering, premium material specification, and flawless execution. The result is a living surface that remains immaculate for a decade and beyond.</p>'''

new_bs_body = '''        <p><strong>Benefits:</strong></p>
        <ul class="bs-list">
          <li>Low Maintenance</li>
          <li>Water Saving</li>
          <li>Pet Friendly</li>
          <li>Non-Toxic</li>
          <li>Built To Last</li>
        </ul>'''

if old_bs_body in content:
    content = content.replace(old_bs_body, new_bs_body)
    log("Brand statement body paragraphs replaced with Benefits list")
else:
    print("  [WARN] Brand statement body not found — trying flexible match")
    flex_bs = re.compile(
        r"<p>PrimeTurf is Gauteng's architectural authority.*?</p>\s*"
        r"<p>Led personally by Managing Director.*?</p>",
        re.DOTALL
    )
    if flex_bs.search(content):
        content = flex_bs.sub(new_bs_body, content)
        log("Brand statement body replaced (flexible match)")
    else:
        print("  [ERROR] Brand statement body not found at all!")

# ─────────────────────────────────────────────
# PHASE 6 — Wording replacements (global)
# ─────────────────────────────────────────────
print("\nPhase 6: Global wording replacements...")

# Architectural → Professional (case-preserving)
count_arch = content.count('Architectural')
count_arch_low = content.count('architectural')

content = content.replace('Architectural', 'Professional')
content = content.replace('architectural', 'professional')

log(f"Replaced {count_arch} instances of 'Architectural' → 'Professional'")
log(f"Replaced {count_arch_low} instances of 'architectural' → 'professional'")

# Proof text replacement
old_proof = "Trusted by Gauteng's Most Distinguished Properties"
new_proof = "6 Year Manufacturer's Warranty"
if old_proof in content:
    content = content.replace(old_proof, new_proof)
    log(f"Proof text: '{old_proof}' → '{new_proof}'")
else:
    print(f"  [WARN] Proof text not found: {old_proof}")

# ─────────────────────────────────────────────
# PHASE 7 — Quality section credential updates
# ─────────────────────────────────────────────
print("\nPhase 7: Credential item updates...")

# Update credential 01 span text
# After phase 6, strong will now read "Professional Turf Systems"
old_cred01_span = 'Precision-planned installations for luxury residential estates, complexes, and commercial developments across Gauteng.'
new_cred01_span = 'We install signature turf systems for estates, schools, complexes, restaurants, and commercial properties across Gauteng. Led by our expert team, every installation meets the highest standard.'

if old_cred01_span in content:
    content = content.replace(old_cred01_span, new_cred01_span)
    log("Credential 01 span text updated")
else:
    print(f"  [WARN] Credential 01 span not found")

# Add credential 05 after credential 04 block
# Find the closing </div> of credential 04
old_cred04_end = '''          <strong class="credential-text">Legacy of Excellence</strong>
            <span class="credential-text">Decades of outdoor craftsmanship, refined into a singular standard that defines the PrimeTurf reputation across the province.</span>
          </div>
        </div>
      </div>
    </div>'''

new_cred04_end = '''          <strong class="credential-text">Legacy of Excellence</strong>
            <span class="credential-text">Decades of outdoor craftsmanship, refined into a singular standard that defines the PrimeTurf reputation across the province.</span>
          </div>
        </div>
        <div class="credential-item">
          <span class="credential-num">05</span>
          <div>
            <strong class="credential-text">Drainage Systems</strong>
            <span class="credential-text">Engineered sub-surface drainage installed beneath every turf system for optimal performance and longevity.</span>
          </div>
        </div>
      </div>
    </div>'''

if old_cred04_end in content:
    content = content.replace(old_cred04_end, new_cred04_end)
    log("Credential 05 (Drainage Systems) added after credential 04")
else:
    print("  [WARN] Credential 04 end block not found — trying flexible match")
    # Try a more flexible approach
    flex_cred04 = re.compile(
        r'(<strong class="credential-text">Legacy of Excellence</strong>\s*'
        r'<span class="credential-text">.*?</span>\s*'
        r'</div>\s*'
        r'</div>)(\s*</div>\s*</div>)',
        re.DOTALL
    )
    new_cred05_block = '''
        <div class="credential-item">
          <span class="credential-num">05</span>
          <div>
            <strong class="credential-text">Drainage Systems</strong>
            <span class="credential-text">Engineered sub-surface drainage installed beneath every turf system for optimal performance and longevity.</span>
          </div>
        </div>'''
    m = flex_cred04.search(content)
    if m:
        content = flex_cred04.sub(r'\1' + new_cred05_block + r'\2', content)
        log("Credential 05 added (flexible match)")
    else:
        print("  [ERROR] Credential 04 block not found at all!")

# ─────────────────────────────────────────────
# PHASE 8 — Services section heading
# ─────────────────────────────────────────────
print("\nPhase 8: Services section heading...")

old_svc_heading = 'Premium Greenscape Services'
new_svc_heading = 'Premium Turf Systems'
if old_svc_heading in content:
    content = content.replace(old_svc_heading, new_svc_heading)
    log(f"Services heading: '{old_svc_heading}' → '{new_svc_heading}'")
else:
    print(f"  [WARN] Services heading not found")

old_svc_intro = "Comprehensive luxury greenscape solutions crafted for Gauteng's finest properties and estates — from Pretoria to Sandton."
new_svc_intro = "Premium artificial grass solutions for complexes, schools, restaurants, commercial properties, and residential estates across Gauteng."
if old_svc_intro in content:
    content = content.replace(old_svc_intro, new_svc_intro)
    log("Services intro paragraph updated")
else:
    print(f"  [WARN] Services intro paragraph not found")

# ─────────────────────────────────────────────
# PHASE 9 — Service categories list update + remove panel 02
# ─────────────────────────────────────────────
print("\nPhase 9: Service list + remove panel 02...")

# Replace svc-list content in panel 01
old_svc_list = '''          <li>Residential estate gardens &amp; lawns</li>
          <li>Complex &amp; development common areas</li>
          <li>Children's play areas (safety-graded)</li>
          <li>Pool surrounds &amp; rooftop terraces</li>
          <li>Pet-safe turf specifications</li>'''

# Try with & entity first, then plain &
new_svc_list = '''          <li>Estate Lawns</li>
          <li>School Grounds</li>
          <li>Play Areas</li>
          <li>Restaurant Play Areas</li>
          <li>Residential</li>
          <li>Commercial</li>
          <li>Patios</li>
          <li>Putting Greens</li>'''

if old_svc_list in content:
    content = content.replace(old_svc_list, new_svc_list)
    log("Service panel 01 list updated with new items")
else:
    # Try with plain & instead of &amp;
    old_svc_list_plain = '''          <li>Residential estate gardens & lawns</li>
          <li>Complex & development common areas</li>
          <li>Children's play areas (safety-graded)</li>
          <li>Pool surrounds & rooftop terraces</li>
          <li>Pet-safe turf specifications</li>'''
    if old_svc_list_plain in content:
        content = content.replace(old_svc_list_plain, new_svc_list)
        log("Service panel 01 list updated (plain & match)")
    else:
        print("  [WARN] Service panel 01 list not found — trying regex")
        flex_svc = re.compile(
            r'<li>Residential estate gardens.*?</li>\s*'
            r'<li>Complex.*?</li>\s*'
            r"<li>Children's play areas.*?</li>\s*"
            r'<li>Pool surrounds.*?</li>\s*'
            r'<li>Pet-safe.*?</li>',
            re.DOTALL
        )
        if flex_svc.search(content):
            content = flex_svc.sub(new_svc_list, content)
            log("Service panel 01 list updated (regex match)")
        else:
            print("  [ERROR] Service panel 01 list not found!")

# Remove entire service panel 02 (Irrigation Engineering)
# Panel 02 contains svc-number "02" and ends with closing </div> of the panel
panel02_pattern = re.compile(
    r'\s*<div class="service-panel">\s*'
    r'<div class="svc-number">02</div>.*?'
    r'</div>\s*\n',
    re.DOTALL
)
m = panel02_pattern.search(content)
if m:
    content = panel02_pattern.sub('\n', content)
    log("Service panel 02 (Irrigation Engineering) removed")
else:
    print("  [WARN] Service panel 02 not found — trying broader pattern")
    panel02_broad = re.compile(
        r'[ \t]*<div class="service-panel">[ \t]*\n'
        r'[ \t]*<div class="svc-number">02</div>.*?'
        r'[ \t]*</div>[ \t]*\n',
        re.DOTALL
    )
    if panel02_broad.search(content):
        content = panel02_broad.sub('', content)
        log("Service panel 02 removed (broad match)")
    else:
        print("  [ERROR] Service panel 02 not found!")

# ─────────────────────────────────────────────
# PHASE 10 — Delete Section 03 (Landscape Illumination)
# ─────────────────────────────────────────────
print("\nPhase 10: Remove service panel 03...")

panel03_pattern = re.compile(
    r'\s*<div class="service-panel">\s*'
    r'<div class="svc-number">03</div>.*?'
    r'</div>\s*\n',
    re.DOTALL
)
m = panel03_pattern.search(content)
if m:
    content = panel03_pattern.sub('\n', content)
    log("Service panel 03 (Landscape Illumination) removed")
else:
    print("  [WARN] Service panel 03 not found — trying broader pattern")
    panel03_broad = re.compile(
        r'[ \t]*<div class="service-panel">[ \t]*\n'
        r'[ \t]*<div class="svc-number">03</div>.*?'
        r'[ \t]*</div>[ \t]*\n',
        re.DOTALL
    )
    if panel03_broad.search(content):
        content = panel03_broad.sub('', content)
        log("Service panel 03 removed (broad match)")
    else:
        print("  [ERROR] Service panel 03 not found!")

# ─────────────────────────────────────────────
# PHASE 11 — Process section step updates
# ─────────────────────────────────────────────
print("\nPhase 11: Process section step updates...")

# Step 3: Precision Install → Site Preparation
old_step3_title = '<h4 class="step-title">Precision Install</h4>'
new_step3_title = '<h4 class="step-title">Site Preparation</h4>'
if old_step3_title in content:
    content = content.replace(old_step3_title, new_step3_title)
    log("Step 3 title: 'Precision Install' → 'Site Preparation'")
else:
    print("  [WARN] Step 3 title not found")

old_step3_desc = "Our installation team executes to spec — site preparation, drainage engineering, premium turf laying."
new_step3_desc = "Our installation team levels and prepares the site — surface preparation, drainage levelling and premium turf installation."
if old_step3_desc in content:
    content = content.replace(old_step3_desc, new_step3_desc)
    log("Step 3 description updated")
else:
    print("  [WARN] Step 3 description not found")

# Step 4: Handover → Final Inspection With Operations Manager
old_step4_title = '<h4 class="step-title">Handover</h4>'
new_step4_title = '<h4 class="step-title">Final Inspection With Operations Manager</h4>'
if old_step4_title in content:
    content = content.replace(old_step4_title, new_step4_title)
    log("Step 4 title: 'Handover' → 'Final Inspection With Operations Manager'")
else:
    print("  [WARN] Step 4 title not found")

old_step4_desc = "Final inspection with Leon personally. Full warranty documentation provided. Your outdoor legacy begins."
new_step4_desc = "Final inspection with our Operations Manager. Full warranty documentation provided. Your Outdoor Legacy Begins."
if old_step4_desc in content:
    content = content.replace(old_step4_desc, new_step4_desc)
    log("Step 4 description updated")
else:
    print("  [WARN] Step 4 description not found")

# Add process-guarantee div after closing </div> of .process-steps, before wrap close
process_guarantee_block = '''    <div class="process-guarantee">
      <p>6 Year Manufacturer's Warranty &nbsp;·&nbsp; 24 Month Installation Guarantee</p>
      <p><em>Your Outdoor Legacy Begins.</em></p>
    </div>'''

old_process_end = '    </div>\n  </div>\n</section>\n<!-- ═══════════════ GAUTENG REGION'
new_process_end = '    </div>\n' + process_guarantee_block + '\n  </div>\n</section>\n<!-- ═══════════════ GAUTENG REGION'

if old_process_end in content:
    content = content.replace(old_process_end, new_process_end)
    log("process-guarantee div added after .process-steps")
else:
    print("  [WARN] Process steps end marker not found — trying flexible approach")
    # Find </div> after process-steps
    flex_process = re.compile(
        r'(</div>[ \t]*\n)([ \t]*</div>[ \t]*\n</section>[ \t]*\n<!-- ═+\s*GAUTENG REGION)',
        re.DOTALL
    )
    m = flex_process.search(content)
    if m:
        replacement = m.group(1) + process_guarantee_block + '\n' + m.group(2)
        content = content[:m.start()] + replacement + content[m.end():]
        log("process-guarantee div added (flexible match)")
    else:
        print("  [ERROR] Could not locate process section end!")

# ─────────────────────────────────────────────
# PHASE 12 — Location and testimonials
# ─────────────────────────────────────────────
print("\nPhase 12: Location and testimonials...")

# Gauteng band label
old_gauteng_label = "<span class=\"t-label\">Gauteng's Professional Authority</span>"
new_gauteng_label = '<span class="t-label">Proudly Serving Gauteng</span>'
# Note: After phase 6, "Architectural" became "Professional"
if old_gauteng_label in content:
    content = content.replace(old_gauteng_label, new_gauteng_label)
    log("Gauteng band label updated")
else:
    # Try original (in case phase 6 didn't catch this)
    old_gauteng_label_orig = "<span class=\"t-label\">Gauteng's Architectural Authority</span>"
    if old_gauteng_label_orig in content:
        content = content.replace(old_gauteng_label_orig, new_gauteng_label)
        log("Gauteng band label updated (original form)")
    else:
        print("  [WARN] Gauteng band label not found")

# Gauteng headline
old_gauteng_h2 = '<h2 class="gauteng-headline">Proudly Serving <em>Luxury Estates</em><br>Across Gauteng</h2>'
new_gauteng_h2 = '<h2 class="gauteng-headline">Bringing Premium Grade Turf<br>To Your <em>Doorstep</em></h2>'
if old_gauteng_h2 in content:
    content = content.replace(old_gauteng_h2, new_gauteng_h2)
    log("Gauteng headline updated")
else:
    print("  [WARN] Gauteng headline not found")

# Remove estate-markers div
estate_markers_pattern = re.compile(
    r'[ \t]*<div class="estate-markers">.*?</div>[ \t]*\n',
    re.DOTALL
)
m = estate_markers_pattern.search(content)
if m:
    content = estate_markers_pattern.sub('', content)
    log("estate-markers div removed")
else:
    print("  [WARN] estate-markers div not found")

# Remove entire testimonials section
# From the comment through the closing </section>
testimonials_pattern = re.compile(
    r'<!-- ═+\s*TESTIMONIALS\s*═+ -->\s*\n'
    r'<section id="testimonials".*?</section>\s*\n',
    re.DOTALL
)
m = testimonials_pattern.search(content)
if m:
    content = testimonials_pattern.sub('', content)
    log("Entire testimonials section removed")
else:
    print("  [WARN] Testimonials section not found — trying broader pattern")
    test_broad = re.compile(
        r'<!-- .*?TESTIMONIALS.*?-->\s*\n<section id="testimonials".*?</section>',
        re.DOTALL
    )
    if test_broad.search(content):
        content = test_broad.sub('', content)
        log("Testimonials section removed (broad match)")
    else:
        print("  [ERROR] Testimonials section not found!")

# ─────────────────────────────────────────────
# PHASE 13 — Contact section
# ─────────────────────────────────────────────
print("\nPhase 13: Contact section updates...")

# Change contact info h2
old_contact_h2 = '<h2>Speak with Leon<br>van Eeden Directly</h2>'
new_contact_h2 = '<h2>Speak With Our Operations Manager Directly</h2>'
if old_contact_h2 in content:
    content = content.replace(old_contact_h2, new_contact_h2)
    log("Contact info h2 updated")
else:
    print("  [WARN] Contact info h2 not found")

# Replace the paragraph about Leon
old_leon_para = '<p>Every PrimeTurf project is personally overseen by Managing Director Leon van Eeden. Reach out directly — no call centres, no junior consultants. Your consultation begins the moment you make contact.</p>'
new_leon_para = '''        <p>Every project is overseen by our Operations Manager.<br>Your consultation begins the moment you make contact.<br>Complete the form and our Operations Manager will respond within 24 hours.</p>'''
if old_leon_para in content:
    content = content.replace(old_leon_para, new_leon_para)
    log("Contact Leon paragraph replaced with Operations Manager text")
else:
    print("  [WARN] Contact Leon paragraph not found — trying flexible match")
    flex_leon = re.compile(
        r'<p>Every PrimeTurf project is personally overseen by Managing Director Leon van Eeden.*?</p>',
        re.DOTALL
    )
    if flex_leon.search(content):
        content = flex_leon.sub(new_leon_para, content)
        log("Contact Leon paragraph replaced (flexible match)")
    else:
        print("  [ERROR] Contact Leon paragraph not found!")

# ─────────────────────────────────────────────
# PHASE 14 — Remove form service selection
# ─────────────────────────────────────────────
print("\nPhase 14: Remove form service selection...")

# Remove the entire form-group div containing the Service Required select
service_select_pattern = re.compile(
    r'[ \t]*<div class="form-group">[ \t]*\n'
    r'[ \t]*<label>Service Required</label>[ \t]*\n'
    r'[ \t]*<select>.*?</select>[ \t]*\n'
    r'[ \t]*</div>[ \t]*\n',
    re.DOTALL
)
m = service_select_pattern.search(content)
if m:
    content = service_select_pattern.sub('', content)
    log("Form 'Service Required' select group removed")
else:
    print("  [WARN] Service Required form group not found")

# ─────────────────────────────────────────────
# PHASE 15 — Footer
# ─────────────────────────────────────────────
print("\nPhase 15: Footer updates...")

# Update footer gradient
old_gradient = 'linear-gradient(175deg, var(--emerald-deep) 0%, #0a1f12 60%, #050e08 100%)'
new_gradient = 'linear-gradient(175deg, #1A3A2A 0%, #1A3A2A 60%, #1C4A2A 100%)'
if old_gradient in content:
    content = content.replace(old_gradient, new_gradient)
    log("Footer gradient updated")
else:
    print("  [WARN] Footer gradient not found")

# Replace footer services nav list
old_footer_nav = '''        <ul class="footer-nav-list">
          <li><a href="#services">Turf Installation</a></li>
          <li><a href="#services">Irrigation Systems</a></li>
          <li><a href="#services">Landscape Lighting</a></li>
          <li><a href="#contact">Free Consultation</a></li>
        </ul>'''

new_footer_nav = '''        <ul class="footer-nav-list">
          <li><a href="#services">Luxury Turf Installation Indoor Or Outdoor</a></li>
          <li><a href="#services">Paving Or Stonework</a></li>
          <li><a href="#services">Playground</a></li>
          <li><a href="#services">Putting Green</a></li>
          <li><a href="#services">Restaurant Play Area</a></li>
          <li><a href="#services">School Indoor Or Outdoor Area</a></li>
          <li><a href="#services">Custom Installs</a></li>
        </ul>'''

if old_footer_nav in content:
    content = content.replace(old_footer_nav, new_footer_nav)
    log("Footer Services nav list updated with new items")
else:
    print("  [WARN] Footer services nav not found — trying flexible match")
    flex_footer_nav = re.compile(
        r'(<span class="footer-col-title">Services</span>\s*)'
        r'<ul class="footer-nav-list">.*?</ul>',
        re.DOTALL
    )
    if flex_footer_nav.search(content):
        content = flex_footer_nav.sub(r'\1' + new_footer_nav, content)
        log("Footer Services nav updated (flexible match)")
    else:
        print("  [ERROR] Footer services nav not found!")

# ─────────────────────────────────────────────
# WRITE OUTPUT
# ─────────────────────────────────────────────
print("\nWriting file...")
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nDone. File written to {OUTPUT_FILE}")
print(f"\n{'='*60}")
print("SUMMARY OF CHANGES:")
print('='*60)
for i, change in enumerate(changes_log, 1):
    print(f"  {i:2d}. {change}")
print('='*60)
print(f"Total: {len(changes_log)} changes applied")

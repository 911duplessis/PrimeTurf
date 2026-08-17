#!/usr/bin/env python3
"""Extract SEO metadata from all GitHub Pages HTML files for comparison.

Usage:
    python3 automation/github-seo-extractor.py

Parses every public HTML file in the repo and extracts: title, meta description,
canonical URL, H1, JSON-LD schema types, OG tags, and internal links. Saves a
structured report to audit/github-seo-baseline.json.
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

REPO_ROOT = Path(".")
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
DESC_RE = re.compile(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', re.I)
CANONICAL_RE = re.compile(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']*)["\']', re.I)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.I | re.S)
NOINDEX_RE = re.compile(r'<meta[^>]*name=["\']robots["\'][^>]*content=["\'][^"\']*noindex', re.I)
OG_TITLE_RE = re.compile(r'<meta[^>]*property=["\']og:title["\'][^>]*content=["\']([^"\']*)["\']', re.I)
OG_DESC_RE = re.compile(r'<meta[^>]*property=["\']og:description["\'][^>]*content=["\']([^"\']*)["\']', re.I)
OG_IMAGE_RE = re.compile(r'<meta[^>]*property=["\']og:image["\'][^>]*content=["\']([^"\']*)["\']', re.I)
SCHEMA_RE = re.compile(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.I | re.S)
HREF_RE = re.compile(r'href=["\']([^"\']*)["\']', re.I)

EXCLUDED_DIRS = {"crm", "design", "community", "node_modules", ".git", ".github"}
EXCLUDED_FILES = {
    "indexMaster.html", "project-plan.html", "seo-dashboard.html",
    "seo-engine.html", "seo-report.html", "tcn-dashboard.html",
    "tcn-whatsapp-flow.html", "connection-network.html",
    "vendor-signup.html", "partner-agreement.html",
    "google2bbf502f984c3743.html", "google57c2ac6f73edc94d.html",
}


def extract_schema_types(html: str) -> list[dict]:
    schemas = []
    for match in SCHEMA_RE.finditer(html):
        try:
            data = json.loads(match.group(1))
            if isinstance(data, list):
                for item in data:
                    if "@type" in item:
                        schemas.append({"@type": item["@type"]})
            elif "@type" in data:
                schemas.append({"@type": data["@type"]})
                if "@graph" in data:
                    for item in data["@graph"]:
                        if "@type" in item:
                            schemas.append({"@type": item["@type"]})
        except json.JSONDecodeError:
            continue
    return schemas


def extract_internal_links(html: str) -> list[str]:
    links = set()
    for match in HREF_RE.finditer(html):
        href = match.group(1)
        if href.startswith("/") and not href.startswith("//"):
            links.add(href.split("#")[0].split("?")[0])
        elif href.startswith("https://www.primeturf.co.za"):
            path = href.replace("https://www.primeturf.co.za", "")
            links.add(path.split("#")[0].split("?")[0] or "/")
    return sorted(links)


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip()


def find_html_files() -> list[Path]:
    files = []
    for f in sorted(REPO_ROOT.rglob("*.html")):
        parts = f.parts
        if any(d in EXCLUDED_DIRS for d in parts):
            continue
        if f.name in EXCLUDED_FILES:
            continue
        if f.name.startswith("."):
            continue
        files.append(f)
    return files


def main():
    html_files = find_html_files()
    print(f"Found {len(html_files)} public HTML files\n")

    pages = []
    for f in html_files:
        html = f.read_text(errors="replace")

        rel_path = "/" + str(f.relative_to(REPO_ROOT))
        if rel_path.endswith("/index.html"):
            url_path = rel_path.rsplit("/index.html", 1)[0] + "/" or "/"
        else:
            url_path = rel_path

        title_m = TITLE_RE.search(html)
        desc_m = DESC_RE.search(html)
        canonical_m = CANONICAL_RE.search(html)
        h1_m = H1_RE.search(html)
        og_title_m = OG_TITLE_RE.search(html)
        og_desc_m = OG_DESC_RE.search(html)
        og_image_m = OG_IMAGE_RE.search(html)

        page = {
            "file": str(f),
            "url_path": url_path,
            "title": strip_html(title_m.group(1)) if title_m else None,
            "meta_description": desc_m.group(1) if desc_m else None,
            "canonical": canonical_m.group(1) if canonical_m else None,
            "h1": strip_html(h1_m.group(1)) if h1_m else None,
            "noindex": bool(NOINDEX_RE.search(html)),
            "og_title": og_title_m.group(1) if og_title_m else None,
            "og_description": og_desc_m.group(1) if og_desc_m else None,
            "og_image": og_image_m.group(1) if og_image_m else None,
            "schemas": extract_schema_types(html),
            "internal_links": extract_internal_links(html),
        }
        pages.append(page)

        schema_types = ", ".join(s["@type"] for s in page["schemas"]) or "none"
        noindex = " [NOINDEX]" if page["noindex"] else ""
        print(f"  {url_path:<55} {(page['title'] or 'NO TITLE')[:50]:<50} schema: {schema_types}{noindex}")

    output = {
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "total_pages": len(pages),
        "pages": pages,
    }

    output_path = Path("audit/github-seo-baseline.json")
    output_path.write_text(json.dumps(output, indent=2))
    print(f"\nBaseline saved to {output_path}")


if __name__ == "__main__":
    main()

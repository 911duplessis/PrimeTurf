#!/usr/bin/env python3
"""Compare GitHub sitemap.xml against the live Wix sitemap.

Usage:
    python3 automation/sitemap-comparator.py

Fetches the live Wix sitemap from https://www.primeturf.co.za/sitemap.xml,
parses the local GitHub sitemap.xml, and produces a three-way comparison
showing which URLs exist on GitHub only, Wix only, or both.

Outputs to stdout and saves to audit/sitemap-comparison.json.
"""

import json
import sys
import xml.etree.ElementTree as ET
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

DOMAIN = "https://www.primeturf.co.za"
GITHUB_SITEMAP = "sitemap.xml"


def parse_sitemap_urls(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = []
    for url_elem in root.findall(".//sm:url", ns):
        loc = url_elem.find("sm:loc", ns)
        lastmod = url_elem.find("sm:lastmod", ns)
        priority = url_elem.find("sm:priority", ns)
        if loc is not None:
            urls.append({
                "url": loc.text.strip(),
                "lastmod": lastmod.text.strip() if lastmod is not None else None,
                "priority": priority.text.strip() if priority is not None else None,
            })
    return urls


def normalize_path(url: str) -> str:
    path = url.replace(DOMAIN, "").replace("http://www.primeturf.co.za", "")
    return path.rstrip("/") or "/"


def main():
    github_path = Path(GITHUB_SITEMAP)
    if not github_path.exists():
        print(f"Error: {GITHUB_SITEMAP} not found. Run from the repo root.", file=sys.stderr)
        sys.exit(1)

    github_urls = parse_sitemap_urls(github_path.read_text())
    github_paths = {normalize_path(u["url"]): u for u in github_urls}

    print(f"GitHub sitemap: {len(github_urls)} URLs\n")

    try:
        req = urllib.request.Request(
            f"{DOMAIN}/sitemap.xml",
            headers={"User-Agent": "PrimeTurf-Sitemap-Comparator/1.0"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            wix_xml = resp.read().decode("utf-8")

        if "<sitemapindex" in wix_xml:
            print("Wix sitemap is a sitemap index. Fetching child sitemaps...")
            root = ET.fromstring(wix_xml)
            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            wix_urls = []
            for sitemap in root.findall(".//sm:sitemap", ns):
                loc = sitemap.find("sm:loc", ns)
                if loc is not None:
                    child_req = urllib.request.Request(
                        loc.text.strip(),
                        headers={"User-Agent": "PrimeTurf-Sitemap-Comparator/1.0"}
                    )
                    with urllib.request.urlopen(child_req, timeout=15) as child_resp:
                        child_xml = child_resp.read().decode("utf-8")
                    wix_urls.extend(parse_sitemap_urls(child_xml))
                    print(f"  Fetched {loc.text.strip()} ({len(parse_sitemap_urls(child_xml))} URLs)")
        else:
            wix_urls = parse_sitemap_urls(wix_xml)

        wix_paths = {normalize_path(u["url"]): u for u in wix_urls}
        print(f"Wix sitemap: {len(wix_urls)} URLs\n")

    except Exception as e:
        print(f"Warning: Could not fetch Wix sitemap: {e}")
        print("Comparison will show GitHub-only URLs.\n")
        wix_urls = []
        wix_paths = {}

    all_paths = sorted(set(list(github_paths.keys()) + list(wix_paths.keys())))

    github_only = []
    wix_only = []
    both = []

    print(f"{'Path':<60} {'GitHub':<10} {'Wix':<10} {'Status'}")
    print("-" * 100)

    for path in all_paths:
        in_github = path in github_paths
        in_wix = path in wix_paths
        if in_github and in_wix:
            status = "BOTH"
            both.append(path)
        elif in_github:
            status = "GITHUB ONLY"
            github_only.append(path)
        else:
            status = "WIX ONLY"
            wix_only.append(path)

        print(f"{path:<60} {'YES' if in_github else '-':<10} {'YES' if in_wix else '-':<10} {status}")

    print(f"\n{'='*100}")
    print(f"On both:      {len(both)}")
    print(f"GitHub only:  {len(github_only)} (need Wix page + redirect)")
    print(f"Wix only:     {len(wix_only)} (new Wix content, no GitHub equivalent)")

    if github_only:
        print(f"\nGitHub-only URLs needing migration:")
        for p in github_only:
            print(f"  {p}")

    output = {
        "compared_at": datetime.now(timezone.utc).isoformat(),
        "github_sitemap_count": len(github_urls),
        "wix_sitemap_count": len(wix_urls),
        "on_both": both,
        "github_only": github_only,
        "wix_only": wix_only,
        "github_urls": github_urls,
        "wix_urls": wix_urls,
    }

    output_path = Path("audit/sitemap-comparison.json")
    output_path.write_text(json.dumps(output, indent=2))
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()

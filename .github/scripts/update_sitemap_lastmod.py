#!/usr/bin/env python3
"""Bump <lastmod> in sitemap.xml for URLs whose source file changed in this push."""
import re
import subprocess
import sys
from datetime import date, timezone, datetime

SITEMAP = "sitemap.xml"

PAGE_TO_URL = {
    "index.html": "https://primeturf.co.za/",
    "contact.html": "https://primeturf.co.za/contact.html",
    "artificial-grass-johannesburg.html": "https://primeturf.co.za/artificial-grass-johannesburg.html",
    "artificial-grass-cape-town.html": "https://primeturf.co.za/artificial-grass-cape-town.html",
    "quote-calculator.html": "https://primeturf.co.za/quote-calculator.html",
    "blog/index.html": "https://primeturf.co.za/blog/",
    "blog/artificial-grass-cost-guide-south-africa.html": "https://primeturf.co.za/blog/artificial-grass-cost-guide-south-africa.html",
    "blog/drought-proof-garden-cape-town.html": "https://primeturf.co.za/blog/drought-proof-garden-cape-town.html",
}


def changed_files(before_sha, after_sha):
    out = subprocess.run(
        ["git", "diff", "--name-only", before_sha, after_sha],
        capture_output=True, text=True, check=True,
    ).stdout
    return set(out.splitlines())


def main():
    if len(sys.argv) != 3:
        print("usage: update_sitemap_lastmod.py <before_sha> <after_sha>")
        sys.exit(1)
    before_sha, after_sha = sys.argv[1], sys.argv[2]

    files = changed_files(before_sha, after_sha)
    urls_to_bump = {PAGE_TO_URL[f] for f in files if f in PAGE_TO_URL}

    if not urls_to_bump:
        print("No tracked sitemap pages changed — nothing to do.")
        return

    with open(SITEMAP, "r", encoding="utf-8") as f:
        content = f.read()

    today = datetime.now(timezone.utc).date().isoformat()
    changed = False

    for url in urls_to_bump:
        pattern = re.compile(
            r"(<loc>" + re.escape(url) + r"</loc>\s*<lastmod>)\d{4}-\d{2}-\d{2}(</lastmod>)"
        )
        new_content, n = pattern.subn(r"\g<1>" + today + r"\g<2>", content)
        if n:
            content = new_content
            changed = True
            print(f"Bumped lastmod for {url} -> {today}")
        else:
            print(f"WARNING: no sitemap entry matched for {url}")

    if changed:
        with open(SITEMAP, "w", encoding="utf-8") as f:
            f.write(content)


if __name__ == "__main__":
    main()

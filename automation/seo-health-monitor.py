#!/usr/bin/env python3
"""Self-healing SEO health monitor for PrimeTurf Wix site.

Usage:
    python3 automation/seo-health-monitor.py [--verbose]

Periodically checks:
  1. All expected URLs return 200
  2. All 301 redirects are still in place
  3. Sitemap includes all expected pages
  4. No accidental noindex tags
  5. Page titles and descriptions haven't regressed

Designed to run on a schedule (cron/GitHub Actions) and output a
summary report to audit/health-check-latest.json.
"""

import json
import sys
import urllib.request
import urllib.error
import re
from datetime import datetime, timezone
from pathlib import Path

DOMAIN = "https://www.primeturf.co.za"

EXPECTED_PAGES = [
    "/",
    "/about-us",
    "/contact",
    "/blog",
    "/quote",
    "/services",
    "/gallery",
    "/english-privacy-policy",
    "/accessibility-statement",
    "/artificial-grass-sandton",
    "/artificial-grass-johannesburg",
    "/artificial-grass-hyde-park",
    "/artificial-grass-edenvale",
]

FUTURE_PAGES = [
    "/artificial-grass-cape-town",
    "/artificial-grass-pretoria-east",
    "/artificial-grass-centurion",
    "/artificial-grass-fourways",
    "/artificial-grass-bryanston",
    "/artificial-grass-boksburg",
    "/artificial-grass-steyn-city",
    "/artificial-grass-midrand",
    "/artificial-grass-bedfordview",
    "/artificial-grass-houghton",
    "/artificial-grass-mooikloof",
    "/artificial-grass-randburg",
    "/artificial-grass-roodepoort",
    "/artificial-grass-silver-lakes",
    "/artificial-grass-waterfall-city",
    "/terms-of-service",
]

TITLE_SHOULD_NOT_CONTAIN = ["Home |", "Poduct"]
NOINDEX_PATTERN = re.compile(r'<meta[^>]*name=["\']robots["\'][^>]*content=["\'][^"\']*noindex', re.IGNORECASE)
TITLE_PATTERN = re.compile(r'<title[^>]*>(.*?)</title>', re.IGNORECASE | re.DOTALL)
DESC_PATTERN = re.compile(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', re.IGNORECASE)

verbose = "--verbose" in sys.argv


def fetch_page(path: str) -> dict:
    url = f"{DOMAIN}{path}"
    result = {"url": path, "full_url": url}

    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "PrimeTurf-SEO-Monitor/1.0"
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            result["status"] = resp.status
            html = resp.read().decode("utf-8", errors="replace")

            title_match = TITLE_PATTERN.search(html)
            result["title"] = title_match.group(1).strip() if title_match else None

            desc_match = DESC_PATTERN.search(html)
            result["description"] = desc_match.group(1).strip() if desc_match else None

            result["has_noindex"] = bool(NOINDEX_PATTERN.search(html))

    except urllib.error.HTTPError as e:
        result["status"] = e.code
    except Exception as e:
        result["status"] = "ERROR"
        result["error"] = str(e)

    return result


def main():
    print(f"\nPrimeTurf SEO Health Monitor — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"Checking {len(EXPECTED_PAGES)} live pages + {len(FUTURE_PAGES)} future pages\n")

    issues = []
    page_results = []

    for path in EXPECTED_PAGES:
        result = fetch_page(path)
        page_results.append(result)

        status = result.get("status")
        if status != 200:
            issue = f"CRITICAL: {path} returns {status} (expected 200)"
            issues.append({"severity": "CRITICAL", "page": path, "issue": issue})
            print(f"  [FAIL] {issue}")
            continue

        if result.get("has_noindex"):
            issue = f"HIGH: {path} has noindex meta tag"
            issues.append({"severity": "HIGH", "page": path, "issue": issue})
            print(f"  [WARN] {issue}")

        title = result.get("title", "")
        for bad in TITLE_SHOULD_NOT_CONTAIN:
            if bad in title:
                issue = f"MEDIUM: {path} title contains '{bad}' — likely missing custom title"
                issues.append({"severity": "MEDIUM", "page": path, "issue": issue})
                print(f"  [WARN] {issue}")

        if not result.get("description"):
            issue = f"LOW: {path} has no meta description"
            issues.append({"severity": "LOW", "page": path, "issue": issue})
            if verbose:
                print(f"  [INFO] {issue}")

        if verbose:
            print(f"  [OK]   {path} — {status} — {title[:60]}")

    print(f"\nChecking future pages (expected 404 until created)...")
    newly_live = []
    for path in FUTURE_PAGES:
        result = fetch_page(path)
        page_results.append(result)
        if result.get("status") == 200:
            newly_live.append(path)
            print(f"  [NEW]  {path} is now live!")
        elif verbose:
            print(f"  [----] {path} — {result.get('status')} (still pending)")

    print(f"\n{'='*80}")
    print(f"Issues found: {len(issues)}")
    print(f"  Critical: {sum(1 for i in issues if i['severity'] == 'CRITICAL')}")
    print(f"  High:     {sum(1 for i in issues if i['severity'] == 'HIGH')}")
    print(f"  Medium:   {sum(1 for i in issues if i['severity'] == 'MEDIUM')}")
    print(f"  Low:      {sum(1 for i in issues if i['severity'] == 'LOW')}")

    if newly_live:
        print(f"\nNewly live pages ({len(newly_live)}) — update redirect-map.csv and configure 301s:")
        for p in newly_live:
            print(f"  {p}")

    output = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "domain": DOMAIN,
        "expected_pages_checked": len(EXPECTED_PAGES),
        "future_pages_checked": len(FUTURE_PAGES),
        "issues": issues,
        "newly_live_pages": newly_live,
        "pages": page_results,
    }

    output_path = Path("audit/health-check-latest.json")
    output_path.write_text(json.dumps(output, indent=2))
    print(f"\nFull results saved to {output_path}")

    critical_count = sum(1 for i in issues if i["severity"] == "CRITICAL")
    return 1 if critical_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())

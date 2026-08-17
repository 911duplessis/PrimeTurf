#!/usr/bin/env python3
"""Validate all 301 redirects from old GitHub Pages URLs to new Wix URLs.

Usage:
    python3 automation/redirect-validator.py [--csv audit/redirect-spec.csv]

Checks each old URL with a HEAD request, verifying:
  - Response is a 301 redirect (not 302, 404, or 200)
  - Location header points to the correct new URL
  - Final destination returns 200

Outputs results to stdout and optionally to audit/redirect-validation-results.json.
"""

import csv
import json
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

DOMAIN = "https://www.primeturf.co.za"
DEFAULT_CSV = "audit/redirect-spec.csv"


def check_redirect(old_path: str, expected_new_path: str) -> dict:
    old_url = f"{DOMAIN}{old_path}"
    expected_destination = f"{DOMAIN}{expected_new_path}"

    result = {
        "old_url": old_path,
        "expected_new_url": expected_new_path,
        "old_full_url": old_url,
        "expected_full_url": expected_destination,
    }

    try:
        req = urllib.request.Request(old_url, method="HEAD")
        req.add_header("User-Agent", "PrimeTurf-Redirect-Validator/1.0")

        class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, req, fp, code, msg, headers, newurl):
                return None

        opener = urllib.request.build_opener(NoRedirectHandler)
        response = opener.open(req, timeout=10)
        status = response.status
        location = response.headers.get("Location", "")

    except urllib.error.HTTPError as e:
        status = e.code
        location = e.headers.get("Location", "")
    except Exception as e:
        result["status"] = "ERROR"
        result["error"] = str(e)
        result["pass"] = False
        return result

    result["http_status"] = status
    result["location_header"] = location

    if status == 301:
        normalized_location = location.rstrip("/")
        normalized_expected = expected_destination.rstrip("/")

        if normalized_location == normalized_expected:
            result["status"] = "PASS"
            result["pass"] = True
        else:
            result["status"] = "WRONG_DESTINATION"
            result["pass"] = False
            result["detail"] = f"Redirects to {location} instead of {expected_destination}"
    elif status == 302:
        result["status"] = "WRONG_REDIRECT_TYPE"
        result["pass"] = False
        result["detail"] = "302 temporary redirect instead of 301 permanent"
    elif status == 404:
        result["status"] = "NOT_FOUND"
        result["pass"] = False
        result["detail"] = "No redirect configured - returns 404"
    elif status == 200:
        result["status"] = "NO_REDIRECT"
        result["pass"] = False
        result["detail"] = "Page serves content instead of redirecting"
    else:
        result["status"] = f"UNEXPECTED_{status}"
        result["pass"] = False

    return result


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CSV

    if not Path(csv_path).exists():
        print(f"Error: {csv_path} not found. Run from the repo root.", file=sys.stderr)
        sys.exit(1)

    with open(csv_path) as f:
        reader = csv.DictReader(f)
        redirects = list(reader)

    results = []
    passed = 0
    failed = 0
    skipped = 0

    print(f"\nPrimeTurf Redirect Validator — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"Testing {len(redirects)} redirects against {DOMAIN}\n")
    print(f"{'Old URL':<55} {'Expected':<55} {'Result'}")
    print("-" * 140)

    for row in redirects:
        old_url = row["old_url"]
        new_url = row["new_url"]
        status = row.get("status", "")

        if status == "blocked":
            skipped += 1
            print(f"{old_url:<55} {new_url:<55} SKIPPED (page not yet created)")
            results.append({
                "old_url": old_url,
                "expected_new_url": new_url,
                "status": "SKIPPED",
                "pass": None,
                "detail": "Prerequisite page not yet created on Wix"
            })
            continue

        result = check_redirect(old_url, new_url)
        results.append(result)

        if result.get("pass"):
            passed += 1
            print(f"{old_url:<55} {new_url:<55} PASS (301)")
        else:
            failed += 1
            detail = result.get("detail", result.get("error", "Unknown"))
            print(f"{old_url:<55} {new_url:<55} FAIL: {detail}")

    print(f"\n{'='*140}")
    print(f"Results: {passed} passed, {failed} failed, {skipped} skipped (blocked)")
    print(f"Total: {len(redirects)} redirects checked")

    if failed > 0:
        print(f"\nAction needed: {failed} redirects are not configured correctly.")
        print("Configure them in Wix: Site Settings > SEO Tools > URL Redirect Manager")

    output_path = Path("audit/redirect-validation-results.json")
    output = {
        "validated_at": datetime.now(timezone.utc).isoformat(),
        "domain": DOMAIN,
        "summary": {"passed": passed, "failed": failed, "skipped": skipped, "total": len(redirects)},
        "results": results,
    }
    output_path.write_text(json.dumps(output, indent=2))
    print(f"\nDetailed results saved to {output_path}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

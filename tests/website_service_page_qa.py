"""Browser acceptance checks for the local P14 service-page prototype."""
from __future__ import annotations

import json
import argparse
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "examples" / "service-page-journey" / "index.html"
WIDTHS = [320, 375, 390, 768, 1024, 1440]


def run(screenshots_dir: Path | None = None) -> dict:
    errors: list[str] = []
    requests: list[str] = []
    captures: list[str] = []
    browser_version = "unknown"
    if screenshots_dir:
        screenshots_dir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        browser_version = browser.version
        page = browser.new_page()
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on("request", lambda request: requests.append(request.url) if request.url.startswith(("http://", "https://")) else None)
        widths: list[dict] = []
        for width in WIDTHS:
            page.set_viewport_size({"width": width, "height": 900})
            page.goto(PAGE.as_uri(), wait_until="load")
            metrics = page.evaluate("({viewport: innerWidth, document: document.documentElement.scrollWidth, body: document.body.scrollWidth})")
            assert metrics["document"] <= width and metrics["body"] <= width, f"horizontal overflow at {width}: {metrics}"
            assert page.locator('meta[name="robots"]').get_attribute("content") == "noindex,nofollow"
            assert page.locator('script[type="application/ld+json"]').count() == 0
            assert page.get_by_role("heading", name="Make the work behind your work easier to see.").is_visible()
            widths.append({"width": width, **metrics})

        page.set_viewport_size({"width": 390, "height": 844})
        page.goto(PAGE.as_uri(), wait_until="load")
        if screenshots_dir:
            target = screenshots_dir / "mobile-390-initial.png"
            page.screenshot(path=str(target), full_page=True)
            captures.append(str(target))
        page.keyboard.press("Tab")
        assert page.locator(".skip").evaluate("el => getComputedStyle(el).transform === 'none'"), "skip link is not exposed on keyboard focus"
        page.get_by_role("link", name="Skip to content").press("Enter")
        assert page.evaluate("document.activeElement.id") == "main"

        form = page.locator("#enquiry-form")
        form.get_by_role("button", name="Send enquiry (prototype only)").click()
        assert page.get_by_role("alert").is_visible(), "invalid form must show an error summary"
        assert page.locator("#name").get_attribute("aria-invalid") == "true"
        assert page.get_by_role("link", name="Add your name.").get_attribute("href") == "#name"
        assert page.locator("#contact-ok").get_attribute("aria-invalid") == "true"
        assert page.locator("#consent-error").is_visible(), "consent checkbox needs its linked inline error"
        assert page.locator("#consent-error").inner_text() == "Confirm that the team may use these details to respond."
        if screenshots_dir:
            target = screenshots_dir / "mobile-390-validation-errors.png"
            page.screenshot(path=str(target), full_page=True)
            captures.append(str(target))

        page.locator("#name").fill("Sam Example")
        page.locator("#email").fill("sam@example.test")
        page.locator("#topic").select_option(label="Systems or tools")
        page.locator("#details").fill("Please discuss how the handoff works.")
        page.locator("#contact-ok").check()
        assert page.locator("#consent-error").is_hidden(), "correcting consent must clear its inline error"
        page.get_by_role("button", name="Preview server error").click()
        assert page.get_by_role("status").inner_text().startswith("A temporary error occurred")
        assert page.locator("#name").input_value() == "Sam Example"
        assert page.locator("#details").input_value() == "Please discuss how the handoff works."

        page.get_by_role("button", name="Send enquiry (prototype only)").click()
        assert "not sent or stored" in page.get_by_role("status").inner_text()
        assert page.locator("#name").input_value() == "Sam Example"
        assert not any("localhost" in url or "example.com/" in url for url in requests), f"unexpected external request(s): {requests}"
        assert not errors, f"browser JavaScript errors: {errors}"
        if screenshots_dir:
            page.set_viewport_size({"width": 1440, "height": 900})
            page.goto(PAGE.as_uri(), wait_until="load")
            target = screenshots_dir / "desktop-1440-initial.png"
            page.screenshot(path=str(target), full_page=True)
            captures.append(str(target))
        browser.close()
    return {"result": "PASS", "browser": "Microsoft Edge via Playwright", "browser_version": browser_version,
            "environment": "Windows host, headless run; viewport changed per case; CPU and network not throttled or emulated",
            "viewports": widths,
            "interaction_checks": ["skip link and focus", "required-field summary and linked errors", "server-error recovery preserves input", "submit remains local and states no data sent"],
            "external_requests": requests, "browser_errors": errors, "screenshots": captures,
            "not_assessed": ["screen reader and assistive-technology compatibility", "200% and 400% zoom/reflow", "WCAG conformance", "cross-browser behaviour", "real-user task completion", "field performance", "production deployment"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--screenshots-dir", type=Path)
    args = parser.parse_args()
    print(json.dumps(run(args.screenshots_dir), indent=2))

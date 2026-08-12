"""
Renders brand-guidelines-print.html to V2-Helicopters-Brand-Guidelines.pdf
using a local Chrome install via Playwright (channel="chrome" - no
separate browser download needed).

Run: python pdf-export/build.py && python pdf-export/render.py
"""
import os
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

html_path = os.path.join(ROOT, "brand-guidelines-print.html")
pdf_path = os.path.join(ROOT, "V2-Helicopters-Brand-Guidelines.pdf")

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome")
    page = browser.new_page()
    page.goto("file:///" + html_path.replace("\\", "/"))
    page.wait_for_timeout(300)
    page.pdf(path=pdf_path, print_background=True, prefer_css_page_size=True)
    browser.close()

print("PDF written:", pdf_path, os.path.getsize(pdf_path), "bytes")

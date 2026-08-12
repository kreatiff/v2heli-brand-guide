"""
Builds brand-guidelines-print.html from pdf-export/template.html +
pdf-export/pages.html, pulling the font/photo/clear-space assets straight
out of the main brand-guidelines.html (single source of truth for those
base64 blobs, so there is nothing to keep in sync by hand).

Run: python pdf-export/build.py
Then: python pdf-export/render.py   (needs `pip install playwright`,
      and a local Chrome install since it launches channel="chrome")
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

with open(os.path.join(ROOT, "brand-guidelines.html"), "r", encoding="utf-8") as f:
    SOURCE = f.read()


def extract(marker, end_char):
    start = SOURCE.find(marker)
    if start == -1:
        raise RuntimeError(f"marker not found: {marker[:50]}")
    end = SOURCE.find(end_char, start)
    return SOURCE[start:end]


font_data_uri = extract("data:font/woff2;base64,d09GMgABAAAAAFcQ", ")")
photo_data_uri = extract("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD", '"')
clh_data_uri = extract("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA8AAAAFXCAMA", '"')
clv_data_uri = extract("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA8AAAAKqCAMA", '"')

font_b64 = font_data_uri.split(",", 1)[1]
photo_b64 = photo_data_uri.split(",", 1)[1]
clh_b64 = clh_data_uri.split(",", 1)[1]
clv_b64 = clv_data_uri.split(",", 1)[1]

with open(os.path.join(HERE, "template.html"), "r", encoding="utf-8") as f:
    template = f.read()
with open(os.path.join(HERE, "pages.html"), "r", encoding="utf-8") as f:
    pages = f.read()

out = template.replace("__PAGES__", pages)
out = out.replace("__FONT_B64__", font_b64)
out = out.replace("__PHOTO_B64__", photo_b64)
out = out.replace("__CLEARSPACE_H_B64__", clh_b64)
out = out.replace("__CLEARSPACE_V_B64__", clv_b64)

out_path = os.path.join(ROOT, "brand-guidelines-print.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(out)

print("Built:", out_path, f"({len(out)} chars)")

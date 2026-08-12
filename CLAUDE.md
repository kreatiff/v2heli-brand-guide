# V2 Helicopters — brand guidelines site

Single-page brand guide for V2 Helicopters (Brisbane-based helicopter charter,
training and scenic flights), built as a standalone webpage from the client's
`brand-Guide.pdf` (not in this folder; ask the user if you need the source PDF
again).

## What's here

- `brand-guidelines.html` — the deliverable. Single self-contained HTML file:
  CSS in a `<style>` block, JS at the bottom, no build step, no npm, no
  external requests at runtime.
- `SVG/` — official logo vectors: `v2heli_logo_horizontal.svg`,
  `v2heli_logo_stacked.svg`, `v2heli_logomark.svg`, plus `_bnw` variants
  (`horizontal_bnw`, `stacked_bnw`) for use on the lime brand colour, where
  the standard two-tone lockup would put lime on lime.
- `PNG/` — raster exports of the same three lockups at 0.5x/1x/2x.
- `spacing_horizontal.png`, `spacing_vertical.png` — client-exported clear
  space diagrams, used as-is (embedded) in the Logo section.

No `package.json`, no git repo. It's one file plus its source assets.

## Hard constraints (do not relax without asking)

- **Single file.** `brand-guidelines.html` must stay self-contained: no
  external font/CDN/script requests. Space Grotesk is embedded as a base64
  variable-font `@font-face` (weights 300–700). Any new image goes in as a
  base64 data URI, not a relative `<img src="...">` link.
- **CSS classes only.** No inline `style="..."` attributes anywhere in the
  HTML. No Tailwind.
- **No em dashes** in visible copy. Grep for `—` before calling anything done.
- Logo SVGs are inlined directly in the HTML with `fill` attributes stripped
  and replaced by classes: `ink` (→ `var(--ink)`), `lime` (→ `var(--lime)`),
  `accent-white` (→ `var(--white)`, only in the `_bnw` variants). Background
  context is set with modifier classes on the wrapping element: `on-dark`
  flips `.ink` to white, `on-lime` keeps `.ink` as ink. This is how one SVG
  works on white, charcoal and lime without duplicate files. Follow this
  pattern for any new logo placement instead of hardcoding fills.

## Brand facts (from the source PDF, treat as ground truth)

- Colours: Velocity Lime `#CADB2B` (CMYK 25/0/100/0), Charcoal `#1A1A1A`
  (CMYK 72/66/65/78), Pure White `#FFFFFF`.
- Fonts: wordmark is a custom-cut display face, logotype only, letters only
  (not a working font, don't try to set other text in it). Everything else
  is Space Grotesk.
- Personality: Precise, Trusted, Skilled, Innovative, Experienced, Agile,
  Professional, Refined.

## My own additions (not in the client PDF, flag if the client pushes back)

These were added while building the page and should be sanity-checked against
what the client actually wants before treating them as fixed brand rules:
suggested minimum logo sizes (32px stacked / 120px horizontal), the usage
"don'ts" grid, the voice-and-tone do/don't section, the nav-bar mockup in
"In use", and the nearest-Pantone note (Velocity Lime ≈ PMS 382 C, Charcoal ≈
PMS Neutral Black C — approximate, confirm against a physical swatch book
before anything goes to print).

## Loose ends

- `v2heli_logo_horizontal_bnw.svg` exists in `SVG/` but isn't used anywhere
  on the current page — there's no horizontal-lockup-on-lime placement yet.
- No test suite and no visual regression setup. The page was last verified
  manually with a throwaway Playwright + Chromium check (font loading,
  console errors, broken images, contrast, nav anchors) that isn't part of
  this repo. If you add real tooling, a lightweight Playwright smoke test
  (load the file, assert no console errors, assert fonts.check() for Space
  Grotesk) would be a reasonable start.

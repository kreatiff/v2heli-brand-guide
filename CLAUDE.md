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
- `fonts/V2helidisplay-Regular.ttf` — the display face as an actual font
  file. Not used anywhere for rendering the page (Space Grotesk is the only
  `@font-face`); it exists purely so the Downloads section has something to
  link to.
- `v2heli-logo-files.zip` — a bundle of `SVG/` + `PNG/` (all files, no
  `desktop.ini`) for the "Download logo pack" link in Downloads. Regenerate
  it whenever a logo file is added, removed or replaced; it is not built
  automatically. Built with `Compress-Archive` (PowerShell) via a staging
  dir so Windows `desktop.ini` cruft doesn't end up inside it.
- `V2-Helicopters-Brand-Guidelines.pdf` — a separately designed print/PDF
  edition of the same brand guide: 14 pages, A4 landscape, cover + contents
  + one page per nav section (Logo and Typography span multiple pages since
  they carry more content). This is NOT the webpage printed to PDF — it's a
  dedicated layout (fixed-size `.page` canvases, its own print type scale,
  running header/footer with page numbers, big mono section-number
  watermarks) that reuses the same design tokens, chamfer/bracket-frame/
  mono-readout system, and logo SVGs as `brand-guidelines.html`.
- `brand-guidelines-print.html` — the source for the PDF above. Self-
  contained like the main file (same embedded font, same inlined images),
  but built from `pdf-export/template.html` (styles + shared SVG
  `<symbol>`/`<use>` defs) + `pdf-export/pages.html` (the 14 pages) rather
  than hand-edited directly. Don't edit this file by hand — edit the
  `pdf-export/` sources and rebuild, or your changes will be lost next
  rebuild.
- `pdf-export/` — the print edition's source + build scripts:
  `template.html` (CSS/tokens/symbols), `pages.html` (the 14 pages),
  `build.py` (assembles both + the font/photo/clear-space base64 pulled
  live from `brand-guidelines.html` into `brand-guidelines-print.html`),
  `render.py` (prints that HTML to the PDF via Playwright, launched against
  the local Chrome install with `channel="chrome"` — no browser download,
  but does need `pip install playwright`). Regenerate with:
  `python pdf-export/build.py && python pdf-export/render.py`.
  Gotcha: SVG `<use>` referencing a shared `<symbol>` does NOT let outside
  CSS reach in with descendant selectors (`.on-dark .logo-svg .ink` never
  matches, even though the identical-looking pattern works fine in the
  main file where SVGs are inlined directly). Colour switching in
  `pdf-export/template.html` instead uses bare class selectors (`.ink`,
  `.lime`) plus an inheritable `--ink-fill` custom property set by
  `.on-dark`/`.on-lime` on an ancestor — custom properties do cross the
  `<use>` shadow boundary. If you add a new on-dark/on-lime logo placement
  in the print pages and it renders black-on-black, this is why.

No `package.json`. Git repo: pushed to
[github.com/kreatiff/v2heli-brand-guide](https://github.com/kreatiff/v2heli-brand-guide)
(public, for GitHub Pages).

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
- The "no relative links, base64 only" rule is about assets *rendered on
  the page* (images, fonts). The Downloads section (`#downloads`) is the one
  deliberate exception: it links out to real files (`v2heli-logo-files.zip`,
  `fonts/V2helidisplay-Regular.ttf`) with plain relative `<a href download>`
  tags, since those are meant to be downloaded, not displayed. Don't inline
  those as data URIs.

## Visual design system ("precision instrument" direction)

The page went through a deliberate visual refresh (2026-08) to move away from
generic SaaS-template aesthetics (uniform 10px-radius cards, straight section
bands, pill buttons everywhere) toward a system grounded in the logomark's own
angular shear and an aviation technical-drawing feel. Follow this system for
any new UI added to the page rather than reverting to plain rounded rectangles:

- **Chamfered panels, not rounded rectangles.** Every card-like surface
  (`.logo-tile`, `.clearspace-card`, `.callout`, `.dont-card`,
  `.download-card`, `.overview-photo`, `.font-specimen-logo`, `.voice-col`,
  `.mockup`) uses a `clip-path` polygon that cuts one or two corners at an
  angle instead of `border-radius`. The chamfer size scales with the
  element (~14px for small chips, ~28-32px for large tiles). `.swatch` uses
  a full parallelogram shear instead, which predates this pass and set the
  precedent.
- **Chamfered buttons vs. pill chips.** Actionable buttons/links
  (`.mockup-cta`, `.download-btn`) get a single-corner chamfer, not
  `border-radius: 999px`. Non-interactive tags/chips (`.pill` in Brand
  personality, `.copy-btn` in Colour) stay full pills on purpose, that
  distinction (chamfer = action, pill = label) is intentional, keep it.
- **Mono readouts.** `--mono` token (system monospace stack, no new
  webfont) powers `.readout`, the eyebrow labels (`.eyebrow`,
  `.eyebrow-onlight`), `.download-meta`, `.swatch-index` and
  `.footer-text`, standing in for technical/spec-sheet annotations. Keep
  body copy on Space Grotesk; mono is only for these short UI labels.
- **Fig. numbering.** `#logo` and its `.logo-tile` elements auto-number via
  CSS counters (`counter-reset`/`counter-increment`, `Fig. 01`...). If you
  add or remove a `.logo-tile`, the numbering updates itself, no manual
  edits needed.
- **Bracket frame.** `.bracket-frame` draws a 4-corner viewfinder mark via
  layered `background-image` gradients (no extra markup). Used sparingly,
  only on the hero wordmark and the Primary logo tile, the two "flagship"
  moments. Don't apply it to every tile or it stops meaning anything.
  Gotcha: any element with `.bracket-frame` must set its background via
  `background-color`, not the `background` shorthand, since the shorthand
  resets `background-image` and silently deletes the brackets. This bit us
  once on `.logo-tile-light/-dark/-lime`.
- **Reveal-on-scroll.** `.reveal-io` + `.in-view` (toggled by an
  `IntersectionObserver` in the footer `<script>`) fades/rises content into
  view once per element. The hero instead uses a CSS-only `@keyframes
  reveal-up` staggered by `nth-child` on `.hero-inner`'s direct children,
  since it's above the fold and doesn't need scroll triggering. Both
  respect `prefers-reduced-motion`.
- Hero also carries a mono coordinate readout (`.hero-tag`, real Brisbane
  lat/long) and a dimension line with tick end-caps under the wordmark
  (`.hero-scale`), reinforcing the technical/instrument framing.

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
"don'ts" grid, the voice-and-tone do/don't section, and the nav-bar mockup in
"In use". (A nearest-Pantone note used to live in the Colour section, too;
removed on request, so don't re-add it without asking.) The
"precision instrument" visual system
above (chamfered panels, bracket framing, mono readouts, Fig. numbering) is
also mine, not the client's, layered on top of their actual colours/type/logo
facts. It's a legitimate interpretation of "Precise, Skilled, Engineered" from
their own personality list, but it's still an interpretation, flag it if the
client has a different visual reference in mind.

The print/PDF edition (`V2-Helicopters-Brand-Guidelines.pdf`,
`pdf-export/`) is entirely mine on top of that: the A4-landscape format,
the cover/contents/back-cover pages, the running header/footer and
big mono section-number watermarks, and the reworded Downloads page
(source files "requested from your project lead" instead of the
website's live download buttons, since a static PDF can't host a zip
download). None of that is client-specified — flag it if they expected
something closer to a literal print of the webpage, a portrait format,
or different page breaks.

## Loose ends

- `v2heli_logo_horizontal_bnw.svg` exists in `SVG/` but isn't used anywhere
  on the current page — there's no horizontal-lockup-on-lime placement yet.
- No test suite and no visual regression setup. The page was last verified
  manually with a throwaway Playwright + Chromium check (font loading,
  console errors, broken images, contrast, nav anchors) that isn't part of
  this repo. If you add real tooling, a lightweight Playwright smoke test
  (load the file, assert no console errors, assert fonts.check() for Space
  Grotesk) would be a reasonable start.

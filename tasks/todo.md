# astro-compat — build plan (2026-10-27)

- [x] Astro engine: JD/UTC via IANA tz (Intl), Sun/Moon/Mercury–Pluto longitudes (Schlyter elements + Moon perturbations), Ascendant/MC from LST, equal houses
- [x] Data: 12 signs (element, modality, ruler, keywords, Sun/Moon/Asc/Venus/Mars blurbs) CZ+EN; 62 cities with lat/lon/IANA tz
- [x] People: localStorage CRUD, 4 sample people preloaded, form (name, date, time, city or custom lat/lon/tz)
- [x] Views: Chart (SVG wheel + placements table), Traits (blurbs + element/modality balance), Compatibility (pair score + breakdown + commentary), Matrix (group heatmap)
- [x] i18n toggle CZ/EN, remembered per browser
- [x] Published: https://claude.ai/artifact/21W24LXPhH9q78sB7QJ3pd (v2); source in deliverables/astro-compat.html

## Review (2026-10-27)

Engine check, node, J2000 (2000-01-01 12:00 UT), diff vs reference in degrees:
sun 0.02 · moon 0.03 (vs independent Meeus ch.47 computation 223.32°; the 217.3° "reference" in the plan was my own error) · mercury 0.01 · venus 0.68 · mars 0.38 · jupiter 0.08 · saturn 0.03 · uranus 0.02 · neptune 0.01 · pluto 0.04.
Time zone: 1988-03-14 07:30 Prague → 06:30Z (CET), 1992-07-21 14:05 Prague → 12:05Z (CEST) — DST handled by Intl.
Rendered look (Chromium 1200px, chart tab): no console errors from the app; zodiac glyphs rendered as emoji → fixed by appending U+FE0E to every sign and planet glyph (v2).
Not verified: phone-width layout and dark theme were designed but not screenshotted; compatibility scoring is a stereotype heuristic with no external oracle.

Verification:
- Type: executable
- Check: run the engine on a known date in node — 2000-01-01 12:00 UTC Sun ≈ 280.5° (10° Capricorn), Moon ≈ 218° (Scorpio), + Ascendant for Prague 2000-01-01 12:00 UTC ≈ ~Taurus/Gemini sanity; artifact preview for overflow/console errors
- Pass condition: Sun/Moon within 1° of reference; all planets land in the known sign for the test date; no console errors
- Evidence: node output pasted in Review section below

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

## v3 (2026-10-27, later) — explanations, real towns, precise engine

- [x] Guide tab (CS/EN): natal chart basics, Big 3, planets, elements/modalities, houses, aspects, how the score is built, accuracy limits; "Stands for" column + house tooltips in the placements table; aspect list under the wheel; house themes on Traits
- [x] Gazetteer: `scripts/build_places.py` → `deliverables/places.json` (17,286 towns from GeoNames cities500: CZ/SK all ≥500, DE/AT/PL/HU ≥15k, world ≥50k, 284 zones, Czech aliases for 60 cities); type-ahead search with diacritics-insensitive matching; manual coordinates as explicit fallback (fixes the v2 dead end where a new person showed "Vlastní místo…" with the coordinate fields hidden)
- [x] Engine: astronomy-engine 2.1.19 from jsdelivr (fallback to the v1 formulas if blocked, footer says which); Placidus houses (equal above ±66° or by user choice)
- [x] Published v3: https://claude.ai/artifact/21W24LXPhH9q78sB7QJ3pd — files listing shows index.html 94 kB + places.json 1.09 MB

Review (v3):
- astronomy-engine vs independent Meeus Moon at J2000: 223.324° vs 223.32°; Sun 280.369° (ref 280.37°).
- Placidus: equator case collapses to equal-RA division (expected); Prague J2000 cusps strictly ordered 10→11→12→1→2→3; Eva's Ascendant 0°17′ Taurus unchanged vs v2 (0°18′).
- Browser run (Chromium 1440px): no app console errors; library loaded (footer "Engine: astronomy-engine 2.1.19"); unequal Placidus houses drawn; "kapl" → Kaplice, South Bohemian (CZ) 48.74/14.49 Europe/Prague, picked via Enter.
- Not verified: phone width, dark theme, CS guide rendering (same code path as EN), fallback-engine branch in the browser (only tested in node).

## v4 (2026-10-27, evening) — tooltips, compact card buttons, footer wording

- [x] Custom tooltip layer (`data-tip`, hover + keyboard focus + tap-to-pin on touch) on tabs, language buttons, add/restore, sample label, Big-3 pills, card buttons, person chips, every form field, chart table headers and cells, wheel (sign arcs, planets, house numbers, AC/MC), aspect rows, trait headings/terms/balance bars, score ring, verdict, factor points and aspect, matrix headers/cells/legend. ~60 CS + EN tooltip strings in `T.<lang>.tip`.
- [x] Card action buttons and pills smaller so CZ labels fit on one row at 430px
- [x] Footer: fallback clause removed from the disclaimer; the engine line explains the simplified model only when the library failed to load
- [x] Published v4 (version id 1793131262-e592)

## Publishing (2026-10-27, late) — GitHub Pages

- [x] Public repo https://github.com/tpavelek/astro-compat (personal account), `main` pushed
- [x] `.github/workflows/pages.yml`: wraps deliverables/astro-compat.html into _site/index.html, copies places.json, deploys via actions/deploy-pages. Pages site had to be created with the user token (`POST /repos/.../pages build_type=workflow`); the workflow's GITHUB_TOKEN cannot create it (`Resource not accessible by integration`).
- [x] Live: https://tpavelek.github.io/astro-compat/

Verification:
- Type: executable
- Check: `curl` of the live index and places.json after the deploy run succeeded; `<title>` read back from the served HTML
- Pass condition: both 200, places.json 1,088,542 B (same size as the local file), title "Astro Compat"
- Evidence: run 40592258490 succeeded; read-back printed `200 135416B`, `places.json 200 1088542B`, `<title>Astro Compat</title>`

## v6 (2026-10-27, late) — synastry, composite, transits

- [x] Aspect legend under the wheel + hover/tap pairing of lines and rows (v5.1)
- [x] Compatibility view switch: Rozbor | Synastrické kolo | Kompozit. Synastry = bi-wheel (A's chart and houses inside, B's planets outside, cross-aspects Sun–Saturn + AC with normal orbs, swap button) + cross-aspect list with hover pairing. Composite = midpoint chart (shorter-arc midpoints for every point, equal houses from the composite AC) with wheel, table, Sun/Moon/AC blurbs and aspects.
- [x] "Dnes / Today" tab: person chips + date picker (noon UTC of the chosen day), natal-inside/transits-outside bi-wheel, Moon-of-the-day pill, transit aspect list (orbs 3°, sextile 2°, natal Sun–Pluto + AC/MC vs transiting Sun–Pluto) sorted slow-first then by orb, each with a "that day × natal" reading and a fast/slow tag.
- [x] Guide: "Two charts together" bullets (synastry, composite, transits) in both languages
- [x] Refactor: placementsTable(), aspectsCard(), aspectRow(), wireAspectHover(), legendHTML(), biWheelSVG() shared by natal, composite, synastry and transit views
- [x] Published v6 (version id 1793134334-0407)

Review (v6): Chromium 1440px, CS. Today tab for Eva on 2026-10-27: outer ring places Sun early Scorpio, Pluto Aquarius, Neptune/Saturn at the Pisces–Aries border (matches the real sky); 13 transit aspects listed, slow ones first (Neptune □ Saturn 0.3° … Pluto □ AC 2.8°), then fast. Synastry Eva/Marek: both rings and cross lines drawn; Composite Eva+Marek: Sun 17° Capricorn, Moon 18° Aries, table and aspects render. No app console errors. Not verified: swap button, transit date change, phone width of the bi-wheel, composite midpoint vs a reference program.

## v5 (2026-10-27, night) — angles, points, highlights

- [x] DC and IC angles (v4.3); "for entertainment only" sentence removed (v4.1); footer merged into one paragraph (v4.2); tooltips removed from buttons/inputs/chips/matrix cells, tap tooltips auto-hide after 4 s (v4.4)
- [x] Points: mean North/South Node (Meeus 47.7), Black Moon Lilith (mean apogee), Part of Fortune (day/night formula); retrograde flags ℞ from a 1-day longitude difference; all in the table, on the wheel (except South Node) and in tooltips
- [x] "Chart highlights" card: chart ruler, Moon phase at birth (8 phases), retrograde planets, stelliums (≥3 planets per sign/house), hemisphere emphasis (above/below horizon, rising/setting half)
- [x] Guide: new section "Other points and highlights" (CS/EN); planets table lists the four points
- [x] Published v5 (version id 1793132964-0836)

Review (v5): node sanity — J2000 mean node 125.04° and Lilith 263.35° match Meeus; retrograde flags: Saturn ℞ on 2000-01-01 and Pluto ℞ on 1988-03-14 are both historically correct. Chromium 1200px, CS chart tab: 18-row table incl. nodes/Lilith/PoF/AC/DC/MC/IC, Pluto ℞ marked, highlights card (ruler Venus in Taurus house 1, Last Quarter 307°). No app console errors. Not verified: stellium branch (none of the 4 samples has one), phone width for the new card.

Review (v4): Chromium 430px, CS: "Horoskop / Upravit / Smazat" on one row; hovering Eva's Sun pill shows the 5-line tooltip (planet meaning, sign keywords, element, modality, ruler); console clean apart from favicon 404 of the local server. Not verified: touch pinning on a real phone, dark theme.

Verification:
- Type: executable
- Check: run the engine on a known date in node — 2000-01-01 12:00 UTC Sun ≈ 280.5° (10° Capricorn), Moon ≈ 218° (Scorpio), + Ascendant for Prague 2000-01-01 12:00 UTC ≈ ~Taurus/Gemini sanity; artifact preview for overflow/console errors
- Pass condition: Sun/Moon within 1° of reference; all planets land in the known sign for the test date; no console errors
- Evidence: node output pasted in Review section below

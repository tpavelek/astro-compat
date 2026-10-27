# astro-compat — Changelog

Work completed by this agent, newest first.

## 2026-10-27 — [auto] built and published Astro Compat demo app (CZ/EN)

Scaffolded the astro-compat project and wrote a single-file, no-backend HTML app at deliverables/astro-compat.html (people store in browser, natal chart wheel with Ascendant/MC/houses, sign-based traits, pairwise compatibility score). Engine positions were checked against an independent Meeus computation (all 10 bodies within 0.7 deg); fixed zodiac glyphs rendering as emoji by adding U+FE0E, then published as a private Claude artifact.

Followed up with v3 of the same artifact: added a bilingual Guide tab and "stands for" column/aspect list for explanations, replaced the city dropdown with a type-ahead search over 17,286 GeoNames towns (CZ/SK >=500 inhabitants, DE/AT/PL/HU >=15k, world >=50k; no map because artifact CSP blocks tiles/geocoding), and swapped simplified formulas for astronomy-engine with Placidus houses. Republished at the same artifact link; the in-session verification was not independently re-read for this entry.

v4: shrank card buttons/pills (Czech labels fit one row at 430 px, checked in Chromium), added a custom tooltip layer (hover, focus, tap-to-pin) with ~60 bilingual strings covering tabs, form fields, chart, aspects and score, added a "for entertainment only" footer line, and made the engine footer state astronomy-engine 2.1.19 / Placidus (fallback wording only if the library fails to load). Republished as a new artifact link; committed as 1b581e1.

# astro-compat

Demo single-page web app: natal chart basics (Sun/Moon/Ascendant + planets), multiple people, stereotype traits, pairwise compatibility. CZ + EN.

## Metadata
- **Category:** personal
- **Status:** active
- **Created:** 2026-10-27
- **Type:** code

## Purpose

Show how quickly a small, polished, bilingual app can be prepared. Astrology is pop-astrology level — computed positions should be in the right sign, but no house-system rigour or scientific claims. Success: a shareable link where someone can add a few people with birth date/time/place, see their Big 3 + planet signs on a chart wheel, read trait blurbs, and compare any two people (plus a group matrix), switching CZ/EN at any time.

## Inputs Processing

On session start:
1. Scan `inputs/` for files not listed in `inputs/.processed.md`
2. For each new file: extract content, create `knowledge/<filename-slug>.md`
3. Log in `inputs/.processed.md` with timestamp
4. Update `knowledge/README.md` navigation map

Supported: PDF, DOCX, PPTX, XLSX, TXT, HTML, MHTML, images, CSV, JSON.
For URLs: maintain `inputs/urls.txt` (one per line), fetch and summarize.

If processing fails for any file, log as "(failed: reason)" in .processed.md
and continue with remaining files. Never block on a single failure.

## Workflow

1. **Spec** — Define requirements
2. **Design** — Architecture decisions, documented in knowledge/
3. **Build** — Implement in phases
4. **Test** — Verify each phase
5. **Ship** — Final review, merge, deploy

## Key Files

| Path | Description |
|------|-------------|
| `deliverables/astro-compat.html` | The app (single self-contained file) |
| `knowledge/README.md` | Knowledge navigation map |

## Active Decisions

- Single self-contained HTML/JS file, published as a claude.ai artifact; people stored per browser (localStorage) with sample people preloaded.
- Planet positions from simplified Meeus/VSOP-lite formulas in JS (sign-level accuracy is enough); Ascendant from local sidereal time + latitude; houses = equal houses from the Ascendant.
- Compatibility = weighted blend of element/modality affinity and Sun/Moon/Venus/Mars cross-aspects, scaled 0–100 with stereotype commentary.

## Domain Learnings

<!-- Claude: append findings here as you discover them.
     Keep entries concise (1-2 lines). Group by topic.
     Include source references: [source: analysis name]
     Max ~100 lines. If a topic exceeds 10 entries, summarize.
     If section exceeds ~100 lines, split to knowledge/learnings/<topic>.md -->

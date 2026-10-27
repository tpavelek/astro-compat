#!/usr/bin/env python3
"""Build deliverables/places.json from GeoNames cities500.txt (CC BY 4.0, https://www.geonames.org).

Tiers: CZ+SK all rows (>=500 inhabitants); DE/AT/PL/HU >= 15k; everywhere else >= 50k.
Output: {"tz":[iana...], "p":[[name, ascii_or_empty, cc, admin1, lat, lon, tzIdx, pop, aliases_or_empty], ...]}
sorted by population desc so prefix search can rank by index.
Run:  python3 scripts/build_places.py temp/cities500.txt temp/admin1CodesASCII.txt deliverables/places.json
"""
import csv, json, sys, unicodedata

src, adm, out = sys.argv[1:4]
NEIGHBOURS = {"DE", "AT", "PL", "HU"}
# Czech names for cities whose GeoNames main name is English/local. alias -> (geonames name, cc)
ALIASES = {
    "Praha": ("Prague", "CZ"), "Vídeň": ("Vienna", "AT"), "Mnichov": ("Munich", "DE"), "Berlín": ("Berlin", "DE"),
    "Hamburk": ("Hamburg", "DE"), "Drážďany": ("Dresden", "DE"), "Lipsko": ("Leipzig", "DE"), "Norimberk": ("Nuremberg", "DE"),
    "Kolín nad Rýnem": ("Köln", "DE"), "Frankfurt": ("Frankfurt am Main", "DE"), "Varšava": ("Warsaw", "PL"), "Krakov": ("Kraków", "PL"),
    "Vratislav": ("Wrocław", "PL"), "Budapešť": ("Budapest", "HU"), "Paříž": ("Paris", "FR"), "Londýn": ("London", "GB"),
    "Řím": ("Rome", "IT"), "Milán": ("Milan", "IT"), "Benátky": ("Venice", "IT"), "Neapol": ("Naples", "IT"), "Florencie": ("Florence", "IT"),
    "Curych": ("Zürich", "CH"), "Ženeva": ("Geneva", "CH"), "Brusel": ("Brussels", "BE"), "Kodaň": ("Copenhagen", "DK"),
    "Lisabon": ("Lisbon", "PT"), "Atény": ("Athens", "GR"), "Moskva": ("Moscow", "RU"), "Petrohrad": ("Saint Petersburg", "RU"),
    "Kyjev": ("Kyiv", "UA"), "Lublaň": ("Ljubljana", "SI"), "Záhřeb": ("Zagreb", "HR"), "Bělehrad": ("Belgrade", "RS"),
    "Bukurešť": ("Bucharest", "RO"), "Sofie": ("Sofia", "BG"), "Káhira": ("Cairo", "EG"), "Peking": ("Beijing", "CN"),
    "Šanghaj": ("Shanghai", "CN"), "Tokio": ("Tokyo", "JP"), "Soul": ("Seoul", "KR"), "Dillí": ("Delhi", "IN"), "Bombaj": ("Mumbai", "IN"),
    "Mexiko": ("Mexico City", "MX"), "Jeruzalém": ("Jerusalem", "IL"), "Helsinky": ("Helsinki", "FI"), "Stockholm": ("Stockholm", "SE"),
    "Edinburgh": ("Edinburgh", "GB"), "Štýrský Hradec": ("Graz", "AT"), "Linec": ("Linz", "AT"), "Solnohrad": ("Salzburg", "AT"),
    "Řezno": ("Regensburg", "DE"), "Pasov": ("Passau", "DE"), "Cáchy": ("Aachen", "DE"), "Mohuč": ("Mainz", "DE"), "Štrasburk": ("Strasbourg", "FR"),
    "Bratislava": ("Bratislava", "SK"), "Vilnius": ("Vilnius", "LT"), "Riga": ("Riga", "LV"), "Tallin": ("Tallinn", "EE"), "Dublin": ("Dublin", "IE"),
}
alias_by_key = {}
for a, (n, cc) in ALIASES.items():
    alias_by_key.setdefault((n, cc), []).append(a)

admin1 = {}
with open(adm, encoding="utf-8") as f:
    for line in f:
        code, name, _ascii, _id = line.rstrip("\n").split("\t")
        admin1[code] = name

def strip(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

tz_list, tz_idx, rows = [], {}, []
with open(src, encoding="utf-8", newline="") as f:
    for r in csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
        name, ascii_, cc, a1, lat, lon, tz, pop = r[1], r[2], r[8], r[10], float(r[4]), float(r[5]), r[17], int(r[14] or 0)
        if cc in ("CZ", "SK"):
            pass
        elif cc in NEIGHBOURS:
            if pop < 15000: continue
        elif pop < 50000:
            continue
        if not tz: continue
        if tz not in tz_idx:
            tz_idx[tz] = len(tz_list); tz_list.append(tz)
        a1name = admin1.get(f"{cc}.{a1}", "")
        if cc in ("CZ", "SK"):  # region names are long; keep short "kraj" form
            a1name = a1name.replace(" Region", "").replace("Region ", "")
        ali = alias_by_key.get((name, cc), [])
        asc = "" if strip(name).lower() == ascii_.lower() else ascii_
        rows.append([name, asc, cc, a1name, round(lat, 3), round(lon, 3), tz_idx[tz], pop, "|".join(ali)])

rows.sort(key=lambda x: -x[7])
missing = [a for (n, cc), al in alias_by_key.items() for a in al if not any(r[0] == n and r[2] == cc for r in rows)]
if missing:
    print("WARNING aliases without a matching row:", missing, file=sys.stderr)
with open(out, "w", encoding="utf-8") as f:
    json.dump({"tz": tz_list, "p": rows}, f, ensure_ascii=False, separators=(",", ":"))
print(f"{len(rows)} places, {len(tz_list)} zones -> {out}")

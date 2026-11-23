"""Good Culture decks: build, brand-check and finalise a deck from a short spec.

    python3 tools/make.py build    SPEC.json OUT      build the slides from the library
    python3 tools/make.py check    OUT                render, brand check, contact sheet (OUT/sheet-*.png)
    python3 tools/make.py blobs    OUT /_blob/... /_blob/...   the upload_asset urls, in upload.json order
    python3 tools/make.py finalize OUT BLOBS.json "Deck title"

SPEC.json: {"name": "Deck name for the footer", "slides": [ {"from": "<component id>", ...changes}, ... ]}
Every slide starts from a slide in the component library (library/specs.py, COMPONENTS) and changes only its words,
its chapter colour, its photo or its swirl. That keeps every deck inside the approved designs.
"""
import os as _os
GCW = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))) + "/"
REPO = GCW
import sys, json, copy, re, asyncio, datetime
sys.path.insert(0, GCW + "tools"); sys.path.insert(0, GCW + "library")

FONTS = {"font-regular": "engram-regular", "font-bold": "engram-bold", "font-extrabold": "engram-extrabold", "font-medium": "engram-medium"}
# Every colour a slide may use: the five chapter pairs, brand yellow, ink, white, cream and the greys the recipes use.
ALLOWED = {"#000000", "#ffffff", "#fbe405", "#f3f2ee", "#e2ded3", "#00bbec", "#253081", "#13b89e", "#134151", "#d46a9f",
           "#4a2580", "#ed8e01", "#bb4b05", "#bfd730", "#004428", "#0b0b0b", "#0c0c0c", "#1d1d1b", "#333333", "#3a3a3a",
           "#4a4a4a", "#6b6b6b", "#8a8a8a", "#bdbdbd", "#c8c8c8", "#d8d8d8", "#0b96d1", "#00b2e7", "#f39200", "#160", "#169"}


def catalogue():
    import specs
    return {s["id"]: s for s in specs.COMPONENTS["slides"]}


def photo(src, slug):
    """A library photo for this deck only: plates/photos/_deck-<slug>.jpg (half slides) and full-_deck-<slug>.jpg."""
    from PIL import Image, ImageOps
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB"); name = f"_deck-{slug}"
    if min(im.size) < 900: sys.exit(f"{src} is too small for a slide ({im.size[0]}x{im.size[1]}); pick a bigger picture")
    for fn, size in ((name, (1200, 1211)), ("full-" + name, (1920, 969))):
        ImageOps.fit(im, size, Image.LANCZOS).save(f"{GCW}plates/photos/{fn}.jpg", quality=84, optimize=True)
    return name


def build(spec_path, out):
    if not _os.path.exists(GCW + "ds/project/fonts/engram-regular.woff2"):
        sys.exit("fonts are locked: run  python3 tools/make.py unlock <key>  first (the key is in the deck skill)")
    import gdeck
    spec = json.load(open(spec_path)); cat = catalogue(); slides = []; seen = {}
    for i, s in enumerate(spec["slides"], 1):
        if "from" in s:
            if s["from"] not in cat: sys.exit(f"slide {i}: no component called {s['from']!r}")
            base = copy.deepcopy(cat[s["from"]]); base.update({k: v for k, v in s.items() if k != "from"})
        else:
            sys.exit(f"slide {i}: every slide must start from a library component (\"from\": ...)")
        base["_meta"] = {"from": s["from"], "chapter": base.get("chapter"), "library_photo": "photo_file" in base, "swirl": "sw" in base}
        if "photo_file" in base:  # a picture from the SharePoint image library, saved locally
            import re as _re
            base["photo"] = photo(base.pop("photo_file"), _re.sub(r"[^a-z0-9]+", "-", f"{spec['name']}-{i}".lower()).strip("-"))
        sid = base.get("id"); seen[sid] = seen.get(sid, 0) + 1
        if seen[sid] > 1: base["id"] = f"{sid}-{seen[sid]}"
        slides.append(base)
    meta = [s.pop("_meta") for s in slides]
    order = gdeck.build({"name": spec["name"], "slides": slides}, out)
    assets = dict(gdeck.ASSETS)
    for k, f in FONTS.items(): assets[k] = f"{GCW}ds/project/fonts/{f}.woff2"
    missing = [p for p in assets.values() if not _os.path.exists(p)]
    if missing: sys.exit("this combination needs art the library doesn't have (pick another chapter or swirl):\n" + "\n".join(missing))
    json.dump({"order": order, "recipes": [s["r"] for s in slides], "meta": meta, "assets": assets, "name": spec["name"]}, open(f"{out}/build.json", "w"), indent=1)
    used = set()
    for sid in order:
        h = open(f"{out}/project/slides/{sid}.html").read(); used |= set(re.findall(r"\{\{([^}]+)\}\}", h))
    up = [{"name": k + _os.path.splitext(p)[1], "path": p} for k, p in assets.items() if k in used or k in FONTS]
    json.dump(up, open(f"{out}/upload.json", "w"), indent=1)
    print(f"built {len(order)} slides; {len(up)} files to upload (OUT/upload.json)")


CSS = "".join(f"@font-face{{font-family:'{fam}';src:url(file://{GCW}ds/project/fonts/{f}.woff2)}}" for fam, f in
              [("Engram", "engram-regular"), ("Engram Bold", "engram-bold"), ("Engram ExtraBold", "engram-extrabold"), ("Engram Medium", "engram-medium")])
CSS += ("body{margin:0} section{position:relative;width:1920px;height:1080px;overflow:hidden;box-sizing:border-box}"
        "section *{margin:0;box-sizing:content-box} aside{display:none} x-icon{display:inline-block;background:currentColor;border-radius:4px}")

JS = r"""() => {
  const P = [], sec = document.querySelector('section'), R = sec.getBoundingClientRect();
  const ok = new Set(['Engram','Engram Bold','Engram ExtraBold','Engram Medium']);
  for (const el of sec.querySelectorAll('*')) {
    const cs = getComputedStyle(el), r = el.getBoundingClientRect();
    if (cs.display === 'none' || r.width === 0) continue;
    const own = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (own) {
      const fam = cs.fontFamily.split(',')[0].replace(/['"]/g, '').trim();
      if (!ok.has(fam)) P.push(`font "${fam}" on "${el.textContent.trim().slice(0, 40)}"`);
      if (r.right > R.right + 2 || r.bottom > R.bottom + 2 || r.left < R.left - 2 || r.top < R.top - 2)
        P.push(`text runs off the slide: "${el.textContent.trim().slice(0, 40)}"`);
      if (el.scrollWidth > el.clientWidth + 4 && cs.overflow !== 'visible') P.push(`text cut off: "${el.textContent.trim().slice(0, 40)}"`);
    }
    const bg = cs.backgroundColor.match(/\d+/g);
    if (bg && (bg[3] === undefined || +bg[3] > 0.9) && +bg[0] < 40 && +bg[1] < 40 && +bg[2] < 40 && r.width >= 1700 && r.height >= 900)
      P.push('black slide background (black only goes in a panel on colour)');
    if (el.tagName === 'IMG' && !el.naturalWidth) P.push(`picture missing: ${el.getAttribute('src')}`);
    if (el.tagName === 'IMG' && !/^file:\/\//.test(el.getAttribute('src') || '')) P.push(`picture from outside the library: ${el.getAttribute('src')}`);
  }
  const T = [...sec.querySelectorAll('*')].filter(el => [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()) && getComputedStyle(el).display !== 'none' && el.textContent.trim().length > 1);
  const hasFooter = /Page \d/.test(sec.innerText);
  for (const el of T) {
    const r = el.getBoundingClientRect();
    if (hasFooter && r.top < R.top + 969 - 4 && r.bottom > R.top + 969 + 4) P.push(`text crosses into the footer: "${el.textContent.trim().slice(0, 40)}"`);
  }
  for (let i = 0; i < T.length; i++) for (let j = i + 1; j < T.length; j++) {
    const a = T[i], b = T[j]; if (a.contains(b) || b.contains(a)) continue;
    const r = a.getBoundingClientRect(), q = b.getBoundingClientRect();
    const ox = Math.min(r.right, q.right) - Math.max(r.left, q.left), oy = Math.min(r.bottom, q.bottom) - Math.max(r.top, q.top);
    if (ox > 6 && oy > 6) P.push(`text overlaps: "${a.textContent.trim().slice(0, 30)}" and "${b.textContent.trim().slice(0, 30)}"`);
  }
  const t = sec.innerText;
  if (/—/.test(t)) P.push('em dash in the copy');
  if (/ – /.test(t)) P.push('dash used as punctuation in the copy');
  if (/\b(it'?s|this is|that'?s) not (just )?[^.]{1,60}[,;] (it'?s|but)\b/i.test(t)) P.push('"it\'s not X, it\'s Y" construction in the copy');
  return P;
}"""

CHAP = {(0x00, 0xbb, 0xec): "sky", (0x13, 0xb8, 0x9e): "teal", (0xd4, 0x6a, 0x9f): "pink", (0xed, 0x8e, 0x01): "orange", (0xbf, 0xd7, 0x30): "lime"}


def ground(png):
    from PIL import Image
    im = Image.open(png).convert("RGB").resize((192, 108)); px = list(im.getdata()); best = (None, 0)
    for c, name in CHAP.items():
        n = sum(1 for p in px if abs(p[0] - c[0]) + abs(p[1] - c[1]) + abs(p[2] - c[2]) < 40)
        if n > best[1]: best = (name, n)
    return best[0] if best[1] > len(px) * 0.3 else None


async def _check(out):
    from playwright.async_api import async_playwright
    b = json.load(open(f"{out}/build.json")); os = _os; os.makedirs(f"{out}/prev", exist_ok=True); fails = []; notes = []; grounds = []
    async with async_playwright() as p:
        exe = "/usr/bin/google-chrome" if os.path.exists("/usr/bin/google-chrome") else None
        br = await p.chromium.launch(executable_path=exe) if exe else await p.chromium.launch()
        pg = await br.new_page(viewport={"width": 1920, "height": 1080})
        for i, sid in enumerate(b["order"], 1):
            h = open(f"{out}/project/slides/{sid}.html").read()
            for hx in set(x.lower() for x in re.findall(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b", h)):
                if hx not in ALLOWED: fails.append(f"{i} {sid}: colour {hx} is not in the palette")
            for k, v in b["assets"].items(): h = h.replace("{{" + k + "}}", "file://" + v)
            if "{{" in h: fails.append(f"{i} {sid}: missing picture")
            open("/tmp/_gcprev.html", "w").write(f"<html><head><style>{CSS}</style></head><body>{h}</body></html>")
            await pg.goto("file:///tmp/_gcprev.html"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(150)
            fails += [f"{i} {sid}: {m}" for m in await pg.evaluate(JS)]
            png = f"{out}/prev/{i:02d}-{sid}.png"; await pg.screenshot(path=png); grounds.append(ground(png))
        await br.close()
    for i in range(1, len(grounds)):
        rc = b.get("recipes", [""] * len(grounds))
        if {rc[i - 1], rc[i]} & {"divider", "cover", "contents", "close"}: continue  # dividers open their chapter's colour
        if grounds[i] and grounds[i] == grounds[i - 1]:
            notes.append(f"{i + 1} {b['order'][i]}: second full-{grounds[i]} slide in a row; a quiet slide between would calm it")
    f2, n2 = quality(b, grounds); fails += f2; notes += n2
    sheet(out, b["order"])
    return fails, notes


FRAME = {"divider", "cover", "contents", "close"}


def quality(b, grounds):
    """What a good deck has, beyond the brand rules (SKILL.md, 'What good looks like'). Fixed colours fail; the rest are notes."""
    fails, notes = [], []
    meta, rc, order = b.get("meta"), b.get("recipes", []), b["order"]
    if not meta: return fails, notes
    fixed = json.load(open(GCW + "library/fixed.json")); quiet = json.load(open(GCW + "library/grounds.json"))
    body = [i for i in range(len(order)) if rc[i] not in FRAME]
    # A slide whose colour is in its art must sit in a chapter of that colour.
    for i, m in enumerate(meta):
        want = fixed.get(m["from"])
        if want and m["chapter"] and m["chapter"] != want:
            fails.append(f"{i + 1} {order[i]}: always {want}, but its chapter is {m['chapter']}; put it in a {want} chapter or pick another slide")
    # Chapters: runs of body slides sharing a chapter colour. Each wants a quiet slide and something with energy.
    runs, prev_c, prev_i = [], None, None
    for i in body:
        c = meta[i]["chapter"] or prev_c  # a slide with no chapter (a full photo, white certs) belongs to the one it sits in
        divider_between = prev_i is not None and any(rc[k] == "divider" for k in range(prev_i + 1, i))
        if not runs or c != prev_c or divider_between: runs.append([])
        runs[-1].append(i); prev_c, prev_i = c, i
    for run in runs:
        if len(run) < 2: continue
        name = meta[run[0]]["chapter"] or "untitled"
        if not any(quiet.get(meta[i]["from"], "quiet" if grounds[i] is None else "colour") == "quiet" for i in run):
            notes.append(f"{run[0] + 1}-{run[-1] + 1}: the {name} chapter has no quiet slide (white, cream or photo)")
        if all(quiet.get(meta[i]["from"]) == "quiet" for i in run):
            notes.append(f"{run[0] + 1}-{run[-1] + 1}: the {name} chapter has no full-colour slide; it will read flat")
    # The deck as a whole.
    if len(body) >= 5 and not any(meta[i]["swirl"] and grounds[i] for i in body):
        notes.append("no swirl slide: a deck this long wants at least one (steps, icons, What's inside, m-photo, m-halves, s-next, s-supply)")
    if not any(m["library_photo"] for m in meta):
        notes.append("no pictures from the image library: check SharePoint for photos that fit better than the built-in ones (SKILL.md, step 2)")
    for i in range(1, len(order)):
        if meta[i]["from"] == meta[i - 1]["from"] or (rc[i] == rc[i - 1] and rc[i] not in ("page", "divider")):
            notes.append(f"{i + 1} {order[i]}: same layout as the slide before")
    return fails, notes


def sheet(out, order):
    from PIL import Image, ImageDraw
    files = [f"{out}/prev/{i:02d}-{s}.png" for i, s in enumerate(order, 1)]
    for k in range(0, len(files), 12):
        part = files[k:k + 12]; rows = (len(part) + 2) // 3
        im = Image.new("RGB", (3 * 640 + 40, rows * 380 + 20), "white"); d = ImageDraw.Draw(im)
        for j, f in enumerate(part):
            x, y = 10 + (j % 3) * 650, 10 + (j // 3) * 380
            im.paste(Image.open(f).resize((640, 360)), (x, y)); d.text((x + 6, y + 6), str(k + j + 1), fill="black")
        im.save(f"{out}/sheet-{k // 12 + 1}.png")


def finalize(out, blobs_path, title):
    b = json.load(open(f"{out}/build.json")); B = json.load(open(blobs_path)); files = []
    for sid in b["order"]:
        h = open(f"{out}/project/slides/{sid}.html").read()
        for k in b["assets"]:
            if "{{" + k + "}}" in h: h = h.replace("{{" + k + "}}", B[k])
        assert "{{" not in h, sid
        open(f"{out}/out-{sid}.html", "w").write(h); files.append({"as": f"project/slides/{sid}.html", "path": f"{out}/out-{sid}.html"})
    deck = {"v": 5, "createdOnFiles": {"v": 1, "at": datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")}, "lists": "css",
            "format": {"v": 1, "shared": ["project/deck.css"]}, "title": title, "cover": b["order"][0], "order": b["order"],
            "sections": {"s1": {"description": title + ".", "start": b["order"][0]}},
            "faces": {"engram": {"family": "Engram", "src": B["font-regular"]}, "engram-bold": {"family": "Engram Bold", "src": B["font-bold"]},
                      "engram-extrabold": {"family": "Engram ExtraBold", "src": B["font-extrabold"]},
                      "engram-medium": {"family": "Engram Medium", "src": B["font-medium"]}}, "designSystems": []}
    json.dump(deck, open(f"{out}/deck.json", "w"), indent=1)
    open(f"{out}/deck.css", "w").write("section { font-family: Engram, Arial, sans-serif; color: #000000; }\n")
    files = [{"as": "project/deck.json", "path": f"{out}/deck.json"}, {"as": "project/deck.css", "path": f"{out}/deck.css"}] + files
    json.dump(files, open(f"{out}/publish.json", "w"), indent=1)
    print(f"ready: {len(files)} files (OUT/publish.json)")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "unlock":  # the Engram fonts are licensed, so they are kept locked; the key is in the deck skill
        import subprocess, glob
        for f in glob.glob(GCW + "ds/project/fonts/*.woff2.enc"):
            r = subprocess.run(["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-in", f, "-out", f[:-4], "-pass", "pass:" + sys.argv[2]], capture_output=True)
            if r.returncode:
                for g in glob.glob(GCW + "ds/project/fonts/*.woff2"): _os.remove(g)
                sys.exit("wrong key: the fonts didn't unlock")
        print("fonts unlocked")
    elif cmd == "build": build(sys.argv[2], sys.argv[3])
    elif cmd == "check":
        f, n = asyncio.run(_check(sys.argv[2]))
        if n: print("Notes (not failures):\n" + "\n".join(n))
        print("\n".join(f) if f else "BRAND CHECK PASSED"); sys.exit(1 if f else 0)
    elif cmd == "blobs":  # the /_blob urls upload_asset returned, in upload.json order
        up = json.load(open(f"{sys.argv[2]}/upload.json")); urls = sys.argv[3:]
        if len(urls) != len(up): sys.exit(f"got {len(urls)} urls for {len(up)} files")
        json.dump({_os.path.splitext(u["name"])[0]: v for u, v in zip(up, urls)}, open(f"{sys.argv[2]}/blobs.json", "w"), indent=1)
        print("wrote blobs.json")
    elif cmd == "finalize": finalize(sys.argv[2], sys.argv[3], sys.argv[4])

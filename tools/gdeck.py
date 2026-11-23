"""Good Culture deck builder: a deck is a list of slide specs, each one a recipe on one of the approved backgrounds.

Recipes (the rules live here, so every deck follows them):
  cover     ribbon cover, title set along the ribbon, label + date + stacked logo
  divider   ribbon divider on the chapter's light colour, up to 3 title lines on the ribbon
  contents  'drinks' background: numbered list left, drinks right
  statement 'drinks' background: headline, standfirst, body and/or ring bullets, all left of the art
  panel     'quiet' background (one ingredient bottom left): headline + standfirst top left,
            content block on the right: table | points | stats
  halves    light half / dark half: words left, points or bar chart in the dark half under the squiggle
  band      headline over a dark band, three facts in the band, drinks crossing the seam on the right
  steps     plain chapter colour: four black step panels with yellow number badges
  close     ribbon close with contact details
A chapter = one colour pair, used for every slide until the next divider.
"""
import os as _os
GCW = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))) + "/"
REPO = GCW
import json, sys, html as H
sys.path.insert(0, GCW + "tools")
import curve

W = GCW + ""
PAIRS = {"sky": ("#00bbec", "#253081"), "teal": ("#13b89e", "#134151"), "pink": ("#d46a9f", "#4a2580"),
         "orange": ("#ed8e01", "#bb4b05"), "lime": ("#bfd730", "#004428")}
Y, INK, WHITE = "#fbe405", "#000000", "#ffffff"
FX = "'Engram ExtraBold', Arial, sans-serif"
FR = "Engram, Arial, sans-serif"
# background plates: kind -> plate numbers, and how far right the words may run (x where the art starts)
DRINKS = {23: 960, 26: 1220, 27: 1080, 28: 1240, 31: 1340, 87: 820, 90: 940}
QUIET = [76, 77, 78, 79, 80, 84]          # ingredient sits bottom left, x 330-800, from y 560
ASSETS = {}                               # name -> local path (uploaded per deck)


def asset(name, path):
    ASSETS[name] = path
    return "{{" + name + "}}"


def plate(kind, n, chap):
    return asset(f"{kind}-{n}-{chap}", f"{W}plates/kit/{kind}-{n}-{chap}.jpg")


def esc(t):
    return t if ("<" in t or "&" in t) else H.escape(t, quote=False)


def h2(t, x=78, y=76, w=1100, col=INK):
    return (f'<h2 style="position:absolute;left:{x}px;top:{y}px;width:{w}px;font-family:{FX};font-weight:400;'
            f'font-size:64px;line-height:1.05;letter-spacing:-1px;color:{col}">{esc(t)}</h2>')


def footer(deck, n):
    return (f'<img src="{asset("wm-ink", W + "ds/project/assets/Logos/wordmark-ink.png")}" alt="Good Culture" '
            f'style="position:absolute;left:78px;top:1009px;width:397px;height:31px;object-fit:contain">'
            f'<p style="position:absolute;left:942px;top:1010px;width:900px;text-align:right;white-space:nowrap;font-family:{FR};'
            f'font-size:24px;color:{INK}">{esc(deck)} &#160;|&#160; Page {n:02d}</p>')


def ring_list(items, col=INK, w=700, size=26):
    rows = "".join(
        f'<div style="display:flex;gap:18px;align-items:flex-start"><div style="width:13px;height:13px;flex:none;'
        f'border:4px solid {col};border-radius:50%;margin-top:{round(size * 0.42)}px"></div>'
        f'<p style="font-family:{FR};font-size:{size}px;line-height:1.4;color:{col};width:{w}px">{esc(t)}</p></div>'
        for t in items)
    return f'<div style="display:flex;flex-direction:column;gap:14px">{rows}</div>'


def col_block(x, y, w, parts, gap=28):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;display:flex;flex-direction:column;gap:{gap}px">{"".join(parts)}</div>'


def standfirst(t, w, col=INK, size=30):
    return f'<p style="font-family:{FX};font-size:{size}px;line-height:1.3;color:{col};width:{w}px">{esc(t)}</p>'


def body(t, w, col=INK, size=26):
    return f'<p style="font-family:{FR};font-size:{size}px;line-height:1.45;color:{col};width:{w}px">{esc(t)}</p>'


def section(sid, bg, inner, notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{bg};color:{INK};font-family:{FR};padding:0px">\n'
            f'{inner}\n<aside>{esc(notes)}</aside>\n</section>\n')


def full_bg(src):
    return f'<img src="{src}" alt="" style="position:absolute;left:0px;top:0px;width:1920px;height:1080px;object-fit:cover">'


# ---------------- recipes ----------------
def r_cover(s, deck, n):
    lines = s["title"]; assert len(lines) == 3, "cover titles always fill all three ribbon lines"
    inner = (full_bg(asset("cover-art", W + "ds/project/assets/Shapes/cover-art.webp"))
             + curve.html("cover", [(i, t, 0.5) for i, t in enumerate(lines)], size=s.get("size", 128))
             + f'<p style="position:absolute;left:1451px;top:700px;width:440px;font-family:{FX};font-size:32px;line-height:1.3;color:{INK}">'
               f'<span style="background:{Y}">&#160;{esc(s["label"])}&#160;</span></p>'
             + f'<p style="position:absolute;left:1451px;top:770px;width:440px;font-family:{FR};font-size:30px;color:{INK}">{esc(s["date"])}</p>'
             + f'<img src="{asset("logo-ink", W + "ds/project/assets/Logos/logo-ink.svg")}" alt="Good Culture" style="position:absolute;left:1451px;top:880px;width:405px;height:121px;object-fit:contain">')
    return section(s["id"], "#00b2e7", inner, "Cover (recipe: cover). Jim's ribbon artwork; the title is set letter by letter along the ribbon.")


def r_divider(s, deck, n, chap):
    lines = s["title"]; assert len(lines) == 3, "divider titles always fill three ribbon lines"
    inner = (full_bg(asset("divider-art", W + "ds/project/assets/Shapes/divider-art.webp"))
             + curve.html("divider", [(i, t, 0.5) for i, t in enumerate(lines)], size=s.get("size", 128))
             + f'<img src="{asset("wm-ink", W + "ds/project/assets/Logos/wordmark-ink.png")}" alt="Good Culture" style="position:absolute;left:72px;top:993px;width:443px;height:39px;object-fit:contain">')
    return section(s["id"], PAIRS[chap][0], inner, f"Section divider (recipe: divider) in the chapter colour ({chap}). Every slide until the next divider uses this colour.")


def r_contents(s, deck, n, chap):
    p = s.get("plate", 87); xmax = DRINKS[p]
    rows = "".join(
        f'<div style="display:flex;gap:28px;align-items:center"><div style="width:60px;height:60px;flex:none;border-radius:50%;background:{INK};display:flex;align-items:center;justify-content:center">'
        f'<p style="font-family:{FX};font-size:24px;line-height:1;color:{Y}">{i + 1:02d}</p></div>'
        f'<p style="font-family:{FX};font-size:38px;line-height:1.15;color:{INK};width:{xmax - 260}px">{esc(t)}</p></div>'
        for i, t in enumerate(s["items"]))
    inner = (full_bg(plate("drinks", p, chap)) + h2("Contents", w=xmax - 160)
             + f'<div style="position:absolute;left:78px;top:250px;width:{xmax - 160}px;display:flex;flex-direction:column;gap:30px">{rows}</div>'
             + footer(deck, n))
    return section(s["id"], WHITE, inner, "Contents (recipe: contents). Up to eight items, numbered in black circles.")


def r_statement(s, deck, n, chap):
    p = s.get("plate", 23); xmax = DRINKS[p]; w = min(xmax - 160, 1000)
    parts = [h2(s["title"], x=0, y=0, w=w).replace("position:absolute;left:0px;top:0px;", "")]
    if s.get("standfirst"): parts.append(standfirst(s["standfirst"], w))
    if s.get("body"): parts.append(body(s["body"], w))
    if s.get("bullets"): parts.append(ring_list(s["bullets"], w=w - 40))
    inner = full_bg(plate("drinks", p, chap)) + col_block(78, 76, w, parts) + footer(deck, n)
    return section(s["id"], WHITE, inner, "Statement (recipe: statement). Words stay left of the drinks.")


def table(rows, w, first=300):
    def cell(t, bold, last):
        f = FX if bold else FR
        br = "" if last else "border-right:1px solid #000000;"
        ww = "flex:1;" if last else f"width:{first}px;"
        return f'<div style="{ww}padding:20px 22px;{br}"><p style="font-family:{f};font-size:24px;line-height:1.3;color:{INK}">{esc(t)}</p></div>'
    out = f'<div style="width:{w}px;display:flex;flex-direction:column;background:{WHITE};border:10px solid {Y}">'
    for i, r in enumerate(rows):
        bg = Y if i == 0 else WHITE
        bt = "" if i == 0 else "border-top:1px solid #000000;"
        out += f'<div style="display:flex;flex-direction:row;background:{bg};{bt}">' + "".join(cell(t, i == 0 or j == 0, j == len(r) - 1) for j, t in enumerate(r)) + "</div>"
    return out + "</div>"


def points(items, w):
    out = ""
    for it in items:
        out += (f'<div style="display:flex;gap:28px;align-items:flex-start"><div style="width:84px;height:84px;flex:none;border-radius:50%;background:{INK};display:flex;align-items:center;justify-content:center">'
                f'<x-icon name="{it["icon"]}" style="color:{Y};width:44px;height:44px"></x-icon></div>'
                f'<div style="display:flex;flex-direction:column;gap:8px;width:{w - 112}px"><p style="font-family:{FX};font-size:30px;line-height:1.15;color:{INK}">{esc(it["title"])}</p>'
                f'<p style="font-family:{FR};font-size:24px;line-height:1.4;color:{INK}">{esc(it["text"])}</p></div></div>')
    return f'<div style="width:{w}px;display:flex;flex-direction:column;gap:34px">{out}</div>'


def stats(items, w, cols=2):
    cw = (w - 28 * (cols - 1)) // cols
    cards = "".join(
        f'<div style="width:{cw}px;box-sizing:border-box;background:{INK};border-top:8px solid {Y};padding:30px 32px 34px;display:flex;flex-direction:column;gap:14px">'
        f'<p style="font-family:{FX};font-size:76px;line-height:1;color:{WHITE}">{esc(it["n"])}</p>'
        f'<div style="width:56px;height:5px;background:{Y}"></div>'
        f'<p style="font-family:{FR};font-size:24px;line-height:1.35;color:{WHITE}">{esc(it["label"])}</p></div>' for it in items)
    return f'<div style="width:{w}px;display:flex;flex-wrap:wrap;gap:28px">{cards}</div>'


def r_panel(s, deck, n, chap):
    p = s.get("plate", 76)
    left = [h2(s["title"], x=0, y=0, w=700).replace("position:absolute;left:0px;top:0px;", "")]
    if s.get("standfirst"): left.append(standfirst(s["standfirst"], 700, size=28))
    k = s["kind"]
    if k == "table": right = table(s["rows"], 960, first=s.get("first", 300))
    elif k == "points": right = points(s["items"], 960)
    else: right = stats(s["items"], 960)
    inner = (full_bg(plate("quiet", p, chap)) + col_block(78, 76, 700, left)
             + f'<div style="position:absolute;left:882px;top:{s.get("top", 250)}px;width:960px">{right}</div>' + footer(deck, n))
    return section(s["id"], WHITE, inner, f"Panel (recipe: panel, {k}). Words top left, above the ingredient; the content block on the right.")


def bars(data, w, h=440):
    mx = max(v for _, v, _ in data)
    bw = (w - 24 * (len(data) - 1)) // len(data)
    cols = "".join(
        f'<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:10px;width:{bw}px;height:{h}px">'
        f'<p style="font-family:{FX};font-size:26px;color:{WHITE}">{esc(lab)}</p>'
        f'<div style="width:{bw}px;height:{round((h - 90) * v / mx)}px;background:{Y if i == len(data) - 1 else WHITE}"></div>'
        f'<p style="font-family:{FR};font-size:22px;color:{WHITE}">{esc(x)}</p></div>' for i, (x, v, lab) in enumerate(data))
    return f'<div style="display:flex;gap:24px;align-items:flex-end;width:{w}px;border-bottom:2px solid {WHITE}">{cols}</div>'


def r_halves(s, deck, n, chap):
    left = [h2(s["title"], x=0, y=0, w=780).replace("position:absolute;left:0px;top:0px;", "")]
    if s.get("standfirst"): left.append(standfirst(s["standfirst"], 780))
    if s.get("body"): left.append(body(s["body"], 780))
    right = []
    if s.get("label"): right.append(f'<p style="font-family:{FX};font-size:32px;line-height:1.2;color:{Y};width:700px">{esc(s["label"])}</p>')
    if s.get("bullets"): right.append(ring_list(s["bullets"], col=WHITE, w=660))
    if s.get("bars"): right.append(bars(s["bars"], 760))
    if s.get("source"): right.append(f'<p style="font-family:{FR};font-size:20px;color:{WHITE}">{esc(s["source"])}</p>')
    inner = (full_bg(plate("halves", 99, chap)) + col_block(78, 76, 780, left)
             + col_block(1040, s.get("top", 300), 780, right, gap=30) + footer(deck, n))
    return section(s["id"], WHITE, inner, "Two halves (recipe: halves). Words in the light half; points or a chart in the dark half, below the squiggle.")


def r_band(s, deck, n, chap):
    p = s.get("plate", 93)
    top = [h2(s["title"], x=0, y=0, w=820).replace("position:absolute;left:0px;top:0px;", "")]
    if s.get("standfirst"): top.append(standfirst(s["standfirst"], 820, size=28))
    items = "".join(
        f'<div style="width:250px;display:flex;flex-direction:column;gap:12px"><p style="font-family:{FX};font-size:64px;line-height:1;color:{Y}">{esc(it["n"])}</p>'
        f'<p style="font-family:{FR};font-size:24px;line-height:1.35;color:{WHITE}">{esc(it["label"])}</p></div>' for it in s["items"])
    inner = (full_bg(plate("band", p, chap)) + col_block(78, 76, 820, top)
             + f'<div style="position:absolute;left:78px;top:668px;width:830px;display:flex;gap:40px">{items}</div>' + footer(deck, n))
    return section(s["id"], WHITE, inner, "Band (recipe: band). Headline above, three facts in the dark band, drinks crossing the seam on the right.")


def r_steps(s, deck, n, chap):
    # Steps in one or more rows. s["rows"] gives panels per row, e.g. [3], [4], [3, 3], [3, 2]; default is one row.
    # s["align"] = "left" or "centre" for a short last row. Headline and panels are one group, centred top to bottom
    # in the colour area (0 to 969).
    import math
    steps = s["steps"]; rows = s.get("rows", [len(steps)]); assert sum(rows) == len(steps)
    gap = 40; per = max(rows); pw = (1764 - gap * (per - 1)) // per
    multi = len(rows) > 1
    h = s.get("h", 300 if multi else (440 if per >= 4 else 400))
    pad = "32px 34px" if multi else "44px 34px"; inner_gap = 14 if multi else 18
    head_h = math.ceil(len(s["title"]) / 30) * 67
    if s.get("standfirst"): head_h += 20 + math.ceil(len(s["standfirst"]) / 62) * 37
    rgap = 40
    total = head_h + 56 + len(rows) * h + (len(rows) - 1) * rgap
    y0 = (969 - total) // 2; top0 = y0 + head_h + 56
    panels = ""; k = 0
    for r, cnt in enumerate(rows):
        rw = cnt * pw + (cnt - 1) * gap
        x0 = 78 + ((1764 - rw) // 2 if s.get("align") == "centre" else 0)
        top = top0 + r * (h + rgap)
        for i in range(cnt):
            st = steps[k]; x = x0 + i * (pw + gap)
            panels += (f'<div style="position:absolute;left:{x}px;top:{top}px;width:{pw}px;height:{h}px;box-sizing:border-box;background:{INK};padding:{pad};display:flex;flex-direction:column;gap:{inner_gap}px">'
                       f'<div style="width:56px;height:56px;border-radius:50%;background:{Y};display:flex;align-items:center;justify-content:center"><p style="font-family:{FX};font-size:22px;line-height:1;color:{INK}">{k + 1:02d}</p></div>'
                       f'<p style="font-family:{FX};font-size:34px;line-height:1.15;color:{WHITE}">{esc(st[0])}</p>'
                       f'<div style="width:56px;height:5px;background:{Y}"></div>'
                       f'<p style="font-family:{FR};font-size:24px;line-height:1.45;color:{WHITE}">{esc(st[1])}</p></div>')
            if i < cnt - 1:
                panels += f'<div style="position:absolute;left:{x + pw - 15}px;top:{top + (48 if multi else 64)}px;width:30px;height:30px;background:{INK};transform:rotate(45deg)"></div>'
            k += 1
    parts = [h2(s["title"], x=0, y=0, w=1050).replace("position:absolute;left:0px;top:0px;", "")]
    if s.get("standfirst"): parts.append(standfirst(s["standfirst"], 1050, size=28))
    inner = full_bg(plate("full", s.get("sw", "99"), chap)) + col_block(78, y0, 1050, parts, gap=20) + panels + footer(deck, n)
    label = " + ".join(str(c) for c in rows)
    return section(s["id"], WHITE, inner, f"Steps (recipe: steps, rows {label}). Full chapter colour with Jim's squiggle top right; headline and black panels centred top to bottom as one group, joined by pointers, yellow number badges.")


def r_icons(s, deck, n, chap):
    # Open icon row, as the website's C.iconRow: the site's round black icons, bold title, a line or two beneath, no boxes.
    # s["items"] = [(title, body, icon key)], s["rows"] panels per row as in r_steps, s["align"] for a short last row.
    import math
    items = s["items"]; rows = s.get("rows", [len(items)]); assert sum(rows) == len(items)
    gap = 64; per = max(rows); cw = (1764 - gap * (per - 1)) // per
    icon = s.get("icon", 104); rgap = s.get("rgap", 72); hw = 1000 if s.get("image") else 1050
    cpl = max(1, int(cw / 12.5))
    row_h = []
    k = 0
    for cnt in rows:
        lines = max(math.ceil(len(items[k + i][1]) / cpl) for i in range(cnt)); k += cnt
        tl = max(math.ceil(len(items[j][0]) / max(1, int(cw / 19))) for j in range(k - cnt, k))
        row_h.append(icon + 22 + tl * 40 + 12 + lines * 35)
    head_h = math.ceil(len(s["title"]) / (hw // 35)) * 67
    if s.get("standfirst"): head_h += 20 + math.ceil(len(s["standfirst"]) / 62) * 37
    if s.get("lead"): head_h += 20 + math.ceil(len(s["lead"]) / (hw // 12.5)) * 35
    if s.get("image"): head_h = max(head_h, s["image"][1])
    hgap = s.get("hgap", 72)
    total = head_h + hgap + sum(row_h) + rgap * (len(rows) - 1)
    y0 = (969 - total) // 2; top = y0 + head_h + hgap
    out = ""; k = 0
    for r, cnt in enumerate(rows):
        rw = cnt * cw + (cnt - 1) * gap
        x0 = 78 + ((1764 - rw) // 2 if s.get("align") == "centre" else 0)
        for i in range(cnt):
            t_, d, ic = items[k]; x = x0 + i * (cw + gap)
            src = asset(f"ic-{ic}", f"{REPO}public/gc/img/concepts/ic-{ic}.webp")
            out += (f'<div style="position:absolute;left:{x}px;top:{top}px;width:{cw}px;display:flex;flex-direction:column;gap:0px">'
                    f'<img src="{src}" alt="" style="width:{icon}px;height:{icon}px;margin-bottom:22px">'
                    f'<h3 style="font-family:{FX};font-weight:400;font-size:34px;line-height:1.15;color:{INK};margin-bottom:12px">{esc(t_)}</h3>'
                    f'<p style="font-family:{FR};font-size:24px;line-height:1.45;color:{INK}">{esc(d)}</p></div>')
            k += 1
        top += row_h[r] + rgap
    parts = [h2(s["title"], x=0, y=0, w=hw).replace("position:absolute;left:0px;top:0px;", "")]
    if s.get("standfirst"): parts.append(standfirst(s["standfirst"], hw, size=28))
    if s.get("lead"): parts.append(body(s["lead"], hw, size=24))
    img = ""
    if s.get("image"):
        (path, ih, iw) = s["image"]
        img = f'<img src="{asset("img-" + path.split("/")[-1].split(".")[0], path)}" alt="" style="position:absolute;left:{1842 - iw}px;top:{y0}px;width:{iw}px;height:{ih}px;object-fit:contain">'
    bg = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0]}"></div>'
          if s.get("flat") else full_bg(plate("full", s.get("sw", "99"), chap)))
    inner = bg + col_block(78, y0, hw, parts, gap=20) + img + out + footer(deck, n)
    label = " + ".join(str(c) for c in rows)
    if s.get("note"): return section(s["id"], WHITE, inner, s["note"].format(label=label))
    return section(s["id"], WHITE, inner, f"Icon row (recipe: icons, rows {label}). The website's open icon row: round black icons, bold title, a line or two beneath, no boxes. Headline and rows centred top to bottom as one group.")


def r_jcards(s, deck, n, chap):
    # Website block 27, What's inside (kpg-jim.ts .jcards): black cards with a thick yellow top, Jim's yellow icon
    # circle sitting over the top edge, white title with a short yellow rule, white text. Headline and lead above.
    # Laid out like the steps: s["rows"] cards per row, s["align"] for a short last row. Group centred top to bottom.
    import math
    items = s["items"]; rows = s.get("rows", [len(items)]); assert sum(rows) == len(items)
    multi = len(rows) > 1
    gap = 52; per = max(rows); cw = (1764 - gap * (per - 1)) // per
    K = 1.4                                   # site px to slide px
    icon = round(70 * K); over = round(43 * K); topb = round(17 * K)
    padt = round((44 if multi else 60) * K); padx = round(29 * K); padb = round((22 if multi else 32) * K)
    ink = "#1d1d1b"
    tl = max(math.ceil(len(x[0]) / max(1, int((cw - 2 * padx) / 18))) for x in items)
    bl = max(math.ceil(len(x[1]) / max(1, int((cw - 2 * padx) / 11))) for x in items)
    ch = topb + padt + tl * 36 + 24 + 6 + 20 + bl * 30 + padb
    rgap = over + (28 if multi else 40)
    head_h = math.ceil(len(s["title"]) / 30) * 67
    if s.get("lead"): head_h += 20 + math.ceil(len(s["lead"]) / 85) * 35
    hgap = over + (28 if multi else 44)
    total = head_h + hgap + len(rows) * ch + (len(rows) - 1) * rgap
    y0 = (969 - total) // 2; top = y0 + head_h + hgap
    out = ""; k = 0
    for r, cnt in enumerate(rows):
        rw = cnt * cw + (cnt - 1) * gap
        x0 = 78 + ((1764 - rw) // 2 if s.get("align") == "centre" else 0)
        for i in range(cnt):
            t_, d, ic = items[k]; x = x0 + i * (cw + gap)
            src = asset(f"jic-{ic}", f"{W}plates/jic/icon-inside-{ic}.png")
            out += (f'<div style="position:absolute;left:{x}px;top:{top}px;width:{cw}px;height:{ch}px;box-sizing:border-box;background:{ink};border-top:{topb}px solid {Y};padding:{padt}px {padx}px {padb}px;display:flex;flex-direction:column">'
                    f'<h3 style="font-family:{FX};font-weight:400;font-size:30px;line-height:1.2;color:{WHITE}">{esc(t_)}</h3>'
                    f'<div style="width:66px;height:6px;background:{Y};margin:18px 0px 22px"></div>'
                    f'<p style="font-family:{FR};font-size:24px;line-height:1.25;color:{WHITE}">{esc(d)}</p></div>'
                    f'<img src="{src}" alt="" style="position:absolute;left:{x + cw // 2 - icon // 2}px;top:{top - over}px;width:{icon}px;height:{icon}px">')
            k += 1
        top += ch + rgap
    parts = [h2(s["title"], x=0, y=0, w=1300).replace("position:absolute;left:0px;top:0px;", "")]
    if s.get("lead"): parts.append(body(s["lead"], 1100, size=24))
    bg = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0]}"></div>'
          if s.get("flat") else full_bg(plate("full", s.get("sw", "99"), chap)))
    label = " + ".join(str(c) for c in rows)
    inner = bg + col_block(78, y0, 1300, parts, gap=20) + out + footer(deck, n)
    return section(s["id"], WHITE, inner, f"What's inside (recipe: jcards, rows {label}). Website block 27: black cards with a yellow top, Jim's yellow icon circle over the top edge, title with a short yellow rule. Laid out like the steps.")


FB = "'Engram Bold', Arial, sans-serif"
PLAY = '<svg viewBox="0 0 10 12" aria-label="" style="width:16px;height:19px;flex:none"><path d="M0 0l10 6-10 6z" fill="#ffffff"/></svg>'


def chal_bars(items, x, y, w, bar=90, gap=40, cols=1, cgap=54):
    # Website block 30, challenge bars (fix-jim.ts .fxj-chal): black bars, Jim's yellow icon circle overlapping the
    # left end, a white play triangle before each label. Site sizes x1.45. Columns fill top to bottom, as on the site.
    icon = round(bar * 80 / 62); over = round(icon * 38 / 80); padl = round(bar * 64 / 62)
    per = -(-len(items) // cols); cw = (w - cgap * (cols - 1)) // cols
    out = ""
    for i, (label, ic) in enumerate(items):
        c, r = divmod(i, per)
        bx = x + c * (cw + cgap) + over; by = y + r * (bar + gap)
        src = asset(f"fxic-{ic}", f"{REPO}public/gc/img/jim/fx-ic-{ic}.webp")
        out += (f'<div style="position:absolute;left:{bx}px;top:{by}px;width:{cw - over}px;height:{bar}px;box-sizing:border-box;background:#000000;padding:0px 24px 0px {padl}px;display:flex;flex-direction:row;align-items:center;gap:16px">'
                f'{PLAY}<p style="font-family:{FB};font-size:{round(bar * 0.33)}px;line-height:1.15;color:{WHITE}">{esc(label)}</p></div>'
                f'<img src="{src}" alt="" style="position:absolute;left:{bx - over}px;top:{by + bar // 2 - icon // 2}px;width:{icon}px;height:{icon}px">')
    return out, per * bar + (per - 1) * gap


def r_challenges(s, deck, n, chap):
    # Challenge bars with text left, a photo left, or two columns across the slide (s["layout"]: text, photo, wide).
    import math
    lay = s.get("layout", "text"); items = s["items"]
    bg = f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0]}"></div>'
    out = bg + (swirl(s) if s.get("swirl") else "")
    if lay == "wide":
        bars, bh = chal_bars(items, 78, 0, 1764, bar=90, gap=40, cols=2)
        hh = math.ceil(len(s["title"]) / 40) * 67
        y0 = (969 - hh - 64 - bh) // 2
        out += col_block(78, y0, 1600, [h2(s["title"], x=0, y=0, w=1600).replace("position:absolute;left:0px;top:0px;", "")])
        bars, _ = chal_bars(items, 78, y0 + hh + 64, 1764, bar=90, gap=40, cols=2)
        out += bars
    elif lay == "text":
        bar, gap = (90, 40) if len(items) <= 5 else (82, 32)
        _, bh = chal_bars(items, 0, 0, 800, bar, gap)
        by = (969 - bh) // 2
        bars, _ = chal_bars(items, 1000, by, 842, bar, gap)
        parts = [h2(s["title"], x=0, y=0, w=780).replace("position:absolute;left:0px;top:0px;", "")]
        lh = math.ceil(len(s["title"]) / 22) * 67
        if s.get("standfirst"): parts.append(standfirst(s["standfirst"], 780, size=30)); lh += 28 + math.ceil(len(s["standfirst"]) / 42) * 39
        if s.get("body"): parts.append(body(s["body"], 780, size=26)); lh += 28 + math.ceil(len(s["body"]) / 52) * 38
        out += col_block(78, max(70, (969 - lh) // 2), 780, parts) + bars
    else:  # photo left, words and bars right
        ph = asset(f"photo-{s['photo']}", f"{W}plates/photos/{s['photo']}.jpg")
        out += f'<img src="{ph}" alt="{esc(s.get("alt", ""))}" style="position:absolute;left:0px;top:0px;width:960px;height:969px;object-fit:cover">'
        bar, gap = (80, 28)
        _, bh = chal_bars(items, 0, 0, 700, bar, gap)
        hh = math.ceil(len(s["title"]) / 22) * 67
        y0 = (969 - hh - 56 - bh) // 2
        out += col_block(1040, y0, 802, [h2(s["title"], x=0, y=0, w=802).replace("position:absolute;left:0px;top:0px;", "")])
        bars, _ = chal_bars(items, 1040, y0 + hh + 56, 802, bar, gap)
        out += bars
    return section(s["id"], WHITE, out + footer(deck, n), f"Challenge bars (recipe: challenges, layout {lay}). Website block 30: black bars, Jim's yellow icon circle over the left end, a play triangle before each label.")


CLOCK = ('<svg viewBox="0 0 24 24" aria-label="" style="width:{s}px;height:{s}px;flex:none"><circle cx="12" cy="12" r="9.5" fill="none" stroke="{c}" stroke-width="2"/>'
         '<path d="M12 7v5l3 2" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"/></svg>')


def r_timeline(s, deck, n, chap):
    # Website "Idea to shelf" (Create a New Drink): numbered stages in columns with dividers, a yellow number circle,
    # title, short rule, text and a Typical timing box at the foot. s["style"]: "panel" puts it in a black panel on the
    # chapter colour (decks never use a black slide), "light" sets it straight on white in ink.
    stages = s["stages"]; cnt = len(stages); dark = s.get("style", "panel") == "panel"
    fg, muted, line = (WHITE, "#d8d8d8", "#3a3a3a") if dark else (INK, "#333333", "#c8c8c8")
    acc = Y if dark else INK; rule = WHITE if dark else Y
    px, py = (64, 52) if dark else (0, 0)
    x0, y0, w = (78, 56, 1764) if dark else (78, 70, 1764)
    iw = w - 2 * px; cw = iw // cnt
    cols = ""
    for i, (t_, d, tm) in enumerate(stages):
        bl = "" if i == 0 else f"border-left:2px solid {line};"
        pl = 0 if i == 0 else 32; pr = 0 if i == cnt - 1 else 32
        cols += (f'<div style="width:{cw}px;box-sizing:border-box;{bl}padding:0px {pr}px 0px {pl}px;display:flex;flex-direction:column">'
                 f'<div style="width:64px;height:64px;border-radius:50%;background:{Y};display:flex;align-items:center;justify-content:center;margin-bottom:28px"><p style="font-family:{FX};font-size:28px;line-height:1;color:{INK}">{i + 1}</p></div>'
                 f'<h3 style="font-family:{FX};font-weight:400;font-size:34px;line-height:1.15;color:{acc}">{esc(t_)}</h3>'
                 f'<div style="width:64px;height:5px;background:{rule};margin:20px 0px 26px"></div>'
                 f'<p style="font-family:{FR};font-size:24px;line-height:1.45;color:{muted}">{esc(d)}</p>'
                 f'<div style="margin-top:auto;padding-top:24px"><div style="border-top:2px solid {line};padding-top:24px">'
                 f'<div style="display:inline-flex;flex-direction:row;align-items:center;gap:20px;border:2px solid {line};padding:14px 26px 14px 20px">'
                 f'{CLOCK.format(s=34, c=Y if dark else INK)}<div style="display:flex;flex-direction:column;gap:4px">'
                 f'<p style="font-family:{FB};font-size:24px;line-height:1.2;color:{fg}">Typical timing</p>'
                 f'<p style="font-family:{FR};font-size:24px;line-height:1.2;color:{muted}">{esc(tm)}</p></div></div></div></div></div>')
    head = (f'<h2 style="font-family:{FX};font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-1px;color:{fg}">{esc(s["title"])}</h2>'
            + (f'<p style="font-family:{FR};font-size:26px;line-height:1.45;color:{muted};margin-top:16px">{esc(s["lead"])}</p>' if s.get("lead") else "")
            + f'<div style="height:2px;background:{line};margin:32px 0px 40px"></div>')
    h = s.get("h", 857 if dark else 830)
    box = (f'<div style="position:absolute;left:{x0}px;top:{y0}px;width:{w}px;height:{h}px;box-sizing:border-box;'
           f'{"background:#0c0c0c;" if dark else ""}padding:{py}px {px}px;display:flex;flex-direction:column">'
           f'{head}<div style="flex:1;display:flex;flex-direction:row">{cols}</div></div>')
    bg = f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0] if dark else WHITE}"></div>'
    bg += (swirl(s) if s.get("swirl") else "")
    return section(s["id"], WHITE, bg + box + footer(deck, n), f"Timeline (recipe: timeline, {cnt} stages, {s.get('style', 'panel')}). The website's Idea to shelf: numbered stages with dividers, a rule under each title and a Typical timing box at the foot.")


def r_problemfix(s, deck, n, chap):
    # Website block 32, Problem and fix table (Fix a Problem): two columns with yellow heads and black bodies, dotted
    # rules between rows, and a pointer from each problem into its fix. Optional headline above.
    rows = s["rows"]; ink = "#1d1d1b"; gap = 44; w = 1764; cw = (w - gap) // 2
    dots = "border-top:3px dotted #8a8a8a;"
    head = (f'<div style="display:flex;flex-direction:row;gap:{gap}px">'
            + "".join(f'<div style="width:{cw}px;box-sizing:border-box;background:{Y};padding:26px 52px"><p style="font-family:{FX};font-size:42px;line-height:1.1;color:{INK}">{esc(h)}</p></div>'
                      for h in s.get("heads", ["The problem", "How we fix it"])) + '</div>')
    body = ""
    for i, (p_, f_) in enumerate(rows):
        bt = "" if i == 0 else dots
        pad = "34px 52px" if len(rows) > 4 else "40px 52px"
        body += (f'<div style="display:flex;flex-direction:row;gap:{gap}px">'
                 f'<div style="width:{cw}px;box-sizing:border-box;background:{ink};padding:{pad};{bt}position:relative">'
                 f'<p style="font-family:{FB};font-size:28px;line-height:1.3;color:{WHITE}">{esc(p_)}</p>'
                 f'<svg viewBox="0 0 28 48" aria-label="" style="position:absolute;right:-28px;top:30px;width:28px;height:48px"><path d="M0 0l28 24L0 48z" fill="{ink}"/></svg></div>'
                 f'<div style="width:{cw}px;box-sizing:border-box;background:{ink};padding:{pad};{bt}">'
                 f'<p style="font-family:{FR};font-size:28px;line-height:1.3;color:{WHITE}">{esc(f_)}</p></div></div>')
    parts = ""
    if s.get("title"):
        parts += f'<h2 style="font-family:{FX};font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-1px;color:{INK};margin-bottom:44px">{esc(s["title"])}</h2>'
    box = f'<div style="position:absolute;left:78px;top:0px;width:{w}px;height:969px;display:flex;flex-direction:column;justify-content:center">{parts}{head}<div style="display:flex;flex-direction:column">{body}</div></div>'
    bg = f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0]}"></div>'
    bg += (swirl(s) if s.get("swirl") else "")
    return section(s["id"], WHITE, bg + box + footer(deck, n), "Problem and fix (recipe: problemfix). Website block 32: yellow column heads, black cells, dotted rules, a pointer from each problem to its fix.")


def r_facts(s, deck, n, chap):
    # Website yellow fact boxes (Ingredients, c4-facts): headline and two paragraphs left, a stack of yellow boxes right,
    # each with a big figure, a bold label and a line. s["style"]: "panel" puts it in a black panel on the chapter
    # colour (decks never use a black slide), "light" sets it on white in ink.
    dark = s.get("style", "panel") == "panel"
    fg, muted = (WHITE, "#bdbdbd") if dark else (INK, "#4a4a4a")
    facts = s["facts"]; fb = ""
    for big, lab, d in facts:
        fb += (f'<div style="background:{Y};padding:34px 44px;display:flex;flex-direction:column">'
               f'<p style="font-family:{FX};font-size:54px;line-height:1.05;color:{INK}">{esc(big)}</p>'
               f'<p style="font-family:{FX};font-size:28px;line-height:1.2;color:{INK};margin-top:8px">{esc(lab)}</p>'
               f'<p style="font-family:{FR};font-size:24px;line-height:1.35;color:{INK};margin-top:18px">{esc(d)}</p></div>')
    left = (f'<h2 style="font-family:{FX};font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-1px;color:{fg}">{esc(s["title"])}</h2>'
            f'<p style="font-family:{FR};font-size:26px;line-height:1.5;color:{fg};margin-top:36px">{esc(s["body"])}</p>'
            + (f'<p style="font-family:{FR};font-size:26px;line-height:1.5;color:{muted};margin-top:26px">{esc(s["more"])}</p>' if s.get("more") else ""))
    pad = 64 if dark else 0
    inner = (f'<div style="position:absolute;left:78px;top:{56 if dark else 70}px;width:1764px;height:{857 if dark else 830}px;box-sizing:border-box;'
             f'{"background:#0c0c0c;" if dark else ""}padding:{pad}px;display:flex;flex-direction:row;align-items:center;gap:80px">'
             f'<div style="flex:1;display:flex;flex-direction:column">{left}</div>'
             f'<div style="width:{760 if dark else 820}px;display:flex;flex-direction:column;gap:24px">{fb}</div></div>')
    bg = f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0]}"></div>'
    return section(s["id"], WHITE, bg + inner + footer(deck, n), f"Fact boxes (recipe: facts, {s.get('style', 'panel')}). The website's yellow fact boxes: headline and text left, big figures in yellow boxes right.")


RETAIL = ["aldi", "tesco", "7-eleven", "costco", "spar", "whole-foods", "amazon", "edeka", "coles", "carrefour", "walmart", "lidl"]


def r_retail(s, deck, n, chap):
    # Retailer logos. "panel": the website block (homepage), yellow logos six by two in a black panel on the chapter
    # colour. "band": the layout from the Carlsberg and Tesco decks, chapter colour above with the headline, the
    # colour logos on a white band, chapter colour below.
    style = s.get("style", "panel"); c = PAIRS[chap][0]
    if style == "panel":
        cells = ""
        for nme in RETAIL:
            src = asset(f"y-{nme}", f"{W}plates/retail/y-{nme}.png")
            cells += f'<div style="width:236px;height:150px;display:flex;align-items:center;justify-content:center"><img src="{src}" alt="{nme}" style="width:236px;height:120px;object-fit:contain"></div>'
        inner = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{c}"></div>'
                 f'<div style="position:absolute;left:78px;top:56px;width:1764px;height:857px;box-sizing:border-box;background:#0c0c0c;padding:80px 90px;display:flex;flex-direction:column;justify-content:center">'
                 f'<h2 style="font-family:{FX};font-weight:400;font-size:72px;line-height:1.08;letter-spacing:-1px;color:{WHITE};width:1400px">{s["title"]}</h2>'
                 f'<div style="display:flex;flex-direction:row;flex-wrap:wrap;column-gap:28px;row-gap:44px;margin-top:80px">{cells}</div></div>')
    else:
        src = asset("logos-colour", f"{W}plates/retail/logos-colour-crop.png")
        lw = 1600; lh = round(lw * 800 / 3187)
        inner = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{c}"></div>'
                 f'<div style="position:absolute;left:0px;top:330px;width:1920px;height:500px;background:{WHITE}"></div>'
                 f'<h2 style="position:absolute;left:78px;top:70px;width:1300px;font-family:{FX};font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
                 f'<img src="{src}" alt="Retailers that sell drinks made with our bases" style="position:absolute;left:{(1920 - lw) // 2}px;top:{330 + (500 - lh) // 2}px;width:{lw}px;height:{lh}px">')
    return section(s["id"], WHITE, inner + footer(deck, n), f"Retailer logos (recipe: retail, {style}).")


CERTS = ["sqf", "usda-organic", "eu-organic", "soil-association", "kosher", "halal"]


def r_certs(s, deck, n, chap):
    # Website certifications block: headline, a line of text across the width, then one row of the certification
    # logos in black. On white, or on the chapter colour with s["colour"].
    bgc = PAIRS[chap][0] if s.get("colour") else WHITE
    cells = "".join(f'<div style="flex:1;height:170px;display:flex;align-items:center;justify-content:center">'
                    f'<img src="{asset("cert-" + c, f"{W}plates/certs/{c}.png")}" alt="{c}" style="width:240px;height:170px;object-fit:contain"></div>'
                    for c in s.get("certs", CERTS))
    inner = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{bgc}"></div>'
             f'<div style="position:absolute;left:78px;top:0px;width:1764px;height:969px;display:flex;flex-direction:column;justify-content:center">'
             f'<h2 style="font-family:{FX};font-weight:400;font-size:72px;line-height:1.05;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
             f'<p style="font-family:{FR};font-size:30px;line-height:1.5;color:{INK};margin-top:40px;width:1500px">{esc(s["body"])}</p>'
             f'<div style="display:flex;flex-direction:row;gap:40px;margin-top:90px">{cells}</div></div>')
    return section(s["id"], WHITE, inner + footer(deck, n), "Certifications (recipe: certs). The website's certifications block: headline, text across the width, then one row of logos.")


def r_bigicons(s, deck, n, chap):
    # The Carlsberg and Tesco decks' challenge slide (page 5): a big headline top left, then a row of large black icon
    # circles (the site's icon set) with a bold label centred under each.
    items = s["items"]; cnt = len(items); size = s.get("size", 230 if cnt >= 5 else 260)
    cw = 1764 // cnt
    cells = "".join(f'<div style="width:{cw}px;display:flex;flex-direction:column;align-items:center">'
                    f'<img src="{asset("big-" + ic, W + "plates/bigic/" + ic + ".png")}" alt="" style="width:{size}px;height:{size}px">'
                    f'<p style="font-family:{FX};font-size:34px;line-height:1.15;text-align:center;color:{INK};margin-top:40px;width:{cw - 40}px">{esc(lab)}</p></div>'
                    for lab, ic in items)
    inner = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0]}"></div>'
             f'<h2 style="position:absolute;left:78px;top:76px;width:{s.get("tw", 1150)}px;font-family:{FX};font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
             f'<div style="position:absolute;left:78px;top:{s.get("row", 470)}px;width:1764px;display:flex;flex-direction:row">{cells}</div>')
    return section(s["id"], WHITE, inner + footer(deck, n), "Big icon row (recipe: bigicons). From the Carlsberg and Tesco decks: big headline, then large black icon circles with a bold label under each. Background to be swapped for one of Luke's.")


def r_statcards(s, deck, n, chap):
    # Website stat cards (category pages): headline and lead, then white cards, each with the figure in a yellow pill,
    # a bold title and a line or two. On cream, or the chapter colour with s["colour"].
    cards = s["cards"]; cnt = len(cards); gap = 36; cw = (1764 - gap * (cnt - 1)) // cnt
    bgc = PAIRS[chap][0] if s.get("colour") else "#f3f2ee"
    cs = "".join(f'<div style="width:{cw}px;box-sizing:border-box;background:{WHITE};padding:40px 40px 52px;display:flex;flex-direction:column">'
                 f'<div style="align-self:flex-start;background:{Y};border-radius:999px;padding:24px 40px"><p style="font-family:{FX};font-size:40px;line-height:1;color:{INK}">{esc(fig)}</p></div>'
                 f'<h3 style="font-family:{FX};font-weight:400;font-size:32px;line-height:1.2;color:{INK};margin-top:40px">{esc(t_)}</h3>'
                 f'<p style="font-family:{FR};font-size:24px;line-height:1.5;color:#4a4a4a;margin-top:16px">{esc(d)}</p></div>'
                 for fig, t_, d in cards)
    inner = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{bgc}"></div>'
             f'<div style="position:absolute;left:78px;top:0px;width:1764px;height:969px;display:flex;flex-direction:column;justify-content:center">'
             f'<h2 style="font-family:{FX};font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
             + (f'<p style="font-family:{FR};font-size:28px;line-height:1.45;color:{INK};margin-top:24px">{esc(s["lead"])}</p>' if s.get("lead") else "")
             + f'<div style="display:flex;flex-direction:row;align-items:stretch;gap:{gap}px;margin-top:72px">{cs}</div></div>')
    return section(s["id"], WHITE, inner + footer(deck, n), "Stat cards (recipe: statcards). The website's stat cards: the figure in a yellow pill, a bold title and a line or two, on white cards.")


def r_casestudy(s, deck, n, chap):
    # Customer success study, from the Carlsberg and Tesco decks: title, a yellow "Customer Success Study" band from the
    # left edge, the bold challenge and a paragraph, "Our Solution:" with ring bullets bottom left, and "The Result:" in a
    # yellow box running off the right edge with the black award icon on its left edge. Drinks art comes with Luke's
    # background; the right of the top half is left for it.
    c = PAIRS[chap][0]
    aw = asset("big-quality", f"{W}plates/bigic/quality.png")
    ph = asset("photo-" + s["photo"], f"{W}plates/photos/{s['photo']}.jpg")
    inner = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{c}"></div>'
             f'<img src="{ph}" alt="{esc(s.get("alt", ""))}" style="position:absolute;left:1010px;top:0px;width:910px;height:{s.get("res_y", 600)}px;object-fit:cover">'
             f'<h2 style="position:absolute;left:78px;top:56px;width:1000px;font-family:{FX};font-weight:400;font-size:64px;line-height:1.02;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
             f'<div style="position:absolute;left:0px;top:212px;width:1060px;height:66px;background:{Y};display:flex;align-items:center;padding-left:78px;box-sizing:border-box">'
             f'<p style="font-family:{FX};font-size:38px;line-height:1;color:{INK}">Customer Success Study</p></div>'
             f'<div style="position:absolute;left:78px;top:306px;width:880px;display:flex;flex-direction:column;gap:14px">'
             f'<p style="font-family:{FX};font-size:28px;line-height:1.18;color:{INK}">{esc(s["challenge"])}</p>'
             f'<p style="font-family:{FR};font-size:24px;line-height:1.35;color:{INK}">{esc(s["body"])}</p></div>'
             f'<div style="position:absolute;left:78px;top:{s.get("sol_y", 610)}px;width:760px;display:flex;flex-direction:column;gap:22px">'
             f'<p style="font-family:{FX};font-size:34px;line-height:1;color:{INK}">Our Solution:</p>{ring_list(s["solution"], INK, 700, 24)}</div>'
             f'<div style="position:absolute;left:1010px;top:{s.get("res_y", 600)}px;width:910px;box-sizing:border-box;background:{Y};padding:36px 70px 40px 100px;display:flex;flex-direction:column;gap:12px">'
             f'<p style="font-family:{FX};font-size:34px;line-height:1;color:{INK}">The Result:</p>'
             f'<p style="font-family:{FR};font-size:24px;line-height:1.38;color:{INK}">{esc(s["result"])}</p></div>'
             f'<img src="{aw}" alt="" style="position:absolute;left:950px;top:{s.get("res_y", 600) + 100}px;width:120px;height:120px">')
    return section(s["id"], WHITE, inner + footer(deck, n), "Case study (recipe: casestudy). From the Carlsberg and Tesco decks: yellow Customer Success Study band, challenge, Our Solution with ring bullets, The Result in a yellow box with the award icon. Drinks art to come with Luke's background.")


def r_global(s, deck, n, chap):
    # "site": the website's reach block (homepage 8): headline, the white map in a black box with its key, and black
    # fact cards with a yellow top, here stacked on the right. "deck": the Carlsberg and Tesco decks' page 2: chapter
    # colour left with the title, black map and key; yellow right with six black icons and labels.
    c = PAIRS[chap][0]
    if s.get("style", "site") == "site":
        mp = asset("map-white", REPO + "public/gc/img/concepts/map-white.webp")
        key = "".join(f'<div style="display:flex;align-items:center;gap:16px"><div style="width:26px;height:26px;border-radius:50%;background:{col}"></div>'
                      f'<p style="font-family:{FB};font-size:24px;line-height:1;color:{WHITE}">{lab}</p></div>'
                      for col, lab in (("#0b96d1", "International operations"), ("#f39200", "Global reach")))
        cards = "".join(f'<div style="background:#1d1d1b;border-top:10px solid {Y};padding:26px 34px 30px;display:flex;flex-direction:column">'
                        f'<p style="font-family:{FB};font-size:34px;line-height:1.1;color:{WHITE}">{esc(big)}</p>'
                        f'<div style="width:56px;height:5px;background:{Y};margin:14px 0px 16px"></div>'
                        f'<p style="font-family:{FB};font-size:24px;line-height:1.2;color:{WHITE}">{esc(t_)}</p>'
                        f'<p style="font-family:{FR};font-size:24px;line-height:1.35;color:#d8d8d8;margin-top:6px">{esc(d)}</p></div>'
                        for big, t_, d in s["facts"])
        inner = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{c}"></div>'
                 f'<h2 style="position:absolute;left:78px;top:56px;width:1764px;font-family:{FX};font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
                 f'<div style="position:absolute;left:78px;top:180px;width:1150px;height:740px;background:#1d1d1b"></div>'
                 f'<img src="{mp}" alt="World map showing where we operate and supply" style="position:absolute;left:150px;top:200px;width:1006px;height:580px;object-fit:contain">'
                 f'<div style="position:absolute;left:118px;top:806px;display:flex;flex-direction:column;gap:18px">{key}</div>'
                 f'<div style="position:absolute;left:1268px;top:180px;width:574px;height:740px;display:flex;flex-direction:column;justify-content:space-between">{cards}</div>')
    else:
        mp = asset("map-ink-y", f"{W}plates/global/map-ink-y.png")
        key = "".join(f'<div style="display:flex;align-items:center;gap:18px"><div style="width:30px;height:30px;border-radius:50%;background:{col}"></div>'
                      f'<p style="font-family:{FR};font-size:26px;line-height:1;color:{INK}">{lab}</p></div>'
                      for col, lab in (("#0b96d1", "International operations"), (Y, "Global reach")))
        rows = "".join(f'<div style="display:flex;flex-direction:row;align-items:center;gap:40px">'
                       f'<img src="{asset("gic-" + ic, W + "plates/global/ic-" + ic + ".png")}" alt="" style="width:110px;height:110px;object-fit:contain">'
                       f'<p style="font-family:{FX};font-size:32px;line-height:1.15;color:{INK};width:520px">{esc(lab)}</p></div>'
                       for lab, ic in s["items"])
        inner = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{Y}"></div>'
                 f'<div style="position:absolute;left:0px;top:0px;width:1130px;height:969px;background:{c}"></div>'
                 f'<h2 style="position:absolute;left:78px;top:60px;width:1000px;font-family:{FX};font-weight:400;font-size:60px;line-height:1.05;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
                 f'<img src="{mp}" alt="World map showing where we operate and supply" style="position:absolute;left:60px;top:250px;width:1000px;height:530px;object-fit:contain">'
                 f'<div style="position:absolute;left:78px;top:830px;display:flex;flex-direction:row;gap:50px">{key}</div>'
                 f'<div style="position:absolute;left:1210px;top:0px;width:680px;height:969px;display:flex;flex-direction:column;justify-content:center;gap:34px">{rows}</div>')
    return section(s["id"], WHITE, inner + footer(deck, n), f"Global reach (recipe: global, {s.get('style', 'site')}). The website's map block, or the Carlsberg and Tesco decks' global company page.")


def grid_table(rows, w, first=260, size=24, bold_col=None, align=None):
    # The range-overview table: yellow frame and header row, white body, label column bold and left, other cells
    # centred, thin grey rules between rows and columns.
    cols = len(rows[0]); cw = (w - 20 - first) // (cols - 1)
    out = f'<div style="width:{w}px;box-sizing:border-box;display:flex;flex-direction:column;background:{WHITE};border:10px solid {Y}">'
    for i, r in enumerate(rows):
        bg = Y if i == 0 else WHITE
        bt = "" if i < 2 else "border-top:2px solid #c8c8c8;"
        cells = ""
        for j, c in enumerate(r):
            bold = i == 0 or j == 0 or j == bold_col
            al = align or ("left" if (j == 0 or cols == 2) else "center")
            br = "" if j == cols - 1 or i == 0 else "border-right:2px solid #c8c8c8;"
            ww = first if j == 0 else cw
            fs = size + 4 if i == 0 and j > 0 and cols > 2 else size
            cells += (f'<div style="width:{ww}px;box-sizing:border-box;padding:{"18px 20px" if i == 0 else "16px 20px"};{br}">'
                      f'<p style="font-family:{FX if bold else FR};font-size:{fs}px;line-height:1.3;text-align:{al};color:{INK}">{esc(c)}</p></div>')
        out += f'<div style="display:flex;flex-direction:row;background:{bg};{bt}">{cells}</div>'
    return out + "</div>"


def table_h(rows, w, first=260, size=24):
    import math
    cols = len(rows[0]); cw = (w - 20 - first) // (cols - 1)
    h = 20
    for i, r in enumerate(rows):
        lines = max(math.ceil(len(c) * 0.52 * size / ((first if j == 0 else cw) - 40)) for j, c in enumerate(r))
        h += lines * size * 1.3 + (36 if i == 0 else 32) + (2 if i >= 2 else 0)
    return int(h)


def r_table(s, deck, n, chap):
    # Full-width table on the chapter's light colour, headline above, the group centred top to bottom.
    w = 1764; th = table_h(s["rows"], w, s.get("first", 260))
    head_h = 67 + (57 if s.get("standfirst") else 0)
    y0 = max(60, (969 - head_h - 48 - th) // 2)
    parts = [h2(s["title"], x=0, y=0, w=1400).replace("position:absolute;left:0px;top:0px;", "")]
    if s.get("standfirst"): parts.append(standfirst(s["standfirst"], 1400, size=28))
    tbl = f'<div style="position:absolute;left:78px;top:{y0 + head_h + 48}px">{grid_table(s["rows"], w, s.get("first", 260))}</div>'
    bg = f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0]}"></div>'
    inner = bg + col_block(78, y0, 1400, parts, gap=20) + tbl + footer(deck, n)
    return section(s["id"], WHITE, inner, "Table (recipe: table). Full-width yellow-framed table on the chapter's light colour, headline above. Background to be swapped for one of Luke's.")


def r_table_side(s, deck, n, chap):
    # Words on the left, a two or three column table on the right, both centred top to bottom.
    import math
    tw = 1060; tx = 1920 - 78 - tw; lw = tx - 78 - 80
    th = table_h(s["rows"], tw, s.get("first", 300))
    parts = [h2(s["title"], x=0, y=0, w=lw).replace("position:absolute;left:0px;top:0px;", "")]
    lh = math.ceil(len(s["title"]) / 17) * 67
    if s.get("standfirst"):
        parts.append(standfirst(s["standfirst"], lw, size=28)); lh += 24 + math.ceil(len(s["standfirst"]) / 34) * 37
    if s.get("body"):
        parts.append(body(s["body"], lw, size=24)); lh += 24 + math.ceil(len(s["body"]) / 42) * 35
    ly = max(60, (969 - lh) // 2); ty = max(60, (969 - th) // 2)
    bg = f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0]}"></div>'
    tbl = f'<div style="position:absolute;left:{tx}px;top:{ty}px">{grid_table(s["rows"], tw, s.get("first", 300))}</div>'
    inner = bg + col_block(78, ly, lw, parts, gap=24) + tbl + footer(deck, n)
    return section(s["id"], WHITE, inner, "Table with words (recipe: table_side). Words left, yellow-framed table right, both centred top to bottom, on the chapter's light colour. Background to be swapped for one of Luke's.")


RINGS_SEAM = [(899, 293, 38), (929, 360, 76), (889, 507, 53)]   # Canva photo-right template (plate 102)


def r_photo(s, deck, n, chap):
    # Canva photo-right backgrounds (102 orange, 103 pink, 104 teal) as they are, rings and all, with the photo
    # swapped in Python (plates/photoplates, rings kept on top). Text goes on top-left as in the template.
    lw = 750
    out = full_bg(asset(f"pp-{s['photo']}", f"{W}plates/photoplates/{s['photo']}.jpg"))
    parts = [h2(s["title"], x=0, y=0, w=lw).replace("position:absolute;left:0px;top:0px;", "")]
    if s.get("standfirst"):
        parts.append(f'<p style="font-family:{FX};font-size:36px;line-height:1.2;color:{Y};width:{lw}px">{esc(s["standfirst"])}</p>')
    if s.get("intro"):
        parts.append(f'<p style="font-family:{FX};font-size:28px;line-height:1.3;color:{INK};width:{lw}px">{esc(s["intro"])}</p>')
    if s.get("body"):
        parts.append(body(s["body"], lw, size=26))
    out += col_block(78, s.get("top", 110), lw, parts, gap=30)
    return section(s["id"], WHITE, out + footer(deck, n), "Photo (recipe: photo). Canva photo-right background (102, 103 or 104) with the photo swapped and the template's rings kept; words top left.")


def r_page(s, deck, n, chap):
    # A page from the Carlsberg and Tesco decks, widened to 16:9 (tools/a4plates.py): Jim's art as the background,
    # the words live on top. s["parts"] is a list of (x, y, w, html) pinned blocks; s["imgs"] (name, x, y, w, h).
    out = (f'<img src="{asset("a4-" + str(s["page"]), f"{W}plates/a4/w{s['page']}.jpg")}" alt="" '
           f'style="position:absolute;left:0px;top:0px;width:1920px;height:969px">')
    for name, x, y, w, h in s.get("imgs", []):
        out += f'<img src="{asset(name, W + "plates/a4/" + name + ".png")}" alt="" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
    for x, y, w, html in s["parts"]:
        out += f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;display:flex;flex-direction:column;gap:18px">{html}</div>'
    return section(s["id"], WHITE, out + footer(deck, n), s.get("note", "Page from the Carlsberg and Tesco decks, widened to 16:9 with the words live."))


def r_compare(s, deck, n, chap):
    # Us against the alternatives, in the website's recipe table (the range overview look): yellow frame and header,
    # white cells, thin grey rules, labels bold on the left, our column in bold.
    rows = [[""] + s["cols"]] + s["rows"]
    tbl = grid_table(rows, 1764, 300, 24, bold_col=s.get("highlight", len(s["cols"])), align="left")
    inner = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0]}"></div>'
             f'<div style="position:absolute;left:78px;top:0px;width:1764px;height:969px;display:flex;flex-direction:column;justify-content:center;gap:44px">'
             f'<div style="display:flex;flex-direction:column;gap:14px"><h2 style="font-family:{FX};font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
             + (f'<p style="font-family:{FR};font-size:28px;line-height:1.4;color:{INK}">{esc(s["lead"])}</p>' if s.get("lead") else "")
             + f'</div>{tbl}</div>')
    return section(s["id"], WHITE, inner + footer(deck, n), "Comparison (recipe: compare). The website's recipe table: yellow frame and header, white cells, thin grey rules, our column in bold.")

def r_supply(s, deck, n, chap):
    # Ordering and supply: words left, the website's fact sheet right (yellow label pills, value beside, soft rules).
    rows = "".join(f'<div style="display:flex;flex-direction:row;align-items:baseline;gap:28px;padding:20px 0px;{"" if i == 0 else "border-top:2px solid #e2ded3;"}">'
                   f'<div style="width:230px;flex:none"><p style="display:inline-block;font-family:{FB};font-size:20px;line-height:1.3;letter-spacing:1px;text-transform:uppercase;color:{INK};background:{Y};padding:6px 14px;border-radius:99px">{esc(k)}</p></div>'
                   f'<p style="font-family:{FR};font-size:25px;line-height:1.35;color:{INK}">{esc(v)}</p></div>'
                   for i, (k, v) in enumerate(s["facts"]))
    SWIRL = (swirl(s) if s.get("swirl") else "")
    inner = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0]}"></div>'
             f'{SWIRL}'
             f'<div style="position:absolute;left:78px;top:0px;width:680px;height:969px;display:flex;flex-direction:column;justify-content:center;gap:28px">'
             f'<h2 style="font-family:{FX};font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
             f'<p style="font-family:{FX};font-size:30px;line-height:1.25;color:{INK}">{esc(s["standfirst"])}</p>'
             f'<p style="font-family:{FR};font-size:26px;line-height:1.45;color:{INK}">{esc(s["body"])}</p></div>'
             f'<div style="position:absolute;left:840px;top:0px;width:1002px;height:969px;display:flex;flex-direction:column;justify-content:center">'
             f'<div style="background:{WHITE};border:2px solid {INK};padding:16px 44px">{rows}</div></div>')
    return section(s["id"], WHITE, inner + footer(deck, n), "Ordering and supply (recipe: supply). Words left, the website's fact sheet right.")


def r_routes(s, deck, n, chap):
    # Website block 2, route cards (homepage concept 4): yellow head with title and line, black body with ringed play rows.
    cards = ""
    for t_, sub, opts in s["routes"]:
        rows = "".join(f'<div style="display:flex;flex-direction:row;align-items:center;gap:22px;padding:22px 0px;{"" if i == 0 else "border-top:3px dotted #6b6b6b;"}">'
                       f'<div style="width:40px;height:40px;flex:none;border-radius:50%;border:3px solid {Y};display:flex;align-items:center;justify-content:center">'
                       f'<svg viewBox="0 0 10 12" aria-label="" style="width:12px;height:14px;margin-left:3px"><path d="M0 0l10 6-10 6z" fill="{Y}"/></svg></div>'
                       f'<p style="font-family:{FB};font-size:27px;line-height:1.2;color:{WHITE}">{esc(o)}</p></div>' for i, o in enumerate(opts))
        cards += (f'<div style="flex:1;display:flex;flex-direction:column;background:#1d1d1b">'
                  f'<div style="background:{Y};padding:40px 48px 36px"><h3 style="font-family:{FX};font-weight:400;font-size:42px;line-height:1.1;color:{INK}">{esc(t_)}</h3>'
                  f'<p style="font-family:{FR};font-size:25px;line-height:1.4;color:{INK};margin-top:16px">{esc(sub)}</p></div>'
                  f'<div style="padding:10px 48px 26px">{rows}</div></div>')
    inner = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0]}"></div>'
             f'<div style="position:absolute;left:78px;top:0px;width:1764px;height:969px;display:flex;flex-direction:column;justify-content:center;gap:48px">'
             f'<h2 style="font-family:{FX};font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
             f'<div style="display:flex;flex-direction:row;gap:40px;align-items:stretch">{cards}</div></div>')
    return section(s["id"], WHITE, inner + footer(deck, n), "Ways we help (recipe: routes). Website route cards: yellow head, black body, ringed play rows with dotted lines.")


def r_who(s, deck, n, chap):
    # Website block 28, Who it's for (guide pages): large yellow icon circles, bold line, text, centred, three across.
    items = s["items"]; cnt = len(items); cw = (1764 - 60 * (cnt - 1)) // cnt
    cells = "".join(f'<div style="width:{cw}px;display:flex;flex-direction:column;align-items:center;text-align:center">'
                    f'<img src="{asset("who-" + str(ic), W + "plates/who/who-" + str(ic) + ".png")}" alt="" style="width:200px;height:200px">'
                    f'<h3 style="font-family:{FX};font-weight:400;font-size:32px;line-height:1.2;color:{INK};margin-top:36px">{esc(t_)}</h3>'
                    f'<p style="font-family:{FR};font-size:24px;line-height:1.45;color:{INK};margin-top:16px">{esc(d)}</p></div>'
                    for t_, d, ic in items)
    inner = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0]}"></div>'
             f'<div style="position:absolute;left:78px;top:0px;width:1764px;height:969px;display:flex;flex-direction:column;justify-content:center;gap:64px">'
             f'<div style="display:flex;flex-direction:column;gap:16px"><h2 style="font-family:{FX};font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
             + (f'<p style="font-family:{FR};font-size:28px;line-height:1.4;color:{INK}">{esc(s["lead"])}</p>' if s.get("lead") else "")
             + f'</div><div style="display:flex;flex-direction:row;gap:60px">{cells}</div></div>')
    return section(s["id"], WHITE, inner + footer(deck, n), "Who it's for (recipe: who). Website block 28: large icon circles with a bold line and text under each.")


def r_chart(s, deck, n, chap):
    # Bar chart in the website's visual style (fx-bars) and the GC chart generator's: ink bars on a white panel,
    # the bar that matters in yellow with an ink outline, ink baseline, Engram labels. Words left, chart right.
    data = s["data"]; hl = s.get("highlight"); unit = s.get("unit", "")
    W_, H_ = 1040, 640; base = 540; top = 70; mx = max(v for _, v in data) * 1.05
    bw = 120; gap = (W_ - 80 - bw * len(data)) // (len(data) - 1)
    svg = f'<svg viewBox="0 0 {W_} {H_}" aria-label="{esc(s.get("alt", s["title"]))}" style="position:absolute;left:0px;top:0px;width:{W_}px;height:{H_}px">'
    labs = ""
    for i, (lab, v) in enumerate(data):
        x = 40 + i * (bw + gap); hgt = round((base - top) * v / mx); y = base - hgt
        fill = Y if lab == hl else INK
        svg += f'<rect x="{x}" y="{y}" width="{bw}" height="{hgt}" fill="{fill}" stroke="{INK}" stroke-width="4"/>'
        labs += f'<p style="position:absolute;left:{x - 40}px;top:{y - 50}px;width:{bw + 80}px;text-align:center;font-family:{FX};font-size:30px;line-height:1.1;color:{INK}">{esc(s.get("fmt", "{}").format(v))}{unit}</p>'
        labs += f'<p style="position:absolute;left:{x - 40}px;top:{base + 14}px;width:{bw + 80}px;text-align:center;font-family:{FB};font-size:24px;line-height:1.15;color:{INK}">{"<br>".join(esc(q) for q in lab.split("|"))}</p>'
    svg += f'<line x1="20" y1="{base}" x2="{W_ - 20}" y2="{base}" stroke="{INK}" stroke-width="4"/></svg>'
    svg = f'<div style="position:relative;width:{W_}px;height:{H_}px">{svg}{labs}</div>'
    inner = (f'<div style="position:absolute;left:0px;top:0px;width:1920px;height:969px;background:{PAIRS[chap][0]}"></div>'
             f'<div style="position:absolute;left:78px;top:0px;width:600px;height:969px;display:flex;flex-direction:column;justify-content:center;gap:28px">'
             f'<h2 style="font-family:{FX};font-weight:400;font-size:64px;line-height:1.05;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
             f'<p style="font-family:{FX};font-size:30px;line-height:1.25;color:{INK}">{esc(s["standfirst"])}</p>'
             f'<p style="font-family:{FR};font-size:24px;line-height:1.45;color:{INK}">{esc(s["body"])}</p></div>'
             f'<div style="position:absolute;left:738px;top:{(969 - H_ - 120) // 2}px;width:{W_ + 64}px;box-sizing:border-box;background:{WHITE};border:2px solid {INK};padding:32px">'
             f'<p style="font-family:{FX};font-size:28px;line-height:1.2;color:{INK}">{esc(s["chart_title"])}</p>{svg}'
             + (f'<p style="font-family:{FR};font-size:20px;line-height:1.3;color:#4a4a4a">{esc(s["source"])}</p>' if s.get("source") else "")
             + '</div>')
    return section(s["id"], WHITE, inner + footer(deck, n), "Chart (recipe: chart). Website bar style: ink bars, the one that matters in yellow with an ink outline, words left.")


def r_fullphoto(s, deck, n, chap):
    # Full-bleed photo with one big line in black label bars (the website's square label-bar containers).
    ph = asset("full-" + s["photo"], f"{W}plates/photos/full-{s['photo']}.jpg")
    lines = "".join(f'<p style="align-self:flex-start;background:{INK};padding:10px 26px 14px;font-family:{FX};font-size:76px;line-height:1.05;letter-spacing:-1px;color:{WHITE}">{esc(l)}</p>' for l in s["lines"])
    inner = (f'<img src="{ph}" alt="{esc(s.get("alt", ""))}" style="position:absolute;left:0px;top:0px;width:1920px;height:969px;object-fit:cover">'
             f'<div style="position:absolute;left:78px;top:0px;width:1400px;height:969px;display:flex;flex-direction:column;justify-content:{s.get("align", "flex-end")};gap:10px;padding-bottom:90px;box-sizing:border-box">{lines}'
             + (f'<p style="align-self:flex-start;background:{Y};padding:10px 26px;font-family:{FX};font-size:32px;line-height:1.2;color:{INK};margin-top:14px">{esc(s["sub"])}</p>' if s.get("sub") else "")
             + '</div>')
    return section(s["id"], WHITE, inner + footer(deck, n), "Full photo (recipe: fullphoto). One big line in black label bars over a full-bleed photo, for a pause between chapters. Swap the photo for any of Luke's.")


FM = "'Engram Medium', Arial, sans-serif"


def swirl(s):
    # Four swirls: Jim's (99) and Luke's three Canva variations (6, 7, 8), all lifted at the same size and place.
    v = str(s.get("sw", "99"))
    return f'<img src="{asset("squiggle-" + v, W + "plates/master/squiggle-" + v + ".png")}" alt="" style="position:absolute;left:960px;top:0px;width:960px;height:969px">'


def m_left(s, col=INK, sf=Y, w=770):
    """The Canva master template's text column: 72px headline, 37px yellow standfirst, 29px bold intro, 29px body,
    with the template's spacing (41, 34 and 19px)."""
    out = f'<h2 style="font-family:{FX};font-weight:400;font-size:72px;line-height:1.0;letter-spacing:-1px;color:{col}">{esc(s["title"])}</h2>'
    if s.get("standfirst"):
        out += f'<p style="font-family:{FX};font-size:37px;line-height:1.15;color:{sf};margin-top:41px">{esc(s["standfirst"])}</p>'
    if s.get("intro"):
        out += f'<p style="font-family:{FX};font-size:29px;line-height:1.24;color:{col};margin-top:{34 if s.get("standfirst") else 41}px">{esc(s["intro"])}</p>'
    if s.get("body"):
        out += f'<p style="font-family:{FM};font-size:29px;line-height:1.24;color:{col};margin-top:19px;width:{w - 13}px">{esc(s["body"])}</p>'
    return f'<div style="position:absolute;left:73px;top:82px;width:{w}px;display:flex;flex-direction:column">{out}</div>'


def r_mphoto(s, deck, n, chap):
    # Master template, half and half: words left on the chapter colour, a photo filling the right half, Jim's squiggle
    # from plate 99 over its top corner (lifted with its transparency, same place and size).
    out = (f'<div style="position:absolute;left:0px;top:0px;width:960px;height:969px;background:{PAIRS[chap][0]}"></div>'
           f'<img src="{asset("photo-" + s["photo"], f"{W}plates/photos/{s['photo']}.jpg")}" alt="{esc(s.get("alt", ""))}" style="position:absolute;left:960px;top:0px;width:960px;height:969px;object-fit:cover">'
           + swirl(s)
           + m_left(s, sf=s.get("sf", Y)))
    return section(s["id"], WHITE, out + footer(deck, n), "Half and half (recipe: mphoto). From the master template: words left, photo right with Jim's squiggle in the top corner. Swap the photo for any of Luke's.")


def r_mhalves(s, deck, n, chap):
    # Master template page 5: words left on the light colour, more words on the dark half under the squiggle.
    d = s["dark"]
    v = str(s.get("sw", "99"))
    pl = f"halves-99-{chap}" if v == "99" else f"halves-{v}-{chap}"
    out = (full_bg(asset(pl, f"{W}plates/kit/{pl}.jpg")) + m_left(s, sf=s.get("sf", Y))
           + f'<p style="position:absolute;left:1052px;top:337px;width:780px;font-family:{FX};font-size:37px;line-height:1.15;color:{Y}">{esc(d[0])}</p>'
           + f'<p style="position:absolute;left:1052px;top:413px;width:760px;font-family:{FX};font-size:29px;line-height:1.24;color:{WHITE}">{esc(d[1])}</p>'
           + f'<p style="position:absolute;left:1052px;top:{413 + d[3] if len(d) > 3 else 625}px;width:760px;font-family:{FM};font-size:29px;line-height:1.24;color:{WHITE}">{esc(d[2])}</p>')
    return section(s["id"], WHITE, out + footer(deck, n), "Halves (recipe: mhalves). Master template page 5: words left, more words on the dark half under Jim's squiggle.")


def m_pairs(pairs, y0=213, step=175, w=706, col=INK):
    out = ""
    for i, (a, b) in enumerate(pairs):
        out += (f'<div style="position:absolute;left:73px;top:{y0 + i * step}px;width:{w}px;display:flex;flex-direction:column">'
                f'<p style="font-family:{FX};font-size:29px;line-height:1.24;color:{col}">{esc(a)}</p>'
                f'<p style="font-family:{FM};font-size:29px;line-height:1.24;color:{col}">{esc(b)}</p></div>')
    return out


def r_mdrinks(s, deck, n, chap):
    # Master template page 14: drinks and squiggle right, headline and three bold-led points left.
    out = (full_bg(asset(s["plate"], f"{W}plates/{s['plate']}")) +
           f'<h2 style="position:absolute;left:73px;top:82px;width:900px;font-family:{FX};font-weight:400;font-size:72px;line-height:1.0;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
           + m_pairs(s["pairs"], y0=82 + 74 * -(-len(s["title"]) // 25) + 57))
    return section(s["id"], WHITE, out + footer(deck, n), "Drinks right (recipe: mdrinks). Master template page 14: headline and three bold-led points, drinks and squiggle right.")


def r_mband(s, deck, n, chap):
    # Master template pages 16 and 17: two points above, the dark band below with a white lead, body and a yellow line.
    b = s["band"]
    out = (full_bg(asset(s["plate"], f"{W}plates/{s['plate']}")) +
           f'<h2 style="position:absolute;left:73px;top:82px;width:900px;font-family:{FX};font-weight:400;font-size:72px;line-height:1.0;letter-spacing:-1px;color:{INK}">{esc(s["title"])}</h2>'
           + m_pairs(s["pairs"][:2], y0=213)
           + f'<p style="position:absolute;left:73px;top:650px;width:740px;font-family:{FX};font-size:29px;line-height:1.24;color:{WHITE}">{esc(b[0])}</p>'
           + f'<p style="position:absolute;left:73px;top:721px;width:740px;font-family:{FM};font-size:29px;line-height:1.24;color:{WHITE}">{esc(b[1])}</p>'
           + f'<p style="position:absolute;left:73px;top:825px;width:760px;font-family:{FX};font-size:29px;line-height:1.24;color:{Y}">{esc(b[2])}</p>')
    return section(s["id"], WHITE, out + footer(deck, n), "Drinks over a band (recipe: mband). Master template pages 16 and 17: two points above, the dark band below with a yellow closing line.")


def r_mbottles(s, deck, n, chap):
    # Bottles and squiggle right (master contents background), words left in the master template's text column.
    out = full_bg(asset(s["plate"], f"{W}plates/{s['plate']}")) + m_left(s, w=s.get("w", 840), sf=s.get("sf", Y))
    return section(s["id"], WHITE, out + footer(deck, n), "Bottles right (recipe: mbottles). Master template bottles and squiggle, words left in the master text column.")


def r_close(s, deck, n):
    inner = (full_bg(asset("cover-art", W + "ds/project/assets/Shapes/cover-art.webp"))
             + curve.html("cover", [(0, "Why Not Get", 0.5), (1, "In Touch?", 0.5), (2, "Call Us Today", 0.5)], size=120)
             + f'<img src="{asset("logo-ink", W + "ds/project/assets/Logos/logo-ink.svg")}" alt="Good Culture" style="position:absolute;left:1451px;top:700px;width:405px;height:121px;object-fit:contain">'
             + f'<p style="position:absolute;left:1351px;top:852px;width:505px;font-family:{FX};font-size:24px;line-height:1.35;text-align:right;color:{INK}">{s.get("contact", "goodcultureingredients.com<br>hello@goodcultureingredients.com")}</p>'
             + f'<p style="position:absolute;left:1351px;top:1004px;width:505px;font-family:{FR};font-size:20px;text-align:right;color:{INK}">&#169; Good Culture 2026</p>')
    return section(s["id"], "#00b2e7", inner, "Close (recipe: close).")


def build(spec, outdir):
    import os
    os.makedirs(outdir + "/project/slides", exist_ok=True)
    deck = spec["name"]; chap = "sky"; order = []
    for i, s in enumerate(spec["slides"], 1):
        r = s["r"]
        if r == "divider": chap = s["chapter"]
        if r == "cover": h = r_cover(s, deck, i)
        elif r == "close": h = r_close(s, deck, i)
        elif r == "divider": h = r_divider(s, deck, i, chap)
        else: h = globals()["r_" + r](s, deck, i, s.get("chapter", chap))
        open(f'{outdir}/project/slides/{s["id"]}.html', "w").write(h)
        order.append(s["id"])
    return order

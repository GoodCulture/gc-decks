"""Lay a title along Jim's ribbon, one real-text letter at a time.

Each run of the ribbon's centre line was traced from Jim's own artwork (centrelines.json). Letters are Engram
ExtraBold at a fixed size, each a pinned <p> rotated to the curve's tangent, so they stay real, editable text.
"""
import os as _os
GCW = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))) + "/"
REPO = GCW
import json, math, numpy as np
from fontTools.ttLib import TTFont

F = TTFont(GCW + "ds/project/fonts/engram-extrabold.woff2")
UPM = F["head"].unitsPerEm
GS = F.getGlyphSet()
CMAP = F.getBestCmap()
HH = F["hhea"]
CAP = getattr(F["OS/2"], "sCapHeight", 0) or 0.7 * UPM
CL = json.load(open(GCW + "centrelines.json"))


def curve_fn(run):
    c = np.poly1d(run["coef"])
    d = c.deriv()
    return c, d


def arc_table(run, n=1200):
    c, d = curve_fn(run)
    xs = np.linspace(run["x0"], run["x1"], n)
    ys = c(xs)
    s = np.concatenate([[0], np.cumsum(np.hypot(np.diff(xs), np.diff(ys)))])
    return xs, ys, s, d


def layout(art, idx, text, size=128, center_frac=0.5):
    run = CL[art][idx]
    xs, ys, s, d = arc_table(run)
    k = size / UPM
    adv = [GS[CMAP[ord(ch)]].width * k for ch in text]
    total = sum(adv)
    start = s[-1] * center_frac - total / 2
    # metrics for a <p> with line-height:1 (box height = size)
    asc, desc = HH.ascent * k, -HH.descent * k
    half_lead = (size - (asc + desc)) / 2
    baseline = half_lead + asc            # from box top
    cap_mid = baseline - CAP * k / 2      # cap centre from box top
    dd = cap_mid - size / 2               # offset from box centre to cap centre (local, downward)
    out = []
    pos = start
    for ch, a in zip(text, adv):
        m = pos + a / 2
        x = float(np.interp(m, s, xs))
        y = float(np.interp(m, s, ys))
        th = math.atan(d(x))
        if ch != " ":
            w = a + 24
            bx = x + dd * math.sin(th)
            by = y - dd * math.cos(th)
            out.append({"ch": ch, "left": round(bx - w / 2, 1), "top": round(by - size / 2, 1), "w": round(w, 1),
                        "rot": round(math.degrees(th), 2), "cx": x, "cy": y})
        pos += a
    return out, total, s[-1]


def html(art, lines, size=128, col="#0b0b0b"):
    """lines: list of (run index, text, centre fraction)."""
    parts = []
    for idx, text, frac in lines:
        letters, total, length = layout(art, idx, text, size, frac)
        assert total < length * 0.98, (text, total, length)
        for L in letters:
            ch = {"&": "&amp;", "'": "&#8217;"}.get(L["ch"], L["ch"])
            parts.append(
                f'<p style="position:absolute;left:{L["left"]}px;top:{L["top"]}px;width:{L["w"]}px;height:{size}px;'
                f"font-family:'Engram ExtraBold', Arial, sans-serif;font-size:{size}px;line-height:1;text-align:center;"
                f'color:{col};transform:rotate({L["rot"]}deg)">{ch}</p>')
    return "\n".join(parts)


def preview(art, lines, out, size=128, bg="#00b2e7"):
    from PIL import Image, ImageDraw, ImageFont
    import os
    ttf = GCW + "engram-xb.ttf"
    if not os.path.exists(ttf):
        f = TTFont(GCW + "ds/project/fonts/engram-extrabold.woff2"); f.flavor = None; f.save(ttf)
    font = ImageFont.truetype(ttf, size)
    base = Image.new("RGBA", (1920, 1080), bg)
    artim = Image.open(f"{GCW}ds/project/assets/Shapes/{art}-art.webp").convert("RGBA")
    base.alpha_composite(artim)
    for idx, text, frac in lines:
        letters, _, _ = layout(art, idx, text, size, frac)
        for L in letters:
            tile = Image.new("RGBA", (int(L["w"]), size), (0, 0, 0, 0))
            dr = ImageDraw.Draw(tile)
            # emulate CSS line-height:1 box: baseline at half_lead+ascent
            k = size / UPM
            asc, desc = HH.ascent * k, -HH.descent * k
            base_y = (size - (asc + desc)) / 2 + asc
            dr.text((L["w"] / 2, base_y), L["ch"], font=font, fill="#0b0b0b", anchor="ms")
            rot = tile.rotate(-L["rot"], expand=True, resample=Image.BICUBIC)
            cx = L["left"] + L["w"] / 2
            cy = L["top"] + size / 2
            base.alpha_composite(rot, (int(cx - rot.width / 2), int(cy - rot.height / 2)))
    base.convert("RGB").resize((960, 540)).save(out)

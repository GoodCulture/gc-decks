import os as _os
GCW = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))) + "/"
REPO = GCW
import sys; sys.path.insert(0, GCW + "tools")
from gdeck import FX, FR, INK, WHITE, Y, esc, ring_list
from a4plates import X, Y as PY
FB = "'Engram Bold', Arial, sans-serif"


def h(t, size=64, col=INK, lh=1.0):
    return f'<h2 style="font-family:{FX};font-weight:400;font-size:{size}px;line-height:{lh};letter-spacing:-1px;color:{col}">{esc(t)}</h2>'


def p(t, size=26, font=FR, col=INK, lh=1.35, extra=""):
    return f'<p style="font-family:{font};font-size:{size}px;line-height:{lh};color:{col};{extra}">{esc(t)}</p>'


def points(items, size=24, w=860):
    rows = "".join(
        f'<div style="display:flex;gap:18px;align-items:flex-start"><div style="width:13px;height:13px;flex:none;border:4px solid {INK};border-radius:50%;margin-top:{round(size * 0.4)}px"></div>'
        f'<div style="display:flex;flex-direction:column;gap:2px;width:{w}px"><p style="font-family:{FX};font-size:{size}px;line-height:1.25;color:{INK}">{esc(a)}</p>'
        f'<p style="font-family:{FR};font-size:{size}px;line-height:1.3;color:{INK}">{esc(b)}</p></div></div>' for a, b in items)
    return f'<div style="display:flex;flex-direction:column;gap:20px">{rows}</div>'


def tight_list(items, size=24, w=560):
    rows = "".join(f'<div style="display:flex;gap:16px;align-items:flex-start"><div style="width:13px;height:13px;flex:none;border:4px solid {INK};border-radius:50%;margin-top:{round(size * 0.36)}px"></div>'
                   f'<p style="font-family:{FR};font-size:{size}px;line-height:1.25;color:{INK};width:{w}px">{esc(x)}</p></div>' for x in items)
    return f'<div style="display:flex;flex-direction:column;gap:7px">{rows}</div>'


def centre(t, size=27):
    return f'<p style="font-family:{FX};font-size:{size}px;line-height:1.15;text-align:center;color:{INK}">{esc(t)}</p>'


BASES = {
    14: dict(title="Organic Green Fermented Tea Base", band="Manna-K™  |  20x strength  |  Raw or pasteurised",
             paras=["Long-fermented for up to six months, our organic fermented green tea base brings bold levels of organic acids, without the sugar or alcohol.",
                    "Bright, lean, elegant and super refreshing, it's the perfect starting point for a functional drink with wide appeal that feels as good as it tastes."],
             pts=["20x strength", "Stable, consistent and alcohol free", "All natural ingredients", "Supports sugar-free claims", "Increase manufacturing capacity", "Reduce manufacturing lead times"],
             avail="Raw and pasteurised"),
    15: dict(title="Organic Green & Black Fermented Tea Base", band="Manna-KX™  |  30x strength  |  Raw or pasteurised",
             paras=["Fermented with a balanced blend of green and black teas, this base brings together the rich, earthy depth of black tea and the crisp, bright acidity of green tea.",
                    "The result is a powerful, balanced, complex fermented base, ready to help you craft a standout functional drink."],
             pts=["30x strength", "Stable, consistent and alcohol free", "All natural ingredients", "Highest quality", "Reliable, consistent and efficient"],
             avail="Raw and pasteurised"),
    16: dict(title="Organic Black Fermented Tea Base", band="Manna-KN™  |  7x strength  |  Raw or pasteurised",
             paras=["Bold and brewed: this cloudy organic black tea base is deeply fermented, alcohol free and packed with tea character.",
                    "Long fermentation and high tea concentration make it full-bodied and robust. Blend it with our other bases to find your balance of tea and tang."],
             pts=["7x strength", "Stable, consistent and alcohol free", "All natural ingredients", "Increase manufacturing capacity", "Reduce manufacturing lead times"],
             avail="Raw and pasteurised"),
    17: dict(title="Organic Fermented Water Kefir Base", band="Manna-FIR™  |  20x strength  |  Pasteurised",
             paras=["Made with real kefir grains and long-fermented using tea as a nutrient source, this organic base delivers a clean, tart kick, full of lactic acidity and completely dairy free.",
                    "Smooth and versatile, it works with bold, fruity, floral or fresh flavours alike."],
             pts=["20x strength", "Stable, consistent and alcohol free", "All natural ingredients", "Increase manufacturing capacity", "Reduce manufacturing lead times"],
             avail="Pasteurised"),
}
BOXSZ = {14: (320, 194), 15: (320, 194), 16: (320, 194), 17: (325, 202)}


def base(n):
    b = BASES[n]; bw, bh = BOXSZ[n]; sc = 1.32
    return {"r": "page", "id": f"base-{n}", "page": n,
            "imgs": [(f"box{n}", 640, 470, round(bw * sc), round(bh * sc))],
            "parts": [(78, 46, 1080, h(b["title"], 62, lh=1.0)),
                      (78, 218, 1080, p(b["band"], 30, FX, lh=1.0)),
                      (78, 290, 1060, "".join(p(x, 25, FX, lh=1.25) for x in b["paras"])),
                      (78, 470, 580, tight_list(b["pts"])),
                      (78, 712, 400, p("Perfect for:", 26, FX, lh=1.0)),
                      (78, 892, 900, f'<p style="font-family:{FX};font-size:26px;line-height:1;color:{INK}">Available: <span style="font-family:{FR}">{esc(b["avail"])}</span></p>')]}


PAGES = [
 {"r": "page", "id": "cats", "page": 6, "parts": [(78, 54, 1000, h("Build winning drinks across multiple high-growth beverage categories", 60, lh=1.0))]},
 {"r": "page", "id": "nolo", "page": 7, "parts": [(78, 54, 980, h("Supporting you in no/low alc innovation", 64)),
    (78, 210, 960, p("No/low is a core growth pillar. As you scale your mainstream no-alcohol portfolio and explore new formats, keeping flavour depth and balance without alcohol becomes critical.", 30, FX, lh=1.25)),
    (78, 440, 960, p("How we support your innovation:", 28, FX, lh=1)),
    (78, 500, 900, points([("Fermentation-led complexity:", "Authentic depth without dealcoholisation."), ("Faster formulation cycles:", "Production-ready bases skip lengthy fermentation timelines."), ("Scalable through your network:", "Compatible with existing co-packer and production infrastructure.")], 25))
    , (78, 800, 960, p("Whether you're refining existing no/low SKUs or exploring fermentation-led RTDs beyond beer, our bases bring natural complexity that complements your brewing expertise.", 24))]},
 {"r": "page", "id": "functional", "page": 9, "parts": [(78, 54, 980, h("Supporting you in functional beverage innovation", 64)),
    (78, 210, 980, p("Functional beverages are a significant growth opportunity, built on refreshment, hydration and natural ingredients that consumers recognise and trust.", 30, FX, lh=1.25)),
    (78, 400, 960, p("How we support your innovation:", 28, FX, lh=1)),
    (78, 460, 470, points([("Natural fermentation credentials:", "Authentic organic acids and depth from traditional methods."), ("Clean label compatible:", "Simple, recognisable ingredients for health-conscious reformulation.")], 24, 420)),
    (590, 460, 470, points([("Lower sugar potential:", "Fermented acidity reduces sugar needs while keeping the taste."), ("RTD-ready formats:", "Works with existing canning and bottling infrastructure.")], 24, 420)),
    (78, 790, 980, p("Our fermented bases let you explore functional benefits through natural brewing processes, delivering refreshment with depth and keeping claims simple.", 24))]},
 {"r": "page", "id": "building-blocks", "page": 11, "parts": [(78, 54, 800, h("Building winning beverages 101", 64)),
    (78, 260, 740, p("While almost every product is unique, most beverages can be broken down into a few fundamental building blocks.", 32, FX, lh=1.2)),
    (78, 520, 720, p("Legacy ingredients are increasingly rejected by consumers who want natural, functional alternatives that are better for them and the world around them.", 27, FX, lh=1.3))]},
 {"r": "page", "id": "range", "page": 12, "parts": [(78, 54, 1300, h("Introducing the Good Culture range", 64))] +
    [(cx - 240, 300, 480, f'<p style="font-family:{FX};font-size:30px;line-height:1.1;text-align:center;color:{c}">{esc(t)}</p>'
      f'<p style="font-family:{FR};font-size:24px;line-height:1.2;text-align:center;color:{c};margin-top:-8px">{esc(sub)}</p>')
     for cx, t, sub, c in [(240, "Green Tea Base", "20x strength", Y), (721, "Green & Black Tea Base", "30x strength", Y), (1201, "Black Tea Base", "7x strength", Y), (1681, "Water Kefir Base", "20x strength", Y)]]},
 {"r": "page", "id": "magic", "page": 13, "parts": [(78, 46, 1400, h("How the magic happens", 64)),
    (78, 150, 620, p("All of the Good Culture range uses recognisable production methods, with a little sprinkling of magic to make them truly unique.", 28, FX, lh=1.22)),
    (X(13, 300), 150, 1060, p("Organic teas are mixed with organic sugar, filtered water, starter and SCOBY, then left to ferment for up to six months. Over that long fermentation the naturally occurring bacteria and yeast ferment out all the sugars and alcohol, leaving the high levels of organic acids that give our bases their delicious taste, without the residual sugar and alcohol often found in fermented products.", 24, lh=1.35))]},
 base(14), base(15), base(16), base(17),
 {"r": "page", "id": "solutions", "page": 19, "parts": [
    (X19 - 135, 800, 270, centre(t, 25)) for X19, t in [(663, "High quality ingredients"), (947, "Global co-packer network"), (1230, "World-leading product and flavour developers")]]},
]

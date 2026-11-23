import os as _os
GCW = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))) + "/"
REPO = GCW
Y = "#fbe405"; INK = "#000000"; WHITE = "#ffffff"
SF = {"orange": Y, "pink": Y, "teal": Y, "sky": WHITE, "lime": INK}
COPY = [
 ("Consistency at scale", "The same drink, every batch.", "We ferment to a standardised process in SQF and GFSI accredited production.", "Every batch is made to the same spec, so your drink tastes the same every time and your production runs to plan."),
 ("Fermentation done for you", "Up to six months, before it reaches you.", "Every base is long-fermented and always finishes under 0.5% ABV, raw or pasteurised.", "The fermentation is done, tested and repeatable before it reaches your line, so you can focus on building the drink."),
 ("Scale without new tanks", "Use the line you already have.", "Our bases blend straight into your existing production, with no new fermentation equipment.", "You don't have to turn orders down when demand outgrows your tank space. The capacity is already there."),
 ("Launch faster", "From idea to shelf, sooner.", "Skip the months of trial and error that come with building a fermentation process from scratch.", "Tell us what you want to make and we'll point you at the right base, with the technical data your team needs."),
 ("Lower sugar, full flavour", "Acidity and body, without the sugar.", "Our fermented bases add natural acidity and body, so you can use less sugar and keep a full flavour.", "That keeps you on the right side of sugar levies as they tighten, without a drink that tastes thin."),
 ("Clean label by design", "Ingredients consumers recognise.", "Organic, all natural and alcohol free, with nothing on the label your customers need to look up.", "Our bases are certified organic, vegan and non-GMO, with Kosher and Halal certification across the range."),
 ("Support from our team", "Technical help at every stage.", "Our technical team helps you dial in the dose, the spec and the process, from first sample to production.", "We can introduce you to our global network of co-packers and flavour developers."),
 ("Supplied near you", "Stock in four locations.", "We hold stock in the USA, the UK, the Netherlands and Ireland, so you get your ingredients in days.", "Order in 1000L IBCs or bag-in-box, raw or pasteurised, and plan production with confidence."),
]


def left(c, **kw):
    t, sf, i, b = c
    return dict(title=t, standfirst=sf, intro=i, body=b, **kw)


PHOTOS = [("brewer", "orange", "A brewer drawing a sample from a tank"), ("tanks", "pink", "A brewer checking stainless fermentation tanks"),
          ("bottling", "teal", "Green bottles on a bottling line"), ("hardkom", "sky", "Two cans of hard kombucha"),
          ("tasting", "lime", "A brewer checking a sample against the light"), ("kombucha", "orange", "Organic kombucha in a can and a bottle"),
          ("icedtea", "pink", "Two bottles of iced tea"), ("kefir", "teal", "Two bottles of water kefir")]
SLIDES = []
for i, (ph, ch, alt) in enumerate(PHOTOS):
    SLIDES.append({"r": "mphoto", "id": f"m-photo-{ph}", "chapter": ch, "photo": ph, "alt": alt, "sf": SF[ch], **left(COPY[i])})

DARK = [("Ready to blend.", "Each base arrives concentrated, from 7x to 30x, ready to dilute into your recipe.", "Pick the base that fits your drink, or blend two to find your balance of tea and tang."),
        ("No new equipment.", "Our bases work with existing canning and bottling infrastructure.", "Your co-packer or production team blends the base in, and the fermentation is already done."),
        ("Documents as standard.", "We supply spec sheets, certificates and test results with every order.", "So your retailer and your auditor get what they need, first time."),
        ("Built for growth.", "Our bases sit behind thousands of drinks in stores around the world.", "From the first sample to full production runs, the spec stays the same."),
        ("Less waste.", "The same result every batch, so you waste less and rerun less.", "That keeps your costs predictable as you grow.")]
for i, ch in enumerate(["orange", "pink", "teal", "sky", "lime"]):
    c = COPY[(i + 2) % len(COPY)]
    SLIDES.append({"r": "mhalves", "id": f"m-halves-{ch}", "chapter": ch, "sf": SF[ch], "dark": DARK[i], **left(c)})

PAIRS3 = [[("Stable and consistent", "Made to one spec, so every batch tastes the same."), ("All natural ingredients", "Organic, vegan and non-GMO, with a clean label."), ("Ready to blend", "Concentrated and production ready, on your existing line.")],
          [("Kombucha and hard kombucha", "Fermented depth without brewing it yourself."), ("Modern soda and water kefir", "Natural acidity and body with less sugar."), ("No and low alcohol", "Real structure without dealcoholisation.")],
          [("Request a sample", "Pick the base that fits your drink."), ("Trial it in your recipe", "Test it side by side with what you use now."), ("Scale with us", "Order the format you need, from stock near you.")]]
DR = [("final2/90.png", "orange"), ("final2/91.png", "pink"), ("final2/92.png", "teal"), ("kit/drinks-90-sky.jpg", "sky"), ("kit/drinks-90-lime.jpg", "lime")]
TITLES = ["Why our bases", "Built for every category", "Getting started", "What you get", "Where our bases work"]
for i, (pl, ch) in enumerate(DR):
    SLIDES.append({"r": "mdrinks", "id": f"m-drinks-{ch}", "chapter": ch, "plate": pl, "title": TITLES[i], "pairs": PAIRS3[i % 3]})

BAND = [("Simpler production", [("One ingredient, many drinks", "A single base can carry a whole range."), ("Works with your co-packer", "No new equipment, no new process.")],
         ("Long-fermented for up to six months", "Every base finishes under 0.5% ABV, raw or pasteurised.", "So your drink tastes the same, every batch.")),
        ("Quality you can prove", [("SQF and GFSI accredited", "Made in accredited production, with full documents."), ("Certified organic", "Kosher and Halal across the range.")],
         ("Documents as standard", "Spec sheets, certificates and test results with every order.", "Ready for your retailer and your auditor.")),
        ("Room to grow", [("Take bigger orders", "The capacity is already there in the base."), ("Launch new SKUs", "Develop in parallel without slowing core production.")],
         ("Stock in four locations", "The USA, the UK, the Netherlands and Ireland.", "Your ingredients arrive in days."))]
for i, n in enumerate([93, 94, 95, 96, 97, 98]):
    t, pr, b = BAND[i % 3]
    SLIDES.append({"r": "mband", "id": f"m-band-{n}", "chapter": ["orange", "pink", "teal"][i % 3], "plate": f"final2/{n}.png", "title": t, "pairs": pr, "band": b})

for i, n in enumerate([87, 88, 89]):
    ch = ["orange", "pink", "teal"][i]
    SLIDES.append({"r": "mbottles", "id": f"m-bottles-{n}", "chapter": ch, "plate": f"final2/{n}.png", "w": 780, "sf": SF[ch], **left(COPY[(i + 5) % len(COPY)])})

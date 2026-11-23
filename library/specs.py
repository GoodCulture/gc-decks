import os as _os
GCW = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))) + "/"
REPO = GCW
GINGER = {"name": "Organic Ginger Juice", "slides": [
 {"r": "cover", "id": "cover", "title": ["Better Ginger", "In. Better", "Drinks Out."], "label": "[Organic Ginger Juice]", "date": "December 2026"},
 {"r": "contents", "id": "contents", "chapter": "orange", "plate": 87, "items": ["The product", "Why it is better", "At a glance", "Your first batch"]},
 {"r": "divider", "id": "part-one", "chapter": "orange", "title": ["Part One", "About The", "Product"]},
 {"r": "statement", "id": "product", "plate": 23, "title": "High-Quality Organic Peruvian Ginger Juice",
  "standfirst": "Better ginger in. Better drinks out.",
  "body": "Premium organic ginger juice for kombucha, health shots, sodas and non-alcoholic drinks. Grown in Peru, with a strong flavour."},
 {"r": "panel", "id": "why", "kind": "points", "plate": 77, "title": "Why it is better", "standfirst": "Four reasons to make the switch.", "top": 230, "items": [
   {"icon": "Lightning", "title": "Ready from the day it arrives", "text": "Aseptically filled and ready to pour. Three years unopened, chilled."},
   {"icon": "Verified", "title": "Certified organic, farm to pack", "text": "Grown, pressed and packed to certified organic standards. No irradiation."},
   {"icon": "Search", "title": "Tested batch by batch", "text": "Independent accredited lab tests for pesticides, glyphosate and heavy metals."},
   {"icon": "Star", "title": "High in bioactives", "text": "Peruvian ginger is naturally rich in compounds that give it a spicy, sharp bite."}]},
 {"r": "band", "id": "ready", "plate": 96, "title": "Ready from day one", "standfirst": "Pasteurised and filled aseptically, with lemon juice to keep it stable.", "items": [
   {"n": "36", "label": "months unopened, chilled at 0 to 5°C"}, {"n": "3", "label": "pack sizes, from a 1L bag to a 200L drum"}, {"n": "1L", "label": "free sample to trial it"}]},
 {"r": "divider", "id": "part-two", "chapter": "lime", "title": ["Part Two", "Getting", "Started"]},
 {"r": "panel", "id": "glance", "kind": "table", "plate": 78, "title": "At a glance", "standfirst": "Everything your technical team will ask first.", "first": 260, "top": 200, "rows": [
   ["Spec", "Detail"], ["Product", "Organic ginger juice"], ["Origin", "Peru"], ["Certification", "Certified organic"],
   ["Processing", "Pasteurised and filled aseptically, with lemon juice for stability"],
   ["Pack sizes", "1L bag, 20L bag-in-box, 200L drum"], ["Shelf life", "3 years unopened, chilled at 0 to 5°C"],
   ["Availability", "UK and EU from 1 December 2026. USA from 2027"]]},
 {"r": "steps", "id": "first-batch", "title": "Your first batch in three steps", "standfirst": "Start with a free 1L sample.", "steps": [
   ["Request a sample", "Email us for a free 1L bag of organic ginger juice."],
   ["Trial it side by side", "Run it against your current ginger in your own recipe."],
   ["Talk it through", "Our technical team will help you dial in the dose and the spec."]]},
 {"r": "close", "id": "close"}]}

FOUNDERS = {"name": "Building a Better Drink", "slides": [
 {"r": "cover", "id": "cover", "title": ["Building", "A Better", "Drink"], "label": "[For Founders]", "date": "November 2026"},
 {"r": "contents", "id": "contents", "chapter": "teal", "plate": 23, "items": ["Why fermented bases", "What makes ours different", "What you get", "How we work together"]},
 {"r": "divider", "id": "part-one", "chapter": "teal", "title": ["Part One", "Why", "Ferment?"]},
 {"r": "statement", "id": "intro", "plate": 27, "title": "Fermented ingredients. Better beverages.",
  "standfirst": "Ready-to-blend fermented bases, so you can create great-tasting functional drinks and scale them with confidence.",
  "bullets": ["No fermenting in your own facility", "Real flavour and body that flavourings cannot copy", "One supplier from sample to scale"]},
 {"r": "halves", "id": "market", "title": "Kombucha keeps growing", "standfirst": "From a health-store curiosity to a fixture in major multiples.",
  "body": "Europe and Asia Pacific are picking up the pace while mature markets stabilise.",
  "label": "Global kombucha market, $USD billions", "top": 440,
  "bars": [["2020", 2.1, "$2.1B"], ["2022", 3.2, "$3.2B"], ["2024", 4.3, "$4.3B"], ["2026", 5.5, "$5.5B"]],
  "source": "Source: The 2026 Global Kombucha Report, Good Culture."},
 {"r": "panel", "id": "different", "kind": "stats", "plate": 80, "title": "What makes our bases different", "standfirst": "Long fermented, verified and ready to blend.", "items": [
   {"n": "<0.5%", "label": "ABV, verified before every despatch"}, {"n": "7x to 40x", "label": "strengths, to suit your recipe"},
   {"n": "6", "label": "months of fermentation, at most"}, {"n": "10,000", "label": "units, where runs typically start"}]},
 {"r": "divider", "id": "part-two", "chapter": "pink", "title": ["Part Two", "Working", "Together"]},
 {"r": "panel", "id": "you-get", "kind": "points", "plate": 76, "title": "What you get from day one", "standfirst": "The paperwork and the stock, sorted.", "items": [
   {"icon": "Verified", "title": "Accredited and certified", "text": "SQF and GFSI accredited production. Organic, kosher and halal certified."},
   {"icon": "Book", "title": "Documents as standard", "text": "Spec sheets, certificates of analysis batch by batch, allergen statements and traceability."},
   {"icon": "Globe", "title": "Stock close to you", "text": "Held in the USA, the UK, the Netherlands and Ireland."}]},
 {"r": "steps", "id": "steps", "title": "Four steps to your success", "steps": [
   ["Start a conversation", "Tell us your product idea or the problem you want to solve. We will make a clear plan."],
   ["Try our samples", "Ingredient samples and simple recipes you can try yourself, or custom recipes."],
   ["Create your recipe", "We find the best recipe for taste, shelf life, alcohol content and cost."],
   ["Scale up and launch", "From a small sample to full production, with paperwork and partners."]]},
 {"r": "band", "id": "supply", "plate": 93, "title": "Supply that keeps up with you", "standfirst": "Stock held close to where you make your drinks.", "items": [
   {"n": "4", "label": "countries where we hold stock"}, {"n": "1,000+", "label": "partners around the world"}, {"n": "10,000", "label": "units, a typical first run"}]},
 {"r": "close", "id": "close"}]}

_S = [("Request a sample", "Email us for a free 1L bag of organic ginger juice."),
      ("Trial it side by side", "Run it against your current ginger in your own recipe."),
      ("Talk it through", "Our technical team will help you dial in the dose and the spec."),
      ("Place your order", "Order in 1L bags or larger formats, ready for production."),
      ("Scale up", "Move from trial to full runs with the same spec every time."),
      ("Keep it consistent", "Batch paperwork and support for every delivery.")]
_I = [("Certified organic", "Organic ginger, so your label stays short and clean.", "blend0"),
      ("Same every batch", "Made to one spec, so your drink tastes the same every time.", "fix1"),
      ("Fits your line", "Blends straight in, with no new equipment.", "fix2"),
      ("Better margins", "Concentrated, so you ship and store less.", "fix0"),
      ("Quick to market", "Short lead times from sample to production.", "fix5"),
      ("Supplied near you", "Held in the UK, Europe and the USA.", "whoink2")]
COMPONENTS = {"name": "Good Culture Components", "slides": [
 {"r": "steps", "id": "steps-3", "chapter": "lime", "title": "Steps: one row of three", "standfirst": "Approved. Start with a free 1L sample.", "steps": _S[:3]},
 {"r": "steps", "id": "steps-4", "chapter": "lime", "title": "Steps: one row of four", "standfirst": "Start with a free 1L sample.", "steps": _S[:4]},
 {"r": "steps", "id": "steps-2x2", "chapter": "lime", "title": "Steps: two rows of two", "standfirst": "Start with a free 1L sample.", "steps": _S[:4], "rows": [2, 2]},
 {"r": "steps", "id": "steps-3x2", "chapter": "lime", "title": "Steps: two rows of three", "standfirst": "Start with a free 1L sample.", "steps": _S, "rows": [3, 3]},
 {"r": "steps", "id": "steps-3-2", "chapter": "lime", "title": "Steps: three, then two", "standfirst": "Second row lined up on the left.", "steps": _S[:5], "rows": [3, 2]},
 {"r": "steps", "id": "steps-3-2c", "chapter": "lime", "title": "Steps: three, then two centred", "standfirst": "Second row centred under the first.", "steps": _S[:5], "rows": [3, 2], "align": "centre"},
 {"r": "icons", "id": "icons-3", "chapter": "lime", "title": "Icon row: one row of three", "standfirst": "Why brands choose our ginger.", "items": _I[:3]},
 {"r": "icons", "id": "icons-4", "chapter": "lime", "title": "Icon row: one row of four", "standfirst": "Why brands choose our ginger.", "items": _I[:4]},
 {"r": "icons", "id": "icons-2x2", "chapter": "lime", "title": "Icon row: two rows of two", "standfirst": "Why brands choose our ginger.", "items": _I[:4], "rows": [2, 2]},
 {"r": "icons", "id": "icons-3x2", "chapter": "lime", "title": "Icon row: two rows of three", "standfirst": "Why brands choose our ginger.", "items": _I, "rows": [3, 3]},
 {"r": "icons", "id": "icons-3-2", "chapter": "lime", "title": "Icon row: three, then two", "standfirst": "Second row lined up on the left.", "items": _I[:5], "rows": [3, 2]},
 {"r": "icons", "id": "icons-3-2c", "chapter": "lime", "title": "Icon row: three, then two centred", "standfirst": "Second row centred under the first.", "items": _I[:5], "rows": [3, 2], "align": "centre"},
 {"r": "table", "id": "table-full", "chapter": "teal", "title": "Good Culture Range Overview", "first": 250, "rows": [
   ["Product", "MANNA-K", "MANNA-KX", "MANNA-KN", "MANNA-FIR"],
   ["Description", "Organic Sugar Free Green Tea Kombucha Base", "Organic Green & Black Tea Kombucha Base", "Cloudy Organic Sugar-Free Black Tea Kombucha Base", "Organic Fermented Water Kefir Base"],
   ["Strength", "20x", "30x", "7x", "20x"],
   ["Taste", "Fermented taste with no off flavours", "Crisp, a mild tea aroma and mild astringency", "Strong black tea, traditional kombucha flavour", "Tart and lactic, similar to yogurt"],
   ["Dilution", "5% to 7%", "2.5% to 4%", "10% to 17%", "3% to 5%"],
   ["Raw", "5L, 20L, 1000L", "1000L", "5L, 20L, 1000L", "Unavailable"],
   ["Pasteurised", "5L, 20L, 1000L", "1000L", "5L, 20L, 1000L", "5L, 20L, 1000L"]]},
 {"r": "table_side", "id": "table-side", "chapter": "teal", "title": "Organic ginger juice at a glance", "standfirst": "Everything your technical team will ask first.", "body": "Pressed from certified organic Peruvian ginger and filled aseptically, so it arrives stable and ready to blend.", "first": 280, "rows": [
   ["Spec", "Detail"], ["Product", "Organic ginger juice"], ["Origin", "Peru"], ["Certification", "Certified organic"],
   ["Processing", "Pasteurised and filled aseptically, with lemon juice for stability"],
   ["Pack sizes", "1L bag, 20L bag-in-box, 200L drum"], ["Shelf life", "3 years unopened, chilled at 0 to 5°C"],
   ["Availability", "UK and EU from 1 December 2026. USA from 2027"]]},
 {"r": "photo", "id": "photo-kommbru", "chapter": "orange", "photo": "kommbru", "alt": "A can of Komm-Bru botanical ale", "title": "Made with Good Culture", "standfirst": "Real brands, real shelves.",
  "intro": "Our bases sit behind drinks on shelves around the world, from kombucha and modern soda to botanical ales.",
  "body": "Brands come to us with an idea, a problem or a recipe that needs to scale. We supply the fermented base and the technical help to turn it into a drink that tastes the same every time."},
 {"r": "photo", "id": "photo-kombucha", "chapter": "teal", "photo": "kombucha", "alt": "Organic kombucha in a can and a bottle", "title": "One base, many drinks", "standfirst": "Start from a proven foundation.",
  "intro": "A single fermented base can carry a whole range, from a sparkling can to a still bottle.",
  "body": "Add your own flavours, carbonate and package on your existing line. The fermentation work is already done, so you go straight to building your range."},
 {"r": "photo", "id": "photo-brewer", "chapter": "sky", "photo": "brewer", "alt": "A brewer drawing a sample from a tank", "title": "Fermentation done for you", "standfirst": "Skip the months of trial and error.",
  "intro": "Every base is long-fermented, up to six months, and finishes under 0.5% ABV.",
  "body": "Brewing in-house means carrying the fermentation risk yourself. A long, controlled ferment means that risk has been taken care of before the base reaches your line."},
 {"r": "photo", "id": "photo-icedtea", "chapter": "pink", "photo": "icedtea", "alt": "Two bottles of iced tea", "title": "Ready for new categories", "standfirst": "Iced tea, soda, kefir and more.",
  "intro": "Our bases work across the fastest growing drink categories.",
  "body": "Tell us what you are making and we will point you at the right base, with the dilution ratio and the technical data your team needs to get started."},
 {"r": "photo", "id": "photo-tasting", "chapter": "orange", "photo": "tasting", "alt": "A brewer checking a sample against the light", "title": "The same every batch", "standfirst": "Consistency you can plan around.",
  "intro": "We ferment to a standardised process in SQF and GFSI accredited production.",
  "body": "Every batch is made to the same spec, so your drink tastes the same every time and your production runs to plan."},
 {"r": "photo", "id": "photo-kefir", "chapter": "teal", "photo": "kefir", "alt": "Two bottles of water kefir with raspberries and lemons", "title": "Water kefir, made simple", "standfirst": "Dairy-free and ready to blend.",
  "intro": "Our water kefir base gives a tart, lactic taste profile at 20x strength.",
  "body": "It is pasteurised and works across soft drinks, functional water and non-alcoholic cocktails."}
]}
_J = [("The global kombucha market", "Where the category stands and which markets move fastest.", 1),
      ("The challenges producers face", "The predictable problems of scaling without the right base.", 2),
      ("The brewing process, for scale", "What makes commercial production different from home brewing.", 3),
      ("8 commercial recipes", "1,000-litre batches with ratios, shelf life and process steps.", 4),
      ("Our fermented base range", "The four standardised bases behind every recipe.", 5),
      ("Innovation stories", "Six brands rewriting the rules of the category.", 6)]
_JL = "A production guide for manufacturers, co-packers, R&D teams and founders who want technical detail and market context in one place."
for _id, _t, _n, _rows, _al in [("inside-3", "What's inside the guide", 3, None, None), ("inside-4", "What's inside the guide", 4, None, None),
        ("inside-2x2", "What's inside the guide", 4, [2, 2], None), ("inside-3x2", "What's inside the guide", 6, [3, 3], None),
        ("inside-3-2", "What's inside the guide", 5, [3, 2], None), ("inside-3-2c", "What's inside the guide", 5, [3, 2], "centre")]:
    _s = {"r": "jcards", "id": _id, "chapter": "lime", "title": _t, "lead": _JL, "items": _J[:_n]}
    if _rows: _s["rows"] = _rows
    if _al: _s["align"] = _al
    COMPONENTS["slides"].append(_s)

_C = [("Quality and consistency", "quality"), ("Alcohol and compliance", "compliance"), ("Scale and capacity", "capacity"),
      ("Cost and margin", "cost"), ("Supply and continuity", "supply"), ("Reformulating an existing product", "reformulation")]
COMPONENTS["slides"] += [
 {"r": "challenges", "id": "chal-wide", "chapter": "sky", "layout": "wide", "title": "Challenges we help brands to overcome", "items": _C},
 {"r": "challenges", "id": "chal-text", "chapter": "sky", "layout": "text", "title": "Challenges we help brands to overcome", "standfirst": "Whatever is holding your drink back, we have fixed it before.",
  "body": "Pick the problem that sounds most like yours and we will show you how our bases and our technical team solve it.", "items": _C},
 {"r": "challenges", "id": "chal-photo", "chapter": "sky", "layout": "photo", "photo": "tasting", "alt": "A brewer checking a sample against the light", "title": "Challenges we help brands to overcome", "items": _C},
]

_T = [("Book a call and tell us about your idea", "Tell us what you want to make, who it is for and the price you want to reach. We will suggest the best way forward.", "1 day to 1 week"),
      ("Develop and test", "We help you develop your drink step by step, with real samples from our network of flavour developers.", "2 to 4 weeks"),
      ("Make sure it works at scale", "Before production, we help you check the expected cost, supply and production needs.", "1 to 2 weeks"),
      ("Scale and launch", "We work with your production team or co-packer and supply your base, so the drink stays consistent.", "Set by your schedule")]
_TL = "We help you turn your idea into a product that's ready to launch. At each stage, you'll know what happens next."
COMPONENTS["slides"] += [
 {"r": "timeline", "id": "timeline-4", "chapter": "orange", "style": "panel", "title": "Go from an idea to the shelf", "lead": _TL, "stages": _T},
 {"r": "timeline", "id": "timeline-3", "chapter": "orange", "style": "panel", "title": "Go from an idea to the shelf", "lead": _TL, "stages": [_T[0], _T[1], _T[3]]},
 {"r": "timeline", "id": "timeline-4-light", "chapter": "orange", "style": "light", "title": "Go from an idea to the shelf", "lead": _TL, "stages": _T},
]

_PF = [("ABV keeps creeping over the legal limit", "Stable, controlled alcohol as part of the base instead of something to manage"),
       ("A retailer or regulator wants documentation you don't have", "We supply spec sheets, certificates and test results as standard"),
       ("You need certification, or an audit you can actually pass", "We're SQF and GFSI accredited, with Organic, Kosher and Halal certification across our range"),
       ("You're not sure your labelling or claims are compliant", "We give labelling and claims guidance as part of the relationship"),
       ("Unstable alcohol is putting you at risk on tax and duty", "We remove the variable that creates the exposure in the first place")]
COMPONENTS["slides"] += [
 {"r": "problemfix", "id": "problemfix-5", "chapter": "orange", "rows": _PF},
 {"r": "problemfix", "id": "problemfix-3", "chapter": "orange", "title": "Alcohol and compliance", "rows": _PF[:3]},
]

_F = dict(title="Get the consistent beverage your customers expect, every single time",
          body="Every base is fermented for up to six months and always finishes under 0.5% ABV, raw or pasteurised. The fermentation is done, tested and repeatable before it reaches your line.",
          more="Brew in-house, or use a short-fermented base, and that risk stays with you: batches that vary, ABV creep and months of trial and error. We take it on for you.",
          facts=[("Up to 6 months", "Long-fermented", "Every base is fermented for up to six months."), ("Under 0.5% ABV", "Always", "Whether you take it raw or pasteurised."),
                 ("Ready to blend", "Plug-and-play", "The fermentation work is already done.")])
COMPONENTS["slides"] += [
 dict(r="facts", id="facts-panel", chapter="teal", style="panel", **_F),
 dict(r="facts", id="facts-light", chapter="teal", style="light", **_F),
]

COMPONENTS["slides"] += [
 {"r": "retail", "id": "retail-panel", "chapter": "sky", "style": "panel", "title": "Trusted by leading brands.<br>Sold in leading retailers"},
 {"r": "retail", "id": "retail-band", "chapter": "lime", "style": "band", "title": "Good Culture products are used in beverages sold in stores around the world"},
]

_CB = "We meet strict food safety and quality standards. Our ingredients hold SQF, Organic, Kosher and Halal certification. We also give you the product details, test results and certificates your team needs to approve us quickly."
COMPONENTS["slides"] += [
 {"r": "certs", "id": "certs-white", "title": "Certified ingredients. Ready for retail.", "body": _CB},
 {"r": "certs", "id": "certs-colour", "chapter": "lime", "colour": True, "title": "Certified ingredients. Ready for retail.", "body": _CB},
]

_BI = [("Scaling challenges", "scaling"), ("Capacity constraints", "capacity"), ("Restricted shelf life", "shelflife"), ("Quality issues", "quality"), ("Capital expenditure pressures", "capex")]
COMPONENTS["slides"] += [
 {"r": "bigicons", "id": "bigicons-5", "chapter": "pink", "title": "Good Culture exists to help our customers overcome the challenges they face to realising their full potential", "items": _BI},
 {"r": "bigicons", "id": "bigicons-4", "chapter": "pink", "title": "Good Culture exists to help our customers overcome the challenges they face to realising their full potential", "items": _BI[:4]},
]

_SC = [("$26.28bn", "The second-largest functional segment", "Functional water is the second-largest of the eight functional beverage segments, inside a market already past $220bn."),
       ("35%", "The growth is coming from function, not hydration", "What sells now is water with one clear benefit. Probiotics make up about 35% of the functional ingredients used."),
       ("4.5g", "Sugar regulation helps this category more than any other", "The UK levy drops its threshold to 4.5g per 100ml in January 2028, and functional water starts on the right side of it.")]
COMPONENTS["slides"] += [
 {"r": "statcards", "id": "statcards-3", "title": "Functional water: everything has to work at 2%", "lead": "Functional water is the hardest brief in the drinks aisle and the one that looks easiest.", "cards": _SC},
 {"r": "statcards", "id": "statcards-3-colour", "chapter": "sky", "colour": True, "title": "Functional water: everything has to work at 2%", "lead": "Functional water is the hardest brief in the drinks aisle and the one that looks easiest.", "cards": _SC},
]

COMPONENTS["slides"] += [
 {"r": "casestudy", "id": "case-beer", "chapter": "sky", "title": "European Functional Beer Brand",
  "challenge": "A Belgian brand was creating functional-first alcohol-free beers in the IPA style, with plans to distribute across European markets initially.",
  "body": "Their core SKU had been performing well, but scaling production looked difficult once they added new SKUs. They thought they would have to delay new products and focus only on their core SKU to avoid bottlenecks.",
  "solution": ["Provided our Organic Green Fermented Tea Base, Organic Black Fermented Tea Base and Organic Fermented Water Kefir Base.", "Supported experimentation on development of a new SKU.", "Enabled parallel development without compromising core production."],
  "result": "The new SKU is progressing quickly, while they've also been able to focus on scaling their current SKU more efficiently in the EU market. They now have a roadmap to new products, which they aim to release just before summer 2026."},
 {"r": "casestudy", "id": "case-kefir", "chapter": "lime", "title": "UK Functional Beverage Brand",
  "challenge": "A UK-based brand had a clear vision: launch a premium probiotic water kefir that could compete in the growing functional beverage market.",
  "body": "But they knew that handling fermentation production themselves would be challenging, requiring significant capital investment, specialised expertise, and delaying their market entry by months.",
  "solution": ["Provided our Organic Fermented Water Kefir Base (20x concentrated, production-ready).", "Connected them with a trusted UK co-packer from our network.", "Supported rapid product development without capital expenditure."],
  "result": "They moved from idea to launch much faster, bypassing production complexity entirely. Today they're selling one of the better-tasting modern functional beverages in the UK market, with a scalable production model that grows with their business."},
]

_SC4 = _SC + [("116", "Every levy that tightens helps", "At least 116 countries tax sugary drinks, and functional water starts on the right side of every threshold.")]
_i = [s["id"] for s in COMPONENTS["slides"]].index("statcards-3")
COMPONENTS["slides"].insert(_i + 1, {"r": "statcards", "id": "statcards-4", "title": "Functional water: everything has to work at 2%", "lead": "Functional water is the hardest brief in the drinks aisle and the one that looks easiest.", "cards": _SC4})
# Removed by Luke in the deck (20 Nov)
COMPONENTS["slides"] = [s for s in COMPONENTS["slides"] if s["id"] not in ("inside-3x2", "inside-3-2", "inside-3-2c", "retail-band", "statcards-3-colour")]

COMPONENTS["slides"] += [
 {"r": "global", "id": "global-site", "chapter": "sky", "style": "site", "title": "Providing a world-class service, wherever you are",
  "facts": [("1,000+", "Partners worldwide", "We work with brands, co-packers and flavour developers around the world."),
            ("In thousands of drinks", "Delighting consumers worldwide", "Our base is the foundation of thousands of drinks across multiple categories."),
            ("Global distribution", "We ship from four locations", "Ingredients from stock nearby, in days, not months.")]},
 {"r": "global", "id": "global-deck", "chapter": "orange", "style": "deck", "title": "A global company with quality and service at its heart",
  "items": [("Global distribution", "distribution"), ("Expert technical support", "support"), ("Based on 10+ years of R&D", "rnd"),
            ("Supported by co-packers", "copackers"), ("Readily available stock", "stock"), ("Accredited by leading certification bodies", "accredited")]},
]

import pages as _pages
COMPONENTS["slides"] += _pages.PAGES

SALES = [
 {"r": "cover", "id": "s-cover", "title": ["Cultivating", "The Future", "Of Beverages"], "label": "[Company Overview]", "date": "[Month Year]"},
 {"r": "contents", "id": "s-contents", "chapter": "sky", "plate": 87, "items": ["Who we are", "How we help", "Why our bases", "Our range", "Working together"]},
 {"r": "divider", "id": "s-divider", "chapter": "sky", "title": ["Part One", "Who We", "Are"]},
 {"r": "statement", "id": "s-statement", "chapter": "sky", "plate": 23, "title": "The fermented bases behind thousands of drinks",
  "standfirst": "We supply long-fermented, ready-to-blend bases to brands, co-packers and flavour developers around the world.",
  "body": "The fermentation is done, tested and repeatable before it reaches your line, so you can focus on building the drink."},
 {"r": "routes", "id": "s-routes", "chapter": "sky", "title": "How can we help your business?", "routes": [
   ("We can help you to create a new drink", "Tell us your idea and we'll take it from first sample to shelf with you.", ["Kombucha and hard kombucha", "Water kefir and modern soda", "No and low alcohol", "Something else"]),
   ("We can help you to fix a problem", "From batches that don't match to ABV creeping over the limit.", ["Reduce costs", "Improve quality and consistency", "Scale up and launch faster", "Lower alcohol levels"])]},
 {"r": "who", "id": "s-who", "chapter": "sky", "title": "Who we work with", "lead": "Most of our partners see themselves in one of these.", "items": [
   ("Launching a new drink brand", "You need a production process that's scalable, compliant and commercially viable from day one.", 1),
   ("Making drinks and hitting limits", "Batches that vary, alcohol limits, no room to grow, rising costs: we solve these production problems.", 2),
   ("Adding a new category", "Co-packers, manufacturers and brand owners use our bases to move into fermented functional drinks.", 3)]},
 {"r": "compare", "id": "s-compare", "chapter": "teal", "title": "Why brands choose a long-fermented base",
  "lead": "Brew in-house, or use a short-fermented base, and the fermentation risk stays with you. With ours, it's already been taken care of.",
  "cols": ["Brew in-house", "Short-fermented base", "Good Culture base"],
  "rows": [["Fermentation", "Your tanks, your time, every batch", "A short ferment, finished on your line", "Up to six months, done before it reaches you"],
           ["Consistency", "Batches that vary", "Batches that vary", "Made to one standardised process, every batch"],
           ["Alcohol", "ABV can creep over the limit", "ABV can creep over the limit", "Always under 0.5% ABV, raw or pasteurised"],
           ["Equipment", "Fermentation tanks, space and expertise", "Your existing line", "Your existing line, no new equipment"],
           ["Time to launch", "Months of trial and error", "Testing and adjusting", "Ready to blend from day one"]]},
 {"r": "chart", "id": "s-chart", "chapter": "orange", "title": "Where the growth is in functional drinks",
  "standfirst": "The functional beverage market is already past $220bn and forecast to reach $300bn by the end of the decade.",
  "body": "Our bases work across every one of these segments, from energy drinks and RTD tea to functional water and modern soda.",
  "chart_title": "Market size by segment ($bn)", "unit": "bn", "fmt": "${}", "highlight": "Functional|water",
  "data": [("Energy|drinks", 82.58), ("RTD tea|and coffee", 40.1), ("Functional|water", 26.28), ("Enhanced|juice", 5.41), ("Modern|soda", 2.81)],
  "source": "Source: Good Culture market analysis. Five of the eight functional beverage segments."},
 {"r": "supply", "id": "s-supply", "chapter": "lime", "title": "Ordering and supply",
  "standfirst": "Stock held near you, ready to ship.",
  "body": "Wherever you make your drinks, we supply from stock nearby, so you get your ingredients in days and can plan production with confidence.",
  "facts": [("Strength", "7x to 30x concentrate, ready to blend"), ("Formats", "Raw or pasteurised (water kefir pasteurised only)"),
            ("Pack sizes", "1000L / 264 US gal IBC, or bag-in-box"), ("Stock held in", "The USA, the UK, the Netherlands and Ireland"),
            ("Certified", "SQF, GFSI, Organic, Kosher and Halal"), ("Samples", "Available to buy from our online shop")]},
 {"r": "steps", "id": "s-next", "chapter": "lime", "title": "Your next steps", "standfirst": "From first sample to first order, we're with you at every stage.",
  "steps": [("Request a sample", "Pick the base that fits your drink and we'll send a sample."), ("Trial it in your recipe", "Test it side by side with what you use now."),
            ("Talk to our team", "Our technical team helps you dial in the dose and the spec."), ("Place your first order", "Order the format you need, shipped from stock near you.")]},
 {"r": "close", "id": "s-close"},
]
COMPONENTS["slides"] += SALES

_i = [s["id"] for s in COMPONENTS["slides"]].index("s-statement")
COMPONENTS["slides"].insert(_i + 1, {"r": "fullphoto", "id": "s-photo", "photo": "tanks", "alt": "A brewer checking stainless fermentation tanks",
  "lines": ["Up to six months of", "fermentation, done for you."], "sub": "So you can focus on building the drink."})

import master as _master
COMPONENTS["slides"] += _master.SLIDES

for _s in COMPONENTS["slides"]:
    if _s["id"] in ("chal-text", "timeline-4", "timeline-3", "problemfix-3", "s-supply"): _s["swirl"] = True
    if _s["id"] == "case-beer": _s.update(photo="tasting", alt="A brewer checking a beer against the light")
    if _s["id"] == "case-kefir": _s.update(photo="kefir", alt="Two bottles of water kefir")

# Four swirls in rotation (Luke, 23 Nov): Jim's 99 and Luke's Canva variations 6, 7 and 8, so neighbours never repeat.
_cyc = ["99", "6", "7", "8"]; _i = 0
for _s in COMPONENTS["slides"]:
    if _s.get("swirl") or _s["r"] in ("mphoto", "mhalves"):
        _s["sw"] = _cyc[_i % 4]; _i += 1

# Full-colour slides (steps, icon rows, What's inside) cycle the four swirls too (Luke, 23 Nov).
_i = 0
for _s in COMPONENTS["slides"]:
    if _s["r"] in ("steps", "icons", "jcards") and not _s.get("flat"):
        _s["sw"] = _cyc[_i % 4]; _i += 1

# Stat cards on colour (Luke, 23 Nov).
for _s in COMPONENTS["slides"]:
    if _s["id"] == "statcards-3": _s.update(colour=True, chapter="orange")
    if _s["id"] == "statcards-4": _s.update(colour=True, chapter="teal")

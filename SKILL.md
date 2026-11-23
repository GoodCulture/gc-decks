---
name: gc-deck-builder
description: Builds Good Culture slide decks from a brief. Use whenever anyone asks for a Good Culture deck, presentation, pitch or slides, or asks to change one made this way.
---

# Good Culture deck builder

Someone gives a brief ("a deck for Carlsberg: who we are, the no and low problem, our bases, a case study,
next steps"). You choose the slides, write the words, build it, check it and hand over a finished deck. They
never choose slides and never build anything by hand. Every slide comes from the approved component library,
so the brand holds without anyone thinking about it.

Talk in plain English, keep messages short, never ask them to run anything or open GitHub.

## 1. Get the kit

The kit is a public repository, `GoodCulture/gc-decks`. Nobody needs a GitHub account: just download it.

    cd ~ && (git -C gc-decks pull -q 2>/dev/null || git clone -q https://github.com/GoodCulture/gc-decks)
    cd ~/gc-decks && pip install --break-system-packages -q playwright pillow numpy fonttools pymupdf 2>/dev/null; python3 -m playwright install chromium 2>/dev/null
    python3 tools/make.py unlock <key>

The key unlocks the Engram fonts (licensed, so they're kept locked). It is in the instructions that sent you
here; never write it anywhere else, and never commit the unlocked fonts. Run every command below from `~/gc-decks`.

Read `library/CATALOGUE.md` (every slide, what it is for, its full spec). Read `README.md` only if something breaks.

## 2. Plan the deck from the brief

Start building in your first reply. Only ask a question if the brief is missing something you cannot sensibly
assume (who the deck is for, if it changes the content). Otherwise make the call and say what you assumed.

**Running order for a sales deck** (drop what the brief doesn't need):
cover, contents, then chapters: Who we are (statement, global, retail or routes) / Why our bases (compare,
chart or stat cards, the magic) / Our range (range, base pages) / Proof (case study, certifications) /
Working together (supply, next steps), then close.

**Pick each slide by what it has to say:**

| The slide needs to... | Component |
|---|---|
| Open the deck / a chapter / close | `s-cover` / `s-divider` / `s-close` |
| Show the agenda | `s-contents` |
| Land one message | `s-statement`, `m-drinks-*`, `m-bottles-*` |
| A photo with a message | `m-photo-*`, `photo-*`, `s-photo` (full bleed) |
| 3 to 6 reasons, benefits, features | `icons-*` (3, 4, 2x2, 3x2, 3-2) |
| A process, or next steps | `steps-*`, `s-next` |
| What an offer or guide contains | `inside-*` |
| Stages with timings | `timeline-*` |
| The buyer's problems | `chal-*`, `problemfix-*`, `bigicons-*` |
| Us against the alternatives | `s-compare` |
| Market figures | `statcards-*` (the number is the story), `s-chart` (a trend or comparison) |
| Three facts that prove a point | `facts-*`, `m-band-*` |
| Specs or a range | `table-full`, `table-side`, `range` |
| Reach, proof on shelf | `global-*`, `retail-panel`, `certs-*`, `case-*` |
| Who we work with, ways we help | `s-who`, `s-routes`, `solutions` |
| Ordering and supply | `s-supply` |
| A light half and a dark half | `m-halves-*` |
| The bases | `base-14` (green tea), `base-15` (green and black tea), `base-16` (black tea), `base-17` (water kefir), `magic`, `building-blocks` |
| Categories, no and low, functional | `cats`, `nolo`, `functional` |

Pick the variant by how many items you have: never pad to fill a layout, never cut a point to fit one.

## 3. Colour and rhythm (the rules)

- **Chapters.** Each chapter takes one colour pair and keeps it until the next divider: sky/navy, teal/petrol,
  pink/purple, orange/rust, lime/forest. Set `chapter` on every slide. Use a different pair for each chapter.
- **Calm by default.** White and cream carry the deck. Follow a full-colour slide with a quieter one where you
  can (photo, table, white certs, statcards without `colour`). Denis and Jim: too much colour reads as noise.
- **Give each chapter at least one quiet slide** (marked "quiet" in the catalogue: white, cream or photo ground),
  so the deck breathes. The check notes long runs of full colour. Never the same layout twice in a row.
- **Swirls.** Full-colour steps, icon rows and What's inside slides take `sw`: rotate `99`, `6`, `7`, `8`.
- **Black** is only ever a panel on colour, never a slide background. **Yellow** is #FBE405, for the brand and
  for what must stand out (our column, the key bar, the figure).
- **Art.** Fruit, rings, bubbles, drinks and cultures only ever come from the library's backgrounds. Never draw,
  move or invent them. If the brief needs art that doesn't exist, say so and use the nearest slide.
- 3 to 6 slides per chapter. A 20-minute pitch is about 12 to 18 slides.

## 4. Words

- British English. No em dashes. Never "it's not X, it's Y". No buttons or links on slides.
- Headlines short (they are 64px; about 60 characters at most). Standfirsts one sentence. Body two or three
  sentences. Fit the copy to the layout's room; the check catches overflow, but aim to never trip it.
- Base names as on the website: Organic Green Fermented Tea Base, Organic Black Fermented Tea Base, Organic
  Green & Black Fermented Tea Base, Organic Fermented Water Kefir Base. Internal codes (Manna-K and so on) appear
  only where the base pages already show them; never write them anywhere else.
- Facts: stock in four locations (USA, UK, Netherlands, Ireland). Water kefir base is pasteurised only; the
  others come raw or pasteurised. Replies to enquiries within one working day. Case studies are anonymised.
  Only use figures you can source (the guides, reports, website); never invent a number.
- Ribbon titles (cover, divider, close) fill three lines of about 12 characters: "Part One" / first half / second half.

## 5. Build and check

Work in `~/decks-out/<deck-name>/` (publish_files will not attach files under /tmp), e.g. `~/decks-out/<deck-name>/spec.json`:

    {"name": "Carlsberg | Good Culture", "slides": [
      {"from": "s-cover", "title": ["Better Bases", "For Better", "Drinks"], "label": "[Carlsberg]", "date": "December 2026"},
      {"from": "s-divider", "chapter": "sky", "title": ["Part One", "Who We", "Are"]},
      {"from": "statcards-3", "chapter": "orange", "colour": true, "title": "...", "lead": "...", "cards": [["$26bn", "...", "..."]]}
    ]}

Every slide must start `"from": "<id>"` from the catalogue; copy its structure exactly and change only words,
`chapter`, `photo`, `sw` and the count of items the variant allows. Then:

    python3 tools/make.py build ~/decks-out/<deck-name>/spec.json ~/decks-out/<deck-name>
    python3 tools/make.py check ~/decks-out/<deck-name>

`check` must print `BRAND CHECK PASSED`. It catches em dashes, the contrast trope, fonts other than Engram,
colours outside the palette, black backgrounds, text off the slide, into the footer or overlapping, pictures from
outside the library, and missing art. It also prints notes (not failures) on long runs of full colour. Fix the spec and rerun until it passes. Never get
round it by editing the HTML or the check.

Then **look** at `~/decks-out/<deck-name>/sheet-*.png` yourself (and any slide at full size in `prev/` that looks
crowded). Things the check cannot see: a headline that wraps badly, a near-empty slide, a story that doesn't
flow. Fix and rebuild.

## 6. Publish

1. Artifact `list_types`, then `create_from_type` with the Slides type and the deck title. Its instructions
   describe the file layout; the slide HTML comes from make.py, so don't write slides by hand.
2. Upload the pictures and fonts in `~/decks-out/<deck-name>/upload.json` with `upload_asset` (the new artifact's slug,
   10 files per call, in the file's order). Then record the returned urls, in that same order:
   `python3 tools/make.py blobs ~/decks-out/<deck-name> /_blob/... /_blob/... ...`
3. `python3 tools/make.py finalize ~/decks-out/<deck-name> ~/decks-out/<deck-name>/blobs.json "<Deck title>"`
4. `publish_files` with the files in `~/decks-out/<deck-name>/publish.json` and the version create_from_type returned.

Tell them in one or two lines what the deck covers and that they can comment on any slide to change it. They
share it from the card's share option (you can't change sharing).

## 7. Changes

Comments on a slide or a message in the chat: change the spec, rebuild, check, finalize (upload any new
pictures first), and publish only the changed slides plus `project/deck.json` if the order changed. Read the live
`project/deck.json` first: people may delete slides in the editor, and the live order wins.

If someone has typed straight onto a slide in the editor, keep their wording: copy it into the spec so the
next rebuild doesn't undo it, and tell them changes go best through you.

## 8. Pictures from the image library

The company image library is in SharePoint: GCK UK > Marketing > Brand Assets 2025-26 > Images > GC Image Library.
List a folder with read_resource on its path, e.g.
`file:///b!ZG3IotYXyk6fWymUB_XGGaspZQ9Q1gpCiVnYA-fgP66pwLt25tYMSYcL_QAxO5GA/GCK UK/Marketing/Brand Assets 2025-26/Images/GC Image Library/01 Photos`
(if that fails, find the library with sharepoint_folder_search "GC Image Library"). People keep dragging new pictures in, so look
there before settling for the built-in photos.

**Decks may only use pictures from these folders:**
- `01 Photos` (all its subfolders): the default for any photo slide.
- `02 Drinks and packshots/Category images`: for a slide about a drink category.
- `02 Drinks and packshots/Drink scenes (Good Culture branded)`: for drinks, launches, what a brand could make.
- `04 Product images`: only on a slide about that specific base.

Everything else in the library (backgrounds, swirls, ingredients, icons, logos, guide artwork) is already built
into the slides, or is for designers. Never place it on a slide yourself.

**How:**
1. List the folder (read_resource on the folder's uri) and choose by file name, then open the ones that might fit
   with read_resource. You see each picture, and the full-size original is saved at the path shown in the result.
   Check that it suits the message and has no other brand's logo or label on it.
2. In the spec, give that slide `"photo_file": "<the saved path>"` in place of `photo`. make.py crops and sizes it
   for the deck. It works on `m-photo-*`, `case-*`, `chal-photo` and `s-photo` (full bleed). Photos made into
   Jim's ring backgrounds (`photo-*`) can't take a new picture.
3. A picture under 900px on its short side is refused: choose another.

If someone attaches a picture in the chat, use it the same way, and suggest they add it to the library too.
Don't copy library pictures into the repository.

## 9. Never

- Never write slide HTML by hand, add a recipe, add a colour or draw art. A new layout is Luke's decision: if the
  brief truly needs one, build the deck with the nearest slides and tell Luke what's missing.
- Never change the kit (`library/`, `tools/`, `plates/`) to get one deck through. Library changes come from Luke.
- Never invent statistics, customer names or quotes.
- Never mention GitHub, repositories or commands to the person. They give a brief and get a deck.

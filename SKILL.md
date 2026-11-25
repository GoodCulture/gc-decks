---
name: gc-deck-builder
description: Builds Good Culture slide decks from a brief. Use whenever anyone asks for a Good Culture deck, presentation, pitch or slides, or asks to change one made this way.
---

# Good Culture deck builder

Someone gives a brief ("a deck for Carlsberg: who we are, the no and low problem, our bases, a case study,
next steps"). You choose the slides, write the words, build it, check it and hand over a finished deck. They
never choose slides and never build anything by hand. Every slide comes from the approved component library,
so the brand holds without anyone thinking about it.

The brand check keeps a deck on-brand. It does not make it good. A deck that passes the check can still be flat,
samey or built from the safest slides. Your job is the good part: section 3 says what that means.

Talk in plain English, keep messages short, never ask them to run anything or open GitHub.

## 1. Get the kit

The kit is a public repository, `GoodCulture/gc-decks`. Nobody needs a GitHub account: just download it.

    cd ~ && (git -C gc-decks pull -q 2>/dev/null || git clone -q https://github.com/GoodCulture/gc-decks)
    cd ~/gc-decks && pip install --break-system-packages -q playwright pillow numpy fonttools brotli pymupdf 2>/dev/null; python3 -m playwright install chromium 2>/dev/null
    python3 tools/make.py unlock <key>

The key unlocks the Engram fonts (licensed, so they're kept locked). It is in the instructions that sent you
here; never write it anywhere else, and never commit the unlocked fonts. Run every command below from `~/gc-decks`.

Read `library/CATALOGUE.md` (every slide, what it is for, its full spec and its tags). Read `README.md` only if
something breaks.

## 2. Plan the deck

Start work in your first reply. Only ask a question if the brief is missing something you cannot sensibly
assume (who the deck is for, if it changes the content). Otherwise make the call and say what you assumed.

Plan in this order:

1. **Read the reference deck closest to the brief** in `examples/` (its README and its contact sheet):
   `short-8` for a brief of up to about 10 pages, `pitch-18` for a full pitch. They show what section 3 looks
   like in practice. Match their balance, not their exact slides.
2. **Look in the image library before choosing photo slides** (section 9). Find the pictures that fit this
   brief first, then pick slides that can show them. A deck with no library pictures needs a reason.
3. **Choose the slides** by what each has to say (table below), then check the plan against section 3 before
   you build.

**Running order for a sales deck** (drop what the brief doesn't need):
cover, contents, then chapters: Who we are (statement, global, retail or routes) / Why our bases (compare,
chart or stat cards, the magic) / Our range (range, base pages) / Proof (case study, certifications) /
Working together (supply, next steps), then close.

**Length.** A 20-minute pitch is about 12 to 18 slides, with contents and a divider per chapter, 3 to 6 slides
per chapter. A short deck (10 pages or fewer) drops the contents and the dividers: they would eat a quarter of
the deck. Its chapters are two to four slides each, and the change of chapter colour marks the change of
subject. Count cover and close in the page count.

**Pick each slide by what it has to say:**

| The slide needs to... | Component |
|---|---|
| Open the deck / a chapter / close | `s-cover` / `s-divider` / `s-close` |
| Show the agenda | `s-contents` |
| Land one message | `s-statement`, `m-drinks-*`, `m-bottles-*` |
| A photo with a message | `m-photo-*`, `photo-*`, `s-photo` (full bleed) |
| 3 to 6 reasons, benefits, features | `icons-*` (3, 4, 2x2, 3x2, 3-2) |
| A process, or next steps | `steps-*`, `s-next` |
| A workflow where the arrows matter: steps that branch into two outcomes | `flow-6`, `flow-4` (3 to 6 steps) |
| Stages with their entry, action and outcome criteria | `criteria-3` (2 to 4 stages) |
| Routes or lanes, with who owns each | `lanes-2` (2 or 3 routes) |
| A numbered list of measures, metrics or checks | `list-swirl` |
| What an offer or guide contains | `inside-*` |
| Stages with timings | `timeline-*` |
| The buyer's problems | `chal-*`, `problemfix-*`, `bigicons-*` |
| Us against the alternatives | `s-compare` |
| Market figures | `statcards-*` (the number is the story), `s-chart` (a trend or comparison) |
| Three facts that prove a point | `facts-*`, `m-band-*` |
| Specs or a range | `table-full`, `table-side`, `range` (`-swirl` versions carry a swirl top right) |
| Reach, proof on shelf | `global-*`, `retail-panel`, `certs-*`, `case-*` |
| Who we work with, ways we help | `s-who`, `s-routes`, `solutions` |
| Ordering and supply | `s-supply` |
| A light half and a dark half | `m-halves-*` |
| The bases | `base-14` (green tea), `base-15` (green and black tea), `base-16` (black tea), `base-17` (water kefir), `magic`, `building-blocks` |
| Categories, no and low, functional | `cats`, `nolo`, `functional` |

Pick the variant by how many items you have: never pad to fill a layout, never cut a point to fit one.

## 3. What good looks like

Aim for every one of these. The check notes most of them when they're missing.

- **Every chapter reads as one colour block.** Every slide in it sits on that chapter's colour pair, so you can
  tell where a chapter starts and ends from the contact sheet alone (section 4).
- **Variety comes from layout, not from dropping the colour.** Within a chapter, mix full colour, a photo half,
  and a black panel on the colour, so no two slides feel the same.
- **At least one swirl slide in any deck of five or more body slides**, two or more in a pitch. The swirls are
  what makes a deck look like Good Culture. Slides tagged `swirl` in the catalogue carry them: steps, icon rows,
  What's inside, `m-photo-*`, `m-halves-*`, `s-next`, `s-supply`.
- **Real pictures where they earn it.** Use library photos (section 9) on the slides tagged
  `takes a library photo` whenever a picture fits the message better than the built-in one. A person at work, a
  drink in context or a production scene beats a second text slide.
- **Every slide does a different job.** No layout twice, and watch for repeated art too: `s-contents` and
  `s-statement` share the same bottles, so don't put them next to each other.
- **The story moves.** Market or problem, then how we help, then proof, then what happens next. Each chapter
  answers one question, and the colour changes when the question does.
- **Pick for the message first.** If the right slide doesn't come in the chapter's colour, change the chapter's
  colour or pick the nearest slide that does, never drop out of the colour.

## 4. Colour (the rules)

- **Consistent colour per chapter. This is the main colour rule.** Each chapter takes one colour pair and keeps it
  on every slide until the next chapter: sky/navy, teal/petrol, pink/purple, orange/rust, lime/forest. Set
  `chapter` on every slide and use a different pair for each chapter. For an orange chapter, all of these are
  right: a full orange slide, a slide that's half orange and half photo, a black panel on orange. A slide on
  white, cream or another chapter's colour is wrong.
- **White and cream are the exception.** The library has very few white or cream slides (tagged `off-chapter`).
  They never carry the deck and are never used to break up colour. Use one only when nothing on the chapter's
  colour can say the same thing, and tell the person why.
- **Fixed-colour slides.** Some slides have their colour in the art, so `chapter` can't change it: they're tagged
  `fixed colour` in the catalogue (`functional` is always pink, `base-15` always teal, every `photo-*`,
  `m-drinks-*`, `m-band-*`, `m-bottles-*` and so on). Only use one in a chapter of its colour, or choose the
  chapter colour to suit it. The check fails a fixed-colour slide in the wrong chapter.
- **Swirls.** Swirl slides take `sw`: rotate `99`, `6`, `7`, `8` through the deck so neighbours never repeat.
- **Black** is only ever a panel on colour, never a slide background. **Yellow** is #FBE405, for the brand and
  for what must stand out (our column, the key bar, the figure).
- **Art.** Fruit, rings, bubbles, drinks and cultures only ever come from the library's backgrounds. Never draw,
  move or invent them. If the brief needs art that doesn't exist, say so and use the nearest slide.

## 5. Words

- British English. No em dashes. Never "it's not X, it's Y". No buttons or links on slides.
- Headlines short (they are 64px; about 60 characters at most). Standfirsts one sentence. Body two or three
  sentences. Fit the copy to the layout's room; the check catches overflow, but aim to never trip it.
- Base names as on the website: Organic Green Fermented Tea Base, Organic Black Fermented Tea Base, Organic
  Green & Black Fermented Tea Base, Organic Fermented Water Kefir Base. Internal codes (Manna-K and so on) appear
  only where the base pages already show them; never write them anywhere else.
- Facts: stock in four locations (USA, UK, Netherlands, Ireland). Water kefir base is pasteurised only; the
  others come raw or pasteurised. Replies to enquiries within one working day. Case studies are anonymised.
  Only use figures you can source (the guides, reports, website, or the library's own copy); never invent a number.
- Ribbon titles (cover, divider, close) fill three lines of about 12 characters: "Part One" / first half / second half.

## 6. Build, check and look

Work in `~/decks-out/<deck-name>/`, e.g. `~/decks-out/<deck-name>/spec.json`:

    {"name": "Carlsberg | Good Culture", "slides": [
      {"from": "s-cover", "title": ["Better Bases", "For Better", "Drinks"], "label": "[Carlsberg]", "date": "December 2026"},
      {"from": "s-divider", "chapter": "sky", "title": ["Part One", "Who We", "Are"]},
      {"from": "statcards-3", "chapter": "orange", "title": "...", "lead": "...", "cards": [["$26bn", "...", "..."]]}
    ]}

Every slide must start `"from": "<id>"` from the catalogue; copy its structure exactly and change only words,
`chapter`, `photo` or `photo_file`, `sw` and the count of items the variant allows. Then:

    python3 tools/make.py build ~/decks-out/<deck-name>/spec.json ~/decks-out/<deck-name>
    python3 tools/make.py check ~/decks-out/<deck-name>

`check` must print `BRAND CHECK PASSED`. It fails em dashes, the contrast trope, fonts other than Engram, colours
outside the palette, black backgrounds, text off the slide, into the footer or overlapping, pictures from outside
the library, missing art and any slide whose colour doesn't match its chapter (including fixed-colour slides in
the wrong chapter). Fix the spec and rerun until it passes.
Never get round it by editing the HTML or the check.

It also prints **notes**: a white or cream slide, no swirl slide, no library pictures, the same layout twice.
Treat each note as a question you must answer. Fix it, or keep it only if fixing it would mean a worse slide for the message, and tell the person why
in one line.

Then **look** at `~/decks-out/<deck-name>/sheet-*.png` yourself, next to the reference deck's contact sheet,
and open any slide in `prev/` that looks crowded. Ask:

- Would Denis and Jim recognise this straight away as a Good Culture deck? Is there enough colour and swirl?
- Does each chapter read as one colour block, with every slide on its colour pair?
- Is there a slide that's nearly empty, or a headline that wraps badly?
- Does any art, photo or layout repeat?
- Read only the headlines in order: do they tell the story of the brief?

Fix and rebuild until the answer to all five is right.

## 7. Publish

1. Artifact `list_types`, then `create_from_type` with the Slides type and the deck title. Its instructions
   describe the file layout; the slide HTML comes from make.py, so don't write slides by hand.
2. Upload the pictures and fonts in `~/decks-out/<deck-name>/upload.json` with `upload_asset` (the new artifact's
   slug, 10 files per call, in the file's order). Then record the returned urls, in that same order:
   `python3 tools/make.py blobs ~/decks-out/<deck-name> /_blob/... /_blob/... ...`
3. `python3 tools/make.py finalize ~/decks-out/<deck-name> ~/decks-out/<deck-name>/blobs.json "<Deck title>"`
4. `publish_files` with the files in `~/decks-out/<deck-name>/publish.json` and the version create_from_type
   returned. If it refuses to attach a file because of where it is, copy the files listed in `publish.json` into
   a folder it accepts (such as `/mnt/user-data/outputs/<deck-name>/`) and send them from there with the same
   `as` paths.

Tell them in one or two lines what the deck covers and that they can comment on any slide to change it. They
share it from the card's share option (you can't change sharing).

## 8. Changes

Comments on a slide or a message in the chat: change the spec, rebuild, check, finalize (upload any new
pictures first), and publish the changed slides plus `project/deck.json` if the order changed. Adding or removing
a slide changes the page number in the footer of every slide after it, so publish those too. Read the live
`project/deck.json` first: people may delete slides in the editor, and the live order wins.

If someone has typed straight onto a slide in the editor, keep their wording: copy it into the spec so the
next rebuild doesn't undo it, and tell them changes go best through you.

## 9. Pictures from the image library

The company image library is in SharePoint: GCK UK > Marketing > Brand Assets 2025-26 > Images > GC Image Library.
List a folder with read_resource on its path, e.g.
`file:///b!ZG3IotYXyk6fWymUB_XGGaspZQ9Q1gpCiVnYA-fgP66pwLt25tYMSYcL_QAxO5GA/GCK UK/Marketing/Brand Assets 2025-26/Images/GC Image Library/01 Photos`
(if that fails, find the library with sharepoint_folder_search "GC Image Library"). The Microsoft 365 tools may
need loading first. People keep dragging new pictures in, so look every time. If you can't reach the library,
say so in your reply rather than skipping it quietly.

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
   for the deck. It works on the slides tagged `takes a library photo`: `m-photo-*`, `case-*`, `chal-photo` and
   `s-photo` (full bleed). Photos made into Jim's ring backgrounds (`photo-*`) can't take a new picture.
3. A picture under 900px on its short side is refused: choose another.

If someone attaches a picture in the chat, use it the same way, and suggest they add it to the library too.
Don't copy library pictures into the repository.

## 10. Never

- Never write slide HTML by hand, add a recipe, add a colour or draw art. A new layout is Luke's decision: if the
  brief truly needs one, build the deck with the nearest slides and tell Luke what's missing.
- Never change the kit (`library/`, `tools/`, `plates/`, `examples/`) to get one deck through. Library changes
  come from Luke.
- Never invent statistics, customer names or quotes.
- Never mention GitHub, repositories or commands to the person. They give a brief and get a deck.

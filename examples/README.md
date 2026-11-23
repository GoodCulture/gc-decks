# Reference decks

Two decks that show what good looks like. Read the one closest to your brief before planning, and look at its
contact sheet. Both pass the brand check. Build either one to see it:

    python3 tools/make.py build examples/short-8.json ~/decks-out/example
    python3 tools/make.py check ~/decks-out/example

They use the built-in photos because library pictures can't live in this repository. In a real deck, the slides
marked **library photo** below should get a picture from the SharePoint image library (`photo_file`) whenever one
fits the message better.

## short-8: a short brief (5 to 8 pages)

"5 to 8 pages on the functional beverage market and how we can help." Contact sheet: `short-8.jpg`.

| # | Slide | Why it's there |
|---|---|---|
| 1 | `s-cover` | Ribbon title in three short lines. |
| 2 | `s-chart` (orange) | The market in one picture. |
| 3 | `statcards-3` (orange) | The three figures behind the trend, on the same orange. |
| 4 | `m-photo-tanks` (pink) | Opens "how we help": half pink, half photo, with a swirl. **Library photo.** |
| 5 | `timeline-4` (pink) | How working with us runs: a black panel on pink. |
| 6 | `icons-4` (pink) | Four reasons, full pink with a swirl. |
| 7 | `case-kefir` (lime) | Proof, in its own colour so it lands as its own moment. **Library photo.** |
| 8 | `s-close` | |

What makes it work:
- **Each chapter is one colour block.** Orange for the market, pink for how we help, lime for proof. You can see
  where each chapter starts from the contact sheet alone.
- **Variety within a chapter comes from layout:** the pink chapter goes photo half, black panel, full colour.
- **No dividers or contents.** In 8 slides they would take a quarter of the deck. The colour change does their job.
- **Two swirl slides** (4 and 6).
- **No layout twice.**

## pitch-18: a full company pitch (12 to 18 pages)

A 20-minute company overview. Contact sheets: `pitch-18-a.jpg`, `pitch-18-b.jpg`.

| Chapter | Slides |
|---|---|
| Who we are (sky) | `s-who`, `global-site` (black panel on sky), `certs-colour` |
| Why our bases (orange) | `s-chart`, `facts-panel` (black panel on orange), `m-photo-brewer` (swirl, **library photo**) |
| Our range (teal) | `range`, `base-15` (always teal, so it sits in the teal chapter) |
| Working together (lime) | `case-kefir` (**library photo**), `timeline-4` (black panel on lime), `s-next` (swirl) |

What makes it work:
- **Cover, contents, a divider per chapter, close.** At this length the structure helps people follow along.
- **Every slide sits on its chapter's colour**, as full colour, a photo half or a black panel on the colour.
- **Fixed-colour slides sit in their own colour's chapter** (`base-15` is always teal).
- **The one exception is `range`**, which is on white. It's the only slide that shows the whole range at once,
  so nothing on teal can say the same thing. The check notes it, and that's the right answer to the note.
- **The contents and the statement slide share their bottles art**, so this deck uses `s-who` instead of
  `s-statement` after the contents. Watch for repeated art as well as repeated layouts.

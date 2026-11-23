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
| 2 | `s-chart` (orange) | The market in one picture. Full colour: the chapter's energy. |
| 3 | `statcards-3-cream` | The three figures behind the trend. Cream: the chapter's quiet slide. |
| 4 | `m-photo-tanks` (pink) | Opens "how we help" on a person and a swirl. **Library photo.** |
| 5 | `timeline-4-light` (pink) | How working with us runs. White: the chapter's quiet slide. |
| 6 | `icons-4` (pink) | Four reasons, on colour with a swirl. |
| 7 | `case-kefir` (lime) | Proof, from a different colour so it lands as its own moment. **Library photo.** |
| 8 | `s-close` | |

What makes it work:
- **No dividers or contents.** In 8 slides they would take a quarter of the deck. The chapter colours still change
  (orange, pink, lime) so the story moves on visibly.
- **Every chapter of two or more slides has one quiet slide and one with energy.** Never two full-colour slides of
  the same chapter back to back.
- **Two swirl slides** (4 and 6), so the deck feels like Good Culture and doesn't read flat.
- **No layout twice.** Each slide does a different job.

## pitch-18: a full company pitch (12 to 18 pages)

A 20-minute company overview. Contact sheets: `pitch-18-a.jpg`, `pitch-18-b.jpg`.

| Chapter | Slides | The quiet one | The energy |
|---|---|---|---|
| Who we are (sky) | `s-who`, `global-site`, `certs-white` | `certs-white` | `s-who` |
| Why our bases (orange) | `s-chart`, `s-photo`, `m-photo-brewer` | `s-photo` (**library photo**) | `m-photo-brewer` (swirl, **library photo**) |
| Our range (teal) | `range`, `base-15` | `range` | `base-15` (always teal, so it sits in the teal chapter) |
| Working together (lime) | `case-kefir`, `timeline-4-light`, `s-next` | `timeline-4-light` | `s-next` (swirl) |

What makes it work:
- **Cover, contents, a divider per chapter, close.** At this length the structure helps people follow along.
- **Each chapter has three moods at most:** something quiet, something on full colour, and where it fits a photo.
- **Fixed-colour slides sit in their own colour's chapter** (`base-15` is always teal).
- **The contents and the statement slide share their bottles art**, so this deck uses `s-who` instead of
  `s-statement` after the contents. Watch for repeated art as well as repeated layouts.

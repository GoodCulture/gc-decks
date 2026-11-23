# Good Culture deck kit

Claude builds Good Culture slide decks from a brief with this kit: approved slide templates, Jim's art, and a
brand check every deck must pass. People never use this repository directly; they give Claude a brief.

- `SKILL.md`: how Claude uses the kit, start to finish.
- `library/specs.py`: every approved slide (`COMPONENTS`); `library/CATALOGUE.md` is generated from it by
  `python3 tools/catalogue.py`.
- `tools/gdeck.py`: the recipes that turn a slide spec into a 1920x1080 slide. `tools/make.py`: build, check,
  finalise.
- `plates/`, `ds/`, `public/`: backgrounds, photos, icons. The Engram fonts are licensed and kept locked
  (`*.woff2.enc`); the key is in the deck skill, never in this repository.

Changes to the library are Luke's call. Live library deck: https://claude.ai/artifact/UWKNyLDdei5ubWNbC5vtbG

# Flashcard Authoring Guide

<a name="_TOP_"></a>

This page is the template and style guide for every flashcard in this repository — it isn't a flashcard itself. For the actual starting position and the first links into the opening tree, see [A00 Start Position](./A00_Start.md).

---

## Page skeleton

> *Set the title of the page with `<ECO CODE> <Opening Name>` followed by the move sequence `<1. xx yy 2. zz aa>`*

*`<Add here a short description of the main characteristics of this position (opening, trap, mate pattern, ...).`* <br>
*`Sources for the description may be a Lichess description, a video introduction (e.g. Daniel Naroditsky, Levy Rozman, Igor Smirnov, ...), an opening book, ...>`*

---

<a name="_initial_move_"></a>

## The position

*`<The diagram below is rendered live from the FEN in the URL: no screenshot is stored in the repository.`* <br>
*` Click the board to open it on the Lichess analysis board, where the position is fully interactive and the opening explorer is one panel away.>`*

```
[![<caption>](https://backscattering.de/web-boardimage/board.svg?fen=<BOARD>&lastMove=<uci>&coordinates=true&size=320)](https://lichess.org/analysis/standard/<FULL_FEN_WITH_UNDERSCORES>)

<full FEN in a code block, so GitHub's copy button can feed it straight to the Lichess mobile app>

<!-- lichess-stats:start fen="<FULL FEN>" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="8" -->
...generated table...
<!-- lichess-stats:end -->
```

> [!IMPORTANT]
> Everything between `lichess-stats:start` and `lichess-stats:end` is **overwritten** by `tools/update_stats.py`. Edit the attributes on the opening marker, never the table itself.

### Candidate moves

*`<List candidate moves, with a short summary of the strategy behind each one>`* <br>
*`<Candidate moves may be: moves of the main line(s), moves pertaining to a named opening or variation (e.g. Italian - Guico Piano), moves with different popularity between masters games and bullet/blitz (usually indicating traps/tactic partterns), moves highlighted in books/videos/websites, moves worth to be mentionned from a specific game>`* <br>
*`<Moves are listed here below with a link to an anchor in this page or a new page: for uncommon moves, highlighted special moves, dubious moves, moves in bullets/blitz, a note or a tip is created in this page. For a specific variation worth a deeper analysis, a new page is created. The main line of an opening remains on this page unless the main line breaks into equivalent popular multiples lines>`* <br>
*`<Mention the Stockfish evaluation of the move in parentheses>`* <br>
*`<When the move leads to a new variation name, place the name with a link to the page analyzing this variation>`* <br>
*`<Examples below>`* <br>

* [**1. `<uncommon_move>`**](#_uncommon_note_) (-0.x): *`<for uncommon moves illustrated in books/videos, create a note to highlight the discussion>`*
* [**1. `<Mate or Trap Pattern>`**](#_mate_or_trap_) (-0.x): *`<create a tip when a mate pattern or a trap pattern should be highlighted>`*
* [**1. `<move>`**](#_move_) (x.x): *`<main moves are discussed after the notes and tips; they can be reached by clicking the internal anchor link — click on the move>`*

[*Back to TOP*](#_TOP_)

---

## Notes & Tips

> [!NOTE]
> Notes gather side variations worth mentioning, although they are not part of the main line of this flash card.

A `[!NOTE]` or `[!TIP]` callout is a full blockquote, not just its opening line. Every line that belongs to the side note — the anchor, the heading, the diagram, the FEN code block, the stats table, and the "Back to" links — is prefixed with `>` (a blank line inside the blockquote is written as a bare `>`), so GitHub renders the whole side note as one boxed callout. This keeps side branches visually distinct from the main line: a reader scanning the page sees at a glance which content is "on the path" and which is a side note to come back from. The blockquote ends right after the "Back to" links; the `---` separator that follows stays outside it. A worked example, in full, lives on [B01 Scandinavian Defense](./e4_openings/B01_Scandinavian.md#_e5_) (2. e5) — its own `[!NOTE]` block is exactly this shape.

Skeleton:

```
> [!NOTE]
> <one-line summary of the side variation>
>
> <a name="_uncommon_note_"></a>
>
> ### 1. <uncommon move worth a note>
>
> <diagram, FEN code block, stats table, as in "The position" above>
>
> [*Back to previous move*](#_initial_move_)
```

> [!TIP]
> Tips highlight mate patterns and traps, to help spotting them in real games.

Tips follow the same skeleton as notes, anchored under a heading like `### 1. <Mate Pattern or Trap Pattern worth a tip>`. Add the tip when a mate pattern or a trap pattern should be highlighted — it helps recognise the pattern in real games, in order to either avoid a trap or use it against the opponent. The worked example on [Grob's Attack](./A00_openings/Grob.md#_mate_or_trap_) (1. g4 e5 2. f3?? — the shortest game) shows a full tip, mate pattern included.

---

<a name="_move_"></a>

### 1. `<move>`

*`<Present subsequent moves with the same structure as the initial move>`* <br>
*`<FEN diagram, generated Lichess statistics block, list of candidate moves, notes and tips when needed...>`*

[*Back to previous move*](#_initial_move_)
[*Back to TOP*](#_TOP_)

---

## How to use this template

### Diagrams

Nothing is stored in `pics/` any more except the `icon_*` files. A diagram is a single line built from the FEN:

```
[![<caption>](https://backscattering.de/web-boardimage/board.svg?fen=<BOARD>&lastMove=<uci>&coordinates=true&size=320)](https://lichess.org/analysis/standard/<FULL_FEN_WITH_UNDERSCORES>)
```

* `<BOARD>` is **only the piece placement field** of the FEN, i.e. everything before the first space. No space means no URL-encoding to worry about.
* `lastMove` uses UCI notation (`g2g4`) and highlights the two squares like Lichess does.
* Useful extras: `orientation=black` for Black-to-play cards, `arrows=Rd8h4` (colour prefixes `G`/`B`/`R`/`Y`) to show a threat, `squares=f2,g2` to mark weak squares, `size=` to shrink boards inside notes.
* `<FULL_FEN_WITH_UNDERSCORES>` is the complete FEN with spaces replaced by underscores. Append `#explorer` to land directly on the opening explorer panel.

### Statistics

Wrap each table in a marker pair; `tools/update_stats.py` queries the Lichess explorer and rewrites what is in between:

```
<!-- lichess-stats:start fen="<FULL FEN>" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="8" -->
...generated table...
<!-- lichess-stats:end -->
```

| Attribute | Applies to | Default | Notes |
| :--- | :--- | :--- | :--- |
| `fen` | both | *required* | Full FEN. Single source of truth for the card. |
| `db` | — | `lichess,masters` | Which databases to query. |
| `speeds` | online only | `bullet,blitz` | `ultraBullet`, `bullet`, `blitz`, `rapid`, `classical`, `correspondence`. |
| `ratings` | online only | `1800,2000,2200,2500` | Buckets run from their value to the next one, so "1800+" must list them all. |
| `since` / `until` | masters only | — | Years, e.g. `since="1952"`. The Masters database ignores `speeds` and `ratings`. |
| `moves` | both | `8` | Number of continuations to list. |
| `bars` | both | `10` | Squares in the W/D/B bar. `0` disables it, `5` narrows the column on phones. |

Each diagram is followed by a code block holding the full FEN. GitHub shows a copy button on it, which is the practical way to load the position in the Lichess **mobile app**: the app captures every `lichess.org` link but only routes a few paths internally, so an `/analysis/<fen>` link lands on its home screen instead of the position. Copying the FEN sidesteps that entirely. On desktop the diagram link works as expected.

That code block is written by hand, alongside the diagram it belongs to. `update_stats.py` does not generate it, but it warns when the FEN of a statistics block cannot be found just above it — which catches the two copies drifting apart after an edit.

Squares are allocated by largest remainder, so a bar always totals exactly `bars` squares. A share under half a square disappears: at `bars="10"` a 4% draw rate shows no 🟫 square. Win/draw/black percentages are hidden below 20 games in a database: on a two-game sample they would be noise. The ⚠ flag marks moves that are played online but nearly unseen in the Masters database.

### Card depth and when to split into a new card

A "main" card — an opening survey rather than a gambit/trap/pattern card — stays bounded to three moves past its own title position: the same depth as B01's own Overview (root → White's 2nd → Black's 2nd → White's 3rd). Content that would go deeper spins off into its own card instead, the way B01's exd5 branch produced the Modern and Blackburne-Kloosterboer cards rather than growing past that depth itself. This keeps every main card's diagram a consistent, legible size as the number of cards grows — depth becomes width (more cards) instead of height (deeper cards).

Gambit, trap and mate-pattern cards (Tennison, Blackmar-Diemer, and similar) are exempt from that limit: depth is the actual subject there, not a byproduct to trim. Their diagrams can run past three levels when the page's own anchors support it — unfold a forced-looking reply (a "3. Nc3" or "3. Ng5" with its own section) into its own node rather than folding it into the edge to the next real choice, the way B01, Tennison and Blackmar-Diemer's diagrams all do. But stay legible rather than mapping every sub-line: Blackmar-Diemer's own diagram still stops one level before the page's prose does (4. f3 and 5. Qxf3/Nxf3 stay prose-only) — use judgement about where a diagram stops earning its keep, even on an exempt card.

### Content diagram (optional)

For a card with enough branches to be worth a map, an "Overview" section near the top can hold a fishbone-style Mermaid flowchart: the main line runs as a straight spine, side lines and traps branch off it. GitHub renders `mermaid` code fences natively, so no image is generated or stored. See B01's Overview for a worked example.

* Each node's label is the move exactly as written in a "### Candidate moves" bullet elsewhere on the page (e.g. `"2. exd5 !<br/>+0.5"`), optionally followed by `!`/`!!`/`?`/`??`/⚠ on the move line and the Stockfish eval on the next line via `<br/>`. These stay editorial calls — nothing checks whether a `!` is chess-correct.
* The node's **shape** is a data-driven claim, checked against that move's own row in this page's stats tables — not decoration:

  | Shape | Mermaid syntax | Claims | Threshold |
  | :--- | :--- | :--- | :--- |
  | ▭ rectangle | `id["text"]` | unclassified | doesn't cleanly meet another threshold |
  | ▭▭ subroutine | `id[["text"]]` | master-safe | masters ≥ 20% |
  | ◇ rhombus | `id{"text"}` | blitz trap | masters < 2%, online ≥ 3%, **and** online is at least 8× the masters share |
  | ⬭ stadium | `id(["text"])` | understudied everywhere | masters < 2% **and** online < 3% |
  | ⬡ hexagon | `id{{"text"}}` | punishable blunder | eval ≥ 0.9 worse than its best sibling |

  This is the repository's actual differentiator from books and other opening sites: the online/masters gap surfaces which "natural-looking" moves are really blitz traps (rhombus) worth knowing both to spring and to meet, separately from lines nobody has studied much anywhere (stadium) — a source of repertoire variety, not just a warning. The 8× ratio (rather than a flat online-percentage floor) is deliberate: a move that's rare in masters but still played 3%+ online is already a large relative gap even when its raw online share looks modest, and these tables only cover 1800+ rated online play to begin with — a gambit better known below that floor (club-level, casual blitz) will look even more under-represented here than it really is, so the bar for calling it a trap should stay low, not high.
* Give the line this card follows deeper the `:::main` class (defined once as `classDef main stroke-width:3px;`) for a thicker border — independent of shape, since the followed line and the statistically "safest" line aren't always the same node (a side reference can be master-safe without being where this card goes next). Don't add custom fill/stroke colours: GitHub's Mermaid theme auto-adapts to light/dark, and a hardcoded colour won't.
* Every node needs a matching `click <id> "<target>"` line: `"#_anchor_"` for a section on the same page, or a full `https://github.com/onclemarcel/chess_flashcards/blob/main/...` URL for another card. GitHub itself doesn't make these clickable (it strips `click` interactivity), but they still work as machine-checkable link targets, and some editor Mermaid previews do render them as links.
* A `click` line can carry a third quoted argument — `click <id> "<target>" "<tooltip>"` — which Mermaid renders as the node's SVG `<title>`, shown as a native hover tooltip in any renderer that keeps it. Use it for `"<ECO> · <variation name>"`, e.g. `"B01 · Scandinavian Defense: Mieses-Kotroc Variation"`; for a position with no distinct name of its own, repeat its nearest *named* ancestor's ECO/name rather than inventing one or leaving it blank — that's what Lichess's own opening explorer does too. Source it from the explorer response's `opening` field (same live query `update_stats.py` already makes), not from memory.

`tools/check_diagram.py` catches drift between the diagram and the prose/tables it summarises: a node's move text not found verbatim in the page, an eval that doesn't appear near that move's bullet, a `⚠` the prose doesn't back up, a shape whose claimed category doesn't match that move's own stats-table row, a hexagon whose eval swing against its best sibling is under 0.9, or a `click` target whose anchor/file doesn't exist. It does not judge whether a `!`/`?` annotation is chess-correct, or generate the diagram — both stay hand-authored. Run it the same way as the stats updater:

```
python tools/check_diagram.py                  # whole repository
python tools/check_diagram.py path/to/card.md   # one file
```

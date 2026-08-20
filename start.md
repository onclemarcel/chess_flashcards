# Start Position (A00)

<a name="_TOP_"></a>

> *Set the title of the page with `<Opening Name (ECO Code)>` followed by the move sequence:*
> *`1. <w1> <b1>` / `2. <w2> <b2>` ...*

*`<Add here a short description of the main characteristics of this position (opening, trap, mate pattern, ...). Sources for the description may be a Lichess description, a video introduction (e.g. Daniel Naroditsky, Levy Rozman, Igor Smirnov, ...), an opening book, ...>`*

---

<a name="_initial_move_"></a>

## The position

*`<The diagram below is rendered live from the FEN in the URL: no screenshot is stored in the repository. Click the board to open it on the Lichess analysis board, where the position is fully interactive and the opening explorer is one panel away.>`*

[![Start position](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR_w_KQkq_-_0_1)

*... Start Position — click the board to analyse it on Lichess*

```
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

### Lichess statistics

Two databases are shown side by side: **Online** (bullet and blitz, 1800+) and **Masters** (over-the-board elite games). A move that is popular online but absent from the Masters database is flagged with a warning sign — that gap is usually where the traps live.

The W/D/B columns carry a ten-square bar: ⬜ White wins · 🟫 draws · ⬛ Black wins. It reads at a glance and needs no styling — GitHub strips `style` attributes, so a real cell background is not an option.

<!-- lichess-stats:start fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="8" -->

| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| — | — | — | — | — | |

*Not generated yet — run `python tools/update_stats.py start.md`*
<!-- lichess-stats:end -->

> [!IMPORTANT]
> Everything between `lichess-stats:start` and `lichess-stats:end` is **overwritten** by `tools/update_stats.py`. Edit the attributes on the opening marker, never the table itself.

### Candidate moves

*`<List here the possible moves, with a short summary of the strategy behind each one>`*
*`<Create an internal link to a paragraph on this page, or an external link when the move transposes to another opening>`*
*`<Mention the Stockfish evaluation of the move in parentheses>`*

* [**1. `<uncommon_move>`**](#_uncommon_note_) (-0.x): *`<for uncommon moves illustrated in books/videos, create a note to highlight the discussion>`*
* [**1. `<Mate or Trap Pattern>`**](#_mate_or_trap_) (-0.x): *`<create a tip when a mate pattern or a trap pattern should be highlighted>`*
* [**1. `<move>`**](#_move_) (x.x): *`<main moves are discussed after the notes and tips; they can be reached by clicking the internal anchor link — click on the move>`*

From the starting position, White chooses how to open the game. Opening theory is extensively documented in books and on the Internet, with golden rules for beginners (piece development, control of the centre, pawn structure, ...):

* [**1. e4**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B00_e4_KPG.md) (+0.2): the [King's Pawn Opening](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B00_e4_KPG.md) is the most popular first move at all levels of the game. White aims at controlling the centre.

---

> [!NOTE]
> Notes gather side variations worth mentioning, although they are not part of the main line of this flash card.

<a name="_uncommon_note_"></a>

### `<uncommon move worth a note>`

*`<Add here notes from books/videos/web sites about a specific move or variation worth mentioning, although not in the main line of this flash card>`*

Example:

* With **1. g4**, White enters the [Grob's Attack](https://github.com/onclemarcel/chess_flashcards/blob/main/g4_opening/Grob.md), significantly compromising the kingside pawn structure and placing the g-pawn on an unusual square that is difficult to defend without giving Black the initiative.

[![1. g4](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pppppppp/8/8/6P1/8/PPPPPP1P/RNBQKBNR&lastMove=g2g4&coordinates=true&size=280)](https://lichess.org/analysis/standard/rnbqkbnr/pppppppp/8/8/6P1/8/PPPPPP1P/RNBQKBNR_b_KQkq_g3_0_1)

*... 1. g4 — the Grob's Attack*

```
rnbqkbnr/pppppppp/8/8/6P1/8/PPPPPP1P/RNBQKBNR b KQkq g3 0 1
```

| ![Lichess](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_lichess.png) | Very Rare | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | -0.9 |
| --- | --- | --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/pppppppp/8/8/6P1/8/PPPPPP1P/RNBQKBNR b KQkq g3 0 1" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="5" -->

| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| — | — | — | — | — | |

*Not generated yet — run `python tools/update_stats.py start.md`*
<!-- lichess-stats:end -->

[*Back to previous move*](#_initial_move_)

---

> [!TIP]
> Tips highlight mate patterns and traps, to help spotting them in real games.

<a name="_mate_or_trap_"></a>

### `<Mate Pattern or Trap Pattern worth a tip>`

*`<Add here notes when a mate pattern appears with this move or can be created from this move. This also applies to specific traps. The tip helps detecting patterns in real games, in order to either avoid a trap or use it against the opponent>`*

Example:

* **1. g4?** the [Grob's Attack](https://github.com/onclemarcel/chess_flashcards/blob/main/g4_opening/Grob.md) is generally considered one of the worst starting moves.
* A typical mate pattern is reached through this sequence: **1. g4? e5 2. f3??**

[![1. g4 e5 2. f3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pppp1ppp/8/4p3/6P1/5P2/PPPPP2P/RNBQKBNR&lastMove=f2f3&arrows=Rd8h4&coordinates=true&size=280)](https://lichess.org/analysis/standard/rnbqkbnr/pppp1ppp/8/4p3/6P1/5P2/PPPPP2P/RNBQKBNR_b_KQkq_-_0_2)

*... Shortest game — **Mate in 1** with 2... Qh4#*

```
rnbqkbnr/pppp1ppp/8/4p3/6P1/5P2/PPPPP2P/RNBQKBNR b KQkq - 0 2
```

| ![Lichess](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_lichess.png) | Very Rare | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | #-1 |
| --- | --- | --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/pppp1ppp/8/4p3/6P1/5P2/PPPPP2P/RNBQKBNR b KQkq - 0 2" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="5" -->

| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| — | — | — | — | — | |

*Not generated yet — run `python tools/update_stats.py start.md`*
<!-- lichess-stats:end -->

[*Back to previous move*](#_initial_move_)

---

<a name="_move_"></a>

### 1. `<move>`

*`<Present subsequent moves with the same structure as the initial move>`*
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

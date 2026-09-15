<a name="_TOP_"></a>

# D06 Queen's Gambit <br> 1. d4 d5 2. c4 #

**2. c4** is by far White's most tested try after 1... d5 (76.9% of masters games — see [A40 Queen's Pawn Game](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A40_QPG.md)). It is not a "true" gambit: if Black simply takes the pawn (2... dxc4), White regains it with an extra tempo in almost every practical line, since ... b5 to hold onto c4 permanently weakens Black's queenside too much to be sound.

### Overview

*Quick map of every move covered on this card — text and evals match the candidate-move lists below exactly. Node shape is a data-driven category (master-safe / blitz trap / understudied / blunder); see the [shape key](https://github.com/onclemarcel/chess_flashcards/blob/main/start.md#content-diagram-optional) in start.md. Hover a node for its ECO code and variation name; click to jump to its section.*

<!-- content-diagram:start -->
```mermaid
flowchart LR
    classDef main stroke-width:3px;

    c4["1. d4 d5 2. c4"]
    click c4 "#_c4_" "D06 · Queen's Gambit"

    c4 --> dxc4a["2... dxc4<br/>+0.3"]
    click dxc4a "https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D20_Queens_Gambit_Accepted.md" "D20 · Queen's Gambit Accepted"
    c4 --> e6a[["2... e6<br/>+0.2"]]
    click e6a "https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D30_Queens_Gambit_Declined.md" "D30 · Queen's Gambit Declined"
    c4 --> c6a[["2... c6 !<br/>+0.2"]]:::main
    click c6a "https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D10_Slav_Defense.md" "D10 · Slav Defense"
    c4 --> Bf5d["2... Bf5<br/>+0.84"]
    click Bf5d "#_Bf5_" "D06 · Queen's Gambit Declined: Baltic Defense"
    c4 --> Nf6d["2... Nf6<br/>+0.52"]
    click Nf6d "#_Nf6d_" "D06 · Queen's Gambit Declined: Marshall Defense"
    c4 --> c5d["2... c5<br/>+0.51"]
    click c5d "#_c5d_" "D06 · Queen's Gambit Declined: Austrian Defense"
```
<!-- content-diagram:end -->

<a name="_c4_"></a>

[![1. d4 d5 2. c4](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR&lastMove=c2c4&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR_b_KQkq_c3_0_2)

*... 1. d4 d5 2. c4 — Queen's Gambit*

```
rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR b KQkq c3 0 2
```

<!-- lichess-stats:start fen="rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR b KQkq c3 0 2" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="8" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| e6 | 29.1 M (31.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 72 k (35.3%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 33/47/19 |  |
| c6 | 25.3 M (27.0%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 101 k (49.5%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 30/52/17 |  |
| Nf6 | 14.0 M (15.0%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/4/42 | 195 (0.1%) | ⬜⬜⬜⬜⬜🟫🟫🟫🟫⬛ 49/42/9 |  |
| dxc4 | 11.8 M (12.6%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/5/43 | 24 k (11.8%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 33/48/20 |  |
| e5 | 4.5 M (4.8%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/47 | 1.5 k (0.7%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 43/32/24 |  |
| Nc6 | 3.1 M (3.3%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/4/43 | 3.8 k (1.8%) | ⬜⬜⬜⬜⬜🟫🟫🟫⬛⬛ 44/34/22 |  |
| Bf5 | 2.7 M (2.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/4/43 | 1.1 k (0.5%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 44/37/19 |  |
| c5 | 2.0 M (2.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 50/5/45 | 385 (0.2%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 38/45/17 |  |

*Online: bullet/blitz, 1800+ — 93.6 M games. Masters: 204 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR_b_KQkq_c3_0_2#explorer) — updated 2026-09-15*
<!-- lichess-stats:end -->

> [!NOTE]
> Masters and online players disagree sharply here: at master level **2... c6** (the Slav, 49.5%) edges out **2... e6** (the Queen's Gambit Declined, 35.3%) — but online, **2... e6** actually leads (31.1% vs 27.0%). The Slav's reputation as a rock-solid, slightly technical defense fits a pattern seen throughout this repository: sound-but-quiet structures do better the stronger the players get.

### Candidate moves

* **2... dxc4** (+0.3): the *Queen's Gambit Accepted* — Black grabs the pawn and lets White regain it with a tempo — its own code, [D20](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D20_Queens_Gambit_Accepted.md)
* **2... e6** (+0.2): the *Queen's Gambit Declined* — solid, at the cost of temporarily boxing in the light-squared bishop — its own code, [D30](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D30_Queens_Gambit_Declined.md)
* **2... c6** (+0.2): the *Slav Defense* — masters' actual top choice (49.5%), keeping the light-squared bishop free — its own code, [D10](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D10_Slav_Defense.md)
* [**2... Bf5**](#_Bf5_) (+0.84, 0.5% masters): the *Grau Defence* — covered below
* [**2... Nf6**](#_Nf6d_) (+0.52, 0.1% masters): the *Marshall Defence* — covered below
* [**2... c5**](#_c5d_) (+0.51, 0.2% masters): the *Symmetrical Defence* — covered below

[*Back to TOP*](#_TOP_)

---

<a name="_Bf5_"></a>

## 2... Bf5 — Grau Defence

[![2... Bf5](https://backscattering.de/web-boardimage/board.svg?fen=rn1qkbnr/ppp1pppp/8/3p1b2/2PP4/8/PP2PPPP/RNBQKBNR&lastMove=c8f5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rn1qkbnr/ppp1pppp/8/3p1b2/2PP4/8/PP2PPPP/RNBQKBNR_w_KQkq_-_1_3)

*... 2... Bf5 — live-tagged the Baltic Defense*

```
rn1qkbnr/ppp1pppp/8/3p1b2/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 1 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.84 |
| --- | --- |

`eco.md` calls this the *Grau Defence*; the live explorer tags it the ***Baltic Defense*** instead — a real, substantial name divergence. Develops the bishop outside the pawn chain before it can be shut in, the Slav's own idea a tempo early and without first supporting d5 with the c-pawn. Masters split between **3. cxd5** (48.3%) and **3. Nc3** (38.2%). Not built out further here (backlog).

[*Back to 1. d4 d5 2. c4*](#_c4_)
[*Back to TOP*](#_TOP_)

---

<a name="_Nf6d_"></a>

## 2... Nf6 — Marshall Defence

[![2... Nf6](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/ppp1pppp/5n2/3p4/2PP4/8/PP2PPPP/RNBQKBNR&lastMove=g8f6&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/ppp1pppp/5n2/3p4/2PP4/8/PP2PPPP/RNBQKBNR_w_KQkq_-_1_3)

*... 2... Nf6 — Marshall Defence*

```
rnbqkb1r/ppp1pppp/5n2/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 1 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.52 |
| --- | --- |

Develops the king's knight immediately rather than deciding on a pawn structure first — a genuine database rarity (0.1% masters), and the engine already prefers White somewhat more than after the main tries. Masters' clear main try is **3. cxd5** (62.2%), simply grabbing the pawn since ...Nxd5 just re-routes the knight without solving Black's structural questions. Not built out further here (backlog).

[*Back to 1. d4 d5 2. c4*](#_c4_)
[*Back to TOP*](#_TOP_)

---

<a name="_c5d_"></a>

## 2... c5 — Symmetrical Defence

[![2... c5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp2pppp/8/2pp4/2PP4/8/PP2PPPP/RNBQKBNR&lastMove=c7c5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp2pppp/8/2pp4/2PP4/8/PP2PPPP/RNBQKBNR_w_KQkq_c6_0_3)

*... 2... c5 — live-tagged the Austrian Defense*

```
rnbqkbnr/pp2pppp/8/2pp4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq c6 0 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.51 |
| --- | --- |

`eco.md` calls this the *Symmetrical Defence*; the live explorer tags it the ***Austrian Defense*** instead — another real, substantial name divergence. Strikes back at the centre immediately rather than defending d5 — a genuine database rarity (0.2% masters). Masters' clear main try is **3. cxd5** (73.0%), resolving the tension at once. Not built out further here (backlog).

[*Back to 1. d4 d5 2. c4*](#_c4_)
[*Back to TOP*](#_TOP_)


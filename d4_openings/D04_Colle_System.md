<a name="_TOP_"></a>

# D04 Queen's Pawn Game: Colle System <br> 1. d4 d5 2. Nf3 Nf6 3. e3 #

Spun off from [D02's 2... Nf6](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D02_QPG_Nf3.md#_Nf6_): named after Belgian master Edgar Colle. Rather than fight for a specific structure, White commits to a fixed plan — e3, Bd3, Nbd2, O-O, and eventually the thematic e3-e4 break — that plays almost the same way regardless of what Black does. That's the defining trait of a "system" opening: Black's 3rd-move reply here is unusually scattered (no single try clears even 33% of masters games) precisely because it doesn't change White's plan very much.

### Overview

*Quick map of every move covered on this card — see the [shape key](https://github.com/onclemarcel/chess_flashcards/blob/main/start.md#content-diagram-optional) in start.md. 3... c5 and the other minor 3rd-move tries are discussed below but have no anchor of their own, so they're left off this map rather than pointing nowhere.*

<!-- content-diagram:start -->
```mermaid
flowchart LR
    classDef main stroke-width:3px;

    e3["1. d4 d5 2. Nf3 Nf6 3. e3"]
    click e3 "#_initial_move_" "D04 · Queen's Pawn Game: Colle System"

    e3 --> e6[["3... e6 !<br/>0.0"]]:::main
    click e6 "#_e6_" "D05 · Queen's Pawn Game: Colle System"

    e6 --> Bd3[["4. Bd3 !<br/>0.0"]]:::main
    click Bd3 "#_Bd3_" "D05 · Queen's Pawn Game: Colle System"
    Bd3 --> c5b[["4... c5 !<br/>+0.1"]]:::main
    click c5b "#_c5_" "D05 · Queen's Pawn Game: Colle System"
```
<!-- content-diagram:end -->

<a name="_initial_move_"></a>

[![3. e3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/ppp1pppp/5n2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R&lastMove=e2e3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/ppp1pppp/5n2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R_b_KQkq_-_0_3)

*... 3. e3 — Colle System*

```
rnbqkb1r/ppp1pppp/5n2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R b KQkq - 0 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkb1r/ppp1pppp/5n2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R b KQkq - 0 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="6" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| e6 | 2.2 M (26.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/5/43 | 1.8 k (32.6%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 29/50/21 |  |
| Bg4 | 1.3 M (15.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/5/45 | 290 (5.2%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 31/41/28 |  |
| Bf5 | 1.3 M (15.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/6/46 | 608 (10.9%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 28/40/32 |  |
| c5 | 1.2 M (14.7%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/5/47 | 1.5 k (27.4%) | ⬜⬜🟫🟫🟫🟫🟫⬛⬛⬛ 21/49/30 |  |
| c6 | 740 k (8.9%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/6/46 | 732 (13.1%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 25/44/31 |  |
| Nc6 | 680 k (8.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/4/44 | 0 | — | ⚠ |
| g6 | 0 | — | 518 (9.3%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 24/44/32 |  |

*Online: bullet/blitz, 1800+ — 8.3 M games. Masters: 5.6 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/ppp1pppp/5n2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R_b_KQkq_-_0_3#explorer) — updated 2026-08-24*
<!-- lichess-stats:end -->

### Candidate moves

* [**3... e6**](#_e6_) (0.0): the most common single try, but only just — masters' top pick at 32.6%, the line this card follows.
* **3... c5** (0.0): a close second (27.4% masters), transposing into a very similar structure a move or two later.
* **3... c6 / 3... Bf5 / 3... g6 / 3... Bg4**: all real, all played (13.1%, 10.9%, 9.3%, 5.2% masters respectively) — none covered further here, since White's own plan barely changes against any of them.

[*Back to TOP*](#_TOP_)

---

<a name="_e6_"></a>

## 3... e6

[![3... e6](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R&lastMove=e7e6&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R_w_KQkq_-_0_4)

*... 3... e6*

```
rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R w KQkq - 0 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Bd3 | 3.2 M (43.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/5/43 | 2.2 k (73.3%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 31/47/21 |  |
| c4 | 1.5 M (20.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/5/45 | 440 (14.4%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 29/47/25 |  |
| Be2 | 1.3 M (17.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 0 | — | ⚠ |
| Nbd2 | 275 k (3.7%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/5/42 | 194 (6.4%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 26/55/19 |  |
| b3 | 0 | — | 128 (4.2%) | ⬜⬜⬜⬜🟫🟫🟫🟫🟫⬛ 40/46/14 |  |

*Online: bullet/blitz, 1800+ — 7.4 M games. Masters: 3.1 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/4PN2/PPP2PPP/RNBQKB1R_w_KQkq_-_0_4#explorer) — updated 2026-08-24*
<!-- lichess-stats:end -->

**4. Bd3** is masters' clear main try (73.3%) — the bishop aims straight down the b1-h7 diagonal at the kingside, the whole point of playing e3 before developing it.

[*Back to 3. e3*](#_initial_move_)
[*Back to TOP*](#_TOP_)

---

<a name="_Bd3_"></a>

## 4. Bd3

[![4. Bd3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/3BPN2/PPP2PPP/RNBQK2R&lastMove=f1d3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/3BPN2/PPP2PPP/RNBQK2R_b_KQkq_-_1_4)

*... 4. Bd3*

```
rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/3BPN2/PPP2PPP/RNBQK2R b KQkq - 1 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/3BPN2/PPP2PPP/RNBQK2R b KQkq - 1 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="6" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| c5 | 1.3 M (37.5%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/5/43 | 1.4 k (61.3%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 29/49/22 |  |
| Be7 | 889 k (25.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 231 (10.3%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 38/43/19 |  |
| Bd6 | 682 k (19.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/5/42 | 216 (9.6%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 43/42/15 |  |
| Nbd7 | 97 k (2.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 120 (5.3%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 42/36/22 |  |
| c6 | 95 k (2.8%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 55/5/40 | 4 (0.2%) | — | ⚠ |
| b6 | 92 k (2.7%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 49/6/45 | 289 (12.9%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 24/53/24 |  |

*Online: bullet/blitz, 1800+ — 3.4 M games. Masters: 2.2 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/ppp2ppp/4pn2/3p4/3P4/3BPN2/PPP2PPP/RNBQK2R_b_KQkq_-_1_4#explorer) — updated 2026-08-24*
<!-- lichess-stats:end -->

**4... c5** is masters' clear main try (61.3%) — striking back at White's centre before it's too late.

[*Back to 3... e6*](#_e6_)
[*Back to TOP*](#_TOP_)

---

<a name="_c5_"></a>

## 4... c5 — the Colle tabiya

[![4... c5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/pp3ppp/4pn2/2pp4/3P4/3BPN2/PPP2PPP/RNBQK2R&lastMove=c7c5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/pp3ppp/4pn2/2pp4/3P4/3BPN2/PPP2PPP/RNBQK2R_w_KQkq_c6_0_5)

*... 4... c5 — reaching the main Colle tabiya*

```
rnbqkb1r/pp3ppp/4pn2/2pp4/3P4/3BPN2/PPP2PPP/RNBQK2R w KQkq c6 0 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.1 |
| --- | --- |

Here masters actually prefer **5. b3** (63.6%) — heading for the *Colle-Zukertort* hybrid setup with Bb2 aiming at the long diagonal — over the traditional **5. c3** (23.4%), the "pure" Colle-Koltanowski structure. Either way White simply continues Nbd2, O-O and the thematic e3-e4 break in more or less any order, since the whole appeal of a system opening is not depending too heavily on move order or Black's exact setup. Not built out further here (backlog).

[*Back to 4. Bd3*](#_Bd3_)
[*Back to TOP*](#_TOP_)

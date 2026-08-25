<a name="_TOP_"></a>

# C80 Ruy Lopez: Open Variation <br> 1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Nxe4 6. d4 #

Spun off from [C84's 5... Nxe4](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C84_Ruy_Lopez_Morphy_Closed.md#_Nxe4_): rather than meet the pin with ... Be7 or ... b5, Black grabs the e4 pawn while it's briefly loose. White doesn't try to win the knight back on the spot — **6. d4!** strikes the centre and the e5 pawn at once, and Black has to give ground there before the extra tempo starts to matter. The resulting positions are sharper and far more concrete than the Closed main line: a real, independent system (9.4% of masters games at move 5, see C84), not a sideline to be refuted.

### Overview

*Quick map of every move covered on this card — see the [shape key](https://github.com/onclemarcel/chess_flashcards/blob/main/start.md#content-diagram-optional) in start.md.*

<!-- content-diagram:start -->
```mermaid
flowchart LR
    classDef main stroke-width:3px;

    d4["6. d4"]
    click d4 "#_initial_move_" "C80 · Ruy Lopez: Open"

    d4 --> b5[["6... b5 !<br/>+0.2"]]:::main
    click b5 "#_b5_" "C80 · Ruy Lopez: Open"
    d4 --> exd4{"6... exd4 ⚠<br/>+1.2"}
    click exd4 "#_exd4_" "C80 · Ruy Lopez: Open"

    b5 --> Bb3["7. Bb3 !<br/>+0.2"]:::main
    click Bb3 "#_Bb3_" "C80 · Ruy Lopez: Open"

    Bb3 --> d5["7... d5 !<br/>+0.2"]:::main
    click d5 "#_d5_" "C80 · Ruy Lopez: Open"
```
<!-- content-diagram:end -->

<a name="_initial_move_"></a>

[![6. d4](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/1ppp1ppp/p1n5/4p3/B2Pn3/5N2/PPP2PPP/RNBQ1RK1&lastMove=d2d4&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/1ppp1ppp/p1n5/4p3/B2Pn3/5N2/PPP2PPP/RNBQ1RK1_b_kq_d3_0_6)

*... 6. d4 — Open Variation*

```
r1bqkb1r/1ppp1ppp/p1n5/4p3/B2Pn3/5N2/PPP2PPP/RNBQ1RK1 b kq d3 0 6
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkb1r/1ppp1ppp/p1n5/4p3/B2Pn3/5N2/PPP2PPP/RNBQ1RK1 b kq d3 0 6" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="5" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| b5 | 162 k (75.3%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 47/7/46 | 7.1 k (93.4%) | ⬜⬜⬜🟫🟫🟫🟫🟫🟫⬛ 28/56/15 |  |
| exd4 | 26 k (12.1%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 38/12/50 | 106 (1.4%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 40/39/22 |  |
| Be7 | 15 k (7.1%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 45/9/47 | 392 (5.2%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 36/44/20 |  |
| d5 | 8.7 k (4.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/6/41 | 3 (0.0%) | — | ⚠ |
| Nxd4 | 805 (0.4%) | ⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛ 65/3/32 | 0 | — | ⚠ |
| Nd6 | 0 | — | 1 (0.0%) | — |  |

*Online: bullet/blitz, 1800+ — 214 k games. Masters: 7.6 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkb1r/1ppp1ppp/p1n5/4p3/B2Pn3/5N2/PPP2PPP/RNBQ1RK1_b_kq_d3_0_6#explorer) — updated 2026-08-25*
<!-- lichess-stats:end -->

### Candidate moves

* [**6... b5**](#_b5_) (+0.2): defends the knight and gains a tempo on the bishop before it does anything else — masters' near-automatic choice (93.4%).
* **6... Be7**: solid, gives back none of the tempo White is owed for the pawn — a real but rare try (5.2% masters).
* [**6... exd4**](#_exd4_) (+1.2 ⚠): grabs a second pawn, but drops the e4 knight's cover and walks into a tactical shot — see the TIP below.

[*Back to TOP*](#_TOP_)

---

> [!TIP]
> **6... exd4?!** looks natural — Black already has one extra pawn on e4, why not take a second? — but it removes the e5 pawn that used to block the e-file, and the e4 knight has nothing else defending it.
>
> <a name="_exd4_"></a>
>
> ### 6... exd4 — the knight has no real shelter
>
> **7. Re1!** pins the idea together: the rook lands on the newly-open e-file and the knight has no good square. Best play still loses the pawn back with interest — Stockfish's own top line runs **7... f5 8. Nxd4 Qh4 9. g3 Qf6 10. Nxc6 bxc6**, and White keeps the bishop pair and a much better structure. This is a genuinely punishable mistake, not just a slightly worse version of 6... b5 (+1.2 vs +0.2 — a full pawn swing).
>
> [![6. d4 exd4 7. Re1](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/1ppp1ppp/p1n5/8/B2pn3/5N2/PPP2PPP/RNBQ1RK1&lastMove=e5d4&arrows=Rf1e1&coordinates=true&size=280)](https://lichess.org/analysis/standard/r1bqkb1r/1ppp1ppp/p1n5/8/B2pn3/5N2/PPP2PPP/RNBQ1RK1_w_kq_-_0_7)
>
> *... 6... exd4 — red: 7. Re1 is coming for the undefended e4 knight*
>
> ```
> r1bqkb1r/1ppp1ppp/p1n5/8/B2pn3/5N2/PPP2PPP/RNBQ1RK1 w kq - 0 7
> ```
>
> | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +1.2 |
> | --- | --- |
>
> [*Back to 6. d4*](#_initial_move_)
> [*Back to TOP*](#_TOP_)

---

<a name="_b5_"></a>

## 6... b5

[![6... b5](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/2pp1ppp/p1n5/1p2p3/B2Pn3/5N2/PPP2PPP/RNBQ1RK1&lastMove=b7b5&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/2pp1ppp/p1n5/1p2p3/B2Pn3/5N2/PPP2PPP/RNBQ1RK1_w_kq_b6_0_7)

*... 6... b5 — defending the knight with tempo*

```
r1bqkb1r/2pp1ppp/p1n5/1p2p3/B2Pn3/5N2/PPP2PPP/RNBQ1RK1 w kq b6 0 7
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkb1r/2pp1ppp/p1n5/1p2p3/B2Pn3/5N2/PPP2PPP/RNBQ1RK1 w kq b6 0 7" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="5" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Bb3 | 159 k (98.3%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 47/7/46 | 7.1 k (99.8%) | ⬜⬜⬜🟫🟫🟫🟫🟫🟫⬛ 28/56/15 |  |
| d5 | 1.5 k (0.9%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 46/4/49 | 7 (0.1%) | — |  |
| Re1 | 854 (0.5%) | ⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛ 38/4/58 | 1 (0.0%) | — | ⚠ |
| Nxe5 | 278 (0.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/5/42 | 5 (0.1%) | — |  |
| dxe5 | 101 (0.1%) | ⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛ 36/2/62 | 0 | — | ⚠ |

*Online: bullet/blitz, 1800+ — 162 k games. Masters: 7.1 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkb1r/2pp1ppp/p1n5/1p2p3/B2Pn3/5N2/PPP2PPP/RNBQ1RK1_w_kq_b6_0_7#explorer) — updated 2026-08-25*
<!-- lichess-stats:end -->

**7. Bb3** is essentially forced (99.8% of masters games) — the bishop has to move off the a4-e8 diagonal before ... b4 could hit it again, and b3 keeps the long-term aim at f7 alive.

[*Back to 6. d4*](#_initial_move_)
[*Back to TOP*](#_TOP_)

---

<a name="_Bb3_"></a>

## 7. Bb3

[![7. Bb3](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/2pp1ppp/p1n5/1p2p3/3Pn3/1B3N2/PPP2PPP/RNBQ1RK1&lastMove=a4b3&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/2pp1ppp/p1n5/1p2p3/3Pn3/1B3N2/PPP2PPP/RNBQ1RK1_b_kq_-_1_7)

*... 7. Bb3*

```
r1bqkb1r/2pp1ppp/p1n5/1p2p3/3Pn3/1B3N2/PPP2PPP/RNBQ1RK1 b kq - 1 7
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkb1r/2pp1ppp/p1n5/1p2p3/3Pn3/1B3N2/PPP2PPP/RNBQ1RK1 b kq - 1 7" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="5" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| d5 | 178 k (93.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 47/7/46 | 7.1 k (99.4%) | ⬜⬜⬜🟫🟫🟫🟫🟫🟫⬛ 28/56/15 |  |
| exd4 | 5.6 k (2.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/4/43 | 5 (0.1%) | — |  |
| Be7 | 3.7 k (1.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 54/5/41 | 38 (0.5%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 42/39/18 |  |
| d6 | 1.1 k (0.6%) | ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛ 78/3/19 | 0 | — | ⚠ |
| Nxd4 | 871 (0.5%) | ⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛ 71/2/27 | 0 | — | ⚠ |

*Online: bullet/blitz, 1800+ — 190 k games. Masters: 7.2 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkb1r/2pp1ppp/p1n5/1p2p3/3Pn3/1B3N2/PPP2PPP/RNBQ1RK1_b_kq_-_1_7#explorer) — updated 2026-08-25*
<!-- lichess-stats:end -->

**7... d5** stakes out the centre while the knight is still solidly placed on e4 — the near-unanimous choice in masters play (99.4%).

[*Back to 6... b5*](#_b5_)
[*Back to TOP*](#_TOP_)

---

<a name="_d5_"></a>

## 7... d5 — the Open Variation tabiya

[![7... d5](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/2p2ppp/p1n5/1p1pp3/3Pn3/1B3N2/PPP2PPP/RNBQ1RK1&lastMove=d7d5&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/2p2ppp/p1n5/1p1pp3/3Pn3/1B3N2/PPP2PPP/RNBQ1RK1_w_kq_d6_0_8)

*... 7... d5 — Black's centre and extra activity balance White's bishop pair and lead*

```
r1bqkb1r/2p2ppp/p1n5/1p1pp3/3Pn3/1B3N2/PPP2PPP/RNBQ1RK1 w kq d6 0 8
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkb1r/2p2ppp/p1n5/1p1pp3/3Pn3/1B3N2/PPP2PPP/RNBQ1RK1 w kq d6 0 8" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="5" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| dxe5 | 150 k (84.3%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 47/7/46 | 7.0 k (98.2%) | ⬜⬜⬜🟫🟫🟫🟫🟫🟫⬛ 28/56/15 |  |
| Nxe5 | 16 k (8.9%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/6/46 | 85 (1.2%) | ⬜⬜🟫🟫🟫🟫🟫🟫⬛⬛ 24/54/22 |  |
| Re1 | 9.4 k (5.3%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 44/5/51 | 4 (0.1%) | — | ⚠ |
| a4 | 1.0 k (0.6%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/43 | 19 (0.3%) | — |  |
| Nc3 | 787 (0.4%) | ⬜⬜⬜⬜⬜⬜🟫⬛⬛⬛ 61/5/34 | 18 (0.3%) | — |  |

*Online: bullet/blitz, 1800+ — 178 k games. Masters: 7.1 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkb1r/2p2ppp/p1n5/1p1pp3/3Pn3/1B3N2/PPP2PPP/RNBQ1RK1_w_kq_d6_0_8#explorer) — updated 2026-08-25*
<!-- lichess-stats:end -->

From here the game is essentially forced for several more moves: **8. dxe5** (98.2% masters) **Be6** (99.9%) reaches a real tabiya, and White's 9th move is a genuine four-way choice — **9. Nbd2** (46.7% masters, the top try — the knight heads for e4/c4 next), **9. c3** (27.7%, supporting a later d4 or Bc2-Nbd2 regrouping), **9. Be3** (14.9%) and **9. Qe2** (9.6%) are all played. After **9. Nbd2 Nc5** (75.0% masters), the position is named the ***Bernstein Variation*** (verified live via the explorer's own `opening` field) — Stockfish still calls it dead level (+0.1), a good summary of the whole Open Variation: Black's activity and structure genuinely compensate for White's extra central space and bishop pair, all the way through forced-looking main theory. Deeper Bernstein/9. c3 theory is its own body of work, not covered further here.

[*Back to 7. Bb3*](#_Bb3_)
[*Back to TOP*](#_TOP_)

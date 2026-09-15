<a name="_TOP_"></a>

# D58 Queen's Gambit Declined: Tartakower (Makagonov-Bondarevsky) System <br> 1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Nf3 h6 7. Bh4 b6 #

Spun off from [D55's own "7. Bh4" card](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D55_Queens_Gambit_Declined_Neo_Orthodox.md#_Bh4_) — **masters' actual overwhelming main try there (72.6%)**, well ahead of the historically better-known Lasker Defence (21.2%, D56) — already live-tagged its own code. `eco.md`'s full name is "Tartakower (Makagonov-Bondarevsky) System"; the live explorer drops the parenthetical entirely and calls it plain ***Tartakower Defense*** — a real, clean divergence, matching the pattern of this whole batch: `eco.md`'s fuller historical names against the live database's shorter modern labels.

<a name="_initial_move_"></a>

[![7... b6](https://backscattering.de/web-boardimage/board.svg?fen=rnbq1rk1/p1p1bpp1/1p2pn1p/3p4/2PP3B/2N1PN2/PP3PPP/R2QKB1R&lastMove=b7b6&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbq1rk1/p1p1bpp1/1p2pn1p/3p4/2PP3B/2N1PN2/PP3PPP/R2QKB1R_w_KQ_-_0_8)

*... 7... b6 — Tartakower Defense*

```
rnbq1rk1/p1p1bpp1/1p2pn1p/3p4/2PP3B/2N1PN2/PP3PPP/R2QKB1R w KQ - 0 8
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.05 |
| --- | --- |

<!-- lichess-stats:start fen="rnbq1rk1/p1p1bpp1/1p2pn1p/3p4/2PP3B/2N1PN2/PP3PPP/R2QKB1R w KQ - 0 8" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="8" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| cxd5 | 136 k (38.8%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 46/8/47 | 951 (15.4%) | ⬜⬜🟫🟫🟫🟫🟫🟫⬛⬛ 21/60/20 |  |
| Bd3 | 79 k (22.6%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 45/7/49 | 1.5 k (25.1%) | ⬜⬜⬜🟫🟫🟫🟫🟫🟫⬛ 25/60/15 |  |
| Rc1 | 44 k (12.6%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 47/8/45 | 1.0 k (16.9%) | ⬜⬜🟫🟫🟫🟫🟫🟫⬛⬛ 26/57/17 |  |
| Be2 | 33 k (9.4%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 45/8/47 | 1.6 k (26.8%) | ⬜⬜🟫🟫🟫🟫🟫🟫🟫⬛ 23/65/12 |  |
| Bxf6 | 15 k (4.3%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 48/7/44 | 226 (3.7%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 30/52/18 |  |
| Qc2 | 15 k (4.2%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 46/7/47 | 273 (4.4%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 28/48/24 |  |
| a3 | 8.6 k (2.5%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 44/6/50 | 0 | — | ⚠ |
| Qb3 | 5.5 k (1.6%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/9/38 | 354 (5.7%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 33/50/16 |  |
| Rb1 | 0 | — | 70 (1.1%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 34/50/16 |  |

*Online: bullet/blitz, 1800+ — 350 k games. Masters: 6.2 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbq1rk1/p1p1bpp1/1p2pn1p/3p4/2PP3B/2N1PN2/PP3PPP/R2QKB1R_w_KQ_-_0_8#explorer) — updated 2026-09-14*
<!-- lichess-stats:end -->

Prepares to fianchetto the light-squared bishop before resolving the central tension, one of the most enduring and flexible treatments of the whole Queen's Gambit Declined. **A real, interesting finding, worth stating plainly rather than glossing over**: White's 8th move is a genuine multi-way spread, and `eco.md`'s own single D59 entry from here (8. cxd5) is *not* masters' most popular choice — it trails **Be2** (26.8%), **Bd3** (25.1%), and **Rc1** (16.9%) at just 15.4%. This mirrors the exact opposite pattern already seen at D50's own Been-Koomen Variation (a rare line given its own code): here `eco.md` codes the *fourth*-most-common try rather than the first three. **8. cxd5** heads for D59, its own code, covered there. **8. Be2**, **8. Bd3**, **8. Rc1**, **8. Qb3**, **8. Qc2**, **8. Bxf6**, and **8. Rb1** are all real, secondary tries with no code of their own in this range.

* [**8. cxd5**](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D59_Queens_Gambit_Declined_Tartakower_Variation.md) (15.4% masters): its own code, D59.
* **8. Be2** (26.8% masters): a real, secondary try with no code of its own in this range — masters' actual most popular choice.
* **8. Bd3** (25.1% masters): a real, secondary try with no code of its own in this range.
* **8. Rc1** (16.9% masters): a real, secondary try with no code of its own in this range.
* **8. Qb3** (5.7%), **8. Qc2** (4.4%), **8. Bxf6** (3.7%), **8. Rb1** (1.1%): all real, secondary tries with no code of their own in this range.

Not built out further here beyond the D59 link — `eco.md` gives this whole entry just this one node.

[*Back to TOP*](#_TOP_)

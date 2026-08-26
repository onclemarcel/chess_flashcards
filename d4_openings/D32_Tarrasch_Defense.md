<a name="_TOP_"></a>

# D32 Tarrasch Defense <br> 1. d4 d5 2. c4 e6 3. Nc3 c5 #

Spun off from [D06's Queen's Gambit Declined section](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D06_Queens_Gambit.md#_e6_), which showed White's 3rd-move split but had no candidate bullets pointing anywhere past it — a genuine zero-coverage gap surfaced by a full A00-E99 ECO-code audit. **Almost missed by a naive text search**: this repo already covers an *unrelated* "Tarrasch Variation" on the French (3. Nd2) and Caro-Kann (3. Nd2) cards, sharing the same 19th-century namesake (Siegbert Tarrasch) but nothing else — this is the actual Tarrasch **Defense**, a QGD system where Black strikes back at the centre with ... c5 immediately rather than developing quietly. It accepts an isolated queen's pawn after the near-inevitable cxd5/exd5 trade in exchange for active piece play — one of the most heavily analysed structures in chess, championed by Tarrasch himself against the "always keep pawns healthy" dogma of his era.

<a name="_initial_move_"></a>

[![3... c5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp3ppp/4p3/2pp4/2PP4/2N5/PP2PPPP/R1BQKBNR&lastMove=c7c5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp3ppp/4p3/2pp4/2PP4/2N5/PP2PPPP/R1BQKBNR_w_KQkq_c6_0_4)

*... 1. d4 d5 2. c4 e6 3. Nc3 c5 — Tarrasch Defense*

```
rnbqkbnr/pp3ppp/4p3/2pp4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq c6 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.3 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/pp3ppp/4p3/2pp4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq c6 0 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| cxd5 | 800 k (42.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/6/47 | 4.4 k (84.1%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 37/44/18 |  |
| Nf3 | 493 k (25.9%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/5/48 | 136 (2.6%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 35/36/29 |  |
| e3 | 354 k (18.6%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/5/47 | 674 (13.0%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 37/42/21 |  |
| dxc5 | 134 k (7.0%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/5/47 | 14 (0.3%) | — |  |

*Online: bullet/blitz, 1800+ — 1.9 M games. Masters: 5.2 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pp3ppp/4p3/2pp4/2PP4/2N5/PP2PPPP/R1BQKBNR_w_KQkq_c6_0_4#explorer) — updated 2026-08-26*
<!-- lichess-stats:end -->

**4. cxd5** is masters' clear main try (84.1%) — trading immediately before Black can support the centre further. **4. e3** (13.0%) declines the trade for now, keeping options flexible a move longer. Not built out further here.

### Candidate moves

* [**4. cxd5**](#_cxd5_) (+0.3, 84.1% masters): the line this card follows.
* **4. e3** (+0.2, 13.0% masters): a real, solid alternative — declines the trade a move longer.

[*Back to TOP*](#_TOP_)

---

<a name="_cxd5_"></a>

## 4. cxd5 exd5 5. Nf3

Masters recapture with the pawn (**4... exd5**, essentially automatic) to keep the isolated d-pawn mobile and central rather than doubled; **5. Nf3** develops naturally before deciding how to meet Black's own development.

[![5. Nf3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp3ppp/8/2pp4/3P4/2N2N2/PP2PPPP/R1BQKB1R&lastMove=g1f3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp3ppp/8/2pp4/3P4/2N2N2/PP2PPPP/R1BQKB1R_b_KQkq_-_1_5)

*... 4. cxd5 exd5 5. Nf3 — Tarrasch Defense: Two Knights Variation*

```
rnbqkbnr/pp3ppp/8/2pp4/3P4/2N2N2/PP2PPPP/R1BQKB1R b KQkq - 1 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.3 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/pp3ppp/8/2pp4/3P4/2N2N2/PP2PPPP/R1BQKB1R b KQkq - 1 5" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="3" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Nc6 | 348 k (52.5%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 47/7/46 | 4.4 k (92.8%) | ⬜⬜⬜⬜🟫🟫🟫🟫🟫⬛ 37/47/16 |  |
| Nf6 | 183 k (27.7%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/6/42 | 326 (6.8%) | ⬜⬜⬜⬜🟫🟫🟫🟫🟫⬛ 38/47/15 |  |
| cxd4 | 72 k (10.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 54/5/41 | 15 (0.3%) | — |  |

*Online: bullet/blitz, 1800+ — 663 k games. Masters: 4.8 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pp3ppp/8/2pp4/3P4/2N2N2/PP2PPPP/R1BQKB1R_b_KQkq_-_1_5#explorer) — updated 2026-08-26*
<!-- lichess-stats:end -->

**5... Nc6** is masters' overwhelming choice (92.8%) — developing the queenside knight to its most natural square before committing the kingside one, matching the isolated-pawn plan of active piece play over structural purity.

[*Back to 4. cxd5*](#_cxd5_)
[*Back to TOP*](#_TOP_)

---

<a name="_Nc6_"></a>

### 5... Nc6 6. g3 — Tarrasch Defense: Rubinstein System

**6. g3** is masters' clear main try (74.1%) — fianchettoing to pressure d5 from a distance rather than blocking it with a piece, the modern main plan against the Tarrasch's isolated pawn.

[![6. g3](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/pp3ppp/2n5/2pp4/3P4/2N2NP1/PP2PP1P/R1BQKB1R&lastMove=g2g3&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/pp3ppp/2n5/2pp4/3P4/2N2NP1/PP2PP1P/R1BQKB1R_b_KQkq_-_0_6)

*... 5... Nc6 6. g3 — Tarrasch Defense: Rubinstein System*

```
r1bqkbnr/pp3ppp/2n5/2pp4/3P4/2N2NP1/PP2PP1P/R1BQKB1R b KQkq - 0 6
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.3 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkbnr/pp3ppp/2n5/2pp4/3P4/2N2NP1/PP2PP1P/R1BQKB1R b KQkq - 0 6" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="3" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Nf6 | 165 k (81.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 46/9/46 | 3.1 k (90.4%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 37/46/17 |  |
| c4 | 14 k (6.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 49/6/45 | 294 (8.5%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 37/38/25 |  |
| cxd4 | 11 k (5.5%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/6/40 | 17 (0.5%) | — |  |

*Online: bullet/blitz, 1800+ — 203 k games. Masters: 3.5 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkbnr/pp3ppp/2n5/2pp4/3P4/2N2NP1/PP2PP1P/R1BQKB1R_b_KQkq_-_0_6#explorer) — updated 2026-08-26*
<!-- lichess-stats:end -->

**6... Nf6** is masters' overwhelming choice (90.4%) — completing development before deciding on the bishop's diagonal.

[*Back to 4. cxd5*](#_cxd5_)
[*Back to TOP*](#_TOP_)

---

<a name="_Nf6_"></a>

#### 6... Nf6 7. Bg2 Be7 — Tarrasch Defense: Prague Variation, Main Line

**7. Bg2** is automatic, completing the fianchetto; **7... Be7** develops the last minor piece and prepares to castle, reaching the true Tarrasch middlegame tabiya — Black's isolated d-pawn gives active piece play in exchange for a long-term structural weakness that White will try to blockade and trade down toward.

[![7... Be7](https://backscattering.de/web-boardimage/board.svg?fen=r1bqk2r/pp2bppp/2n2n2/2pp4/3P4/2N2NP1/PP2PPBP/R1BQK2R&lastMove=f8e7&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqk2r/pp2bppp/2n2n2/2pp4/3P4/2N2NP1/PP2PPBP/R1BQK2R_w_KQkq_-_3_8)

*... 6... Nf6 7. Bg2 Be7 — Tarrasch Defense: Prague Variation, Main Line*

```
r1bqk2r/pp2bppp/2n2n2/2pp4/3P4/2N2NP1/PP2PPBP/R1BQK2R w KQkq - 3 8
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.3 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqk2r/pp2bppp/2n2n2/2pp4/3P4/2N2NP1/PP2PPBP/R1BQK2R w KQkq - 3 8" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="3" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| O-O | 150 k (89.6%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 48/8/44 | 3.6 k (98.7%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 37/46/17 |  |
| dxc5 | 10 k (6.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 47/7/46 | 28 (0.8%) | ⬜⬜⬜⬜🟫🟫🟫🟫🟫⬛ 39/50/11 |  |
| Bg5 | 4.5 k (2.7%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 45/8/47 | 16 (0.4%) | — |  |

*Online: bullet/blitz, 1800+ — 168 k games. Masters: 3.7 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqk2r/pp2bppp/2n2n2/2pp4/3P4/2N2NP1/PP2PPBP/R1BQK2R_w_KQkq_-_3_8#explorer) — updated 2026-08-26*
<!-- lichess-stats:end -->

**8. O-O** is essentially forced (98.7% masters). Not built out further here (backlog) — the isolated-queen's-pawn middlegame from here is its own vast body of theory.

[*Back to 4. cxd5*](#_cxd5_)
[*Back to TOP*](#_TOP_)

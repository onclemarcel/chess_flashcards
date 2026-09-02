<a name="_TOP_"></a>

# B22 Sicilian Defense: Alapin Variation <br> 1. e4 c5 2. c3 #

Spun off from [B20's own root fork](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B20_Sicilian.md): offers a completely different kind of game from the Open Sicilian — quieter, less forcing, and much less theory-dependent, a popular practical choice against opponents who know their Sicilian theory cold. Live-confirmed its own code via the Lichess explorer's own `opening` field — this card was originally built (and mislabeled) as part of `B20_Sicilian.md`; moved here once the wrong-code bug was caught.

<a name="_initial_move_"></a>

[![2. c3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp1ppppp/8/2p5/4P3/2P5/PP1P1PPP/RNBQKBNR&lastMove=c2c3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp1ppppp/8/2p5/4P3/2P5/PP1P1PPP/RNBQKBNR_b_KQkq_-_0_2)

*... 2. c3 — Alapin Variation*

```
rnbqkbnr/pp1ppppp/8/2p5/4P3/2P5/PP1P1PPP/RNBQKBNR b KQkq - 0 2
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/pp1ppppp/8/2p5/4P3/2P5/PP1P1PPP/RNBQKBNR b KQkq - 0 2" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="6" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Nc6 | 4.7 M (24.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/4/43 | 0 | — | ⚠ |
| d5 | 3.7 M (19.7%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 49/6/45 | 13 k (33.2%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 28/45/27 |  |
| e6 | 3.1 M (16.3%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 50/5/46 | 3.0 k (7.9%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 29/42/29 |  |
| d6 | 2.9 M (15.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 50/5/45 | 2.7 k (7.2%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 34/35/30 |  |
| Nf6 | 2.6 M (13.6%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/6/47 | 17 k (44.6%) | ⬜⬜🟫🟫🟫🟫🟫⬛⬛⬛ 26/46/27 |  |
| g6 | 955 k (5.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/5/47 | 1.3 k (3.3%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 34/37/30 |  |
| e5 | 0 | — | 497 (1.3%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 35/37/28 |  |

*Online: bullet/blitz, 1800+ — 18.8 M games. Masters: 38 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pp1ppppp/8/2p5/4P3/2P5/PP1P1PPP/RNBQKBNR_b_KQkq_-_0_2#explorer) — updated 2026-09-02*
<!-- lichess-stats:end -->

**2... Nf6** (44.6% masters) is the main try, attacking e4 at once: after **3. e5 Nd5**, the knight is well placed on d5 and Black continues ... d6, ... Nc6, and ... g6/... e6 depending on taste. **2... d5** (33.2% masters) strikes back in the centre immediately instead, and after **3. exd5 Qxd5 4. d4**, White develops with tempo against the queen — a structure similar in spirit to the Center Game.

* [**2... Nf6**](#_Nf6_) (44.6% masters): the line this card follows further — covered below.
* **2... d5** (33.2% masters): strikes back immediately. Not built out further here (backlog).

[*Back to TOP*](#_TOP_)

---

<a name="_Nf6_"></a>

## 2... Nf6 3. e5 Nd5 4. Nf3 Nc6

[![4... Nc6](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/pp1ppppp/2n5/2pnP3/8/2P2N2/PP1P1PPP/RNBQKB1R&lastMove=b8c6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/pp1ppppp/2n5/2pnP3/8/2P2N2/PP1P1PPP/RNBQKB1R_w_KQkq_-_3_5)

*... 4... Nc6*

```
r1bqkb1r/pp1ppppp/2n5/2pnP3/8/2P2N2/PP1P1PPP/RNBQKB1R w KQkq - 3 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

**5. Na3**, live-tagged the *Heidenfeld Variation*, develops the knight toward c4 rather than the more natural-looking Bc4 or d4 — a genuine, if minor, named try (85 masters games). Masters split between **5... g6** (40.0%) and **5... d6** (34.1%). Deeper Alapin theory past this point is its own extensive body of work, not covered further here.

[*Back to TOP*](#_TOP_)

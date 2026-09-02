<a name="_TOP_"></a>

# B74 Sicilian Defense: Dragon Variation, Classical Variation, Normal Line <br> 1. e4 c5 2. Nf3 d6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 g6 6. Be3 Bg7 7. Be2 Nc6 8. O-O O-O 9. Nb3 #

Spun off from [`B73_Sicilian_Dragon_Classical_OO.md`](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B73_Sicilian_Dragon_Classical_OO.md)'s own 9th-move fork — masters' top try there (38.2%). Live-tagged the *Normal Line*. The deepest, most heavily analysed tabiya in the whole Classical Variation, with several named historical tries branching off it.

<a name="_initial_move_"></a>

[![9. Nb3](https://backscattering.de/web-boardimage/board.svg?fen=r1bq1rk1/pp2ppbp/2np1np1/8/4P3/1NN1B3/PPP1BPPP/R2Q1RK1&lastMove=d4b3&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bq1rk1/pp2ppbp/2np1np1/8/4P3/1NN1B3/PPP1BPPP/R2Q1RK1_b_-_-_7_9)

*... 9. Nb3 — Normal Line*

```
r1bq1rk1/pp2ppbp/2np1np1/8/4P3/1NN1B3/PPP1BPPP/R2Q1RK1 b - - 7 9
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.0 |
| --- | --- |

<!-- lichess-stats:start fen="r1bq1rk1/pp2ppbp/2np1np1/8/4P3/1NN1B3/PPP1BPPP/R2Q1RK1 b - - 7 9" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Be6 | 40 k (38.5%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/6/47 | 713 (70.7%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 27/38/35 |  |
| a6 | 22 k (21.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/5/45 | 124 (12.3%) | ⬜⬜⬜🟫🟫⬛⬛⬛⬛⬛ 27/26/47 |  |
| Bd7 | 19 k (18.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 0 | — | ⚠ |
| a5 | 12 k (11.3%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 46/6/49 | 76 (7.5%) | ⬜⬜⬜🟫🟫🟫⬛⬛⬛⬛ 24/33/43 |  |
| b6 | 0 | — | 54 (5.4%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 30/37/33 |  |

*Online: bullet/blitz, 1800+ — 105 k games. Masters: 1.0 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bq1rk1/pp2ppbp/2np1np1/8/4P3/1NN1B3/PPP1BPPP/R2Q1RK1_b_-_-_7_9#explorer) — updated 2026-09-02*
<!-- lichess-stats:end -->

**9... Be6** is masters' clear main try (70.7%), developing toward the queenside and preparing ... Na5/... Rc8. **9... a5** (7.5%, the *Alekhine Line* — `eco.md`: "Alekhine Variation") is a real independent try, immediately grabbing queenside space rather than developing the bishop first — White replies **10. a4** (86.8%) to keep the pawn from advancing further.

<a name="_afterBe6_"></a>

[![9... Be6](https://backscattering.de/web-boardimage/board.svg?fen=r2q1rk1/pp2ppbp/2npbnp1/8/4P3/1NN1B3/PPP1BPPP/R2Q1RK1&lastMove=c8e6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r2q1rk1/pp2ppbp/2npbnp1/8/4P3/1NN1B3/PPP1BPPP/R2Q1RK1_w_-_-_8_10)

*... 9... Be6*

```
r2q1rk1/pp2ppbp/2npbnp1/8/4P3/1NN1B3/PPP1BPPP/R2Q1RK1 w - - 8 10
```

**10. f4** follows almost automatically (93.2% of masters games), pushing the kingside pawn storm forward. Black's own reply is a genuine three-way fork: **10... Qc8** (42.9%, the *Tartakower Line* — `eco.md`: "Reti-Tartakower Variation" — preparing ... Bh3 to trade off White's own fianchetto-adjacent bishop), **10... Rc8** (29.8%, untagged), and **10... Na5** (21.9%, heading toward the historically-named lines below).

[*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **10... Na5 11. f5** (66.3% masters at that fork) **Bc4** reaches a tabiya with three real historical names attached, all sitting past this card's own depth budget — presented here as brief, honestly-scoped mentions rather than fully diagrammed:
>
> - **12. Bd3** (63.1% masters) — the *Spielmann Variation*. If Black continues **12... Bxd3 13. cxd3 d5**, it's the *Bernard Defense* (a real database rarity, 10 masters games, eval +0.5 — objectively fine for White despite giving up the bishop pair).
> - **12. Nxa5** (27.2% masters) — the *Stockholm Attack* (`eco.md`'s own fuller line: 12. Nxa5 Bxe2 13. Qxe2 Qxa5 14. g4). A genuine database rarity at this exact depth (only 3 masters games), eval dead level (0.0).
>
> Deeper theory for all three is its own extensive, highly specialised body of work, not covered further here.
>
> [*Back to 9... Be6*](#_afterBe6_)
> [*Back to TOP*](#_TOP_)

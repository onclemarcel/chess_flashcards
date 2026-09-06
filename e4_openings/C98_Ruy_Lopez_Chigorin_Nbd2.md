<a name="_TOP_"></a>

# C98 Ruy Lopez: Closed, Chigorin Defense <br> 1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3 Na5 10. Bc2 c5 11. d4 Qc7 12. Nbd2 Nc6 #

Spun off from [C97's own "12. Nbd2" candidate bullet](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C97_Ruy_Lopez_Chigorin.md#_Nbd2c_) — a real, respected regrouping try, already live-tagged its own code. The knight returns to its original square, undoing its own opening tempo, in order to support a later ... d5 or meet dxc5 without conceding the c-file.

<a name="_initial_move_"></a>

[![12... Nc6](https://backscattering.de/web-boardimage/board.svg?fen=r1b2rk1/2q1bppp/p1np1n2/1pp1p3/3PP3/2P2N1P/PPBN1PP1/R1BQR1K1&lastMove=a5c6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1b2rk1/2q1bppp/p1np1n2/1pp1p3/3PP3/2P2N1P/PPBN1PP1/R1BQR1K1_w_-_-_3_13)

*... 12... Nc6 — Chigorin Defense*

```
r1b2rk1/2q1bppp/p1np1n2/1pp1p3/3PP3/2P2N1P/PPBN1PP1/R1BQR1K1 w - - 3 13
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +1.03 |
| --- | --- |

<!-- lichess-stats:start fen="r1b2rk1/2q1bppp/p1np1n2/1pp1p3/3PP3/2P2N1P/PPBN1PP1/R1BQR1K1 w - - 3 13" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| d5 | 11 k (59.0%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/6/47 | 477 (85.0%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 35/47/17 |  |
| Nf1 | 5.9 k (32.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/5/46 | 16 (2.9%) | — |  |
| dxc5 | 424 (2.3%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/8/39 | 47 (8.4%) | ⬜⬜🟫🟫🟫🟫🟫🟫⬛⬛ 19/57/23 |  |
| Nb3 | 392 (2.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/8/40 | 0 | — | ⚠ |
| a3 | 0 | — | 6 (1.1%) | — |  |

*Online: bullet/blitz, 1800+ — 19 k games. Masters: 561 games. [Open in the explorer](https://lichess.org/analysis/standard/r1b2rk1/2q1bppp/p1np1n2/1pp1p3/3PP3/2P2N1P/PPBN1PP1/R1BQR1K1_w_-_-_3_13#explorer) — updated 2026-09-06*
<!-- lichess-stats:end -->

Masters' clear main try is **13. d5** (85.0%), closing the centre now that the knight blocks its own c-pawn's queenside plans — the same structural idea seen on C96's own Borisenko Variation. The rare alternative, **13. dxc5**, carries its own name.

* [**13. dxc5**](#_Rauzer_) (8.4% masters): the *Rauzer Attack* — covered below.

[*Back to TOP*](#_TOP_)

---

<a name="_Rauzer_"></a>

## 13. dxc5 — Rauzer Attack

[![13. dxc5](https://backscattering.de/web-boardimage/board.svg?fen=r1b2rk1/2q1bppp/p1np1n2/1pP1p3/4P3/2P2N1P/PPBN1PP1/R1BQR1K1&lastMove=d4c5&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1b2rk1/2q1bppp/p1np1n2/1pP1p3/4P3/2P2N1P/PPBN1PP1/R1BQR1K1_b_-_-_0_13)

*... 13. dxc5 — Rauzer Attack*

```
r1b2rk1/2q1bppp/p1np1n2/1pP1p3/4P3/2P2N1P/PPBN1PP1/R1BQR1K1 b - - 0 13
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.06 |
| --- | --- |

Resolves the central tension by capturing rather than closing with d5 — a genuine database rarity (47 masters games), and the engine calls the resulting position dead level despite White giving up the centre entirely. Masters' only recorded reply is **13... dxc5**, simply recapturing. Not built out further here (backlog).

[*Back to 12... Nc6*](#_initial_move_)
[*Back to TOP*](#_TOP_)

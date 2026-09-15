<a name="_TOP_"></a>

# E78 King's Indian Defence: Four Pawns Attack, With Be2 and Nf3 <br> 1. d4 Nf6 2. c4 g6 3. Nc3 Bg7 4. e4 d6 5. f4 O-O 6. Be2 c5 7. Nf3 #

Continues from [E77's own "6... c5" node](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E77_Kings_Indian_Four_Pawns_Be2.md#_c5_), where **7. Nf3** is masters' actual majority (54.3%) — genuinely more common than 7. d5 (45.0%), the move that keeps E77's own trunk going. Live-tagged **King's Indian Defense: Four Pawns Attack, Fluid Attack**, a specific name `eco.md`'s own bare "With Be2 and Nf3" doesn't carry.

**A real move-order distinction, verified rather than assumed**: this position is *not* the same as [E77's own "8. Nf3" node](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E77_Kings_Indian_Four_Pawns_Be2.md#_Nf3b_) (also tagged "Four Pawns Attack," reached after 7. d5 e6 8. Nf3 instead). There, d5/e6 have already been played and the centre is locked; here, White develops the knight *before* committing the centre, and Black replies by capturing on d4 instead of pushing ... e6. Confirmed via `tools/apply_san.py`: the two FENs differ (pawns still on c5/d4 here vs. the locked d5/e6 structure there) — a genuine, verified divergence, not merely a naming coincidence.

<a name="_initial_move_"></a>

[![7. Nf3](https://backscattering.de/web-boardimage/board.svg?fen=rnbq1rk1/pp2ppbp/3p1np1/2p5/2PPPP2/2N2N2/PP2B1PP/R1BQK2R&lastMove=g1f3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbq1rk1/pp2ppbp/3p1np1/2p5/2PPPP2/2N2N2/PP2B1PP/R1BQK2R_b_KQ_-_1_7)

*... 7. Nf3 — King's Indian Defence: Four Pawns Attack, With Be2 and Nf3*

```
rnbq1rk1/pp2ppbp/3p1np1/2p5/2PPPP2/2N2N2/PP2B1PP/R1BQK2R b KQ - 1 7
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.23 |
| --- | --- |

<!-- lichess-stats:start fen="rnbq1rk1/pp2ppbp/3p1np1/2p5/2PPPP2/2N2N2/PP2B1PP/R1BQK2R b KQ - 1 7" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="6" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| cxd4 | 21 k (79.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/5/42 | 137 (90.7%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 34/42/24 |  |
| Nc6 | 1.9 k (7.3%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/5/43 | 1 (0.7%) | — | ⚠ |
| Bg4 | 1.6 k (6.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 11 (7.3%) | — |  |
| e6 | 596 (2.3%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/46 | 1 (0.7%) | — | ⚠ |
| Qa5 | 374 (1.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/5/44 | 1 (0.7%) | — | ⚠ |
| a6 | 288 (1.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 52/4/44 | 0 | — | ⚠ |

*Online: bullet/blitz, 1800+ — 26 k games. Masters: 151 games. [Open in the explorer](https://lichess.org/analysis/standard/rnbq1rk1/pp2ppbp/3p1np1/2p5/2PPPP2/2N2N2/PP2B1PP/R1BQK2R_b_KQ_-_1_7#explorer) — updated 2026-09-15*
<!-- lichess-stats:end -->

### Candidate moves

* [**7... cxd4**](#_cxd4_) (+0.12, 90.7% masters): masters' overwhelming main try — see below, this card's own trunk, leading to [E79](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E79_Kings_Indian_Four_Pawns_Main_Line.md).
* **7... Bg4** (7.3% masters): a real, minor secondary with no code of its own in this range.

[*Back to TOP*](#_TOP_)

---

<a name="_cxd4_"></a>

## 7... cxd4 8. Nxd4 Nc6

**7... cxd4** is masters' overwhelming main try (90.7%). **8. Nxd4** follows automatically (100% masters). **8... Nc6** is masters' clear main reply (77.5%), hitting the centralised knight at once.

[![8... Nc6](https://backscattering.de/web-boardimage/board.svg?fen=r1bq1rk1/pp2ppbp/2np1np1/8/2PNPP2/2N5/PP2B1PP/R1BQK2R&lastMove=b8c6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bq1rk1/pp2ppbp/2np1np1/8/2PNPP2/2N5/PP2B1PP/R1BQK2R_w_KQ_-_1_9)

*... 7... cxd4 8. Nxd4 Nc6*

```
r1bq1rk1/pp2ppbp/2np1np1/8/2PNPP2/2N5/PP2B1PP/R1BQK2R w KQ - 1 9
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.21 |
| --- | --- |

<!-- lichess-stats:start fen="r1bq1rk1/pp2ppbp/2np1np1/8/2PNPP2/2N5/PP2B1PP/R1BQK2R w KQ - 1 9" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="6" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Be3 | 13 k (62.0%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 54/6/40 | 101 (91.8%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 35/44/22 |  |
| Nxc6 | 3.0 k (13.9%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 45/5/50 | 4 (3.6%) | — | ⚠ |
| Nc2 | 2.2 k (10.3%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 60/3/37 | 5 (4.5%) | — |  |
| O-O | 1.8 k (8.5%) | ⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛ 39/4/56 | 0 | — | ⚠ |
| Nf3 | 775 (3.6%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 43/5/52 | 0 | — | ⚠ |
| Nb3 | 199 (0.9%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/6/46 | 0 | — | ⚠ |

*Online: bullet/blitz, 1800+ — 21 k games. Masters: 110 games. [Open in the explorer](https://lichess.org/analysis/standard/r1bq1rk1/pp2ppbp/2np1np1/8/2PNPP2/2N5/PP2B1PP/R1BQK2R_w_KQ_-_1_9#explorer) — updated 2026-09-15*
<!-- lichess-stats:end -->

White's own 9th move is masters' clear main try, **9. Be3** (91.8%), reaching [E79](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E79_Kings_Indian_Four_Pawns_Main_Line.md).

### Candidate moves

* [**9. Be3**](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E79_Kings_Indian_Four_Pawns_Main_Line.md) (+0.13, 91.8% masters): masters' clear main try — the Main line, its own card, E79.
* **9. Nxc6** (13.9% online, 3.6% masters) / **9. Nc2** (10.3% online, 4.5% masters): real, uncoded secondaries — online play spreads more evenly than masters here.

[*Back to 7. Nf3*](#_initial_move_)
[*Back to TOP*](#_TOP_)

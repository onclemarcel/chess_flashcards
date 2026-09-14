<a name="_TOP_"></a>

# C71 Ruy Lopez: Modern Steinitz Defense <br> 1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 d6 #

Spun off from [C70's own "4... d6" candidate bullet](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C70_Ruy_Lopez_Deferred_Defenses.md#_initial_move_) — a real minority try there (6.0% masters), already live-tagged its own code. Solidifies e5 a second time, the same idea as the direct 3... d6 Steinitz Defense, just delayed a tempo since the bishop has already retreated to a4. Each different 5th move for White escalates its own code from here: **5. O-O** → [C72](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C72_Ruy_Lopez_Modern_Steinitz_Castle.md), **5. Bxc6+ ...6. d4** → [C73](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C73_Ruy_Lopez_Modern_Steinitz_Richter.md), **5. c3** → [C74](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C74_Ruy_Lopez_Modern_Steinitz_Siesta.md)/[C75](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C75_Ruy_Lopez_Modern_Steinitz_Rubinstein.md)/[C76](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C76_Ruy_Lopez_Modern_Steinitz_Fianchetto.md) — while **5. d4**, **5. Nc3**, and **5. c4** all stay at this parent code, C71.

<a name="_initial_move_"></a>

[![4... d6](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/1pp2ppp/p1np4/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R&lastMove=d7d6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/1pp2ppp/p1np4/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R_w_KQkq_-_0_5)

*... 4... d6 — Modern Steinitz Defense*

```
r1bqkbnr/1pp2ppp/p1np4/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.30 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkbnr/1pp2ppp/p1np4/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 5" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="6" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| O-O | 281 k (40.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/46 | 2.6 k (41.3%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 39/38/23 |  |
| c3 | 164 k (23.5%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/5/45 | 2.2 k (35.2%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 35/41/24 |  |
| d4 | 100 k (14.3%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 42/6/52 | 290 (4.6%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 25/42/33 |  |
| h3 | 75 k (10.7%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/46 | 0 | — | ⚠ |
| d3 | 30 k (4.3%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/46 | 0 | — | ⚠ |
| Bxc6+ | 21 k (3.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/6/43 | 847 (13.3%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 36/36/28 |  |
| c4 | 0 | — | 280 (4.4%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 34/40/26 |  |
| Nc3 | 0 | — | 34 (0.5%) | ⬜⬜⬜⬜⬜🟫🟫🟫⬛⬛ 44/32/24 |  |

*Online: bullet/blitz, 1800+ — 700 k games. Masters: 6.4 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkbnr/1pp2ppp/p1np4/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R_w_KQkq_-_0_5#explorer) — updated 2026-09-14*
<!-- lichess-stats:end -->

Masters' reply forks five ways: **O-O** 41.3% (→ C72), **c3** 35.2% (→ C74/C75/C76), **Bxc6+** 13.3% (→ C73), **d4** 4.6% (stays C71, the Noah's Ark Trap tabiya), **c4** 4.4% (stays C71, Duras/Keres Variation), **Nc3** 0.5% (stays C71, Three Knights Variation).

* [**5. d4**](#_d4_) — leads toward the famous Noah's Ark Trap — covered below.
* [**5. Nc3**](#_ThreeKnights_) — *Three Knights Variation* — covered below.
* [**5. c4**](#_Duras_) — *Duras (Keres) Variation* — covered below.
* **5. O-O** (41.3% masters): its own code, [C72](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C72_Ruy_Lopez_Modern_Steinitz_Castle.md).
* **5. Bxc6+** (13.3% masters): its own code, [C73](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C73_Ruy_Lopez_Modern_Steinitz_Richter.md).
* **5. c3** (35.2% masters): its own codes, [C74](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C74_Ruy_Lopez_Modern_Steinitz_Siesta.md)/[C75](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C75_Ruy_Lopez_Modern_Steinitz_Rubinstein.md)/[C76](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C76_Ruy_Lopez_Modern_Steinitz_Fianchetto.md).

[*Back to TOP*](#_TOP_)

---

<a name="_d4_"></a>

### 5. d4 — toward the Noah's Ark Trap

[![5. d4](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/1pp2ppp/p1np4/4p3/B2PP3/5N2/PPP2PPP/RNBQK2R&lastMove=d2d4&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/1pp2ppp/p1np4/4p3/B2PP3/5N2/PPP2PPP/RNBQK2R_b_KQkq_d3_0_5)

*... 5. d4*

```
r1bqkbnr/1pp2ppp/p1np4/4p3/B2PP3/5N2/PPP2PPP/RNBQK2R b KQkq d3 0 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.00 |
| --- | --- |

Strikes the center immediately rather than castling or supporting with c3 first (4.6% masters). Masters split between **5... b5** (74.5%, kicking the bishop before anything else) and **5... Bd7** (20.0%). The **5... b5 6. Bb3 Nxd4 7. Nxd4 exd4 8. Qxd4 c5** sequence is the famous, named ***Noah's Ark Trap*** tabiya:

[![Noah's Ark Trap](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/5ppp/p2p4/1pp5/3QP3/1B6/PPP2PPP/RNB1K2R&lastMove=c6c5&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/5ppp/p2p4/1pp5/3QP3/1B6/PPP2PPP/RNB1K2R_w_KQkq_c6_0_9)

```
r1bqkbnr/5ppp/p2p4/1pp5/3QP3/1B6/PPP2PPP/RNB1K2R w KQkq c6 0 9
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −2.87 |
| --- | --- |

A genuine, major engine swing toward Black (−2.87) — c5 traps the queen, and no matter where she retreats, Black's advancing queenside pawns (b5-c5-...b4/c4) win a full piece back a move or two later. Masters' replies here are **8. Qd5** (66.7%) and **8. Qd3** (22.2%), both real tries to salvage something rather than simply losing material outright, but the engine confirms the trap's fearsome practical reputation is fully deserved. Not built out further here beyond this trap summary (backlog).

[*Back to 4... d6*](#_initial_move_)
[*Back to TOP*](#_TOP_)

---

<a name="_ThreeKnights_"></a>

### 5. Nc3 — Three Knights Variation

[![5. Nc3](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/1pp2ppp/p1np4/4p3/B3P3/2N2N2/PPPP1PPP/R1BQK2R&lastMove=b1c3&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/1pp2ppp/p1np4/4p3/B3P3/2N2N2/PPPP1PPP/R1BQK2R_b_KQkq_-_1_5)

*... 5. Nc3 — Three Knights Variation*

```
r1bqkbnr/1pp2ppp/p1np4/4p3/B3P3/2N2N2/PPPP1PPP/R1BQK2R b KQkq - 1 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.16 |
| --- | --- |

Develops the queenside knight before committing the king, a genuine minority try (0.5% masters). Masters split between **5... Bd7** (67.6%) and **5... Nf6** (23.5%). Not built out further here (backlog).

[*Back to 4... d6*](#_initial_move_)
[*Back to TOP*](#_TOP_)

---

<a name="_Duras_"></a>

### 5. c4 — Duras (Keres) Variation

[![5. c4](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/1pp2ppp/p1np4/4p3/B1P1P3/5N2/PP1P1PPP/RNBQK2R&lastMove=c2c4&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/1pp2ppp/p1np4/4p3/B1P1P3/5N2/PP1P1PPP/RNBQK2R_b_KQkq_c3_0_5)

*... 5. c4 — Duras (Keres) Variation*

```
r1bqkbnr/1pp2ppp/p1np4/4p3/B1P1P3/5N2/PP1P1PPP/RNBQK2R b KQkq c3 0 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.21 |
| --- | --- |

Grabs extra queenside space at once rather than developing or castling — a genuine minority try (4.4% masters). Masters split between **5... Bg4** (47.1%) and **5... Bd7** (31.1%). Not built out further here (backlog).

[*Back to 4... d6*](#_initial_move_)
[*Back to TOP*](#_TOP_)

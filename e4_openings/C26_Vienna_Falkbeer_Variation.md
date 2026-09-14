<a name="_TOP_"></a>

# C26 Vienna Game: Falkbeer Variation <br> 1. e4 e5 2. Nc3 Nf6 #

Spun off from [`C25_Vienna_Game.md`](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md)'s own candidate list — masters' main line by a wide margin (72.0% of C25 masters games). Already live-tagged its own code, **C26**, the *Falkbeer Variation* — attacking e4 at once, forcing White to make a concrete decision on move 3 rather than complete development at leisure.

<a name="_initial_move_"></a>

[![2... Nf6](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR&lastMove=g8f6&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR_w_KQkq_-_2_3)

*... 2... Nf6 — Falkbeer Variation*

```
rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR w KQkq - 2 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR w KQkq - 2 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="6" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Nf3 | 3.5 M (34.8%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/46 | 1.1 k (17.0%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 26/51/23 |  |
| f4 | 2.7 M (26.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 54/4/42 | 1.2 k (18.4%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 29/41/30 |  |
| Bc4 | 2.0 M (20.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 51/5/45 | 1.6 k (24.1%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 27/44/29 |  |
| d3 | 660 k (6.7%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/5/48 | 0 | — | ⚠ |
| g3 | 542 k (5.5%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 54/5/41 | 2.3 k (35.1%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 31/47/22 |  |
| d4 | 267 k (2.7%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 50/4/46 | 274 (4.2%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 40/32/28 |  |
| a3 | 0 | — | 45 (0.7%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 38/42/20 |  |

*Online: bullet/blitz, 1800+ — 9.9 M games. Masters: 6.6 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N5/PPPP1PPP/R1BQKBNR_w_KQkq_-_2_3#explorer) — updated 2026-09-14*
<!-- lichess-stats:end -->

No White try dominates the masters statistics the way Nf6 itself did for Black: **3. g3** (35.1% masters), **3. Bc4** (24.1%), **3. f4** (18.4%, the sharp *Vienna Gambit*), and **3. Nf3** (17.0%, transposing back toward C40) are all seen regularly, and Stockfish rates all four within a few hundredths of a pawn of each other. Online, **3. Nf3** is the most reached-for (34.8%).

### Candidate moves

* [**3. g3**](#_g3_) (0.0, 35.1% masters): the *Paulsen-Mieses Variation* — masters' top choice, flexible, avoiding early commitments while preparing Bg2. See below.
* [**3. Bc4**](#_Bc4_) (0.0, 24.1% masters): live-tagged the *Stanley Variation* — see below.
* [**3. f4**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C29_Vienna_Gambit.md) (-0.2, 18.4% masters): already live-tagged its own code, **C29**, the *Vienna Gambit* — the code attaches at this exact move, before Black even replies. See `C29_Vienna_Gambit.md`, not built out further here.
* **3. Nf3** (+0.1, 17.0% masters): the calmest choice, folding back into King's Knight Opening themes a tempo down for Black. Stays C26, not built out further here.
* [**3. a3**](#_a3_) (0.7% masters): the *Mengarini Variation* — see below.

[*Back to TOP*](#_TOP_)

---

<a name="_a3_"></a>

> [!NOTE]
> **3. a3** is the *Mengarini Variation* — a slow, prophylactic try (preparing b4) rather than an immediate central commitment.
>
> [![3. a3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/pppp1ppp/5n2/4p3/4P3/P1N5/1PPP1PPP/R1BQKBNR&lastMove=a2a3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/5n2/4p3/4P3/P1N5/1PPP1PPP/R1BQKBNR_b_KQkq_-_0_3)
>
> *... 3. a3 — Mengarini Variation*
>
> ```
> rnbqkb1r/pppp1ppp/5n2/4p3/4P3/P1N5/1PPP1PPP/R1BQKBNR b KQkq - 0 3
> ```
>
> | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.1 |
> | --- | --- |
>
> **3... Nc6** is masters' main try (48.8%), a real database rarity even so (86 masters games). Deeper theory not covered further here.
>
> [*Back to TOP*](#_TOP_)

---

<a name="_g3_"></a>

## 3. g3 — Paulsen-Mieses Variation

[![3. g3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N3P1/PPPP1P1P/R1BQKBNR&lastMove=g2g3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N3P1/PPPP1P1P/R1BQKBNR_b_KQkq_-_0_3)

*... 3. g3 — Paulsen-Mieses Variation*

```
rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N3P1/PPPP1P1P/R1BQKBNR b KQkq - 0 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N3P1/PPPP1P1P/R1BQKBNR b KQkq - 0 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| d5 | 142 k (26.0%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 48/7/45 | 1.1 k (47.8%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 28/49/22 |  |
| Nc6 | 139 k (25.6%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 56/5/39 | 236 (10.2%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 39/38/23 |  |
| Bc5 | 122 k (22.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 55/5/40 | 742 (32.2%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 31/49/20 |  |
| Bb4 | 64 k (11.8%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 55/5/40 | 0 | — | ⚠ |
| c6 | 0 | — | 89 (3.9%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 35/34/31 |  |

*Online: bullet/blitz, 1800+ — 545 k games. Masters: 2.3 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/5n2/4p3/4P3/2N3P1/PPPP1P1P/R1BQKBNR_b_KQkq_-_0_3#explorer) — updated 2026-09-14*
<!-- lichess-stats:end -->

**3... d5** is masters' clear main try (47.8%), striking in the centre while White's own kingside development is only half-finished. Deeper theory not covered further here.

[*Back to TOP*](#_TOP_)

---

<a name="_Bc4_"></a>

## 3. Bc4 — Stanley Variation

[![3. Bc4](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/pppp1ppp/5n2/4p3/2B1P3/2N5/PPPP1PPP/R1BQK1NR&lastMove=f1c4&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/5n2/4p3/2B1P3/2N5/PPPP1PPP/R1BQK1NR_b_KQkq_-_3_3)

*... 3. Bc4 — Stanley Variation*

```
rnbqkb1r/pppp1ppp/5n2/4p3/2B1P3/2N5/PPPP1PPP/R1BQK1NR b KQkq - 3 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

Live-tagged the *Stanley Variation* — a name `eco.md`'s own bare "Vienna Game" label at this position doesn't carry.

<!-- lichess-stats:start fen="rnbqkb1r/pppp1ppp/5n2/4p3/2B1P3/2N5/PPPP1PPP/R1BQK1NR b KQkq - 3 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Bc5 | 938 k (27.4%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 51/4/45 | 392 (19.1%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 27/47/26 |  |
| Nc6 | 906 k (26.5%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 50/5/45 | 965 (47.1%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 27/45/28 |  |
| Nxe4 | 466 k (13.6%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/5/48 | 466 (22.8%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 30/43/27 |  |
| Bb4 | 377 k (11.0%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 51/4/45 | 124 (6.1%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 27/39/35 |  |

*Online: bullet/blitz, 1800+ — 3.4 M games. Masters: 2.0 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/5n2/4p3/2B1P3/2N5/PPPP1PPP/R1BQK1NR_b_KQkq_-_3_3#explorer) — updated 2026-09-14*
<!-- lichess-stats:end -->

Genuine three-way fork: **3... Nc6** (47.1% masters) reaches its own further code, and **3... Nxe4** (22.8%) also reaches its own further code — both already live-tagged separately.

### Candidate moves

* [**3... Nxe4**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C27_Vienna_Frankenstein_Dracula.md) (22.8% masters): already live-tagged **C27**, the *Frankenstein-Dracula Variation* — see `C27_Vienna_Frankenstein_Dracula.md`, not built out further here.
* [**3... Nc6**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C28_Vienna_Stanley_Three_Knights.md) (47.1% masters): already live-tagged **C28**, the *Three Knights Variation* — see `C28_Vienna_Stanley_Three_Knights.md`, not built out further here.
* **3... Bc5** (19.1% masters): stays C26, not built out further here.
* **3... Bb4** (6.1% masters): stays C26, not built out further here.

[*Back to TOP*](#_TOP_)

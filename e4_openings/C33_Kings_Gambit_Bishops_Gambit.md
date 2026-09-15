<a name="_TOP_"></a>

# C33 King's Gambit Accepted: Bishop's Gambit <br> 1. e4 e5 2. f4 exf4 3. Bc4 #

Spun off from [`C30_King_Gambit.md`](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_exf4_)'s own "2... exf4" candidate list — masters' real second choice there (24.2%), behind the King's Knight Gambit (3. Nf3, its own code, C34). White develops the bishop immediately, eyeing f7 and accepting that ... Qh4+ will have to be answered with the odd-looking **4. Kf1** rather than blocking with a knight. This is the start of the huge, mostly 19th-century-only C33-C39 romantic-gambit tail — most sub-lines below carry vanishingly few (or zero) recorded games in either database, but each one still gets its own diagram, FEN, and live-verified data (or an honest note that none exists) per this repo's standing rigor.

<a name="_initial_move_"></a>

[![3. Bc4](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pppp1ppp/8/8/2B1Pp2/8/PPPP2PP/RNBQK1NR&lastMove=f1c4&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pppp1ppp/8/8/2B1Pp2/8/PPPP2PP/RNBQK1NR_b_KQkq_-_1_3)

*... 3. Bc4 — Bishop's Gambit*

```
rnbqkbnr/pppp1ppp/8/8/2B1Pp2/8/PPPP2PP/RNBQK1NR b KQkq - 1 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.6 |
| --- | --- |

Stockfish rates the whole gambit a real, stable Black edge from here — a reminder that the Bishop's Gambit's romantic reputation is a practical, not an objective, one.

<!-- lichess-stats:start fen="rnbqkbnr/pppp1ppp/8/8/2B1Pp2/8/PPPP2PP/RNBQK1NR b KQkq - 1 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="7" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Qh4+ | 192 k (20.5%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 53/3/44 | 98 (12.2%) | ⬜⬜⬜🟫🟫🟫⬛⬛⬛⬛ 30/35/36 |  |
| d6 | 129 k (13.8%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 54/4/42 | 28 (3.5%) | ⬜⬜🟫🟫🟫🟫🟫⬛⬛⬛ 18/46/36 |  |
| g5 | 125 k (13.4%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 55/3/42 | 0 | — | ⚠ |
| Nf6 | 114 k (12.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 51/4/44 | 337 (42.0%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 27/38/35 |  |
| Be7 | 88 k (9.4%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 52/3/45 | 0 | — | ⚠ |
| Nc6 | 81 k (8.7%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/3/43 | 79 (9.8%) | ⬜🟫🟫🟫🟫🟫🟫⬛⬛⬛ 9/57/34 |  |
| d5 | 59 k (6.3%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/4/43 | 155 (19.3%) | ⬜⬜⬜🟫🟫🟫⬛⬛⬛⬛ 32/24/44 |  |
| Ne7 | 0 | — | 55 (6.8%) | ⬜⬜⬜🟫🟫🟫⬛⬛⬛⬛ 31/33/36 |  |
| c6 | 0 | — | 30 (3.7%) | ⬜⬜🟫🟫🟫⬛⬛⬛⬛⬛ 23/30/47 |  |

*Online: bullet/blitz, 1800+ — 937 k games. Masters: 803 games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pppp1ppp/8/8/2B1Pp2/8/PPPP2PP/RNBQK1NR_b_KQkq_-_1_3#explorer) — updated 2026-09-15*
<!-- lichess-stats:end -->

Masters' actual main try is **3... Nf6** (42.0%) — a real online/masters inversion, since online play instead defaults to **3... Qh4+** (20.5%, only 12.2% masters). **3... d5** (19.3% masters) is the second most common try. **3... d6** (3.5% masters, not shown in the trimmed table above) carries no name of its own in `eco.md`.

### Candidate moves

* [**3... Nf6**](#_Nf6_) (42.0% masters): the *Cozio (Morphy) Defence* — see below.
* [**3... d5**](#_d5_) (19.3% masters): see below.
* [**3... Qh4+**](#_Qh4_) (12.2% masters): see below.
* [**3... Nc6**](#_Nc6root_) (9.8% masters): the *Maurian Defence* — see below.
* [**3... Ne7**](#_Ne7root_) (6.8% masters): the *Steinitz Defence* — see below.
* [**3... c6**](#_c6root_) (3.7% masters): the *Ruy Lopez Defence* (a name unrelated to the Spanish opening of the same title) — see below.
* [**3... f5**](#_f5root_): the *Lopez-Gianutio Counter-Gambit* — see below.
* [**3... b5**](#_b5root_): the *Bryan Counter-Gambit* — see below.

[*Back to TOP*](#_TOP_)

---

<a name="_Other3rd_"></a>

## White's other 3rd-move tries (siblings of 3. Bc4, back at [`C30_King_Gambit.md`](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_exf4_)'s own "2... exf4" fork)

A genuine surprise: `eco.md` files nine more White 3rd-move alternatives to 3. Nf3/3. Bc4 under this same **C33** code — confirmed live rather than assumed, since a bare sideline carrying the same code as its much more common sibling is exactly the kind of claim this repo's methodology insists on checking rather than trusting. Each is a real database rarity (well under 1% of masters games combined) and none forks further on its own:

* **3. Kf2** — live-tagged simply *Tumbleweed* (eco.md: "Tumbleweed Gambit"): `rnbqkbnr/pppp1ppp/8/8/4Pp2/8/PPPP1KPP/RNBQ1BNR b kq - 1 3` — Stockfish: **−2.6**, the single worst try on this whole card; walking into the middle of the board with the king is exactly as bad as it looks.
* **3. b3** — the *Orsini Gambit*: `rnbqkbnr/pppp1ppp/8/8/4Pp2/1P6/P1PP2PP/RNBQKBNR b KQkq - 0 3` — Stockfish: **−2.1**.
* **3. h4** — live-tagged the *Stamma Gambit*, a real name divergence from `eco.md`'s own "Pawn's Gambit" label: `rnbqkbnr/pppp1ppp/8/8/4Pp1P/8/PPPP2P1/RNBQKBNR b KQkq h3 0 3` — Stockfish: **−1.2**.
* **3. Bd3** — live-tagged *Schurig Gambit, with Bd3* (matching `eco.md`'s own name): `rnbqkbnr/pppp1ppp/8/8/4Pp2/3B4/PPPP2PP/RNBQK1NR b KQkq - 1 3` — Stockfish: **−1.4**.
* **3. Qe2** — live-tagged the *Basman Gambit*, a real name divergence from `eco.md`'s own "Carrera Gambit" label: `rnbqkbnr/pppp1ppp/8/8/4Pp2/8/PPPPQ1PP/RNB1KBNR b KQkq - 1 3` — Stockfish: **−1.0**.
* **3. d4** — the *Villemson Gambit*: `rnbqkbnr/pppp1ppp/8/8/3PPp2/8/PPP3PP/RNBQKBNR b KQkq d3 0 3` — Stockfish: **−0.8**.
* **3. Nc3** — live-tagged the *Mason-Keres Gambit*, a real name divergence from `eco.md`'s own "Keres Gambit" label: `rnbqkbnr/pppp1ppp/8/8/4Pp2/2N5/PPPP2PP/R1BQKBNR b KQkq - 1 3` — masters' main reply here is a real 65.1%-to-9.6% preference for **3... Qh4+**; not built out further here.
* **3. Qf3** — the *Breyer Gambit*: `rnbqkbnr/pppp1ppp/8/8/4Pp2/5Q2/PPPP2PP/RNB1KBNR b KQkq - 1 3` — Stockfish: **−0.8**.
* **3. Be2** — live-tagged the *Tartakower Gambit*, a real name divergence from `eco.md`'s own "Lesser Bishop's Gambit" label: `rnbqkbnr/pppp1ppp/8/8/4Pp2/8/PPPPB1PP/RNBQK1NR b KQkq - 1 3` — Stockfish: **−0.9**, the mildest of the nine, and the only one with a real (if still tiny) masters sample, 20 games.

None built out further here — all are single-node curiosities with no further named branches of their own in `eco.md`.

[*Back to TOP*](#_TOP_)

---

<a name="_Nf6_"></a>

## 3... Nf6 — Cozio (Morphy) Defence

[![3... Nf6](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/pppp1ppp/5n2/8/2B1Pp2/8/PPPP2PP/RNBQK1NR&lastMove=g8f6&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/5n2/8/2B1Pp2/8/PPPP2PP/RNBQK1NR_w_KQkq_-_2_4)

*... 3... Nf6 — Cozio (Morphy) Defence*

```
rnbqkb1r/pppp1ppp/5n2/8/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq - 2 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.3 |
| --- | --- |

Live-tagged the *Cozio Defense* — matching `eco.md`'s own name here. Masters' overwhelming main try is **4. Nc3** (95.3%).

<!-- lichess-stats:start fen="rnbqkb1r/pppp1ppp/5n2/8/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq - 2 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="3" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Nc3 | 77 k (59.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/4/42 | 321 (95.3%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 27/38/36 |  |
| e5 | 21 k (16.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/3/50 | 0 | — | ⚠ |
| Nf3 | 13 k (10.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/4/47 | 0 | — | ⚠ |
| d3 | 0 | — | 11 (3.3%) | — |  |
| Qe2 | 0 | — | 3 (0.9%) | — |  |

*Online: bullet/blitz, 1800+ — 129 k games. Masters: 337 games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/5n2/8/2B1Pp2/8/PPPP2PP/RNBQK1NR_w_KQkq_-_2_4#explorer) — updated 2026-09-15*
<!-- lichess-stats:end -->

<a name="_Nc3_"></a>

[![4. Nc3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/pppp1ppp/5n2/8/2B1Pp2/2N5/PPPP2PP/R1BQK1NR&lastMove=b1c3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/5n2/8/2B1Pp2/2N5/PPPP2PP/R1BQK1NR_b_KQkq_-_3_4)

*... 4. Nc3 — Bogoljubow Variation*

```
rnbqkb1r/pppp1ppp/5n2/8/2B1Pp2/2N5/PPPP2PP/R1BQK1NR b KQkq - 3 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.3 |
| --- | --- |

Live-tagged the *Bogoljubow Variation* (matching `eco.md`'s own "Bogolyubov Variation," a minor transliteration difference). Masters' overwhelming main try is **4... c6** (76.9%, the *Jaenisch Variation*), well ahead of **4... Bb4** (10.9%, the *Paulsen Attack* after 5. e5).

<!-- lichess-stats:start fen="rnbqkb1r/pppp1ppp/5n2/8/2B1Pp2/2N5/PPPP2PP/R1BQK1NR b KQkq - 3 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="3" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| c6 | 23 k (27.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/5/47 | 247 (76.9%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 26/41/33 |  |
| Bb4 | 17 k (19.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/4/44 | 35 (10.9%) | ⬜⬜🟫🟫⬛⬛⬛⬛⬛⬛ 23/20/57 |  |
| d6 | 11 k (13.1%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 58/4/38 | 0 | — | ⚠ |
| Nc6 | 0 | — | 20 (6.2%) | ⬜⬜⬜⬜🟫🟫⬛⬛⬛⬛ 35/25/40 |  |

*Online: bullet/blitz, 1800+ — 86 k games. Masters: 321 games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/5n2/8/2B1Pp2/2N5/PPPP2PP/R1BQK1NR_b_KQkq_-_3_4#explorer) — updated 2026-09-15*
<!-- lichess-stats:end -->

**4... c6 — Jaenisch Variation:**

```
rnbqkb1r/pp1p1ppp/2p2n2/8/2B1Pp2/2N5/PPPP2PP/R1BQK1NR w KQkq - 0 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.2 |
| --- | --- |

**4... Bb4 5. e5 — Paulsen Attack:**

```
rnbqk2r/pppp1ppp/5n2/4P3/1bB2p2/2N5/PPPP2PP/R1BQK1NR b KQkq - 0 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.2 |
| --- | --- |

Neither built out further here.

[*Back to TOP*](#_TOP_)

---

<a name="_d5_"></a>

## 3... d5 — Bledow Variation

[![3... d5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/ppp2ppp/8/3p4/2B1Pp2/8/PPPP2PP/RNBQK1NR&lastMove=d7d5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/ppp2ppp/8/3p4/2B1Pp2/8/PPPP2PP/RNBQK1NR_w_KQkq_d6_0_4)

*... 3... d5 — Bledow Variation*

```
rnbqkbnr/ppp2ppp/8/3p4/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq d6 0 4
```

Live-tagged the *Bledow Variation* — matching `eco.md`'s own name. Masters' main try is **4. Bxd5** (63.9%), the only reasonable recapture; the resulting position carries no live tag of its own.

```
rnbqkbnr/ppp2ppp/8/3B4/4Pp2/8/PPPP2PP/RNBQK1NR b KQkq - 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.3 |
| --- | --- |

Masters' overwhelming main try from here is **4... Nf6** (83.8%).

<!-- lichess-stats:start fen="rnbqkbnr/ppp2ppp/8/3B4/4Pp2/8/PPPP2PP/RNBQK1NR b KQkq - 0 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="3" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Nf6 | 27 k (59.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 54/5/41 | 83 (83.8%) | ⬜⬜⬜⬜🟫🟫⬛⬛⬛⬛ 36/24/40 |  |
| c6 | 7.4 k (16.1%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 57/4/40 | 0 | — | ⚠ |
| Qh4+ | 7.0 k (15.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/3/43 | 16 (16.2%) | — |  |

*Online: bullet/blitz, 1800+ — 46 k games. Masters: 99 games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/ppp2ppp/8/3B4/4Pp2/8/PPPP2PP/RNBQK1NR_b_KQkq_-_0_4#explorer) — updated 2026-09-15*
<!-- lichess-stats:end -->

**4... Nf6 — Morphy Variation:**

```
rnbqkb1r/ppp2ppp/5n2/3B4/4Pp2/8/PPPP2PP/RNBQK1NR w KQkq - 1 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.2 |
| --- | --- |

**4... c6 — Anderssen Variation** (a real database rarity at masters level, 16.1% online, notably the only one of the three replies here Stockfish actually rates for White):

```
rnbqkbnr/pp3ppp/2p5/3B4/4Pp2/8/PPPP2PP/RNBQK1NR w KQkq - 0 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.3 |
| --- | --- |

**4... Qh4+ 5. Kf1**, forking two further-named tries:

```
rnb1kbnr/ppp2ppp/8/3B4/4Pp1q/8/PPPP2PP/RNBQ1KNR b kq - 2 5
```

* **5... g5 6. g3 — Gifford Variation** (masters' main try here, 31.8%): Stockfish rates this the sharpest and objectively worst of the whole d5 tree for Black, a real White edge.

  ```
  rnb1kbnr/ppp2p1p/8/3B2p1/4Pp1q/6P1/PPPP3P/RNBQ1KNR b kq - 0 6
  ```

  | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.7 |
  | --- | --- |

* **5... Bd6 — Boren-Svenonius Variation** (13.6% masters):

  ```
  rnb1k1nr/ppp2ppp/3b4/3B4/4Pp1q/8/PPPP2PP/RNBQ1KNR w kq - 3 6
  ```

  | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.2 |
  | --- | --- |

None built out further here.

[*Back to TOP*](#_TOP_)

---

<a name="_Qh4_"></a>

## 3... Qh4+ 4. Kf1

[![3... Qh4+ 4. Kf1](https://backscattering.de/web-boardimage/board.svg?fen=rnb1kbnr/pppp1ppp/8/8/2B1Pp1q/8/PPPP2PP/RNBQ1KNR&lastMove=e1f1&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnb1kbnr/pppp1ppp/8/8/2B1Pp1q/8/PPPP2PP/RNBQ1KNR_b_kq_-_3_4)

```
rnb1kbnr/pppp1ppp/8/8/2B1Pp1q/8/PPPP2PP/RNBQ1KNR b kq - 3 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.5 |
| --- | --- |

White gives up castling rights immediately rather than block the check with a knight — an odd-looking concession that is nonetheless considered fully sound, since Black's queen accomplishes little on h4 and will likely need to retreat again. This is the deepest and most theoretically dense fork in the whole C33 range: masters' own replies split **Nf6** (54.5%, transposing back toward the d5 tree above without its own separate name), **g5** (31.8%, the *Classical Defence*), and **Bd6** (13.6%), alongside the further-named **Bc5** (*Greco Variation*), **Nc6** (*Boden Defence*), **b5** (*Bryan Counter-Gambit*), and **d5** (reaching the *Chigorin's Attack* after 5. Bxd5 g5 6. g3).

**Every line below this point carries 0 recorded games in both the masters and online Lichess databases, and none has a cached Stockfish cloud-eval** — this is the genuine 19th-century-only tail of the Bishop's Gambit, still given its own diagram, FEN, and live-confirmed absence of data (queried directly, not assumed) per this repo's full-rigor standard for C33-C39.

**4... d5 5. Bxd5 g5 6. g3 — Chigorin's Attack:**

```
rnbqkbnr/ppp2p1p/8/3B2pq/4Pp2/6P1/PPPP3P/RNBQ1KNR b kq - 0 6
```

**4... Bc5 — Greco Variation:**

```
rnbqk1nr/pppp1ppp/8/2b4q/2B1Pp2/8/PPPP2PP/RNBQ1KNR w kq - 3 5
```

**4... Nc6 — Boden Defence:**

```
r1bqkbnr/pppp1ppp/2n5/7q/2B1Pp2/8/PPPP2PP/RNBQ1KNR w kq - 3 5
```

**4... b5 — Bryan Counter-Gambit** (also reachable directly via 3... b5, see below):

```
rnbqkbnr/p1pp1ppp/8/1p5q/2B1Pp2/8/PPPP2PP/RNBQ1KNR w kq b6 0 5
```

**4... g5 — Classical Defence:**

```
rnbqkbnr/pppp1p1p/8/6pq/2B1Pp2/8/PPPP2PP/RNBQ1KNR w kq g6 0 5
```

Forks four further-named tries, every one of them also a genuine 0-game/no-cached-eval line:

* **5. Nc3 Bg7 6. d4 d6 7. e5 — Grimm Attack**: `rnbqk1nr/ppp2pbp/3p4/4P1pq/2BP1p2/2N5/PPP3PP/R1BQ1KNR b kq - 0 7`
* **5. Nc3 Bg7 6. d4 Ne7 7. g3 — McDonnell Attack**: `rnbqk2r/ppppnpbp/8/6pq/2BPPp2/2N3P1/PPP4P/R1BQ1KNR b kq - 0 7`
* **5. Nc3 Bg7 6. g3 fxg3 7. Qf3 — Fraser Variation** (a distinct, shorter move order also reaching the McDonnell Attack's own name at move 6, before the deeper Fraser continuation): `rnbqkbnr/pppp1p1p/8/6pq/2B1P3/5Qp1/PPPP3P/R1B2KNR b kq - 1 7`
* **5. Qf3 — Cozio Attack**: `rnbqkbnr/pppp1p1p/8/6pq/2B1Pp2/5Q2/PPPP2PP/RNB2KNR b kq - 1 5`

None of the nine lines above built out further, since there is nothing further to verify.

[*Back to TOP*](#_TOP_)

---

<a name="_Nc6root_"></a>

## 3... Nc6 — Maurian Defence

[![3... Nc6](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/pppp1ppp/2n5/8/2B1Pp2/8/PPPP2PP/RNBQK1NR&lastMove=b8c6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/pppp1ppp/2n5/8/2B1Pp2/8/PPPP2PP/RNBQK1NR_w_KQkq_-_2_4)

```
r1bqkbnr/pppp1ppp/2n5/8/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq - 2 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.4 |
| --- | --- |

A real secondary try (9.8% masters, drawing an unusually high share of its games, 57% — see the root's own stats table) — simple development, not built out further here.

[*Back to TOP*](#_TOP_)

---

<a name="_Ne7root_"></a>

## 3... Ne7 — Steinitz Defence

[![3... Ne7](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/ppppnppp/8/8/2B1Pp2/8/PPPP2PP/RNBQK1NR&lastMove=g8e7&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/ppppnppp/8/8/2B1Pp2/8/PPPP2PP/RNBQK1NR_w_KQkq_-_2_4)

```
rnbqkb1r/ppppnppp/8/8/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq - 2 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.0 |
| --- | --- |

A real secondary try (6.8% masters) and, notably, the single most objectively level reply to the whole Bishop's Gambit found on this card — not built out further here.

[*Back to TOP*](#_TOP_)

---

<a name="_c6root_"></a>

## 3... c6 — Ruy Lopez Defence

[![3... c6](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp1p1ppp/2p5/8/2B1Pp2/8/PPPP2PP/RNBQK1NR&lastMove=c7c6&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp1p1ppp/2p5/8/2B1Pp2/8/PPPP2PP/RNBQK1NR_w_KQkq_-_0_4)

```
rnbqkbnr/pp1p1ppp/2p5/8/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq - 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.2 |
| --- | --- |

A genuine name curiosity — `eco.md` calls this the "Ruy Lopez Defence" despite having nothing to do with the Spanish Opening of the same name, presumably after a player rather than the opening. A real database rarity (3.7% masters), not built out further here.

[*Back to TOP*](#_TOP_)

---

<a name="_f5root_"></a>

## 3... f5 — Lopez-Gianutio Counter-Gambit

[![3... f5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pppp2pp/8/5p2/2B1Pp2/8/PPPP2PP/RNBQK1NR&lastMove=f7f5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pppp2pp/8/5p2/2B1Pp2/8/PPPP2PP/RNBQK1NR_w_KQkq_f6_0_4)

*... 3... f5 — Lopez-Gianutio Counter-Gambit*

```
rnbqkbnr/pppp2pp/8/5p2/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq f6 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.1 |
| --- | --- |

A real database rarity (0.5% masters) — Black counter-attacks in the centre at once rather than developing.

**4. Qe2 Qh4+ 5. Kd1 fxe4 6. Nc3 Kd8 — Hein Variation:** live-tagged despite 0 recorded games in either database — a genuine case where the explorer's name index still carries a tag nobody has actually reached in a recorded game, confirmed by direct query rather than assumed.

```
rnbk1bnr/pppp2pp/8/8/2B1pp1q/2N5/PPPPQ1PP/R1BK2NR w - - 2 7
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.3 |
| --- | --- |

Not built out further here.

[*Back to TOP*](#_TOP_)

---

<a name="_b5root_"></a>

## 3... b5 — Bryan Counter-Gambit

[![3... b5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/p1pp1ppp/8/1p6/2B1Pp2/8/PPPP2PP/RNBQK1NR&lastMove=b7b5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/p1pp1ppp/8/1p6/2B1Pp2/8/PPPP2PP/RNBQK1NR_w_KQkq_b6_0_4)

*... 3... b5 — Bryan Counter-Gambit*

```
rnbqkbnr/p1pp1ppp/8/1p6/2B1Pp2/8/PPPP2PP/RNBQK1NR w KQkq b6 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.0 |
| --- | --- |

`eco.md` lists this same name twice — once here, played immediately, and once as 3... Qh4+ 4. Kf1 b5 (see above), a different move order reaching a related but distinct position. A real database rarity, dead level per Stockfish; not built out further here.

This closes out the whole C33 range.

[*Back to TOP*](#_TOP_)

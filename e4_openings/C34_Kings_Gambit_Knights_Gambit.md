<a name="_TOP_"></a>

# C34 King's Gambit Accepted: King's Knight's Gambit <br> 1. e4 e5 2. f4 exf4 3. Nf3 #

Spun off from [`C30_King_Gambit.md`](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_exf4_)'s own "2... exf4" candidate list — by far masters' most common try there (71.8%). White develops naturally, guards against ... Qh4+, and prepares to meet Black's attempt to hold the extra pawn with h4 or d4-based play. This code covers the King's Knight's Gambit hub itself plus five minor, shallow Black tries; the three deeper systems (Cunningham Defence, Abbazia Defence, and the huge ... g5 romantic-gambit complex) each already carry their own further code.

<a name="_initial_move_"></a>

[![3. Nf3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pppp1ppp/8/8/4Pp2/5N2/PPPP2PP/RNBQKB1R&lastMove=g1f3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pppp1ppp/8/8/4Pp2/5N2/PPPP2PP/RNBQKB1R_b_KQkq_-_1_3)

*... 3. Nf3 — King's Knight's Gambit*

```
rnbqkbnr/pppp1ppp/8/8/4Pp2/5N2/PPPP2PP/RNBQKB1R b KQkq - 1 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.4 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/pppp1ppp/8/8/4Pp2/5N2/PPPP2PP/RNBQKB1R b KQkq - 1 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="7" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| g5 | 2.5 M (27.3%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/3/48 | 876 (36.8%) | ⬜⬜🟫🟫🟫🟫⬛⬛⬛⬛ 24/42/34 |  |
| d6 | 1.4 M (15.3%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 50/4/46 | 439 (18.4%) | ⬜⬜⬜🟫🟫🟫⬛⬛⬛⬛ 26/34/41 |  |
| Be7 | 1.2 M (13.4%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/3/49 | 170 (7.1%) | ⬜⬜⬜🟫🟫🟫⬛⬛⬛⬛ 31/31/39 |  |
| d5 | 1.2 M (13.4%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/4/47 | 336 (14.1%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 30/43/27 |  |
| Nc6 | 806 k (8.8%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 54/3/42 | 0 | — | ⚠ |
| Nf6 | 711 k (7.8%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/4/47 | 203 (8.5%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 25/43/33 |  |
| h6 | 402 k (4.4%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/3/50 | 133 (5.6%) | ⬜⬜⬜⬜🟫🟫⬛⬛⬛⬛ 38/22/40 |  |
| Ne7 | 0 | — | 200 (8.4%) | ⬜⬜🟫🟫🟫🟫⬛⬛⬛⬛ 24/36/40 |  |

*Online: bullet/blitz, 1800+ — 9.1 M games. Masters: 2.4 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pppp1ppp/8/8/4Pp2/5N2/PPPP2PP/RNBQKB1R_b_KQkq_-_1_3#explorer) — updated 2026-09-07*
<!-- lichess-stats:end -->

Masters' overwhelming main try is **3... g5** (36.8%), holding the extra pawn and hunting for a further one on e4/h2 — the start of the huge C37-C39 romantic-gambit complex. **3... d6** (18.4%, the *Fischer Defence*), **3... d5** (14.1%, the *Abbazia Defence*, already its own code C36), and **3... Be7** (7.1%, the *Cunningham Defence*, already its own code C35) are all real tries.

### Candidate moves

* [**3... g5**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md) (36.8% masters): stays coded C34 itself, but forks immediately into the huge C37-C39 romantic-gambit complex — see `C37_Kings_Gambit_Muzio_Complex.md`, not built out further here.
* [**3... d6**](#_d6_) (18.4% masters): the *Fischer Defense* — see below.
* [**3... Be7**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C35_Kings_Gambit_Cunningham_Defense.md) (7.1% masters): the *Cunningham Defense* — already live-tagged its own code, **C35** — see `C35_Kings_Gambit_Cunningham_Defense.md`, not built out further here.
* [**3... d5**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C36_Kings_Gambit_Abbazia_Defense.md) (14.1% masters): already live-tagged its own code, **C36** — see `C36_Kings_Gambit_Abbazia_Defense.md`, not built out further here.
* [**3... Nf6**](#_Nf6_) (8.5% masters): the *Schallopp Defense* — see below.
* [**3... h6**](#_h6_) (5.6% masters): the *Becker Defense* — see below.
* [**3... Ne7**](#_Ne7_) (8.4% masters): the *Bonsch-Osmolovsky Variation* — see below.
* [**3... f5**](#_f5_): the *Gianutio Countergambit* — see below.

[*Back to TOP*](#_TOP_)

---

<a name="_d6_"></a>

## 3... d6 — Fischer Defense

[![3... d6](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/ppp2ppp/3p4/8/4Pp2/5N2/PPPP2PP/RNBQKB1R&lastMove=d7d6&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/ppp2ppp/3p4/8/4Pp2/5N2/PPPP2PP/RNBQKB1R_w_KQkq_-_0_4)

*... 3... d6 — Fischer Defense*

```
rnbqkbnr/ppp2ppp/3p4/8/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq - 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.2 |
| --- | --- |

Named for Bobby Fischer's own 1961 essay "A Bust to the King's Gambit," which recommended this exact move — a real database rarity (18.4% masters despite the fame of the recommendation) that simply supports ... g5 without committing the g-pawn yet. Masters' main follow-up is 4. d4 (62.7%); not built out further here.

[*Back to TOP*](#_TOP_)

---

<a name="_Ne7_"></a>

## 3... Ne7 — Bonsch-Osmolovsky Variation

[![3... Ne7](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/ppppnppp/8/8/4Pp2/5N2/PPPP2PP/RNBQKB1R&lastMove=g8e7&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/ppppnppp/8/8/4Pp2/5N2/PPPP2PP/RNBQKB1R_w_KQkq_-_2_4)

```
rnbqkb1r/ppppnppp/8/8/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq - 2 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.1 |
| --- | --- |

A real secondary try (8.4% masters) — the knight eyes g6 to defend the extra pawn from a safer square than f6. Not built out further here.

[*Back to TOP*](#_TOP_)

---

<a name="_h6_"></a>

## 3... h6 — Becker Defense

[![3... h6](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pppp1pp1/7p/8/4Pp2/5N2/PPPP2PP/RNBQKB1R&lastMove=h7h6&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pppp1pp1/7p/8/4Pp2/5N2/PPPP2PP/RNBQKB1R_w_KQkq_-_0_4)

```
rnbqkbnr/pppp1pp1/7p/8/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq - 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.2 |
| --- | --- |

A real secondary try (5.6% masters) — pre-empting Ng5 before committing to ... g5 itself. Not built out further here.

[*Back to TOP*](#_TOP_)

---

<a name="_Nf6_"></a>

## 3... Nf6 — Schallopp Defense

[![3... Nf6](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/pppp1ppp/5n2/8/4Pp2/5N2/PPPP2PP/RNBQKB1R&lastMove=g8f6&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/5n2/8/4Pp2/5N2/PPPP2PP/RNBQKB1R_w_KQkq_-_2_4)

*... 3... Nf6 — Schallopp Defense*

```
rnbqkb1r/pppp1ppp/5n2/8/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq - 2 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.3 |
| --- | --- |

Attacks e4 directly rather than holding the extra f4-pawn. Masters' main reply is 4. e5 (74.1%), gaining a tempo on the knight; not built out further here.

[*Back to TOP*](#_TOP_)

---

<a name="_f5_"></a>

## 3... f5 — Gianutio Countergambit

[![3... f5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pppp2pp/8/5p2/4Pp2/5N2/PPPP2PP/RNBQKB1R&lastMove=f7f5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pppp2pp/8/5p2/4Pp2/5N2/PPPP2PP/RNBQKB1R_w_KQkq_f6_0_4)

*... 3... f5 — Gianutio Countergambit*

```
rnbqkbnr/pppp2pp/8/5p2/4Pp2/5N2/PPPP2PP/RNBQKB1R w KQkq f6 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
| --- | --- |

A genuine database rarity (4 masters games) and the only try on this card Stockfish actually rates for White — counter-attacking e4 rather than holding the f4-pawn gives it back immediately. Not built out further here.

This closes out the whole C34 range.

[*Back to TOP*](#_TOP_)

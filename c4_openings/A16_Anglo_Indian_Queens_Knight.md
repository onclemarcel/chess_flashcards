<a name="_TOP_"></a>

# A16 English Opening: Anglo-Indian Defense, Queen's Knight Variation <br> 1. c4 Nf6 2. Nc3 #

**Corrected 2026-08-25**: spun off from [A15_Anglo_Indian_Defense.md](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A15_Anglo_Indian_Defense.md), which used to build this whole "2. Nc3" branch (masters' clear favourite, 59.2%) as if it stayed A15. It doesn't — live-confirmed via the Lichess explorer's own `opening` field, and cross-checked against [chessopenings.com's ECO reference](https://chessopenings.com/eco/A16): the bare position right after 2. Nc3, before Black has even replied, is already **A16**. Same class of "wrong root code" bug already found and fixed elsewhere in this repo (A02/A04/B10, see `memory.md`). White develops the queen's knight, preparing e4 or g3 next.

<a name="_Nc3_"></a>

[![1. c4 Nf6 2. Nc3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/pppppppp/5n2/8/2P5/2N5/PP1PPPPP/R1BQKBNR&lastMove=b1c3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/pppppppp/5n2/8/2P5/2N5/PP1PPPPP/R1BQKBNR_b_KQkq_-_2_2)

*... 1. c4 Nf6 2. Nc3 — Anglo-Indian Defense: Queen's Knight Variation*

```
rnbqkb1r/pppppppp/5n2/8/2P5/2N5/PP1PPPPP/R1BQKBNR b KQkq - 2 2
```

<!-- lichess-stats:start fen="rnbqkb1r/pppppppp/5n2/8/2P5/2N5/PP1PPPPP/R1BQKBNR b KQkq - 2 2" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="8" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| g6 | 5.2 M (36.5%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/5/45 | 9.4 k (28.7%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 41/37/22 |  |
| e6 | 4.0 M (28.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/5/45 | 6.3 k (19.3%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 39/42/19 |  |
| e5 | 1.2 M (8.7%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 7.3 k (22.4%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 29/50/21 |  |
| c5 | 1.0 M (7.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/6/45 | 5.2 k (16.0%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 37/41/21 |  |
| d5 | 1.0 M (7.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 48/6/46 | 2.9 k (8.9%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 41/39/19 |  |
| d6 | 789 k (5.6%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/45 | 577 (1.8%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 41/37/21 |  |
| c6 | 595 k (4.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/5/45 | 794 (2.4%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 42/42/16 |  |
| b6 | 174 k (1.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/5/45 | 93 (0.3%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 38/35/27 |  |

*Online: bullet/blitz, 1800+ — 14.2 M games. Masters: 33 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/pppppppp/5n2/8/2P5/2N5/PP1PPPPP/R1BQKBNR_b_KQkq_-_2_2#explorer) — updated 2026-08-31*
<!-- lichess-stats:end -->

### Candidate moves

* [**2... g6**](#_g6_) (+0.5): masters' top choice (28.7%) — a King's Indian-style fianchetto against the English, covered below
* [**2... e6**](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A17_Anglo_Indian_Hedgehog.md) (+0.2, 19.3% masters): the **A17** Hedgehog System — covered on its own card
* [**2... e5**](#_e5_) (+0.2): the Two Knights Variation (22.4%) — transposes into **A22**, covered on [A21_Kings_English_Reversed_Sicilian.md](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A21_Kings_English_Reversed_Sicilian.md), the same tabiya reached from the other move order
* [**2... c5**](#_c5_) (+0.2): transposes into **A34**, the Symmetrical Variation's own Three Knights tabiya, covered on [A30_Symmetrical_Variation.md](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A30_Symmetrical_Variation.md)
* [**2... d5**](#_d5_) (+0.3): the Anglo-Grünfeld Defense (8.9% masters) — stays A16, covered in a NOTE below

[*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **2... e6**, played 19.3% of the time at master level, is live-confirmed **A17** — the *Hedgehog System*, split off into its own card, [`A17_Anglo_Indian_Hedgehog.md`](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A17_Anglo_Indian_Hedgehog.md) (which also covers **A18** Mikenas-Carls and **A19** Mikenas-Carls: Sicilian, both reached a few plies further down this same line, each split into their own cards too).
>
> [*Back to 2. Nc3*](#_Nc3_)
> [*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **2... d5**, the Anglo-Grünfeld Defense, is met almost exclusively by **3. cxd5** (92.8% masters) — a real but secondary try (8.9% masters) compared with 2... g6. This branch stays A16 throughout (the code doesn't advance further here per the live-confirmed ECO reference).
>
> <a name="_d5_"></a>
>
> ### 2... d5 — Anglo-Grünfeld Defense
>
> [![1. c4 Nf6 2. Nc3 d5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/ppp1pppp/5n2/3p4/2P5/2N5/PP1PPPPP/R1BQKBNR&lastMove=d7d5&coordinates=true&size=280)](https://lichess.org/analysis/standard/rnbqkb1r/ppp1pppp/5n2/3p4/2P5/2N5/PP1PPPPP/R1BQKBNR_w_KQkq_-_0_3)
>
> *... 2... d5 — English Opening: Anglo-Indian Defense, Anglo-Grünfeld Defense*
>
> ```
> rnbqkb1r/ppp1pppp/5n2/3p4/2P5/2N5/PP1PPPPP/R1BQKBNR w KQkq - 0 3
> ```
>
> | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.3 |
> | --- | --- |
>
> Not built out further here (backlog). Deeper named A16 sub-lines, all mention-only: after **3. cxd5 Nxd5**, White's **4. Nf3** (generic Anglo-Grünfeld, +0.2) meets a later ... g6/... Bg7/... e5 in the ***Korchnoi Variation*** (4. Nf3 g6 5. g3 Bg7 6. Bg2 e5, +0.4); **4. g3 g6 5. Bg2** forks into the ***Smyslov Defence*** (5... Nxc3, +0.5) and the ***Czech Defence*** (5... Nb6, +0.6).
>
> [*Back to 2. Nc3*](#_Nc3_)
> [*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **2... e5**, the Two Knights Variation, is the second-most common try (22.4%) here — but it is the *exact same tabiya* as reached via 1. c4 e5 2. Nc3 Nf6 on the reversed-Sicilian side, tagged **A22**. See [A22_Two_Knights_Variation.md](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A22_Two_Knights_Variation.md) for the actual coverage, kept in one place rather than duplicated.
>
> <a name="_e5_"></a>
>
> ### 2... e5 — transposes to A22 (Two Knights Variation)
>
> [![1. c4 Nf6 2. Nc3 e5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/pppp1ppp/5n2/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR&lastMove=e7e5&coordinates=true&size=280)](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/5n2/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR_w_KQkq_e6_0_3)
>
> *... 2... e5 — King's English Variation: Two Knights Variation*
>
> ```
> rnbqkb1r/pppp1ppp/5n2/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR w KQkq e6 0 3
> ```
>
> | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
> | --- | --- |
>
> [*Back to 2. Nc3*](#_Nc3_)
> [*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **2... c5**, the third real try here (16.0%), most often continues **3. Nf3** (50.9% masters) straight into **A34**, the Symmetrical Variation's own Three Knights tabiya. See [A30_Symmetrical_Variation.md](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A30_Symmetrical_Variation.md#_Nc3_) for the actual coverage, kept in one place rather than duplicated.
>
> <a name="_c5_"></a>
>
> ### 2... c5 — transposes to A34 (Symmetrical, Three Knights)
>
> [![1. c4 Nf6 2. Nc3 c5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/pp1ppppp/5n2/2p5/2P5/2N5/PP1PPPPP/R1BQKBNR&lastMove=c7c5&coordinates=true&size=280)](https://lichess.org/analysis/standard/rnbqkb1r/pp1ppppp/5n2/2p5/2P5/2N5/PP1PPPPP/R1BQKBNR_w_KQkq_c6_0_3)
>
> *... 2... c5*
>
> ```
> rnbqkb1r/pp1ppppp/5n2/2p5/2P5/2N5/PP1PPPPP/R1BQKBNR w KQkq c6 0 3
> ```
>
> | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
> | --- | --- |
>
> [*Back to 2. Nc3*](#_Nc3_)
> [*Back to TOP*](#_TOP_)

---

<a name="_g6_"></a>

## 2... g6

Masters' top try (28.7%): Black meets the English with a King's Indian-style fianchetto rather than an immediate central pawn move.

[![1. c4 Nf6 2. Nc3 g6](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/pppppp1p/5np1/8/2P5/2N5/PP1PPPPP/R1BQKBNR&lastMove=g7g6&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/pppppp1p/5np1/8/2P5/2N5/PP1PPPPP/R1BQKBNR_w_KQkq_-_0_3)

*... 2... g6*

```
rnbqkb1r/pppppp1p/5np1/8/2P5/2N5/PP1PPPPP/R1BQKBNR w KQkq - 0 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.5 |
| --- | --- |

White's 3rd move is a genuine two-way split, both aiming at King's Indian-style middlegames:

* **3. e4** (43.0% masters): grabs the maximum centre immediately, directly transposing into the [King's Indian Defense](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E70_Kings_Indian.md) tabiya if Black continues ... Bg7/... d6
* **3. g3** (38.5% masters): the more distinctly "English" try, fianchettoing before committing the centre
* **3. d4** (12.4% masters): transposes straight into the [King's Indian/Grünfeld fork](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E61_KID_Grunfeld_Fork.md) from the d4 side

None of these are built out from the English move order yet in this repository (backlog).

[*Back to 2. Nc3*](#_Nc3_)
[*Back to TOP*](#_TOP_)

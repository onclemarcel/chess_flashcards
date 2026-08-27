<a name="_TOP_"></a>

# E01 Catalan Opening <br> 1. d4 Nf6 2. c4 e6 3. g3 d5 4. Bg2 #

Spun off from [E00's own "3... d5" reply](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E00_Catalan.md#_d5_): masters' clear main try at White's 4th move (55.1%), completing the fianchetto and reaching the point where the Catalan's three real branches split. Live-confirmed its own code via the Lichess explorer's own `opening` field, which tags this exact bare tabiya the *Open Defense* — a genuinely confusing name, since `eco.md`'s own entry for this same position instead calls it "Catalan Opening, Closed." Neither name is really earned yet at this exact leaf; Black's own next move is what actually decides open vs. closed.

<a name="_initial_move_"></a>

[![4. Bg2](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/6P1/PP2PPBP/RNBQK1NR&lastMove=f1g2&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/6P1/PP2PPBP/RNBQK1NR_b_KQkq_-_1_4)

*... 4. Bg2 — reaching the main Catalan tabiya*

```
rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/6P1/PP2PPBP/RNBQK1NR b KQkq - 1 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.1 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/6P1/PP2PPBP/RNBQK1NR b KQkq - 1 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Be7 | 352 k (31.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/7/43 | 4.0 k (36.6%) | ⬜⬜⬜🟫🟫🟫🟫🟫🟫⬛ 28/57/14 |  |
| c6 | 254 k (22.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/6/41 | 283 (2.6%) | ⬜⬜⬜⬜⬜🟫🟫🟫⬛⬛ 46/35/19 |  |
| dxc4 | 148 k (13.3%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/6/43 | 3.1 k (28.5%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 27/53/20 |  |
| Bb4+ | 132 k (12.0%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/7/42 | 3.2 k (29.0%) | ⬜⬜🟫🟫🟫🟫🟫🟫⬛⬛ 21/62/17 |  |

*Online: bullet/blitz, 1800+ — 1.1 M games. Masters: 11 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/6P1/PP2PPBP/RNBQK1NR_b_KQkq_-_1_4#explorer) — updated 2026-08-26*
<!-- lichess-stats:end -->

This is the point where the Catalan's three real branches split:

* [**4... Be7**](#_Be7_) (+0.2, 36.6% masters): the *Closed Catalan* — solid, declining the pawn and just finishing development — covered below.
* [**4... dxc4**](#_dxc4_) (+0.2, 28.5% masters): the *Open Catalan* — grabs the pawn, betting the extra material is worth more than letting the Bg2 bishop's diagonal go completely unopposed. Not a blunder: White's compensation is famous but not close to forced, and this remains a fully respected, heavily analysed choice at the top level. Live-confirmed its own code, **E02** — covered below.
* [**4... Bb4+**](#_Bb4_) (+0.2, 29.0% masters): checks with the bishop rather than developing it to e7 — covered below.

Each branch is its own extensive body of theory, on a par with the Nimzo-Indian or Queen's Indian covered elsewhere in this repository.

[*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **4... Be7**, the *Closed Catalan*, simply finishes development and declines the pawn — Black bets that a solid structure is worth more than material. This exact leaf carries no further name of its own; the position stays **E01** until White's 5th move.
>
> <a name="_Be7_"></a>
>
> ### 4... Be7 — Closed Catalan
>
> [![4... Be7](https://backscattering.de/web-boardimage/board.svg?fen=rnbqk2r/ppp1bppp/4pn2/3p4/2PP4/6P1/PP2PPBP/RNBQK1NR&lastMove=f8e7&coordinates=true&size=280)](https://lichess.org/analysis/standard/rnbqk2r/ppp1bppp/4pn2/3p4/2PP4/6P1/PP2PPBP/RNBQK1NR_w_KQkq_-_2_5)
>
> *... 4... Be7 — Closed Catalan*
>
> ```
> rnbqk2r/ppp1bppp/4pn2/3p4/2PP4/6P1/PP2PPBP/RNBQK1NR w KQkq - 2 5
> ```
>
> | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
> | --- | --- |
>
> **5. Nf3** (+0.2) is close to automatic (98.8% of masters games) — completing development before deciding between the main plan (Qc2/Rd1, aiming to recapture on c4 profitably) and other tries. Live-confirmed **5. Nf3** already reaches its own code, **E06** — [covered on its own card](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E06_Catalan_Closed.md).
>
> [*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **4... Bb4+** checks immediately rather than committing the bishop to e7, forcing White to make an early decision about how to meet it. Stays **E01** — no further code attaches to this branch within the E00-E09 range.
>
> <a name="_Bb4_"></a>
>
> ### 4... Bb4+
>
> [![4... Bb4+](https://backscattering.de/web-boardimage/board.svg?fen=rnbqk2r/ppp2ppp/4pn2/3p4/1bPP4/6P1/PP2PPBP/RNBQK1NR&lastMove=f8b4&coordinates=true&size=280)](https://lichess.org/analysis/standard/rnbqk2r/ppp2ppp/4pn2/3p4/1bPP4/6P1/PP2PPBP/RNBQK1NR_w_KQkq_-_2_5)
>
> *... 4... Bb4+*
>
> ```
> rnbqk2r/ppp2ppp/4pn2/3p4/1bPP4/6P1/PP2PPBP/RNBQK1NR w KQkq - 2 5
> ```
>
> | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
> | --- | --- |
>
> **5. Bd2** (+0.2) is masters' clear main try (62.6%) — trading off the dark-squared bishops, since the Catalan's whole plan runs through the *light*-squared one on g2. **5. Nd2** is a real second choice (35.2%), keeping the bishops on and recapturing with the knight instead so the queenside pawn structure stays intact. (This position gets a genuinely different reply than the earlier 3... Bb4+ check, played before ... d5/Bg2 — there 4. Bd2 is close to automatic at 81.6% masters; move-order matters here.) Not built out further here (backlog).
>
> [*Back to TOP*](#_TOP_)

---

<a name="_dxc4_"></a>

## 4... dxc4 — Open Catalan (E02)

[![4... dxc4](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/ppp2ppp/4pn2/8/2pP4/6P1/PP2PPBP/RNBQK1NR&lastMove=d5c4&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/ppp2ppp/4pn2/8/2pP4/6P1/PP2PPBP/RNBQK1NR_w_KQkq_-_0_5)

*... 4... dxc4 — Open Catalan, live-confirmed E02*

```
rnbqkb1r/ppp2ppp/4pn2/8/2pP4/6P1/PP2PPBP/RNBQK1NR w KQkq - 0 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkb1r/ppp2ppp/4pn2/8/2pP4/6P1/PP2PPBP/RNBQK1NR w KQkq - 0 5" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="3" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Nf3 | 127 k (72.6%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/6/42 | 2.6 k (83.3%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 28/52/20 |  |
| Qa4+ | 23 k (12.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/7/44 | 513 (16.4%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 25/55/20 |  |
| Nc3 | 15 k (8.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/4/44 | 4 (0.1%) | — | ⚠ |

*Online: bullet/blitz, 1800+ — 175 k games. Masters: 3.1 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/ppp2ppp/4pn2/8/2pP4/6P1/PP2PPBP/RNBQK1NR_w_KQkq_-_0_5#explorer) — updated 2026-08-26*
<!-- lichess-stats:end -->

Grabs the c4 pawn immediately, betting that holding onto it (or trading it back on White's terms) is worth more than leaving the long diagonal totally uncontested. Not a blunder: White's compensation is famous but not close to forced, and this remains a fully respected, heavily analysed choice at the top level. Live-confirmed this exact leaf already carries its own code, **E02** — White's own 5th-move reply then forks further into deeper codes:

* [**5. Qa4+**](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E02_Catalan_Open_Qa4.md) (+0.1, 16.4% masters): stays **E02** — covered on its own card.
* [**5. Nf3**](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E04_Catalan_Open_Nf3.md) (+0.2, 83.3% masters): masters' overwhelming choice. Live-confirmed its own code, **E04** — covered on its own card.

[*Back to TOP*](#_TOP_)

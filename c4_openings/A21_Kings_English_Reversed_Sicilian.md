<a name="_TOP_"></a>

# A21 English Opening: King's English Variation, Reversed Sicilian <br> 1. c4 e5 2. Nc3 #

**Corrected 2026-08-25**: spun off from [A20_Kings_English_Variation.md](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A20_Kings_English_Variation.md), which used to build this whole "2. Nc3" branch (masters' clear favourite, 62.2%) as if it stayed A20. It doesn't — live-confirmed via the Lichess explorer's own `opening` field, and cross-checked against [chessopenings.com's ECO reference](https://chessopenings.com/eco/A21): the bare position right after 2. Nc3, before Black has even replied, is already **A21**. Same class of "wrong root code" bug already found and fixed elsewhere in this repo (A02/A04/B10, and A15→A16 earlier in this same session — see `memory.md`). The most natural developing move, keeping every plan (g3, e3, or a quick d4) open.

<a name="_Nc3_"></a>

[![1. c4 e5 2. Nc3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pppp1ppp/8/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR&lastMove=b1c3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pppp1ppp/8/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR_b_KQkq_-_1_2)

*... 1. c4 e5 2. Nc3 — King's English Variation, Reversed Sicilian*

```
rnbqkbnr/pppp1ppp/8/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR b KQkq - 1 2
```

<!-- lichess-stats:start fen="rnbqkbnr/pppp1ppp/8/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR b KQkq - 1 2" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="6" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Nf6 | 5.0 M (35.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 18 k (57.1%) | ⬜⬜🟫🟫🟫🟫🟫🟫⬛⬛ 24/56/20 |  |
| Nc6 | 3.4 M (23.9%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 50/5/45 | 6.9 k (22.2%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 35/39/27 |  |
| d6 | 1.6 M (11.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/5/43 | 2.2 k (6.9%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 33/37/30 |  |
| f5 | 1.2 M (8.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/4/43 | 240 (0.8%) | ⬜⬜⬜⬜⬜🟫🟫🟫⬛⬛ 47/28/25 |  |
| Bc5 | 1.1 M (7.6%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 54/4/42 | 0 | — | ⚠ |
| Bb4 | 737 k (5.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/46 | 3.8 k (12.1%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 30/38/32 |  |
| c5 | 0 | — | 123 (0.4%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 33/46/20 |  |

*Online: bullet/blitz, 1800+ — 14.1 M games. Masters: 31 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pppp1ppp/8/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR_b_KQkq_-_1_2#explorer) — updated 2026-08-26*
<!-- lichess-stats:end -->

* [**2... Nf6**](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A22_Two_Knights_Variation.md) (+0.2, 57.1% masters): the **A22** Two Knights Variation — masters' clear main try, covered on its own card (also reachable from [A16_Anglo_Indian_Queens_Knight.md](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A16_Anglo_Indian_Queens_Knight.md#_e5_) via 1... Nf6 2. Nc3 e5)
* [**2... Nc6**](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A25_Reversed_Closed_Sicilian.md) (+0.2, 22.2% masters): the **A25** Reversed Closed Sicilian — a real second try, covered on its own card
* [**2... d6**](#_d6_) (+0.3, 6.9% masters): stays **A21** — covered in a NOTE below
* [**2... Bb4**](#_Bb4_) (+0.2, 12.1% masters): the *Kramnik-Shirov Counterattack* — stays **A21**, covered in a NOTE below
* **2... f5** (+0.2, 0.8% masters): a real minor try, no distinct name of its own here

[*Back to 1. c4 e5*](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A20_Kings_English_Variation.md#_e5_)
[*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **2... d6** keeps the structure flexible before committing a knight. White's 3rd move forks: **3. g3** (55.6% masters) heads for either the ***Troeger Defence*** (3... Be6 4. Bg2 Nc6, +0.5, mention-only) or the ***Keres Defense*** (3... c6, +0.4, mention-only); **3. Nf3** (27.1% masters, +0.3) is met almost exclusively by 3... f5 (70.2%), or by the ***Smyslov Defense*** (3... Bg4, +0.8, mention-only) instead.
>
> <a name="_d6_"></a>
>
> ### 2... d6
>
> [![1. c4 e5 2. Nc3 d6](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/ppp2ppp/3p4/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR&lastMove=d7d6&coordinates=true&size=280)](https://lichess.org/analysis/standard/rnbqkbnr/ppp2ppp/3p4/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR_w_KQkq_-_0_3)
>
> *... 2... d6*
>
> ```
> rnbqkbnr/ppp2ppp/3p4/4p3/2P5/2N5/PP1PPPPP/R1BQKBNR w KQkq - 0 3
> ```
>
> | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.3 |
> | --- | --- |
>
> Not built out further here (backlog).
>
> [*Back to 1. c4 e5 2. Nc3*](#_Nc3_)
> [*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **2... Bb4**, the *Kramnik-Shirov Counterattack*, pins the knight immediately rather than developing normally — a real, well-tested try (12.1% masters), most often met by **3. Nd5** (51.3%).
>
> <a name="_Bb4_"></a>
>
> ### 2... Bb4 — Kramnik-Shirov Counterattack
>
> [![1. c4 e5 2. Nc3 Bb4](https://backscattering.de/web-boardimage/board.svg?fen=rnbqk1nr/pppp1ppp/8/4p3/1bP5/2N5/PP1PPPPP/R1BQKBNR&lastMove=f8b4&coordinates=true&size=280)](https://lichess.org/analysis/standard/rnbqk1nr/pppp1ppp/8/4p3/1bP5/2N5/PP1PPPPP/R1BQKBNR_w_KQkq_-_2_3)
>
> *... 2... Bb4 — Kramnik-Shirov Counterattack*
>
> ```
> rnbqk1nr/pppp1ppp/8/4p3/1bP5/2N5/PP1PPPPP/R1BQKBNR w KQkq - 2 3
> ```
>
> | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
> | --- | --- |
>
> Not built out further here (backlog).
>
> [*Back to 1. c4 e5 2. Nc3*](#_Nc3_)
> [*Back to TOP*](#_TOP_)

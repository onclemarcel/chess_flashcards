<a name="_TOP_"></a>

# A07 King's Indian Attack <br> 1. Nf3 d5 2. g3 #

Spun off from [A06_Zukertort_d5.md](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A06_Zukertort_d5.md), where **2. g3** was masters' clear top try (39.7%) with no card of its own. White fianchettoes the king's bishop before deciding on c4, d4, or even e4 — the setup Bobby Fischer famously used to great effect, sidestepping mainstream theory in favour of a plan that plays similarly against almost anything Black tries.

**A naming precision worth stating up front, verified live rather than assumed**: this exact root position is genuinely A07, but its own main reply (below) dives one ply further into **A05** — the *same* code this repo's own [`A05_Zukertort_Nf6.md`](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A05_Zukertort_Nf6.md) card uses, just under a different name ("King's Indian Attack" here vs. "Zukertort Opening" there — A05 turns out to be another multi-name code, the same shape as `A41_Queens_Pawn_Game.md`'s own finding).

<a name="_initial_move_"></a>

[![2. g3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/ppp1pppp/8/3p4/8/5NP1/PPPPPP1P/RNBQKB1R&lastMove=g2g3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/ppp1pppp/8/3p4/8/5NP1/PPPPPP1P/RNBQKB1R_b_KQkq_-_0_2)

*... 1. Nf3 d5 2. g3 — King's Indian Attack*

```
rnbqkbnr/ppp1pppp/8/3p4/8/5NP1/PPPPPP1P/RNBQKB1R b KQkq - 0 2
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.1 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/ppp1pppp/8/3p4/8/5NP1/PPPPPP1P/RNBQKB1R b KQkq - 0 2" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="6" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Nf6 | 3.2 M (27.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/6/42 | 14 k (36.5%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 37/45/18 |  |
| c6 | 2.0 M (17.0%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/6/42 | 7.9 k (20.9%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 33/43/24 |  |
| c5 | 1.9 M (16.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 55/5/40 | 2.8 k (7.4%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 34/46/20 |  |
| e6 | 1.3 M (11.3%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 55/5/39 | 0 | — | ⚠ |
| Nc6 | 1.3 M (11.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/5/42 | 1.9 k (5.0%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 37/33/30 |  |
| Bg4 | 458 k (4.0%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/6/41 | 4.2 k (11.2%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 34/42/24 |  |
| g6 | 0 | — | 5.1 k (13.6%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 28/48/23 |  |

*Online: bullet/blitz, 1800+ — 11.5 M games. Masters: 38 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/ppp1pppp/8/3p4/8/5NP1/PPPPPP1P/RNBQKB1R_b_KQkq_-_0_2#explorer) — updated 2026-08-26*
<!-- lichess-stats:end -->

### Candidate moves

* [**2... Nf6**](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A05_Zukertort_Nf6.md) (+0.1, 36.5% masters): masters' clear main try — reaches **A05**, covered on its own card (under its "King's Indian Attack" name rather than "Zukertort Opening").
* **2... c6** (+0.1, 20.9% masters): a solid, flexible reply, keeping options for ... Bg4 or ... Bf5 open.
* **2... g6** (+0.1, 13.6% masters): mirrors White's own fianchetto plan.
* **2... Bg4** (+0.1, 11.2% masters): develops actively and pins the knight before White can castle.
* [**2... c5**](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A08_Kings_Indian_Attack_Sicilian.md) (+0.1, 7.4% masters): stakes a claim on the queenside immediately — after 3. Bg2 (92.6% masters), this reaches **A08**, covered on its own card.

Not built out further here (backlog) — each of the remaining real A07-coded siblings above is its own body of theory.

[*Back to TOP*](#_TOP_)

---

> [!NOTE]
> Three named A07 sub-lines sit deeper than this card's own build-out — mention-only, no diagram, each independently verified:
>
> - **Yugoslav Variation** (2... Nf6 3. Bg2 c6 4. O-O Bg4, +0.2): develops actively, pinning the knight once White has castled.
> - **Keres Variation** (2... Bg4 3. Bg2 Nd7, +0.3): pins the knight immediately, before White's own kingside fianchetto is even finished.
> - **Pachman System** (2... g6 3. Bg2 Bg7 4. O-O e5 5. d3 Ne7, +0.2): a King's Indian-style reversed setup, developing the knight to e7 rather than f6.
>
> [*Back to TOP*](#_TOP_)

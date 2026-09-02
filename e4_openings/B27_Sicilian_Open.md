<a name="_TOP_"></a>

# B27 Sicilian Defense <br> 1. e4 c5 2. Nf3 #

Spun off from [B20's own root fork](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B20_Sicilian.md): masters' overwhelming preference at White's 2nd move (82.7%), preparing d4 to trade off Black's c-pawn and open the centre. Live-confirmed its own code via the Lichess explorer's own `opening` field — this whole hub was originally built (and mislabeled) as part of `B20_Sicilian.md`; moved here once the wrong-code bug was caught. Leads to the sharpest and most theoretically dense Sicilian lines.

<a name="_initial_move_"></a>

[![2. Nf3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R&lastMove=g1f3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R_b_KQkq_-_1_2)

*... 2. Nf3 — Open Sicilian*

```
rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="9" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Nc6 | 66.9 M (38.6%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/46 | 135 k (26.9%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 32/44/24 |  |
| d6 | 56.3 M (32.5%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/5/47 | 231 k (46.1%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 30/46/24 |  |
| e6 | 34.0 M (19.7%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/5/49 | 115 k (23.0%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 34/37/28 |  |
| g6 | 8.8 M (5.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/5/48 | 10 k (2.1%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 37/39/24 |  |
| a6 | 3.7 M (2.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 46/5/49 | 4.9 k (1.0%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 35/35/30 |  |
| Nf6 | 1.6 M (0.9%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 45/5/51 | 3.6 k (0.7%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 37/38/25 |  |
| d5 | 853 k (0.5%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 46/5/49 | 0 | — | ⚠ |
| b6 | 463 k (0.3%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 50/4/45 | 588 (0.1%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 37/29/34 |  |
| e5 | 123 k (0.1%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 54/4/42 | 0 | — | ⚠ |
| Qc7 | 0 | — | 55 (0.0%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 38/38/24 |  |
| Qa5 | 0 | — | 48 (0.0%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 46/27/27 |  |

*Online: bullet/blitz, 1800+ — 173.1 M games. Masters: 501 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R_b_KQkq_-_1_2#explorer) — updated 2026-09-02*
<!-- lichess-stats:end -->

Masters are close to evenly split three ways here, and each answer opens into its own vast body of theory:

* [**2... d6**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B50_Sicilian_d6_Open.md) (+0.3, 46.1% masters): prepares ... Nf6 without allowing e5 tricks, keeping options open between the [*Najdorf*](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B50_Sicilian_d6_Open.md), *Classical*, and *Dragon* families depending on how the game continues after 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3.
* [**2... Nc6**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B30_Sicilian_Nc6_Open.md) (+0.3, 26.9% masters): develops naturally and keeps flexible, heading toward the [*Sveshnikov*](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B30_Sicilian_Nc6_Open.md), *Taimanov*, or a *Rossolimo*-style **3. Bb5** setup.
* [**2... e6**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B40_Sicilian_e6_Open.md) (+0.3, 23.0% masters): flexible and solid, aiming for the [*Taimanov* or *Kan*](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B40_Sicilian_e6_Open.md) systems, often delaying ... Nf6 or ... d6 for a move or two.
* [**2... g6**](#_g6_) (+0.3, 2.1% masters): live-tagged the *Hyperaccelerated Dragon* — stays genuinely B27 — covered below.
* [**2... a6**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B28_Sicilian_OKelly.md) (+0.3, 1.0% masters): the *O'Kelly Variation*. Live-confirmed its own code, **B28** — covered on its own card.
* [**2... Nf6**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B29_Sicilian_Nimzovich_Rubinstein.md) (+0.3, 0.7% masters): the *Nimzovich-Rubinstein Variation*. Live-confirmed its own code, **B29** — covered on its own card.
* **2... Qa5** (mention-only): live-tagged the *Mongoose Variation* — see the note below.
* **2... Qc7** (mention-only): the *Quinteros Variation* — see the note below.
* **2... b6** (mention-only): the *Katalimov Variation* — see the note below.

All of the main systems above are fully sound.

[*Back to TOP*](#_TOP_)

---

<a name="_g6_"></a>

## 2... g6 — Hyperaccelerated Dragon

[![2... g6](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp1ppp1p/6p1/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R&lastMove=g7g6&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp1ppp1p/6p1/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R_w_KQkq_-_0_3)

*... 2... g6 — Hyperaccelerated Dragon*

```
rnbqkbnr/pp1ppp1p/6p1/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.3 |
| --- | --- |

Fianchettoes immediately, before even developing the queen's knight — a tempo faster still than the regular Accelerated Dragon (2... Nc6 first, then ... g6 one move later). Live-tagged the *Hyperaccelerated Dragon* (`eco.md` calls it the "Hungarian Variation," a real name divergence). **3. d4** is masters' clear main try (64.6%).

> [!NOTE]
> **A genuine mismatch found while building this card, flagged for a future correction rather than fixed here (out of today's B20-B29 scope)**: `B34_Sicilian_g6_Accelerated_Dragon.md` is currently rooted at this exact position (bare 2... g6) and calls it the "Accelerated Dragon" — but `eco.md`'s own move order for B34 (the *Accelerated Fianchetto*, chessopenings.com's own name for the Accelerated Dragon complex) is actually **2... Nc6 3. d4 cxd4 4. Nxd4 g6** — knight developed *before* the fianchetto, a genuinely different move order from this one. This bare "2... g6" position is B27's own *Hyperaccelerated Dragon*, not B34's Accelerated Dragon. Worth fixing properly when a future B30-B39 batch reaches B34's own real scope.

**3. c3** (19.3% masters) is a real second choice, an Alapin-style approach that sidesteps Open Sicilian theory while the fianchetto is still in progress.

> [!NOTE]
> **2... g6 3. c4 Bh6!?**, the *Acton Extension* (mention-only), develops the bishop actively to h6 rather than g7 — a genuine database curiosity (only 2 masters games, the smallest sample on this whole card).

Not built out further here otherwise (backlog).

[*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **2... Qa5!?**, live-tagged the *Mongoose Variation* (+0.7, mention-only — `eco.md` calls it the "Stiletto Variation," a real name divergence), develops the queen actively and eyes a future ... Qxe4/pin on the c3 knight — a genuine database rarity (48 masters games). **3. Nc3** is masters' clear main reply (60.4%).
>
> [*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **2... Qc7!?**, the *Quinteros Variation* (+0.6, mention-only), develops the queen to a quieter square, eyeing the long diagonal and a future ... e5 — a genuine database rarity (55 masters games).
>
> [*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **2... b6!?**, the *Katalimov Variation* (+0.6, mention-only), fianchettoes the queen's bishop before doing anything else — a real, if minor, try (592 masters games). **3. d4** is masters' clear main reply (72.8%).
>
> [*Back to TOP*](#_TOP_)

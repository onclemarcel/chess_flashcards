<a name="_TOP_"></a>

# E32 Nimzo-Indian Defense: Classical Variation <br> 1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Qc2 #

Spun off from [E20's own root fork](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E20_Nimzo_Indian.md): a real, well-tested try at White's 4th move (33.6% masters) — avoids doubled c-pawns altogether if Black ever takes on c3, at the cost of a slower development. Live-confirmed its own code via the Lichess explorer's own `opening` field — this card was originally built (and mislabeled) as part of `E20_Nimzo_Indian.md`; moved here once the wrong-code bug was caught.

<a name="_initial_move_"></a>

[![4. Qc2](https://backscattering.de/web-boardimage/board.svg?fen=rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N5/PPQ1PPPP/R1B1KBNR&lastMove=d1c2&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N5/PPQ1PPPP/R1B1KBNR_b_KQkq_-_3_4)

*... 4. Qc2 — Classical Variation*

```
rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N5/PPQ1PPPP/R1B1KBNR b KQkq - 3 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.1 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N5/PPQ1PPPP/R1B1KBNR b KQkq - 3 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| O-O | 800 k (35.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 49/6/45 | 16 k (54.0%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 25/54/20 |  |
| c5 | 514 k (22.5%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 49/6/46 | 5.2 k (17.5%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 33/42/25 |  |
| d5 | 407 k (17.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/6/44 | 5.3 k (18.0%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 26/54/20 |  |
| b6 | 248 k (10.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 0 | — | ⚠ |
| d6 | 0 | — | 1.1 k (3.7%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 28/42/31 |  |

*Online: bullet/blitz, 1800+ — 2.3 M games. Masters: 30 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N5/PPQ1PPPP/R1B1KBNR_b_KQkq_-_3_4#explorer) — updated 2026-09-02*
<!-- lichess-stats:end -->

**4... O-O** is masters' clear main try (54.0%), with **4... d5** (18.0%) and **4... c5** (17.5%) both real second choices, fighting for the centre immediately instead.

* [**4... O-O**](#_OO_) (54.0% masters): the line this card follows further — covered below.
* [**4... Nc6**](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E33_Nimzo_Indian_Classical_Zurich.md) (mention-only): the *Zurich Variation*. Live-confirmed its own code, **E33** — covered on its own card.
* [**4... d5**](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E34_Nimzo_Indian_Classical_Noa.md) (18.0% masters): the *Noa Variation*. Live-confirmed its own code, **E34** — covered on its own card.
* [**4... c5**](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E38_Nimzo_Indian_Classical_Berlin.md) (17.5% masters): the *Berlin Variation*. Live-confirmed its own code, **E38** — covered on its own card.

[*Back to TOP*](#_TOP_)

---

<a name="_OO_"></a>

## 4... O-O

[![4... O-O](https://backscattering.de/web-boardimage/board.svg?fen=rnbq1rk1/pppp1ppp/4pn2/8/1bPP4/2N5/PPQ1PPPP/R1B1KBNR&lastMove=e8g8&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbq1rk1/pppp1ppp/4pn2/8/1bPP4/2N5/PPQ1PPPP/R1B1KBNR_w_KQ_-_4_5)

*... 4... O-O*

```
rnbq1rk1/pppp1ppp/4pn2/8/1bPP4/2N5/PPQ1PPPP/R1B1KBNR w KQ - 4 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.1 |
| --- | --- |

**5. a3** is a real, well-tested try, immediately forcing the bishop to decide.

> [!NOTE]
> **5. a3 Bxc3 6. Qxc3 b5!?**, live-tagged the *Vitolins-Adorjan Gambit* (+0.3, mention-only — `eco.md`'s own entry just calls it the "Adorjan Gambit"), offers a queenside pawn for active piece play rather than the calmer recapture. **7. cxb5** is masters' overwhelming reply (94.8%).

Deeper Classical Variation theory past this point is its own extensive body of work, not covered further here.

[*Back to TOP*](#_TOP_)

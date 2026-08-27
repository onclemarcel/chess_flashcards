<a name="_TOP_"></a>

# E15 Queen's Indian Defense: Fianchetto Variation <br> 1. d4 Nf6 2. c4 e6 3. Nf3 b6 4. g3 #

**Corrected 2026-08-26**: this whole tabiya (and everything built past it — the 4... Ba6/Bb7 fork) used to live on [`E12_Queens_Indian.md`](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E12_Queens_Indian.md), built as if it stayed E12. Live-confirmed via the Lichess explorer's own `opening` field: **4. g3** already reaches its own code, **E15** — moved here, matching the same "wrong root code" pattern found repeatedly throughout this project.

<a name="_initial_move_"></a>

[![4. g3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/p1pp1ppp/1p2pn2/8/2PP4/5NP1/PP2PP1P/RNBQKB1R&lastMove=g2g3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/p1pp1ppp/1p2pn2/8/2PP4/5NP1/PP2PP1P/RNBQKB1R_b_KQkq_-_0_4)

*... 4. g3 — Fianchetto Variation*

```
rnbqkb1r/p1pp1ppp/1p2pn2/8/2PP4/5NP1/PP2PP1P/RNBQKB1R b KQkq - 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkb1r/p1pp1ppp/1p2pn2/8/2PP4/5NP1/PP2PP1P/RNBQKB1R b KQkq - 0 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Bb7 | 656 k (67.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/7/43 | 11 k (32.4%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 30/53/17 |  |
| Ba6 | 272 k (27.9%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 46/7/47 | 22 k (61.1%) | ⬜⬜🟫🟫🟫🟫🟫🟫⬛⬛ 24/59/17 |  |
| Bb4+ | 32 k (3.3%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 48/7/45 | 1.9 k (5.3%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 27/53/19 |  |
| c6 | 5.3 k (0.5%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 41/9/50 | 230 (0.6%) | ⬜⬜🟫🟫🟫🟫🟫⬛⬛⬛ 24/51/25 |  |

*Online: bullet/blitz, 1800+ — 976 k games. Masters: 35 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/p1pp1ppp/1p2pn2/8/2PP4/5NP1/PP2PP1P/RNBQKB1R_b_KQkq_-_0_4#explorer) — updated 2026-08-26*
<!-- lichess-stats:end -->

Masters' actual main try, **4... Ba6** (61.1%), is a real online/masters inversion: the natural-looking **4... Bb7** dominates online instead (67.2% online, only 32.4% masters).

* **4... Ba6** (+0.2, 61.1% masters): the *Nimzovich Variation* — see the note below.
* [**4... Bb7**](#_Bb7_) (32.4% masters): the more straightforward alternative, staying **E15** — covered below.

[*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **4... Ba6!?**, the *Nimzovich Variation* (+0.2), takes indirect aim at the c4 pawn from the side rather than developing straight to the long diagonal — forcing White to spend a tempo defending it (e.g. Qc2 or b3) before Black completes development. A genuinely more sophisticated try that's harder to find over the board than it looks in a database, and masters' own actual main choice at this fork despite the online numbers running the other way. Not built out further here (backlog).
>
> [*Back to TOP*](#_TOP_)

---

<a name="_Bb7_"></a>

## 4... Bb7 — Traditional Line

[![4... Bb7](https://backscattering.de/web-boardimage/board.svg?fen=rn1qkb1r/pbpp1ppp/1p2pn2/8/2PP4/5NP1/PP2PP1P/RNBQKB1R&lastMove=c8b7&coordinates=true&size=320)](https://lichess.org/analysis/standard/rn1qkb1r/pbpp1ppp/1p2pn2/8/2PP4/5NP1/PP2PP1P/RNBQKB1R_w_KQkq_-_1_5)

*... 4... Bb7 — Fianchetto Variation, Traditional Line*

```
rn1qkb1r/pbpp1ppp/1p2pn2/8/2PP4/5NP1/PP2PP1P/RNBQKB1R w KQkq - 1 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.3 |
| --- | --- |

<!-- lichess-stats:start fen="rn1qkb1r/pbpp1ppp/1p2pn2/8/2PP4/5NP1/PP2PP1P/RNBQKB1R w KQkq - 1 5" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Bg2 | 816 k (99.3%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/7/43 | 12 k (99.8%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 30/53/17 |  |
| Nc3 | 2.8 k (0.3%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/5/48 | 19 (0.2%) | — |  |
| a3 | 1.2 k (0.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/6/44 | 0 | — | ⚠ |
| Nbd2 | 681 (0.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/6/42 | 0 | — | ⚠ |
| Bd2 | 0 | — | 3 (0.0%) | — |  |
| b3 | 0 | — | 2 (0.0%) | — |  |

*Online: bullet/blitz, 1800+ — 822 k games. Masters: 12 k games. [Open in the explorer](https://lichess.org/analysis/standard/rn1qkb1r/pbpp1ppp/1p2pn2/8/2PP4/5NP1/PP2PP1P/RNBQKB1R_w_KQkq_-_1_5#explorer) — updated 2026-08-26*
<!-- lichess-stats:end -->

**5. Bg2** is close to automatic (99.8% masters), completing the fianchetto on the other side. Black's own reply is a genuine three-way split:

* **5... Be7** (68.9% masters): live-confirmed its own code, **E17** — [covered on its own card](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E17_Queens_Indian_Traditional.md).
* **5... Bb4+** (21.2% masters): live-confirmed its own code, **E16** — [covered on its own card](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E16_Queens_Indian_Capablanca.md).
* [**5... c5**](#_c5_) (5.5% masters): strikes at the centre instead, staying **E15** — covered below.

[*Back to TOP*](#_TOP_)

---

<a name="_c5_"></a>

## 5... c5 6. d5 exd5

[![6...exd5](https://backscattering.de/web-boardimage/board.svg?fen=rn1qkb1r/pb1p1ppp/1p3n2/2pp4/2P5/5NP1/PP2PPBP/RNBQK2R&lastMove=e6d5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rn1qkb1r/pb1p1ppp/1p3n2/2pp4/2P5/5NP1/PP2PPBP/RNBQK2R_w_KQkq_-_0_7)

*... 6... exd5*

```
rn1qkb1r/pb1p1ppp/1p3n2/2pp4/2P5/5NP1/PP2PPBP/RNBQK2R w KQkq - 0 7
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.3 |
| --- | --- |

White's own 7th move forks into two named lines:

* [**7. Nh4**](#_Nh4_) (+0.5, mention-only): the *Rubinstein Variation* — covered below.
* [**7. Ng5**](#_Ng5_) (+0.4, mention-only): the *Buerger Variation* — covered below.

[*Back to 4... Bb7*](#_Bb7_)
[*Back to TOP*](#_TOP_)

---

<a name="_Nh4_"></a>

### 7. Nh4 — Rubinstein Variation

[![7. Nh4](https://backscattering.de/web-boardimage/board.svg?fen=rn1qkb1r/pb1p1ppp/1p3n2/2pp4/2P4N/6P1/PP2PPBP/RNBQK2R&lastMove=f3h4&coordinates=true&size=280)](https://lichess.org/analysis/standard/rn1qkb1r/pb1p1ppp/1p3n2/2pp4/2P4N/6P1/PP2PPBP/RNBQK2R_b_KQkq_-_1_7)

*... 7. Nh4 — Rubinstein Variation*

```
rn1qkb1r/pb1p1ppp/1p3n2/2pp4/2P4N/6P1/PP2PPBP/RNBQK2R b KQkq - 1 7
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.5 |
| --- | --- |

Reroutes the knight toward f5, eyeing the weakened dark squares around Black's king rather than recapture the pawn immediately. **7... g6** is masters' clear main reply (76.0%), covering f5 pre-emptively. Not built out further here (backlog).

[*Back to 5... c5*](#_c5_)
[*Back to TOP*](#_TOP_)

---

<a name="_Ng5_"></a>

### 7. Ng5 — Buerger Variation

[![7. Ng5](https://backscattering.de/web-boardimage/board.svg?fen=rn1qkb1r/pb1p1ppp/1p3n2/2pp2N1/2P5/6P1/PP2PPBP/RNBQK2R&lastMove=f3g5&coordinates=true&size=280)](https://lichess.org/analysis/standard/rn1qkb1r/pb1p1ppp/1p3n2/2pp2N1/2P5/6P1/PP2PPBP/RNBQK2R_b_KQkq_-_1_7)

*... 7. Ng5 — Buerger Variation*

```
rn1qkb1r/pb1p1ppp/1p3n2/2pp2N1/2P5/6P1/PP2PPBP/RNBQK2R b KQkq - 1 7
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.4 |
| --- | --- |

A genuine database rarity (59 masters games) compared to the Rubinstein Variation. **7... h6** is masters' clear main reply (59.3%), immediately questioning the knight. Not built out further here (backlog).

[*Back to 5... c5*](#_c5_)
[*Back to TOP*](#_TOP_)

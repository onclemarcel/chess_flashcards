<a name="_TOP_"></a>

# B10 Caro-Kann Defense <br> 1. e4 c6 #

Like the French, Black prepares ... d5 before playing it — but from c6 instead of e6, keeping the light-squared bishop free to develop outside the pawn chain via ... Bf5 or ... Bg4 before the position closes around it. This is generally considered the main structural advantage the Caro-Kann holds over the French. In exchange, the c-pawn no longer supports a future ... c5 break, and Black's position can be slightly slower to develop active piece play.

**Corrected 2026-08-25**: this card used to be built around **2. d4**, but that specific move — and everything built past it, including the whole Advance Variation — is actually **B12**, not B10 (the same pattern first found on `D04_Colle_System.md`/`D05_Colle_System.md`) — split off into [`B12_Caro_Kann.md`](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B12_Caro_Kann.md). B10 itself stays the correct code for every *other* 2nd-move try below.

<a name="_initial_move_"></a>

[![1. e4 c6](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR&lastMove=c7c6&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR_w_KQkq_-_0_2)

*... 1. e4 c6 — Caro-Kann Defense*

```
rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.3 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="8" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| d4 | 61.6 M (49.4%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/46 | 86 k (80.5%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 32/44/24 |  |
| Nf3 | 29.0 M (23.3%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 46/5/49 | 5.3 k (4.9%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 35/39/26 |  |
| Nc3 | 14.0 M (11.3%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/5/47 | 7.8 k (7.3%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 32/41/27 |  |
| f4 | 4.4 M (3.6%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/4/49 | 116 (0.1%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 31/36/33 |  |
| d3 | 4.2 M (3.4%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/46 | 2.6 k (2.5%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 33/38/28 |  |
| Bc4 | 3.8 M (3.0%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 43/4/53 | 0 | — | ⚠ |
| c4 | 3.7 M (2.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/5/45 | 4.3 k (4.0%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 34/41/25 |  |
| e5 | 1.1 M (0.9%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/4/48 | 0 | — | ⚠ |
| Ne2 | 0 | — | 427 (0.4%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 40/35/25 |  |
| b3 | 0 | — | 68 (0.1%) | ⬜⬜⬜🟫🟫🟫⬛⬛⬛⬛ 29/28/43 |  |

*Online: bullet/blitz, 1800+ — 124.7 M games. Masters: 106 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR_w_KQkq_-_0_2#explorer) — updated 2026-09-02*
<!-- lichess-stats:end -->

### Candidate moves

* [**2. d4**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B12_Caro_Kann.md) (+0.3, 80.5% masters): masters' overwhelming preference — this is **B12**, not B10, covered on its own card.
* [**2. Nc3**](#_Nc3_) (+0.2, 7.3% masters): the line this card follows below — stays genuinely B10.
* **2. Nf3** (+0.2, 4.9% masters): delays d4 a move longer, most often transposing back into B12 lines once White does play d4.
* **2. c4** (+0.4, 4.0% masters): live-tagged the *Accelerated Panov Attack* (`eco.md` calls it the *Anti-Caro-Kann Defence*, and the further **2... d5** reply the *Anti-Anti-Caro-Kann Defence* — both real name divergences, the live tag stays the same "Accelerated Panov Attack" at both plies); eval +0.1/+0.2 respectively. Not built out further here (backlog).
* **2. d3** (+0.3, 2.5% masters): the *Breyer Variation* — `eco.md` separately calls this exact position the *Closed Variation*, a real name divergence.
* **2. Bc4** (mention-only): the *Hillbilly Attack* — see the note below.

[*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **2. Bc4!?**, the *Hillbilly Attack* (−0.3, mention-only), develops the bishop immediately toward f7 — a genuine online-only curiosity (0 masters games out of 106k in this fork's own sample) rather than a real try at any serious level.
>
> [*Back to TOP*](#_TOP_)

---

<a name="_Nc3_"></a>

## 2. Nc3

[![2. Nc3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp1ppppp/2p5/8/4P3/2N5/PPPP1PPP/R1BQKBNR&lastMove=b1c3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp1ppppp/2p5/8/4P3/2N5/PPPP1PPP/R1BQKBNR_b_KQkq_-_1_2)

*... 2. Nc3*

```
rnbqkbnr/pp1ppppp/2p5/8/4P3/2N5/PPPP1PPP/R1BQKBNR b KQkq - 1 2
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/pp1ppppp/2p5/8/4P3/2N5/PPPP1PPP/R1BQKBNR b KQkq - 1 2" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| d5 | 13.0 M (88.9%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/5/47 | 7.6 k (97.6%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 31/41/27 |  |
| d6 | 898 k (6.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 50/4/47 | 23 (0.3%) | ⬜⬜⬜⬜⬜⬜🟫🟫⬛⬛ 57/17/26 |  |
| e6 | 250 k (1.7%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 52/4/44 | 0 | — | ⚠ |
| g6 | 178 k (1.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 50/4/46 | 138 (1.8%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 36/36/28 |  |
| e5 | 0 | — | 14 (0.2%) | — |  |

*Online: bullet/blitz, 1800+ — 14.6 M games. Masters: 7.8 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pp1ppppp/2p5/8/4P3/2N5/PPPP1PPP/R1BQKBNR_b_KQkq_-_1_2#explorer) — updated 2026-09-02*
<!-- lichess-stats:end -->

**2... d5** is essentially automatic (97.6% masters), reaching the *Two Knights Attack* family once White follows up with 3. Nf3 — usually transposing back toward the same structures as 2. d4, just with the king's knight developed a move earlier and White's own d-pawn not yet committed.

* [**3. Nf3**](#_Nf3_) (+0.2, 80.6% masters): the *Two Knights Attack* — masters' overwhelming choice — covered below.
* **3. d4** (mention-only, 9.3% masters): transposes straight into `B12_Caro_Kann.md`'s own tree — not duplicated here.
* **3. Qf3** (0.0, mention-only, 4.5% masters): the *Goldman Variation* — an offbeat try, developing the queen early to eye f7/b7.

[*Back to 1. e4 c6*](#_initial_move_)
[*Back to TOP*](#_TOP_)

---

<a name="_Nf3_"></a>

## 3. Nf3 — Two Knights Attack

[![3. Nf3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp2pppp/2p5/3p4/4P3/2N2N2/PPPP1PPP/R1BQKB1R&lastMove=g1f3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp2pppp/2p5/3p4/4P3/2N2N2/PPPP1PPP/R1BQKB1R_b_KQkq_-_1_3)

*... 3. Nf3 — Two Knights Attack*

```
rnbqkbnr/pp2pppp/2p5/3p4/4P3/2N2N2/PPPP1PPP/R1BQKB1R b KQkq - 1 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/pp2pppp/2p5/3p4/4P3/2N2N2/PPPP1PPP/R1BQKB1R b KQkq - 1 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="5" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| dxe4 | 5.2 M (57.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/5/44 | 2.6 k (28.6%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 34/42/24 |  |
| Bg4 | 1.8 M (19.5%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 46/5/49 | 5.2 k (56.6%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 30/42/28 |  |
| d4 | 924 k (10.3%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 54/4/43 | 0 | — | ⚠ |
| Nf6 | 557 k (6.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/4/48 | 760 (8.3%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 37/33/30 |  |
| e6 | 324 k (3.6%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 51/4/45 | 0 | — | ⚠ |
| g6 | 0 | — | 332 (3.6%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 35/37/28 |  |
| a6 | 0 | — | 194 (2.1%) | ⬜⬜⬜🟫🟫🟫⬛⬛⬛⬛ 32/32/36 |  |

*Online: bullet/blitz, 1800+ — 9.0 M games. Masters: 9.1 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pp2pppp/2p5/3p4/4P3/2N2N2/PPPP1PPP/R1BQKB1R_b_KQkq_-_1_3#explorer) — updated 2026-09-02*
<!-- lichess-stats:end -->

* [**3... Bg4**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B11_Caro_Kann_Two_Knights_Mindeno.md) (+0.2, 56.6% masters): the *Mindeno Variation* — masters' clear main try. Live-confirmed its own code, **B11** — covered on its own card.
* **3... dxe4** (mention-only, 28.6% masters): trades off the tension immediately, transposing toward similar structures to the Classical/Modern Variation reached via 3. Nc3. Not built out further here (backlog).

[*Back to 2. Nc3*](#_Nc3_)
[*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **3. Qf3!?**, the *Goldman Variation* (0.0, mention-only), develops the queen early to eye f7/b7 rather than the knight — a genuine, if offbeat, database try (4.5% masters).
>
> [*Back to 2. Nc3*](#_Nc3_)
> [*Back to TOP*](#_TOP_)

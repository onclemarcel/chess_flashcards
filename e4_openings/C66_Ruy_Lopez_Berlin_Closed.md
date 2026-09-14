<a name="_TOP_"></a>

# C66 Ruy Lopez: Berlin Defense, Improved Steinitz Defense <br> 1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O d6 #

Spun off from [C65's own "4. O-O" candidate note](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C65_Ruy_Lopez_Berlin_Defense.md#_initial_move_) — already live-tagged its own code. `eco.md` gives no independent name to this exact bare tabiya; the live explorer tags it the ***Improved Steinitz Defense*** — the extra tempo from castling first (compared with the plain Steinitz Defense at C62) is the whole point of the name.

<a name="_initial_move_"></a>

[![4... d6](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/ppp2ppp/2np1n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQ1RK1&lastMove=d7d6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/ppp2ppp/2np1n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQ1RK1_w_kq_-_0_5)

*... 4... d6 — Improved Steinitz Defense*

```
r1bqkb1r/ppp2ppp/2np1n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQ1RK1 w kq - 0 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.61 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkb1r/ppp2ppp/2np1n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQ1RK1 w kq - 0 5" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Re1 | 427 k (39.5%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 54/5/41 | 91 (21.3%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 42/37/21 |  |
| d4 | 280 k (25.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 54/6/40 | 302 (70.7%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 35/49/16 |  |
| c3 | 116 k (10.7%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 54/4/42 | 0 | — | ⚠ |
| d3 | 103 k (9.6%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 0 | — | ⚠ |
| Nc3 | 0 | — | 10 (2.3%) | — |  |
| Bxc6+ | 0 | — | 8 (1.9%) | — |  |

*Online: bullet/blitz, 1800+ — 1.1 M games. Masters: 427 games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkb1r/ppp2ppp/2np1n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQ1RK1_w_kq_-_0_5#explorer) — updated 2026-09-14*
<!-- lichess-stats:end -->

**5. d4** is masters' clear main try (70.7%), striking the centre. **5... Bd7 6. Nc3**, and Black's own 6th move genuinely forks:

* [**6... Be7**](#_hedgehog_) (64.3% masters): masters' clear main try — the *Hedgehog Variation* — covered below.
* [**6... exd4**](#_Wolf_) (33.9% masters): the *Wolf Variation* — covered below.

**5. d4 Nd7!?**, the *Chigorin Variation*, is a genuine database rarity (only 2 masters games), rerouting the knight instead of developing the bishop; not built out further here (backlog).

[*Back to TOP*](#_TOP_)

---

<a name="_hedgehog_"></a>

### 6... Be7 — Hedgehog Variation

[![6... Be7](https://backscattering.de/web-boardimage/board.svg?fen=r2qk2r/pppbbppp/2np1n2/1B2p3/3PP3/2N2N2/PPP2PPP/R1BQ1RK1&lastMove=f8e7&coordinates=true&size=320)](https://lichess.org/analysis/standard/r2qk2r/pppbbppp/2np1n2/1B2p3/3PP3/2N2N2/PPP2PPP/R1BQ1RK1_w_kq_-_3_7)

*... 6... Be7 — Hedgehog Variation*

```
r2qk2r/pppbbppp/2np1n2/1B2p3/3PP3/2N2N2/PPP2PPP/R1BQ1RK1 w kq - 3 7
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.53 |
| --- | --- |

A solid, flexible setup — not the modern "Hedgehog System" reached from the Sicilian/English, just a repurposed name for this compact, cramped-looking Berlin structure. White's own 7th move genuinely forks:

* **7. Re1 O-O**, the *Tarrasch Trap*: **8. Bxc6!?** (91.7% masters) wins the bishop pair outright and, per the engine, a real, substantial edge (+1.40) — the trap being that the natural-looking 7...O-O actually drops material.
* [**7. Bg5**](#_Bernstein_) (a real, if secondary, try): the *Closed Bernstein Variation* — covered below.
* [**7. Bxc6**](#_Showalter66_) (22.7% masters): the *Closed Showalter Variation* — covered below.

[*Back to 4... d6*](#_initial_move_)
[*Back to TOP*](#_TOP_)

---

<a name="_Bernstein_"></a>

### 7. Bg5 — Closed Bernstein Variation

[![7. Bg5](https://backscattering.de/web-boardimage/board.svg?fen=r2qk2r/pppbbppp/2np1n2/1B2p1B1/3PP3/2N2N2/PPP2PPP/R2Q1RK1&lastMove=c1g5&coordinates=true&size=320)](https://lichess.org/analysis/standard/r2qk2r/pppbbppp/2np1n2/1B2p1B1/3PP3/2N2N2/PPP2PPP/R2Q1RK1_b_kq_-_4_7)

*... 7. Bg5 — Closed Bernstein Variation*

```
r2qk2r/pppbbppp/2np1n2/1B2p1B1/3PP3/2N2N2/PPP2PPP/R2Q1RK1 b kq - 4 7
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.29 |
| --- | --- |

Pins the f6-knight before resolving the centre — a genuine database rarity at this exact depth (only 7 masters games). Masters split between **7... exd4** (71.4%) and **7... h6** (28.6%). Not built out further here (backlog).

[*Back to 6... Be7*](#_hedgehog_)
[*Back to TOP*](#_TOP_)

---

<a name="_Showalter66_"></a>

### 7. Bxc6 — Closed Showalter Variation

[![7. Bxc6](https://backscattering.de/web-boardimage/board.svg?fen=r2qk2r/pppbbppp/2Bp1n2/4p3/3PP3/2N2N2/PPP2PPP/R1BQ1RK1&lastMove=b5c6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r2qk2r/pppbbppp/2Bp1n2/4p3/3PP3/2N2N2/PPP2PPP/R1BQ1RK1_b_kq_-_0_7)

*... 7. Bxc6 — Closed Showalter Variation*

```
r2qk2r/pppbbppp/2Bp1n2/4p3/3PP3/2N2N2/PPP2PPP/R1BQ1RK1 b kq - 0 7
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.51 |
| --- | --- |

Trades the bishop for the knight before Black can castle, matching the same structural idea as C62's own Nimzowitsch Attack one code earlier. Masters' forced recapture is **7... Bxc6** (100%). Not built out further here (backlog).

[*Back to 6... Be7*](#_hedgehog_)
[*Back to TOP*](#_TOP_)

---

<a name="_Wolf_"></a>

### 6... exd4 — Wolf Variation

[![6... exd4](https://backscattering.de/web-boardimage/board.svg?fen=r2qkb1r/pppb1ppp/2np1n2/1B6/3pP3/2N2N2/PPP2PPP/R1BQ1RK1&lastMove=e5d4&coordinates=true&size=320)](https://lichess.org/analysis/standard/r2qkb1r/pppb1ppp/2np1n2/1B6/3pP3/2N2N2/PPP2PPP/R1BQ1RK1_w_kq_-_0_7)

*... 6... exd4 — Wolf Variation*

```
r2qkb1r/pppb1ppp/2np1n2/1B6/3pP3/2N2N2/PPP2PPP/R1BQ1RK1 w kq - 0 7
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.59 |
| --- | --- |

Resolves the central tension immediately rather than developing the bishop first. Masters' near-unanimous reply is **7. Nxd4** (99.2%), recapturing at once. Not built out further here (backlog).

[*Back to 4... d6*](#_initial_move_)
[*Back to TOP*](#_TOP_)

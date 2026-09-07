<a name="_TOP_"></a>

# C67 Ruy Lopez: Berlin Defense, Rio Gambit Accepted <br> 1. e4 e5 2. Nf3 Nc6 3. Bb5 Nf6 4. O-O Nxe4 #

Spun off from [C65's own "4. O-O" candidate note](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C65_Ruy_Lopez_Berlin_Defense.md#_initial_move_) — masters' clear main try there (91.0%), already live-tagged its own code. `eco.md`'s own name for this bare tabiya is the *open Variation*; the live explorer tags it the ***Rio Gambit Accepted*** — the whole famous "Berlin Wall" endgame complex that shut down 1. e4 at the top level for a decade lives here.

<a name="_initial_move_"></a>

[![4... Nxe4](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/pppp1ppp/2n5/1B2p3/4n3/5N2/PPPP1PPP/RNBQ1RK1&lastMove=f6e4&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/pppp1ppp/2n5/1B2p3/4n3/5N2/PPPP1PPP/RNBQ1RK1_w_kq_-_0_5)

*... 4... Nxe4 — Rio Gambit Accepted*

```
r1bqkb1r/pppp1ppp/2n5/1B2p3/4n3/5N2/PPPP1PPP/RNBQ1RK1 w kq - 0 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.14 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkb1r/pppp1ppp/2n5/1B2p3/4n3/5N2/PPPP1PPP/RNBQ1RK1 w kq - 0 5" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Re1 | 558 k (52.1%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 46/7/46 | 5.7 k (34.0%) | ⬜🟫🟫🟫🟫🟫🟫🟫🟫⬛ 12/80/8 |  |
| d4 | 449 k (41.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 47/9/44 | 11 k (65.1%) | ⬜⬜🟫🟫🟫🟫🟫🟫🟫⬛ 19/67/14 |  |
| Bxc6 | 38 k (3.5%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 46/6/47 | 11 (0.1%) | — |  |
| Qe2 | 15 k (1.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 49/7/45 | 144 (0.9%) | ⬜⬜🟫🟫🟫🟫🟫🟫⬛⬛ 25/58/17 |  |

*Online: bullet/blitz, 1800+ — 1.1 M games. Masters: 17 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkb1r/pppp1ppp/2n5/1B2p3/4n3/5N2/PPPP1PPP/RNBQ1RK1_w_kq_-_0_5#explorer) — updated 2026-09-07*
<!-- lichess-stats:end -->

**5. d4** is masters' clear main try (65.1%); **5. Re1**, pinning the knight back to defend e4 indirectly, is a real, substantial secondary try (34.0%) but has no independent name in `eco.md` — not built out further here (backlog). After **5. d4 Nd6 6. Bxc6**, masters' overwhelming choice (90.4% at that fork), White trades the bishop for the knight before Black can consolidate, reaching the famous Berlin endgame tabiya after **6... dxc6 7. dxe5 Nf5 8. Qxd8+ Kxd8** — Black's king loses castling rights but the position is a genuinely holdable, near-symmetrical endgame, not a real practical problem for a well-prepared defender.

* [**5... Nd6**](#_lHermet_) (92.3% masters): masters' overwhelming choice — covered below.
* [**5... Be7**](#_Rio_) (5.4% masters): the *Rio de Janeiro Variation* — already independently named at this exact bare ply, not just at `eco.md`'s own deeper ending point — covered below.
* [**5... a6**](#_Rosenthal_) (a real, if secondary, try): the *Rosenthal Variation* — covered below.

[*Back to TOP*](#_TOP_)

---

<a name="_lHermet_"></a>

### 5... Nd6 — l'Hermet Variation

[![5... Nd6](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/pppp1ppp/2nn4/1B2p3/3P4/5N2/PPP2PPP/RNBQ1RK1&lastMove=e4d6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/pppp1ppp/2nn4/1B2p3/3P4/5N2/PPP2PPP/RNBQ1RK1_w_kq_-_1_6)

*... 5... Nd6 — l'Hermet Variation*

```
r1bqkb1r/pppp1ppp/2nn4/1B2p3/3P4/5N2/PPP2PPP/RNBQ1RK1 w kq - 1 6
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.16 |
| --- | --- |

Retreats the knight to defend the bishop-under-attack and keep an eye on the e4/f5 squares. White's own 6th move genuinely forks:

* [**6. Bxc6**](#_BerlinWall_) (90.4% masters): masters' overwhelming choice — leads to the Berlin Wall endgame tabiya — covered below.
* [**6. dxe5**](#_lHermetProper_) (7.1% masters): the *l'Hermet Variation* proper — covered below.
* **6. Ba4** (1.3% masters, a real database rarity): the *Showalter Variation* — covered below.

[*Back to 4... Nxe4*](#_initial_move_)
[*Back to TOP*](#_TOP_)

---

<a name="_BerlinWall_"></a>

### 6. Bxc6 — the Berlin Wall

[![6. Bxc6](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/pppp1ppp/2Bn4/4p3/3P4/5N2/PPP2PPP/RNBQ1RK1&lastMove=b5c6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/pppp1ppp/2Bn4/4p3/3P4/5N2/PPP2PPP/RNBQ1RK1_b_kq_-_0_6)

*... 6. Bxc6 dxc6 7. dxe5 Nf5 8. Qxd8+ Kxd8 — the Berlin Wall*

```
r1bqkb1r/pppp1ppp/2Bn4/4p3/3P4/5N2/PPP2PPP/RNBQ1RK1 b kq - 0 6
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.14 |
| --- | --- |

The move that gives this whole complex its nickname: **6... dxc6 7. dxe5 Nf5 8. Qxd8+ Kxd8** trades queens early and leaves Black's king stuck in the centre, unable to castle — but the resulting structure (bishop pair for White, a healthy extra pawn-island for Black, and a genuinely balanced endgame) has proven extremely resilient in practice, famously used by Kramnik to neutralise Kasparov's 1. e4 in their 2000 world championship match and by countless top players since. Not built out further here (backlog) — the deep endgame theory from here is its own vast body of work.

[*Back to 5... Nd6*](#_lHermet_)
[*Back to TOP*](#_TOP_)

---

<a name="_lHermetProper_"></a>

### 6. dxe5 — l'Hermet Variation proper

[![6. dxe5](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/pppp1ppp/2nn4/1B2P3/8/5N2/PPP2PPP/RNBQ1RK1&lastMove=d4e5&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/pppp1ppp/2nn4/1B2P3/8/5N2/PPP2PPP/RNBQ1RK1_b_kq_-_0_6)

*... 6. dxe5 — l'Hermet Variation*

```
r1bqkb1r/pppp1ppp/2nn4/1B2P3/8/5N2/PPP2PPP/RNBQ1RK1 b kq - 0 6
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.00 |
| --- | --- |

Recaptures the pawn immediately rather than trading the bishop first — a real, if secondary, try (7.1% at the parent fork). Masters' near-forced reply is **6... Nxb5** (99.9%), recapturing the bishop before anything else. Not built out further here (backlog).

[*Back to 5... Nd6*](#_lHermet_)
[*Back to TOP*](#_TOP_)

---

<a name="_ShowalterOpen_"></a>

### 6. Ba4 — Showalter Variation

[![6. Ba4](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/pppp1ppp/2nn4/4p3/B2P4/5N2/PPP2PPP/RNBQ1RK1&lastMove=b5a4&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/pppp1ppp/2nn4/4p3/B2P4/5N2/PPP2PPP/RNBQ1RK1_b_kq_-_2_6)

*... 6. Ba4 — Showalter Variation*

```
r1bqkb1r/pppp1ppp/2nn4/4p3/B2P4/5N2/PPP2PPP/RNBQ1RK1 b kq - 2 6
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | −0.04 |
| --- | --- |

Retreats the bishop to keep it on the board rather than trading it off — a genuine database rarity (only 132 masters games out of the whole l'Hermet fork). Masters split between **6... e4** (63.6%, gaining a tempo on the knight) and **6... exd4** (34.1%, resolving the tension immediately). Not built out further here (backlog).

[*Back to 5... Nd6*](#_lHermet_)
[*Back to TOP*](#_TOP_)

---

<a name="_Rio_"></a>

### 5... Be7 — Rio de Janeiro Variation

[![5... Be7](https://backscattering.de/web-boardimage/board.svg?fen=r1bqk2r/ppppbppp/2n5/1B2p3/3Pn3/5N2/PPP2PPP/RNBQ1RK1&lastMove=f8e7&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqk2r/ppppbppp/2n5/1B2p3/3Pn3/5N2/PPP2PPP/RNBQ1RK1_w_kq_-_1_6)

*... 5... Be7 — Rio de Janeiro Variation*

```
r1bqk2r/ppppbppp/2n5/1B2p3/3Pn3/5N2/PPP2PPP/RNBQ1RK1 w kq - 1 6
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.35 |
| --- | --- |

Develops the bishop rather than retreating the knight — a real, substantial minority try (5.4% at the parent fork), and, worth noting explicitly, this bare tabiya is *already* live-tagged the *Rio de Janeiro Variation*, one full move earlier than `eco.md`'s own entry for the same name (which only attaches it after the long forcing sequence below). Masters' clear reply is **6. Qe2** (69.2%), pinning the e4-knight to the king in effect. Continuing **6... Nd6 7. Bxc6 bxc6 8. dxe5 Nb7**, White's own 9th move genuinely forks four ways, all real named lines:

* **9. Nc3** (43.1% masters): continuing **9... O-O 10. Re1 Nc5 11. Nd4 Ne6 12. Be3 Nxd4 13. Bxd4 c5!?** reaches the deepest and most heavily analysed named endpoint of this whole complex, engine-verified a real dead heat (+0.30) despite the long manoeuvring. Not built out further here (backlog).
* [**9. c4**](#_Zukertort67_) (13.6% masters): the *Zukertort Variation* — covered below.
* [**9. b3**](#_Pillsbury_) (8.5% masters): the *Pillsbury Variation* — covered below.
* [**9. Nd4**](#_Winawer_) (16.6% masters): the *Winawer Attack* — covered below.

**8... Nf5!?** instead of 8...Nb7, the *Cordel Variation* (+0.60), keeps the knight more actively placed; masters' clear reply is **9. Qe4** (69.1%), forking the knight and the a8-rook's own diagonal. Not built out further here (backlog).

[*Back to 4... Nxe4*](#_initial_move_)
[*Back to TOP*](#_TOP_)

---

<a name="_Zukertort67_"></a>

### 9. c4 — Zukertort Variation

[![9. c4](https://backscattering.de/web-boardimage/board.svg?fen=r1bqk2r/pnppbppp/2p5/4P3/2P5/5N2/PP2QPPP/RNB2RK1&lastMove=c2c4&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqk2r/pnppbppp/2p5/4P3/2P5/5N2/PP2QPPP/RNB2RK1_b_kq_c3_0_9)

*... 9. c4 — Zukertort Variation*

```
r1bqk2r/pnppbppp/2p5/4P3/2P5/5N2/PP2QPPP/RNB2RK1 b kq c3 0 9
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.29 |
| --- | --- |

Gains queenside space instead of developing the queenside knight — masters' near-unanimous reply is **9... O-O** (100%). Not built out further here (backlog).

[*Back to 5... Be7*](#_Rio_)
[*Back to TOP*](#_TOP_)

---

<a name="_Pillsbury_"></a>

### 9. b3 — Pillsbury Variation

[![9. b3](https://backscattering.de/web-boardimage/board.svg?fen=r1bqk2r/pnppbppp/2p5/4P3/8/1P3N2/P1P1QPPP/RNB2RK1&lastMove=b2b3&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqk2r/pnppbppp/2p5/4P3/8/1P3N2/P1P1QPPP/RNB2RK1_b_kq_-_0_9)

*... 9. b3 — Pillsbury Variation*

```
r1bqk2r/pnppbppp/2p5/4P3/8/1P3N2/P1P1QPPP/RNB2RK1 b kq - 0 9
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.53 |
| --- | --- |

Fianchetto-style development for the queen's own bishop rather than a direct central commitment — masters' near-unanimous reply is **9... O-O** (100%). Not built out further here (backlog).

[*Back to 5... Be7*](#_Rio_)
[*Back to TOP*](#_TOP_)

---

<a name="_Winawer_"></a>

### 9. Nd4 — Winawer Attack

[![9. Nd4](https://backscattering.de/web-boardimage/board.svg?fen=r1bqk2r/pnppbppp/2p5/4P3/3N4/8/PPP1QPPP/RNB2RK1&lastMove=f3d4&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqk2r/pnppbppp/2p5/4P3/3N4/8/PPP1QPPP/RNB2RK1_b_kq_-_2_9)

*... 9. Nd4 — Winawer Attack*

```
r1bqk2r/pnppbppp/2p5/4P3/3N4/8/PPP1QPPP/RNB2RK1 b kq - 2 9
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.30 |
| --- | --- |

Centralises the knight at once rather than developing another piece first — masters' near-unanimous reply is **9... O-O** (98.0%). Not built out further here (backlog).

[*Back to 5... Be7*](#_Rio_)
[*Back to TOP*](#_TOP_)

---

<a name="_Minckwitz_"></a>

### 6. dxe5 — Minckwitz Variation

[![6. dxe5](https://backscattering.de/web-boardimage/board.svg?fen=r1bqk2r/ppppbppp/2n5/1B2P3/4n3/5N2/PPP2PPP/RNBQ1RK1&lastMove=d4e5&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqk2r/ppppbppp/2n5/1B2P3/4n3/5N2/PPP2PPP/RNBQ1RK1_b_kq_-_0_6)

*... 6. dxe5 — Minckwitz Variation*

```
r1bqk2r/ppppbppp/2n5/1B2P3/4n3/5N2/PPP2PPP/RNBQ1RK1 b kq - 0 6
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.33 |
| --- | --- |

Recaptures the pawn immediately instead of pinning the knight with Qe2 first — a real alternative from the same 5...Be7 tabiya. Masters' clear reply is **6... O-O** (80.7%). Not built out further here (backlog).

[*Back to 5... Be7*](#_Rio_)
[*Back to TOP*](#_TOP_)

---

<a name="_Trifunovic_"></a>

### 6. Qe2 d5 — Trifunovic Variation

[![6... d5](https://backscattering.de/web-boardimage/board.svg?fen=r1bqk2r/ppp1bppp/2n5/1B1pp3/3Pn3/5N2/PPP1QPPP/RNB2RK1&lastMove=d7d5&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqk2r/ppp1bppp/2n5/1B1pp3/3Pn3/5N2/PPP1QPPP/RNB2RK1_w_kq_d6_0_7)

*... 6... d5 — Trifunovic Variation*

```
r1bqk2r/ppp1bppp/2n5/1B1pp3/3Pn3/5N2/PPP1QPPP/RNB2RK1 w kq d6 0 7
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +1.02 |
| --- | --- |

Holds the centre with a further pawn rather than retreating the knight — a genuine database rarity (only 17 masters games), and per the engine a real, substantial edge for White. Masters' clear reply is **7. Nxe5!?** (88.2%), grabbing the pawn back at once since the e4-knight is pinned to defend it. Not built out further here (backlog).

[*Back to 5... Be7*](#_Rio_)
[*Back to TOP*](#_TOP_)

---

<a name="_Rosenthal_"></a>

### 5... a6 — Rosenthal Variation

[![5... a6](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/1ppp1ppp/p1n5/1B2p3/3Pn3/5N2/PPP2PPP/RNBQ1RK1&lastMove=a7a6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/1ppp1ppp/p1n5/1B2p3/3Pn3/5N2/PPP2PPP/RNBQ1RK1_w_kq_-_0_6)

*... 5... a6 — Rosenthal Variation*

```
r1bqkb1r/1ppp1ppp/p1n5/1B2p3/3Pn3/5N2/PPP2PPP/RNBQ1RK1 w kq - 0 6
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.22 |
| --- | --- |

Asks the bishop the question immediately rather than retreating the knight first. Masters split between **6. Ba4** (60.8%, keeping the pin/pressure alive) and **6. Bxc6** (34.5%, trading at once). Not built out further here (backlog).

[*Back to 4... Nxe4*](#_initial_move_)
[*Back to TOP*](#_TOP_)

<a name="_TOP_"></a>

# E30 Nimzo-Indian Defense: Leningrad Variation <br> 1. d4 Nf6 2. c4 e6 3. Nc3 Bb4 4. Bg5 #

Spun off from [E20's own root fork](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E20_Nimzo_Indian.md): a real, well-tested try at White's 4th move — pins the knight immediately, mirroring the Nimzo-Indian's own idea back at Black. Live-confirmed its own code via the Lichess explorer's own `opening` field.

<a name="_initial_move_"></a>

[![4. Bg5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqk2r/pppp1ppp/4pn2/6B1/1bPP4/2N5/PP2PPPP/R2QKBNR&lastMove=c1g5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqk2r/pppp1ppp/4pn2/6B1/1bPP4/2N5/PP2PPPP/R2QKBNR_b_KQkq_-_3_4)

*... 4. Bg5 — Leningrad Variation*

```
rnbqk2r/pppp1ppp/4pn2/6B1/1bPP4/2N5/PP2PPPP/R2QKBNR b KQkq - 3 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqk2r/pppp1ppp/4pn2/6B1/1bPP4/2N5/PP2PPPP/R2QKBNR b KQkq - 3 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| h6 | 390 k (31.7%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/5/48 | 1.1 k (52.3%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 32/39/30 |  |
| c5 | 329 k (26.7%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 43/5/52 | 896 (42.8%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 25/43/32 |  |
| O-O | 175 k (14.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/46 | 0 | — | ⚠ |
| Bxc3+ | 135 k (11.0%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 45/4/50 | 0 | — | ⚠ |
| d5 | 0 | — | 43 (2.1%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 35/49/16 |  |
| b6 | 0 | — | 23 (1.1%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 26/48/26 |  |

*Online: bullet/blitz, 1800+ — 1.2 M games. Masters: 2.1 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqk2r/pppp1ppp/4pn2/6B1/1bPP4/2N5/PP2PPPP/R2QKBNR_b_KQkq_-_3_4#explorer) — updated 2026-08-26*
<!-- lichess-stats:end -->

**4... h6** is masters' narrow plurality (52.3%), questioning the bishop immediately; **4... c5** (42.8%) strikes at the centre instead. **5. Bh4 c5 6. d5** reaches the tabiya where Black's own 6th move splits into two real named branches.

* [**6... b5**](#_b5_) (mention-only): the *Averbakh Gambit* — covered below.
* **6... d6** (mention-only): live-confirmed its own code, **E31** — [covered on its own card](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E31_Nimzo_Indian_Leningrad_Benoni.md).

[*Back to TOP*](#_TOP_)

---

<a name="_b5_"></a>

## 6... b5 — Averbakh Gambit

[![6... b5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqk2r/p2p1pp1/4pn1p/1ppP4/1bP4B/2N5/PP2PPPP/R2QKBNR&lastMove=b7b5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqk2r/p2p1pp1/4pn1p/1ppP4/1bP4B/2N5/PP2PPPP/R2QKBNR_w_KQkq_b6_0_7)

*... 6... b5 — Averbakh Gambit*

```
rnbqk2r/p2p1pp1/4pn1p/1ppP4/1bP4B/2N5/PP2PPPP/R2QKBNR w KQkq b6 0 7
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
| --- | --- |

Offers a pawn to gain time on the centre and open lines for the light-squared bishop, live-tagged the *Averbakh Gambit* (`eco.md`'s own entry just describes it as the "...b5 Gambit"). **7. dxe6** is masters' clear main reply (45.2%), accepting the pawn back immediately rather than the sharper 7. cxb5. Not built out further here (backlog).

[*Back to TOP*](#_TOP_)

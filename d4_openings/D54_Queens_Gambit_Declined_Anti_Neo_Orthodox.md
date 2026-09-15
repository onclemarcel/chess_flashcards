<a name="_TOP_"></a>

# D54 Queen's Gambit Declined: Anti-neo-orthodox Variation <br> 1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 5. e3 O-O 6. Rc1 #

Spun off from [D53's own "5. e3 O-O" card](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D53_Queens_Gambit_Declined_Be7.md#_OO_) — a real, secondary try there (11.5% masters), already live-tagged its own code. A genuine, worth-noting naming collision: `eco.md` calls this entry the *Anti-neo-orthodox Variation*, with an explicit "Anti-" prefix, while the live explorer drops it entirely and calls it plain ***Neo-Orthodox Variation*** — the exact same name (minus "Anti-") that `eco.md` separately uses two codes later, at D55's own 6...h6 branch. The two names describe genuinely different ideas (this one is about White developing the rook before committing the bishop; D55's is about Black's own 6th move) but the live database doesn't distinguish them at all.

<a name="_initial_move_"></a>

[![6. Rc1](https://backscattering.de/web-boardimage/board.svg?fen=rnbq1rk1/ppp1bppp/4pn2/3p2B1/2PP4/2N1P3/PP3PPP/2RQKBNR&lastMove=a1c1&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbq1rk1/ppp1bppp/4pn2/3p2B1/2PP4/2N1P3/PP3PPP/2RQKBNR_b_K_-_2_6)

*... 6. Rc1 — live-tagged the Neo-Orthodox Variation*

```
rnbq1rk1/ppp1bppp/4pn2/3p2B1/2PP4/2N1P3/PP3PPP/2RQKBNR b K - 2 6
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.00 |
| --- | --- |

<!-- lichess-stats:start fen="rnbq1rk1/ppp1bppp/4pn2/3p2B1/2PP4/2N1P3/PP3PPP/2RQKBNR b K - 2 6" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| c6 | 7.6 k (24.0%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/6/43 | 29 (11.6%) | ⬜⬜⬜⬜🟫🟫🟫🟫🟫⬛ 41/45/14 |  |
| h6 | 6.5 k (20.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/6/42 | 106 (42.4%) | ⬜⬜⬜⬜🟫🟫🟫🟫🟫⬛ 37/49/14 |  |
| b6 | 5.2 k (16.5%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/6/43 | 16 (6.4%) | — |  |
| Nbd7 | 4.9 k (15.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/43 | 86 (34.4%) | ⬜⬜⬜⬜🟫🟫🟫🟫🟫⬛ 40/49/12 |  |

*Online: bullet/blitz, 1800+ — 31 k games. Masters: 250 games. [Open in the explorer](https://lichess.org/analysis/standard/rnbq1rk1/ppp1bppp/4pn2/3p2B1/2PP4/2N1P3/PP3PPP/2RQKBNR_b_K_-_2_6#explorer) — updated 2026-09-14*
<!-- lichess-stats:end -->

Develops the rook to its natural file before deciding how to meet ...h6 — the point being to keep the bishop's options (Bxf6 vs Bh4) open a move longer than the immediate 6. Nf3 does. Black's reply is a genuine multi-way spread rather than one clear main try: masters split **h6** (42.4%), **Nbd7** (34.4%), **c6** (11.6%), and **b6** (6.4%), with **a6**, **c5**, **Ne4**, and **dxc4** all real minor tries below 2%. None of these carry a code of their own here — `eco.md` gives this whole entry just this one node, with no further D54-coded forks. **6... h6** is masters' nominal plurality choice and likely converges with D55's own 6...h6 Neo-orthodox tree by a different move order (Rc1 played before h6 rather than after) — not independently verified here via `apply_san.py`, so stated as a likely convergence rather than a confirmed transposition. **6... Nbd7** heads toward the Orthodox Defence proper, D60 — a real `eco.md` code that simply hasn't been built in this repo yet (not "no code," just not-yet-covered).

* **6... h6** (42.4% masters): a real, secondary try, likely converging with D55's own Neo-orthodox tree by a different move order — not independently verified.
* **6... Nbd7** (34.4% masters): heads toward the Orthodox Defence complex, `eco.md` code D60 — not yet covered in this repo.
* **6... c6** (11.6% masters): a real, secondary try with no code of its own in this range.
* **6... b6** (6.4% masters): a real, secondary try with no code of its own in this range.

Not built out further here — a single fork-point node, per `eco.md`'s own one-entry treatment of this code.

[*Back to 5. e3 O-O*](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D53_Queens_Gambit_Declined_Be7.md#_OO_)
[*Back to TOP*](#_TOP_)

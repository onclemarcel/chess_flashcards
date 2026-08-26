<a name="_TOP_"></a>

# A44 Benoni Defense: Old Benoni <br> 1. d4 c5 2. d5 e5 #

Split off from [A43_Old_Benoni.md](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A43_Old_Benoni.md) on 2026-08-25, after a stage-2 pass of this repo's own Phase D ECO audit found a real code mismatch: **2... e5** is the move that actually gives the "Old Benoni" line its name, but it's live-tagged **A44**, not A43 — while the untaken sibling **2... d6** turned out to be the position that's genuinely coded **A43 · Old Benoni** (now the main line on the A43 card instead). Both codes share the exact same "Old Benoni" name in Lichess's own data, which is what let the mismatch go unnoticed for so long — a subtler case than the D04/D05 split found in the same audit pass, where the names at least differed.

<a name="_initial_move_"></a>

[![2... e5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp1p1ppp/8/2pPp3/8/8/PPP1PPPP/RNBQKBNR&lastMove=e7e5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp1p1ppp/8/2pPp3/8/8/PPP1PPPP/RNBQKBNR_w_KQkq_e6_0_3)

*... 1. d4 c5 2. d5 e5 — locking the centre, the move the whole line is named for*

```
rnbqkbnr/pp1p1ppp/8/2pPp3/8/8/PPP1PPPP/RNBQKBNR w KQkq e6 0 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +1.3 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/pp1p1ppp/8/2pPp3/8/8/PPP1PPPP/RNBQKBNR w KQkq e6 0 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| c4 | 911 k (48.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/4/49 | 449 (19.2%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 40/29/31 |  |
| e4 | 419 k (22.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 50/5/46 | 1.7 k (71.0%) | ⬜⬜⬜⬜⬜🟫🟫🟫⬛⬛ 54/26/20 |  |
| dxe6 | 271 k (14.3%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 45/4/51 | 42 (1.8%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 40/36/24 |  |
| Nc3 | 250 k (13.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/5/42 | 173 (7.4%) | ⬜⬜⬜⬜⬜🟫🟫🟫⬛⬛ 50/27/23 |  |

*Online: bullet/blitz, 1800+ — 1.9 M games. Masters: 2.3 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pp1p1ppp/8/2pPp3/8/8/PPP1PPPP/RNBQKBNR_w_KQkq_e6_0_3#explorer) — updated 2026-08-26*
<!-- lichess-stats:end -->

> [!NOTE]
> **2... e5** is masters' plurality choice at the parent fork (35.0% of all replies to 2. d5) despite being objectively the *worst* of Black's realistic options per Stockfish (+1.3, a real 0.7-pawn swing worse than 2... Nf6/d6/g6 — see [A43_Old_Benoni.md](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A43_Old_Benoni.md) for those). A recurring pattern in this repository: the historically "classical" line and the engine's own preference don't always agree, even among masters.

**3. e4** is masters' clear main try (71.0%) — completing a broad pawn centre while Black's own centre is already fixed and the dark-squared bishop stays boxed in behind the e5 pawn for a long time.

[*Back to TOP*](#_TOP_)

---

<a name="_e4_"></a>

## 3. e4

[![3. e4](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp1p1ppp/8/2pPp3/4P3/8/PPP2PPP/RNBQKBNR&lastMove=e2e4&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp1p1ppp/8/2pPp3/4P3/8/PPP2PPP/RNBQKBNR_b_KQkq_e3_0_3)

*... 3. e4 — reaching the main Old Benoni tabiya*

```
rnbqkbnr/pp1p1ppp/8/2pPp3/4P3/8/PPP2PPP/RNBQKBNR b KQkq e3 0 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +1.4 |
| --- | --- |

From here Black typically continues **... d6**, the ***Semi-Benoni*** (+1.3, mention-only, live-confirmed still A44), and **... g6/... Nf6**, aiming for a King's-Indian-like setup with a permanently cramped position — playable at club level but rarely seen at the top today, which is exactly why the Modern Benoni (delaying ... e5, or avoiding it) superseded this line in serious practice. Deeper theory past this point is its own body of work, not covered further here.

[*Back to 2... e5*](#_initial_move_)
[*Back to TOP*](#_TOP_)

<a name="_TOP_"></a>

# D71 Neo-Grünfeld Defense <br> 1. d4 Nf6 2. c4 g6 3. g3 d5 #

Spun off from [A40's 1... Nf6 2. c4 g6 note](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A40_QPG.md#_Nf6_c4_g6_), which asserted White's 3. Nc3 share (80.0% masters) in prose without ever showing a real stats table for the alternatives — a genuine zero-coverage gap surfaced by a full A00-E99 ECO-code audit, covering all ten D70-D79 codes at once (none had a single mention anywhere in the repo before this card). Instead of committing the king's knight to c3 immediately, White fianchettoes first; if Black answers with the same central strike used against the classical Grünfeld (... d5), the resulting positions carry White's g3/Bg2 setup a move earlier than the classical Grünfeld's own Exchange Variation — hence "Neo."

**A naming precision worth stating up front, verified live rather than assumed**: the D70-D79 code range doesn't attach to *this* position — Lichess's own explorer still tags it under the generic King's Indian/Grünfeld umbrella (`E60`). The Neo-Grünfeld code only starts once the position below is reached (**D71 · Neo-Grünfeld Defense: Exchange Variation**), the same "the code can start a few plies after the practical branch point" pattern already documented for the Richter-Veresov Attack (`D01_Richter_Veresov_Attack.md`) — noted explicitly here instead of being left for a future audit to catch.

<a name="_initial_move_"></a>

[![3. g3 d5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/6P1/PP2PP1P/RNBQKBNR&lastMove=d7d5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/6P1/PP2PP1P/RNBQKBNR_w_KQkq_d6_0_4)

*... 1. d4 Nf6 2. c4 g6 3. g3 d5*

```
rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/6P1/PP2PP1P/RNBQKBNR w KQkq d6 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.1 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/6P1/PP2PP1P/RNBQKBNR w KQkq d6 0 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Bg2 | 58 k (60.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/6/45 | 44 (15.7%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 30/36/34 |  |
| cxd5 | 30 k (30.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/7/42 | 231 (82.5%) | ⬜⬜⬜⬜🟫🟫🟫🟫🟫⬛ 35/50/14 |  |
| Nf3 | 5.6 k (5.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 49/6/44 | 5 (1.8%) | — |  |
| Nc3 | 1.5 k (1.6%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/46 | 0 | — | ⚠ |

*Online: bullet/blitz, 1800+ — 96 k games. Masters: 280 games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/6P1/PP2PP1P/RNBQKBNR_w_KQkq_d6_0_4#explorer) — updated 2026-08-31*
<!-- lichess-stats:end -->

> [!NOTE]
> **3... d5** is a genuine minority pick after 3. g3 — only 2.1% of masters games, well behind **3... Bg7** (76.7%), which simply transposes into the generic King's Indian Fianchetto complex instead of Neo-Grünfeld theory. Real, but rare: worth knowing it exists rather than expecting to face it often. Sample sizes from here on are small (low hundreds of masters games) since this whole branch is a minority choice off an already-minority choice — read the percentages as directional, not precise.

**4. cxd5** is masters' clear main try (82.5%) — capturing immediately, before Black's bishop even reaches g7, rather than developing the bishop first. This is worth stating plainly since it's easy to assume the fianchetto comes first: **4. Bg2** (15.7%) is real but clearly secondary.

[*Back to TOP*](#_TOP_)

---

<a name="_cxd5_"></a>

## 4. cxd5 Nxd5 5. Bg2 Bg7 — Neo-Grünfeld Defense: Exchange Variation

**4... Nxd5** is masters' clear main try (88.8%) — recapturing with the knight to keep the position simple; **5. Bg2** (90.2%) completes the fianchetto, and **5... Bg7** (90.9%) matches it, reaching the same tabiya a delayed-Bg2 move order would transpose into. This exact position is where the D71 code genuinely begins.

[![5... Bg7](https://backscattering.de/web-boardimage/board.svg?fen=rnbqk2r/ppp1ppbp/6p1/3n4/3P4/6P1/PP2PPBP/RNBQK1NR&lastMove=f8g7&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqk2r/ppp1ppbp/6p1/3n4/3P4/6P1/PP2PPBP/RNBQK1NR_w_KQkq_-_2_6)

*... 4. cxd5 Nxd5 5. Bg2 Bg7 — Neo-Grünfeld Defense: Exchange Variation*

```
rnbqk2r/ppp1ppbp/6p1/3n4/3P4/6P1/PP2PPBP/RNBQK1NR w KQkq - 2 6
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.4 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqk2r/ppp1ppbp/6p1/3n4/3P4/6P1/PP2PPBP/RNBQK1NR w KQkq - 2 6" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| e4 | 22 k (40.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/6/44 | 1.2 k (49.9%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 37/46/17 |  |
| Nf3 | 20 k (35.6%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/7/40 | 1.2 k (47.5%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 26/56/18 |  |
| Nc3 | 12 k (20.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 48/7/45 | 63 (2.5%) | ⬜⬜🟫🟫🟫🟫🟫⬛⬛⬛ 22/44/33 |  |
| e3 | 1.2 k (2.1%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 45/6/48 | 1 (0.0%) | — | ⚠ |

*Online: bullet/blitz, 1800+ — 56 k games. Masters: 2.5 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqk2r/ppp1ppbp/6p1/3n4/3P4/6P1/PP2PPBP/RNBQK1NR_w_KQkq_-_2_6#explorer) — updated 2026-08-31*
<!-- lichess-stats:end -->

Masters split almost evenly between **6. e4** (49.9%, claiming the centre immediately, kicking the knight) and **6. Nf3** (47.5%, developing first and keeping the e-pawn flexible) — a genuine near-even fork with no dominant try. Not built out further here (backlog) — each branch is its own extensive body of theory, and this card's job was closing the zero-coverage gap, not exhausting the family.

[*Back to 3. g3 d5*](#_initial_move_)
[*Back to TOP*](#_TOP_)

<a name="_TOP_"></a>

# B10 Caro-Kann Defense <br> 1. e4 c6 #

Like the French, Black prepares ... d5 before playing it — but from c6 instead of e6, keeping the light-squared bishop free to develop outside the pawn chain via ... Bf5 or ... Bg4 before the position closes around it. This is generally considered the main structural advantage the Caro-Kann holds over the French. In exchange, the c-pawn no longer supports a future ... c5 break, and Black's position can be slightly slower to develop active piece play.

### Overview

*Quick map of every move covered on this card — see the [shape key](https://github.com/onclemarcel/chess_flashcards/blob/main/start.md#content-diagram-optional) in start.md. White's other three tries after 2... d5 (Nc3/exd5/Nd2) don't have their own card yet, so that fan-out is left off the map — see the candidate-move list below instead.*

<!-- content-diagram:start -->
```mermaid
flowchart LR
    classDef main stroke-width:3px;

    c6["1. e4 c6"]
    click c6 "#_initial_move_" "B10 · Caro-Kann Defense"

    c6 --> d4[["2. d4 !<br/>+0.3"]]:::main
    click d4 "#_d4_" "B10 · Caro-Kann Defense"

    d4 --> e5[["3. e5 !<br/>+0.3"]]:::main
    click e5 "#_e5_" "B12 · Caro-Kann Defense: Advance Variation"

    e5 --> Bf5[["3... Bf5 !<br/>+0.2"]]:::main
    click Bf5 "#_e5_" "B12 · Caro-Kann Defense: Advance Variation"
```
<!-- content-diagram:end -->

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

*Online: bullet/blitz, 1800+ — 124.7 M games. Masters: 106 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR_w_KQkq_-_0_2#explorer) — updated 2026-08-24*
<!-- lichess-stats:end -->

### Candidate moves

* [**2. d4**](#_d4_) (+0.3): occupies the centre and is masters' overwhelming preference (80.5%) — Black answers almost automatically with **2... d5**, completing the point of 1... c6.

[*Back to TOP*](#_TOP_)

---

<a name="_d4_"></a>

### 2. d4 d5

[![2. d4 d5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp2pppp/2p5/3p4/3PP3/8/PPP2PPP/RNBQKBNR&lastMove=d7d5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp2pppp/2p5/3p4/3PP3/8/PPP2PPP/RNBQKBNR_w_KQkq_d6_0_3)

*... 2. d4 d5 — masters play 2... d5 97.6% of the time*

```
rnbqkbnr/pp2pppp/2p5/3p4/3PP3/8/PPP2PPP/RNBQKBNR w KQkq d6 0 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/pp2pppp/2p5/3p4/3PP3/8/PPP2PPP/RNBQKBNR w KQkq d6 0 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="6" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| exd5 | 19.6 M (33.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/6/47 | 17 k (20.0%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 29/44/26 |  |
| e5 | 18.2 M (30.7%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/47 | 33 k (39.9%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 35/43/22 |  |
| Nc3 | 13.9 M (23.5%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/5/45 | 20 k (23.5%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 29/47/24 |  |
| Nd2 | 3.5 M (6.0%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/6/44 | 11 k (13.6%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 32/46/22 |  |
| f3 | 2.6 M (4.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/4/43 | 2.5 k (3.0%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 37/32/30 |  |
| Bd3 | 614 k (1.0%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/5/47 | 27 (0.0%) | ⬜⬜⬜⬜🟫🟫⬛⬛⬛⬛ 41/22/37 |  |

*Online: bullet/blitz, 1800+ — 59.2 M games. Masters: 84 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pp2pppp/2p5/3p4/3PP3/8/PPP2PPP/RNBQKBNR_w_KQkq_d6_0_3#explorer) — updated 2026-08-24*
<!-- lichess-stats:end -->

Unlike the French, masters' top choice here is to gain space rather than develop first.

* [**3. e5**](#_e5_) (+0.3, 39.9% masters): the *Advance Variation* — masters' main line, covered below.
* **3. Nc3** (+0.4, 23.5% masters): the *Classical* / *Modern* Variation, developing naturally and keeping the tension; often continues 3... dxe4 4. Nxe4.
* **3. exd5** (+0.2, 20.0% masters): the *Exchange Variation* — trades off the tension for a symmetrical structure, similar in spirit to the French Exchange but generally considered to give White somewhat better long-term chances here thanks to the open diagonal for the light-squared bishop.
* **3. Nd2** (+0.3, 13.6% masters): the *Tarrasch Variation*, avoiding ... dxe4 lines that trade off a piece for the knight and keeping options flexible.

[*Back to 1... c6*](#_initial_move_)
[*Back to TOP*](#_TOP_)

---

<a name="_e5_"></a>

## 3. e5 — Advance Variation

[![3. e5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/pp2pppp/2p5/3pP3/3P4/8/PPP2PPP/RNBQKBNR&lastMove=e4e5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/pp2pppp/2p5/3pP3/3P4/8/PPP2PPP/RNBQKBNR_b_KQkq_-_0_3)

*... 3. e5 — Advance Variation*

```
rnbqkbnr/pp2pppp/2p5/3pP3/3P4/8/PPP2PPP/RNBQKBNR b KQkq - 0 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.3 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkbnr/pp2pppp/2p5/3pP3/3P4/8/PPP2PPP/RNBQKBNR b KQkq - 0 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="3" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Bf5 | 12.2 M (66.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/46 | 26 k (77.6%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 34/43/23 |  |
| c5 | 4.3 M (23.6%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 46/5/49 | 7.0 k (21.0%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 34/45/21 |  |
| e6 | 1.2 M (6.3%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 51/4/46 | 0 | — | ⚠ |
| g6 | 0 | — | 216 (0.6%) | ⬜⬜⬜⬜⬜🟫🟫🟫⬛⬛ 49/26/25 |  |

*Online: bullet/blitz, 1800+ — 18.4 M games. Masters: 33 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkbnr/pp2pppp/2p5/3pP3/3P4/8/PPP2PPP/RNBQKBNR_b_KQkq_-_0_3#explorer) — updated 2026-08-24*
<!-- lichess-stats:end -->

**3... Bf5** (+0.2) is masters' clear main try (77.6%) — getting the light-squared bishop outside the pawn chain before ... e6 closes it in, the whole structural point of the Caro-Kann. From here White typically continues **4. Nf3**/**4. h4** (the sharper *Botvinnik-Carls* setup, gaining space on the kingside where Black's bishop just landed) and Black completes development with ... e6, ... Nd7 and ... c5, aiming to undermine White's space with a well-timed break. Deeper theory past this point is its own body of work, not covered further here.

[*Back to 2. d4 d5*](#_d4_)
[*Back to TOP*](#_TOP_)

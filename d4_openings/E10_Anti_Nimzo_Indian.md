<a name="_TOP_"></a>

# E10 Indian Defense: Anti-Nimzo-Indian <br> 1. d4 Nf6 2. c4 e6 3. Nf3 #

Spun off from [E20's own "2... e6" reply](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E20_Nimzo_QI_Fork.md): White sidesteps the Nimzo-Indian pin, at least for a move. Live-confirmed the bare position's own name via the Lichess explorer's own `opening` field — Lichess tags it *Anti-Nimzo-Indian*; `eco.md`'s own entry just calls it the generic "Queen's Pawn Game," a real name divergence.

<a name="_initial_move_"></a>

[![3. Nf3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/pppp1ppp/4pn2/8/2PP4/5N2/PP2PPPP/RNBQKB1R&lastMove=g1f3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/4pn2/8/2PP4/5N2/PP2PPPP/RNBQKB1R_b_KQkq_-_1_3)

*... 3. Nf3 — Anti-Nimzo-Indian*

```
rnbqkb1r/pppp1ppp/4pn2/8/2PP4/5N2/PP2PPPP/RNBQKB1R b KQkq - 1 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.1 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkb1r/pppp1ppp/4pn2/8/2PP4/5N2/PP2PPPP/RNBQKB1R b KQkq - 1 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="6" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| d5 | 4.8 M (42.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/6/44 | 58 k (38.5%) | ⬜⬜🟫🟫🟫🟫🟫🟫⬛⬛ 24/59/17 |  |
| b6 | 2.2 M (19.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 48/6/45 | 56 k (37.0%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 28/52/19 |  |
| Bb4+ | 2.2 M (19.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 49/6/45 | 23 k (15.4%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 34/44/21 |  |
| c5 | 1.2 M (11.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 49/5/45 | 12 k (7.8%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 37/35/28 |  |
| Be7 | 432 k (3.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/5/43 | 0 | — | ⚠ |
| d6 | 84 k (0.8%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 54/4/42 | 0 | — | ⚠ |
| a6 | 0 | — | 875 (0.6%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 31/38/31 |  |
| Nc6 | 0 | — | 557 (0.4%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 35/39/26 |  |

*Online: bullet/blitz, 1800+ — 11.1 M games. Masters: 151 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/pppp1ppp/4pn2/8/2PP4/5N2/PP2PPPP/RNBQKB1R_b_KQkq_-_1_3#explorer) — updated 2026-08-31*
<!-- lichess-stats:end -->

Black's own 3rd move is a genuine four-way split, none dominant:

* **3... d5** (38.5% masters): simply transposes into the [Queen's Gambit Declined](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D06_Queens_Gambit.md#_e6_) — not duplicated here.
* [**3... b6**](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E12_Queens_Indian.md) (37.0% masters): the *Queen's Indian Defense*. Live-confirmed its own code, **E12** — covered on its own card.
* [**3... Bb4+**](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E11_Bogo_Indian.md) (15.4% masters): the *Bogo-Indian Defense*. Live-confirmed its own code, **E11** — covered on its own card.
* [**3... c5**](#_c5_) (7.8% masters): heads toward the *Blumenfeld Countergambit* — stays **E10**, covered below.
* **3... a6** (0.6% masters): the *Dzindzi-Indian Defense* — see the note below.
* **3... Ne4** (mention-only): the *Döry Indian* — see the note below.

[*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **3... a6!?**, live-tagged the *Dzindzi-Indian Defense* (+0.3, mention-only — `eco.md`'s own spelling is "Dzindzikhashvili Defence"), delays every commitment to see how White continues — a genuine, if rare, database try (0.6% masters). **4. Nc3** is masters' clear main reply (71.1%).
>
> [*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **3... Ne4!?**, live-tagged the *Döry Indian* (+0.5, mention-only), grabs the e4 outpost immediately — a genuine database rarity (only 60 masters games). Not to be confused with the *other* Döry Defense in this repo, [`A46_Indian_Knights_Variation.md`](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A46_Indian_Knights_Variation.md) (1. d4 Nf6 2. Nf3 Ne4) — the same name reused at a genuinely different position, one move order apart (c4/e6 already played here).
>
> [*Back to TOP*](#_TOP_)

---

<a name="_c5_"></a>

## 3... c5 — toward the Blumenfeld Countergambit

Spun off from [E20's own 3. Nf3 bullet](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E20_Nimzo_QI_Fork.md#_e6_Nf3_), where **3... c5** sat in the stats table at a real 7.8% masters share with no candidate bullet at all — a genuine zero-coverage gap surfaced by a full A00-E99 ECO-code audit. After **4. d5** (masters' clear main try, 69.7%), rather than retreat or transpose toward a Benoni structure, Black offers a second pawn with **4... b5** — opening the long diagonal for the c8-bishop and lines on the queenside in exchange for material, the same spirit as the Benko Gambit but reached from a Queen's-Indian-flavoured move order instead.

<a name="_b5_"></a>

[![4... b5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/p2p1ppp/4pn2/1ppP4/2P5/5N2/PP2PPPP/RNBQKB1R&lastMove=b7b5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/p2p1ppp/4pn2/1ppP4/2P5/5N2/PP2PPPP/RNBQKB1R_w_KQkq_b6_0_5)

*... 1. d4 Nf6 2. c4 e6 3. Nf3 c5 4. d5 b5 — Blumenfeld Countergambit*

```
rnbqkb1r/p2p1ppp/4pn2/1ppP4/2P5/5N2/PP2PPPP/RNBQKB1R w KQkq b6 0 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.5 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkb1r/p2p1ppp/4pn2/1ppP4/2P5/5N2/PP2PPPP/RNBQKB1R w KQkq b6 0 5" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="5" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| dxe6 | 48 k (35.6%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 48/4/47 | 898 (39.8%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 44/28/28 |  |
| Bg5 | 21 k (15.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/6/41 | 1.1 k (50.2%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 38/35/27 |  |
| cxb5 | 21 k (15.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 46/5/49 | 0 | — | ⚠ |
| Nc3 | 12 k (9.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/4/49 | 0 | — | ⚠ |
| b3 | 9.8 k (7.2%) | ⬜⬜⬜⬜🟫⬛⬛⬛⬛⬛ 43/4/52 | 0 | — | ⚠ |
| e4 | 0 | — | 110 (4.9%) | ⬜⬜⬜⬜⬜🟫🟫🟫⬛⬛ 54/26/20 |  |
| Bf4 | 0 | — | 38 (1.7%) | ⬜⬜⬜⬜⬜🟫🟫🟫⬛⬛ 47/32/21 |  |
| a4 | 0 | — | 21 (0.9%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 29/38/33 |  |

*Online: bullet/blitz, 1800+ — 136 k games. Masters: 2.3 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/p2p1ppp/4pn2/1ppP4/2P5/5N2/PP2PPPP/RNBQKB1R_w_KQkq_b6_0_5#explorer) — updated 2026-08-31*
<!-- lichess-stats:end -->

### Candidate moves

* [**5. Bg5**](#_Bg5_) (+0.5, 50.2% masters): pins the knight before deciding how to meet the gambit — the line this card follows.
* [**5. dxe6**](#_dxe6_) (+0.5, 39.8% masters): accepts the second pawn outright — see below.

[*Back to TOP*](#_TOP_)

---

<a name="_Bg5_"></a>

## 5. Bg5 — Duz-Khotimirsky Variation

[![5. Bg5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/p2p1ppp/4pn2/1ppP2B1/2P5/5N2/PP2PPPP/RN1QKB1R&lastMove=c1g5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/p2p1ppp/4pn2/1ppP2B1/2P5/5N2/PP2PPPP/RN1QKB1R_b_KQkq_-_1_5)

*... 5. Bg5 — Duz-Khotimirsky Variation*

```
rnbqkb1r/p2p1ppp/4pn2/1ppP2B1/2P5/5N2/PP2PPPP/RN1QKB1R b KQkq - 1 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.4 |
| --- | --- |

<!-- lichess-stats:start fen="rnbqkb1r/p2p1ppp/4pn2/1ppP2B1/2P5/5N2/PP2PPPP/RN1QKB1R b KQkq - 1 5" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| bxc4 | 7.0 k (33.9%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 57/5/39 | 0 | — | ⚠ |
| exd5 | 5.0 k (24.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 49/7/44 | 578 (51.0%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 34/43/23 |  |
| h6 | 3.1 k (15.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/5/42 | 112 (9.9%) | ⬜⬜⬜⬜⬜🟫🟫⬛⬛⬛ 50/21/29 |  |
| Qa5+ | 2.5 k (11.9%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/6/42 | 230 (20.3%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 40/31/30 |  |
| b4 | 0 | — | 146 (12.9%) | ⬜⬜⬜🟫🟫🟫⬛⬛⬛⬛ 33/27/40 |  |

*Online: bullet/blitz, 1800+ — 21 k games. Masters: 1.1 k games. [Open in the explorer](https://lichess.org/analysis/standard/rnbqkb1r/p2p1ppp/4pn2/1ppP2B1/2P5/5N2/PP2PPPP/RN1QKB1R_b_KQkq_-_1_5#explorer) — updated 2026-08-31*
<!-- lichess-stats:end -->

Pins the f6-knight before either side resolves the central tension, keeping the option of dxe6 or cxb5 in reserve. Live-tagged the *Duz-Khotimirsky Variation* (`eco.md`'s own spelling: "Dus-Khotimirsky," a minor divergence). **5... exd5** is masters' clear main reply (51.0%).

> [!NOTE]
> **5... exd5 6. cxd5 h6!?**, the *Spielmann Variation* (+0.2, mention-only), questions the bishop immediately. **7. Bxf6** is masters' clear main reply (88.3%) — a real online/masters split, since online play prefers retreating with **7. Bh4** almost as often (42.8% online vs only 9.5% masters).

Deeper theory past this point is its own body of work, not covered further here.

[*Back to _c5_*](#_c5_)
[*Back to TOP*](#_TOP_)

---

> [!NOTE]
> **5. dxe6**, the *Blumenfeld Countergambit Accepted*, simply takes the pawn — Black's recapture is essentially forced.
>
> <a name="_dxe6_"></a>
>
> ### 5. dxe6 fxe6 — Blumenfeld Countergambit Accepted
>
> [![5. dxe6 fxe6](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/p2p2pp/4pn2/1pp5/2P5/5N2/PP2PPPP/RNBQKB1R&lastMove=f7e6&coordinates=true&size=280)](https://lichess.org/analysis/standard/rnbqkb1r/p2p2pp/4pn2/1pp5/2P5/5N2/PP2PPPP/RNBQKB1R_w_KQkq_-_0_6)
>
> *... 5. dxe6 fxe6 — Blumenfeld Countergambit Accepted*
>
> ```
> rnbqkb1r/p2p2pp/4pn2/1pp5/2P5/5N2/PP2PPPP/RNBQKB1R w KQkq - 0 6
> ```
>
> | ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.6 |
> | --- | --- |
>
> **5... fxe6** is essentially forced (100% masters) — recapturing toward the centre, giving up the right to castle kingside cleanly in exchange for a strong pawn duo on c5/e6 and open lines for both bishops. White is up a pawn but Black's real compensation is the same central control and piece activity the Benko Gambit offers, from a different move order. Deeper theory past this point is its own body of work, not covered further here.
>
> [*Back to _c5_*](#_c5_)
> [*Back to TOP*](#_TOP_)

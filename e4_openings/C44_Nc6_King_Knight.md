<a name="_TOP_"></a>

# C44 King's Knight Opening: Normal Variation <br> 1. e4 e5 2. Nf3 Nc6 #

Black develops a piece while defending e5 a second time, controlling both e5 and d4 at once. This is masters' overwhelming preference against 2. Nf3 (85.6% of games) and the gateway into most of the game's oldest and best-known openings — none of which continue on this page, since each is its own established body of theory.

**Merged 2026-09-06**: this code previously had two of its own deep branches split into separate files, `C44_Ponziani.md` and `C44_Scotch.md` — a genuine violation of this repo's own "one file per ECO code" rule (the same class of fix the C20 merge already made once), since both are genuinely C44 at their own root, not a different code. Folded back into this page as their own sections below.

### Overview

*Quick map of every move covered on this card — see the [shape key](https://github.com/onclemarcel/chess_flashcards/blob/main/start.md#content-diagram-optional) in start.md.*

<!-- content-diagram:start -->
```mermaid
flowchart LR
    classDef main stroke-width:3px;

    Nc6["1. e4 e5 2. Nf3 Nc6"]
    click Nc6 "#_initial_move_" "C44 · King's Knight Opening: Normal Variation"

    Nc6 --> Bb5[["3. Bb5 !<br/>+0.2"]]:::main
    click Bb5 "https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C60_Ruy_Lopez.md" "C60 · Ruy Lopez"
    Nc6 --> Bc4[["3. Bc4<br/>+0.1"]]
    click Bc4 "https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md" "C50 · Italian Game"
    Nc6 --> d4["3. d4<br/>+0.1"]
    click d4 "#_Scotch_" "C44 · Scotch Opening"
    Nc6 --> Nc3["3. Nc3<br/>+0.1"]
    click Nc3 "https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md" "C47 · Four Knights Game"
    Nc6 --> c3n["3. c3<br/>-0.1"]
    click c3n "#_Ponziani_" "C44 · Ponziani Opening"
```
<!-- content-diagram:end -->

<a name="_initial_move_"></a>

[![1. e4 e5 2. Nf3 Nc6](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R&lastMove=b8c6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R_w_KQkq_-_2_3)

*... 1. e4 e5 2. Nf3 Nc6 — King's Knight Opening: Normal Variation*

```
r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.2 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="8" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Bc4 | 48.1 M (39.6%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/4/46 | 48 k (19.3%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 30/47/23 |  |
| Bb5 | 33.5 M (27.6%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/5/45 | 162 k (65.0%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 29/53/18 |  |
| d4 | 24.6 M (20.2%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 22 k (8.9%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 30/46/25 |  |
| Nc3 | 9.4 M (7.7%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 14 k (5.7%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 27/48/24 |  |
| c3 | 3.7 M (3.0%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 50/4/46 | 1.6 k (0.6%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 32/38/30 |  |
| d3 | 1.0 M (0.9%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/5/49 | 234 (0.1%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 26/39/35 |  |
| Be2 | 365 k (0.3%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/5/48 | 278 (0.1%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 31/39/30 |  |
| g3 | 216 k (0.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 46/5/49 | 331 (0.1%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 39/39/23 |  |

*Online: bullet/blitz, 1800+ — 121.5 M games. Masters: 249 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkbnr/pppp1ppp/2n5/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R_w_KQkq_-_2_3#explorer) — updated 2026-09-09*
<!-- lichess-stats:end -->

### Candidate moves

None of White's main tries here is objectively much stronger than the others — Stockfish rates all four within a couple tenths of a pawn. The split is almost entirely a matter of style and how much of the resulting theory each side is willing to learn.

* [**3. Bb5**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C60_Ruy_Lopez.md) (+0.2): the [Ruy Lopez](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C60_Ruy_Lopez.md) (Spanish Opening) — masters' clear favourite (65.0% of masters games) and the most studied opening in chess history. Pins the knight defending e5 and prepares to add long-term pressure on the centre.
* [**3. Bc4**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md) (+0.1): the [Italian Game](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md), the most popular try online (39.6%) though second to the Ruy Lopez in masters play (19.3%). Develops actively toward f7 at once.
* [**3. d4**](#_Scotch_) (+0.1): the *Scotch Opening* — opens the centre immediately rather than building up slowly. Popular online (20.2%) but a clear third choice for masters (8.9%) — covered below.
* [**3. Nc3**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md) (+0.1): the [Four Knights Game](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md), developing symmetrically and keeping the position flexible; the least common of the four both online (7.7%) and in masters play (5.7%).
* [**3. c3**](#_Ponziani_) (-0.1, 0.6% masters): the *Ponziani Opening* — a genuine rarity today, preparing an immediate d4 — covered below.

Four further C44-coded tries sit in the stats table above with no candidate bullet, a genuine zero-coverage gap surfaced by a full A00-E99 ECO-code audit — none built out further here (backlog):

* **3. g3** (0.1% masters): live-tagged the *Konstantinopolsky Opening*, fianchettoing rather than committing the centre.
* **3. Be2** (0.1% masters): live-tagged the *Tayler Opening* already at this root ply — `eco.md`'s own umbrella name here is *Inverted Hungarian*, only narrowing to *Tayler Opening* one ply further after 3... Nf6 4. d4. After **3... Nf6 4. d3 d5 5. Nbd2**, the *Inverted Hanham* (−0.2), a real transposition-flavoured name from the Hanham complex reached a move early.
* **3. c4** (masters: negligible sample): the *Dresden Opening*.
* **3. Nxe5!? Nxe5 4. d4** (−2.2, a genuine database curiosity): live-tagged the *Schulze-Müller Gambit* — the same name `eco.md` gives the analogous piece sacrifice reached one move later from the Four Knights (C46), for a materially different but thematically identical idea. A real piece sacrifice, not a fork: Black simply retreats the attacked knight (**4... Nc6** or **4... Ng6**) and stays up a full piece for one pawn.

[*Back to TOP*](#_TOP_)

---

<a name="_Ponziani_"></a>

## 3. c3 — Ponziani Opening

Named after 18th-century Italian player Domenico Lorenzo Ponziani: rather than develop a bishop, White prepares an immediate **d4**, building a full pawn centre before Black's own knight development can pressure e4.

[![3. c3](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/pppp1ppp/2n5/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R&lastMove=c2c3&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/pppp1ppp/2n5/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R_b_KQkq_-_0_3)

*... 1. e4 e5 2. Nf3 Nc6 3. c3 — Ponziani Opening*

```
r1bqkbnr/pppp1ppp/2n5/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R b KQkq - 0 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | -0.1 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkbnr/pppp1ppp/2n5/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R b KQkq - 0 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="4" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Nf6 | 1.6 M (41.9%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/4/47 | 908 (57.6%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 33/39/29 |  |
| Bc5 | 899 k (23.4%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 52/4/44 | 0 | — | ⚠ |
| d5 | 531 k (13.8%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 45/5/51 | 505 (32.0%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 28/38/34 |  |
| d6 | 446 k (11.6%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/4/43 | 62 (3.9%) | ⬜⬜⬜⬜🟫🟫🟫🟫⬛⬛ 39/42/19 |  |
| f5 | 0 | — | 57 (3.6%) | ⬜⬜⬜⬜⬜🟫🟫⬛⬛⬛ 49/19/32 |  |

*Online: bullet/blitz, 1800+ — 3.8 M games. Masters: 1.6 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkbnr/pppp1ppp/2n5/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R_b_KQkq_-_0_3#explorer) — updated 2026-09-09*
<!-- lichess-stats:end -->

> [!NOTE]
> A real online/masters inversion: online, **3... Bc5** is the second most popular reply (23.4%) — but masters barely touch it, favouring **3... Nf6** (57.6%) and **3... d5** (32.0%) instead, both of which challenge e4 immediately rather than developing quietly.

### Candidate moves

* [**3... Nf6**](#_Ponziani_Nf6_) (0.0, 57.6% masters): the *Jaenisch Counterattack* — the line this card follows.
* [**3... d5**](#_Ponziani_d5_) (0.0, 32.0% masters): the *Ponziani Countergambit*'s quieter cousin — striking the centre from the other side, covered below.
* [**3... f5**](#_Ponziani_CounterGambit_) (3.6% masters): the *Ponziani Countergambit* proper — covered below.

Two further real, live-confirmed C44 tries sit below the root stats table's own display cutoff: **3... Nge7** (the *Reti Variation*) and **3... Be7** (the *Romanishin Variation*) — both masters' near-forced answer is **4. d4** (75.5%/94.4%), simply building the centre while Black's own last move did little to contest it. Neither built out further here (backlog).

[*Back to TOP*](#_TOP_)

---

<a name="_Ponziani_Nf6_"></a>

### 3... Nf6 — Ponziani Opening: Jaenisch Counterattack

[![3... Nf6](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R&lastMove=g8f6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R_w_KQkq_-_1_4)

*... 3... Nf6 — Ponziani Opening: Jaenisch Counterattack*

```
r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R w KQkq - 1 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R w KQkq - 1 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="3" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| d4 | 990 k (58.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/4/44 | 737 (81.1%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 31/39/29 |  |
| d3 | 319 k (18.8%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 46/4/50 | 158 (17.4%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 38/35/27 |  |
| Qc2 | 122 k (7.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 46/4/50 | 6 (0.7%) | — |  |

*Online: bullet/blitz, 1800+ — 1.7 M games. Masters: 909 games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/2P2N2/PP1P1PPP/RNBQKB1R_w_KQkq_-_1_4#explorer) — updated 2026-09-09*
<!-- lichess-stats:end -->

**4. d4** is masters' clear main try (81.1%) — the whole point of 3. c3, claiming the centre now that it's supported. Black typically continues **4... Nxe4**, grabbing the pawn back before White can consolidate; deeper theory past this point is its own body of work, not covered further here. One named deeper line: **4... Nxe4 5. d5 Bc5**, the *Fraser Defence* — the extra tempo White spent on d5 is roughly balanced by Black's active bishop (−0.4).

[*Back to 3. c3*](#_Ponziani_)
[*Back to TOP*](#_TOP_)

---

<a name="_Ponziani_d5_"></a>

### 3... d5

[![3... d5](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/ppp2ppp/2n5/3pp3/4P3/2P2N2/PP1P1PPP/RNBQKB1R&lastMove=d7d5&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/ppp2ppp/2n5/3pp3/4P3/2P2N2/PP1P1PPP/RNBQKB1R_w_KQkq_d6_0_4)

*... 3... d5*

```
r1bqkbnr/ppp2ppp/2n5/3pp3/4P3/2P2N2/PP1P1PPP/RNBQKB1R w KQkq d6 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

**4. Qa4** pins the c6-knight to defend e4 indirectly while eyeing a future Bb5 — masters' clear main try. Three named replies fork from here, none built out further (all backlog):

* **4... Bd7** (−0.1): the *Caro Variation* — unpins by blocking, the calmest choice.
* **4... Nf6** (0.0): the *Leonhardt Variation* — develops instead, ignoring the pin for now.
* **4... f6** (−0.1): the *Steinitz Variation* — shores up e5 directly.

[*Back to 3. c3*](#_Ponziani_)
[*Back to TOP*](#_TOP_)

---

<a name="_Ponziani_CounterGambit_"></a>

### 3... f5 — Ponziani Countergambit

[![3... f5](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/pppp2pp/2n5/4pp2/4P3/2P2N2/PP1P1PPP/RNBQKB1R&lastMove=f7f5&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/pppp2pp/2n5/4pp2/4P3/2P2N2/PP1P1PPP/RNBQKB1R_w_KQkq_f6_0_4)

*... 3... f5 — Ponziani Countergambit*

```
r1bqkbnr/pppp2pp/2n5/4pp2/4P3/2P2N2/PP1P1PPP/RNBQKB1R w KQkq f6 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.4 |
| --- | --- |

Masters' clear main try is **4. d4** (87.7%), building the centre while Black's last move did nothing to defend it. Deeper theory continues **4... d6 5. d5**, the *Schmidt Attack* (+0.5), gaining space rather than resolving the tension on f5/e5. From there, **5... fxe4 6. Ng5 Nb8 7. Nxe4 Nf6 8. Bd3 Be7**, the *Cordel Variation* (+1.1, a real engine swing toward White) — Black's knight retreat to b8 costs real time that White converts into a lasting edge. Neither built out further here beyond this backlog summary.

[*Back to 3. c3*](#_Ponziani_)
[*Back to TOP*](#_TOP_)

---

<a name="_Scotch_"></a>

## 3. d4 — Scotch Opening

White opens the centre immediately rather than developing a piece first, offering a pawn trade that leads to rapid piece activity. Named after a correspondence match between the Edinburgh and London chess clubs in 1824, it was a top-level rarity for most of the 20th century until Garry Kasparov revived it in the 1990s as a way to sidestep well-prepared Ruy Lopez defences.

### Overview

*Quick map of every move covered in this section — see the [shape key](https://github.com/onclemarcel/chess_flashcards/blob/main/start.md#content-diagram-optional) in start.md.*

<!-- content-diagram:start -->
```mermaid
flowchart LR
    classDef main stroke-width:3px;

    Scotchd4["3. d4"]
    click Scotchd4 "#_Scotch_" "C44 · Scotch Opening"

    Scotchd4 --> exd4[["3... exd4 !<br/>0.0"]]:::main
    click exd4 "#_exd4_" "C44 · Scotch Opening"

    exd4 --> Nxd4["4. Nxd4 !<br/>0.0"]:::main
    click Nxd4 "https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md" "C45 · Scotch Game"
    exd4 --> Bc4{"4. Bc4<br/>0.0"}
    click Bc4 "#_Bc4_" "C44 · Scotch Opening: Scotch Gambit"
```
<!-- content-diagram:end -->

[![1. e4 e5 2. Nf3 Nc6 3. d4](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R&lastMove=d2d4&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R_b_KQkq_d3_0_3)

*... 1. e4 e5 2. Nf3 Nc6 3. d4 — Scotch Opening*

```
r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq d3 0 3
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.1 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq d3 0 3" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="6" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| exd4 | 22.3 M (86.1%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/5/44 | 22 k (99.6%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 29/46/25 |  |
| d6 | 1.2 M (4.5%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 51/6/43 | 65 (0.3%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 35/35/29 |  |
| Nf6 | 1.0 M (3.9%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 52/4/44 | 11 (0.0%) | — |  |
| f5 | 286 k (1.1%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 47/3/50 | 0 | — | ⚠ |
| Nxd4 | 254 k (1.0%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/5/42 | 13 (0.1%) | — |  |
| Bc5 | 207 k (0.8%) | ⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛ 72/3/25 | 0 | — | ⚠ |
| d5 | 0 | — | 6 (0.0%) | — |  |
| Qf6 | 0 | — | 2 (0.0%) | — |  |

*Online: bullet/blitz, 1800+ — 26.0 M games. Masters: 22 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R_b_KQkq_d3_0_3#explorer) — updated 2026-09-09*
<!-- lichess-stats:end -->

### Candidate moves

Capturing is essentially forced at the top level — 99.6% of masters games — since ignoring the tension lets White simply keep an extra central pawn.

* [**3... exd4**](#_exd4_) (0.0): the only serious try.

**3... Nxd4** (0.1% masters), recapturing with the knight directly instead of the pawn, is the *Lolli Variation* — a real, if rare, named alternative. Masters mostly just retake with **4. Nxd4** (69.2% at that point), transposing back toward normal structures; the sharper **4. Nxe5** heads for the *Cochrane Variation* (**4... Ne6 5. Bc4 c6 6. O-O Nf6 7. Nxf7**, a piece sacrifice that levels out to a roughly balanced position, −0.02). Neither built out further here (backlog).

[*Back to TOP*](#_TOP_)

---

<a name="_exd4_"></a>

### 3... exd4

[![3... exd4](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/pppp1ppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R&lastMove=e5d4&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/pppp1ppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R_w_KQkq_-_0_4)

*... 3... exd4*

```
r1bqkbnr/pppp1ppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkbnr/pppp1ppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="6" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Nxd4 | 14.3 M (58.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 50/5/45 | 19 k (84.1%) | ⬜⬜⬜🟫🟫🟫🟫🟫⬛⬛ 30/46/23 |  |
| Bc4 | 7.3 M (29.7%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/4/43 | 2.8 k (12.5%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 25/43/31 |  |
| c3 | 2.3 M (9.3%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 54/4/42 | 736 (3.3%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 31/38/31 |  |
| Ng5 | 342 k (1.4%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 52/3/45 | 0 | — | ⚠ |
| Bb5 | 134 k (0.5%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 51/4/45 | 33 (0.1%) | ⬜⬜🟫🟫🟫🟫🟫⬛⬛⬛ 24/45/30 |  |
| Bd3 | 59 k (0.2%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 52/3/45 | 0 | — | ⚠ |

*Online: bullet/blitz, 1800+ — 24.5 M games. Masters: 23 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkbnr/pppp1ppp/2n5/8/3pP3/5N2/PPP2PPP/RNBQKB1R_w_KQkq_-_0_4#explorer) — updated 2026-09-09*
<!-- lichess-stats:end -->

* [**4. Nxd4**](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md) (0.0): the principled recapture, centralising the knight — masters' clear main line (84.1%), and its own card since it's already live-tagged **C45 · Scotch Game**, not C44.
* [**4. Bc4**](#_Bc4_) (0.0): the *Scotch Gambit* — develops with tempo instead of recapturing at once, offering the pawn back for a lead in development. Notably more popular online (29.7%) than in masters play (12.5%), where 4. Nxd4 is far more trusted.
* [**4. Bb5**](#_Relfsson_) (-0.1, 0.1% masters): the *Relfsson Gambit* (also known as "MacLopez"), a rarer bishop check instead.
* [**4. c3**](#_Goering_) (-0.1, 3.3% masters): the *Goering Gambit*, offering the pawn back immediately for rapid development.

[*Back to 3. d4*](#_Scotch_)
[*Back to TOP*](#_TOP_)

---

<a name="_Relfsson_"></a>

### 4. Bb5 — Relfsson Gambit ("MacLopez")

[![4. Bb5](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/pppp1ppp/2n5/1B6/3pP3/5N2/PPP2PPP/RNBQK2R&lastMove=f1b5&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/pppp1ppp/2n5/1B6/3pP3/5N2/PPP2PPP/RNBQK2R_b_KQkq_-_1_4)

*... 4. Bb5 — Relfsson Gambit*

```
r1bqkbnr/pppp1ppp/2n5/1B6/3pP3/5N2/PPP2PPP/RNBQK2R b KQkq - 1 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | -0.1 |
| --- | --- |

Checks first rather than recapturing, in a similar gambit spirit to 4. Bc4. Masters' main try is **4... a6** (57.6%), simply asking the question; online, **4... Bc5** is more common (34.4%). Not built out further here (backlog).

[*Back to 3... exd4*](#_exd4_)
[*Back to TOP*](#_TOP_)

---

<a name="_Goering_"></a>

### 4. c3 — Goering Gambit

[![4. c3](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/pppp1ppp/2n5/8/3pP3/2P2N2/PP3PPP/RNBQKB1R&lastMove=c2c3&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/pppp1ppp/2n5/8/3pP3/2P2N2/PP3PPP/RNBQKB1R_b_KQkq_-_0_4)

*... 4. c3 — Goering Gambit*

```
r1bqkbnr/pppp1ppp/2n5/8/3pP3/2P2N2/PP3PPP/RNBQKB1R b KQkq - 0 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | -0.1 |
| --- | --- |

Masters split between **4... d5** (42.7%, declining) and **4... dxc3** (33.6%, accepting a second pawn). After **4... dxc3 5. Nxc3**, White has a big lead in development for the two pawns, and two named lines follow:

* **5... d6 6. Bc4 Bg4 7. O-O Ne5 8. Nxe5 Bxd1 9. Bxf7+ Ke7 10. Nd5+** — the *Sea-cadet mate*: Black grabs the queen but walks into a forced mating attack (no cached engine eval this deep, but the pattern is a well-known named trap — not built out further here).
* **5... Bb4**, continuing **6. Bc4 Nf6**, the *Bardeleben Variation* (0.00) — a fully balanced main line instead of walking into the trap above.

[*Back to 3... exd4*](#_exd4_)
[*Back to TOP*](#_TOP_)

---

<a name="_Bc4_"></a>

### 4. Bc4 — Scotch Gambit

[![4. Bc4](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkbnr/pppp1ppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R&lastMove=f1c4&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkbnr/pppp1ppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R_b_KQkq_-_1_4)

*... 4. Bc4 — Scotch Gambit*

```
r1bqkbnr/pppp1ppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R b KQkq - 1 4
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

<!-- lichess-stats:start fen="r1bqkbnr/pppp1ppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R b KQkq - 1 4" db="lichess,masters" speeds="bullet,blitz" ratings="1800,2000,2200,2500" moves="5" -->
| Move | Online | W/D/B | Masters | W/D/B | |
| :--- | ---: | :--- | ---: | :--- | :-- |
| Nf6 | 2.6 M (34.9%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 49/5/46 | 1.9 k (67.5%) | ⬜⬜⬜🟫🟫🟫🟫⬛⬛⬛ 26/43/32 |  |
| Bc5 | 1.8 M (24.4%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 53/4/43 | 644 (22.7%) | ⬜⬜🟫🟫🟫🟫⬛⬛⬛⬛ 24/40/36 |  |
| d6 | 1.0 M (13.7%) | ⬜⬜⬜⬜⬜🟫⬛⬛⬛⬛ 52/5/43 | 88 (3.1%) | ⬜⬜⬜⬜🟫🟫🟫⬛⬛⬛ 40/32/28 |  |
| Be7 | 583 k (7.7%) | ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛ 55/4/41 | 44 (1.5%) | ⬜⬜⬜⬜⬜🟫🟫🟫⬛⬛ 52/32/16 |  |
| Bb4+ | 506 k (6.7%) | ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛ 53/3/44 | 130 (4.6%) | ⬜🟫🟫🟫🟫🟫🟫🟫🟫⬛ 7/78/15 |  |

*Online: bullet/blitz, 1800+ — 7.5 M games. Masters: 2.8 k games. [Open in the explorer](https://lichess.org/analysis/standard/r1bqkbnr/pppp1ppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R_b_KQkq_-_1_4#explorer) — updated 2026-09-09*
<!-- lichess-stats:end -->

Masters' clear main try is **4... Nf6** (67.5%), attacking e4 in return rather than accepting a second pawn — after **5. e5 d5** the gambit pawn usually comes back with interest for White's development. **4... Bc5** (22.7%) instead heads straight for Italian Game/Giuoco Piano-style structures a tempo down for Black. Either way, White develops actively and often follows up with **5. O-O** or **5. e5**, betting on faster piece activity to compensate for the pawn — very similar in spirit to the Danish Gambit reached from the Center Game.

* [**4... Bc5**](#_ScotchGambit_Bc5_) (22.7% masters): covered below.
* [**4... Bb4**](#_ScotchGambit_Bb4_) (4.6% masters): covered below.
* [**4... Be7**](#_Benima_) (1.5% masters): the *Benima Defense*.
* [**4... Nf6**](#_DuboisReti_) (67.5% masters): the *Dubois Réti Defense* — covered below.

[*Back to 3... exd4*](#_exd4_)
[*Back to TOP*](#_TOP_)

---

<a name="_ScotchGambit_Bc5_"></a>

### 4... Bc5

[![4... Bc5](https://backscattering.de/web-boardimage/board.svg?fen=r1bqk1nr/pppp1ppp/2n5/2b5/2BpP3/5N2/PPP2PPP/RNBQK2R&lastMove=f8c5&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqk1nr/pppp1ppp/2n5/2b5/2BpP3/5N2/PPP2PPP/RNBQK2R_w_KQkq_-_2_5)

*... 4... Bc5*

```
r1bqk1nr/pppp1ppp/2n5/2b5/2BpP3/5N2/PPP2PPP/RNBQK2R w KQkq - 2 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

Two main tries, both with real named theory:

* **5. O-O d6 6. c3 Bg4** (-0.2): the *Anderssen Counter-attack* — Black returns the pawn to finish development safely.
* [**5. Ng5**](#_Sarratt_) — live-tagged the *Sarratt Variation*, a sharper try, covered below.

[*Back to 4. Bc4*](#_Bc4_)
[*Back to TOP*](#_TOP_)

---

<a name="_Sarratt_"></a>

### 5. Ng5 — Sarratt Variation

[![5. Ng5](https://backscattering.de/web-boardimage/board.svg?fen=r1bqk1nr/pppp1ppp/2n5/2b3N1/2BpP3/8/PPP2PPP/RNBQK2R&lastMove=f3g5&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqk1nr/pppp1ppp/2n5/2b3N1/2BpP3/8/PPP2PPP/RNBQK2R_b_KQkq_-_3_5)

*... 5. Ng5 — Sarratt Variation*

```
r1bqk1nr/pppp1ppp/2n5/2b3N1/2BpP3/8/PPP2PPP/RNBQK2R b KQkq - 3 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

Masters' near-forced reply is **5... Nh6** (98.1%), covering f7 immediately. Two named White tries follow:

* **6. Nxf7 Nxf7 7. Bxf7+ Kxf7 8. Qh5+ g6 9. Qxc5 d5** (0.00): the *Cochrane-Shumov Defence* — White wins the exchange for a pawn, but Black's centre and development fully compensate.
* **6. Qh5** (-1.1, a real engine swing toward Black): the *Vitzhum Attack* — looks threatening but Stockfish already rates it as a clear error.

[*Back to 4... Bc5*](#_ScotchGambit_Bc5_)
[*Back to TOP*](#_TOP_)

---

<a name="_ScotchGambit_Bb4_"></a>

### 4... Bb4 — London Defense

[![4... Bb4](https://backscattering.de/web-boardimage/board.svg?fen=r1bqk1nr/pppp1ppp/2n5/8/1bBpP3/5N2/PPP2PPP/RNBQK2R&lastMove=f8b4&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqk1nr/pppp1ppp/2n5/8/1bBpP3/5N2/PPP2PPP/RNBQK2R_w_KQkq_-_2_5)

*... 4... Bb4 — London Defense*

```
r1bqk1nr/pppp1ppp/2n5/8/1bBpP3/5N2/PPP2PPP/RNBQK2R w KQkq - 2 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | -0.1 |
| --- | --- |

**Live-confirmed**: this position itself already carries a name, the *London Defense* — one ply earlier than `eco.md`'s own bare "Gambit" label. **5. c3** is masters' near-unanimous reply (97.7%), and after **5... dxc3**, two named branches follow:

* **6. O-O cxb2 7. Bxb2 Nf6 8. Ng5 O-O 9. e5 Nxe5** (0.00): the *Hanneken Variation* — Black grabs a second pawn and returns it right back for full equality.
* [**6. bxc3**](#_ScotchGambit_bxc3_) (-0.2): covered below.

[*Back to 4. Bc4*](#_Bc4_)
[*Back to TOP*](#_TOP_)

---

<a name="_ScotchGambit_bxc3_"></a>

### 6. bxc3

[![6. bxc3](https://backscattering.de/web-boardimage/board.svg?fen=r1bqk1nr/pppp1ppp/2n5/8/1bB1P3/2P2N2/P4PPP/RNBQK2R&lastMove=b2c3&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqk1nr/pppp1ppp/2n5/8/1bB1P3/2P2N2/P4PPP/RNBQK2R_b_KQkq_-_0_6)

*... 6. bxc3*

```
r1bqk1nr/pppp1ppp/2n5/8/1bB1P3/2P2N2/P4PPP/RNBQK2R b KQkq - 0 6
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | -0.2 |
| --- | --- |

**6... Ba5**, continuing **7. e5**, is the *Cochrane Variation* — a real engine swing toward Black (-0.8) despite the name's aggressive-sounding reputation. Not built out further here (backlog).

[*Back to 4... Bb4*](#_ScotchGambit_Bb4_)
[*Back to TOP*](#_TOP_)

---

<a name="_Benima_"></a>

### 4... Be7 — Benima Defense

[![4... Be7](https://backscattering.de/web-boardimage/board.svg?fen=r1bqk1nr/ppppbppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R&lastMove=f8e7&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqk1nr/ppppbppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R_w_KQkq_-_2_5)

*... 4... Be7 — Benima Defense*

```
r1bqk1nr/ppppbppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R w KQkq - 2 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | +0.4 |
| --- | --- |

A solid, unambitious way to decline further complications — masters split between **5. Nxd4** (51.8%), **5. c3** (35.7%), and **5. O-O** (12.6%). Not built out further here (backlog).

[*Back to 4. Bc4*](#_Bc4_)
[*Back to TOP*](#_TOP_)

---

<a name="_DuboisReti_"></a>

### 4... Nf6 — Dubois Réti Defense

[![4... Nf6](https://backscattering.de/web-boardimage/board.svg?fen=r1bqkb1r/pppp1ppp/2n2n2/8/2BpP3/5N2/PPP2PPP/RNBQK2R&lastMove=g8f6&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1bqkb1r/pppp1ppp/2n2n2/8/2BpP3/5N2/PPP2PPP/RNBQK2R_w_KQkq_-_2_5)

*... 4... Nf6 — Dubois Réti Defense*

```
r1bqkb1r/pppp1ppp/2n2n2/8/2BpP3/5N2/PPP2PPP/RNBQK2R w KQkq - 2 5
```

| ![Stockfish](https://github.com/onclemarcel/chess_flashcards/raw/main/pics/icon_stockfish.png) | 0.0 |
| --- | --- |

Masters' clear main try is **5. e5** (70.0%), pushing the attacked knight before it can consolidate; **5. O-O** (26.8%) is also common. This exact position is reached by transposition from the Two Knights Defense too (3... Nf6 4. d4 exd4) — the deeper theory from here (5. e5's *Keidansky Variation*, 5. O-O's own Nxe4/*Max Lange Attack* fork, 5. Ng5's *Perreux Variation*) is covered on that card's own child, [C56](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md), not duplicated here.

[*Back to 4. Bc4*](#_Bc4_)
[*Back to TOP*](#_TOP_)

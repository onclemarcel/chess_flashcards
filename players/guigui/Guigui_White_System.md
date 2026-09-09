# Guigui4378 — White Repertoire Scouting Report

<a name="_TOP_"></a>

This is **not** a theory card. It's a scouting profile of one specific opponent — **Guigui4378**, a chess.com regular the repo owner plays against often — built from his own game history rather than from any masters/online database. It follows this repo's usual visual conventions (board diagrams, FENs, live Stockfish evals, Lichess links) but deliberately **breaks from the standard card template** in how frequency is measured and presented: see "Methodology" immediately below before reading the tables. If you haven't read that section, the numbers in this file will look like the repo's usual masters/online stats tables — they are not.

The archive: 1887 games with Guigui4378 as White (`players/guigui/Guigui4378-white_2025.pgn`), all from 2025-2026. This file covers his **White repertoire only** — a Black-repertoire companion (`players/guigui/Guigui4378-black_2025.pgn`, 1886 games) is a separate, later task.

---

## Methodology

Two new tools, promoted to `tools/` for this task and exercised end-to-end for the first time here:

```
python tools/player_tree.py Guigui4378 players/guigui/Guigui4378-white_2025.pgn players/guigui/Guigui4378-black_2025.pgn \
    --max-plies 20 --dump-json players/guigui/guigui_tree.json

python tools/player_report.py players/guigui/guigui_tree.json white 16 0.15 2 20
python tools/player_report.py players/guigui/guigui_tree.json black 16 0.15 2 20
```

`player_tree.py` replays every game in the archive move-by-move (via `tools/fen.py`/`tools/apply_san.py`, the same replay primitives every other card in this repo already uses) and builds a frequency tree keyed by a **normalized FEN** (board + turn + castling + en-passant, with the halfmove/fullmove counters dropped). That normalization is the whole point: two different move orders that reach the *same position* collapse onto the *same tree node*, so the tool directly answers "does this player converge on the same position via different move orders" — which is exactly the "constantly transposing between A40/Dxx/Exx without knowing it" pattern the repo owner described going in. `player_report.py` then walks that tree and prints it as an indented report: at Guigui's own turns it shows every reply carrying at least `min_share` of that node's traffic (his real, repeatable choices); at his opponents' turns it shows the top `opp_top_k` replies regardless of share, so the tree doesn't explode while still showing what a reader would actually face.

Reproduced this session: **1887 White games, all 1887 matched by the PGN's own header, 1870 fully replayed to 20 plies** (17 games hit an unresolvable SAN token, almost certainly rare chess.com annotation quirks — noise at this sample size, not investigated further). 18,449 distinct normalized positions recorded on the White side.

**Why this file skips the repo's usual stats mechanics** (see `start.md` and `memory.md`'s sourcing rules for what's normally required):

- **No `<!-- lichess-stats:start/end -->` markers anywhere in this file.** Those markers are reserved for `tools/update_stats.py`, which pulls masters/online frequency from the *live Lichess API* — meaningless here (there's no "masters database" for one specific opponent) and could silently corrupt hand-authored content if the updater is ever run repo-wide without excluding this path. Every frequency table below is hand-authored from `player_tree.py`'s own JSON output and headed **"Guigui's own games (n=NNN)"** — never phrased in a way that could be mistaken for this repo's usual masters/online convention.
- **No Overview-mermaid shape classification** (rectangle/subroutine/rhombus/stadium/hexagon). That system's thresholds (masters ≥20% = subroutine, masters <2% & online ≥3% & 8x gap = rhombus trap, etc.) are calibrated for a masters-vs-online comparison that doesn't exist for a single player's practice. No mermaid diagram is used in this file at all — the branching is wide enough that plain prose + tables read more clearly than a flowchart would, and `tools/check_diagram.py` was not run against this file (it isn't built to understand a personal-frequency data model and would misfire on it). It **was** run repo-wide before finishing this task, to confirm nothing else broke.
- Every FEN below is still derived via `tools/apply_san.py` (never hand-typed), every board diagram still follows the exact backscattering.de/Lichess convention every other card uses, and every engine eval is still a live Stockfish query via the Lichess `cloud-eval` API — same discipline as everywhere else in this repo. Positive eval = good for White throughout, same convention as always.

[*Back to TOP*](#_TOP_)

---

<a name="_root_"></a>

## The headline pattern: 1. d4, then 2. e3 almost no matter what

Guigui's White repertoire is remarkably narrow for a 1880-game sample. He opens **1. d4 in 1880/1886 games (99.7%)** (4 games 1.e4, 1 each 1.d3/1.e3 — noise). Given that, here's how often his very next move is **e3**, broken out by Black's first reply:

**Guigui's own games (n=1879, all his White games after 1. d4)**

| Black's 1st move | share of his games | Guigui's reply | share of that reply being e3 |
| :--- | ---: | :--- | ---: |
| 1... d5 | 48.1% (904) | 2. e3 | **99.1%** (896/904) |
| 1... e6 | 11.3% (213) | 2. e3 | **95.3%** (203/213) |
| 1... e5 | 10.8% (203) | *(forced deviation — see below)* | 19.3% only |
| 1... Nf6 | 7.3% (138) | 2. e3 | **94.9%** (131/138) |
| 1... g6 | 5.5% (103) | 2. e3 | **99.0%** (102/103) |
| 1... c6 | 4.0% (75) | 2. e3 | **97.3%** (73/75) |
| 1... d6 | 3.1% (59) | 2. e3 | **98.3%** (58/59) |
| 1... b6 | 3.1% (59) | 2. e3 | **100.0%** (59/59) |
| 1... c5 | 2.9% (55) | *(forced deviation — see below)* | 20.0% only |
| 1... Nc6 | 1.4% (26) | 2. e3 | **100.0%** (26/26) |
| 1... f5 | 1.0% (19) | 2. e3 | **89.5%** (17/19) |

Everything else (a6, a5, h5, h6, b5, g5, f6 — under 0.5% each) gets e3 too, without exception in every sample large enough to matter. The only two Black replies that reliably knock him off e3 are the two that directly challenge d4 — **1... e5** and **1... c5** — and even there, e3 is still one of his three real tries (see below).

This is a genuine, personally-consistent "quiet universal e3 system," and it is **not a recognized named opening**. Live-checked this session via `tools/explore.py` against the actual masters database:

**Guigui's own games (n=895, replies to 2. e3 after 1. d4 d5)**

| Black's 2nd move | Guigui's games | share |
| :--- | ---: | ---: |
| 2... Nf6 | 216 | 24.1% |
| 2... Nc6 | 213 | 23.8% |
| 2... e6 | 159 | 17.8% |
| 2... Bf5 | 144 | 16.1% |
| 2... c5 | 44 | 4.9% |
| 2... c6 | 43 | 4.8% |
| (rest: a6/e5/g6/h6/b6/f5/Qd6/f6/…) | 36 | 4.0% |

### The system's own root

<a name="_system_root_"></a>

[![1.d4 d5 2.e3](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkbnr/ppp1pppp/8/3p4/3P4/4P3/PPP2PPP/RNBQKBNR&lastMove=e2e3&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkbnr/ppp1pppp/8/3p4/3P4/4P3/PPP2PPP/RNBQKBNR_b_KQkq_-_0_2)

```
rnbqkbnr/ppp1pppp/8/3p4/3P4/4P3/PPP2PPP/RNBQKBNR b KQkq - 0 2
```

Live-tagged **D00, "Queen's Pawn Game"** — a generic catch-all code, not a named system. Stockfish cloud-eval: **+0.03** (dead equal — this is a genuinely quiet try, not an inaccuracy). `d4_openings/D00_Queens_Pawn_Game.md` already exists and already carries a one-line "2. e3 (Stonewall Attack, mention-only, 0.2% masters)" note under its own `## 2. e3 Nf6 3. Bd3 — Stonewall Attack` section — **that is not the same thing as Guigui's system.** The Stonewall Attack commits to a specific follow-up (f4, Nd2, Ngf3, eventually Bd3 vs Nf6) that Guigui simply doesn't play: his e3 is never followed by an early f4, and Bd3 only shows up much later, situationally, after Black has already committed to a specific piece placement (see the Bb4-pin section below). His e3 is best described as **"delay the c-pawn and the light-squared bishop by one full move, see what Black actually commits to, then play c4."** A cross-reference note has been added to the D00 card pointing here (see "Cross-references" at the end of this file).

The genuinely uncharted part: his single most-repeated *deep* node, **1. d4 d5 2. e3 Nf6 3. c4** (214/216 games at that branch, 99.1%), comes back **`opening: None`** even in the masters database (masters sample n=53 — this really isn't book). Same for **1. d4 Nf6 2. e3** (`opening: None`, masters n=401). Multiple engine/explorer queries this session confirm this isn't a database gap — it's a real, personally-idiosyncratic move order that simply doesn't get played at any serious level.

### Direct proof of the transposition claim

This is the most important thing this tree makes visible, and it's the concrete evidence behind the repo owner's own framing ("constantly transposing between A40/Dxx/Exx without knowing it"). Two of Guigui's most common move orders — **2... Nf6** (24.1% of his 2.e3 games) and **2... Nc6** (23.8%) — independently reach the exact same position a few plies later:

```
d4 d5 e3 Nc6 c4 dxc4 Bxc4 Nf6   ->  r1bqkb1r/ppp1pppp/2n2n2/8/2BP4/4P3/PP3PPP/RNBQK1NR w KQkq - 1 5
d4 d5 e3 Nf6 c4 dxc4 Bxc4 Nc6   ->  r1bqkb1r/ppp1pppp/2n2n2/8/2BP4/4P3/PP3PPP/RNBQK1NR w KQkq - 1 5
```

Byte-for-byte identical normalized FEN, verified via `tools/apply_san.py` replay of both move sequences independently — not inferred, checked. Whichever order his opponent develops their knights in, Guigui's own tree funnels both branches into one node with **26/48 (54.2%) Nc3 and 22/48 (45.8%) Nf3** as his next move, and both sub-trees continue identically from there (same `Bb4`/`a3` pattern, same numbers, down to `18/32 Bb4 -> 15/21 a3`). He is playing one system; his opponents' move-order choices just rename the path to it.

[*Back to TOP*](#_TOP_)

---

<a name="_d5_branch_"></a>

## 1... d5 main branch (48.1% of his White games)

### 3. c4: the fork between contesting and conceding the center

After **2. e3**, Guigui plays **3. c4 in 99%+ of games** regardless of which minor piece Black developed first (214/216 after 2...Nf6, 211/213 after 2...Nc6). This is the real second commitment of the system — and unlike 2.e3, it's a normal, structurally sound try (transposing toward Queen's Gambit-family structures a tempo later than usual). Black's replies split into two structurally different plans:

**Guigui's own games (n=259, replies to 3. c4 after 2...Nf6)**

| Black's 3rd move | games | share |
| :--- | ---: | ---: |
| 3... e6 | 93 | 35.9% |
| 3... dxc4 | 65 | 25.1% |
| 3... c6 | 36 | 13.9% |
| 3... Nc6 | 22 | 8.5% |
| 3... Bf5 | 21 | 8.1% |
| 3... Bg4 | 8 | 3.1% |
| 3... c5 | 3 | 1.2% |

*(1...d5 2.e3 Bf5 also occurs on its own, 144 times / 16.1% of all 2.e3 replies — Guigui answers it 3. c4 100% of the time (144/144), never Bd3 challenging the bishop directly; eval +0.16, roughly balanced, `opening: None`, masters n=32. Not built out further here — no distinctive pattern beyond "he always meets it with c4 too.")*

<a name="_dxc4_recapture_"></a>

### The dxc4 / Bxc4 recapture pattern

[![3...dxc4 4.Bxc4](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/ppp1pppp/5n2/8/2BP4/4P3/PP3PPP/RNBQK1NR&lastMove=f1c4&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/ppp1pppp/5n2/8/2BP4/4P3/PP3PPP/RNBQK1NR_b_KQkq_-_0_4)

```
rnbqkb1r/ppp1pppp/5n2/8/2BP4/4P3/PP3PPP/RNBQK1NR b KQkq - 0 4
```

Guigui's own games (n=65 at this exact node): after 3... dxc4, he recaptures **4. Bxc4 in 100% of games (65/65)** — never `e4` grabbing the center back, never an intermezzo. Stockfish cloud-eval: **+0.23**, `opening: None` (masters n=2586). Recapturing with the bishop rather than contesting the center immediately is objectively fine here (this transposes toward a normal QGA-style structure, just reached a tempo late) — it isn't a mistake, just an unhurried move order.

Where it becomes a real, concrete edge for White is one specific continuation deeper. If Black then commits **both** minor pieces before challenging the bishop (e.g. `...Nc6 5.Nf3 e6 6.Nc3`), Guigui reaches a position with a genuine, engine-verified pull:

```
r1bqk2r/ppp2ppp/2n1pn2/8/1bBP4/2N1PN2/PP3PPP/R1BQK2R w KQkq - 2 7   (before 7...Bb4)
```
Stockfish cloud-eval: **+0.93**. Even after the natural-looking `7. a3` reply to the coming pin, White keeps **+0.86**. Compare that to the near-dead-equal (+0.00, see below) result when Black instead contests the center directly with `...e6` and `...exd5`. **The concrete takeaway for the side facing this system: recapturing `dxc4` and only later challenging the bishop concedes noticeably more than meeting `c4` with a direct central challenge does** — roughly a full pawn of engine evaluation, not a marginal stylistic difference.

<a name="_e6first_asymmetry_"></a>

### A real asymmetry: the e6-first move order keeps an extra option

Guigui reaches the *same* dxc4/Bxc4 idea via a second move order — 1...e6 first, then 2...d5 — and it transposes into the same continuation trees deeper (same Nc3/Nf3 numbers as the d5-first order, once both minor pieces are out). But **before** it converges, the e6-first order gives Black one option the d5-first order essentially doesn't:

**Guigui's own games — replies to 3. c4, by move order**

| Black's move order so far | 3rd move | share |
| :--- | :--- | ---: |
| `1...d5 2.e3 Nf6 3.c4` (n=259) | ...c5 | **1.2%** (3/259) |
| `1...e6 2.e3 d5 3.c4` (n=244) | ...c5 | **24.2%** (59/244) |

Once Black has already committed the knight to f6, ...c5 (a Tarrasch/Semi-Tarrasch-style central break) is essentially never played against Guigui's system in practice (3/259). But delaying that knight and playing ...e6 first keeps ...c5 alive as a real, frequently-chosen option — nearly a quarter of the time when facing him this way. Engine-wise the two central breaks aren't hugely different in isolation (`...c5` cloud-eval **+0.27** vs `...dxc4` **+0.25** at the analogous node), so this isn't "c5 refutes his move order" — it's a genuine **flexibility** asymmetry, not an evaluation one: the e6-first order keeps a structurally different try (central pawn break, contesting d4 directly) on the table that the Nf6-first order has effectively already forfeited. **Concrete recommendation**: against this system, delaying ...Nf6 in favor of ...e6 keeps more structural options open for longer.

<a name="_cxd5_exchange_"></a>

### The cxd5 exchange lines (both recaptures)

[![3...e6 4.cxd5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/ppp2ppp/4pn2/3P4/3P4/4P3/PP3PPP/RNBQKBNR&lastMove=c4d5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/ppp2ppp/4pn2/3P4/3P4/4P3/PP3PPP/RNBQKBNR_b_KQkq_-_0_4)

```
rnbqkb1r/ppp2ppp/4pn2/3P4/3P4/4P3/PP3PPP/RNBQKBNR b KQkq - 0 4
```

After 3...e6, Guigui plays **4. cxd5 in 95.1% of games (137/144)** — a real, near-automatic exchange rather than maintaining tension. Black's two recaptures give genuinely different structures, and the difference is worth knowing precisely:

| Recapture | Guigui's own games (of 146) | share | resulting position (White to move) | Stockfish cloud-eval |
| :--- | ---: | ---: | :--- | ---: |
| 4... exd5 | 63 | 43.2% | `rnbqkb1r/ppp2ppp/5n2/3p4/3P4/4P3/PP3PPP/RNBQKBNR w KQkq - 0 5` | **−0.19** |
| 4... Nxd5 | 58 | 39.7% | `rnbqkb1r/ppp2ppp/4p3/3n4/3P4/4P3/PP3PPP/RNBQKBNR w KQkq - 0 5` | **+0.25** |

[![4...exd5](https://backscattering.de/web-boardimage/board.svg?fen=rnbqkb1r/ppp2ppp/5n2/3p4/3P4/4P3/PP3PPP/RNBQKBNR&lastMove=e6d5&coordinates=true&size=320)](https://lichess.org/analysis/standard/rnbqkb1r/ppp2ppp/5n2/3p4/3P4/4P3/PP3PPP/RNBQKBNR_w_KQkq_-_0_5)

That's a genuine, engine-verified 0.44-pawn swing between the two recaptures, both from the *same* preceding position. `...exd5` produces a simple, symmetric-looking pawn-on-d5-vs-pawn-on-d4 structure with no early minority-attack setup from White (no Bg5, no early Nc3-then-b4 plan visible in his own practice) — practically fine, and per the engine very slightly *preferable* for Black. `...Nxd5` produces a Semi-Tarrasch-style structure with the knight centralized on d5 but White's d4 pawn now standing alone, comfortably supported — and the engine consistently prefers White there by a quarter of a pawn. **Concrete recommendation: recapture `...exd5`, not `...Nxd5`, against this specific system** — the instinct to recapture toward the center with a piece rather than a pawn is not the better choice here.

<a name="_bb4_pin_"></a>

### The Nc3-meets-Bb4 pin: a3 / Nf3 / Bd2

Wherever Guigui's e3-c4 system reaches `Nc3` with Black able to pin via `...Bb4`, three replies recur across his practice — and which one dominates depends on the exact structure, not on a fixed personal preference:

**Guigui's own games, by structure (all reached after ...Bb4 pins Nc3)**

| Structure | n | Nf3 | a3 | Bd2 | Bd3 |
| :--- | ---: | ---: | ---: | ---: | ---: |
| `exd5` structure, Bb4 pins immediately | 24 | 50.0% | 29.2% | 12.5% | 8.3% |
| `Nxd5` structure, Bb4 pins immediately | 19 | — | 5.3% | **84.2%** | — |
| `exd5` structure, after both knights out (`Nc3 Nc6 Nf3`) | 21 | — | 19.0% | 4.8% | **61.9%** |
| `dxc4/Bxc4` structure, both knights + e6 out | 32 | — | **71.4%** (of a 56.2% Bb4 subset) | — | — |

Live evals confirm this isn't arbitrary hedging — the choices cluster where the engine says they should. At the first `exd5` node (`rnbqk2r/ppp2ppp/5n2/3p4/1b1P4/2N1P3/PP3PPP/R1BQKBNR w KQkq - 2 6`), both his two real tries come back essentially dead equal: **Nf3 = 0.00**, **a3 = −0.01**. This is one of the places his instincts hold up honestly under engine check — no manufactured criticism here, both replies are simply fine. **Bd2** shows up specifically and heavily (84.2%) only in the `Nxd5` structure, where the knight already sits on d5 rather than needing Nf3 to develop toward it — a sensible, structure-driven choice, not noise.

[*Back to TOP*](#_TOP_)

---

<a name="_e5_deviation_"></a>

## 1... e5: the first forced deviation, and a real trap from the archive

**1. d4 e5** (10.8% of his games, 203 total) is live-tagged **A40, Englund Gambit** — and e3 genuinely doesn't fit here (it neither takes the free pawn nor contests the center), so Guigui's practice splits three ways:

**Guigui's own games (n=203)**

| Reply | games | share | live tag / eval |
| :--- | ---: | ---: | :--- |
| 2. dxe5 | 98 | 48.5% | takes the pawn — Stockfish **+1.07** |
| 2. d5 | 57 | 28.2% | A40 "Englund Gambit Declined" — Stockfish **+0.00** |
| 2. e3 | 39 | 19.3% | A40 "Englund Gambit Declined: Reversed French" — Stockfish **+0.14** |

His most common choice, `2. dxe5`, is also the engine's clear best (+1.07 vs +0.14 and +0.00) — good news for him on this one deviation: nearly half the time he takes the objectively correct path. The other two (47.5% combined) essentially hand back the entire first-move advantage.

### A real trap example from his own archive

After **2. dxe5**, his own practice (n=98) splits **Nc6 52.0% / Bc5 16.3% / d6 13.3% / f6 9.2% / Qe7 4.1%**, and at the critical `2...Nc6 3.Nf3 Qe7` tabiya (n=34) his 4th move splits **Qd5 44.1% / Nc3 26.5% / e3 20.6% / Bg5 5.9%**. `4. Qd5` — hitting Nc6 and keeping the extra pawn under real pressure — is both his most common try there and a genuinely strong one: Stockfish **+0.58**, and it stays comfortably ahead even against Black's sharpest tries (`4...Nb4` +1.57, `4...Qb4+` +1.79). This line is not a weakness for him in general.

But **`4. Bg5`** — a rarer try in his own practice (2/34 in this sample, so treat this as one concrete illustrative example rather than a repeatable percentage) — walked directly into a real trap in at least one of his archived games:

**Guigui4378 vs. xerberos56, 2025.11.11** (chess.com's own `ECOUrl` tags this exact position `Englund-Gambit-2.dxe5-Nc6-3.Nf3-Qe7`), result **0-1**:

```
1. d4 e5 2. dxe5 Nc6 3. Nf3 Qe7 4. Bg5 Qb4+ 5. c3 Qxb2 6. Nbd2 Qxc3 7. Rc1 Qb4 8. e3 Qa5 ...
```

[![4...Qb4+](https://backscattering.de/web-boardimage/board.svg?fen=r1b1kbnr/pppp1ppp/2n5/4P1B1/1q6/5N2/PPP1PPPP/RN1QKB1R&lastMove=e7b4&coordinates=true&size=320)](https://lichess.org/analysis/standard/r1b1kbnr/pppp1ppp/2n5/4P1B1/1q6/5N2/PPP1PPPP/RN1QKB1R_w_KQkq_-_5_5)

```
r1b1kbnr/pppp1ppp/2n5/4P1B1/1q6/5N2/PPP1PPPP/RN1QKB1R w KQkq - 5 5
```

At this exact point, Stockfish's own top choice is **5. Nc3!** — eval **+1.57**, clearly better for White (the queen has no comfortable retreat after, e.g., `5...Qxb2 6.Rb1` trapping it, or Black simply has to retreat losing time). Guigui instead played **5. c3?**, and the position collapses to **−0.35** — an engine-verified swing of just under two full pawns from one move. Crucially, the follow-up wasn't actually a further blunder: `6. Nbd2` in the game is the engine's own top choice at that point (also −0.32 to −0.35, essentially unavoidable once 5.c3 has been played), and even after `6...Qxc3 7.Rc1`, the position only sits at −0.28 — Black has grabbed a pawn and kept a slight practical edge, not won outright. **The actual mistake was the single move 5.c3, not the sequence that followed it** — worth stating precisely rather than blaming the whole line. **Concrete recommendation**: if he ever answers a `...Qb4+` check with `c3` rather than `Nc3` in this structure, `...Qxb2` is a real, engine-backed pawn grab, not a speculative try — but don't expect it to work if he finds `Nc3` instead, where the same idea is simply bad for Black (+1.79).

[*Back to TOP*](#_TOP_)

---

<a name="_c5_deviation_"></a>

## 1... c5: the second forced deviation

**1. d4 c5** (2.9%, 55 games) is live-tagged **A43, "Benoni Defense: Old Benoni"**. Masters overwhelmingly answer it **2. d5** (6695/8772, 76.3%), and the engine agrees it's clearly best:

**Guigui's own games (n=55)**

| Reply | games | share | Stockfish eval |
| :--- | ---: | ---: | ---: |
| 2. d5 | 33 | 60.0% | **+0.60** |
| 2. e3 | 11 | 20.0% | **+0.08** |
| 2. c3 | 10 | 18.2% | **+0.00** |

Unlike the e5 deviation (where his most common try is also the correct one but the split is roughly even), here he plays the objectively correct move a clear majority of the time (60%), but still gives away most of White's structural advantage in two games out of five — `2.e3` drops more than half a pawn of engine evaluation (+0.60 → +0.08) and `2.c3` gives it up almost entirely (+0.60 → +0.00). **Concrete recommendation**: if he doesn't play `2.d5` against `1...c5`, the position is already close to level for free — no specific tactical punish is needed, just develop normally and treat it as an equal Queen's-pawn middlegame rather than the space-gaining Benoni White is supposed to get. Full Benoni theory for the Black side of `2.d5` itself is out of scope here (White-only profile) — it's a natural candidate for the Black-repertoire follow-up.

[*Back to TOP*](#_TOP_)

---

<a name="_punishes_"></a>

## Practical cheat-sheet

1. **Expect 1.d4, then almost always 2.e3, whatever you play.** This is a personal system with no book name (`opening: None` at several of its own deepest, most-repeated nodes) — don't look for a "refutation" in existing theory, there isn't a specific one to look up. It's structurally sound but very slow (system root itself: dead equal, +0.03).
2. **Delay ...Nf6 in favor of ...e6** if you want to keep the option of meeting his eventual c4 with ...c5 — that specific central break all but disappears from play (1.2% vs 24.2%) once the knight commits to f6 first.
3. **After his 4.cxd5, recapture ...exd5, not ...Nxd5** — a real, engine-verified 0.44-pawn difference in Black's favor for the pawn recapture.
4. **Don't hand him the dxc4/Bxc4 structure for free** if you can instead contest with ...e6 and ...exd5 — the Bxc4-with-both-knights-out structure gives him a genuine ~+0.9 pull; the direct central challenge keeps it near dead equal.
5. **Facing his Nc3 against your ...Bb4 pin, expect a3, Nf3, Bd3, or Bd2 depending on the exact structure** — all of them check out as objectively sound replies once verified; there's no punishable inaccuracy to hunt for at this specific junction.
6. **If 1.d4 e5 gets a `...Qb4+` check answered with `c3` rather than `Nc3`, `...Qxb2` is a real pawn grab** (verified via his own archived loss to xerberos56) — but he finds the correct `Nc3` often enough in similar spots that this shouldn't be assumed automatically.
7. **If 1.d4 c5 doesn't get met with 2.d5** (2 games in 5, in his own practice), the position is already close to equal — no need to look for anything sharper than normal development.

[*Back to TOP*](#_TOP_)

---

## Cross-references

- [`d4_openings/D00_Queens_Pawn_Game.md`](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D00_Queens_Pawn_Game.md#_Stonewall_) carries a pointer note back to this file, next to its existing (and structurally distinct) "2. e3 — Stonewall Attack" section.
- No other existing card was found to overlap this profile's own content during research — every deep node this file covers came back `opening: None` in the live masters explorer, which is itself one of this profile's own findings (see "The system's own root" above).

[*Back to TOP*](#_TOP_)

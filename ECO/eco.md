# ECO Code Reference

Raw index of every ECO code A00-E99, scraped from [chessopenings.com/eco/&lt;CODE&gt;](https://chessopenings.com/eco/) (fetched 2026-08-25). This is **not a flashcard** — no diagrams, no Lichess stats, no Stockfish evals — it's a lookup table for discovering which move sequence a given code covers, used the same way `start.md` is used for card-authoring conventions rather than being one itself.

> [!IMPORTANT]
> Every fact here is a claim about what this one external site says, **not** a verified fact about this repo. Before building or correcting any card from an entry below, cross-check the code boundary and the position itself live via `tools/explore.py` (the Lichess explorer's own `opening` field) — this is what caught the A15→A16 and A20→A21 "wrong root code" bugs (see `memory.md`), and chessopenings.com's own listed name/PGN is not automatically the source of truth on its own.

---

## A00

- **Polish Opening** — `1.b4`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Polish.md)
- **Polish Opening, Tuebingen Variation** — `1.b4 Nh6`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Polish.md#_Tuebingen_)
- **Polish Opening, Outflank Variation** — `1.b4 c6`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Polish.md)
- **Benko's Opening** — `1.g3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Hungarian.md)
- **Lasker Simul Special** — `1.g3 h5`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Hungarian.md#_Lasker_Simul_)
- **Benko's Opening, Reversed Alekhine** — `1.g3 e5 2.Nf3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Hungarian.md#_Reversed_Alekhine_)
- **Grob's Attack** — `1.g4`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Grob.md)
- **Grob's Attack, Spike Attack** — `1.g4 d5 2.Bg2 c6 3.g5`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Grob.md#_Spike_)
- **Grob's Attack, Fritz Gambit** — `1.g4 d5 2.Bg2 Bxg4 3.c4`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Grob.md#_Fritz_)
- **Grob's Attack, Romford Counter-Gambit** — `1.g4 d5 2.Bg2 Bxg4 3.c4 d4`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Grob.md#_Romford_)
- **Clemenz Opening** — `1.h3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Clemenz.md)
- **Global Opening** — `1.h3 e5 2.a3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Clemenz.md#_Global_)
- **Amar Opening** — `1.Nh3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Amar.md)
- **Amar Opening, Gambit** — `1.Nh3 d5 2.g3 e5 3.f4 Bxh3 4.Bxh3 exf4`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Amar.md)
- **Dunst Opening** — `1.Nc3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Van_Geet.md)
- **Dunst Opening** — `1.Nc3 e5`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Van_Geet.md)
- **Battambang Opening** — `1.Nc3 e5 2.a3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Van_Geet.md#_Battambang_)
- **Novosibirsk Opening** — `1.Nc3 c5 2.d4 cxd4 3.Qxd4 Nc6 4.Qh4`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Van_Geet.md#_Novosibirsk_)
- **Anderssen's Opening** — `1.a3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Anderssen.md)
- **Ware Opening** — `1.a4`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Ware.md)
- **Crab Opening** — `1.a4 e5 2.h4`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Ware.md#_Crab_)
- **Saragossa Opening** — `1.c3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Saragossa.md)
- **Mieses Opening** — `1.d3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Mieses.md)
- **Mieses Opening** — `1.d3 e5`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Mieses.md)
- **Valencia Opening** — `1.d3 e5 2.Nd2`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Mieses.md#_Valencia_)
- **Venezolana Opening** — `1.d3 c5 2.Nc3 Nc6 3.g3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Mieses.md#_Venezolana_)
- **Van't Kruijs Opening** — `1.e3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Vant_Kruijs.md)
- **Amsterdam Attack** — `1.e3 e5 2.c4 d6 3.Nc3 Nc6 4.b3 Nf6`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Vant_Kruijs.md)
- **Gedult's Opening** — `1.f3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Barnes.md)
- **Hammerschlag** — `1.f3 e5 2.Kf2`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Barnes.md#_Hammerschlag_)
- **Anti-Borg Opening** — `1.h4`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Kadas.md)
- **Durkin's Attack** — `1.Na3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/A00_openings/Sodium.md)

## A01

- **Nimzovich-Larsen Attack** — `1.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/b3_openings/A01_Nimzo_Larsen.md#_initial_move_)
- **Nimzovich-Larsen Attack, Modern Variation** — `1.b3 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/b3_openings/A01_Nimzo_Larsen.md#_e5_)
- **Nimzovich-Larsen Attack, Indian Variation** — `1.b3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/b3_openings/A01_Nimzo_Larsen.md#_Nf6_)
- **Nimzovich-Larsen Attack, Classical Variation** — `1.b3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/b3_openings/A01_Nimzo_Larsen.md#_d5_)
- **Nimzovich-Larsen Attack, English Variation** — `1.b3 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/b3_openings/A01_Nimzo_Larsen.md#_c5_)
- **Nimzovich-Larsen Attack, Dutch Variation** — `1.b3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/b3_openings/A01_Nimzo_Larsen.md#_f5_)
- **Nimzovich-Larsen Attack, Polish Variation** — `1.b3 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/b3_openings/A01_Nimzo_Larsen.md#_b5_)
- **Nimzovich-Larsen Attack, Symmetrical Variation** — `1.b3 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/b3_openings/A01_Nimzo_Larsen.md#_b6_)

## A02

- **Bird's Opening** — `1.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/f4_openings/A02_Bird.md#_initial_move_)
- **Bird's Opening, From Gambit** — `1.f4 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/f4_openings/A02_Bird.md#_e5_)
- **Bird's Opening, From Gambit,  Lasker Variation** — `1.f4 e5 2.fxe5 d6 3.exd6 Bxd6 4.Nf3 g5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/f4_openings/A02_Bird.md#_e5_)
- **Bird's Opening, From Gambit,  Lipke Variation** — `1.f4 e5 2.fxe5 d6 3.exd6 Bxd6 4.Nf3 Nh6 5.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/f4_openings/A02_Bird.md#_e5_)
- **Bird's Opening, Swiss Gambit** — `1.f4 f5 2.e4 fxe4 3.Nc3 Nf6 4.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/f4_openings/A02_Bird.md#_f5_)
- **Bird's Opening, Hobbs Gambit** — `1.f4 g5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/f4_openings/A02_Bird.md#_g5_)

## A03

- **Bird's Opening** — `1.f4 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/f4_openings/A03_Bird_Dutch_Variation.md#_initial_move_)
- **Mujannah Opening** — `1.f4 d5 2.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/f4_openings/A03_Bird_Dutch_Variation.md#_c4_)
- **Bird's Opening, Williams Gambit** — `1.f4 d5 2.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/f4_openings/A03_Bird_Dutch_Variation.md#_e4_)
- **Bird's Opening, Lasker Variation** — `1.f4 d5 2.Nf3 Nf6 3.e3 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/f4_openings/A03_Bird_Dutch_Variation.md#_Lasker_Var_)

## A04

- **King's Indian Attack, Reti Opening** — `1.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A04_Zukertort.md#_Nf3_)
- **King's Indian Attack, Reti Opening,  Reti v Dutch** — `1.Nf3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A04_Zukertort.md#_f5_)
- **King's Indian Attack, Reti Opening,  Pirc-Lisitsin Gambit** — `1.Nf3 f5 2.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A04_Zukertort.md#_f5_)
- **King's Indian Attack, Reti Opening,  Lisitsin Gambit,  Deferred** — `1.Nf3 f5 2.d3 Nf6 3.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A04_Zukertort.md#_f5_)
- **King's Indian Attack, Reti Opening** — `1.Nf3 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A04_Zukertort.md#_d6_)
- **King's Indian Attack, Reti Opening,  Wade Defence** — `1.Nf3 d6 2.e4 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A04_Zukertort.md#_d6_)
- **King's Indian Attack, Reti Opening,  Herrstroem Gambit** — `1.Nf3 g5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A04_Zukertort.md#_g5_)

## A05

- **King's Indian Attack, Reti Opening** — `1.Nf3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A05_Zukertort_Nf6.md#_initial_move_)
- **King's Indian Attack, Reti Opening,  Spassky's Variation** — `1.Nf3 Nf6 2.g3 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A05_Zukertort_Nf6.md#_g3_)
- **King's Indian Attack, Reti Opening** — `1.Nf3 Nf6 2.g3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A05_Zukertort_Nf6.md#_g3_)
- **King's Indian Attack, Reti Opening,  Reti-Smyslov Variation** — `1.Nf3 Nf6 2.g3 g6 3.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A05_Zukertort_Nf6.md#_g3_)

## A06

- **King's Indian Attack, Reti Opening** — `1.Nf3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A06_Zukertort_d5.md#_initial_move_)
- **King's Indian Attack, Reti Opening,  Old Indian Attack** — `1.Nf3 d5 2.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A06_Zukertort_d5.md#_initial_move_)
- **Santasiere's folly, Reti Opening** — `1.Nf3 d5 2.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A06_Zukertort_d5.md#_initial_move_)
- **Tennison (Lemberg, Zukertort) Gambit, Reti Opening** — `1.Nf3 d5 2.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Tennison/Tennison.md)
- **King's Indian Attack, Reti Opening,  Nimzovich-Larsen Attack** — `1.Nf3 d5 2.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A06_Zukertort_d5.md#_initial_move_)

## A07

- **King's Indian Attack, Reti Opening,  King's Indian Attack (Barcza System)** — `1.Nf3 d5 2.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A07_Kings_Indian_Attack.md#_initial_move_)
- **King's Indian Attack, Reti Opening,  Yugoslav Variation** — `1.Nf3 d5 2.g3 Nf6 3.Bg2 c6 4.O-O Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A07_Kings_Indian_Attack.md)
- **King's Indian Attack, Reti Opening,  Keres Variation** — `1.Nf3 d5 2.g3 Bg4 3.Bg2 Nd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A07_Kings_Indian_Attack.md)
- **King's Indian Attack, Reti Opening** — `1.Nf3 d5 2.g3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A07_Kings_Indian_Attack.md#_initial_move_)
- **King's Indian Attack, Reti Opening,  Pachman System** — `1.Nf3 d5 2.g3 g6 3.Bg2 Bg7 4.O-O e5 5.d3 Ne7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A07_Kings_Indian_Attack.md)
- **King's Indian Attack, Reti Opening (with ...c5)** — `1.Nf3 d5 2.g3 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A08_Kings_Indian_Attack_Sicilian.md#_initial_move_)

## A08

- **King's Indian Attack, Reti Opening** — `1.Nf3 d5 2.g3 c5 3.Bg2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A08_Kings_Indian_Attack_Sicilian.md#_initial_move_)
- **King's Indian Attack, Reti Opening,  French Variation** — `1.Nf3 d5 2.g3 c5 3.Bg2 Nc6 4.O-O e6 5.d3 Nf6 6.Nbd2 Be7 7.e4 O-O 8.Re1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A08_Kings_Indian_Attack_Sicilian.md#_Nc6_)

## A09

- **King's Indian Attack, Reti Opening** — `1.Nf3 d5 2.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A09_Reti_Opening.md#_initial_move_)
- **King's Indian Attack, Reti Opening,  Advance Variation** — `1.Nf3 d5 2.c4 d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A09_Reti_Opening.md#_initial_move_)
- **King's Indian Attack, Reti Opening,  Accepted** — `1.Nf3 d5 2.c4 dxc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A09_Reti_Opening.md#_initial_move_)
- **King's Indian Attack, Reti Opening,  Accepted,  Keres Variation** — `1.Nf3 d5 2.c4 dxc4 3.e3 Be6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/Nf3_openings/A09_Reti_Opening.md)

## A10

- **English Opening** — `1.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A10_English.md#_c4_)
- **English Opening** — `1.c4 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A10_English.md#_g6_)
- **English Opening, Adorjan Defence** — `1.c4 g6 2.e4 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A10_English.md#_g6_)
- **English Opening, Jaenisch Gambit** — `1.c4 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A10_English.md#_b5_)
- **English Opening, Anglo-Dutch Defence** — `1.c4 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A10_English.md#_f5_)

## A11

- **English Opening, Caro-Kann defensive System** — `1.c4 c6`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A11_Caro_Kann_System.md#_c6_)

## A12

- **English Opening, Caro-Kann defensive System** — `1.c4 c6 2.Nf3 d5 3.b3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A12_Caro_Kann_System_b3.md#_initial_move_)
- **English Opening, Torre defensive System** — `1.c4 c6 2.Nf3 d5 3.b3 Nf6 4.g3 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A12_Caro_Kann_System_b3.md#_Nf6_g3_Bg4_)
- **English Opening, London defensive System** — `1.c4 c6 2.Nf3 d5 3.b3 Nf6 4.g3 Bf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A12_Caro_Kann_System_b3.md#_Nf6_g3_Bf5_)
- **English Opening, Caro-Kann defensive System** — `1.c4 c6 2.Nf3 d5 3.b3 Nf6 4.Bb2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A12_Caro_Kann_System_b3.md#_Nf6_Bb2_)
- **English Opening, Bled Variation** — `1.c4 c6 2.Nf3 d5 3.b3 Nf6 4.Bb2 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A12_Caro_Kann_System_b3.md#_Nf6_Bb2_g6_)
- **English Opening, New York (London) defensive System** — `1.c4 c6 2.Nf3 d5 3.b3 Nf6 4.Bb2 Bf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A12_Caro_Kann_System_b3.md#_Nf6_Bb2_Bf5_)
- **English Opening, Capablanca's Variation** — `1.c4 c6 2.Nf3 d5 3.b3 Nf6 4.Bb2 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A12_Caro_Kann_System_b3.md#_Nf6_Bb2_Bg4_)
- **English Opening, Caro-Kann defensive System,  Bogolyubov Variation** — `1.c4 c6 2.Nf3 d5 3.b3 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A12_Caro_Kann_System_b3.md#_Bg4_)

## A13

- **English Opening** — `1.c4 e6`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A13_Agincourt_Defense.md#_e6_)
- **English Opening, Romanishin Gambit** — `1.c4 e6 2.Nf3 Nf6 3.g3 a6 4.Bg2 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A13_Agincourt_Defense.md#_Nf6_romanishin_)
- **English Opening, Agincourt Variation** — `1.c4 e6 2.Nf3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A13_Agincourt_Defense.md#_Nf3_d5_)
- **English Opening, Wimpey System** — `1.c4 e6 2.Nf3 d5 3.b3 Nf6 4.Bb2 c5 5.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A13_Agincourt_Defense.md#_Nf3_d5_)
- **English Opening, Agincourt Variation** — `1.c4 e6 2.Nf3 d5 3.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A13_Agincourt_Defense.md#_Nf3_d5_g3_)
- **English Opening, Kurajica Defence** — `1.c4 e6 2.Nf3 d5 3.g3 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A13_Agincourt_Defense.md#_Nf3_d5_g3_)
- **English Opening, Neo-Catalan** — `1.c4 e6 2.Nf3 d5 3.g3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A13_Agincourt_Defense.md#_Nf3_d5_g3_)
- **English Opening, Neo-Catalan Accepted** — `1.c4 e6 2.Nf3 d5 3.g3 Nf6 4.Bg2 dxc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A13_Agincourt_Defense.md#_Nf3_d5_g3_)

## A14

- **English Opening, Neo-Catalan declined** — `1.c4 e6 2.Nf3 d5 3.g3 Nf6 4.Bg2 Be7 5.O-O`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A14_Neo_Catalan_Declined.md#_initial_move_)
- **English Opening, Symmetrical,  Keres Defence** — `1.c4 e6 2.Nf3 d5 3.g3 Nf6 4.Bg2 Be7 5.O-O c5 6.cxd5 Nxd5 7.Nc3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A14_Neo_Catalan_Declined.md#_c5_)

## A15

- **English Opening** — `1...Nf6 (Anglo-Indian Defence)` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A15_Anglo_Indian_Defense.md#_Nf6_)
- **English Opening, Orang-utan** — `1.c4 Nf6 2.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A15_Anglo_Indian_Defense.md#_b4_)
- **English Opening** — `1.c4 Nf6 2.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A15_Anglo_Indian_Defense.md#_alt_)

## A16

- **English Opening** — `1.c4 Nf6 2.Nc3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A16_Anglo_Indian_Queens_Knight.md#_Nc3_)
- **English Opening, Anglo-Gruenfeld Defence** — `1.c4 Nf6 2.Nc3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A16_Anglo_Indian_Queens_Knight.md#_d5_)
- **English Opening, Anglo-Gruenfeld Defence,  Smyslov Defence** — `1.c4 Nf6 2.Nc3 d5 3.cxd5 Nxd5 4.g3 g6 5.Bg2 Nxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A16_Anglo_Indian_Queens_Knight.md#_d5_)
- **English Opening, Anglo-Gruenfeld Defence,  Czech Defence** — `1.c4 Nf6 2.Nc3 d5 3.cxd5 Nxd5 4.g3 g6 5.Bg2 Nb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A16_Anglo_Indian_Queens_Knight.md#_d5_)
- **English Opening, Anglo-Gruenfeld Defence** — `1.c4 Nf6 2.Nc3 d5 3.cxd5 Nxd5 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A16_Anglo_Indian_Queens_Knight.md#_d5_)
- **English Opening, Anglo-Gruenfeld Defence,  Korchnoi Variation** — `1.c4 Nf6 2.Nc3 d5 3.cxd5 Nxd5 4.Nf3 g6 5.g3 Bg7 6.Bg2 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A16_Anglo_Indian_Queens_Knight.md#_d5_)

## A17

- **English Opening** — `1.c4 Nf6 2.Nc3 e6`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A17_Anglo_Indian_Hedgehog.md#_initial_move_)
- **English Opening, Queen's Indian formation** — `1.c4 Nf6 2.Nc3 e6 3.Nf3 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A17_Anglo_Indian_Hedgehog.md#_Nf3_b6_)
- **English Opening, Queen's Indian,  Romanishin Variation** — `1.c4 Nf6 2.Nc3 e6 3.Nf3 b6 4.e4 Bb7 5.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A17_Anglo_Indian_Hedgehog.md#_Nf3_b6_)
- **English Opening, Nimzo-English Opening** — `1.c4 Nf6 2.Nc3 e6 3.Nf3 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A17_Anglo_Indian_Hedgehog.md#_Nf3_Bb4_)

## A18

- **English Opening, Mikenas-Carls Variation** — `1.c4 Nf6 2.Nc3 e6 3.e4`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A18_Mikenas_Carls.md#_initial_move_)
- **English Opening, Mikenas-Carls,  Flohr Variation** — `1.c4 Nf6 2.Nc3 e6 3.e4 d5 4.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A18_Mikenas_Carls.md#_d5_)
- **English Opening, Mikenas-Carls,  Kevitz Variation** — `1.c4 Nf6 2.Nc3 e6 3.e4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A18_Mikenas_Carls.md#_Nc6_)

## A19

- **English Opening, Mikenas-Carls,  Sicilian Variation** — `1.c4 Nf6 2.Nc3 e6 3.e4 c5`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A19_Mikenas_Carls_Sicilian.md#_initial_move_)

## A20

- **English Opening** — `1.c4 e5`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A20_Kings_English_Variation.md#_e5_)
- **English Opening, Nimzovich Variation** — `1.c4 e5 2.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A20_Kings_English_Variation.md#_Nf3_)
- **English Opening, Nimzovich,  Flohr Variation** — `1.c4 e5 2.Nf3 e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A20_Kings_English_Variation.md#_Nf3_)

## A21

- **English Opening** — `1.c4 e5 2.Nc3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A21_Kings_English_Reversed_Sicilian.md#_Nc3_)
- **English Opening, Troeger Defence** — `1.c4 e5 2.Nc3 d6 3.g3 Be6 4.Bg2 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A21_Kings_English_Reversed_Sicilian.md#_d6_)
- **English Opening, Keres Variation** — `1.c4 e5 2.Nc3 d6 3.g3 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A21_Kings_English_Reversed_Sicilian.md#_d6_)
- **English Opening** — `1.c4 e5 2.Nc3 d6 3.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A21_Kings_English_Reversed_Sicilian.md#_d6_)
- **English Opening, Smyslov Defence** — `1.c4 e5 2.Nc3 d6 3.Nf3 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A21_Kings_English_Reversed_Sicilian.md#_d6_)
- **English Opening, Kramnik-Shirov Counterattack** — `1.c4 e5 2.Nc3 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A21_Kings_English_Reversed_Sicilian.md#_Bb4_)

## A22

- **English Opening** — `1.c4 e5 2.Nc3 Nf6`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A22_Two_Knights_Variation.md#_initial_move_)
- **English Opening, Bellon Gambit** — `1.c4 e5 2.Nc3 Nf6 3.Nf3 e4 4.Ng5 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A22_Two_Knights_Variation.md#_Nf3_)
- **English Opening, Carls' Bremen System** — `1.c4 e5 2.Nc3 Nf6 3.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A22_Two_Knights_Variation.md#_g3_)
- **English Opening, Bremen System,  Reverse Dragon** — `1.c4 e5 2.Nc3 Nf6 3.g3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A22_Two_Knights_Variation.md#_g3_d5_)
- **English Opening, Bremen System,  Smyslov System** — `1.c4 e5 2.Nc3 Nf6 3.g3 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A22_Two_Knights_Variation.md#_g3_Bb4_)

## A23

- **English Opening, Bremen System,  Keres Variation** — `1.c4 e5 2.Nc3 Nf6 3.g3 c6`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A23_Bremen_Keres_Variation.md#_initial_move_)

## A24

- **English Opening, Bremen System,  With ...g6** — `1.c4 e5 2.Nc3 Nf6 3.g3 g6`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A24_Bremen_Fianchetto.md#_initial_move_)

## A25

- **English Opening, Sicilian reversed** — `1.c4 e5 2.Nc3 Nc6`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A25_Reversed_Closed_Sicilian.md#_initial_move_)
- **English Opening, Closed** — `1.c4 e5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A25_Reversed_Closed_Sicilian.md#_Closed_)
- **English Opening, Closed,  Taimanov Variation** — `1.c4 e5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.e3 d6 6.Nge2 Nh6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A25_Reversed_Closed_Sicilian.md#_Closed_)
- **English Opening, Closed,  Hort Variation** — `1.c4 e5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.e3 d6 6.Nge2 Be6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A25_Reversed_Closed_Sicilian.md#_Closed_)
- **English Opening, Closed,  5.Rb1** — `1.c4 e5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.Rb1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A25_Reversed_Closed_Sicilian.md#_Closed_)
- **English Opening, Closed,  5.Rb1 Taimanov Variation** — `1.c4 e5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.Rb1 Nh6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A25_Reversed_Closed_Sicilian.md#_Closed_)
- **English Opening, Closed,  without ...d6** — `1.c4 e5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A25_Reversed_Closed_Sicilian.md#_Closed_)

## A26

- **English Opening, Closed** — `1.c4 e5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.d3 d6`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A26_Closed_System_Full_Symmetry.md#_initial_move_)
- **English Opening, Botvinnik System** — `1.c4 e5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.d3 d6 6.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A26_Closed_System_Full_Symmetry.md#_e4_)

## A27

- **English Opening, three Knights System** — `1.c4 e5 2.Nc3 Nc6 3.Nf3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A27_Three_Knights_System.md#_initial_move_)

## A28

- **English Opening, Four Knights System** — `1.c4 e5 2.Nc3 Nc6 3.Nf3 Nf6`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A28_Four_Knights_System.md#_initial_move_)
- **English Opening, Nenarokov Variation** — `1.c4 e5 2.Nc3 Nc6 3.Nf3 Nf6 4.d4 exd4 5.Nxd4 Bb4 6.Bg5 h6 7.Bh4 Bxc3 8.bxc3 Ne5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A28_Four_Knights_System.md#_d4_)
- **English Opening, Bradley Beach Variation** — `1.c4 e5 2.Nc3 Nc6 3.Nf3 Nf6 4.d4 e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A28_Four_Knights_System.md#_d4_)
- **English Opening, Four Knights,  Nimzovich Variation** — `1.c4 e5 2.Nc3 Nc6 3.Nf3 Nf6 4.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A28_Four_Knights_System.md#_e4_)
- **English Opening, Four Knights,  Marini Variation** — `1.c4 e5 2.Nc3 Nc6 3.Nf3 Nf6 4.a3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A28_Four_Knights_System.md#_a3_)
- **English Opening, Four Knights,  Capablanca Variation** — `1.c4 e5 2.Nc3 Nc6 3.Nf3 Nf6 4.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A28_Four_Knights_System.md#_d3_)
- **English Opening, Four Knights,  4.e3** — `1.c4 e5 2.Nc3 Nc6 3.Nf3 Nf6 4.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A28_Four_Knights_System.md#_e3_)
- **English Opening, Four Knights,  Stean Variation** — `1.c4 e5 2.Nc3 Nc6 3.Nf3 Nf6 4.e3 Bb4 5.Qc2 O-O 6.Nd5 Re8 7.Qf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A28_Four_Knights_System.md#_e3_)
- **English Opening, Four Knights,  Romanishin Variation** — `1.c4 e5 2.Nc3 Nc6 3.Nf3 Nf6 4.e3 Bb4 5.Qc2 Bxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A28_Four_Knights_System.md#_e3_)

## A29

- **English Opening, Four Knights,  kingside Fianchetto** — `1.c4 e5 2.Nc3 Nc6 3.Nf3 Nf6 4.g3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A29_Four_Knights_Fianchetto.md#_initial_move_)

## A30

- **English Opening, Symmetrical Variation** — `1.c4 c5`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A30_Symmetrical_Variation.md#_c5_)
- **English Opening, Symmetrical Variation,  hedgehog System** — `1.c4 c5 2.Nf3 Nf6 3.g3 b6 4.Bg2 Bb7 5.O-O e6 6.Nc3 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A30_Symmetrical_Variation.md)
- **English Opening, Symmetrical Variation,  hedgehog,  flexible formation** — `1.c4 c5 2.Nf3 Nf6 3.g3 b6 4.Bg2 Bb7 5.O-O e6 6.Nc3 Be7 7.d4 cxd4 8.Qxd4 d6 9.Rd1 a6 10.b3 Nbd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A30_Symmetrical_Variation.md)

## A31

- **English Opening, Symmetrical Variation,  Benoni formation** — `1.c4 c5 2.Nf3 Nf6 3.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A31_Anti_Benoni_Variation.md#_initial_move_)

## A32

- **English Opening, Symmetrical Variation** — `1.c4 c5 2.Nf3 Nf6 3.d4 cxd4 4.Nxd4 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A32_Anti_Benoni_Spielmann_Defense.md#_initial_move_)

## A33

- **English Opening, Symmetrical Variation** — `1.c4 c5 2.Nf3 Nf6 3.d4 cxd4 4.Nxd4 e6 5.Nc3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A33_Anti_Benoni_Spielmann_Defense.md#_initial_move_)
- **English Opening, Symmetrical Variation,  Geller Variation** — `1.c4 c5 2.Nf3 Nf6 3.d4 cxd4 4.Nxd4 e6 5.Nc3 Nc6 6.g3 Qb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A33_Anti_Benoni_Spielmann_Defense.md#_Geller_)

## A34

- **English Opening, Symmetrical Variation** — `1.c4 c5 2.Nc3`  ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A34_Symmetrical_Normal_Variation.md#_initial_move_)
- **English Opening, Symmetrical Variation,  three Knights System** — `1.c4 c5 2.Nc3 Nf6 3.Nf3 d5 4.cxd5 Nxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A34_Symmetrical_Normal_Variation.md#_Nf3_)
- **English Opening, Symmetrical Variation** — `1.c4 c5 2.Nc3 Nf6 3.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A34_Symmetrical_Normal_Variation.md#_g3_)
- **English Opening, Symmetrical Variation,  Rubinstein System** — `1.c4 c5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A34_Symmetrical_Normal_Variation.md#_g3_)

## A35

- **English Opening, Symmetrical Variation** — `1.c4 c5 2.Nc3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A35_Symmetrical_Two_Knights_Variation.md#_initial_move_)
- **English Opening, Symmetrical Variation,  Four Knights System** — `1.c4 c5 2.Nc3 Nc6 3.Nf3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A35_Symmetrical_Two_Knights_Variation.md#_Nf3_)

## A36

- **English Opening, Symmetrical Variation** — `1.c4 c5 2.Nc3 Nc6 3.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A36_Symmetrical_Fianchetto_Variation.md#_initial_move_)
- **English Opening, ultra-symmetrical Variation** — `1.c4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A36_Symmetrical_Fianchetto_Variation.md#_ultra_)
- **English Opening, Symmetrical Variation,  Botvinnik System reversed** — `1.c4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.e3 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A36_Symmetrical_Fianchetto_Variation.md#_e3_)
- **English Opening, Symmetrical Variation,  Botvinnik System** — `1.c4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A36_Symmetrical_Fianchetto_Variation.md#_e4_)

## A37

- **English Opening, Symmetrical Variation** — `1.c4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A37_Symmetrical_Three_Knights_Fianchetto.md#_initial_move_)
- **English Opening, Symmetrical Variation,  Botvinnik System reversed** — `1.c4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.Nf3 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A37_Symmetrical_Three_Knights_Fianchetto.md#_e5_)

## A38

- **English Opening, Symmetrical Variation** — `1.c4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.Nf3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A38_Symmetrical_Full_Symmetry.md#_initial_move_)
- **English Opening, Symmetrical Variation,  Main line With d3** — `1.c4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.Nf3 Nf6 6.O-O O-O 7.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A38_Symmetrical_Full_Symmetry.md#_d3_)
- **English Opening, Symmetrical Variation,  Main line With b3** — `1.c4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.Nf3 Nf6 6.O-O O-O 7.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A38_Symmetrical_Full_Symmetry.md#_b3_)

## A39

- **English Opening, Symmetrical Variation,  Main line With d4** — `1.c4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.Nf3 Nf6 6.O-O O-O 7.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/c4_openings/A39_Symmetrical_Mecking_Variation.md#_initial_move_)

## A40

- **Queen's Pawn Game** — `1.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A40_QPG.md#_d4_)
- **Queen's Pawn Game, Lundin (Kevitz-Mikenas) Defence** — `1.d4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A40_Mikenas_Defense.md#_initial_move_)
- **Queen's Pawn Game, Charlick (Englund) Gambit** — `1.d4 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A40_QPG.md#_e5_)
- **Queen's Pawn Game, Englund Gambit** — `1.d4 e5 2.dxe5 Nc6 3.Nf3 Qe7 4.Qd5 f6 5.exf6 Nxf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A40_QPG.md#_e5_)
- **Queen's Pawn Game, English Defence** — `1.d4 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A40_QPG.md#_b6_)
- **Polish Defence** — `1.d4 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A40_Polish_Defense.md#_initial_move_)
- **Queen's Pawn Game** — `1.d4 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A40_QPG.md#_e6_)
- **Queen's Pawn Game, Keres Defence** — `1.d4 e6 2.c4 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A40_QPG.md#_e6_)
- **Queen's Pawn Game, Franco-Indian (Keres) Defence** — `1.d4 e6 2.c4 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A40_QPG.md#_e6_)
- **Modern Defence** — `1.d4 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A40_QPG.md#_g6_)
- **Beefeater Defence** — `1.d4 g6 2.c4 Bg7 3.Nc3 c5 4.d5 Bxc3 5.bxc3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A40_QPG.md#_g6_)

## A41

- **Queen's Pawn Game** — `1.d4 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A41_Queens_Pawn_Game.md#_initial_move_)
- **Old Indian Defence, Tartakower (Wade) Variation** — `1.d4 d6 2.Nf3 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A41_Queens_Pawn_Game.md#_Nf3_)
- **Old Indian Defence** — `1.d4 d6 2.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A41_Queens_Pawn_Game.md#_c4_)
- **Modern Defence** — `1.d4 d6 2.c4 g6 3.Nc3 Bg7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A41_Queens_Pawn_Game.md#_c4_)
- **Robatsch Defence, Rossolimo Variation** — `1.e4 g6 2.d4 Bg7 3.Nf3 d6 4.c4 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A41_Queens_Pawn_Game.md#_c4_)

## A42

- **Modern Defence, Averbakh System** — `1.d4 d6 2.c4 g6 3.Nc3 Bg7 4.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A42_Modern_Averbakh_System.md#_initial_move_)
- **Pterodactyl Defence** — `1.d4 d6 2.c4 g6 3.Nc3 Bg7 4.e4 c5 5.Nf3 Qa5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A42_Modern_Averbakh_System.md#_c5_)
- **Modern Defence, Averbakh System,  Randspringer Variation** — `1.d4 d6 2.c4 g6 3.Nc3 Bg7 4.e4 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A42_Modern_Averbakh_System.md#_f5_)
- **Modern Defence, Averbakh System,  Kotov Variation** — `1.d4 d6 2.c4 g6 3.Nc3 Bg7 4.e4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A42_Modern_Averbakh_System.md#_Nc6_)

## A43

- **Benoni Defence, Old Benoni Defence** — `1.d4 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A43_Old_Benoni.md#_initial_move_)
- **Benoni Defence, Old Benoni Defence,  Franco-Benoni Defence** — `1.d4 c5 2.d5 e6 3.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A43_Old_Benoni.md#_e6_)
- **Benoni Defence, Old Benoni Defence,  Mujannah formation** — `1.d4 c5 2.d5 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A43_Old_Benoni.md#_f5_)
- **Benoni Defence, Old Benoni Defence** — `1.d4 c5 2.d5 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A43_Old_Benoni.md#_Nf6_)
- **Woozle Defence** — `1.d4 c5 2.d5 Nf6 3.Nc3 Qa5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A43_Old_Benoni.md#_Nf6_)
- **Benoni Defence, Old Benoni Defence** — `1.d4 c5 2.d5 Nf6 3.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A43_Old_Benoni.md#_Nf6_)
- **Hawk Defence** — `1.d4 c5 2.d5 Nf6 3.Nf3 c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A43_Old_Benoni.md#_Nf6_)
- **Benoni Defence, Old Benoni Defence** — `1.d4 c5 2.d5 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A43_Old_Benoni.md#_d6_)
- **Benoni Defence, Old Benoni Defence,  Schmid's System** — `1.d4 c5 2.d5 d6 3.Nc3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A43_Old_Benoni.md#_d6_)

## A44

- **Benoni Defence, Old Benoni Defence** — `1.d4 c5 2.d5 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A44_Old_Benoni.md#_initial_move_)
- **Semi-Benoni** — `1.d4 c5 2.d5 e5 3.e4 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A44_Old_Benoni.md#_e4_)

## A45

- **Queen's Pawn Game** — `1.d4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A45_Trompowsky_Attack.md)
- **Queen's Pawn Game, Bronstein Gambit** — `1.d4 Nf6 2.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A45_Trompowsky_Attack.md#_g4_)
- **Canard Opening** — `1.d4 Nf6 2.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A45_Trompowsky_Attack.md#_f4_)
- **Paleface Attack** — `1.d4 Nf6 2.f3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A45_Trompowsky_Attack.md#_f3_)
- **Blackmar-Diemer Gambit** — `1.d4 Nf6 2.f3 d5 3.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A45_Trompowsky_Attack.md#_f3_)
- **Gedult Attack** — `1.d4 Nf6 2.f3 d5 3.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A45_Trompowsky_Attack.md#_f3_)
- **Trompowsky Attack** — `1.d4 Nf6 2.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A45_Trompowsky_Attack.md#_initial_move_)

## A46

- **Queen's Pawn Game** — `1.d4 Nf6 2.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A46_Indian_Knights_Variation.md#_initial_move_)
- **Queen's Pawn Game, Torre Attack** — `1.d4 Nf6 2.Nf3 e6 3.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A46_Indian_Knights_Variation.md#_Bg5_)
- **Queen's Pawn Game, Torre Attack,  Wagner Gambit** — `1.d4 Nf6 2.Nf3 e6 3.Bg5 c5 4.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A46_Indian_Knights_Variation.md#_Bg5_)
- **Queen's Pawn Game, Yusupov-Rubinstein System** — `1.d4 Nf6 2.Nf3 e6 3.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A46_Indian_Knights_Variation.md#_e3_)
- **Doery Defence** — `1.d4 Nf6 2.Nf3 Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A46_Indian_Knights_Variation.md#_Ne4_)

## A47

- **Queen's Indian Defence** — `1.d4 Nf6 2.Nf3 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A47_Pseudo_Queens_Indian.md#_initial_move_)
- **Queen's Indian Defence, Marienbad System** — `1.d4 Nf6 2.Nf3 b6 3.g3 Bb7 4.Bg2 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A47_Pseudo_Queens_Indian.md#_c5_)
- **Queen's Indian Defence, Marienbad System,  Berg Variation** — `1.d4 Nf6 2.Nf3 b6 3.g3 Bb7 4.Bg2 c5 5.c4 cxd4 6.Qxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A47_Pseudo_Queens_Indian.md#_c5_)

## A48

- **King's Indian Defence, East Indian Defence** — `1.d4 Nf6 2.Nf3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A48_East_Indian_Defense.md#_initial_move_)
- **King's Indian Defence, Torre Attack** — `1.d4 Nf6 2.Nf3 g6 3.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A48_East_Indian_Defense.md#_Bg5_)
- **King's Indian Defence, London System** — `1.d4 Nf6 2.Nf3 g6 3.Bf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A48_East_Indian_Defense.md#_Bf4_)

## A49

- **King's Indian Defence, Fianchetto Without c4** — `1.d4 Nf6 2.Nf3 g6 3.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A49_Indian_Przepiorka_Variation.md#_initial_move_)

## A50

- **Queen's Pawn Game** — `1.d4 Nf6 2.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A50_Indian_Normal_Variation.md#_initial_move_)
- **Kevitz-Trajkovich Defence** — `1.d4 Nf6 2.c4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A50_Indian_Normal_Variation.md#_Nc6_)
- **Queen's Indian Defence, Accelerated** — `1.d4 Nf6 2.c4 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A50_Indian_Normal_Variation.md#_b6_)

## A51

- **Budapest Defence, Declined** — `1.d4 Nf6 2.c4 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A51_Budapest_Gambit_Declined.md#_initial_move_)
- **Budapest Defence, Fajarowicz Variation** — `1.d4 Nf6 2.c4 e5 3.dxe5 Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A51_Budapest_Gambit_Declined.md#_Ne4_)
- **Budapest Defence, Fajarowicz Variation,  Steiner Variation** — `1.d4 Nf6 2.c4 e5 3.dxe5 Ne4 4.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A51_Budapest_Gambit_Declined.md#_Ne4_)

## A52

- **Budapest Defence** — `1.d4 Nf6 2.c4 e5 3.dxe5 Ng4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A52_Budapest_Gambit_Accepted.md#_initial_move_)
- **Budapest Defence, Adler Variation** — `1.d4 Nf6 2.c4 e5 3.dxe5 Ng4 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A52_Budapest_Gambit_Accepted.md#_Nf3_)
- **Budapest Defence, Rubinstein Variation** — `1.d4 Nf6 2.c4 e5 3.dxe5 Ng4 4.Bf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A52_Budapest_Gambit_Accepted.md#_Bf4_)
- **Budapest Defence, Alekhine Variation** — `1.d4 Nf6 2.c4 e5 3.dxe5 Ng4 4.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A52_Budapest_Gambit_Accepted.md#_e4_)
- **Budapest Defence, Alekhine,  Abonyi Variation** — `1.d4 Nf6 2.c4 e5 3.dxe5 Ng4 4.e4 Nxe5 5.f4 Nec6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A52_Budapest_Gambit_Accepted.md#_e4_)
- **Budapest Defence, Alekhine Variation,  Balogh Gambit** — `1.d4 Nf6 2.c4 e5 3.dxe5 Ng4 4.e4 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A52_Budapest_Gambit_Accepted.md#_e4_)

## A53

- **Old Indian Defence** — `1.d4 Nf6 2.c4 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A53_Old_Indian_Defense.md#_initial_move_)
- **Old Indian Defence, Janowski Variation** — `1.d4 Nf6 2.c4 d6 3.Nc3 Bf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A53_Old_Indian_Defense.md#_Bf5_)

## A54

- **Old Indian Defence, Ukrainian Variation** — `1.d4 Nf6 2.c4 d6 3.Nc3 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A54_Old_Indian_Ukrainian_Variation.md#_initial_move_)
- **Old Indian Defence, Dus-Khotimirsky Variation** — `1.d4 Nf6 2.c4 d6 3.Nc3 e5 4.e3 Nbd7 5.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A54_Old_Indian_Ukrainian_Variation.md#_e3_)
- **Old Indian Defence, Ukrainian Variation,  4.Nf3** — `1.d4 Nf6 2.c4 d6 3.Nc3 e5 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A54_Old_Indian_Ukrainian_Variation.md#_Nf3_)

## A55

- **Old Indian Defence, Main line** — `1.d4 Nf6 2.c4 d6 3.Nc3 e5 4.Nf3 Nbd7 5.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A55_Old_Indian_Normal_Variation.md#_initial_move_)

## A56

- **Benoni Defence** — `1.d4 Nf6 2.c4 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A56_Benoni_Defense.md#_c5_)
- **Benoni Defence, Hromodka System** — `1.d4 Nf6 2.c4 c5 3.d5 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A56_Benoni_Defense.md#_d6_)
- **Vulture Defence** — `1.d4 Nf6 2.c4 c5 3.d5 Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A56_Benoni_Defense.md#_Ne4_)
- **Benoni Defence, Czech Benoni Defence** — `1.d4 Nf6 2.c4 c5 3.d5 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A56_Benoni_Defense.md#_e5_)
- **Benoni Defence, Czech Benoni Defence,  King's Indian System** — `1.d4 Nf6 2.c4 c5 3.d5 e5 4.Nc3 d6 5.e4 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A56_Benoni_Defense.md#_e5_)

## A57

- **Benko Defence, Gambit** — `1.d4 Nf6 2.c4 c5 3.d5 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A57_Benko_Gambit.md#_initial_move_)
- **Benko Defence, Gambit,  Half Accepted** — `1.d4 Nf6 2.c4 c5 3.d5 b5 4.cxb5 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A57_Benko_Gambit.md#_a6_)
- **Benko Defence, Gambit,  Zaitsev System** — `1.d4 Nf6 2.c4 c5 3.d5 b5 4.cxb5 a6 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A57_Benko_Gambit.md#_Nc3_)
- **Benko Defence, Gambit,  Nescafe Frappe Attack** — `1.d4 Nf6 2.c4 c5 3.d5 b5 4.cxb5 a6 5.Nc3 axb5 6.e4 b4 7.Nb5 d6 8.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A57_Benko_Gambit.md#_Nc3_)

## A58

- **Benko Defence, Gambit,  Accepted** — `1.d4 Nf6 2.c4 c5 3.d5 b5 4.cxb5 a6 5.bxa6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A58_Benko_Gambit_Fully_Accepted.md#_initial_move_)
- **Benko Defence, Gambit,  Nd2 Variation** — `1.d4 Nf6 2.c4 c5 3.d5 b5 4.cxb5 a6 5.bxa6 Bxa6 6.Nc3 d6 7.Nf3 g6 8.Nd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A58_Benko_Gambit_Fully_Accepted.md#_Nd2_)
- **Benko Defence, Gambit,  Fianchetto Variation** — `1.d4 Nf6 2.c4 c5 3.d5 b5 4.cxb5 a6 5.bxa6 Bxa6 6.Nc3 d6 7.Nf3 g6 8.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A58_Benko_Gambit_Fully_Accepted.md#_g3_)

## A59

- **Benko Defence, Gambit,  7.e4** — `1.d4 Nf6 2.c4 c5 3.d5 b5 4.cxb5 a6 5.bxa6 Bxa6 6.Nc3 d6 7.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A59_Benko_Gambit_Yugoslav.md#_initial_move_)
- **Benko Defence, Gambit,  Ne2 Variation** — `1.d4 Nf6 2.c4 c5 3.d5 b5 4.cxb5 a6 5.bxa6 Bxa6 6.Nc3 d6 7.e4 Bxf1 8.Kxf1 g6 9.Nge2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A59_Benko_Gambit_Yugoslav.md#_Nge2_)
- **Benko Defence, Gambit** — `1.d4 Nf6 2.c4 c5 3.d5 b5 4.cxb5 a6 5.bxa6 Bxa6 6.Nc3 d6 7.e4 Bxf1 8.Kxf1 g6 9.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A59_Benko_Gambit_Yugoslav.md#_g3_)
- **Benko Defence, Gambit,  Main line** — `1.d4 Nf6 2.c4 c5 3.d5 b5 4.cxb5 a6 5.bxa6 Bxa6 6.Nc3 d6 7.e4 Bxf1 8.Kxf1 g6 9.g3 Bg7 10.Kg2 O-O 11.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A59_Benko_Gambit_Yugoslav.md#_g3_)

## A60

- **Benoni Defence** — `1.d4 Nf6 2.c4 c5 3.d5 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A60_Modern_Benoni.md#_initial_move_)

## A61

- **Benoni Defence** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.Nf3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A61_Benoni_Nf3_Systems.md#_initial_move_)
- **Benoni Defence, Uhlmann Variation** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.Nf3 g6 7.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A61_Benoni_Nf3_Systems.md#_Bg5_)
- **Benoni Defence, Nimzovich (knight's tour) Variation** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.Nf3 g6 7.Nd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A61_Benoni_Nf3_Systems.md#_Nd2_)
- **Benoni Defence, Fianchetto Variation** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.Nf3 g6 7.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A62_Benoni_Fianchetto_Variation.md#_initial_move_)

## A62

- **Benoni Defence, Fianchetto Variation** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.Nf3 g6 7.g3 Bg7 8.Bg2 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A62_Benoni_Fianchetto_Variation.md#_initial_move_)

## A63

- **Benoni Defence, Fianchetto,  9...Nbd7** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.Nf3 g6 7.g3 Bg7 8.Bg2 O-O 9.O-O Nbd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A63_Benoni_Fianchetto_Hastings_Defense.md#_initial_move_)

## A64

- **Benoni Defence, Fianchetto,  11...Re8** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.Nf3 g6 7.g3 Bg7 8.Bg2 O-O 9.O-O Nbd7 10.Nd2 a6 11.a4 Re8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A64_Benoni_Fianchetto_Hastings_Main_Line.md#_initial_move_)

## A65

- **Benoni Defence, 6.e4** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A65_Benoni_Kings_Pawn_Line.md#_initial_move_)

## A66

- **Benoni Defence, pawn Storm Variation** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A66_Benoni_Pawn_Storm.md#_initial_move_)
- **Benoni Defence, Mikenas Variation** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.f4 Bg7 8.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A66_Benoni_Pawn_Storm.md#_e5_)

## A67

- **Benoni Defence, Taimanov Variation** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.f4 Bg7 8.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A67_Benoni_Taimanov_Variation.md#_initial_move_)

## A68

- **Benoni Defence, Four Pawns Attack** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.f4 Bg7 8.Nf3 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A68_Benoni_Four_Pawns_Attack.md#_initial_move_)

## A69

- **Benoni Defence, Four Pawns Attack,  Main line** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.f4 Bg7 8.Nf3 O-O 9.Be2 Re8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A69_Benoni_Four_Pawns_Main_Line.md#_initial_move_)

## A70

- **Benoni Defence, Classical With e4 and Nf3** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A70_Benoni_Classical_Variation.md#_initial_move_)
- **Benoni Defence, Classical Without 9.O-O** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.Nf3 Bg7 8.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A70_Benoni_Classical_Variation.md#_Be2_)

## A71

- **Benoni Defence, Classical,  8.Bg5** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.Nf3 Bg7 8.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A71_Benoni_Averbakh_Grivas_Attack.md#_initial_move_)

## A72

- **Benoni Defence, Classical Without 9.O-O** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.Nf3 Bg7 8.Be2 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A72_Benoni_Classical_Both_Castled.md#_initial_move_)

## A73

- **Benoni Defence, Classical,  9.O-O** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.Nf3 Bg7 8.Be2 O-O 9.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A73_Benoni_Classical_Main_Line.md#_initial_move_)

## A74

- **Benoni Defence, Classical,  9...a6,  10.a4** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.Nf3 Bg7 8.Be2 O-O 9.O-O a6 10.a4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A74_Benoni_Classical_Full_Line.md#_initial_move_)

## A75

- **Benoni Defence, Classical With ...a6 and 10...Bg4** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.Nf3 Bg7 8.Be2 O-O 9.O-O a6 10.a4 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A75_Benoni_Argentine_Counterattack.md#_initial_move_)

## A76

- **Benoni Defence, Classical,  9...Re8** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.Nf3 Bg7 8.Be2 O-O 9.O-O Re8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A76_Benoni_Czerniak_Defense.md#_initial_move_)

## A77

- **Benoni Defence, Classical,  9...Re8,  10.Nd2** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.Nf3 Bg7 8.Be2 O-O 9.O-O Re8 10.Nd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A77_Benoni_Czerniak_Tal_Line.md#_initial_move_)

## A78

- **Benoni Defence, Classical With ...Re8 and ...Na6** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.Nf3 Bg7 8.Be2 O-O 9.O-O Re8 10.Nd2 Na6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A78_Benoni_Czerniak_Na6.md#_initial_move_)

## A79

- **Benoni Defence, Classical,  11.f3** — `1.d4 Nf6 2.c4 c5 3.d5 e6 4.Nc3 exd5 5.cxd5 d6 6.e4 g6 7.Nf3 Bg7 8.Be2 O-O 9.O-O Re8 10.Nd2 Na6 11.f3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A79_Benoni_Czerniak_f3.md#_initial_move_)

## A80

- **Dutch Defence** — `1.d4 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A80_Dutch_Defense.md#_initial_move_)
- **Dutch Defence, Spielmann Gambit** — `1.d4 f5 2.Nc3 Nf6 3.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A80_Dutch_Defense.md#_Nc3_g4_)
- **Dutch Defence, Manhattan (Alapin,  Ulvestad) Variation** — `1.d4 f5 2.Qd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A80_Dutch_Defense.md#_Qd3_)
- **Dutch Defence, Von Pretzel Gambit** — `1.d4 f5 2.Qd3 e6 3.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A80_Dutch_Defense.md#_Qd3_)
- **Dutch Defence, Korchnoi Attack** — `1.d4 f5 2.h3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A80_Dutch_Defense.md#_h3_)
- **Dutch Defence, Krejcik Gambit** — `1.d4 f5 2.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A80_Dutch_Defense.md#_g4_)
- **Dutch Defence, 2.Bg5 Variation** — `1.d4 f5 2.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A80_Dutch_Defense.md#_Bg5_)

## A81

- **Dutch Defence** — `1.d4 f5 2.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A81_Dutch_Fianchetto_Attack.md#_g3_)
- **Dutch Defence, Blackburne Variation** — `1.d4 f5 2.g3 Nf6 3.Bg2 e6 4.Nh3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A81_Dutch_Fianchetto_Attack.md#_e6_)
- **Dutch Defence** — `1.d4 f5 2.g3 Nf6 3.Bg2 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A81_Dutch_Fianchetto_Attack.md#_g6_2_)
- **Dutch Defence, Leningrad,  Basman System** — `1.d4 f5 2.g3 g6 3.Bg2 Bg7 4.Nf3 c6 5.O-O Nh6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A81_Dutch_Fianchetto_Attack.md#_Nh6_)
- **Dutch Defence, Leningrad,  Karlsbad Variation** — `1.d4 f5 2.g3 g6 3.Bg2 Bg7 4.Nh3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A81_Dutch_Fianchetto_Attack.md#_Nh3_)

## A82

- **Dutch Defence, Staunton Gambit** — `1.d4 f5 2.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A82_Dutch_Staunton_Gambit.md#_initial_move_)
- **Dutch Defence, Balogh Defence** — `1.d4 f5 2.e4 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A82_Dutch_Staunton_Gambit.md#_d6_)
- **Dutch Defence, Staunton Gambit** — `1.d4 f5 2.e4 fxe4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A82_Dutch_Staunton_Gambit.md#_fxe4_)
- **Dutch Defence, Staunton Gambit,  Tartakower Variation** — `1.d4 f5 2.e4 fxe4 3.Nc3 Nf6 4.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A82_Dutch_Staunton_Gambit.md#_g4_)

## A83

- **Dutch Defence, Staunton Gambit,  Staunton's line** — `1.d4 f5 2.e4 fxe4 3.Nc3 Nf6 4.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A83_Dutch_Staunton_Gambit_Bg5.md#_initial_move_)
- **Dutch Defence, Staunton Gambit,  Alekhine Variation** — `1.d4 f5 2.e4 fxe4 3.Nc3 Nf6 4.Bg5 g6 5.h4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A83_Dutch_Staunton_Gambit_Bg5.md#_h4_)
- **Dutch Defence, Staunton Gambit,  Lasker Variation** — `1.d4 f5 2.e4 fxe4 3.Nc3 Nf6 4.Bg5 g6 5.f3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A83_Dutch_Staunton_Gambit_Bg5.md#_f3_)
- **Dutch Defence, Staunton Gambit,  Chigorin Variation** — `1.d4 f5 2.e4 fxe4 3.Nc3 Nf6 4.Bg5 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A83_Dutch_Staunton_Gambit_Bg5.md#_c6_)
- **Dutch Defence, Staunton Gambit,  Nimzovich Variation** — `1.d4 f5 2.e4 fxe4 3.Nc3 Nf6 4.Bg5 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A83_Dutch_Staunton_Gambit_Bg5.md#_b6_)

## A84

- **Dutch Defence** — `1.d4 f5 2.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A84_Dutch_c4_Systems.md#_initial_move_)
- **Dutch Defence, Bladel Variation** — `1.d4 f5 2.c4 g6 3.Nc3 Nh6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A84_Dutch_c4_Systems.md#_g6_)
- **Dutch Defence** — `1.d4 f5 2.c4 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A84_Dutch_c4_Systems.md#_e6_)
- **Dutch Defence, Rubinstein Variation** — `1.d4 f5 2.c4 e6 3.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A84_Dutch_c4_Systems.md#_Nc3_)
- **Dutch Defence, Staunton Gambit,  Deferred** — `1.d4 f5 2.c4 e6 3.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A84_Dutch_c4_Systems.md#_e4_)
- **Dutch Defence** — `1.d4 f5 2.c4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A84_Dutch_c4_Systems.md#_Nf6_)

## A85

- **Dutch Defence, With c4 & Nc3** — `1.d4 f5 2.c4 Nf6 3.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A85_Dutch_Queens_Knight_Variation.md#_initial_move_)

## A86

- **Dutch Defence, With c4 & g3** — `1.d4 f5 2.c4 Nf6 3.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A86_Dutch_Fianchetto_Variation.md#_initial_move_)
- **Dutch Defence, Hort-Antoshin System** — `1.d4 f5 2.c4 Nf6 3.g3 d6 4.Bg2 c6 5.Nc3 Qc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A86_Dutch_Fianchetto_Variation.md#_d6_)
- **Dutch Defence, Leningrad Variation** — `1.d4 f5 2.c4 Nf6 3.g3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A86_Dutch_Fianchetto_Variation.md#_g6_)

## A87

- **Dutch Defence, Leningrad,  main Variation** — `1.d4 f5 2.c4 Nf6 3.g3 g6 4.Bg2 Bg7 5.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A87_Dutch_Leningrad_Variation.md#_initial_move_)

## A88

- **Dutch Defence, Leningrad,  main Variation With c6** — `1.d4 f5 2.c4 Nf6 3.g3 g6 4.Bg2 Bg7 5.Nf3 O-O 6.O-O d6 7.Nc3 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A88_Dutch_Leningrad_Warsaw_Variation.md#_initial_move_)

## A89

- **Dutch Defence, Leningrad,  main Variation With Nc6** — `1.d4 f5 2.c4 Nf6 3.g3 g6 4.Bg2 Bg7 5.Nf3 O-O 6.O-O d6 7.Nc3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A89_Dutch_Leningrad_Matulovic_Variation.md#_initial_move_)

## A90

- **Dutch Defence** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A90_Dutch_Classical_and_Stonewall.md#_initial_move_)
- **Dutch Defence, Dutch-Indian (Nimzo-Dutch) Variation** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A90_Dutch_Classical_and_Stonewall.md#_Bb4_)
- **Dutch Defence, Dutch-Indian,  Alekhine Variation** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Bb4 5.Bd2 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A90_Dutch_Classical_and_Stonewall.md#_Bb4_)

## A91

- **Dutch Defence** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A91_Dutch_Be7.md#_initial_move_)

## A92

- **Dutch Defence** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7 5.Nf3 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A92_Dutch_Stonewall_and_Classical.md#_initial_move_)
- **Dutch Defence, Alekhine Variation** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7 5.Nf3 O-O 6.O-O Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A92_Dutch_Stonewall_and_Classical.md#_Ne4_)
- **Dutch Defence, Stonewall Variation** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7 5.Nf3 O-O 6.O-O d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A92_Dutch_Stonewall_and_Classical.md#_d5_)
- **Dutch Defence, Stonewall With Nc3** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7 5.Nf3 O-O 6.O-O d5 7.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A92_Dutch_Stonewall_and_Classical.md#_Nc3_)

## A93

- **Dutch Defence, Stonewall,  Botvinnik Variation** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7 5.Nf3 O-O 6.O-O d5 7.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A93_Dutch_Stonewall_Botvinnik_Variation.md#_initial_move_)

## A94

- **Dutch Defence, Stonewall With Ba3** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7 5.Nf3 O-O 6.O-O d5 7.b3 c6 8.Ba3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A94_Dutch_Stonewall_Ba3_Variation.md#_initial_move_)

## A95

- **Dutch Defence, Stonewall With Nc3** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7 5.Nf3 O-O 6.O-O d5 7.Nc3 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A95_Dutch_Stonewall_Nc3_c6.md#_initial_move_)
- **Dutch Defence, Stonewall: Chekhover Variation** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7 5.Nf3 O-O 6.O-O d5 7.Nc3 c6 8.Qc2 Qe8 9.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A95_Dutch_Stonewall_Nc3_c6.md#_Qc2_)

## A96

- **Dutch Defence, Classical Variation** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7 5.Nf3 O-O 6.O-O d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A96_Dutch_Classical_Variation.md#_initial_move_)

## A97

- **Dutch Defence, Ilyin-Genevsky Variation** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7 5.Nf3 O-O 6.O-O d6 7.Nc3 Qe8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A97_Dutch_Ilyin_Zhenevsky_Variation.md#_initial_move_)
- **Dutch Defence, Ilyin-Genevsky,  Winter Variation** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7 5.Nf3 O-O 6.O-O d6 7.Nc3 Qe8 8.Re1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A97_Dutch_Ilyin_Zhenevsky_Variation.md#_Re1_)

## A98

- **Dutch Defence, Ilyin-Genevsky Variation With Qc2** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7 5.Nf3 O-O 6.O-O d6 7.Nc3 Qe8 8.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A98_Dutch_Ilyin_Zhenevsky_Alatortsev_Lisitsyn_Line.md#_initial_move_)

## A99

- **Dutch Defence, Ilyin-Genevsky Variation With b3** — `1.d4 f5 2.c4 Nf6 3.g3 e6 4.Bg2 Be7 5.Nf3 O-O 6.O-O d6 7.Nc3 Qe8 8.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/A99_Dutch_Ilyin_Zhenevsky_Modern_Main_Line.md#_initial_move_)

## B00

- **King's Pawn Game** — `1.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B00_KPG.md#_e4_)
- **King's Pawn Game, Hippopotamus Defence** — `1.e4 Nh6 2.d4 g6 3.c4 f6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/B00_openings/Hippopotamus.md#_initial_move_)
- **King's Pawn Game, Corn Stalk Defence** — `1.e4 a5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/B00_openings/Ware_Defense.md#_initial_move_) — live-tagged the *Ware Defense*, a real name divergence
- **King's Pawn Game, Lemming Defence** — `1.e4 Na6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/B00_openings/Lemming.md#_initial_move_)
- **King's Pawn Game, Fred Defence** — `1.e4 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/B00_openings/Duras_Gambit.md#_initial_move_) — live-tagged the *Duras Gambit*, a real name divergence
- **King's Pawn Game, Barnes Defence** — `1.e4 f6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/B00_openings/Barnes.md#_initial_move_)
- **King's Pawn Game, Fried fox Defence** — `1.e4 f6 2.d4 Kf7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/B00_openings/Barnes.md#_fried_fox_)
- **King's Pawn Game, Carr's Defence** — `1.e4 h6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/B00_openings/Carr.md#_initial_move_)
- **King's Pawn Game, Reversed Grob** — `1.e4 g5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/B00_openings/Borg.md#_initial_move_) — the card's own title uses the established name *Borg Defense* instead
- **King's Pawn Game, St. George Defence** — `1.e4 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/B00_openings/St_George.md#_initial_move_)
- **King's Pawn Game, Owen Defence** — `1.e4 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/B00_openings/Owen.md#_initial_move_)
- **King's Pawn Game, Guatemala Defence** — `1.e4 b6 2.d4 Ba6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/B00_openings/Owen.md#_d4_)
- **King's Pawn Game, Nimzovich Defence** — `1.e4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B00_Nimzowitsch_Defense.md#_initial_move_)
- **King's Pawn Game, Nimzovich Defence,  Wheeler Gambit** — `1.e4 Nc6 2.b4 Nxb4 3.c3 Nc6 4.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B00_Nimzowitsch_Defense.md#_initial_move_)
- **King's Pawn Game, Nimzovich Defence** — `1.e4 Nc6 2.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B00_Nimzowitsch_Defense.md#_Nf3_)
- **King's Pawn Game, Colorado Counter** — `1.e4 Nc6 2.Nf3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B00_Nimzowitsch_Defense.md#_Nf3_)
- **King's Pawn Game, Nimzovich Defence** — `1.e4 Nc6 2.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B00_Nimzowitsch_Defense.md#_d4_)
- **King's Pawn Game, Nimzovich Defence,  Marshall Gambit** — `1.e4 Nc6 2.d4 d5 3.exd5 Qxd5 4.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B00_Nimzowitsch_Defense.md#_Exchange_)
- **King's Pawn Game, Nimzovich Defence,  Bogolyubov Variation** — `1.e4 Nc6 2.d4 d5 3.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B00_Nimzowitsch_Defense.md#_Bogolyubov_) — live-tagged *Bogoljubow*, a minor spelling divergence
- **King's Pawn Game, Neo-Mongoloid Defence** — `1.e4 Nc6 2.d4 f6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B00_Nimzowitsch_Defense.md#_d4_)

## B01

- **Scandinavian Defence, Centre Counter Variation** — `1.e4 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Scandinavian.md#_d5_)
- **Scandinavian Defence, Lasker Variation** — `1.e4 d5 2.exd5 Qxd5 3.Nc3 Qa5 4.d4 Nf6 5.Nf3 Bg4 6.h3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Scandinavian.md#_Lasker_)
- **Scandinavian Defence** — `1.e4 d5 2.exd5 Qxd5 3.Nc3 Qa5 4.d4 Nf6 5.Nf3 Bf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Scandinavian.md#_Classical_)
- **Scandinavian Defence, Gruenfeld Variation** — `1.e4 d5 2.exd5 Qxd5 3.Nc3 Qa5 4.d4 Nf6 5.Nf3 Bf5 6.Ne5 c6 7.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Scandinavian.md#_Classical_)
- **Scandinavian Defence, Anderssen Counter-attack** — `1.e4 d5 2.exd5 Qxd5 3.Nc3 Qa5 4.d4 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Scandinavian.md#_Anderssen_)
- **Scandinavian Defence, Anderssen Counter-attack,  Orthodox Attack** — `1.e4 d5 2.exd5 Qxd5 3.Nc3 Qa5 4.d4 e5 5.dxe5 Bb4 6.Bd2 Nc6 7.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Scandinavian.md#_Anderssen_)
- **Scandinavian Defence, Anderssen Counter-attack,  Goteborg System** — `1.e4 d5 2.exd5 Qxd5 3.Nc3 Qa5 4.d4 e5 5.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Scandinavian.md#_Anderssen_)
- **Scandinavian Defence, Anderssen Counter-attack,  Collijn Variation** — `1.e4 d5 2.exd5 Qxd5 3.Nc3 Qa5 4.d4 e5 5.Nf3 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Scandinavian.md#_Anderssen_)
- **Scandinavian Defence, Mieses-Kotrvc Gambit** — `1.e4 d5 2.exd5 Qxd5 3.Nc3 Qa5 4.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Scandinavian.md#_Qa5_d4_) — live-tagged the *Leonhardt Gambit*
- **Scandinavian Defence, Pytel-Wade Variation** — `1.e4 d5 2.exd5 Qxd5 3.Nc3 Qd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Scandinavian.md#_Qxd5_Nc3_) — the card's own name for this position is the *Gubinsky-Melts Defense*, a real name divergence from `eco.md`
- **Scandinavian Defence** — `1.e4 d5 2.exd5 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Modern.md#_Nf6_)
- **Scandinavian Defence, Icelandic Gambit** — `1.e4 d5 2.exd5 Nf6 3.c4 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Modern.md#_Modern_alt_) — live-tagged the *Icelandic-Palme Gambit*
- **Scandinavian Defence, Gambit** — `1.e4 d5 2.exd5 Nf6 3.c4 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Modern.md#_Modern_alt_) — live-tagged the *Panov Transfer*
- **Scandinavian Defence** — `1.e4 d5 2.exd5 Nf6 3.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Modern.md#_d4_)
- **Scandinavian Defence, Marshall Variation** — `1.e4 d5 2.exd5 Nf6 3.d4 Nxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Modern.md#_Marshall_)
- **Scandinavian Defence, Kiel Variation** — `1.e4 d5 2.exd5 Nf6 3.d4 Nxd5 4.c4 Nb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Modern.md#_Marshall_)
- **Scandinavian Defence, Richter Variation** — `1.e4 d5 2.exd5 Nf6 3.d4 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B01_Modern.md#_d4_)

## B02

- **Alekhine's Defence** — `1.e4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_initial_move_)
- **Alekhine's Defence, Scandinavian Variation** — `1.e4 Nf6 2.Nc3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_Nc3_) — live-verified untagged despite `eco.md`'s own name here
- **Alekhine's Defence, Spielmann Variation** — `1.e4 Nf6 2.Nc3 d5 3.e5 Nfd7 4.e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_Nc3_)
- **Alekhine's Defence, Maroczy Variation** — `1.e4 Nf6 2.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_initial_move_)
- **Alekhine's Defence, Krejcik Variation** — `1.e4 Nf6 2.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_initial_move_)
- **Alekhine's Defence, Mokele Mbembe (Buecker) Variation** — `1.e4 Nf6 2.e5 Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_e5_)
- **Alekhine's Defence, Brooklyn Defence** — `1.e4 Nf6 2.e5 Ng8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_e5_)
- **Alekhine's Defence** — `1.e4 Nf6 2.e5 Nd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_Nd5_)
- **Alekhine's Defence, Kmoch Variation** — `1.e4 Nf6 2.e5 Nd5 3.Bc4 Nb6 4.Bb3 c5 5.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_Nd5_)
- **Alekhine's Defence, Saemisch Attack** — `1.e4 Nf6 2.e5 Nd5 3.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_Saemisch_)
- **Alekhine's Defence, Welling Variation** — `1.e4 Nf6 2.e5 Nd5 3.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_Welling_)
- **Alekhine's Defence** — `1.e4 Nf6 2.e5 Nd5 3.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_c4_)
- **Alekhine's Defence, Steiner Variation** — `1.e4 Nf6 2.e5 Nd5 3.c4 Nb6 4.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_Steiner_)
- **Alekhine's Defence, Two Pawns' (Lasker's) Attack** — `1.e4 Nf6 2.e5 Nd5 3.c4 Nb6 4.c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_Lasker_) — Lichess separates this from the deeper Mikenas line as its own *Lasker Variation*
- **Alekhine's Defence, Two Pawns' Attack,  Mikenas Variation** — `1.e4 Nf6 2.e5 Nd5 3.c4 Nb6 4.c5 Nd5 5.Bc4 e6 6.Nc3 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_Lasker_)

## B03

- **Alekhine's Defence** — `1.e4 Nf6 2.e5 Nd5 3.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_d4_) — a genuine "wrong root code" bug found and fixed this batch: this position had been labelled B02 on its own card; now disclosed as live-B03 in place, per this repo's established root/next-code mismatch convention
- **Alekhine's Defence, O'Sullivan Gambit** — `1.e4 Nf6 2.e5 Nd5 3.d4 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B02_Alekhine_Defense.md#_d4_)
- **Alekhine's Defence** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_initial_move_)
- **Alekhine's Defence, Balogh Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_initial_move_)
- **Alekhine's Defence** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_c4_)
- **Alekhine's Defence, Exchange Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.c4 Nb6 5.exd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_Nb6_)
- **Alekhine's Defence, Exchange,  Karpov Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.c4 Nb6 5.exd6 cxd6 6.Nf3 g6 7.Be2 Bg7 8.O-O O-O 9.h3 Nc6 10.Nc3 Bf5 11.Bf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_Nb6_)
- **Alekhine's Defence, Four Pawns Attack** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.c4 Nb6 5.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_f4_)
- **Alekhine's Defence, Four Pawns Attack,  Korchnoi Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.c4 Nb6 5.f4 dxe5 6.fxe5 Bf5 7.Nc3 e6 8.Nf3 Be7 9.Be2 O-O 10.O-O f6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_fxe5_)
- **Alekhine's Defence, Four Pawns Attack,  6...Nc6** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.c4 Nb6 5.f4 dxe5 6.fxe5 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_Nc6_fpa_)
- **Alekhine's Defence, Four Pawns Attack,  Ilyin-Genevsky var.** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.c4 Nb6 5.f4 dxe5 6.fxe5 Nc6 7.Nf3 Bg4 8.e6 fxe6 9.c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_Be3_fpa_)
- **Alekhine's Defence, Four Pawns Attack,  7.Be3** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.c4 Nb6 5.f4 dxe5 6.fxe5 Nc6 7.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_Be3_fpa_)
- **Alekhine's Defence, Four Pawns Attack,  Tartakower Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.c4 Nb6 5.f4 dxe5 6.fxe5 Nc6 7.Be3 Bf5 8.Nc3 e6 9.Nf3 Qd7 10.Be2 O-O-O 11.O-O Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_Be3_fpa_)
- **Alekhine's Defence, Four Pawns Attack,  Planinc Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.c4 Nb6 5.f4 g5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_fxe5_)
- **Alekhine's Defence, Four Pawns Attack,  Fianchetto Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.c4 Nb6 5.f4 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_fxe5_)
- **Alekhine's Defence, Four Pawns Attack,  Trifunovic Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.c4 Nb6 5.f4 Bf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B03_Alekhine_Defense.md#_fxe5_)

## B04

- **Alekhine's Defence, Modern Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B04_Alekhine_Modern_Variation.md#_initial_move_)
- **Alekhine's Defence, Modern,  Larsen Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Nf3 dxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B04_Alekhine_Modern_Variation.md#_dxe5_)
- **Alekhine's Defence, Modern,  Schmid Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Nf3 Nb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B04_Alekhine_Modern_Variation.md#_initial_move_)
- **Alekhine's Defence, Modern,  Fianchetto Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Nf3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B04_Alekhine_Modern_Variation.md#_g6_)
- **Alekhine's Defence, Modern,  Keres Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Nf3 g6 5.Bc4 Nb6 6.Bb3 Bg7 7.a4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B04_Alekhine_Modern_Variation.md#_g6_)

## B05

- **Alekhine's Defence, Modern Variation,  4...Bg4** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Nf3 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B05_Alekhine_Modern_Bg4.md#_initial_move_)
- **Alekhine's Defence, Modern,  Flohr Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Nf3 Bg4 5.Be2 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B05_Alekhine_Modern_Bg4.md#_Be2_)
- **Alekhine's Defence, Modern,  Panov Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Nf3 Bg4 5.h3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B05_Alekhine_Modern_Bg4.md#_initial_move_)
- **Alekhine's Defence, Modern,  Alekhine Variation** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Nf3 Bg4 5.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B05_Alekhine_Modern_Bg4.md#_initial_move_)
- **Alekhine's Defence, Modern,  Vitolins Attack** — `1.e4 Nf6 2.e5 Nd5 3.d4 d6 4.Nf3 Bg4 5.c4 Nb6 6.d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B05_Alekhine_Modern_Bg4.md#_initial_move_)

## B06

- **Robatsch Defence, Modern** — `1.e4 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B06_Modern_Defense.md#_initial_move_)
- **Norwegian Defence** — `1.e4 g6 2.d4 Nf6 3.e5 Nh5 4.g4 Ng7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B06_Modern_Defense.md#_d4_)
- **Robatsch Defence** — `1.e4 g6 2.d4 Bg7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B06_Modern_Defense.md#_Bg7_)
- **Robatsch Defence, three Pawns Attack** — `1.e4 g6 2.d4 Bg7 3.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B06_Modern_Defense.md#_f4_TPA_)
- **Robatsch Defence** — `1.e4 g6 2.d4 Bg7 3.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B06_Modern_Defense.md#_Nc3_)
- **Robatsch Defence, Gurgenidze Variation** — `1.e4 g6 2.d4 Bg7 3.Nc3 c6 4.f4 d5 5.e5 h5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B06_Modern_Defense.md#_Nc3_) — `eco.md` spells it *Gurgenidze Defense*
- **Robatsch Defence** — `1.e4 g6 2.d4 Bg7 3.Nc3 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B06_Modern_Defense.md#_d6_)
- **Robatsch Defence, Two Knights Variation** — `1.e4 g6 2.d4 Bg7 3.Nc3 d6 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B06_Modern_Defense.md#_Nf3_TKV_)
- **Robatsch Defence, Two Knights,  Suttles Variation** — `1.e4 g6 2.d4 Bg7 3.Nc3 d6 4.Nf3 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B06_Modern_Defense.md#_Nf3_TKV_)
- **Robatsch Defence, Pseudo-Austrian Attack** — `1.e4 g6 2.d4 Bg7 3.Nc3 d6 4.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B06_Modern_Defense.md#_f4_PAA_)

## B07

- **Pirc Defence** — `1.e4 d6 2.d4 Nf6 3.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B07_Pirc_Defense.md#_Nc3_)
- **Pirc Defence, Ufimtsev-Pytel Variation** — `1.e4 d6 2.d4 Nf6 3.Nc3 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B07_Pirc_Defense.md#_c6_) — live-tagged the *Czech Defense*, a real name divergence
- **Pirc Defence** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B07_Pirc_Defense.md#_g6_)
- **Pirc Defence, 150 Attack** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.Be3 c6 5.Qd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B07_Pirc_Defense.md#_Be3_)
- **Pirc Defence, Sveshnikov System** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B07_Pirc_Defense.md#_g6_) — a genuine zero-coverage gap found and fixed this batch
- **Pirc Defence, Holmov System** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B07_Pirc_Defense.md#_g6_) — live spells it *Kholmov System*, a minor spelling divergence; found and fixed this batch
- **Pirc Defence, Byrne Variation** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B07_Pirc_Defense.md#_g6_) — found and fixed this batch
- **Pirc Defence** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B07_Pirc_Defense.md#_g6_) — found and fixed this batch, untagged at this bare ply
- **Pirc Defence, Chinese Variation** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.Be2 Bg7 5.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B07_Pirc_Defense.md#_g6_) — found and fixed this batch
- **Pirc Defence, Bayonet Attack** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.Be2 Bg7 5.h4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B07_Pirc_Defense.md#_g6_) — found and fixed this batch
- **Robatsch Defence, Geller's System** — `1.e4 g6 2.d4 Bg7 3.Nf3 d6 4.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B07_Pirc_Defense.md#_g6_)

## B08

- **Pirc Defence, Classical System** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B08_Pirc_Classical_System.md#_initial_move_)
- **Pirc Defence, Classical System** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.Nf3 Bg7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B08_Pirc_Classical_System.md#_Bg7_)
- **Pirc Defence, Classical System,  h3 System** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.Nf3 Bg7 5.h3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B08_Pirc_Classical_System.md#_h3_) — live-tagged the *Schlechter Variation*
- **Pirc Defence, Classical System,  5.Be2** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.Nf3 Bg7 5.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B08_Pirc_Classical_System.md#_Be2_) — live-tagged the *Quiet System*

## B09

- **Pirc Defence, Austrian Attack** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B09_Pirc_Austrian_Attack.md#_initial_move_)
- **Pirc Defence, Austrian Attack** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.f4 Bg7 5.Nf3 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B09_Pirc_Austrian_Attack.md#_Nf3_)
- **Pirc Defence, Austrian Attack,  6.e5** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.f4 Bg7 5.Nf3 O-O 6.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B09_Pirc_Austrian_Attack.md#_e5_) — live-tagged the *Unzicker Attack*
- **Pirc Defence, Austrian Attack,  6.Be3** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.f4 Bg7 5.Nf3 O-O 6.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B09_Pirc_Austrian_Attack.md#_Be3_) — live-tagged the *Kurajica Variation*
- **Pirc Defence, Austrian Attack,  6.Bd3** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.f4 Bg7 5.Nf3 O-O 6.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B09_Pirc_Austrian_Attack.md#_Bd3_) — live-tagged the *Weiss Variation*
- **Pirc Defence, Austrian Attack,  Dragon formation** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.f4 Bg7 5.Nf3 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B09_Pirc_Austrian_Attack.md#_Nf3_)
- **Pirc Defence, Austrian Attack,  Ljubojevic Variation** — `1.e4 d6 2.d4 Nf6 3.Nc3 g6 4.f4 Bg7 5.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B09_Pirc_Austrian_Attack.md#_Bg7_)

## B10

- **Caro-Kann Defence** — `1.e4 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B10_Caro_Kann.md#_initial_move_)
- **Caro-Kann Defence, Hillbilly Attack** — `1.e4 c6 2.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B10_Caro_Kann.md)
- **Caro-Kann Defence, Anti-Caro-Kann Defence** — `1.e4 c6 2.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B10_Caro_Kann.md)
- **Caro-Kann Defence, Anti-Anti-Caro-Kann Defence** — `1.e4 c6 2.c4 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B10_Caro_Kann.md)
- **Caro-Kann Defence, Closed Variation** — `1.e4 c6 2.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B10_Caro_Kann.md)
- **Caro-Kann Defence** — `1.e4 c6 2.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B10_Caro_Kann.md#_Nc3_)
- **Caro-Kann Defence, Goldman Variation** — `1.e4 c6 2.Nc3 d5 3.Qf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B10_Caro_Kann.md)
- **Caro-Kann Defence, Two Knights Variation** — `1.e4 c6 2.Nc3 d5 3.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B10_Caro_Kann.md#_Nf3_)

## B11

- **Caro-Kann Defence, Two Knights,  3...Bg4** — `1.e4 c6 2.Nc3 d5 3.Nf3 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B11_Caro_Kann_Two_Knights_Mindeno.md#_initial_move_)

## B12

- **Caro-Kann Defence** — `1.e4 c6 2.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B12_Caro_Kann.md#_initial_move_)
- **Caro-Kann Defence, De Bruycker Defence** — `1.e4 c6 2.d4 Na6 3.Nc3 Nc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B12_Caro_Kann.md)
- **Caro-Kann Defence, Caro-Masi Defence** — `1.e4 c6 2.d4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B12_Caro_Kann.md)
- **Caro-Kann Defence** — `1.e4 c6 2.d4 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B12_Caro_Kann.md#_d5_)
- **Caro-Kann Defence, Tartakower Variation** — `1.e4 c6 2.d4 d5 3.f3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B12_Caro_Kann.md#_d5_)
- **Caro-Kann Defence, 3.Nd2** — `1.e4 c6 2.d4 d5 3.Nd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B12_Caro_Kann.md#_Nd2_)
- **Caro-Kann Defence, Edinburgh Variation** — `1.e4 c6 2.d4 d5 3.Nd2 Qb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B12_Caro_Kann.md#_Nd2_)
- **Caro-Kann Defence, Advance Variation** — `1.e4 c6 2.d4 d5 3.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B12_Caro_Kann.md#_e5_)
- **Caro-Kann Defence, Advance Variation,  Short Variation** — `1.e4 c6 2.d4 d5 3.e5 Bf5 4.c3 e6 5.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B12_Caro_Kann.md#_e5_)

## B13

- **Caro-Kann Defence, Exchange Variation** — `1.e4 c6 2.d4 d5 3.exd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B13_Caro_Kann_Exchange_Panov.md#_initial_move_)
- **Caro-Kann Defence, Exchange Variation,  Rubinstein Variation** — `1.e4 c6 2.d4 d5 3.exd5 cxd5 4.Bd3 Nc6 5.c3 Nf6 6.Bf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B13_Caro_Kann_Exchange_Panov.md#_Bf4_)
- **Caro-Kann Defence, Panov-Botvinnik Attack** — `1.e4 c6 2.d4 d5 3.exd5 cxd5 4.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B13_Caro_Kann_Exchange_Panov.md#_c4_)
- **Caro-Kann Defence, Panov-Botvinnik Attack,  Gunderam Attack** — `1.e4 c6 2.d4 d5 3.exd5 cxd5 4.c4 Nf6 5.c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B13_Caro_Kann_Exchange_Panov.md#_c4_)
- **Caro-Kann Defence, Panov-Botvinnik Attack** — `1.e4 c6 2.d4 d5 3.exd5 cxd5 4.c4 Nf6 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B13_Caro_Kann_Exchange_Panov.md#_Nc3_)
- **Caro-Kann Defence, Panov-Botvinnik Attack,  Herzog Defence** — `1.e4 c6 2.d4 d5 3.exd5 cxd5 4.c4 Nf6 5.Nc3 Nc6 6.Bg5 dxc4 7.d5 Na5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B13_Caro_Kann_Exchange_Panov.md#_Herzog_)
- **Caro-Kann Defence, Panov-Botvinnik Attack,  normal Variation** — `1.e4 c6 2.d4 d5 3.exd5 cxd5 4.c4 Nf6 5.Nc3 Nc6 6.Bg5 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B13_Caro_Kann_Exchange_Panov.md#_Carlsbad_)
- **Caro-Kann Defence, Panov-Botvinnik Attack,  Czerniak Variation** — `1.e4 c6 2.d4 d5 3.exd5 cxd5 4.c4 Nf6 5.Nc3 Nc6 6.Bg5 Qa5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B13_Caro_Kann_Exchange_Panov.md#_Czerniak_)
- **Caro-Kann Defence, Panov-Botvinnik Attack,  Reifir (Spielmann) Variation** — `1.e4 c6 2.d4 d5 3.exd5 cxd5 4.c4 Nf6 5.Nc3 Nc6 6.Bg5 Qb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B13_Caro_Kann_Exchange_Panov.md#_Reifir_)

## B14

- **Caro-Kann Defence, Panov-Botvinnik Attack,  5...e6** — `1.e4 c6 2.d4 d5 3.exd5 cxd5 4.c4 Nf6 5.Nc3 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B14_Caro_Kann_Panov_Attack.md#_initial_move_)
- **Caro-Kann Defence, Panov-Botvinnik Attack,  5...g6** — `1.e4 c6 2.d4 d5 3.exd5 cxd5 4.c4 Nf6 5.Nc3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B14_Caro_Kann_Panov_Attack.md#_g6_)

## B15

- **Caro-Kann Defence** — `1.e4 c6 2.d4 d5 3.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B15_Caro_Kann_Classical_Modern.md#_initial_move_)
- **Caro-Kann Defence, Gurgenidze Counter-attack** — `1.e4 c6 2.d4 d5 3.Nc3 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B15_Caro_Kann_Classical_Modern.md)
- **Caro-Kann Defence, Gurgenidze System** — `1.e4 c6 2.d4 d5 3.Nc3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B15_Caro_Kann_Classical_Modern.md)
- **Caro-Kann Defence, Rasa-Studier Gambit** — `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.f3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B15_Caro_Kann_Classical_Modern.md#_dxe4_)
- **Caro-Kann Defence** — `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B15_Caro_Kann_Classical_Modern.md#_dxe4_)
- **Caro-Kann Defence, Alekhine Gambit** — `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nf6 5.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B15_Caro_Kann_Classical_Modern.md#_Nf6_)
- **Caro-Kann Defence, Tartakower Variation** — `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nf6 5.Nxf6 exf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B15_Caro_Kann_Classical_Modern.md#_exf6_)
- **Caro-Kann Defence, Forgacs Variation** — `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nf6 5.Nxf6 exf6 6.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B15_Caro_Kann_Classical_Modern.md#_exf6_)

## B16

- **Caro-Kann Defence, Bronstein-Larsen Variation** — `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nf6 5.Nxf6 gxf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B16_Caro_Kann_Bronstein_Larsen.md#_initial_move_)

## B17

- **Caro-Kann Defence, Steinitz Variation** — `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B17_Caro_Kann_Karpov_Variation.md#_initial_move_)

## B18

- **Caro-Kann Defence, Classical Variation** — `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B18_Caro_Kann_Classical_Variation.md#_initial_move_)
- **Caro-Kann Defence, Classical Variation,  Flohr Variation** — `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.Nh3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B18_Caro_Kann_Classical_Variation.md#_Nh3_)
- **Caro-Kann Defence, Classical Variation,  Maroczy Attack** — `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B18_Caro_Kann_Classical_Variation.md#_Bg6_)
- **Caro-Kann Defence, Classical Variation,  6.h4** — `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B18_Caro_Kann_Classical_Variation.md#_h4_)

## B19

- **Caro-Kann Defence, Classical Variation,  7...Nd7** — `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B19_Caro_Kann_Spassky_Variation.md#_initial_move_)
- **Caro-Kann Defence, Classical Variation,  Spassky Variation** — `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7 8.h5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B19_Caro_Kann_Spassky_Variation.md#_h5_)

## B20

- **Sicilian Defence** — `1.e4 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B20_Sicilian.md#_initial_move_)
- **Sicilian Defence, Gloria Variation** — `1.e4 c5 2.c4 d6 3.Nc3 Nc6 4.g3 h5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B20_Sicilian.md#_Gloria_)
- **Sicilian Defence, Steinitz Variation** — `1.e4 c5 2.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B20_Sicilian.md#_g3_)
- **Sicilian Defence, Wing Gambit** — `1.e4 c5 2.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B20_Sicilian.md#_b4_)
- **Sicilian Defence, Wing Gambit,  Santasiere Variation** — `1.e4 c5 2.b4 cxb4 3.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B20_Sicilian.md#_b4_)
- **Sicilian Defence, Wing Gambit,  Marshall Variation** — `1.e4 c5 2.b4 cxb4 3.a3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B20_Sicilian.md#_b4_)
- **Sicilian Defence, Wing Gambit,  Marienbad Variation** — `1.e4 c5 2.b4 cxb4 3.a3 d5 4.exd5 Qxd5 5.Bb2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B20_Sicilian.md#_b4_)
- **Sicilian Defence, Wing Gambit,  Carlsbad Variation** — `1.e4 c5 2.b4 cxb4 3.a3 bxa3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B20_Sicilian.md#_b4_)
- **Sicilian Defence, Keres Variation (2.Ne2)** — `1.e4 c5 2.Ne2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B20_Sicilian.md#_Ne2_)

## B21

- **Sicilian Defence, Grand Prix Attack** — `1.e4 c5 2.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B21_Sicilian_McDonnell_Smith_Morra.md#_initial_move_)
- **Sicilian Defence, Smith-Morra Gambit** — `1.e4 c5 2.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B21_Sicilian_McDonnell_Smith_Morra.md#_d4_)
- **Sicilian Defence, Andreaschek Gambit** — `1.e4 c5 2.d4 cxd4 3.Nf3 e5 4.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B21_Sicilian_McDonnell_Smith_Morra.md#_c3_)
- **Sicilian Defence, Smith-Morra Gambit** — `1.e4 c5 2.d4 cxd4 3.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B21_Sicilian_McDonnell_Smith_Morra.md#_c3_)
- **Sicilian Defence, Smith-Morra Gambit,  Chicago Defence** — `1.e4 c5 2.d4 cxd4 3.c3 dxc3 4.Nxc3 Nc6 5.Nf3 d6 6.Bc4 e6 7.O-O a6 8.Qe2 b5 9.Bb3 Ra7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B21_Sicilian_McDonnell_Smith_Morra.md#_c3_)

## B22

- **Sicilian Defence, Alapin Variation** — `1.e4 c5 2.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B22_Sicilian_Alapin.md#_initial_move_)
- **Sicilian Defence, Alapin Variation,  Heidenfeld Variation** — `1.e4 c5 2.c3 Nf6 3.e5 Nd5 4.Nf3 Nc6 5.Na3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B22_Sicilian_Alapin.md#_Nf6_)

## B23

- **Sicilian Defence, Closed** — `1.e4 c5 2.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B23_Sicilian_Closed.md#_initial_move_)
- **Sicilian Defence, Closed,  Korchnoi Variation** — `1.e4 c5 2.Nc3 e6 3.g3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B23_Sicilian_Closed.md#_e6_)
- **Sicilian Defence, Closed,  2...Nc6** — `1.e4 c5 2.Nc3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B23_Sicilian_Closed.md#_Nc6_)
- **Sicilian Defence, Chameleon Variation** — `1.e4 c5 2.Nc3 Nc6 3.Nge2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B23_Sicilian_Closed.md#_Nge2_)
- **Sicilian Defence, Grand Prix Attack** — `1.e4 c5 2.Nc3 Nc6 3.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B23_Sicilian_Closed.md#_f4_)
- **Sicilian Defence, Grand Prix Attack,  Schofman Variation** — `1.e4 c5 2.Nc3 Nc6 3.f4 g6 4.Nf3 Bg7 5.Bc4 e6 6.f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B23_Sicilian_Closed.md#_f4_)

## B24

- **Sicilian Defence, Closed** — `1.e4 c5 2.Nc3 Nc6 3.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B24_Sicilian_Closed_g3.md#_initial_move_)
- **Sicilian Defence, Closed,  Smyslov Variation** — `1.e4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.d3 e6 6.Be3 Nd4 7.Nce2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B24_Sicilian_Closed_g3.md#_g6_)

## B25

- **Sicilian Defence, Closed** — `1.e4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.d3 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B25_Sicilian_Closed_d6.md#_initial_move_)
- **Sicilian Defence, Closed,  6.Ne2 e5 (Botvinnik)** — `1.e4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.d3 d6 6.Nge2 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B25_Sicilian_Closed_d6.md#_Nge2_)
- **Sicilian Defence, Closed,  6.f4** — `1.e4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.d3 d6 6.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B25_Sicilian_Closed_d6.md#_f4_)
- **Sicilian Defence, Closed,  6.f4 e5 (Botvinnik)** — `1.e4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.d3 d6 6.f4 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B25_Sicilian_Closed_d6.md#_f4_)

## B26

- **Sicilian Defence, Closed,  6.Be3** — `1.e4 c5 2.Nc3 Nc6 3.g3 g6 4.Bg2 Bg7 5.d3 d6 6.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B26_Sicilian_Closed_Be3.md#_initial_move_)

## B27

- **Sicilian Defence** — `1.e4 c5 2.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B27_Sicilian_Open.md#_initial_move_)
- **Sicilian Defence, Stiletto Variation** — `1.e4 c5 2.Nf3 Qa5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B27_Sicilian_Open.md)
- **Sicilian Defence, Quinteros Variation** — `1.e4 c5 2.Nf3 Qc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B27_Sicilian_Open.md)
- **Sicilian Defence, Katalimov Variation** — `1.e4 c5 2.Nf3 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B27_Sicilian_Open.md)
- **Sicilian Defence, Hungarian Variation** — `1.e4 c5 2.Nf3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B27_Sicilian_Open.md#_g6_)
- **Sicilian Defence, Acton extension** — `1.e4 c5 2.Nf3 g6 3.c4 Bh6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B27_Sicilian_Open.md#_g6_)

## B28

- **Sicilian Defence, O'Kelly Variation** — `1.e4 c5 2.Nf3 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B28_Sicilian_OKelly.md#_initial_move_)

## B29

- **Sicilian Defence, Nimzovich-Rubinstein Variation** — `1.e4 c5 2.Nf3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B29_Sicilian_Nimzovich_Rubinstein.md#_initial_move_)
- **Sicilian Defence, Nimzovich-Rubinstein Variation,  Rubinstein Counter-Gambit** — `1.e4 c5 2.Nf3 Nf6 3.e5 Nd5 4.Nc3 e6 5.Nxd5 exd5 6.d4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B29_Sicilian_Nimzovich_Rubinstein.md#_e5_)

## B30

- **Sicilian Defence** — `1.e4 c5 2.Nf3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B30_Sicilian_Nc6_Open.md#_initial_move_)
- **Sicilian Defence, Nimzovich-Rossolimo Attack (without ...d6)** — `1.e4 c5 2.Nf3 Nc6 3.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B30_Sicilian_Nc6_Open.md#_Bb5_)

## B31

- **Sicilian Defence, Nimzovich-Rossolimo Attack (with ...g6,  Without ...d6)** — `1.e4 c5 2.Nf3 Nc6 3.Bb5 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B31_Sicilian_Rossolimo_Fianchetto.md#_initial_move_)
- **Sicilian Defence, Nimzovich-Rossolimo Attack,  Gurgenidze Variation** — `1.e4 c5 2.Nf3 Nc6 3.Bb5 g6 4.O-O Bg7 5.Re1 e5 6.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B31_Sicilian_Rossolimo_Fianchetto.md#_Gurgenidze_)

## B32

- **Sicilian Defence** — `1.e4 c5 2.Nf3 Nc6 3.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B32_Sicilian_Open.md#_initial_move_)
- **Sicilian Defence, Flohr Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Qc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B32_Sicilian_Open.md#_Qc7_)
- **Sicilian Defence, Nimzovich Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B32_Sicilian_Open.md#_d5_)
- **Sicilian Defence, Labourdonnais-Loewenthal Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B32_Sicilian_Open.md#_e5_)
- **Sicilian Defence, Labourdonnais-Loewenthal Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 e5 5.Nb5 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B32_Sicilian_Open.md#_Kalashnikov_)

## B33

- **Sicilian Defence** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B33_Sicilian_Lasker_Pelikan.md#_initial_move_)
- **Sicilian Defence, Pelikan Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B33_Sicilian_Lasker_Pelikan.md#_e5_)
- **Sicilian Defence, Pelikan Variation,  Bird Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e5 6.Ndb5 d6 7.Bg5 a6 8.Na3 Be6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B33_Sicilian_Lasker_Pelikan.md#_Bird_)
- **Sicilian Defence, Pelikan Variation,  Chelyabinsk Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e5 6.Ndb5 d6 7.Bg5 a6 8.Na3 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B33_Sicilian_Lasker_Pelikan.md#_Sveshnikov_)
- **Sicilian Defence, Sveshnikov Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e5 6.Ndb5 d6 7.Bg5 a6 8.Na3 b5 9.Bxf6 gxf6 10.Nd5 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B33_Sicilian_Lasker_Pelikan.md#_Sveshnikov_)

## B34

- **Sicilian Defence, Accelerated Fianchetto,  Exchange Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nxc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B34_Sicilian_g6_Accelerated_Dragon.md#_Nxc6_)
- **Sicilian Defence, Accelerated Fianchetto,  Modern Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B34_Sicilian_g6_Accelerated_Dragon.md#_Nc3_)

## B35

- **Sicilian Defence, Accelerated Fianchetto,  Modern Variation With Bc4** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B35_Sicilian_Accelerated_Dragon_Bc4.md#_initial_move_)

## B36

- **Sicilian Defence, Accelerated Fianchetto,  Maroczy bind** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B36_Sicilian_Accelerated_Dragon_Maroczy.md#_initial_move_)
- **Sicilian Defence, Accelerated Fianchetto,  Gurgenidze Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Nxd4 7.Qxd4 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B36_Sicilian_Accelerated_Dragon_Maroczy.md#_Gurgenidze_)

## B37

- **Sicilian Defence, Accelerated Fianchetto,  Maroczy bind,  5...Bg7** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Bg7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B37_Sicilian_Accelerated_Dragon_Maroczy_Bg7.md#_initial_move_)
- **Sicilian Defence, Accelerated Fianchetto,  Simagin Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Bg7 6.Nc2 d6 7.Be2 Nh6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B37_Sicilian_Accelerated_Dragon_Maroczy_Bg7.md#_Nc2_)

## B38

- **Sicilian Defence, Accelerated Fianchetto,  Maroczy bind,  6.Be3** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Bg7 6.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B38_Sicilian_Accelerated_Dragon_Maroczy_Be3.md#_initial_move_)

## B39

- **Sicilian Defence, Accelerated Fianchetto,  Breyer Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Bg7 6.Be3 Nf6 7.Nc3 Ng4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B39_Sicilian_Accelerated_Dragon_Maroczy_Breyer.md#_initial_move_)

## B40

- **Sicilian Defence** — `1.e4 c5 2.Nf3 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B40_Sicilian_e6_Open.md#_initial_move_)
- **Sicilian Defence, Marshall Variation** — `1.e4 c5 2.Nf3 e6 3.d4 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B40_Sicilian_e6_Open.md#_Marshall_)
- **Sicilian Defence** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B40_Sicilian_e6_Open.md#_d4_)
- **Sicilian Defence, Anderssen Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B40_Sicilian_e6_Open.md#_Nf6_)
- **Sicilian Defence, Pin Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B40_Sicilian_e6_Open.md#_Pin_)
- **Sicilian Defence, Pin Variation,  Jaffe Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Bb4 6.Bd3 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B40_Sicilian_e6_Open.md#_Jaffe_)
- **Sicilian Defence, Pin Variation,  Koch Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Bb4 6.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B40_Sicilian_e6_Open.md#_Koch_)

## B41

- **Sicilian Defence, Kan Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B41_Sicilian_Kan_Variation.md#_initial_move_)
- **Sicilian Defence, Kan Variation,  Maroczy bind** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 a6 5.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B41_Sicilian_Kan_Variation.md#_c4_)
- **Sicilian Defence, Kan Variation,  Maroczy bind,  Bronstein Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 a6 5.c4 Nf6 6.Nc3 Bb4 7.Bd3 Nc6 8.Bc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B41_Sicilian_Kan_Variation.md#_c4_)

## B42

- **Sicilian Defence, Kan Variation,  5.Bd3** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 a6 5.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B42_Sicilian_Kan_Modern_Variation.md#_initial_move_)
- **Sicilian Defence, Kan Variation,  Gipslis Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 a6 5.Bd3 Nf6 6.O-O d6 7.c4 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B42_Sicilian_Kan_Modern_Variation.md#_initial_move_)
- **Sicilian Defence, Kan Variation,  Polugaievsky Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 a6 5.Bd3 Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B42_Sicilian_Kan_Modern_Variation.md#_initial_move_)
- **Sicilian Defence, Kan Variation,  Swiss cheese Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 a6 5.Bd3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B42_Sicilian_Kan_Modern_Variation.md#_initial_move_)

## B43

- **Sicilian Defence, Kan Variation,  5.Nc3** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 a6 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B43_Sicilian_Kan_Knight_Variation.md#_initial_move_)

## B44

- **Sicilian Defence** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B44_Sicilian_Taimanov_Szen.md#_initial_move_)
- **Sicilian Defence, Szen Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B44_Sicilian_Taimanov_Szen.md#_Nb5_)
- **Sicilian Defence, Szen Variation,  Hedgehog Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nb5 d6 6.c4 Nf6 7.N1c3 a6 8.Na3 Be7 9.Be2 O-O 10.O-O b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B44_Sicilian_Taimanov_Szen.md#_Nb5_)
- **Sicilian Defence, Szen Variation,  Dely-Kasparov Gambit** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nb5 d6 6.c4 Nf6 7.N1c3 a6 8.Na3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B44_Sicilian_Taimanov_Szen.md#_Nb5_)

## B45

- **Sicilian Defence, Taimanov Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B45_Sicilian_Taimanov_Nc3.md#_initial_move_)
- **Sicilian Defence, Taimanov Variation,  American Attack** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 Nf6 6.Ndb5 Bb4 7.Nd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B45_Sicilian_Taimanov_Nc3.md#_Nf6_)

## B46

- **Sicilian Defence, Taimanov Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B46_Sicilian_Taimanov_a6.md#_initial_move_)

## B47

- **Sicilian Defence, Taimanov Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 Qc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B47_Sicilian_Taimanov_Bastrikov.md#_initial_move_)

## B48

- **Sicilian Defence, Taimanov Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 Qc7 6.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B48_Sicilian_Taimanov_English_Attack.md#_initial_move_)

## B49

- **Sicilian Defence, Taimanov Variation** — `1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 Qc7 6.Be3 a6 7.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B49_Sicilian_Taimanov_a6_Be2.md#_initial_move_)

## B50

- **Sicilian Defence** — `1.e4 c5 2.Nf3 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B50_Sicilian_d6_Open.md#_initial_move_)
- **Sicilian Defence, Wing Gambit,  Deferred** — `1.e4 c5 2.Nf3 d6 3.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B50_Sicilian_d6_Open.md#_b4_)

## B51

- **Sicilian Defence, Canal-Sokolsky Attack** — `1.e4 c5 2.Nf3 d6 3.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B51_Sicilian_Moscow_Variation.md#_initial_move_)

## B52

- **Sicilian Defence, Canal-Sokolsky Attack,  3...Bd7** — `1.e4 c5 2.Nf3 d6 3.Bb5 Bd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B52_Sicilian_Moscow_Bd7.md#_initial_move_)
- **Sicilian Defence, Canal-Sokolsky Attack,  Bronstein Gambit** — `1.e4 c5 2.Nf3 d6 3.Bb5 Bd7 4.Bxd7 Qxd7 5.O-O Nc6 6.c3 Nf6 7.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B52_Sicilian_Moscow_Bd7.md#_OO_)
- **Sicilian Defence, Canal-Sokolsky Attack,  Sokolsky Variation** — `1.e4 c5 2.Nf3 d6 3.Bb5 Bd7 4.Bxd7 Qxd7 5.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B52_Sicilian_Moscow_Bd7.md#_c4_)

## B53

- **Sicilian Defence, Chekhover Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Qxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B53_Sicilian_Chekhover.md#_initial_move_)
- **Sicilian Defence, Chekhover Variation,  Zaitsev Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Qxd4 Nc6 5.Bb5 Qd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B53_Sicilian_Chekhover.md#_Zaitsev_)

## B54

- **Sicilian Defence** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B54_Sicilian_d6_Modern_Main_Line.md#_initial_move_)
- **Sicilian Defence, Prins Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.f3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B54_Sicilian_d6_Modern_Main_Line.md#_Nf6_)

## B55

- **Sicilian Defence, Prins Variation,  Venice Attack** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.f3 e5 6.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B55_Sicilian_Prins_Venice_Attack.md#_initial_move_)

## B56

- **Sicilian Defence** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B56_Sicilian_Classical_Variation.md#_initial_move_)
- **Sicilian Defence, Venice Attack** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e5 6.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B56_Sicilian_Classical_Variation.md#_e5_)
- **Sicilian Defence** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B56_Sicilian_Classical_Variation.md#_Nc6_)

## B57

- **Sicilian Defence, Sozin** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B57_Sicilian_Sozin_Attack.md#_initial_move_)
- **Sicilian Defence, Magnus Smith trap** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bc4 g6 7.Nxc6 bxc6 8.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B57_Sicilian_Sozin_Attack.md#_MagnusSmith_)
- **Sicilian Defence, Sozin,  Benko Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bc4 Qb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B57_Sicilian_Sozin_Attack.md#_Qb6_)

## B58

- **Sicilian Defence, Classical** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 d6 6.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B58_Sicilian_Classical_System.md#_initial_move_)
- **Sicilian Defence, Boleslavsky Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 d6 6.Be2 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B58_Sicilian_Classical_System.md#_e5_)
- **Sicilian Defence, Boleslavsky Variation,  Louma Variation** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 d6 6.Be2 e5 7.Nxc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B58_Sicilian_Classical_System.md#_Louma_)

## B59

- **Sicilian Defence, Boleslavsky Variation,  7.Nb3** — `1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 d6 6.Be2 e5 7.Nb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B59_Sicilian_Boleslavsky_Nb3.md#_initial_move_)

## B60

- **Sicilian Defence, Richter-Rauzer** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B60_Sicilian_Richter_Rauzer.md#_initial_move_)
- **Sicilian Defence, Richter-Rauzer,  Bondarevsky Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B60_Sicilian_Richter_Rauzer.md#_g6_)
- **Sicilian Defence, Richter-Rauzer,  Larsen Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 Bd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B60_Sicilian_Richter_Rauzer.md#_Bd7_)

## B61

- **Sicilian Defence, Richter-Rauzer,  Larsen Variation,  7.Qd2** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 Bd7 7.Qd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B61_Sicilian_Richter_Rauzer_Larsen.md#_initial_move_)

## B62

- **Sicilian Defence, Richter-Rauzer,  6...e6** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B62_Sicilian_Richter_Rauzer_e6.md#_initial_move_)
- **Sicilian Defence, Richter-Rauzer,  Podvebrady Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Nb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B62_Sicilian_Richter_Rauzer_e6.md#_initial_move_)
- **Sicilian Defence, Richter-Rauzer,  Margate Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B62_Sicilian_Richter_Rauzer_e6.md#_Margate_)
- **Sicilian Defence, Richter-Rauzer,  Richter Attack** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Nxc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B62_Sicilian_Richter_Rauzer_e6.md#_initial_move_)
- **Sicilian Defence, Richter-Rauzer,  Keres Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B62_Sicilian_Richter_Rauzer_e6.md#_Keres_)

## B63

- **Sicilian Defence, Richter-Rauzer,  Rauzer Attack** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B63_Sicilian_Richter_Rauzer_Traditional.md#_initial_move_)
- **Sicilian Defence, Richter-Rauzer,  Rauzer Attack,  7...Be7** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B63_Sicilian_Richter_Rauzer_Traditional.md#_Be7_)

## B64

- **Sicilian Defence, Richter-Rauzer,  Rauzer Attack,  7...Be7 Defence,  9.f4** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B64_Sicilian_Richter_Rauzer_f4.md#_initial_move_)
- **Sicilian Defence, Richter-Rauzer,  Rauzer Attack,  Geller Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B64_Sicilian_Richter_Rauzer_f4.md#_Geller_)

## B65

- **Sicilian Defence, Richter-Rauzer,  Rauzer Attack,  7...Be7 Defence,  9...Nxd4** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4 Nxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B65_Sicilian_Richter_Rauzer_Nxd4.md#_initial_move_)
- **Sicilian Defence, Richter-Rauzer,  Rauzer Attack,  7...Be7 Defence,  9...Nxd4** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4 Nxd4 10.Qxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B65_Sicilian_Richter_Rauzer_Nxd4.md#_initial_move_)

## B66

- **Sicilian Defence, Richter-Rauzer,  Rauzer Attack,  7...a6** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B66_Sicilian_Richter_Rauzer_Neo_Modern.md#_initial_move_)

## B67

- **Sicilian Defence, Richter-Rauzer,  Rauzer Attack,  7...a6 Defence,  8...Bd7** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 a6 8.O-O-O Bd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B67_Sicilian_Richter_Rauzer_a6_Bd7.md#_initial_move_)

## B68

- **Sicilian Defence, Richter-Rauzer,  Rauzer Attack,  7...a6 Defence,  9...Be7** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 a6 8.O-O-O Bd7 9.f4 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B68_Sicilian_Richter_Rauzer_a6_f4.md#_initial_move_)

## B69

- **Sicilian Defence, Richter-Rauzer,  Rauzer Attack,  7...a6 Defence,  11.Bxf6** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 a6 8.O-O-O Bd7 9.f4 Be7 10.Nf3 b5 11.Bxf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B69_Sicilian_Richter_Rauzer_Bxf6.md#_initial_move_)

## B70

- **Sicilian Defence, Dragon Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B70_Sicilian_Dragon.md#_initial_move_)

## B71

- **Sicilian Defence, Dragon Variation,  Levenfish Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B71_Sicilian_Dragon_Levenfish.md#_initial_move_)
- **Sicilian Defence, Dragon Variation,  Levenfish; Flohr Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.f4 Nbd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B71_Sicilian_Dragon_Levenfish.md#_Flohr_)

## B72

- **Sicilian Defence, Dragon Variation,  6.Be3** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B72_Sicilian_Dragon_Be3.md#_initial_move_)
- **Sicilian Defence, Dragon Variation,  Classical Attack** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B72_Sicilian_Dragon_Be3.md#_Be2_)
- **Sicilian Defence, Dragon Variation,  Classical Attack,  Amsterdam Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Be2 Nc6 8.Qd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B72_Sicilian_Dragon_Be3.md#_Amsterdam_)
- **Sicilian Defence, Dragon Variation,  Classical Attack,  Grigoriev Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Be2 Nc6 8.Qd2 O-O 9.O-O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B72_Sicilian_Dragon_Be3.md#_Grigoriev_)
- **Sicilian Defence, Dragon Variation,  Classical Attack,  Nottingham Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Be2 Nc6 8.Nb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B72_Sicilian_Dragon_Be3.md#_Nottingham_)

## B73

- **Sicilian Defence, Dragon Variation,  Classical Attack,  8.O-O** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Be2 Nc6 8.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B73_Sicilian_Dragon_Classical_OO.md#_initial_move_)
- **Sicilian Defence, Dragon Variation,  Classical Attack,  Zollner Gambit** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Be2 Nc6 8.O-O O-O 9.f4 Qb6 10.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B73_Sicilian_Dragon_Classical_OO.md#_afterOO_)
- **Sicilian Defence, Dragon Variation,  Classical Attack,  Richter Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Be2 Nc6 8.O-O O-O 9.Qd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B73_Sicilian_Dragon_Classical_OO.md#_afterOO_)

## B74

- **Sicilian Defence, Dragon Variation,  Classical Attack,  9.Nb3** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Be2 Nc6 8.O-O O-O 9.Nb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B74_Sicilian_Dragon_Classical_Nb3.md#_initial_move_)
- **Sicilian Defence, Dragon Variation,  Classical Attack,  Stockholm Attack** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Be2 Nc6 8.O-O O-O 9.Nb3 Be6 10.f4 Na5 11.f5 Bc4 12.Nxa5 Bxe2 13.Qxe2 Qxa5 14.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B74_Sicilian_Dragon_Classical_Nb3.md#_afterBe6_)
- **Sicilian Defence, Dragon Variation,  Classical Attack,  Spielmann Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Be2 Nc6 8.O-O O-O 9.Nb3 Be6 10.f4 Na5 11.f5 Bc4 12.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B74_Sicilian_Dragon_Classical_Nb3.md#_afterBe6_)
- **Sicilian Defence, Dragon Variation,  Classical Attack,  Bernard Defence** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Be2 Nc6 8.O-O O-O 9.Nb3 Be6 10.f4 Na5 11.f5 Bc4 12.Bd3 Bxd3 13.cxd3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B74_Sicilian_Dragon_Classical_Nb3.md#_afterBe6_)
- **Sicilian Defence, Dragon Variation,  Classical Attack,  Reti-Tartakower Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Be2 Nc6 8.O-O O-O 9.Nb3 Be6 10.f4 Qc8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B74_Sicilian_Dragon_Classical_Nb3.md#_afterBe6_)
- **Sicilian Defence, Dragon Variation,  Classical Attack,  Alekhine Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.Be2 Nc6 8.O-O O-O 9.Nb3 a5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B74_Sicilian_Dragon_Classical_Nb3.md#_initial_move_)

## B75

- **Sicilian Defence, Dragon Variation,  Yugoslav Attack** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B75_Sicilian_Dragon_Yugoslav.md#_initial_move_)

## B76

- **Sicilian Defence, Dragon Variation,  Yugoslav Attack,  7...O-O** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B76_Sicilian_Dragon_Yugoslav_OO.md#_initial_move_)
- **Sicilian Defence, Dragon Variation,  Yugoslav Attack,  Rauser Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.O-O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B76_Sicilian_Dragon_Yugoslav_OO.md#_Rauser_)

## B77

- **Sicilian Defence, Dragon Variation,  Yugoslav Attack,  9.Bc4** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B77_Sicilian_Dragon_Yugoslav_Bc4.md#_initial_move_)
- **Sicilian Defence, Dragon Variation,  Yugoslav Attack,  Byrne Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 a5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B77_Sicilian_Dragon_Yugoslav_Bc4.md#_Byrne_)
- **Sicilian Defence, Dragon Variation,  Yugoslav Attack,  9...Bd7** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B77_Sicilian_Dragon_Yugoslav_Bc4.md#_Bd7_)

## B78

- **Sicilian Defence, Dragon Variation,  Yugoslav Attack,  10.O-O-O** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7 10.O-O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B78_Sicilian_Dragon_Yugoslav_OOO.md#_initial_move_)

## B79

- **Sicilian Defence, Dragon Variation,  Yugoslav Attack,  12.h4** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7 10.O-O-O Qa5 11.Bb3 Rfc8 12.h4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B79_Sicilian_Dragon_Yugoslav_h4.md#_initial_move_)

## B80

- **Sicilian Defence, Scheveningen Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B80_Sicilian_Scheveningen.md#_initial_move_)
- **Sicilian Defence, Scheveningen Variation,  English Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be3 a6 7.Qd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B80_Sicilian_Scheveningen.md#_Be3_)
- **Sicilian Defence, Scheveningen Variation,  Vitolins Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B80_Sicilian_Scheveningen.md#_initial_move_)
- **Sicilian Defence, Scheveningen Variation,  Fianchetto Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B80_Sicilian_Scheveningen.md#_initial_move_)

## B81

- **Sicilian Defence, Scheveningen Variation,  Keres Attack** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B81_Sicilian_Scheveningen_Keres.md#_initial_move_)

## B82

- **Sicilian Defence, Scheveningen Variation,  6.f4** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B82_Sicilian_Scheveningen_f4.md#_initial_move_)
- **Sicilian Defence, Scheveningen Variation,  Tal Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.f4 Nc6 7.Be3 Be7 8.Qf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B82_Sicilian_Scheveningen_f4.md#_initial_move_)

## B83

- **Sicilian Defence, Scheveningen Variation,  6.Be2** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B83_Sicilian_Scheveningen_Be2.md#_initial_move_)
- **Sicilian Defence, Modern Scheveningen Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B83_Sicilian_Scheveningen_Be2.md#_Nc6_)
- **Sicilian Defence, Modern Scheveningen Variation,  Main line** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Nc6 7.O-O Be7 8.Be3 O-O 9.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B83_Sicilian_Scheveningen_Be2.md#_MainLine_)
- **Sicilian Defence, Modern Scheveningen Variation,  Main line With Nb3** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 Nc6 7.O-O Be7 8.Be3 O-O 9.f4 Bd7 10.Nb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B83_Sicilian_Scheveningen_Be2.md#_MainLine_)

## B84

- **Sicilian Defence, Scheveningen Variation,  Classical Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B84_Sicilian_Scheveningen_Classical_a6.md#_initial_move_)
- **Sicilian Defence, Scheveningen Variation,  Classical Variation,  Nd7 System** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 a6 7.O-O Nbd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B84_Sicilian_Scheveningen_Classical_a6.md#_afterOO_)
- **Sicilian Defence, Scheveningen Variation,  Classical Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 a6 7.O-O Qc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B84_Sicilian_Scheveningen_Classical_a6.md#_afterOO_)

## B85

- **Sicilian Defence, Scheveningen Variation,  Classical Variation With ...Qc7 and ...Nc6** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 a6 7.O-O Qc7 8.f4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B85_Sicilian_Scheveningen_Classical_f4.md#_initial_move_)
- **Sicilian Defence, Scheveningen Variation,  Classical Variation,  Maroczy System** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 a6 7.O-O Qc7 8.f4 Nc6 9.Kh1 Be7 10.a4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B85_Sicilian_Scheveningen_Classical_f4.md#_Maroczy_)
- **Sicilian Defence, Scheveningen Variation,  Classical Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 a6 7.O-O Qc7 8.f4 Nc6 9.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B85_Sicilian_Scheveningen_Classical_f4.md#_initial_move_)
- **Sicilian Defence, Scheveningen Variation,  Classical Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Be2 a6 7.O-O Qc7 8.f4 Nc6 9.Be3 Be7 10.Qe1 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B85_Sicilian_Scheveningen_Classical_f4.md#_initial_move_)

## B86

- **Sicilian Defence, Sozin Attack** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B86_Sicilian_Scheveningen_Sozin.md#_initial_move_)

## B87

- **Sicilian Defence, Sozin Attack With ...a6 and ...b5** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Bc4 a6 7.Bb3 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B87_Sicilian_Sozin_Flank.md#_initial_move_)

## B88

- **Sicilian Defence, Sozin Attack,  Leonhardt Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Bc4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B88_Sicilian_Sozin_Leonhardt.md#_initial_move_)
- **Sicilian Defence, Sozin Attack,  Fischer Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Bc4 Nc6 7.Bb3 Be7 8.Be3 O-O 9.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B88_Sicilian_Sozin_Leonhardt.md#_initial_move_)

## B89

- **Sicilian Defence, Sozin Attack,  7.Be3** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Bc4 Nc6 7.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B89_Sicilian_Sozin_Be3.md#_initial_move_)
- **Sicilian Defence, Velimirovic Attack** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 e6 6.Bc4 Nc6 7.Be3 Be7 8.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B89_Sicilian_Sozin_Be3.md#_Velimirovic_)

## B90

- **Sicilian Defence, Najdorf** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B90_Sicilian_Najdorf.md#_initial_move_)
- **Sicilian Defence, Najdorf Variation,  Adams Attack** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.h3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B90_Sicilian_Najdorf.md#_h3_)
- **Sicilian Defence, Najdorf Variation,  Lipnitzky Attack** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B90_Sicilian_Najdorf.md#_Bc4_)
- **Sicilian Defence, Najdorf Variation,  Byrne (English) Attack** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B90_Sicilian_Najdorf.md#_Be3_)

## B91

- **Sicilian Defence, Najdorf Variation,  Zagreb (Fianchetto) Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B91_Sicilian_Najdorf_Zagreb.md#_initial_move_)

## B92

- **Sicilian Defence, Najdorf Variation,  Opovcensky Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B92_Sicilian_Najdorf_Opocensky.md#_initial_move_)

## B93

- **Sicilian Defence, Najdorf Variation,  6.f4** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B93_Sicilian_Najdorf_Amsterdam.md#_initial_move_)

## B94

- **Sicilian Defence, Najdorf Variation,  6.Bg5** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B94_Sicilian_Najdorf_Bg5.md#_initial_move_)
- **Sicilian Defence, Najdorf Variation,  Ivkov Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 Nbd7 7.Bc4 Qa5 8.Qd2 e6 9.O-O-O b5 10.Bb3 Bb7 11.Rhe1 Nc5 12.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B94_Sicilian_Najdorf_Bg5.md#_initial_move_)

## B95

- **Sicilian Defence, Najdorf Variation,  6...e6** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B95_Sicilian_Najdorf_e6.md#_initial_move_)

## B96

- **Sicilian Defence, Najdorf Variation,  7.f4** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B96_Sicilian_Najdorf_f4.md#_initial_move_)
- **Sicilian Defence, Najdorf Variation,  Polugayevsky Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B96_Sicilian_Najdorf_f4.md#_Polugayevsky_)
- **Sicilian Defence, Najdorf Variation,  Polugayevsky,  Simagin Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4 b5 8.e5 dxe5 9.fxe5 Qc7 10.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B96_Sicilian_Najdorf_f4.md#_Polugayevsky_)

## B97

- **Sicilian Defence, Najdorf Variation,  7...Qb6** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4 Qb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B97_Sicilian_Najdorf_Poisoned_Pawn.md#_initial_move_)
- **Sicilian Defence, Najdorf Variation,  Poisoned Pawn Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4 Qb6 8.Qd2 Qxb2 9.Rb1 Qa3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B97_Sicilian_Najdorf_Poisoned_Pawn.md#_Accepted_)

## B98

- **Sicilian Defence, Najdorf Variation,  7...Be7** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B98_Sicilian_Najdorf_Be7.md#_initial_move_)
- **Sicilian Defence, Najdorf Variation,  Browne Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4 Be7 8.Qf3 h6 9.Bh4 Qc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B98_Sicilian_Najdorf_Be7.md#_Browne_)
- **Sicilian Defence, Najdorf Variation,  Goteborg Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4 Be7 8.Qf3 h6 9.Bh4 g5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B98_Sicilian_Najdorf_Be7.md#_Browne_)
- **Sicilian Defence, Najdorf Variation** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4 Be7 8.Qf3 Qc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B98_Sicilian_Najdorf_Be7.md#_Qc7_)

## B99

- **Sicilian Defence, Najdorf Variation,  7...Be7 Main line** — `1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 a6 6.Bg5 e6 7.f4 Be7 8.Qf3 Qc7 9.O-O-O Nbd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/B99_Sicilian_Najdorf_Main_Line.md#_initial_move_)

## C00

- **French Defence** — `1.e4 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_initial_move_)
- **French Defence, Steiner Variation** — `1.e4 e6 2.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_initial_move_)
- **French Defence, Reti Variation** — `1.e4 e6 2.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_initial_move_) — live-tagged the *Horwitz Attack*
- **French Defence, Steinitz Attack** — `1.e4 e6 2.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_initial_move_)
- **French Defence, Labourdonnais Variation** — `1.e4 e6 2.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_initial_move_) — live spells it *La Bourdonnais*
- **French Defence** — `1.e4 e6 2.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_initial_move_) — live-tagged the *Knight Variation*
- **French Defence, Wing Gambit** — `1.e4 e6 2.Nf3 d5 3.e5 c5 4.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_initial_move_)
- **French Defence** — `1.e4 e6 2.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_initial_move_) — live-tagged the *Queen's Knight*
- **French Defence, Pelikan Variation** — `1.e4 e6 2.Nc3 d5 3.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_initial_move_)
- **French Defence, Two Knights Variation** — `1.e4 e6 2.Nc3 d5 3.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_initial_move_)
- **French Defence, Chigorin Variation** — `1.e4 e6 2.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_initial_move_)
- **French Defence, King's Indian Attack** — `1.e4 e6 2.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_initial_move_)
- **French Defence, Reversed Philidor formation** — `1.e4 e6 2.d3 d5 3.Nd2 Nf6 4.Ngf3 Nc6 5.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_initial_move_)
- **French Defence** — `1.e4 e6 2.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_d4_)
- **French Defence, Lengfellner System** — `1.e4 e6 2.d4 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_d4_) — live-tagged *Rat Defense: Small Center Defense*, a real name AND family divergence
- **French Defence, St. George Defence** — `1.e4 e6 2.d4 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_d4_)
- **French Defence** — `1.e4 e6 2.d4 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_d4_)
- **French Defence, Schlechter Variation** — `1.e4 e6 2.d4 d5 3.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_d4_)
- **French Defence, Alapin Variation** — `1.e4 e6 2.d4 d5 3.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C00_French_Defense.md#_d4_) — live-tagged the *Alapin Gambit*

## C01

- **French Defence, Exchange Variation** — `1.e4 e6 2.d4 d5 3.exd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C01_French_Exchange.md#_initial_move_)
- **French Defence, Exchange Variation,  Svenonius Variation** — `1.e4 e6 2.d4 d5 3.exd5 exd5 4.Nc3 Nf6 5.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C01_French_Exchange.md#_Svenonius_)
- **French Defence, Exchange Variation,  Bogolyubov Variation** — `1.e4 e6 2.d4 d5 3.exd5 exd5 4.Nc3 Nf6 5.Bg5 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C01_French_Exchange.md#_Svenonius_)

## C02

- **French Defence, Advance Variation** — `1.e4 e6 2.d4 d5 3.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C02_French_Advance.md#_initial_move_)
- **French Defence, Advance Variation,  Steinitz Variation** — `1.e4 e6 2.d4 d5 3.e5 c5 4.dxc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C02_French_Advance.md#_afterc5_)
- **French Defence, Advance Variation,  Nimzovich Variation** — `1.e4 e6 2.d4 d5 3.e5 c5 4.Qg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C02_French_Advance.md#_afterc5_)
- **French Defence, Advance Variation,  Nimzovich System** — `1.e4 e6 2.d4 d5 3.e5 c5 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C02_French_Advance.md#_afterc5_)
- **French Defence, Advance Variation** — `1.e4 e6 2.d4 d5 3.e5 c5 4.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C02_French_Advance.md#_c3_)
- **French Defence, Advance Variation,  Wade Variation** — `1.e4 e6 2.d4 d5 3.e5 c5 4.c3 Qb6 5.Nf3 Bd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C02_French_Advance.md#_Wade_)
- **French Defence, Advance Variation** — `1.e4 e6 2.d4 d5 3.e5 c5 4.c3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C02_French_Advance.md#_c3_)
- **French Defence, Advance Variation,  Paulsen Attack** — `1.e4 e6 2.d4 d5 3.e5 c5 4.c3 Nc6 5.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C02_French_Advance.md#_PaulsenAttack_)
- **French Defence, Advance Variation,  Milner-Barry Gambit** — `1.e4 e6 2.d4 d5 3.e5 c5 4.c3 Nc6 5.Nf3 Qb6 6.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C02_French_Advance.md#_PaulsenAttack_)
- **French Defence, Advance Variation,  Euwe Variation** — `1.e4 e6 2.d4 d5 3.e5 c5 4.c3 Nc6 5.Nf3 Bd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C02_French_Advance.md#_PaulsenAttack_)

## C03

- **French Defence, Tarrasch** — `1.e4 e6 2.d4 d5 3.Nd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C03_French_Tarrasch.md#_initial_move_)
- **French Defence, Tarrasch,  Haberditz Variation** — `1.e4 e6 2.d4 d5 3.Nd2 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C03_French_Tarrasch.md#_Haberditz_)
- **French Defence, Tarrasch,  Guimard Variation** — `1.e4 e6 2.d4 d5 3.Nd2 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C03_French_Tarrasch.md#_Guimard_)

## C04

- **French Defence, Tarrasch,  Guimard Main line** — `1.e4 e6 2.d4 d5 3.Nd2 Nc6 4.Ngf3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C04_French_Tarrasch_Guimard.md#_initial_move_)

## C05

- **French Defence, Tarrasch,  closed Variation** — `1.e4 e6 2.d4 d5 3.Nd2 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C05_French_Tarrasch_Closed.md#_initial_move_)
- **French Defence, Tarrasch,  Botvinnik Variation** — `1.e4 e6 2.d4 d5 3.Nd2 Nf6 4.e5 Nfd7 5.Bd3 c5 6.c3 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C05_French_Tarrasch_Closed.md#_Botvinnik_)
- **French Defence, Tarrasch,  closed Variation** — `1.e4 e6 2.d4 d5 3.Nd2 Nf6 4.e5 Nfd7 5.Bd3 c5 6.c3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C05_French_Tarrasch_Closed.md#_after6c3_)

## C06

- **French Defence, Tarrasch,  closed Variation,  Main line** — `1.e4 e6 2.d4 d5 3.Nd2 Nf6 4.e5 Nfd7 5.Bd3 c5 6.c3 Nc6 7.Ne2 cxd4 8.cxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C06_French_Tarrasch_Closed_Main_Line.md#_initial_move_)
- **French Defence, Tarrasch,  Leningrad Variation** — `1.e4 e6 2.d4 d5 3.Nd2 Nf6 4.e5 Nfd7 5.Bd3 c5 6.c3 Nc6 7.Ne2 cxd4 8.cxd4 Nb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C06_French_Tarrasch_Closed_Main_Line.md#_initial_move_)

## C07

- **French Defence, Tarrasch,  open Variation** — `1.e4 e6 2.d4 d5 3.Nd2 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C07_French_Tarrasch_Open.md#_initial_move_)
- **French Defence, Tarrasch,  Eliskases Variation** — `1.e4 e6 2.d4 d5 3.Nd2 c5 4.exd5 Qxd5 5.Ngf3 cxd4 6.Bc4 Qd8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C07_French_Tarrasch_Open.md#_Eliskases_)

## C08

- **French Defence, Tarrasch,  open,  4.ed ed** — `1.e4 e6 2.d4 d5 3.Nd2 c5 4.exd5 exd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C08_French_Tarrasch_Open_Exchange.md#_initial_move_)

## C09

- **French Defence, Tarrasch,  open Variation,  Main line** — `1.e4 e6 2.d4 d5 3.Nd2 c5 4.exd5 exd5 5.Ngf3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C09_French_Tarrasch_Open_Main_Line.md#_initial_move_)

## C10

- **French Defence, Paulsen Variation** — `1.e4 e6 2.d4 d5 3.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C10_French_Paulsen.md#_initial_move_)
- **French Defence, Marshall Variation** — `1.e4 e6 2.d4 d5 3.Nc3 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C10_French_Paulsen.md#_initial_move_)
- **French Defence, Rubinstein Variation** — `1.e4 e6 2.d4 d5 3.Nc3 dxe4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C10_French_Paulsen.md#_Rubinstein_)
- **French Defence, Fort Knox Variation** — `1.e4 e6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bd7 5.Nf3 Bc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C10_French_Paulsen.md#_FortKnox_)
- **French Defence, Rubinstein Variation** — `1.e4 e6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C10_French_Paulsen.md#_Nd7_)
- **French Defence, Rubinstein,  Capablanca line** — `1.e4 e6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Nf3 Ngf6 6.Nxf6 Nxf6 7.Ne5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C10_French_Paulsen.md#_Nd7_)
- **French Defence, Frere Variation** — `1.e4 e6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Qd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C10_French_Paulsen.md#_Rubinstein_)

## C11

- **French Defence** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C11_French_Classical.md#_initial_move_)
- **French Defence, Swiss Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C11_French_Classical.md#_initial_move_)
- **French Defence, Henneberger Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C11_French_Classical.md#_initial_move_)
- **French Defence, Steinitz Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C11_French_Classical.md#_Steinitz_)
- **French Defence, Steinitz Variation,  Bradford Attack** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.e5 Nfd7 5.f4 c5 6.dxc5 Bxc5 7.Qg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C11_French_Classical.md#_Steinitz_)
- **French Defence, Steinitz Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.e5 Nfd7 5.f4 c5 6.dxc5 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C11_French_Classical.md#_Steinitz_)
- **French Defence, Steinitz Variation,  Brodsky-Jones Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.e5 Nfd7 5.f4 c5 6.dxc5 Nc6 7.a3 Bxc5 8.Qg4 O-O 9.Nf3 f6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C11_French_Classical.md#_Steinitz_)
- **French Defence, Steinitz Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.e5 Nfd7 5.f4 c5 6.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C11_French_Classical.md#_Steinitz_)
- **French Defence, Steinitz Variation,  Boleslavsky Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.e5 Nfd7 5.f4 c5 6.Nf3 Nc6 7.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C11_French_Classical.md#_Steinitz_)
- **French Defence, Steinitz Variation,  Gledhill Attack** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.e5 Nfd7 5.Qg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C11_French_Classical.md#_Steinitz_)
- **French Defence, Burn Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 dxe4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C11_French_Classical.md#_initial_move_)

## C12

- **French Defence, MacCutcheon Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C12_French_MacCutcheon.md#_initial_move_)
- **French Defence, MacCutcheon Variation,  Bogolyubov Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Bb4 5.exd5 Qxd5 6.Bxf6 gxf6 7.Qd2 Qa5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C12_French_MacCutcheon.md#_initial_move_)
- **French Defence, MacCutcheon Variation,  Advance Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Bb4 5.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C12_French_MacCutcheon.md#_Advance_)
- **French Defence, MacCutcheon Variation,  Chigorin Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Bb4 5.e5 h6 6.exf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C12_French_MacCutcheon.md#_Advance_)
- **French Defence, MacCutcheon Variation,  Grigoriev Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Bb4 5.e5 h6 6.exf6 hxg5 7.fxg7 Rg8 8.h4 gxh4 9.Qg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C12_French_MacCutcheon.md#_Advance_)
- **French Defence, MacCutcheon Variation,  Bernstein Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Bb4 5.e5 h6 6.Bh4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C12_French_MacCutcheon.md#_Advance_)
- **French Defence, MacCutcheon Variation,  Janowski Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Bb4 5.e5 h6 6.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C12_French_MacCutcheon.md#_Advance_)
- **French Defence, MacCutcheon Variation,  Dr. Olland (Dutch) Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Bb4 5.e5 h6 6.Bc1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C12_French_MacCutcheon.md#_Advance_)
- **French Defence, MacCutcheon Variation,  Tartakower Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Bb4 5.e5 h6 6.Bd2 Nfd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C12_French_MacCutcheon.md#_Advance_)
- **French Defence, MacCutcheon Variation,  Lasker Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Bb4 5.e5 h6 6.Bd2 Bxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C12_French_MacCutcheon.md#_Advance_)
- **French Defence, MacCutcheon Variation,  Duras Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Bb4 5.e5 h6 6.Bd2 Bxc3 7.bxc3 Ne4 8.Qg4 Kf8 9.Bc1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C12_French_MacCutcheon.md#_Advance_)
- **French Defence, MacCutcheon Variation,  Lasker Variation,  8...g6** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Bb4 5.e5 h6 6.Bd2 Bxc3 7.bxc3 Ne4 8.Qg4 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C12_French_MacCutcheon.md#_Advance_)

## C13

- **French Defence, Classical Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C13_French_Classical.md#_initial_move_)
- **French Defence, Classical Variation,  Anderssen Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.Bxf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C13_French_Classical.md#_initial_move_)
- **French Defence, Classical Variation,  Anderssen-Richter Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.Bxf6 Bxf6 6.e5 Be7 7.Qg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C13_French_Classical.md#_initial_move_)
- **French Defence, Classical Variation,  Vistaneckis (Nimzovich) Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Ng8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C13_French_Classical.md#_after5e5_)
- **French Defence, Classical Variation,  Frankfurt Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Ng8 6.Be3 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C13_French_Classical.md#_after5e5_)
- **French Defence, Classical Variation,  Tartakower Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C13_French_Classical.md#_after5e5_)
- **French Defence, Albin-Alekhine-Chatard Attack** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.h4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C13_French_Classical.md#_Chatard_)
- **French Defence, Albin-Alekhine-Chatard Attack,  Maroczy Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.h4 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C13_French_Classical.md#_Chatard_)
- **French Defence, Albin-Alekhine-Chatard Attack,  Breyer Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.h4 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C13_French_Classical.md#_Chatard_)
- **French Defence, Albin-Alekhine-Chatard Attack,  Teichmann Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.h4 f6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C13_French_Classical.md#_Chatard_)
- **French Defence, Albin-Alekhine-Chatard Attack,  Spielmann Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.h4 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C13_French_Classical.md#_Chatard_)

## C14

- **French Defence, Classical Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.Bxe7 Qxe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C14_French_Classical_Main_Line.md#_initial_move_)
- **French Defence, Classical Variation,  Tarrasch Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.Bxe7 Qxe7 7.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C14_French_Classical_Main_Line.md#_initial_move_)
- **French Defence, Classical Variation,  Rubinstein Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.Bxe7 Qxe7 7.Qd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C14_French_Classical_Main_Line.md#_initial_move_)
- **French Defence, Classical Variation,  Alapin Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.Bxe7 Qxe7 7.Nb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C14_French_Classical_Main_Line.md#_initial_move_)
- **French Defence, Classical Variation,  Pollock Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.Bxe7 Qxe7 7.Qg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C14_French_Classical_Main_Line.md#_initial_move_)
- **French Defence, Classical Variation,  Steinitz Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.Bxe7 Qxe7 7.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C14_French_Classical_Main_Line.md#_Steinitz_)
- **French Defence, Classical Variation,  Stahlberg Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Nf6 4.Bg5 Be7 5.e5 Nfd7 6.Bxe7 Qxe7 7.f4 O-O 8.Nf3 c5 9.Qd2 Nc6 10.O-O-O c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C14_French_Classical_Main_Line.md#_Steinitz_)

## C15

- **French Defence, Winawer Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C15_French_Winawer.md#_initial_move_)
- **French Defence, Winawer Variation,  Kondratiyev Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.Bd3 c5 5.exd5 Qxd5 6.Bd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C15_French_Winawer.md#_initial_move_)
- **French Defence, Winawe Variationr,  Fingerslip Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.Bd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C15_French_Winawer.md#_initial_move_)
- **French Defence, Winawer Variation,  Alekhine Gambit** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.Ne2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C15_French_Winawer.md#_Ne2_)
- **French Defence, Winawer Variation,  Alekhine Gambit,  Alatortsev Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.Ne2 dxe4 5.a3 Be7 6.Nxe4 Nf6 7.N2g3 O-O 8.Be2 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C15_French_Winawer.md#_Ne2_)
- **French Defence, Winawer Variation,  Alekhine Gambit** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.Ne2 dxe4 5.a3 Bxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C15_French_Winawer.md#_Ne2_)
- **French Defence, Winawer Variation,  Alekhine Gambit,  Kan Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.Ne2 dxe4 5.a3 Bxc3 6.Nxc3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C15_French_Winawer.md#_Kan_)

## C16

- **French Defence, Winawer Variation,  Advance Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C16_French_Winawer_Advance.md#_initial_move_)
- **French Defence, Winawer Variation,  Petrosian Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 Qd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C16_French_Winawer_Advance.md#_initial_move_)

## C17

- **French Defence, Winawer Variation,  Advance Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C17_French_Winawer_Advance_c5.md#_initial_move_)
- **French Defence, Winawer Variation,  Advance Variation,  Bogolyubov Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.Bd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C17_French_Winawer_Advance_c5.md#_initial_move_)
- **French Defence, Winawer Variation,  Advance Variation,  Russian Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.Qg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C17_French_Winawer_Advance_c5.md#_initial_move_)
- **French Defence, Winawer Variation,  Advance Variation,  5.a3** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.a3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C17_French_Winawer_Advance_c5.md#_a3fork_)
- **French Defence, Winawer Variation,  Advance Variation,  Rauzer Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.a3 cxd4 6.axb4 dxc3 7.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C17_French_Winawer_Advance_c5.md#_a3fork_)

## C18

- **French Defence, Winawer Variation,  Advance Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.a3 Bxc3 6.bxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C18_French_Winawer_Advance_Classical.md#_initial_move_)
- **French Defence, Winawer Variation,  Classical Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.a3 Bxc3 6.bxc3 Qc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C18_French_Winawer_Advance_Classical.md#_Classical_)

## C19

- **French Defence, Winawer Variation,  Advance Variation,  6...Ne7** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.a3 Bxc3 6.bxc3 Ne7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C19_French_Winawer_Advance_Main_Line.md#_initial_move_)
- **French Defence, Winawer Variation,  Advance Variation,  Smyslov Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.a3 Bxc3 6.bxc3 Ne7 7.a4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C19_French_Winawer_Advance_Main_Line.md#_initial_move_)
- **French Defence, Winawer Variation,  Advance Variation,  positional Main line** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.a3 Bxc3 6.bxc3 Ne7 7.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C19_French_Winawer_Advance_Main_Line.md#_initial_move_)
- **French Defence, Winawer Variation,  Advance Variation,  poisoned Pawn Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.a3 Bxc3 6.bxc3 Ne7 7.Qg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C19_French_Winawer_Advance_Main_Line.md#_PoisonedPawn_)
- **French Defence, Winawer Variation,  Advance Variation,  poisoned Pawn,  Euwe-Gligoric Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.a3 Bxc3 6.bxc3 Ne7 7.Qg4 Qc7 8.Qxg7 Rg8 9.Qxh7 cxd4 10.Kd1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C19_French_Winawer_Advance_Main_Line.md#_PoisonedPawn_)
- **French Defence, Winawer Variation,  Advance Variation,  poisoned Pawn,  Konstantinopolsky Variation** — `1.e4 e6 2.d4 d5 3.Nc3 Bb4 4.e5 c5 5.a3 Bxc3 6.bxc3 Ne7 7.Qg4 Qc7 8.Qxg7 Rg8 9.Qxh7 cxd4 10.Ne2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C19_French_Winawer_Advance_Main_Line.md#_PoisonedPawn_)

## C20

- **King's Pawn Game** — `1.e4 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C20_KPG.md#_initial_move_)
- **King's Pawn Game, Indian Opening** — `1.e4 e5 2.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C20_KPG.md#_initial_move_) — live-tagged the *Leonardis Variation*
- **King's Pawn Game, Mengarini's Opening** — `1.e4 e5 2.a3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C20_KPG.md#_initial_move_)
- **King's Pawn Game, King's head Opening** — `1.e4 e5 2.f3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C20_KPG.md#_initial_move_)
- **King's Pawn Game, Patzer Opening** — `1.e4 e5 2.Qh5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C20_KPG.md#_Qh5_)
- **King's Pawn Game, Napoleon's Opening** — `1.e4 e5 2.Qf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C20_KPG.md#_initial_move_) — live-tagged the *Napoleon Attack*
- **King's Pawn Game, Lopez Opening** — `1.e4 e5 2.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C20_KPG.md#_initial_move_) — live-tagged the *MacLeod Attack*
- **Alapin Opening** — `1.e4 e5 2.Ne2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C20_KPG.md#_initial_move_)

## C21

- **Centre Game** — `1.e4 e5 2.d4 exd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C21_Center_Game_Accepted.md#_initial_move_)
- **Centre Game, Kieseritsky Variation** — `1.e4 e5 2.d4 exd4 3.Nf3 c5 4.Bc4 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C21_Center_Game_Accepted.md#_initial_move_)
- **Halasz Gambit** — `1.e4 e5 2.d4 exd4 3.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C21_Center_Game_Accepted.md#_initial_move_)
- **Danish Gambit** — `1.e4 e5 2.d4 exd4 3.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C21_Center_Game_Accepted.md#_c3_)
- **Danish Gambit, Collijn Defence** — `1.e4 e5 2.d4 exd4 3.c3 dxc3 4.Bc4 cxb2 5.Bxb2 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C21_Center_Game_Accepted.md#_c3_)
- **Danish Gambit, Schlechter Defence** — `1.e4 e5 2.d4 exd4 3.c3 dxc3 4.Bc4 cxb2 5.Bxb2 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C21_Center_Game_Accepted.md#_c3_)
- **Danish Gambit, Soerensen Defence** — `1.e4 e5 2.d4 exd4 3.c3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C21_Center_Game_Accepted.md#_c3_)
- **Centre Game** — `1.e4 e5 2.d4 exd4 3.Qxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C21_Center_Game_Accepted.md#_Qxd4_)

## C22

- **Centre Game** — `1.e4 e5 2.d4 exd4 3.Qxd4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C22_Center_Game_Normal_Variation.md#_initial_move_)
- **Centre Game, Paulsen Attack** — `1.e4 e5 2.d4 exd4 3.Qxd4 Nc6 4.Qe3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C22_Center_Game_Normal_Variation.md#_PaulsenAttack_)
- **Centre Game, Charousek Variation** — `1.e4 e5 2.d4 exd4 3.Qxd4 Nc6 4.Qe3 Bb4 5.c3 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C22_Center_Game_Normal_Variation.md#_PaulsenAttack_)
- **Centre Game, l'Hermet Variation** — `1.e4 e5 2.d4 exd4 3.Qxd4 Nc6 4.Qe3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C22_Center_Game_Normal_Variation.md#_PaulsenAttack_)
- **Centre Game, Berger Variation** — `1.e4 e5 2.d4 exd4 3.Qxd4 Nc6 4.Qe3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C22_Center_Game_Normal_Variation.md#_Berger_)
- **Centre Game, Kupreichik Variation** — `1.e4 e5 2.d4 exd4 3.Qxd4 Nc6 4.Qe3 Nf6 5.Nc3 Bb4 6.Bd2 O-O 7.O-O-O Re8 8.Bc4 d6 9.Nh3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C22_Center_Game_Normal_Variation.md#_Berger_)
- **Centre Game, Hall Variation** — `1.e4 e5 2.d4 exd4 3.Qxd4 Nc6 4.Qc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C22_Center_Game_Normal_Variation.md#_Hall_)

## C23

- **Bishop's Opening** — `1.e4 e5 2.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_initial_move_)
- **Bishop's Opening, Philidor Counter-attack** — `1.e4 e5 2.Bc4 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_PhilidorCA_)
- **Bishop's Opening, Lisitsyn Variation** — `1.e4 e5 2.Bc4 c6 3.d4 d5 4.exd5 cxd5 5.Bb5 Bd7 6.Bxd7 Nxd7 7.dxe5 Nxe5 8.Ne2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_PhilidorCA_)
- **Bishop's Opening, Calabrese Counter-Gambit** — `1.e4 e5 2.Bc4 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_Calabrese_)
- **Bishop's Opening, Calabrese Counter-Gambit,  Jaenisch Variation** — `1.e4 e5 2.Bc4 f5 3.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_Calabrese_)
- **Bishop's Opening, Classical Variation** — `1.e4 e5 2.Bc4 Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_Bc5_)
- **Bishop's Opening, Lopez Gambit** — `1.e4 e5 2.Bc4 Bc5 3.Qe2 Nc6 4.c3 Nf6 5.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_Bc5_)
- **Bishop's Opening, Philidor Variation** — `1.e4 e5 2.Bc4 Bc5 3.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_Bc5_)
- **Bishop's Opening, Pratt Variation** — `1.e4 e5 2.Bc4 Bc5 3.c3 Nf6 4.d4 exd4 5.e5 d5 6.exf6 dxc4 7.Qh5 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_Bc5_)
- **Bishop's Opening, Lewis Counter-Gambit** — `1.e4 e5 2.Bc4 Bc5 3.c3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_Bc5_)
- **Bishop's Opening, del Rio Variation** — `1.e4 e5 2.Bc4 Bc5 3.c3 Qg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_Bc5_)
- **Bishop's Opening, Lewis Gambit** — `1.e4 e5 2.Bc4 Bc5 3.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_Bc5_)
- **Bishop's Opening, Wing Gambit** — `1.e4 e5 2.Bc4 Bc5 3.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_Bc5_)
- **Bishop's Opening, MacDonnell double Gambit** — `1.e4 e5 2.Bc4 Bc5 3.b4 Bxb4 4.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_Bc5_)
- **Bishop's Opening, Four Pawns' Gambit** — `1.e4 e5 2.Bc4 Bc5 3.b4 Bxb4 4.f4 exf4 5.Nf3 Be7 6.d4 Bh4 7.g3 fxg3 8.O-O gxh2 9.Kh1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_Bc5_)

## C24

- **Bishop's Opening, Berlin Defence** — `1.e4 e5 2.Bc4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C24_Bishop_Opening_Berlin_Defense.md#_initial_move_)
- **Bishop's Opening, Greco Gambit** — `1.e4 e5 2.Bc4 Nf6 3.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C24_Bishop_Opening_Berlin_Defense.md#_initial_move_)
- **Bishop's Opening, Ponziani Gambit** — `1.e4 e5 2.Bc4 Nf6 3.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C24_Bishop_Opening_Berlin_Defense.md#_initial_move_)
- **Bishop's Opening, Urusov Gambit** — `1.e4 e5 2.Bc4 Nf6 3.d4 exd4 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C24_Bishop_Opening_Berlin_Defense.md#_initial_move_)
- **Bishop's Opening, Urusov Gambit,  Panov Variation** — `1.e4 e5 2.Bc4 Nf6 3.d4 exd4 4.Nf3 d5 5.exd5 Bb4 6.c3 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C24_Bishop_Opening_Berlin_Defense.md#_initial_move_)

## C25

- **Vienna Game** — `1.e4 e5 2.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_initial_move_)
- **Vienna Game, Zhuravlev CounterGambit** — `1.e4 e5 2.Nc3 Bb4 3.Qg4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_Bb4_)
- **Vienna Game, Max Lange Defence** — `1.e4 e5 2.Nc3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_Nc6_)
- **Vienna Game, Paulsen Variation** — `1.e4 e5 2.Nc3 Nc6 3.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_g3_)
- **Vienna Game, Fyfe Gambit** — `1.e4 e5 2.Nc3 Nc6 3.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_d4_)
- **Vienna Game, Gambit** — `1.e4 e5 2.Nc3 Nc6 3.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_f4_)
- **Vienna Game, Steinitz Gambit** — `1.e4 e5 2.Nc3 Nc6 3.f4 exf4 4.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_SteinitzGambit_)
- **Vienna Game, Steinitz Gambit,  Zukertort Defence** — `1.e4 e5 2.Nc3 Nc6 3.f4 exf4 4.d4 Qh4 5.Ke2 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_SteinitzGambit_)
- **Vienna Game, Steinitz Gambit,  Fraser-Minckwitz Variation** — `1.e4 e5 2.Nc3 Nc6 3.f4 exf4 4.d4 Qh4 5.Ke2 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_SteinitzGambit_)
- **Vienna Game, Gambit** — `1.e4 e5 2.Nc3 Nc6 3.f4 exf4 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_4Nf3_)
- **Vienna Game, Hamppe-Allgaier Gambit** — `1.e4 e5 2.Nc3 Nc6 3.f4 exf4 4.Nf3 g5 5.h4 g4 6.Ng5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_4Nf3_)
- **Vienna Game, Hamppe-Allgaier Gambit,  Alapin Variation** — `1.e4 e5 2.Nc3 Nc6 3.f4 exf4 4.Nf3 g5 5.h4 g4 6.Ng5 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_4Nf3_)
- **Vienna Game, Hamppe-Muzio Gambit** — `1.e4 e5 2.Nc3 Nc6 3.f4 exf4 4.Nf3 g5 5.Bc4 g4 6.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_4Nf3_)
- **Vienna Game, Hamppe-Muzio,  Dubois Variation** — `1.e4 e5 2.Nc3 Nc6 3.f4 exf4 4.Nf3 g5 5.Bc4 g4 6.O-O gxf3 7.Qxf3 Ne5 8.Qxf4 Qf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_4Nf3_)
- **Vienna Game, Pierce Gambit** — `1.e4 e5 2.Nc3 Nc6 3.f4 exf4 4.Nf3 g5 5.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_4Nf3_)
- **Vienna Game, Pierce Gambit,  Rushmere Attack** — `1.e4 e5 2.Nc3 Nc6 3.f4 exf4 4.Nf3 g5 5.d4 g4 6.Bc4 gxf3 7.O-O d5 8.exd5 Bg4 9.dxc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C25_Vienna_Game.md#_4Nf3_)

## C26

- **Vienna Game, Falkbeer Variation** — `1.e4 e5 2.Nc3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C26_Vienna_Falkbeer_Variation.md#_initial_move_)
- **Vienna Game, Mengarini Variation** — `1.e4 e5 2.Nc3 Nf6 3.a3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C26_Vienna_Falkbeer_Variation.md#_a3_)
- **Vienna Game, Paulsen-Mieses Variation** — `1.e4 e5 2.Nc3 Nf6 3.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C26_Vienna_Falkbeer_Variation.md#_g3_)
- **Vienna Game** — `1.e4 e5 2.Nc3 Nf6 3.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C26_Vienna_Falkbeer_Variation.md#_Bc4_)

## C27

- **Vienna Game** — `1.e4 e5 2.Nc3 Nf6 3.Bc4 Nxe4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C27_Vienna_Frankenstein_Dracula.md#_initial_move_)
- **Vienna Game, 'Frankenstein-Dracula' Variation** — `1.e4 e5 2.Nc3 Nf6 3.Bc4 Nxe4 4.Qh5 Nd6 5.Bb3 Nc6 6.Nb5 g6 7.Qf3 f5 8.Qd5 Qe7 9.Nxc7 Kd8 10.Nxa8 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C27_Vienna_Frankenstein_Dracula.md#_Nc6_)
- **Vienna Game, Adams' Gambit** — `1.e4 e5 2.Nc3 Nf6 3.Bc4 Nxe4 4.Qh5 Nd6 5.Bb3 Nc6 6.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C27_Vienna_Frankenstein_Dracula.md#_Nc6_)
- **Vienna Game** — `1.e4 e5 2.Nc3 Nf6 3.Bc4 Nxe4 4.Qh5 Nd6 5.Bb3 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C27_Vienna_Frankenstein_Dracula.md#_Bb3_)
- **Vienna Game, Alekhine Variation** — `1.e4 e5 2.Nc3 Nf6 3.Bc4 Nxe4 4.Qh5 Nd6 5.Bb3 Be7 6.Nf3 Nc6 7.Nxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C27_Vienna_Frankenstein_Dracula.md#_Bb3_)
- **Petrov's Defence** — `1.e4 e5 2.Nc3 Nf6 3.Bc4 Nxe4 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C27_Vienna_Frankenstein_Dracula.md#_initial_move_) — **name divergence**: live-tagged "Bishop's Opening: Boden-Kieseritzky Gambit" and stays C27, not Petrov's own code
- **Petrov's Defence, Lichtenhein Defence** — `1.e4 e5 2.Nc3 Nf6 3.Bc4 Nxe4 4.Nf3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C27_Vienna_Frankenstein_Dracula.md#_initial_move_)

## C28

- **Vienna Game** — `1.e4 e5 2.Nc3 Nf6 3.Bc4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C28_Vienna_Stanley_Three_Knights.md#_initial_move_)

## C29

- **Vienna Game, Gambit,  Kaufmann Variation** — `1.e4 e5 2.Nc3 Nf6 3.f4 d5 4.fxe5 Nxe4 5.Nf3 Bg4 6.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C29_Vienna_Gambit.md#_5Nf3_)
- **Vienna Game, Gambit,  Breyer Variation** — `1.e4 e5 2.Nc3 Nf6 3.f4 d5 4.fxe5 Nxe4 5.Nf3 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C29_Vienna_Gambit.md#_5Nf3_)
- **Vienna Game, Gambit,  Paulsen Attack** — `1.e4 e5 2.Nc3 Nf6 3.f4 d5 4.fxe5 Nxe4 5.Qf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C29_Vienna_Gambit.md#_PaulsenAttack_)
- **Vienna Game, Gambit,  Bardeleben Variation** — `1.e4 e5 2.Nc3 Nf6 3.f4 d5 4.fxe5 Nxe4 5.Qf3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C29_Vienna_Gambit.md#_PaulsenAttack_)
- **Vienna Game, Gambit,  Heyde Variation** — `1.e4 e5 2.Nc3 Nf6 3.f4 d5 4.fxe5 Nxe4 5.Qf3 f5 6.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C29_Vienna_Gambit.md#_PaulsenAttack_)
- **Vienna Game, Gambit** — `1.e4 e5 2.Nc3 Nf6 3.f4 d5 4.fxe5 Nxe4 5.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C29_Vienna_Gambit.md#_Wurzburger_)
- **Vienna Game, Gambit,  Wurzburger trap** — `1.e4 e5 2.Nc3 Nf6 3.f4 d5 4.fxe5 Nxe4 5.d3 Qh4 6.g3 Nxg3 7.Nf3 Qh5 8.Nxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C29_Vienna_Gambit.md#_Wurzburger_)
- **Vienna Game, Gambit,  Steinitz Variation** — `1.e4 e5 2.Nc3 Nf6 3.f4 d5 4.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C29_Vienna_Gambit.md#_Steinitz_)

## C30

- **King's Gambit** — `1.e4 e5 2.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_initial_move_)
- **King's Gambit, Declined,  Keene's Defence** — `1.e4 e5 2.f4 Qh4 3.g3 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_Keene_)
- **King's Gambit, Declined,  Mafia Defence** — `1.e4 e5 2.f4 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_Mafia_)
- **King's Gambit, Declined,  Norwalde Variation** — `1.e4 e5 2.f4 Qf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_Norwalde_)
- **King's Gambit, Declined,  Norwalde Variation,  Buecker Gambit** — `1.e4 e5 2.f4 Qf6 3.Nf3 Qxf4 4.Nc3 Bb4 5.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_Norwalde_)
- **King's Gambit, Declined,  Classical Variation** — `1.e4 e5 2.f4 Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_Bc5_)
- **King's Gambit, Declined,  Classical,  Svenonius Variation** — `1.e4 e5 2.f4 Bc5 3.Nf3 d6 4.Nc3 Nf6 5.Bc4 Nc6 6.d3 Bg4 7.h3 Bxf3 8.Qxf3 exf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_Nc3KGD_)
- **King's Gambit, Declined,  Classical,  Hanham Variation** — `1.e4 e5 2.f4 Bc5 3.Nf3 d6 4.Nc3 Nd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_Nc3KGD_)
- **King's Gambit, Declined,  Classical,  4.c3** — `1.e4 e5 2.f4 Bc5 3.Nf3 d6 4.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_4c3_)
- **King's Gambit, Declined,  Classical,  Marshall Attack** — `1.e4 e5 2.f4 Bc5 3.Nf3 d6 4.c3 Bg4 5.fxe5 dxe5 6.Qa4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_4c3_) — live-tagged the *Euwe Attack*, a real name divergence
- **King's Gambit, Declined,  Classical Counter-Gambit** — `1.e4 e5 2.f4 Bc5 3.Nf3 d6 4.c3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_4c3_) — live-tagged the *Rubinstein Countergambit*, a real name divergence
- **King's Gambit, Declined,  Classical,  Reti Variation** — `1.e4 e5 2.f4 Bc5 3.Nf3 d6 4.c3 f5 5.fxe5 dxe5 6.d4 exd4 7.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_4c3_)
- **King's Gambit, Declined,  Classical,  Soldatenkov Variation** — `1.e4 e5 2.f4 Bc5 3.Nf3 d6 4.fxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_Soldatenkov_)
- **King's Gambit, Declined,  Classical,  Heath Variation** — `1.e4 e5 2.f4 Bc5 3.Nf3 d6 4.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_Heath_) — live-tagged the *Rotlewi Countergambit*, a real name divergence
- **King's Gambit, Declined,  2...Nf6** — `1.e4 e5 2.f4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_PetrovKGD_) — live-tagged *Petrov's Defense*, a real name divergence

## C31

- **King's Gambit, Declined,  Falkbeer Counter-Gambit** — `1.e4 e5 2.f4 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C31_Kings_Gambit_Falkbeer.md#_initial_move_)
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  Tartakower Variation** — `1.e4 e5 2.f4 d5 3.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C31_Kings_Gambit_Falkbeer.md#_initial_move_) — live-tagged the *Blackburne Attack*, a real name divergence
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  Milner-Barry Variation** — `1.e4 e5 2.f4 d5 3.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C31_Kings_Gambit_Falkbeer.md#_initial_move_)
- **King's Gambit, Declined,  Falkbeer Counter-Gambit** — `1.e4 e5 2.f4 d5 3.exd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C31_Kings_Gambit_Falkbeer.md#_exd5_)
- **King's Gambit, Declined,  Nimzovich Counter-Gambit** — `1.e4 e5 2.f4 d5 3.exd5 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C31_Kings_Gambit_Falkbeer.md#_exd5_) — live-tagged the *Nimzowitsch-Marshall Countergambit*, a real name divergence
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  3...e4** — `1.e4 e5 2.f4 d5 3.exd5 e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C31_Kings_Gambit_Falkbeer.md#_e4_) — live-tagged the *Staunton Line*
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  Rubinstein Variation** — `1.e4 e5 2.f4 d5 3.exd5 e4 4.Nc3 Nf6 5.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C31_Kings_Gambit_Falkbeer.md#_e4_)
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  Nimzovich Variation** — `1.e4 e5 2.f4 d5 3.exd5 e4 4.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C31_Kings_Gambit_Falkbeer.md#_e4_) — live-tagged the *Anderssen Attack*, a real name divergence
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  4.d3** — `1.e4 e5 2.f4 d5 3.exd5 e4 4.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C31_Kings_Gambit_Falkbeer.md#_d3_) — live-tagged the *Charousek Gambit*
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  Morphy Gambit** — `1.e4 e5 2.f4 d5 3.exd5 e4 4.d3 Nf6 5.Nc3 Bb4 6.Bd2 e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C31_Kings_Gambit_Falkbeer.md#_d3_) — live-tagged the *Morphy Defense*, a real name divergence

## C32

- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  5.de** — `1.e4 e5 2.f4 d5 3.exd5 e4 4.d3 Nf6 5.dxe4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C32_Kings_Gambit_Falkbeer_Charousek.md#_initial_move_) — live-tagged the *Charousek Gambit Accepted*
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  Alapin Variation** — `1.e4 e5 2.f4 d5 3.exd5 e4 4.d3 Nf6 5.dxe4 Nxe4 6.Nf3 Bc5 7.Qe2 Bf2 8.Kd1 Qxd5 9.Nfd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C32_Kings_Gambit_Falkbeer_Charousek.md#_Alapin_) — confirmed live-tagged, but only at this exact depth; the bare 7...Bf2+ carries no tag of its own
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  Main line,  7...Bf5** — `1.e4 e5 2.f4 d5 3.exd5 e4 4.d3 Nf6 5.dxe4 Nxe4 6.Nf3 Bc5 7.Qe2 Bf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C32_Kings_Gambit_Falkbeer_Charousek.md#_Bf5_)
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  Tarrasch Variation** — `1.e4 e5 2.f4 d5 3.exd5 e4 4.d3 Nf6 5.dxe4 Nxe4 6.Nf3 Bc5 7.Qe2 Bf5 8.g4 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C32_Kings_Gambit_Falkbeer_Charousek.md#_g4_)
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  Charousek Gambit** — `1.e4 e5 2.f4 d5 3.exd5 e4 4.d3 Nf6 5.dxe4 Nxe4 6.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C32_Kings_Gambit_Falkbeer_Charousek.md#_Qe2_)
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  Charousek Variation** — `1.e4 e5 2.f4 d5 3.exd5 e4 4.d3 Nf6 5.dxe4 Nxe4 6.Qe2 Qxd5 7.Nd2 f5 8.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C32_Kings_Gambit_Falkbeer_Charousek.md#_Qe2_)
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  Keres Variation** — `1.e4 e5 2.f4 d5 3.exd5 e4 4.d3 Nf6 5.Nd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C32_Kings_Gambit_Falkbeer_Charousek.md#_OldLine_) — a genuine surprise: sidesteps the dxe4 capture entirely, yet is already live-tagged C32 regardless of `eco.md`'s own move order here
- **King's Gambit, Declined,  Falkbeer Counter-Gambit,  Reti Variation** — `1.e4 e5 2.f4 d5 3.exd5 e4 4.d3 Nf6 5.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C32_Kings_Gambit_Falkbeer_Charousek.md#_OldLine_) — live-tagged the *Old Line*, a real name divergence, and likewise sidesteps dxe4

## C33

- **King's Gambit, Accepted** — `1.e4 e5 2.f4 exf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C30_King_Gambit.md#_exf4_)
- **King's Gambit, Accepted,  Tumbleweed Gambit** — `1.e4 e5 2.f4 exf4 3.Kf2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Other3rd_) — live-tagged simply *Tumbleweed*
- **King's Gambit, Accepted,  Orsini Gambit** — `1.e4 e5 2.f4 exf4 3.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Other3rd_)
- **King's Gambit, Accepted,  Pawn's Gambit** — `1.e4 e5 2.f4 exf4 3.h4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Other3rd_) — live-tagged the *Stamma Gambit*, a real name divergence
- **King's Gambit, Accepted,  Schurig Gambit** — `1.e4 e5 2.f4 exf4 3.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Other3rd_)
- **King's Gambit, Accepted,  Carrera Gambit** — `1.e4 e5 2.f4 exf4 3.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Other3rd_) — live-tagged the *Basman Gambit*, a real name divergence
- **King's Gambit, Accepted,  Villemson Gambit** — `1.e4 e5 2.f4 exf4 3.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Other3rd_)
- **King's Gambit, Accepted,  Keres Gambit** — `1.e4 e5 2.f4 exf4 3.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Other3rd_) — live-tagged the *Mason-Keres Gambit*, a real name divergence
- **King's Gambit, Accepted,  Breyer Gambit** — `1.e4 e5 2.f4 exf4 3.Qf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Other3rd_)
- **King's Gambit, Accepted,  Lesser Bishop's Gambit** — `1.e4 e5 2.f4 exf4 3.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Other3rd_) — live-tagged the *Tartakower Gambit*, a real name divergence
- **King's Gambit, Accepted,  Bishop's Gambit** — `1.e4 e5 2.f4 exf4 3.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_initial_move_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Chigorin's Attack** — `1.e4 e5 2.f4 exf4 3.Bc4 Qh4 4.Kf1 d5 5.Bxd5 g5 6.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Qh4_) — 0 recorded games in either database, no cached eval, confirmed live rather than assumed
- **King's Gambit, Accepted,  Bishop's Gambit,  Greco Variation** — `1.e4 e5 2.f4 exf4 3.Bc4 Qh4 4.Kf1 Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Qh4_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Classical Defence** — `1.e4 e5 2.f4 exf4 3.Bc4 Qh4 4.Kf1 g5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Qh4_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Grimm Attack** — `1.e4 e5 2.f4 exf4 3.Bc4 Qh4 4.Kf1 g5 5.Nc3 Bg7 6.d4 d6 7.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Qh4_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Classical Defence** — `1.e4 e5 2.f4 exf4 3.Bc4 Qh4 4.Kf1 g5 5.Nc3 Bg7 6.d4 Ne7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Qh4_)
- **King's Gambit, Accepted,  Bishop's Gambit,  McDonnell Attack** — `1.e4 e5 2.f4 exf4 3.Bc4 Qh4 4.Kf1 g5 5.Nc3 Bg7 6.d4 Ne7 7.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Qh4_)
- **King's Gambit, Bishop's Gambit,  McDonnell Attack** — `1.e4 e5 2.f4 exf4 3.Bc4 Qh4 4.Kf1 g5 5.Nc3 Bg7 6.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Qh4_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Fraser Variation** — `1.e4 e5 2.f4 exf4 3.Bc4 Qh4 4.Kf1 g5 5.Nc3 Bg7 6.g3 fxg3 7.Qf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Qh4_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Classical Defence,  Cozio Attack** — `1.e4 e5 2.f4 exf4 3.Bc4 Qh4 4.Kf1 g5 5.Qf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Qh4_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Boden Defence** — `1.e4 e5 2.f4 exf4 3.Bc4 Qh4 4.Kf1 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Qh4_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Bryan Counter-Gambit** — `1.e4 e5 2.f4 exf4 3.Bc4 Qh4 4.Kf1 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Qh4_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Bryan Counter-Gambit** — `1.e4 e5 2.f4 exf4 3.Bc4 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_b5root_) — a distinct, direct move order from the Qh4+ 4.Kf1 b5 entry above
- **King's Gambit, Accepted,  Bishop's Gambit,  Steinitz Defence** — `1.e4 e5 2.f4 exf4 3.Bc4 Ne7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Ne7root_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Maurian Defence** — `1.e4 e5 2.f4 exf4 3.Bc4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Nc6root_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Ruy Lopez Defence** — `1.e4 e5 2.f4 exf4 3.Bc4 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_c6root_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Lopez-Gianutio Counter-Gambit** — `1.e4 e5 2.f4 exf4 3.Bc4 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_f5root_)
- **King's Gambit, Accepted,  Lopez-Gianutio Counter-Gambit,  Hein Variation** — `1.e4 e5 2.f4 exf4 3.Bc4 f5 4.Qe2 Qh4 5.Kd1 fxe4 6.Nc3 Kd8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_f5root_) — live-tagged despite 0 recorded games, confirmed by direct query
- **King's Gambit, Accepted,  Bishop's Gambit,  Bledow Variation** — `1.e4 e5 2.f4 exf4 3.Bc4 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_d5_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Gifford Variation** — `1.e4 e5 2.f4 exf4 3.Bc4 d5 4.Bxd5 Qh4 5.Kf1 g5 6.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_d5_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Boren-Svenonius Variation** — `1.e4 e5 2.f4 exf4 3.Bc4 d5 4.Bxd5 Qh4 5.Kf1 Bd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_d5_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Anderssen Variation** — `1.e4 e5 2.f4 exf4 3.Bc4 d5 4.Bxd5 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_d5_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Morphy Variation** — `1.e4 e5 2.f4 exf4 3.Bc4 d5 4.Bxd5 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_d5_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Cozio (Morphy) Defence** — `1.e4 e5 2.f4 exf4 3.Bc4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Nf6_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Bogolyubov Variation** — `1.e4 e5 2.f4 exf4 3.Bc4 Nf6 4.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Nc3_) — live-tagged "Bogoljubow Variation", a minor transliteration difference
- **King's Gambit, Accepted,  Bishop's Gambit,  Paulsen Attack** — `1.e4 e5 2.f4 exf4 3.Bc4 Nf6 4.Nc3 Bb4 5.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Nc3_)
- **King's Gambit, Accepted,  Bishop's Gambit,  Jaenisch Variation** — `1.e4 e5 2.f4 exf4 3.Bc4 Nf6 4.Nc3 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C33_Kings_Gambit_Bishops_Gambit.md#_Nc3_)

## C34

- **King's Gambit, Knight's Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C34_Kings_Gambit_Knights_Gambit.md#_initial_move_) — live-tagged "King's Knight's Gambit"
- **King's Gambit, Accepted,  Bonsch-Osmolovsky Variation** — `1.e4 e5 2.f4 exf4 3.Nf3 Ne7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C34_Kings_Gambit_Knights_Gambit.md#_Ne7_)
- **King's Gambit, Accepted,  Gianutio Counter-Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C34_Kings_Gambit_Knights_Gambit.md#_f5_)
- **King's Gambit, Accepted,  Fischer Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C34_Kings_Gambit_Knights_Gambit.md#_d6_)
- **King's Gambit, Accepted,  Becker Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 h6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C34_Kings_Gambit_Knights_Gambit.md#_h6_)
- **King's Gambit, Accepted,  Schallop Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C34_Kings_Gambit_Knights_Gambit.md#_Nf6_) — live-tagged "Schallopp Defense"

## C35

- **King's Gambit, Accepted,  Cunningham Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C35_Kings_Gambit_Cunningham_Defense.md#_initial_move_)
- **King's Gambit, Accepted,  Cunningham Defence,  Bertin Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 Be7 4.Bc4 Bh4 5.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C35_Kings_Gambit_Cunningham_Defense.md#_Bh4_)
- **King's Gambit, Accepted,  Cunningham Defence,  three Pawns Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 Be7 4.Bc4 Bh4 5.g3 fxg3 6.O-O gxh2 7.Kh1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C35_Kings_Gambit_Cunningham_Defense.md#_Bh4_) — the live explorer doesn't distinguish this depth from the Bertin Gambit itself, a real name/depth divergence
- **King's Gambit, Accepted,  Cunningham Defence,  Euwe Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 Be7 4.Bc4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C35_Kings_Gambit_Cunningham_Defense.md#_McCormick_) — live-tagged the *McCormick Defense*, a real name divergence

## C36

- **King's Gambit, Accepted,  Abbazia Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C36_Kings_Gambit_Abbazia_Defense.md#_initial_move_) — live-tagged the *Modern Defense*, a real name divergence
- **King's Gambit, Accepted,  Abbazia Defence,  Modern Variation** — `1.e4 e5 2.f4 exf4 3.Nf3 d5 4.exd5 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C36_Kings_Gambit_Abbazia_Defense.md#_Nf6_)
- **King's Gambit, Accepted,  Abbazia Defence,  Botvinnik Variation** — `1.e4 e5 2.f4 exf4 3.Nf3 d5 4.exd5 Nf6 5.Bb5 c6 6.dxc6 bxc6 7.Bc4 Nd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C36_Kings_Gambit_Abbazia_Defense.md#_MainLine_) — live-tagged "Abbazia Defense, Main Line" instead, a real name divergence

## C37

- **King's Gambit, Accepted,  Quaade Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_Nc3_)
- **King's Gambit, Accepted,  Rosentreter Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_d4_)
- **King's Gambit, Accepted,  Soerensen Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.d4 g4 5.Ne5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_d4_)
- **King's Gambit, Accepted,  King's Knight's Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_Bc4_) — the actual C37 root; same generic name reused across the family
- **King's Gambit, Accepted,  Blachly Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_Nc6_)
- **King's Gambit, Accepted,  Lolli Gambit (wild Muzio Gambit)** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.Bxf7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_LolliGhulamMac_) — 0 recorded masters games, confirmed live
- **King's Gambit, Accepted,  Lolli Gambit,  Young Variation** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.Bxf7 Kxf7 6.O-O gxf3 7.Qxf3 Qf6 8.d4 Qxd4 9.Be3 Qf6 10.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_LolliGhulamMac_)
- **King's Gambit, Accepted,  Ghulam Kassim Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_LolliGhulamMac_)
- **King's Gambit, Accepted,  MacDonnell Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_LolliGhulamMac_)
- **King's Gambit, Accepted,  Salvio Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.Ne5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_Salvio_)
- **King's Gambit, Accepted,  Silberschmidt Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.Ne5 Qh4 6.Kf1 Nh6 7.d4 f3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_Nh6_)
- **King's Gambit, Accepted,  Salvio Gambit,  Anderssen Counter-attack** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.Ne5 Qh4 6.Kf1 Nh6 7.d4 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_Nh6_)
- **King's Gambit, Accepted,  Cochrane Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.Ne5 Qh4 6.Kf1 f3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_Cochrane_)
- **King's Gambit, Accepted,  Herzfeld Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.Ne5 Qh4 6.Kf1 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_Herzfeld_)
- **King's Gambit, Accepted,  Muzio Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_Muzio_)
- **King's Gambit, Accepted,  Muzio Gambit,  Paulsen Variation** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.O-O gxf3 6.Qxf3 Qf6 7.e5 Qxe5 8.d3 Bh6 9.Nc3 Ne7 10.Bd2 Nbc6 11.Rae1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_Qf6_) — 0 masters games, 15 online, no cached Stockfish eval at this exact depth
- **King's Gambit, Accepted,  double Muzio Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.O-O gxf3 6.Qxf3 Qf6 7.e5 Qxe5 8.Bxf7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_Qf6_)
- **King's Gambit, Accepted,  Muzio Gambit,  From Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.O-O gxf3 6.Qxf3 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_From_)
- **King's Gambit, Accepted,  Muzio Gambit,  Holloway Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.O-O gxf3 6.Qxf3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_Holloway_)
- **King's Gambit, Accepted,  Muzio Gambit,  Kling and Horwitz Counter-attack** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.O-O Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_KlingHorwitz_)
- **King's Gambit, Accepted,  Muzio Gambit,  Brentano Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 g4 5.O-O d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C37_Kings_Gambit_Muzio_Complex.md#_Brentano_)

## C38

- **King's Gambit, Knight's Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 Bg7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C38_Kings_Gambit_Hanstein_Philidor.md#_initial_move_) — live-tagged the *Traditional Variation*, a real name divergence
- **King's Gambit, Accepted,  Hanstein Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 Bg7 5.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C38_Kings_Gambit_Hanstein_Philidor.md#_Hanstein_)
- **King's Gambit, Accepted,  Philidor Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 Bg7 5.h4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C38_Kings_Gambit_Hanstein_Philidor.md#_Philidor_)
- **King's Gambit, Accepted,  Greco Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 Bg7 5.h4 h6 6.d4 d6 7.Nc3 c6 8.hxg5 hxg5 9.Rxh8 Bxh8 10.Ne5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C38_Kings_Gambit_Hanstein_Philidor.md#_h6d4d6_) — 0 masters games, confirmed live
- **King's Gambit, Accepted,  Philidor Gambit,  Schultz Variation** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.Bc4 Bg7 5.h4 h6 6.d4 d6 7.Qd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C38_Kings_Gambit_Hanstein_Philidor.md#_h6d4d6_)

## C39

- **King's Gambit, Knight's Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_initial_move_) — live-tagged the same generic "King's Knight's Gambit" name reused across the family
- **King's Gambit, Accepted,  Allgaier Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ng5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Allgaier_)
- **King's Gambit, Accepted,  Allgaier Gambit,  Horny Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ng5 h6 6.Nxf7 Kxf7 7.Qxg4 Nf6 8.Qxf4 Bd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_h6Nxf7_)
- **King's Gambit, Accepted,  Allgaier Gambit,  Thorold Variation** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ng5 h6 6.Nxf7 Kxf7 7.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_h6Nxf7_) — live-tagged "Thorold Attack", a real name divergence
- **King's Gambit, Accepted,  Allgaier Gambit,  Cook Variation** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ng5 h6 6.Nxf7 Kxf7 7.d4 d5 8.Bxf4 dxe4 9.Bc4 Kg7 10.Be5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_h6Nxf7_)
- **King's Gambit, Accepted,  Allgaier Gambit,  Blackburne Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ng5 h6 6.Nxf7 Kxf7 7.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_h6Nxf7_)
- **King's Gambit, Accepted,  Allgaier Gambit,  Walker Attack** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ng5 h6 6.Nxf7 Kxf7 7.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_h6Nxf7_) — live-tagged "Urusov Attack" already at this depth, a real name/depth divergence
- **King's Gambit, Accepted,  Allgaier Gambit,  Urusov Attack** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ng5 h6 6.Nxf7 Kxf7 7.Bc4 d5 8.Bxd5 Kg7 9.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_h6Nxf7_)
- **King's Gambit, Accepted,  Allgaier Gambit,  Schlechter Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ng5 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Schlechter_)
- **King's Gambit, Accepted,  Kieseritsky,  Paulsen Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 Bg7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Paulsen_)
- **King's Gambit, Accepted,  Kieseritsky,  long Whip (Stockwhip,  Classical) Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 h5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_LongWhip_)
- **King's Gambit, Accepted,  Kieseritsky,  long Whip Defence,  Jaenisch Variation** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 h5 6.Bc4 Rh7 7.d4 Bh6 8.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_LongWhip_)
- **King's Gambit, Accepted,  Kieseritsky,  Brentano Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Brentano_)
- **King's Gambit, Accepted,  Kieseritsky,  Brentano Defence,  Kaplanek Variation** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 d5 6.d4 Nf6 7.exd5 Qxd5 8.Nc3 Bb4 9.Kf2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Brentano_)
- **King's Gambit, Accepted,  Kieseritsky,  Brentano Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 d5 6.d4 Nf6 7.Bxf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Brentano_)
- **King's Gambit, Accepted,  Kieseritsky,  Brentano Defence,  Caro Variation** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 d5 6.d4 Nf6 7.Bxf4 Nxe4 8.Nd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Brentano_)
- **King's Gambit, Accepted,  Kieseritsky,  Salvio (Rosenthal) Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Rosenthal_) — live-tagged simply "Rosenthal Defense"
- **King's Gambit, Accepted,  Kieseritsky,  Salvio Defence,  Cozio Variation** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 Qe7 6.d4 f5 7.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Rosenthal_)
- **King's Gambit, Accepted,  Kieseritsky,  Polerio Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Polerio_)
- **King's Gambit, Accepted,  Kieseritsky,  Neumann Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Neumann_)
- **King's Gambit, Accepted,  Kieseritsky,  Kolisch Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Kolisch_)
- **King's Gambit, Accepted,  Kieseritsky,  Berlin Defence** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Berlin_) — masters' actual main try (56.3%), a real online/masters inversion
- **King's Gambit, Accepted,  Kieseritsky,  Berlin Defence,  Riviere Variation** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 Nf6 6.Nxg4 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Riviere_)
- **King's Gambit, Accepted,  Kieseritsky,  Berlin Defence,  6.Bc4** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 Nf6 6.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Bc4Berlin_) — masters' actual main try at this fork (46.4%), untagged despite that
- **King's Gambit, Accepted,  Kieseritsky,  Rice Gambit** — `1.e4 e5 2.f4 exf4 3.Nf3 g5 4.h4 g4 5.Ne5 Nf6 6.Bc4 d5 7.exd5 Bd6 8.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C39_Kings_Gambit_Kieseritsky_Allgaier.md#_Bc4Berlin_)

## C40

- **King's Knight Opening** — `1.e4 e5 2.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C40_King_Knight.md#_initial_move_)
- **Gunderam Defence** — `1.e4 e5 2.Nf3 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C40_King_Knight.md#_initial_move_)
- **Greco Defence** — `1.e4 e5 2.Nf3 Qf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C40_King_Knight.md#_initial_move_) — live-tagged *King's Pawn Game: McConnell Defense*, a real name divergence
- **Damiano's Defence** — `1.e4 e5 2.Nf3 f6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C40_King_Knight.md#_initial_move_)
- **Queen's Pawn Game, Counter-Gambit,  Elephant Gambit** — `1.e4 e5 2.Nf3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Elephant/Elephant.md#_initial_move_)
- **Queen's Pawn Game, Counter-Gambit,  Maroczy Gambit** — `1.e4 e5 2.Nf3 d5 3.exd5 Bd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Elephant/Elephant.md#_exd5_)
- **Latvian, Counter-Gambit** — `1.e4 e5 2.Nf3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Latvian/Latvian.md#_initial_move_)
- **Latvian, Nimzovich Variation** — `1.e4 e5 2.Nf3 f5 3.Nxe5 Qf6 4.d4 d6 5.Nc4 fxe4 6.Ne3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Latvian/Latvian.md#_Nxe5_) — essentially unplayed at this depth, no cached eval
- **Latvian, Fraser Defence** — `1.e4 e5 2.Nf3 f5 3.Nxe5 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Latvian/Latvian.md#_Nxe5_)
- **Latvian, Gambit,  3.Bc4** — `1.e4 e5 2.Nf3 f5 3.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Latvian/Latvian.md#_Bc4_) — live-tagged the *Mayet Attack*
- **Latvian, Behting Variation** — `1.e4 e5 2.Nf3 f5 3.Bc4 fxe4 4.Nxe5 Qg5 5.Nf7 Qxg2 6.Rf1 d5 7.Nxh8 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Latvian/Latvian.md#_Bc4_)
- **Latvian, Polerio Variation** — `1.e4 e5 2.Nf3 f5 3.Bc4 fxe4 4.Nxe5 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Latvian/Latvian.md#_Bc4_)
- **Latvian, Corkscrew Counter-Gambit** — `1.e4 e5 2.Nf3 f5 3.Bc4 fxe4 4.Nxe5 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Latvian/Latvian.md#_Bc4_)

## C41

- **Philidor's Defence** — `1.e4 e5 2.Nf3 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_initial_move_)
- **Philidor's Defence, Steinitz Variation** — `1.e4 e5 2.Nf3 d6 3.Bc4 Be7 4.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Steinitz_)
- **Philidor's Defence, Lopez Counter-Gambit** — `1.e4 e5 2.Nf3 d6 3.Bc4 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_LopezCG_)
- **Philidor's Defence, Lopez Counter-Gambit,  Jaenisch Variation** — `1.e4 e5 2.Nf3 d6 3.Bc4 f5 4.d4 exd4 5.Ng5 Nh6 6.Nxh7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_LopezCG_)
- **Philidor's Defence** — `1.e4 e5 2.Nf3 d6 3.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_d4_)
- **Philidor's Defence, Philidor Counter-Gambit** — `1.e4 e5 2.Nf3 d6 3.d4 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_f5d4_)
- **Philidor's Defence, Philidor Counter-Gambit,  del Rio Attack** — `1.e4 e5 2.Nf3 d6 3.d4 f5 4.dxe5 fxe4 5.Ng5 d5 6.e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_f5d4_)
- **Philidor's Defence, Philidor Counter-Gambit,  Berger Variation** — `1.e4 e5 2.Nf3 d6 3.d4 f5 4.dxe5 fxe4 5.Ng5 d5 6.e6 Bc5 7.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_f5d4_)
- **Philidor's Defence, Philidor Counter-Gambit,  Zukertort Variation** — `1.e4 e5 2.Nf3 d6 3.d4 f5 4.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_f5d4_)
- **Philidor's Defence, Exchange Variation** — `1.e4 e5 2.Nf3 d6 3.d4 exd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_exd4_)
- **Philidor's Defence, Boden Variation** — `1.e4 e5 2.Nf3 d6 3.d4 exd4 4.Qxd4 Bd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Qxd4d_)
- **Philidor's Defence, Exchange Variation** — `1.e4 e5 2.Nf3 d6 3.d4 exd4 4.Nxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Nxd4d_)
- **Philidor's Defence, Paulsen Attack** — `1.e4 e5 2.Nf3 d6 3.d4 exd4 4.Nxd4 d5 5.exd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Nxd4d_)
- **Philidor's Defence, Exchange Variation** — `1.e4 e5 2.Nf3 d6 3.d4 exd4 4.Nxd4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Nxd4d_)
- **Philidor's Defence, Berger Variation** — `1.e4 e5 2.Nf3 d6 3.d4 exd4 4.Nxd4 Nf6 5.Nc3 Be7 6.Be2 O-O 7.O-O c5 8.Nf3 Nc6 9.Bg5 Be6 10.Re1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Nxd4d_)
- **Philidor's Defence, Larsen Variation** — `1.e4 e5 2.Nf3 d6 3.d4 exd4 4.Nxd4 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Nxd4d_)
- **Philidor's Defence, Nimzovich (Jaenisch) Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Nf6d4_) — live-tagged the *Nimzowitsch Variation* already at this root ply
- **Philidor's Defence, Improved Hanham Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nf6 4.Nc3 Nbd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Nc3Nf6_)
- **Philidor's Defence, Nimzovich,  Sozin Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nf6 4.Nc3 Nbd7 5.Bc4 Be7 6.O-O O-O 7.Qe2 c6 8.a4 exd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Nc3Nf6_)
- **Philidor's Defence, Nimzovich,  Larobok Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nf6 4.Nc3 Nbd7 5.Bc4 Be7 6.Ng5 O-O 7.Bxf7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Nc3Nf6_)
- **Philidor's Defence, Nimzovich Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nf6 4.dxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_dxe5_)
- **Philidor's Defence, Nimzovich,  Sokolsky Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nf6 4.dxe5 Nxe4 5.Nbd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_dxe5_)
- **Philidor's Defence, Nimzovich,  Rellstab Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nf6 4.dxe5 Nxe4 5.Qd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_dxe5_)
- **Philidor's Defence, Nimzovich,  Locock Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nf6 4.Ng5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Ng5d4_)
- **Philidor's Defence, Nimzovich,  Klein Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nf6 4.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Bc4Nf6_)
- **Philidor's Defence, Hanham Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Nd7_)
- **Philidor's Defence, Hanham,  Krause Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nd7 4.Bc4 c6 5.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Bc4c6_)
- **Philidor's Defence, Hanham,  Steiner Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nd7 4.Bc4 c6 5.O-O Be7 6.dxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Bc4c6_)
- **Philidor's Defence, Hanham,  Kmoch Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nd7 4.Bc4 c6 5.Ng5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Bc4c6_)
- **Philidor's Defence, Hanham,  Berger Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nd7 4.Bc4 c6 5.Ng5 Nh6 6.f4 Be7 7.O-O O-O 8.c3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Bc4c6_)
- **Philidor's Defence, Hanham,  Schlechter Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nd7 4.Bc4 c6 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Bc4c6_)
- **Philidor's Defence, Hanham,  Delmar Variation** — `1.e4 e5 2.Nf3 d6 3.d4 Nd7 4.Bc4 c6 5.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C41_Philidor_Defense.md#_Bc4c6_)

## C42

- **Petrov's Defence** — `1.e4 e5 2.Nf3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_initial_move_)
- **Petrov's Defence, French Attack** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_d6_)
- **Petrov's Defence, Kaufmann Attack** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_d6_)
- **Petrov's Defence, Nimzovich Attack** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_d6_)
- **Petrov's Defence, Cozio (Lasker) Attack** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_d6_)
- **Petrov's Defence, Classical Attack** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Classical_)
- **Petrov's Defence, Classical Attack,  Chigorin Variation** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4 d5 6.Bd3 Be7 7.O-O Nc6 8.Re1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Classical_)
- **Petrov's Defence, Classical Attack,  Berger Variation** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4 d5 6.Bd3 Be7 7.O-O Nc6 8.Re1 Bg4 9.c3 f5 10.Nbd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Classical_)
- **Petrov's Defence, Classical Attack,  Krause Variation** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4 d5 6.Bd3 Be7 7.O-O Nc6 8.Re1 Bg4 9.c3 f5 10.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Classical_)
- **Petrov's Defence, Classical Attack,  Maroczy Variation** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4 d5 6.Bd3 Be7 7.O-O Nc6 8.Re1 Bg4 9.c3 f5 10.c4 Bh4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Classical_)
- **Petrov's Defence, Classical Attack,  Jaenisch Variation** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4 d5 6.Bd3 Be7 7.O-O Nc6 8.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Classical_)
- **Petrov's Defence, Classical Attack,  Mason Variation** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4 d5 6.Bd3 Be7 7.O-O O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Classical_)
- **Petrov's Defence, Classical Attack,  Marshall Variation** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4 d5 6.Bd3 Bd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Classical_)
- **Petrov's Defence, Classical Attack,  Tarrasch Variation** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4 d5 6.Bd3 Bd6 7.O-O O-O 8.c4 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Classical_)
- **Petrov's Defence, Classical Attack,  Marshall trap** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4 d5 6.Bd3 Bd6 7.O-O O-O 8.c4 Bg4 9.cxd5 f5 10.Re1 Bxh2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Classical_)
- **Petrov's Defence, Classical Attack,  close Variation** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nf3 Nxe4 5.d4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Classical_) — live-tagged *Closed Variation*
- **Petrov's Defence, Cochrane Gambit** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nxf7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_d6_) — Stockfish already rates this *better for Black* (−0.5), contrary to the line's reputation
- **Petrov's Defence, Paulsen Attack** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 d6 4.Nc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_d6_)
- **Petrov's Defence, Damiano Variation** — `1.e4 e5 2.Nf3 Nf6 3.Nxe5 Nxe4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Nxe4_trap_)
- **Petrov's Defence, Three Knights Game** — `1.e4 e5 2.Nf3 Nf6 3.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Nc3_)
- **Petrov's Defence, Italian Variation** — `1.e4 e5 2.Nf3 Nf6 3.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C42_Petrov_Defense.md#_Bc4_trap_)

## C43

- **Petrov's Defence, Modern (Steinitz) Attack** — `1.e4 e5 2.Nf3 Nf6 3.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C43_Petrov_Modern_Attack.md#_initial_move_)
- **Petrov's Defence, Modern Attack,  Main line** — `1.e4 e5 2.Nf3 Nf6 3.d4 exd4 4.e5 Ne4 5.Qxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C43_Petrov_Modern_Attack.md#_Qxd4_) — live-tagged the *Center Attack*
- **Petrov's Defence, Modern Attack,  Steinitz Variation** — `1.e4 e5 2.Nf3 Nf6 3.d4 exd4 4.e5 Ne4 5.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C43_Petrov_Modern_Attack.md#_Qe2_)
- **Petrov's Defence, Modern Attack,  Bardeleben Variation** — `1.e4 e5 2.Nf3 Nf6 3.d4 exd4 4.e5 Ne4 5.Qe2 Nc5 6.Nxd4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C43_Petrov_Modern_Attack.md#_Qe2_)
- **Petrov's Defence, Urusov Gambit** — `1.e4 e5 2.Nf3 Nf6 3.d4 exd4 4.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C43_Petrov_Modern_Attack.md#_Urusov_)
- **Petrov's Defence, Modern Attack,  Symmetrical Variation** — `1.e4 e5 2.Nf3 Nf6 3.d4 Nxe4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C43_Petrov_Modern_Attack.md#_Nxe4_) — live-tagged the *Center Variation*
- **Petrov's Defence, Modern Attack,  Trifunovic Variation** — `1.e4 e5 2.Nf3 Nf6 3.d4 Nxe4 4.Bd3 d5 5.Nxe5 Bd6 6.O-O O-O 7.c4 Bxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C43_Petrov_Modern_Attack.md#_Bd3_)

## C44

- **King's Pawn Game** — `1.e4 e5 2.Nf3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_initial_move_)
- **Irish Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Nxe5 Nxe5 4.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_initial_move_) — live-tagged the *Schulze-Müller Gambit*, the same name as C46's own analogous line
- **Konstantinopolsky Opening** — `1.e4 e5 2.Nf3 Nc6 3.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_initial_move_)
- **Dresden Opening** — `1.e4 e5 2.Nf3 Nc6 3.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_initial_move_)
- **Inverted Hungarian** — `1.e4 e5 2.Nf3 Nc6 3.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_initial_move_) — live-tagged *Tayler Opening* already at this root ply
- **Inverted Hanham** — `1.e4 e5 2.Nf3 Nc6 3.Be2 Nf6 4.d3 d5 5.Nbd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_initial_move_)
- **Tayler Opening** — `1.e4 e5 2.Nf3 Nc6 3.Be2 Nf6 4.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_initial_move_)
- **Ponziani Opening** — `1.e4 e5 2.Nf3 Nc6 3.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Ponziani_)
- **Ponziani Opening, Caro Variation** — `1.e4 e5 2.Nf3 Nc6 3.c3 d5 4.Qa4 Bd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Ponziani_d5_)
- **Ponziani Opening, Leonhardt Variation** — `1.e4 e5 2.Nf3 Nc6 3.c3 d5 4.Qa4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Ponziani_d5_)
- **Ponziani Opening, Steinitz Variation** — `1.e4 e5 2.Nf3 Nc6 3.c3 d5 4.Qa4 f6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Ponziani_d5_)
- **Ponziani Opening, Jaenisch Counter-attack** — `1.e4 e5 2.Nf3 Nc6 3.c3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Ponziani_Nf6_)
- **Ponziani Opening, Fraser Defence** — `1.e4 e5 2.Nf3 Nc6 3.c3 Nf6 4.d4 Nxe4 5.d5 Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Ponziani_Nf6_)
- **Ponziani Opening, Reti Variation** — `1.e4 e5 2.Nf3 Nc6 3.c3 Nge7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Ponziani_)
- **Ponziani Opening, Romanishin Variation** — `1.e4 e5 2.Nf3 Nc6 3.c3 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Ponziani_)
- **Ponziani Counter-Gambit** — `1.e4 e5 2.Nf3 Nc6 3.c3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Ponziani_CounterGambit_)
- **Ponziani Counter-Gambit, Schmidt Attack** — `1.e4 e5 2.Nf3 Nc6 3.c3 f5 4.d4 d6 5.d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Ponziani_CounterGambit_)
- **Ponziani Counter-Gambit, Cordel Variation** — `1.e4 e5 2.Nf3 Nc6 3.c3 f5 4.d4 d6 5.d5 fxe4 6.Ng5 Nb8 7.Nxe4 Nf6 8.Bd3 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Ponziani_CounterGambit_)
- **Scotch Opening** — `1.e4 e5 2.Nf3 Nc6 3.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Scotch_)
- **Scotch Opening, Lolli Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 Nxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Scotch_)
- **Scotch Opening, Cochrane Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 Nxd4 4.Nxe5 Ne6 5.Bc4 c6 6.O-O Nf6 7.Nxf7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Scotch_)
- **Scotch Opening, Relfsson Gambit ('MacLopez')** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Relfsson_)
- **Scotch Opening, Goering Gambit** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Goering_)
- **Scotch Opening, Sea-cadet mate** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.c3 dxc3 5.Nxc3 d6 6.Bc4 Bg4 7.O-O Ne5 8.Nxe5 Bxd1 9.Bxf7 Ke7 10.Nd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Goering_) — no cached engine eval this deep
- **Scotch Opening, Goering Gambit** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.c3 dxc3 5.Nxc3 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Goering_)
- **Scotch Opening, Goering Gambit,  Bardeleben Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.c3 dxc3 5.Nxc3 Bb4 6.Bc4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Goering_)
- **Scotch Opening, Gambit** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Bc4_)
- **Scotch Opening, Gambit,  Anderssen Counter-attack** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Bc4 Bc5 5.O-O d6 6.c3 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_ScotchGambit_Bc5_)
- **Scotch Opening, Gambit** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Bc4 Bc5 5.Ng5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Sarratt_) — live-tagged the *Sarratt Variation*
- **Scotch Opening, Gambit,  Cochrane-Shumov Defence** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Bc4 Bc5 5.Ng5 Nh6 6.Nxf7 Nxf7 7.Bxf7 Kxf7 8.Qh5 g6 9.Qxc5 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Sarratt_)
- **Scotch Opening, Gambit,  Vitzhum Attack** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Bc4 Bc5 5.Ng5 Nh6 6.Qh5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Sarratt_) — a real engine swing toward Black (−1.1), contrary to its threatening look
- **Scotch Opening, Gambit** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Bc4 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_ScotchGambit_Bb4_) — live-tagged the *London Defense* already at this ply
- **Scotch Opening, Gambit,  Hanneken Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Bc4 Bb4 5.c3 dxc3 6.O-O cxb2 7.Bxb2 Nf6 8.Ng5 O-O 9.e5 Nxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_ScotchGambit_Bb4_)
- **Scotch Opening, Gambit** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Bc4 Bb4 5.c3 dxc3 6.bxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_ScotchGambit_bxc3_)
- **Scotch Opening, Gambit,  Cochrane Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Bc4 Bb4 5.c3 dxc3 6.bxc3 Ba5 7.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_ScotchGambit_bxc3_) — a real engine swing toward Black (−0.8)
- **Scotch Opening, Gambit,  Benima Defence** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Bc4 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_Benima_)
- **Scotch Opening, Gambit,  Dubois-Reti Defence** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Bc4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_DuboisReti_)

## C45

- **Scotch Opening** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_initial_move_)
- **Scotch Opening, Ghulam Kassim Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Nxd4 5.Qxd4 d6 6.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Nxd4_)
- **Scotch Opening, Pulling Counter-attack** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Qh4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Qh4_) — live-tagged *Steinitz Variation* already at this ply
- **Scotch Opening, Horwitz Attack** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Qh4 5.Nb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Horwitz_)
- **Scotch Opening, Berger Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Qh4 5.Nb5 Bb4 6.Nd2 Qxe4 7.Be2 Qxg2 8.Bf3 Qh3 9.Nxc7 Kd8 10.Nxa8 Nf6 11.a3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Horwitz_) — the trapped a8-knight leaves this heavily lost for White (−2.5), despite winning the exchange
- **Scotch Opening** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Qh4 5.Nb5 Bb4 6.Bd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Horwitz_)
- **Scotch Opening, Rosenthal Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Qh4 5.Nb5 Bb4 6.Bd2 Qxe4 7.Be2 Kd8 8.O-O Bxd2 9.Nxd2 Qg6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Horwitz_)
- **Scotch Opening, Fraser Attack** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Qh4 5.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Qh4_)
- **Scotch Opening, Steinitz Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Qh4 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Steinitz5Nc3_)
- **Scotch Opening, Schmidt Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Nf6_)
- **Scotch Opening, Mieses Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Nf6 5.Nxc6 bxc6 6.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Nf6_)
- **Scotch Opening, Tartakower Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Nf6 5.Nxc6 bxc6 6.Nd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Nf6_)
- **Scotch Opening** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Bc5_) — live-tagged the *Classical Variation* already at this ply
- **Scotch Opening, Blackburne Attack** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Bc5 5.Be3 Qf6 6.c3 Nge7 7.Qd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Be3Bc5_)
- **Scotch Opening, Gottschall Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Bc5 5.Be3 Qf6 6.c3 Nge7 7.Qd2 d5 8.Nb5 Bxe3 9.Qxe3 O-O 10.Nxc7 Rb8 11.Nxd5 Nxd5 12.exd5 Nb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Be3Bc5_) — another "wins material, loses the game" trap (−1.5)
- **Scotch Opening, Paulsen Attack** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Bc5 5.Be3 Qf6 6.c3 Nge7 7.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Be3Bc5_)
- **Scotch Opening, Paulsen,  Gunsberg Defence** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Bc5 5.Be3 Qf6 6.c3 Nge7 7.Bb5 Nd8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Be3Bc5_)
- **Scotch Opening, Meitner Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Bc5 5.Be3 Qf6 6.c3 Nge7 7.Nc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Be3Bc5_)
- **Scotch Opening, Blumenfeld Attack** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Bc5 5.Be3 Qf6 6.Nb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Be3Bc5_)
- **Scotch Opening, Potter Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Bc5 5.Nb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Nb3Bc5_)
- **Scotch Opening, Romanishin Variation** — `1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Bc5 5.Nb3 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C45_Scotch_Main_Line.md#_Nb3Bc5_)

## C46

- **Three Knights Game** — `1.e4 e5 2.Nf3 Nc6 3.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md#_initial_move_) — this card's root, disclosed as one ply early for C47 in its own naming note
- **Three Knights Game, Schlechter Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Bb4 4.Nd5 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md#_C46_siblings_)
- **Three Knights Game, Winawer Defence** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md#_C46_siblings_)
- **Three Knights Game, Steinitz Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md#_C46_siblings_) — live-tagged the *Steinitz Defense*
- **Three Knights Game, Steinitz,  Rosenthal Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 g6 4.d4 exd4 5.Nd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md#_C46_siblings_)
- **Four Knights Game** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md#_Nf6_)
- **Four Knights Game, Schultze-Mueller Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Nxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md#_Nf6_) — live-tagged the *Halloween Gambit*, a real code AND name divergence (this exact position is live-coded C47, not C46)
- **Four Knights Game, Italian Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md#_Nf6_)
- **Four Knights Game, Gunsberg Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.a3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md#_Nf6_)

## C47

- **Four Knights Game, Scotch Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md#_ScotchFour_)
- **Four Knights Game, Scotch,  Krause Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.d4 Bb4 5.Nxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md#_ScotchFour_)
- **Four Knights Game, Scotch,  4...exd4** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.d4 exd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md#_ScotchFourExd4_) — live-tagged the *Scotch Variation Accepted*
- **Four Knights Game, Belgrade Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.d4 exd4 5.Nd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C47_Four_Knights_Game.md#_ScotchFourExd4_) — a small edge for Black (−0.2), contrary to its sharp reputation

## C48

- **Four Knights Game, Spanish Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C48_Four_Knights_Spanish.md#_initial_move_)
- **Four Knights Game, Ranken Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 a6 5.Bxc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C48_Four_Knights_Spanish.md#_a6_)
- **Four Knights Game, Spielmann Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 a6 5.Bxc6 dxc6 6.Nxe5 Nxe4 7.Nxe4 Qd4 8.O-O Qxe5 9.Re1 Be6 10.d4 Qd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C48_Four_Knights_Spanish.md#_a6_)
- **Four Knights Game, Spanish,  Classical Defence** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C48_Four_Knights_Spanish.md#_Bc5_)
- **Four Knights Game, Bardeleben Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bc5 5.O-O O-O 6.Nxe5 Nxe5 7.d4 Bd6 8.f4 Nc6 9.e5 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C48_Four_Knights_Spanish.md#_Bc5_)
- **Four Knights Game, Marshall Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bc5 5.O-O O-O 6.Nxe5 Nd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C48_Four_Knights_Spanish.md#_Bc5_)
- **Four Knights Game, Rubinstein Counter-Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Nd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C48_Four_Knights_Spanish.md#_Nd4_) — live-tagged the *Rubinstein Variation*
- **Four Knights Game, Rubinstein Counter-Gambit,  Bogolyubov Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Nd4 5.Nxe5 Qe7 6.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C48_Four_Knights_Spanish.md#_Nd4_)
- **Four Knights Game, Rubinstein Counter-Gambit,  5.Be2** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Nd4 5.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C48_Four_Knights_Spanish.md#_Nd4_)
- **Four Knights Game, Rubinstein Counter-Gambit Maroczy Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Nd4 5.Be2 Nxf3 6.Bxf3 Bc5 7.O-O O-O 8.d3 d6 9.Na4 Bb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C48_Four_Knights_Spanish.md#_Nd4_)
- **Four Knights Game, Rubinstein Counter-Gambit,  Exchange Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Nd4 5.Nxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C48_Four_Knights_Spanish.md#_Nd4_)
- **Four Knights Game, Rubinstein Counter-Gambit,  Henneberger Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Nd4 5.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C48_Four_Knights_Spanish.md#_Nd4_)

## C49

- **Four Knights Game, double Ruy Lopez** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_initial_move_) — live-tagged the *Double Spanish*
- **Four Knights Game, Gunsberg Counter-attack** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_initial_move_)
- **Four Knights Game, double Ruy Lopez** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_d3_)
- **Four Knights Game, Alatortsev Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.d3 Qe7 7.Ne2 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_d3_)
- **Four Knights Game** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.d3 Bxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_Bxc3_)
- **Four Knights Game, Janowski Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.d3 Bxc3 7.bxc3 d6 8.Re1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_Bxc3_)
- **Four Knights Game, Svenonius Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.d3 Bxc3 7.bxc3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_Bxc3_)
- **Four Knights Game, Symmetrical Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.d3 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_d6_)
- **Four Knights Game, Symmetrical,  Metger unpin** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.d3 d6 7.Bg5 Bxc3 8.bxc3 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_d6_)
- **Four Knights Game, Symmetrical,  Capablanca Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.d3 d6 7.Bg5 Bxc3 8.bxc3 Qe7 9.Re1 Nd8 10.d4 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_d6_)
- **Four Knights Game, Symmetrical,  Pillsbury Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.d3 d6 7.Bg5 Ne7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_d6_)
- **Four Knights Game, Symmetrical,  Blake Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.d3 d6 7.Bg5 Ne7 8.Nh4 c6 9.Bc4 d5 10.Bb3 Qd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_d6_)
- **Four Knights Game, Symmetrical,  Tarrasch Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.d3 d6 7.Bg5 Be6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_d6_)
- **Four Knights Game, Symmetrical,  Maroczy System** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.d3 d6 7.Ne2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_d6_)
- **Four Knights Game, Nimzovich (Paulsen) Variation** — `1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Bxc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C49_Four_Knights_Symmetrical.md#_Bxc6_) — live-tagged the *Nimzowitsch Variation*

## C50

- **Italian Game, King's Pawn Game** — `1.e4 e5 2.Nf3 Nc6 3.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md#_initial_move_)
- **Italian Game, Blackburne Shilling Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nd4 4.Nxe5 Qg5 5.Nxf7 Qxg2 6.Rf1 Qxe4 7.Be2 Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md#_Nd4_) (live-tagged the *Blackburne-Kostić Gambit*, a real name divergence)
- **Italian Game, Rousseau Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Rousseau/Rousseau.md)
- **Italian Game, Hungarian Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md#_Be7_)
- **Italian Game, Hungarian Defence,  Tartakower Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Be7 4.d4 exd4 5.c3 Nf6 6.e5 Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md#_Be7_)
- **Italian Game, Giuoco Piano** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md#_Bc5_)
- **Italian Game, Giuoco Piano,  Four Knights Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.Nc3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md#_FourKnightsVar_)
- **Italian Game, Giuoco Piano,  Jerome Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.Bxf7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md#_Jerome_)
- **Italian Game, Giuoco Pianissimo** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md#_Pianissimo_)
- **Italian Game, Giuoco Pianissimo,  Dubois Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 f5 5.Ng5 f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md#_Pianissimo_)
- **Italian Game, Giuoco Pianissimo** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md#_PianissimoNormal_)
- **Italian Game, Giuoco Pianissimo,  Italian Four Knights Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md#_ItalianFourKnights_)
- **Italian Game, Giuoco Pianissimo,  Canal Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.Nc3 d6 6.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C50_Italian.md#_ItalianFourKnights_)

## C51

- **Italian Game, Evans Gambit,  Declined** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Bb6_)
- **Italian Game, Evans Gambit,  Declined,  Lange Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bb6 5.b5 Na5 6.Nxe5 Nh6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Lange_)
- **Italian Game, Evans Gambit, Declined,  Pavlov Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bb6 5.b5 Na5 6.Nxe5 Nh6 7.d4 d6 8.Bxh6 dxe5 9.Bxg7 Rg8 10.Bxf7 Kxf7 11.Bxe5 Qg5 12.Nd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Lange_)
- **Italian Game, Evans Gambit, Declined,  Hirschbach Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bb6 5.b5 Na5 6.Nxe5 Qg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Hirschbach_)
- **Italian Game, Evans Gambit, Declined,  Vasquez Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bb6 5.b5 Na5 6.Nxe5 Qg5 7.Bxf7 Ke7 8.Qh5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Hirschbach_)
- **Italian Game, Evans Gambit,  Declined,  Hicken Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bb6 5.b5 Na5 6.Nxe5 Qg5 7.Qf3 Qxe5 8.Qxf7 Kd8 9.Bb2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Hirschbach_)
- **Italian Game, Evans Gambit,  Declined,  5.a4** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bb6 5.a4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_a4_)
- **Italian Game, Evans Gambit,  Declined,  Showalter Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bb6 5.a4 a6 6.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_a4_)
- **Italian Game, Evans Gambit,  Declined,  Cordel Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bb6 5.Bb2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Cordel_) (name collision with the other "Cordel Variation" below, at 5.c3 Be7 6.d4 Na5 — `eco.md` reuses the bare name for both; the live explorer disambiguates the deeper one as *Anderssen Variation, Cordel Line*)
- **Italian Game, Evans Counter-Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_d5_) (live-tagged the *Hein Countergambit*, a real name divergence)
- **Italian Game, Evans Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Bxb4_)
- **Italian Game, Evans Gambit,  normal Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Bc5 6.d4 exd4 7.O-O d6 8.cxd4 Bb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_c3_) (live-tagged the *McDonnell Defense, Main Line*)
- **Italian Game, Evans Gambit,  Ulvestad Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Bc5 6.d4 exd4 7.O-O d6 8.cxd4 Bb6 9.d5 Na5 10.Bb2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Ulvestad_)
- **Italian Game, Evans Gambit,  Paulsen Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Bc5 6.d4 exd4 7.O-O d6 8.cxd4 Bb6 9.d5 Na5 10.Bb2 Ne7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Ulvestad_)
- **Italian Game, Evans Gambit,  Morphy Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Bc5 6.d4 exd4 7.O-O d6 8.cxd4 Bb6 9.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Morphy_)
- **Italian Game, Evans Gambit,  Goering Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Bc5 6.d4 exd4 7.O-O d6 8.cxd4 Bb6 9.Nc3 Na5 10.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Morphy_) (live spells it *Göring Attack*)
- **Italian Game, Evans Gambit,  Steinitz Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Bc5 6.d4 exd4 7.O-O d6 8.cxd4 Bb6 9.Nc3 Na5 10.Bg5 f6 11.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Morphy_)
- **Italian Game, Evans Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Bc5 6.d4 exd4 7.O-O d6 8.cxd4 Bb6 9.Nc3 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Bg4_)
- **Italian Game, Evans Gambit,  Fraser Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Bc5 6.d4 exd4 7.O-O d6 8.cxd4 Bb6 9.Nc3 Bg4 10.Qa4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Bg4_)
- **Italian Game, Evans Gambit,  Fraser-Mortimer Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Bc5 6.d4 exd4 7.O-O d6 8.cxd4 Bb6 9.Nc3 Bg4 10.Qa4 Bd7 11.Qb3 Na5 12.Bxf7 Kf8 13.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Bg4_)
- **Italian Game, Evans Gambit,  Stone-Ware Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Bd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_StoneWare_)
- **Italian Game, Evans Gambit,  Mayet Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Bf8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_MayetDefence_)
- **Italian Game, Evans Gambit,  5...Be7** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_Anderssen_) (live-tagged the *Anderssen Variation*, a real name divergence from `eco.md`'s bare "5...Be7")
- **Italian Game, Evans Gambit,  Cordel Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Be7 6.d4 Na5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C51_Evans_Gambit.md#_CordelLine_) (live-tagged *Anderssen Variation, Cordel Line* — see the name-collision note above)

## C52

- **Italian Game, Evans Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_initial_move_) (live-tagged the *Main Line*)
- **Italian Game, Evans Gambit,  compromised Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.d4 exd4 7.O-O dxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_Compromised_)
- **Italian Game, Evans Gambit,  compromised Defence,  Paulsen Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.d4 exd4 7.O-O dxc3 8.Qb3 Qf6 9.e5 Qg6 10.Nxc3 Nge7 11.Ba3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_CompromisedMain_) (live-tagged *Compromised Defense, Main Line*, a real name divergence from `eco.md`'s own "Paulsen Variation")
- **Italian Game, Evans Gambit,  compromised Defence,  Potter Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.d4 exd4 7.O-O dxc3 8.Qb3 Qf6 9.e5 Qg6 10.Nxc3 Nge7 11.Rd1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_Potter_)
- **Italian Game, Evans Gambit,  Leonhardt Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.d4 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_Leonhardt_) (live-tagged the *Leonhardt Countergambit*, a real name divergence)
- **Italian Game, Evans Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.d4 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_d6_) (live-tagged the *Bronstein Defense*, a real name divergence)
- **Italian Game, Evans Gambit,  Tartakower Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.d4 d6 7.Qb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_Tartakower_)
- **Italian Game, Evans Gambit,  Levenfish Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.d4 d6 7.Qb3 Qd7 8.dxe5 dxe5 9.O-O Bb6 10.Ba3 Na5 11.Nxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_Tartakower_)
- **Italian Game, Evans Gambit,  Sokolsky Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.d4 d6 7.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_Sokolsky_)
- **Italian Game, Evans Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_OO_) (live-tagged the *Slow Variation*, a real name divergence)
- **Italian Game, Evans Gambit,  Richardson Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.O-O Nf6 7.d4 O-O 8.Nxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_Richardson_)
- **Italian Game, Evans Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.O-O d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_OOd6_)
- **Italian Game, Evans Gambit,  Waller Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.O-O d6 7.d4 exd4 8.Qb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_Waller_)
- **Italian Game, Evans Gambit,  Lasker Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.O-O d6 7.d4 Bb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_Lasker_)
- **Italian Game, Evans Gambit,  Sanders-Alapin Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.O-O d6 7.d4 Bd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_SandersAlapin_)
- **Italian Game, Evans Gambit,  Alapin-Steinitz Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.b4 Bxb4 5.c3 Ba5 6.O-O d6 7.d4 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C52_Evans_Gambit_Main_Line.md#_AlapinSteinitz_)

## C53

- **Italian Game, Giuoco Piano** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C53_Giuoco_Piano_Classical_Variation.md#_initial_move_) (live-tagged the *Classical Variation*)
- **Italian Game, Giuoco Piano,  LaBourdonnais Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 d6 5.d4 exd4 6.cxd4 Bb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C53_Giuoco_Piano_Classical_Variation.md#_LaBourdonnais_)
- **Italian Game, Giuoco Piano,  close Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C53_Giuoco_Piano_Classical_Variation.md#_Qe7_) (live-tagged the *Closed Variation*)
- **Italian Game, Giuoco Piano,  centre-holding Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Qe7 5.d4 Bb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C53_Giuoco_Piano_Classical_Variation.md#_Qe7Center_) (live spells it *Center Holding Variation*)
- **Italian Game, Giuoco Piano,  Tarrasch Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Qe7 5.d4 Bb6 6.O-O Nf6 7.a4 a6 8.Re1 d6 9.h3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C53_Giuoco_Piano_Classical_Variation.md#_Tarrasch_)
- **Italian Game, Giuoco Piano,  Mestel Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Qe7 5.d4 Bb6 6.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C53_Giuoco_Piano_Classical_Variation.md#_Mestel_)
- **Italian Game, Giuoco Piano,  Eisinger Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Qe7 5.d4 Bb6 6.d5 Nb8 7.d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C53_Giuoco_Piano_Classical_Variation.md#_Eisinger_)
- **Italian Game, Giuoco Piano** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C53_Giuoco_Piano_Classical_Variation.md#_Nf6_)
- **Italian Game, Giuoco Piano,  Bird's Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C53_Giuoco_Piano_Classical_Variation.md#_Bird_)
- **Italian Game, Giuoco Piano** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_initial_move_) (a real "wrong root code" find: already live-tagged **C54**, the *Center Attack*, at this exact bare ply — `eco.md` keeps filing it, and the next two entries below, under C53)
- **Italian Game, Giuoco Piano,  Ghulam Kassim Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.e5 Ne4 7.Bd5 Nxf2 8.Kxf2 dxc3 9.Kg3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_e5_) (live-tagged **C54**, not C53 — see the note above)
- **Italian Game, Giuoco Piano** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.e5 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_d5_) (live-tagged **C54**, not C53)
- **Italian Game, Giuoco Piano,  Anderssen Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.e5 d5 7.Bb5 Ne4 8.cxd4 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_d5_) (live-tagged **C54**, not C53 — see the note above)

## C54

- **Italian Game, Giuoco Piano** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_cxd4_) (live-tagged the *Greco Gambit, Traditional Line*)
- **Italian Game, Giuoco Piano,  Krause Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4 7.Bd2 Nxe4 8.Bxb4 Nxb4 9.Bxf7 Kxf7 10.Qb3 d5 11.Ne5 Kf6 12.f3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_Krause_)
- **Italian Game, Giuoco Piano,  Cracow Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4 7.Kf1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_Cracow_)
- **Italian Game, Giuoco Piano,  Greco's Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4 7.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_Greco_)
- **Italian Game, Giuoco Piano,  Greco Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4 7.Nc3 Nxe4 8.O-O Nxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_GrecoNamed_) (a real finding: masters' actual overwhelming choice at this fork is 8...Bxc3, 98.0% — this named line is the rare one, only 2.0%)
- **Italian Game, Giuoco Piano,  Bernstein Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4 7.Nc3 Nxe4 8.O-O Nxc3 9.bxc3 Bxc3 10.Qb3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_GrecoNamed_)
- **Italian Game, Giuoco Piano,  Aitken Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4 7.Nc3 Nxe4 8.O-O Nxc3 9.bxc3 Bxc3 10.Ba3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_GrecoNamed_)
- **Italian Game, Giuoco Piano** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4 7.Nc3 Nxe4 8.O-O Bxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_Bxc3_) (live-tagged the *Greco Gambit, Main Line* — masters' actual overwhelming choice at this fork, 98.0%, see the note above)
- **Italian Game, Giuoco Piano,  SSteinitz Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4 7.Nc3 Nxe4 8.O-O Bxc3 9.bxc3 d5 10.Ba3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_Steinitz_) (`eco.md` has a doubled-letter typo here, "SSteinitz" — the live tag is plain *Steinitz Variation*)
- **Italian Game, Giuoco Piano,  Moeller (Therkatz) Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4 7.Nc3 Nxe4 8.O-O Bxc3 9.d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_Moeller_) (live spells it *Moeller-Therkatz Attack*)
- **Italian Game, Giuoco Piano,  Therkatz-Herzog Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4 7.Nc3 Nxe4 8.O-O Bxc3 9.d5 Bf6 10.Re1 Ne7 11.Rxe4 d6 12.Bg5 Bxg5 13.Nxg5 O-O 14.Nxh7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_Therkatz_)
- **Italian Game, Giuoco Piano,  Moeller,  bayonet Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d4 exd4 6.cxd4 Bb4 7.Nc3 Nxe4 8.O-O Bxc3 9.d5 Bf6 10.Re1 Ne7 11.Rxe4 d6 12.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_Bayonet_) (live spells it *Moeller-Bayonet Attack*)

## C55

- **Italian Game, Two Knights Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C55_Two_Knights_Defense.md#_initial_move_)
- **Italian Game, Giuoco Piano,  Rosentreter Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.O-O Bc5 5.d4 Bxd4 6.Nxd4 Nxd4 7.Bg5 h6 8.Bh4 g5 9.f4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_Rosentreter_) (live-tagged **C54**, not C55)
- **Italian Game, Giuoco Piano** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.O-O Bc5 5.d4 Bxd4 6.Nxd4 Nxd4 7.Bg5 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C55_Two_Knights_Defense.md#_OO_)
- **Italian Game, Giuoco Piano,  Holzhausen Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.O-O Bc5 5.d4 Bxd4 6.Nxd4 Nxd4 7.Bg5 d6 8.f4 Qe7 9.fxe5 dxe5 10.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C54_Giuoco_Piano_Center_Attack.md#_Holzhausen_) (live-tagged **C54**, not C55)
- **Italian Game, Two Knights Defence,  Modern Bishop's Opening** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C24_Bishop_Opening_Berlin_Defense.md#_d3_) (shares its nearest live-tagged ancestor with C24's own Bishop's Opening card, carries no ECO code of its own)
- **Italian Game, Two Knights Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_initial_move_) (a real "wrong root code" find: already live-tagged **C56**, "Open Variation," at this exact bare ply — `eco.md` splits this whole tree across its own C55/C56 headings, but the live explorer keeps it uniformly C56, occasionally dipping to **C44** at points that transpose with the [Scotch Gambit](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Nc6_King_Knight.md#_DuboisReti_))
- **Italian Game, Two Knights Defence,  Keidanz Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.e5 d5 6.Bb5 Ne4 7.Nxd4 Bc5 8.Nxc6 Bxf2 9.Kf1 Qh4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_e5_) (live-tagged **C56**, spelled *Keidansky*)
- **Italian Game, Two Knights Defence,  Perreux Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.Ng5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_Perreux_) (live-tagged **C56**)
- **Italian Game, Two Knights Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_OO_) (live-tagged **C56**, "Scotch Gambit")
- **Italian Game, Two Knights Defence,  Max Lange Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.O-O Bc5 6.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_MaxLange_) (a real finding: masters' actual main try at the parent 5.O-O fork is 5...Nxe4, 77.1% — this whole famous complex is only masters' second choice, 11.7%)
- **Italian Game, Two Knights Defence,  Max Lange Attack,  Berger Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.O-O Bc5 6.e5 d5 7.exf6 dxc4 8.Re1 Be6 9.Ng5 Qd5 10.Nc3 Qf5 11.g4 Qg6 12.Nce4 Bb6 13.f4 O-O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_Ng5Fork_)
- **Italian Game, Two Knights Defence,  Max Lange Attack,  Marshall Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.O-O Bc5 6.e5 d5 7.exf6 dxc4 8.Re1 Be6 9.Ng5 Qd5 10.Nc3 Qf5 11.Nce4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_Ng5Fork_) (live spells it the *Long Variation*)
- **Italian Game, Two Knights Defence,  Max Lange Attack,  Rubinstein Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.O-O Bc5 6.e5 d5 7.exf6 dxc4 8.Re1 Be6 9.Ng5 Qd5 10.Nc3 Qf5 11.Nce4 Bf8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_Ng5Fork_)
- **Italian Game, Two Knights Defence,  Max Lange Attack,  Loman Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.O-O Bc5 6.e5 d5 7.exf6 dxc4 8.Re1 Be6 9.Ng5 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_Ng5Fork_)
- **Italian Game, Two Knights Defence,  Max Lange Attack,  Schlechter Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.O-O Bc5 6.e5 d5 7.exf6 dxc4 8.Re1 Be6 9.fxg7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_Schlechter_)
- **Italian Game, Two Knights Defence,  Max Lange Attack,  Steinitz Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.O-O Bc5 6.e5 Ng4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_Steinitz2_) (live spells it the *Spielmann Defense*)
- **Italian Game, Two Knights Defence,  Max Lange Attack,  Krause Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.O-O Bc5 6.e5 Ng4 7.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_Steinitz2_)

## C56

- **Italian Game, Two Knights Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.O-O Nxe4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_Nxe4_) (live-tagged *Double Gambit Accepted* — masters' actual main choice at the parent fork, 77.1%)
- **Italian Game, Two Knights Defence,  Yurdansky Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.O-O Nxe4 6.Re1 d5 7.Bxd5 Qxd5 8.Nc3 Qa5 9.Nxe4 Be6 10.Bg5 h6 11.Bh4 g5 12.Nf6 Ke7 13.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_Yurdansky_)
- **Italian Game, Two Knights Defence,  Canal Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d4 exd4 5.O-O Nxe4 6.Re1 d5 7.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C56_Two_Knights_Defense_Max_Lange_Attack.md#_Canal_)

## C57

- **Italian Game, Two Knights Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C57_Two_Knights_Defense_Knight_Attack.md#_initial_move_) (live-tagged the *Knight Attack*)
- **Italian Game, Two Knights Defence, Wilkes Barre (Traxler) Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C57_Two_Knights_Defense_Knight_Attack.md#_Traxler_)
- **Italian Game, Two Knights Defence,  Ulvestad Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C57_Two_Knights_Defense_Knight_Attack.md#_Ulvestad_)
- **Italian Game, Two Knights Defence,  Fritz Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Nd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C57_Two_Knights_Defense_Knight_Attack.md#_Fritz_)
- **Italian Game, Two Knights Defence,  Fritz Variation,  Gruber Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Nd4 6.c3 b5 7.Bf1 Nxd5 8.Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C57_Two_Knights_Defense_Knight_Attack.md#_Fritz_)
- **Italian Game, Two Knights Defence,  Lolli Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Nxd5 6.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C57_Two_Knights_Defense_Knight_Attack.md#_Lolli_)
- **Italian Game, Two Knights Defence,  incus Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Nxd5 6.d4 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C57_Two_Knights_Defense_Knight_Attack.md#_Lolli_) (`eco.md` has a typo here — live spells it *Pincus Variation*)
- **Italian Game, Two Knights Defence,  Fegatello Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Nxd5 6.Nxf7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C57_Two_Knights_Defense_Knight_Attack.md#_Fegatello_) (live-tagged the *Fried Liver Attack*, the English name for the same Italian idea)
- **Italian Game, Two Knights Defence,  Fegatello Attack,  Leonhardt Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Nxd5 6.Nxf7 Kxf7 7.Qf3 Ke6 8.Nc3 Nb4 9.Qe4 c6 10.a3 Na6 11.d4 Nc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C57_Two_Knights_Defense_Knight_Attack.md#_Leonhardt_)
- **Italian Game, Two Knights Defence,  Fegatello Attack,  Polerio Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Nxd5 6.Nxf7 Kxf7 7.Qf3 Ke6 8.Nc3 Ne7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C57_Two_Knights_Defense_Knight_Attack.md#_Polerio_) (name collision: a different, earlier "Polerio Defense" lives at C58's own root)

## C58

- **Italian Game, Two Knights Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C58_Two_Knights_Defense_Na5.md#_initial_move_) (live-tagged the *Polerio Defense* — see the name-collision note above)
- **Italian Game, Two Knights Defence,  Kieseritsky Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C58_Two_Knights_Defense_Na5.md#_Kieseritsky_) (live spells it *Kieseritzky*)
- **Italian Game, Two Knights Defence,  Yankovich Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.d3 h6 7.Nf3 e4 8.Qe2 Nxc4 9.dxc4 Bc5 10.Nfd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C58_Two_Knights_Defense_Na5.md#_Kieseritsky_)
- **Italian Game, Two Knights Defence,  Maroczy Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.d3 h6 7.Nf3 e4 8.Qe2 Nxc4 9.dxc4 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C58_Two_Knights_Defense_Na5.md#_Kieseritsky_)
- **Italian Game, Two Knights Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C58_Two_Knights_Defense_Na5.md#_Bb5_) (live-tagged the *Bishop Check Line*)
- **Italian Game, Two Knights Defence,  Bogolyubov Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.Bb5 c6 7.dxc6 bxc6 8.Qf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C58_Two_Knights_Defense_Na5.md#_Qf3_) (live spells it *Bogoljubow*; masters' actual main try at this fork is 8. Bd3, 50.9%, not built out — a real gap)
- **Italian Game, Two Knights Defence,  Paoli Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.Bb5 c6 7.dxc6 bxc6 8.Qf3 Qc7 9.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C58_Two_Knights_Defense_Na5.md#_Paoli_)
- **Italian Game, Two Knights Defence,  Colman Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.Bb5 c6 7.dxc6 bxc6 8.Qf3 Rb8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C58_Two_Knights_Defense_Na5.md#_Qf3_)
- **Italian Game, Two Knights Defence,  Blackburne Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.Bb5 c6 7.dxc6 bxc6 8.Qf3 cxb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C58_Two_Knights_Defense_Na5.md#_Blackburne_)
- **Italian Game, Two Knights Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.Bb5 c6 7.dxc6 bxc6 8.Be2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C58_Two_Knights_Defense_Na5.md#_Be2_)

## C59

- **Italian Game, Two Knights Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.Bb5 c6 7.dxc6 bxc6 8.Be2 h6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C59_Two_Knights_Defense_Polerio_h6.md#_initial_move_) (live-tagged the *Suhle Defense*)
- **Italian Game, Two Knights Defence,  Knorre Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.Bb5 c6 7.dxc6 bxc6 8.Be2 h6 9.Nf3 e4 10.Ne5 Bd6 11.d4 Qc7 12.Bd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C59_Two_Knights_Defense_Polerio_h6.md#_Knorre_)
- **Italian Game, Two Knights Defence,  Goering Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.Bb5 c6 7.dxc6 bxc6 8.Be2 h6 9.Nf3 e4 10.Ne5 Qc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C59_Two_Knights_Defense_Polerio_h6.md#_Goering_) (live spells it *Göring*)
- **Italian Game, Two Knights Defence,  Steinitz Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.Ng5 d5 5.exd5 Na5 6.Bb5 c6 7.dxc6 bxc6 8.Be2 h6 9.Nh3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C59_Two_Knights_Defense_Polerio_h6.md#_Steinitz_)

## C60

- **Ruy Lopez** — `1.e4 e5 2.Nf3 Nc6 3.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C60_Ruy_Lopez.md#_initial_move_)
- **Ruy Lopez, Nuernberg Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 f6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C60_Ruy_Lopez.md#_initial_move_)
- **Ruy Lopez, Pollock Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Na5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C60_Ruy_Lopez.md#_initial_move_)
- **Ruy Lopez, Lucena Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C60_Ruy_Lopez.md#_initial_move_)
- **Ruy Lopez, Vinogradov Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C60_Ruy_Lopez.md#_initial_move_)
- **Ruy Lopez, Brentano Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 g5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C60_Ruy_Lopez.md#_initial_move_)
- **Ruy Lopez, Fianchetto (Smyslov/Barnes) Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C60_Ruy_Lopez.md#_initial_move_)
- **Ruy Lopez, Cozio Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nge7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C60_Ruy_Lopez.md#_initial_move_)
- **Ruy Lopez, Cozio Defence,  Paulsen Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nge7 4.Nc3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C60_Ruy_Lopez.md#_initial_move_)

## C61

- **Ruy Lopez, Bird's Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C61_Ruy_Lopez_Bird_Defence.md#_initial_move_) (live spells it *Bird Variation*)
- **Ruy Lopez, Bird's Defence,  Paulsen Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nd4 4.Nxd4 exd4 5.O-O Ne7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C61_Ruy_Lopez_Bird_Defence.md#_Paulsen_) (a real finding: masters' actual main try at that fork is 5...Bc5, 69.2% — this named line is a real minority, only 2.0%)

## C62

- **Ruy Lopez, old Steinitz Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C62_Ruy_Lopez_Steinitz_Defense.md#_initial_move_) (live spells it plain *Steinitz Defense*)
- **Ruy Lopez, old Steinitz Defence,  Nimzovich Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 d6 4.d4 Bd7 5.Nc3 Nf6 6.Bxc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C62_Ruy_Lopez_Steinitz_Defense.md#_Nimzovich_) (live spells it *Nimzowitsch Attack*)
- **Ruy Lopez, old Steinitz Defence,  Semi-Duras Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 d6 4.d4 Bd7 5.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C62_Ruy_Lopez_Steinitz_Defense.md#_SemiDuras_)

## C63

- **Ruy Lopez, Schliemann Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C63_Ruy_Lopez_Schliemann_Defense.md#_initial_move_) (live spells it *Schliemann Defense*)
- **Ruy Lopez, Schliemann Defence,  Berger Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 f5 4.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C63_Ruy_Lopez_Schliemann_Defense.md#_Berger_) (also independently live-tagged the *Dyckhoff Variation*)

## C64

- **Ruy Lopez, Classical (Cordel) Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C64_Ruy_Lopez_Classical_Variation.md#_initial_move_) (live spells it plain *Classical Variation*)
- **Ruy Lopez, Classical Defence,  Zaitsev Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Bc5 4.O-O Nd4 5.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C64_Ruy_Lopez_Classical_Variation.md#_OO_)
- **Ruy Lopez, Classical Defence,  4.c3** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Bc5 4.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C64_Ruy_Lopez_Classical_Variation.md#_c3_) (live-tagged the *Central Variation*)
- **Ruy Lopez, Classical Defence,  Benelux Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Bc5 4.c3 Nf6 5.O-O O-O 6.d4 Bb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C64_Ruy_Lopez_Classical_Variation.md#_Benelux_)
- **Ruy Lopez, Classical Defence,  Charousek Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Bc5 4.c3 Bb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C64_Ruy_Lopez_Classical_Variation.md#_Charousek_)
- **Ruy Lopez, Classical Defence,  Boden Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Bc5 4.c3 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C64_Ruy_Lopez_Classical_Variation.md#_Boden_)
- **Ruy Lopez, Cordel Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Bc5 4.c3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C64_Ruy_Lopez_Classical_Variation.md#_CordelGambit_)

## C65

- **Ruy Lopez, Berlin Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C65_Ruy_Lopez_Berlin_Defense.md#_initial_move_)
- **Ruy Lopez, Berlin Defence,  Nyholm Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d4 exd4 5.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C65_Ruy_Lopez_Berlin_Defense.md#_Nyholm_)
- **Ruy Lopez, Berlin Defence,  Mortimer Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d3 Ne7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C65_Ruy_Lopez_Berlin_Defense.md#_Mortimer_) (4.d3 itself already live-tagged the *Anti-Berlin Variation*)
- **Ruy Lopez, Berlin Defence,  Mortimer trap** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d3 Ne7 5.Nxe5 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C65_Ruy_Lopez_Berlin_Defense.md#_Mortimer_)
- **Ruy Lopez, Berlin Defence,  Anderssen Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d3 d6 5.Bxc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C65_Ruy_Lopez_Berlin_Defense.md#_d3d6_)
- **Ruy Lopez, Berlin Defence,  Duras Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d3 d6 5.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C65_Ruy_Lopez_Berlin_Defense.md#_d3d6_)
- **Ruy Lopez, Berlin Defence,  Kaufmann Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d3 Bc5 5.Be3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C65_Ruy_Lopez_Berlin_Defense.md#_Kaufmann_)
- **Ruy Lopez, Berlin Defence,  4.O-O** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C65_Ruy_Lopez_Berlin_Defense.md#_initial_move_) (forks its own children, C66/C67)
- **Ruy Lopez, Berlin Defence,  Beverwijk Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C65_Ruy_Lopez_Berlin_Defense.md#_Beverwijk_)

## C66

- **Ruy Lopez, Berlin Defence,  4.O-O,  d6** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C66_Ruy_Lopez_Berlin_Closed.md#_initial_move_) (live-tagged the *Improved Steinitz Defense*)
- **Ruy Lopez, Berlin Defence,  hedgehog Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O d6 5.d4 Bd7 6.Nc3 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C66_Ruy_Lopez_Berlin_Closed.md#_hedgehog_) (live capitalises it *Hedgehog Variation*)
- **Ruy Lopez, Berlin Defence,  Tarrasch trap** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O d6 5.d4 Bd7 6.Nc3 Be7 7.Re1 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C66_Ruy_Lopez_Berlin_Closed.md#_hedgehog_)
- **Ruy Lopez, Closed Berlin Defence,  Bernstein Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O d6 5.d4 Bd7 6.Nc3 Be7 7.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C66_Ruy_Lopez_Berlin_Closed.md#_Bernstein_)
- **Ruy Lopez, Closed Berlin Defence,  Showalter Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O d6 5.d4 Bd7 6.Nc3 Be7 7.Bxc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C66_Ruy_Lopez_Berlin_Closed.md#_Showalter66_)
- **Ruy Lopez, Closed Berlin Defence,  Wolf Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O d6 5.d4 Bd7 6.Nc3 exd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C66_Ruy_Lopez_Berlin_Closed.md#_Wolf_)
- **Ruy Lopez, Closed Berlin Defence,  Chigorin Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O d6 5.d4 Nd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C66_Ruy_Lopez_Berlin_Closed.md#_initial_move_)

## C67

- **Ruy Lopez, Berlin Defence,  open Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C67_Ruy_Lopez_Berlin_Open.md#_initial_move_) (live-tagged the *Rio Gambit Accepted*)
- **Ruy Lopez, Open Berlin Defence,  l'Hermet Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4 5.d4 Nd6 6.dxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C67_Ruy_Lopez_Berlin_Open.md#_lHermetProper_)
- **Ruy Lopez, Open Berlin Defence,  Showalter Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4 5.d4 Nd6 6.Ba4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C67_Ruy_Lopez_Berlin_Open.md#_ShowalterOpen_)
- **Ruy Lopez, Open Berlin Defence,  5...Be7** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4 5.d4 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C67_Ruy_Lopez_Berlin_Open.md#_Rio_) (a real finding: this bare tabiya is already live-tagged the *Rio de Janeiro Variation* itself, one full move earlier than this entry's own deeper ending point below)
- **Ruy Lopez, Berlin Defence,  Rio de Janeiro Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4 5.d4 Be7 6.Qe2 Nd6 7.Bxc6 bxc6 8.dxe5 Nb7 9.Nc3 O-O 10.Re1 Nc5 11.Nd4 Ne6 12.Be3 Nxd4 13.Bxd4 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C67_Ruy_Lopez_Berlin_Open.md#_Rio_) (see the naming note above)
- **Ruy Lopez, Berlin Defence,  Zukertort Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4 5.d4 Be7 6.Qe2 Nd6 7.Bxc6 bxc6 8.dxe5 Nb7 9.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C67_Ruy_Lopez_Berlin_Open.md#_Zukertort67_)
- **Ruy Lopez, Berlin Defence,  Pillsbury Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4 5.d4 Be7 6.Qe2 Nd6 7.Bxc6 bxc6 8.dxe5 Nb7 9.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C67_Ruy_Lopez_Berlin_Open.md#_Pillsbury_)
- **Ruy Lopez, Berlin Defence,  Winawer Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4 5.d4 Be7 6.Qe2 Nd6 7.Bxc6 bxc6 8.dxe5 Nb7 9.Nd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C67_Ruy_Lopez_Berlin_Open.md#_Winawer_)
- **Ruy Lopez, Berlin Defence,  Cordel Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4 5.d4 Be7 6.Qe2 Nd6 7.Bxc6 bxc6 8.dxe5 Nf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C67_Ruy_Lopez_Berlin_Open.md#_Rio_)
- **Ruy Lopez, Berlin Defence,  Trifunovic Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4 5.d4 Be7 6.Qe2 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C67_Ruy_Lopez_Berlin_Open.md#_Trifunovic_)
- **Ruy Lopez, Berlin Defence,  Minckwitz Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4 5.d4 Be7 6.dxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C67_Ruy_Lopez_Berlin_Open.md#_Minckwitz_)
- **Ruy Lopez, Berlin Defence,  Rosenthal Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4 5.d4 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C67_Ruy_Lopez_Berlin_Open.md#_Rosenthal_)

## C68

- **Ruy Lopez, Exchange Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Bxc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C68_Ruy_Lopez_Exchange_Variation.md#_initial_move_)
- **Ruy Lopez, Exchange,  Alekhine Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Bxc6 dxc6 5.d4 exd4 6.Qxd4 Qxd4 7.Nxd4 Bd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C68_Ruy_Lopez_Exchange_Variation.md#_Alekhine_)
- **Ruy Lopez, Exchange,  Keres Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Bxc6 dxc6 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C68_Ruy_Lopez_Exchange_Variation.md#_Keres_)
- **Ruy Lopez, Exchange,  Romanovsky Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Bxc6 dxc6 5.Nc3 f6 6.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C68_Ruy_Lopez_Exchange_Variation.md#_Keres_)

## C69

- **Ruy Lopez, Exchange Variation,  5.O-O** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Bxc6 dxc6 5.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C69_Ruy_Lopez_Exchange_Normal.md#_initial_move_) (live-tagged the *Normal Variation*)
- **Ruy Lopez, Exchange Variation,  Alapin Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Bxc6 dxc6 5.O-O Bg4 6.h3 h5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C69_Ruy_Lopez_Exchange_Normal.md#_Alapin_)
- **Ruy Lopez, Exchange,  Gligoric Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Bxc6 dxc6 5.O-O f6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C69_Ruy_Lopez_Exchange_Normal.md#_Gligoric_)
- **Ruy Lopez, Exchange,  Bronstein Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Bxc6 dxc6 5.O-O Qd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C69_Ruy_Lopez_Exchange_Normal.md#_Bronstein_)

## C70

- **Ruy Lopez** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C70_Ruy_Lopez_Deferred_Defenses.md#_initial_move_) (left untagged live, `opening=None`)
- **Ruy Lopez, Fianchetto Defence,  Deferred** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C70_Ruy_Lopez_Deferred_Defenses.md#_Fianchetto_)
- **Ruy Lopez, Cozio Defence,  Deferred** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nge7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C70_Ruy_Lopez_Deferred_Defenses.md#_Cozio_)
- **Ruy Lopez, Bird's Defence,  Deferred** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C70_Ruy_Lopez_Deferred_Defenses.md#_Bird_) (genuine database rarity, 1 masters game)
- **Ruy Lopez, Alapin Defence,  Deferred** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C70_Ruy_Lopez_Deferred_Defenses.md#_Alapin_) (genuine database rarity, 3 masters games)
- **Ruy Lopez, Classical Defence,  Deferred** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C70_Ruy_Lopez_Deferred_Defenses.md#_Classical_)
- **Ruy Lopez, Caro Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C70_Ruy_Lopez_Deferred_Defenses.md#_Caro_)
- **Ruy Lopez, Graz Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 b5 5.Bb3 Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C70_Ruy_Lopez_Deferred_Defenses.md#_Graz_) (a real finding: masters' actual main try at the 5.Bb3 fork is 5...Na5, 55.4% — this named line is a real minority, only 5.4%)
- **Ruy Lopez, Taimanov Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 b5 5.Bb3 Na5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C70_Ruy_Lopez_Deferred_Defenses.md#_Taimanov_) (live-tagged the *Norwegian Variation* — a real name divergence)
- **Ruy Lopez, Schliemann Defence,  Deferred** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C70_Ruy_Lopez_Deferred_Defenses.md#_Schliemann_)

## C71

- **Ruy Lopez, Modern Steinitz,  Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C71_Ruy_Lopez_Modern_Steinitz_Defense.md#_initial_move_)
- **Ruy Lopez, Noah's ark trap** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 d6 5.d4 b5 6.Bb3 Nxd4 7.Nxd4 exd4 8.Qxd4 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C71_Ruy_Lopez_Modern_Steinitz_Defense.md#_d4_) (a major finding: −2.87, a genuine massive engine swing to Black, fully confirming the trap's fearsome practical reputation)
- **Ruy Lopez, Modern Steinitz Defence,  Three Knights Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 d6 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C71_Ruy_Lopez_Modern_Steinitz_Defense.md#_ThreeKnights_)
- **Ruy Lopez, Modern Steinitz Defence,  Duras (Keres) Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 d6 5.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C71_Ruy_Lopez_Modern_Steinitz_Defense.md#_Duras_)

## C72

- **Ruy Lopez, Modern Steinitz Defence,  5.O-O** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 d6 5.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C72_Ruy_Lopez_Modern_Steinitz_Castle.md#_initial_move_)

## C73

- **Ruy Lopez, Modern Steinitz Defence,  Richter Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 d6 5.Bxc6 bxc6 6.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C73_Ruy_Lopez_Modern_Steinitz_Richter.md#_initial_move_)
- **Ruy Lopez, Modern Steinitz Defence,  Alapin Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 d6 5.Bxc6 bxc6 6.d4 f6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C73_Ruy_Lopez_Modern_Steinitz_Richter.md#_Alapin_)

## C74

- **Ruy Lopez, Modern Steinitz Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 d6 5.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C74_Ruy_Lopez_Modern_Steinitz_Siesta.md#_initial_move_)
- **Ruy Lopez, Modern Steinitz Defence,  Siesta Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 d6 5.c3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C74_Ruy_Lopez_Modern_Steinitz_Siesta.md#_Siesta_)
- **Ruy Lopez, Siesta,  Kopayev Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 d6 5.c3 f5 6.exf5 Bxf5 7.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C74_Ruy_Lopez_Modern_Steinitz_Siesta.md#_Siesta_)

## C75

- **Ruy Lopez, Modern Steinitz Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 d6 5.c3 Bd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C75_Ruy_Lopez_Modern_Steinitz_Rubinstein.md#_initial_move_)
- **Ruy Lopez, Modern Steinitz Defence,  Rubinstein Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 d6 5.c3 Bd7 6.d4 Nge7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C75_Ruy_Lopez_Modern_Steinitz_Rubinstein.md#_Rubinstein_)

## C76

- **Ruy Lopez, Modern Steinitz Defence,  Fianchetto (Bronstein) Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 d6 5.c3 Bd7 6.d4 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C76_Ruy_Lopez_Modern_Steinitz_Fianchetto.md#_initial_move_) (live shortens it to plain *Fianchetto Variation*)

## C77

- **Ruy Lopez, Morphy Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C77_Ruy_Lopez_Morphy_Defense.md#_initial_move_)
- **Ruy Lopez, Four Knights Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C77_Ruy_Lopez_Morphy_Defense.md#_FourKnights_) (live-tagged the *Tarrasch Variation* — a real name divergence)
- **Ruy Lopez, Treybal Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.Bxc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C77_Ruy_Lopez_Morphy_Defense.md#_Treybal_) (live-tagged the *Bayreuth Variation* — a real name divergence)
- **Ruy Lopez, Wormald Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C77_Ruy_Lopez_Morphy_Defense.md#_Wormald_)
- **Ruy Lopez, Wormald Attack,  Gruenfeld Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.Qe2 b5 6.Bb3 Be7 7.d4 d6 8.c3 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C77_Ruy_Lopez_Morphy_Defense.md#_Gruenfeld_) (live nests it under the Wormald Attack rather than tagging it its own name)
- **Ruy Lopez, Anderssen Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C77_Ruy_Lopez_Morphy_Defense.md#_Anderssen_)
- **Ruy Lopez, Morphy Defence,  Duras Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.d3 d6 6.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C77_Ruy_Lopez_Morphy_Defense.md#_MorphyDuras_)

## C78

- **Ruy Lopez, 5.O-O** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C78_Ruy_Lopez_Morphy_Defense_Castle.md#_initial_move_) (a real "wrong root code" situation, disclosed rather than migrated: this exact root is also stated as [C84_Ruy_Lopez_Morphy_Closed.md](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C84_Ruy_Lopez_Morphy_Closed.md)'s own root, but C84's deeper content — the 5...Be7 branch — genuinely stays C84; this card covers the sibling 5...b5/5...Bc5/5...d6 branches C84 only mentioned in passing)
- **Ruy Lopez, Wing Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O b5 6.Bb3 Be7 7.a4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C78_Ruy_Lopez_Morphy_Defense_Castle.md#_Wing_)
- **Ruy Lopez, ...b5 & ...d6** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O b5 6.Bb3 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C78_Ruy_Lopez_Morphy_Defense_Castle.md#_bd6_)
- **Ruy Lopez, Rabinovich Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O b5 6.Bb3 d6 7.Ng5 d5 8.exd5 Nd4 9.Re1 Bc5 10.Rxe5 Kf8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C78_Ruy_Lopez_Morphy_Defense_Castle.md#_Rabinovich_) (genuine database rarity, 1 masters game)
- **Ruy Lopez, Archangelsk (counterthrust) Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O b5 6.Bb3 Bb7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C78_Ruy_Lopez_Morphy_Defense_Castle.md#_Archangelsk_) (live spells it *Arkhangelsk Variation*)
- **Ruy Lopez, Moeller Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C78_Ruy_Lopez_Morphy_Defense_Castle.md#_Moeller_) (live spells it *Møller Variation*)

## C79

- **Ruy Lopez, Steinitz Defence,  Deferred** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C79_Ruy_Lopez_Steinitz_Defense_Deferred.md#_initial_move_)
- **Ruy Lopez, Steinitz Defence,  Deferred,  Lipnitsky Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O d6 6.Bxc6 bxc6 7.d4 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C79_Ruy_Lopez_Steinitz_Defense_Deferred.md#_Lipnitsky_) (genuine database rarity, 7 masters games)
- **Ruy Lopez, Steinitz Defence,  Deferred,  Rubinstein Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O d6 6.Bxc6 bxc6 7.d4 Nxe4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C79_Ruy_Lopez_Steinitz_Defense_Deferred.md#_Rubinstein79_) (genuine database rarity, 14 masters games — too rare for the live explorer to tag with its own name at this node)
- **Ruy Lopez, Steinitz Defence,  Deferred,  Boleslavsky Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O d6 6.Bxc6 bxc6 7.d4 Nxe4 8.Re1 f5 9.dxe5 d5 10.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C79_Ruy_Lopez_Steinitz_Defense_Deferred.md#_Boleslavsky_) (genuine database rarity, 0 masters games found at this exact node)

## C80

- **Ruy Lopez, Open Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C84_Ruy_Lopez_Morphy_Closed.md#_Nxe4_) (built on C84; theory continues on C80)
- **Ruy Lopez, Open,  Tartakower Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_Tartakower_) (genuine database rarity, 11 masters games)
- **Ruy Lopez, Open,  Knorre Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_Knorre_) (genuine database rarity, 0 masters games)
- **Ruy Lopez, Open,  6.d4** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_initial_move_)
- **Ruy Lopez, Open,  Riga Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 exd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_exd4_)
- **Ruy Lopez, Open,  6.d4 b5** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_b5_)
- **Ruy Lopez, Open,  Friess Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Nxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_Friess_)
- **Ruy Lopez, Open,  Richter Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_Richter_) (a real, punishable mistake — masters' reply bxa4 simply wins the hanging bishop)
- **Ruy Lopez, Open,  7.Bb3** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_Bb3_)
- **Ruy Lopez, Open,  Schlechter Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.a4 Nxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_Schlechter_)
- **Ruy Lopez, Open,  Berger Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.a4 Nxd4 9.Nxd4 exd4 10.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_Berger_) (genuine database rarity, 1 masters game)
- **Ruy Lopez, Open,  Harksen Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_Harksen_) (a real, punishable gambit, −1.84)
- **Ruy Lopez, Open,  8.de** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_dxe5o_)
- **Ruy Lopez, Open,  Zukertort Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Ne7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_Zukertort_) (genuine database rarity, 2 masters games)
- **Ruy Lopez, Open,  8...Be6** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_dxe5o_)
- **Ruy Lopez, Open,  Bernstein Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.Nbd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_Nbd2o_)
- **Ruy Lopez, Open,  Bernstein Variation,  Karpov Gambit** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.Nbd2 Nc5 10.c3 d4 11.Ng5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C80_Ruy_Lopez_Open_Variation.md#_Karpov_)

## C81

- **Ruy Lopez, Open,  Howell Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C81_Ruy_Lopez_Open_Howell_Attack.md#_initial_move_)
- **Ruy Lopez, Open,  Howell Attack,  Ekstroem Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.Qe2 Be7 10.Rd1 O-O 11.c4 bxc4 12.Bxc4 Qd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C81_Ruy_Lopez_Open_Howell_Attack.md#_Ekstroem_) (live drops the umlaut, spelling it *Ekstrom*)
- **Ruy Lopez, Open,  Howell Attack,  Adam Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.Qe2 Be7 10.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C81_Ruy_Lopez_Open_Howell_Attack.md#_Be7_) (genuine database rarity, 3 masters games — too rare for the live explorer to tag with its own name)

## C82

- **Ruy Lopez, Open,  9.c3** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C82_Ruy_Lopez_Open_9c3.md#_initial_move_)
- **Ruy Lopez, Open,  Berlin Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.c3 Nc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C82_Ruy_Lopez_Open_9c3.md#_Berlin_)
- **Ruy Lopez, Open,  Italian Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.c3 Bc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C82_Ruy_Lopez_Open_9c3.md#_Italian_)
- **Ruy Lopez, Open,  St. Petersburg Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.c3 Bc5 10.Nbd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C82_Ruy_Lopez_Open_9c3.md#_StPetersburg_)
- **Ruy Lopez, Open,  Dilworth Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.c3 Bc5 10.Nbd2 O-O 11.Bc2 Nxf2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C82_Ruy_Lopez_Open_9c3.md#_Dilworth_) (a real, respected exchange sacrifice, not a blunder)
- **Ruy Lopez, Open,  Motzko Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.c3 Bc5 10.Qd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C82_Ruy_Lopez_Open_9c3.md#_Motzko_)
- **Ruy Lopez, Open,  Motzko Attack,  Nenarokov Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.c3 Bc5 10.Qd3 Ne7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C82_Ruy_Lopez_Open_9c3.md#_Nenarokov_) (genuine database rarity, 15 masters games)

## C83

- **Ruy Lopez, Open,  Classical Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.c3 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C83_Ruy_Lopez_Open_Classical_Defense.md#_initial_move_)
- **Ruy Lopez, Open,  Malkin Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.c3 Be7 10.Nbd2 O-O 11.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C83_Ruy_Lopez_Open_Classical_Defense.md#_Malkin_)
- **Ruy Lopez, Open,  9...Be7,  10.Re1** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.c3 Be7 10.Re1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C83_Ruy_Lopez_Open_Classical_Defense.md#_Re1_) (a real name/popularity mismatch: live-tagged its own *Classical Defense, Main Line* despite only 3.5% of masters games at this fork)
- **Ruy Lopez, Open,  Tarrasch trap** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.c3 Be7 10.Re1 O-O 11.Nd4 Qd7 12.Nxe6 fxe6 13.Rxe4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C83_Ruy_Lopez_Open_Classical_Defense.md#_Tarrasch_) (a major finding: +3.46, a genuine massive engine swing, confirming a real practical trap)
- **Ruy Lopez, Open,  Breslau Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Nxe4 6.d4 b5 7.Bb3 d5 8.dxe5 Be6 9.c3 Be7 10.Re1 O-O 11.Nd4 Nxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C83_Ruy_Lopez_Open_Classical_Defense.md#_Breslau_)

## C84

- **Ruy Lopez, Closed Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C84_Ruy_Lopez_Morphy_Closed.md#_Be7_)
- **Ruy Lopez, Closed,  centre Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C84_Ruy_Lopez_Morphy_Closed.md#_CentreAttack_) (live spells it *Center Attack*)
- **Ruy Lopez, Closed,  Basque Gambit (North Spanish Variation)** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.d4 exd4 7.e5 Ne4 8.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C84_Ruy_Lopez_Morphy_Closed.md#_Basque_) (genuine database rarity, 4 masters games)

## C85

- **Ruy Lopez, Exchange Variation Doubly,  Deferred** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Bxc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C85_Ruy_Lopez_Delayed_Exchange.md#_initial_move_) (live shortens it to plain *Delayed Exchange*)

## C86

- **Ruy Lopez, Worrall Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C86_Ruy_Lopez_Worrall_Attack.md#_initial_move_)
- **Ruy Lopez, Worrall Attack,  Sharp line** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Qe2 b5 7.Bb3 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C86_Ruy_Lopez_Worrall_Attack.md#_Sharp_) (live-tagged the *Castling Line* instead)
- **Ruy Lopez, Worrall Attack,  Solid line** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Qe2 b5 7.Bb3 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C86_Ruy_Lopez_Worrall_Attack.md#_Solid_) (live-tagged the *Delayed Castling Line* instead)

## C87

- **Ruy Lopez, Closed,  Averbakh Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C87_Ruy_Lopez_Averbakh_Variation.md#_initial_move_)

## C88

- **Ruy Lopez, Closed** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C88_Ruy_Lopez_Closed_Bb3.md#_initial_move_)
- **Ruy Lopez, Closed,  Leonhardt Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 Na5 9.Bc2 c5 10.d4 Qc7 11.h3 Nc6 12.d5 Nb8 13.Nbd2 g5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C88_Ruy_Lopez_Closed_Bb3.md#_Leonhardt_) (genuine 0-masters-game rarity in the modern database)
- **Ruy Lopez, Closed,  Balla Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 Na5 9.Bc2 c5 10.d4 Qc7 11.a4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C88_Ruy_Lopez_Closed_Bb3.md#_Balla_)
- **Ruy Lopez, Closed,  7...d6,  8.d4** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C88_Ruy_Lopez_Closed_Bb3.md#_Rosen_) (live-tagged the *Rosen Attack* — a real name divergence)
- **Ruy Lopez, Noah's ark trap** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.d4 Nxd4 9.Nxd4 exd4 10.Qxd4 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C88_Ruy_Lopez_Closed_Bb3.md#_NoahsArk2_) (a second, independent instance of the trap seen on C71 — another major finding, −2.86)
- **Ruy Lopez, Trajkovic Counter-attack** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 Bb7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C88_Ruy_Lopez_Closed_Bb3.md#_Trajkovic_)
- **Ruy Lopez, Closed,  7...O-O** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C88_Ruy_Lopez_Closed_Bb3.md#_OO_)
- **Ruy Lopez, Closed,  Anti-Marshall 8.a4** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.a4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C88_Ruy_Lopez_Closed_Bb3.md#_AntiMarshall_)
- **Ruy Lopez, Closed,  8.c3** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C88_Ruy_Lopez_Closed_Bb3.md#_c3_OO_)

## C89

- **Ruy Lopez, Marshall Counter-attack** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C89_Ruy_Lopez_Marshall_Attack.md#_initial_move_)
- **Ruy Lopez, Marshall Counter-attack,  11...c6** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d5 9.exd5 Nxd5 10.Nxe5 Nxe5 11.Rxe5 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C89_Ruy_Lopez_Marshall_Attack.md#_Nxe5b_)
- **Ruy Lopez, Marshall Counter-attack,  Kevitz Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d5 9.exd5 Nxd5 10.Nxe5 Nxe5 11.Rxe5 c6 12.Bxd5 cxd5 13.d4 Bd6 14.Re3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C89_Ruy_Lopez_Marshall_Attack.md#_Kevitz_) (live-tagged the *Re3 Variation* — a real name divergence)
- **Ruy Lopez, Marshall Counter-attack,  Main line,  12.d2d4** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d5 9.exd5 Nxd5 10.Nxe5 Nxe5 11.Rxe5 c6 12.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C89_Ruy_Lopez_Marshall_Attack.md#_MainLine_)
- **Ruy Lopez, Marshall Counter-attack,  Main line,  14...Qh3** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d5 9.exd5 Nxd5 10.Nxe5 Nxe5 11.Rxe5 c6 12.d4 Bd6 13.Re1 Qh4 14.g3 Qh3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C89_Ruy_Lopez_Marshall_Attack.md#_MainLine_) (live-tagged the *Modern Main Line*)
- **Ruy Lopez, Marshall Counter-attack,  Main line,  Spassky Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d5 9.exd5 Nxd5 10.Nxe5 Nxe5 11.Rxe5 c6 12.d4 Bd6 13.Re1 Qh4 14.g3 Qh3 15.Be3 Bg4 16.Qd3 Rae8 17.Nd2 Re6 18.a4 Qh5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C89_Ruy_Lopez_Marshall_Attack.md#_Spassky_)
- **Ruy Lopez, Marshall Counter-attack,  Herman Steiner Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d5 9.exd5 e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C89_Ruy_Lopez_Marshall_Attack.md#_HermanSteiner_) (live drops the first name, spelling it plain *Steiner Variation*)

## C90

- **Ruy Lopez, Closed (with ...d6)** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C90_Ruy_Lopez_Closed_Tabiya.md#_initial_move_) (transposes to the same position already built as C90's own root, reached in this repo via 7...d6 8.c3 O-O)
- **Ruy Lopez, Closed,  Pilnik Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.d3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C90_Ruy_Lopez_Closed_Tabiya.md#_Pilnik_)
- **Ruy Lopez, Closed,  Lutikov Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.Bc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C90_Ruy_Lopez_Closed_Tabiya.md#_Lutikov_) (genuine database rarity, 11 masters games)
- **Ruy Lopez, Closed,  Suetin Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.a3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C90_Ruy_Lopez_Closed_Tabiya.md#_Suetin_)

## C91

- **Ruy Lopez, Closed,  9.d4** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C91_Ruy_Lopez_Yates_Variation.md#_initial_move_) (live-tagged the *Yates Variation*; migrated off C90, where it previously lived as a NOTE box)
- **Ruy Lopez, Closed,  Bogolyubov Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.d4 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C91_Ruy_Lopez_Yates_Variation.md#_Bogoljubow_) (live spells it *Bogoljubow*)

## C92

- **Ruy Lopez, Closed,  9.h3** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C92_Ruy_Lopez_Zaitsev.md#_initial_move_) (a real "wrong root code" find: this bare tabiya is live-tagged C92, not C90 — migrated here from C90's own file, where it previously lived as a full built-out section)
- **Ruy Lopez, Closed,  Keres (9...a5) Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 a5` ✅ [mentioned](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C92_Ruy_Lopez_Zaitsev.md#_initial_move_) (left untagged live, `opening=None`, despite carrying a named `eco.md` entry — too obscure for the live database to tag independently; not built out with its own section)
- **Ruy Lopez, Closed,  Kholmov Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Be6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C92_Ruy_Lopez_Zaitsev.md#_Kholmov_)
- **Ruy Lopez, Closed,  Ragozin-Petrosian ('Keres') Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Nd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C92_Ruy_Lopez_Zaitsev.md#_Karpov_) (live-tagged the *Karpov Variation* instead — a real name divergence)
- **Ruy Lopez, Closed,  Flohr-Zaitsev System (Lenzerheide Variation)** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Bb7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C92_Ruy_Lopez_Zaitsev.md#_Bb7_) (live-tagged the *Flohr System*; becomes the *Zaitsev Variation* proper one move later at 10...Re8)

## C93

- **Ruy Lopez, Closed,  Smyslov Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 h6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C93_Ruy_Lopez_Smyslov_Defense.md#_initial_move_)

## C94

- **Ruy Lopez, Closed,  Breyer Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Nb8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C94_Ruy_Lopez_Breyer.md#_initial_move_) (deeper content migrated out to C95, where it's already live-tagged)

## C95

- **Ruy Lopez, Closed,  Breyer Defence,  10.d4** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Nb8 10.d4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C95_Ruy_Lopez_Breyer_Main_Line.md#_initial_move_) (migrated off C94, where it previously lived as a full built-out section already live-tagged C95 in its own cross-links)
- **Ruy Lopez, Closed,  Breyer Defence,  Borisenko Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Nb8 10.d4 Nbd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C95_Ruy_Lopez_Breyer_Main_Line.md#_Nbd7_)
- **Ruy Lopez, Closed,  Breyer Defence,  Gligoric Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Nb8 10.d4 Nbd7 11.Nbd2 Bb7 12.Bc2 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C95_Ruy_Lopez_Breyer_Main_Line.md#_Gligoric_) (live-tagged simply as a continuation of the Breyer Defense, not distinctly named at this exact node)
- **Ruy Lopez, Closed,  Breyer Defence,  Simagin Variation** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Nb8 10.d4 Nbd7 11.Nh4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C95_Ruy_Lopez_Breyer_Main_Line.md#_Simagin_) (genuine database rarity, 24 masters games)

## C96

- **Ruy Lopez, Closed (8...Na5)** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Na5 10.Bc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C96_Ruy_Lopez_Chigorin_Bc2.md#_initial_move_) (a real "wrong root code" find: this bare tabiya is live-tagged C96, not C97 — migrated here from C97's own file, where it previously lived as a full built-out section)
- **Ruy Lopez, Closed,  Rossolimo Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Na5 10.Bc2 c6 11.d4 Qc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C96_Ruy_Lopez_Chigorin_Bc2.md#_Rossolimo_) (genuine database rarity, 7 masters games)
- **Ruy Lopez, Closed (10...c5)** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Na5 10.Bc2 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C96_Ruy_Lopez_Chigorin_Bc2.md#_c5_)
- **Ruy Lopez, Closed,  Borisenko Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Na5 10.Bc2 c5 11.d4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C96_Ruy_Lopez_Chigorin_Bc2.md#_Borisenko_) (live spells it *Borisenko Variation*)
- **Ruy Lopez, Closed,  Keres (...Nd7) Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Na5 10.Bc2 c5 11.d4 Nd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C96_Ruy_Lopez_Chigorin_Bc2.md#_Keres_) (live shortens it to *Keres Defense*)

## C97

- **Ruy Lopez, Closed,  Chigorin Defence** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Na5 10.Bc2 c5 11.d4 Qc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C97_Ruy_Lopez_Chigorin.md#_Qc7_) (reached back from C96's own 11.d4 fork; C97's own file otherwise now roots one full escalation earlier, at the bare 9...Na5 tabiya, after the C96 split)
- **Ruy Lopez, Closed,  Chigorin Defence,  Yugoslav System** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 Bd7 13.Nf1 Rfe8 14.Ne3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C97_Ruy_Lopez_Chigorin.md#_Yugoslav_) (genuine database rarity in the modern sample, 7 masters games)

## C98

- **Ruy Lopez, Closed,  Chigorin Defence,  12...Nc6** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C98_Ruy_Lopez_Chigorin_Nbd2.md#_initial_move_)
- **Ruy Lopez, Closed,  Chigorin Defence,  Rauzer Attack** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 Nc6 13.dxc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C98_Ruy_Lopez_Chigorin_Nbd2.md#_Rauzer_) (genuine database rarity, 47 masters games)

## C99

- **Ruy Lopez, Closed,  Chigorin Defence,  12...c5d4** — `1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C99_Ruy_Lopez_Chigorin_Panov_System.md#_initial_move_) (a real, substantial name divergence: `eco.md` leaves this bare tabiya untitled, the live explorer independently names it the ***Panov System***)

## D00

- **Queen's Pawn Game** — `1.d4 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D00_Queens_Pawn_Game.md#_initial_move_)
- **Queen's Pawn Game, Mason Variation** — `1.d4 d5 2.Bf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D00_Queens_Pawn_Game.md#_Bf4_) (live-tagged the *Accelerated London System*)
- **Queen's Pawn Game, Mason Variation,  Steinitz Counter-Gambit** — `1.d4 d5 2.Bf4 c5` ✅ [mentioned](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D00_Queens_Pawn_Game.md#_Bf4_) (inline, 29.4% masters at that fork)
- **Levitsky Attack** — `1.d4 d5 2.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D00_Queens_Pawn_Game.md#_Bg5_)
- **Blackmar Gambit** — `1.d4 d5 2.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D00_Queens_Pawn_Game.md#_initial_move_) (live-tagged the *Hübsch Gambit*; the accepted line is covered in full on its own dedicated card, [gambits/Blackmar-Diemer](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Blackmar-Diemer/Blackmar-Diemer.md))
- **Queen's Pawn Game, Stonewall Attack** — `1.d4 d5 2.e3 Nf6 3.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D00_Queens_Pawn_Game.md#_Stonewall_)
- **Queen's Pawn Game, Chigorin Variation** — `1.d4 d5 2.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D00_Queens_Pawn_Game.md#_Nc3_) (a real finding: this exact position is live-tagged **A45**, reusing the name from an unrelated ECO branch)
- **Queen's Pawn Game, Anti-Veresov** — `1.d4 d5 2.Nc3 Bg4` ✅ [mentioned](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D00_Queens_Pawn_Game.md#_Nc3_) (genuine database rarity, 3 masters games)
- **Blackmar-Diemer Gambit** — `1.d4 d5 2.Nc3 Nf6 3.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Blackmar-Diemer/Blackmar-Diemer.md#_3_Nc3_) (full dedicated card, not duplicated on D00)
- **Blackmar-Diemer Gambit, Euwe Defence** — `1.d4 d5 2.Nc3 Nf6 3.e4 dxe4 4.f3 exf3 5.Nxf3 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Blackmar-Diemer/Blackmar-Diemer.md#_5_Nxf3_e6_)
- **Blackmar-Diemer Gambit, Lemberg Counter-Gambit** — `1.d4 d5 2.Nc3 Nf6 3.e4 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/gambits/Blackmar-Diemer/Blackmar-Diemer.md#_3_Nc3_e5_) (live spells it *Lemberger Countergambit*)

## D01

- **Richter-Veresov Attack** — `1.d4 d5 2.Nc3 Nf6 3.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D01_Richter_Veresov_Attack.md#_Bg5_)
- **Richter-Veresov Attack, Veresov Variation** — `1.d4 d5 2.Nc3 Nf6 3.Bg5 Bf5 4.Bxf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D01_Richter_Veresov_Attack.md#_Veresov_)
- **Richter-Veresov Attack, Richter Variation** — `1.d4 d5 2.Nc3 Nf6 3.Bg5 Bf5 4.f3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D01_Richter_Veresov_Attack.md#_Richter_)

## D02

- **Queen's Pawn Game** — `1.d4 d5 2.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D02_Zukertort_Variation.md#_initial_move_)
- **Queen's Pawn Game, Chigorin Variation** — `1.d4 d5 2.Nf3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D02_Zukertort_Variation.md#_Chigorin_)
- **Queen's Pawn Game, Krause Variation** — `1.d4 d5 2.Nf3 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D02_Zukertort_Variation.md#_Krause_)
- **Queen's Pawn Game** — `1.d4 d5 2.Nf3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D02_Zukertort_Variation.md#_Nf6_) (live-tagged the *Symmetrical Variation*)
- **Queen's Bishop Game** — `1.d4 d5 2.Nf3 Nf6 3.Bf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D02_London_System.md#_initial_move_) (covered under this repo's own "London System" card title, matching its real content)

## D03

- **Torre Attack, Tartakower Variation** — `1.d4 d5 2.Nf3 Nf6 3.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D03_Torre_Attack.md#_initial_move_) (live-tagged plain *Torre Attack* — a real name divergence, now stated inline)

## D04

- **Queen's Pawn Game** — `1.d4 d5 2.Nf3 Nf6 3.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D04_Colle_System.md#_initial_move_)

## D05

- **Queen's Pawn Game** — `1.d4 d5 2.Nf3 Nf6 3.e3 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D05_Colle_System.md#_initial_move_)
- **Queen's Pawn Game, Zukertort Variation** — `1.d4 d5 2.Nf3 Nf6 3.e3 e6 4.Nbd2 c5 5.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D05_Colle_System.md#_Zukertort_)
- **Queen's Pawn Game** — `1.d4 d5 2.Nf3 Nf6 3.e3 e6 4.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D05_Colle_System.md#_Bd3_)
- **Queen's Pawn Game, Rubinstein (Colle-Zukertort) Variation** — `1.d4 d5 2.Nf3 Nf6 3.e3 e6 4.Bd3 c5 5.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D05_Colle_System.md#_b3_) (live-tagged the *Rubinstein Opening*)
- **Colle System** — `1.d4 d5 2.Nf3 Nf6 3.e3 e6 4.Bd3 c5 5.c3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D05_Colle_System.md#_c3_) (live-tagged the *Traditional Colle*)

## D06

- **Queen's Gambit** — `1.d4 d5 2.c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D06_Queens_Gambit.md#_c4_)
- **Queen's Gambit, Declined,  Grau Defence** — `1.d4 d5 2.c4 Bf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D06_Queens_Gambit.md#_Bf5_) (live-tagged the *Baltic Defense* — a real, substantial name divergence)
- **Queen's Gambit, Declined,  Marshall Defence** — `1.d4 d5 2.c4 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D06_Queens_Gambit.md#_Nf6d_)
- **Queen's Gambit, Declined,  Symmetrical Defence** — `1.d4 d5 2.c4 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D06_Queens_Gambit.md#_c5d_) (live-tagged the *Austrian Defense* — another real, substantial name divergence)

## D07

- **Queen's Gambit, Declined,  Chigorin Defence** — `1.d4 d5 2.c4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D07_Chigorin_Defense.md#_initial_move_)
- **Queen's Gambit, Declined,  Chigorin Defence,  Janowski Variation** — `1.d4 d5 2.c4 Nc6 3.Nc3 dxc4 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D07_Chigorin_Defense.md#_Nc3_)

## D08

- **Queen's Gambit, Declined,  Albin Counter-Gambit** — `1.d4 d5 2.c4 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D08_Albin_Countergambit.md#_initial_move_)
- **Queen's Gambit, Declined,  Albin Counter-Gambit,  Lasker trap** — `1.d4 d5 2.c4 e5 3.dxe5 d4 4.e3 Bb4 5.Bd2 dxe3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D08_Albin_Countergambit.md#_Lasker_) (genuine database rarity, 2 masters games; the position itself is dead level, −0.03 — the trap is purely a mating pattern, not a raw material swing)
- **Queen's Gambit, Declined,  Albin Counter-Gambit** — `1.d4 d5 2.c4 e5 3.dxe5 d4 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D08_Albin_Countergambit.md#_Nf3_) (live-tagged the *Normal Line*)
- **Queen's Gambit, Declined,  Albin Counter-Gambit,  Alapin Variation** — `1.d4 d5 2.c4 e5 3.dxe5 d4 4.Nf3 Nc6 5.Nbd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D08_Albin_Countergambit.md#_Modern_) (live-tagged the *Modern Line* instead — a real name divergence)
- **Queen's Gambit, Declined,  Albin Counter-Gambit,  Krenosz Variation** — `1.d4 d5 2.c4 e5 3.dxe5 d4 4.Nf3 Nc6 5.Nbd2 Bg4 6.h3 Bxf3 7.Nxf3 Bb4 8.Bd2 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D08_Albin_Countergambit.md#_Krenosz_) (genuine database rarity, 7 masters games)
- **Queen's Gambit, Declined,  Albin Counter-Gambit,  Janowski Variation** — `1.d4 d5 2.c4 e5 3.dxe5 d4 4.Nf3 Nc6 5.Nbd2 f6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D08_Albin_Countergambit.md#_Janowski08_) (a real finding: this name is reused from D07's own unrelated "Janowski Variation" — both named for Dawid Janowski)
- **Queen's Gambit, Declined,  Albin Counter-Gambit,  Balogh Variation** — `1.d4 d5 2.c4 e5 3.dxe5 d4 4.Nf3 Nc6 5.Nbd2 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D08_Albin_Countergambit.md#_Balogh_)

## D09

- **Queen's Gambit, Declined,  Albin Counter-Gambit,  5.g3** — `1.d4 d5 2.c4 e5 3.dxe5 d4 4.Nf3 Nc6 5.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D09_Albin_Countergambit_Fianchetto.md#_initial_move_) (live-tagged the *Fianchetto Variation*)

## D10

- **Queen's Gambit, Declined,  Slav Defence** — `1.d4 d5 2.c4 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D10_Slav_Defense.md#_initial_move_)
- **Queen's Gambit, Declined,  Slav Defence,  Alekhine Variation** — `1.d4 d5 2.c4 c6 3.Nc3 dxc4 4.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D10_Slav_Defense.md#_Alekhine10_) — live-tagged the *Slav Gambit, Alekhine Attack*, unrelated to D15's own "Slav Gambit"
- **Queen's Gambit, Declined,  Slav Defence,  Winawer Counter-Gambit** — `1.d4 d5 2.c4 c6 3.Nc3 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D10_Slav_Defense.md#_Winawer_)
- **Queen's Gambit, Declined,  Slav Defence,  Exchange Variation** — `1.d4 d5 2.c4 c6 3.cxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D10_Slav_Defense.md#_Exchange10_) — left untagged live (`opening=None`)

## D11

- **Queen's Gambit, Declined,  Slav Defence,  3.Nf3** — `1.d4 d5 2.c4 c6 3.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D11_Slav_Defense_Modern_Line.md#_initial_move_) — migrated out of D06's own "Queen's Gambit" card, where it had been built as if it stayed there
- **Queen's Gambit, Declined,  Slav Defence,  Breyer Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nbd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D11_Slav_Defense_Modern_Line.md#_Breyer_)
- **Queen's Gambit, Declined,  Slav Defence,  4.e3** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D11_Slav_Defense_Modern_Line.md#_e3_) — live-tagged the *Quiet Variation*

## D12

- **Queen's Gambit, Declined,  Slav Defence,  4.e3 Bf5** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.e3 Bf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D12_Slav_Defense_Schallopp_Defense.md#_initial_move_) — live-tagged the *Quiet Variation, Schallopp Defense*
- **Queen's Gambit, Declined,  Slav Defence,  Landau Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.e3 Bf5 5.cxd5 cxd5 6.Qb3 Qc8 7.Bd2 e6 8.Na3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D12_Slav_Defense_Schallopp_Defense.md#_Landau_)
- **Queen's Gambit, Declined,  Slav Defence,  Exchange Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.e3 Bf5 5.cxd5 cxd5 6.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D12_Slav_Defense_Schallopp_Defense.md#_Exchange12_) — live explorer tags this exact position **D13**, "Schallopp Variation", a real eco.md-vs-live code discrepancy, not just a name one
- **Queen's Gambit, Declined,  Slav Defence,  Amsterdam Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.e3 Bf5 5.cxd5 cxd5 6.Nc3 e6 7.Ne5 Nfd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D12_Slav_Defense_Schallopp_Defense.md#_Amsterdam_)

## D13

- **Queen's Gambit, Declined,  Slav Defence,  Exchange Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.cxd5 cxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D13_Slav_Defense_Exchange_Variation.md#_initial_move_) — a different move order from D12's own "Exchange Variation" (cxd5 played before e3/Bf5, not after)

## D14

- **Queen's Gambit, Declined,  Slav Defence,  Exchange Variation,  6.Bf4 Bf5** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.cxd5 cxd5 5.Nc3 Nc6 6.Bf4 Bf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D14_Slav_Defense_Symmetrical_Line.md#_initial_move_) — live-tagged the *Symmetrical Line*
- **Queen's Gambit, Declined,  Slav Defence,  Exchange,  Trifunovic Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.cxd5 cxd5 5.Nc3 Nc6 6.Bf4 Bf5 7.e3 e6 8.Qb3 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D14_Slav_Defense_Symmetrical_Line.md#_Trifunovic_)

## D15

- **Queen's Gambit, Declined,  Slav Defence,  4.Nc3** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D15_Slav_Defense_Three_Knights.md#_initial_move_) — live-tagged the *Three Knights Variation*
- **Queen's Gambit, Declined,  Slav Defence,  Suechting Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 Qb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D15_Slav_Defense_Three_Knights.md#_Suechting_)
- **Queen's Gambit, Declined,  Slav Defence,  Schlechter Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D15_Slav_Defense_Three_Knights.md#_Schlechter_)
- **Queen's Gambit, Declined,  Slav Defence Accepted** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D15_Slav_Defense_Three_Knights.md#_Accepted_) — live-tagged the *Two Knights Attack*
- **Queen's Gambit, Declined,  Slav Defence,  5.e3 (Alekhine Variation)** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D15_Slav_Defense_Three_Knights.md#_Alekhine15_) — unrelated to D10's own "Alekhine"-named line
- **Queen's Gambit, Declined,  Slav Defence,  Slav Gambit** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D15_Slav_Defense_Three_Knights.md#_SlavGambit_) — live-tagged the *Geller Gambit*
- **Queen's Gambit, Declined,  Slav Defence,  Tolush-Geller Gambit** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.e4 b5 6.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D15_Slav_Defense_Three_Knights.md#_TolushGeller_)

## D16

- **Queen's Gambit, Declined,  Slav Defence Accepted,  Alapin Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D16_Slav_Defense_Alapin_Variation.md#_initial_move_)
- **Queen's Gambit, Declined,  Slav Defence,  Smyslov Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4 Na6 6.e4 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D16_Slav_Defense_Alapin_Variation.md#_Smyslov_)
- **Queen's Gambit, Declined,  Slav Defence,  Soultanbeieff Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D16_Slav_Defense_Alapin_Variation.md#_Soultanbeieff_)
- **Queen's Gambit, Declined,  Slav Defence,  Steiner Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D16_Slav_Defense_Alapin_Variation.md#_Steiner_)

## D17

- **Queen's Gambit, Declined,  Slav Defence,  Czech Defence** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4 Bf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D17_Slav_Defense_Czech_Defence.md#_initial_move_) — live-tagged the *Czech Variation*
- **Queen's Gambit, Declined,  Slav Defence,  Krause Attack** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4 Bf5 6.Ne5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D17_Slav_Defense_Czech_Defence.md#_Krause_)
- **Queen's Gambit, Declined,  Slav Defence,  Carlsbad Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4 Bf5 6.Ne5 Nbd7 7.Nxc4 Qc7 8.g3 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D17_Slav_Defense_Czech_Defence.md#_Carlsbad_)
- **Queen's Gambit, Declined,  Slav Defence,  Wiesbaden Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4 Bf5 6.Ne5 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D17_Slav_Defense_Czech_Defence.md#_Wiesbaden_)

## D18

- **Queen's Gambit, Declined,  Slav Defence,  Dutch Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4 Bf5 6.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D18_Slav_Defense_Dutch_Variation.md#_initial_move_) — live-tagged the *Classical System*; first of three D10-D19 entries independently reusing the name "Dutch Variation"
- **Queen's Gambit, Declined,  Slav Defence,  Dutch,  Lasker Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4 Bf5 6.e3 Na6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D18_Slav_Defense_Dutch_Variation.md#_Lasker_) — unrelated to D08's own Lasker Trap

## D19

- **Queen's Gambit, Declined,  Slav Defence,  Dutch Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4 Bf5 6.e3 e6 7.Bxc4 Bb4 8.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D19_Slav_Defense_Dutch_Variation_Main_Line.md#_initial_move_) — live-tagged the *Czech Variation, Dutch Variation*; second reuse of the "Dutch Variation" name
- **Queen's Gambit, Declined,  Slav Defence,  Dutch Variation,  Main line** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4 Bf5 6.e3 e6 7.Bxc4 Bb4 8.O-O O-O 9.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D19_Slav_Defense_Dutch_Variation_Main_Line.md#_MainLine_) — third reuse of the "Dutch Variation" name
- **Queen's Gambit, Declined,  Slav Defence,  Dutch,  Saemisch Variation** — `1.d4 d5 2.c4 c6 3.Nf3 Nf6 4.Nc3 dxc4 5.a4 Bf5 6.e3 e6 7.Bxc4 Bb4 8.O-O O-O 9.Qe2 Ne4 10.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D19_Slav_Defense_Dutch_Variation_Main_Line.md#_Saemisch_)

## D20

- **Queen's Gambit, Accepted** — `1.d4 d5 2.c4 dxc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D20_Queens_Gambit_Accepted.md#_initial_move_) — migrated out of D06's own "Queen's Gambit" card (only a thin NOTE box there, now trimmed to an outbound link)
- **Queen's Gambit, Accepted,  3.e4** — `1.d4 d5 2.c4 dxc4 3.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D20_Queens_Gambit_Accepted.md#_e4_) — live-tagged the *Saduleto Variation*
- **Queen's Gambit, Accepted,  Linares Variation** — `1.d4 d5 2.c4 dxc4 3.e4 c5 4.d5 Nf6 5.Nc3 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D20_Queens_Gambit_Accepted.md#_Linares_)
- **Queen's Gambit, Accepted,  Schwartz Defence** — `1.d4 d5 2.c4 dxc4 3.e4 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D20_Queens_Gambit_Accepted.md#_Schwartz_) — 0 masters games in the sample

## D21

- **Queen's Gambit, Accepted,  3.Nf3** — `1.d4 d5 2.c4 dxc4 3.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D21_Queens_Gambit_Accepted_Normal_Variation.md#_initial_move_) — live-tagged the *Normal Variation* (reused, unrelated, at D25's own 4.e3)
- **Queen's Gambit, Accepted,  Ericson Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D21_Queens_Gambit_Accepted_Normal_Variation.md#_Ericson_) — live-tagged the *Slav Gambit*, a striking cross-code name clash with D15's own eco.md-titled "Slav Gambit" (live-tagged *Geller Gambit* there instead)
- **Queen's Gambit, Accepted,  Alekhine Defence,  Borisenko-Furman Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 a6 4.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D21_Queens_Gambit_Accepted_Normal_Variation.md#_BorisenkoFurman_) — reached back from D22's own 4.e4 fork

## D22

- **Queen's Gambit, Accepted,  Alekhine Defence** — `1.d4 d5 2.c4 dxc4 3.Nf3 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D22_Queens_Gambit_Accepted_Alekhine_Defense.md#_initial_move_)
- **Queen's Gambit, Accepted,  Alekhine Defence,  Alatortsev Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 a6 4.e3 Bg4 5.Bxc4 e6 6.d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D22_Queens_Gambit_Accepted_Alekhine_Defense.md#_Alatortsev_)
- **Queen's Gambit, Accepted,  Haberditz Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 a6 4.e3 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D22_Queens_Gambit_Accepted_Alekhine_Defense.md#_Haberditz_)

## D23

- **Queen's Gambit, Accepted** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D23_Queens_Gambit_Accepted.md#_initial_move_) — `eco.md` itself reuses the bare root name one ply deeper here
- **Queen's Gambit, Accepted,  Mannheim Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.Qa4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D23_Queens_Gambit_Accepted.md#_Mannheim_)

## D24

- **Queen's Gambit, Accepted,  4.Nc3** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D24_Queens_Gambit_Accepted_Showalter_Variation.md#_initial_move_) — live-tagged the *Showalter Variation*
- **Queen's Gambit, Accepted,  Bogolyubov Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.Nc3 a6 5.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D24_Queens_Gambit_Accepted_Showalter_Variation.md#_Bogolyubov_) — live-spelled the *Bogoljubow Defense*, the same spelling divergence already seen at C91

## D25

- **Queen's Gambit, Accepted,  4.e3** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D25_Queens_Gambit_Accepted_Normal_Variation.md#_initial_move_) — live-tagged the *Normal Variation* (a second, unrelated reuse of D21's own name)
- **Queen's Gambit, Accepted,  Smyslov Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D25_Queens_Gambit_Accepted_Normal_Variation.md#_Smyslov_) — unrelated to D16's own Smyslov Variation
- **Queen's Gambit, Accepted,  Janowsky-Larsen Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D25_Queens_Gambit_Accepted_Normal_Variation.md#_JanowskyLarsen_)
- **Queen's Gambit, Accepted,  Flohr Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 Be6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D25_Queens_Gambit_Accepted_Normal_Variation.md#_Flohr_) — unrelated to D28's own Classical, Flohr Variation

## D26

- **Queen's Gambit, Accepted,  4...e6** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D26_Queens_Gambit_Accepted_Traditional_System.md#_initial_move_) — live-tagged the *Normal Variation, Traditional System*
- **Queen's Gambit, Accepted,  Classical Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D26_Queens_Gambit_Accepted_Traditional_System.md#_Classical_) — live-spelled the *Classical Defense*
- **Queen's Gambit, Accepted,  Classical,  Furman Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.Qe2 a6 7.dxc5 Bxc5 8.O-O Nc6 9.e4 b5 10.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D26_Queens_Gambit_Accepted_Traditional_System.md#_Furman_)
- **Queen's Gambit, Accepted,  Classical Variation,  6.O-O** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D26_Queens_Gambit_Accepted_Traditional_System.md#_6OO_) — live-tagged the *Classical Defense, Normal Line*
- **Queen's Gambit, Accepted,  Classical,  Steinitz Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.O-O cxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D26_Queens_Gambit_Accepted_Traditional_System.md#_Steinitz_)

## D27

- **Queen's Gambit, Accepted,  Classical,  6...a6** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.O-O a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D27_Queens_Gambit_Accepted_Classical_Main_Line.md#_initial_move_) — live-tagged the *Classical Defense, Main Line*
- **Queen's Gambit, Accepted,  Classical,  Rubinstein Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.O-O a6 7.a4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D27_Queens_Gambit_Accepted_Classical_Main_Line.md#_Rubinstein_)
- **Queen's Gambit, Accepted,  Classical,  Geller Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.O-O a6 7.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D27_Queens_Gambit_Accepted_Classical_Main_Line.md#_Geller_) — unrelated to D15's own Geller Gambit/Tolush-Geller Gambit

## D28

- **Queen's Gambit, Accepted,  Classical,  7.Qe2** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.O-O a6 7.Qe2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D28_Queens_Gambit_Accepted_Classical_Alekhine_System.md#_initial_move_) — live-tagged the *Alekhine System*, unrelated to D22's own Alekhine Defense
- **Queen's Gambit, Accepted,  Classical,  7...b5** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.O-O a6 7.Qe2 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D28_Queens_Gambit_Accepted_Classical_Alekhine_System.md#_b5_)
- **Queen's Gambit, Accepted,  Classical,  Flohr Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.O-O a6 7.Qe2 b5 8.Bb3 Nc6 9.Rd1 c4 10.Bc2 Nb4 11.Nc3 Nxc2 12.Qxc2 Bb7 13.d5 Qc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D28_Queens_Gambit_Accepted_Classical_Alekhine_System.md#_Flohr_) — unrelated to D25's own Flohr Variation; 13 moves deep, one of the deepest lines in this D-series sweep

## D29

- **Queen's Gambit, Accepted,  Classical,  8...Bb7** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.O-O a6 7.Qe2 b5 8.Bb3 Bb7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D29_Queens_Gambit_Accepted_Classical_Smyslov_Variation.md#_initial_move_) — live-tagged the *Classical Defense, Alekhine System, Main Line*
- **Queen's Gambit, Accepted,  Classical,  Smyslov Variation** — `1.d4 d5 2.c4 dxc4 3.Nf3 Nf6 4.e3 e6 5.Bxc4 c5 6.O-O a6 7.Qe2 b5 8.Bb3 Bb7 9.Rd1 Nbd7 10.Nc3 Bd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D29_Queens_Gambit_Accepted_Classical_Smyslov_Variation.md#_Smyslov_) — a third, unrelated Smyslov Variation alongside D16's and D25's own

## D30

- **Queen's Gambit, Declined** — `1.d4 d5 2.c4 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D30_Queens_Gambit_Declined.md#_initial_move_) — carries the entire 3.Nf3 system; migrated out of D06's own "Queen's Gambit" card, where it had been built as a thin NOTE box
- **Queen's Gambit, Declined,  Slav Defence** — `1.d4 d5 2.c4 e6 3.Nf3 Nf6 4.e3 c6 5.Nbd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D30_Queens_Gambit_Declined.md#_Nbd2_) — live-tagged the *Semi-Slav Defense: Quiet Variation*
- **Queen's Gambit, Declined,  Stonewall Variation** — `1.d4 d5 2.c4 e6 3.Nf3 Nf6 4.e3 c6 5.Nbd2 Ne4 6.Bd3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D30_Queens_Gambit_Declined.md#_Stonewall_)
- **Queen's Gambit, Declined,  Slav Defence** — `1.d4 d5 2.c4 e6 3.Nf3 Nf6 4.e3 c6 5.Nbd2 Nbd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D30_Queens_Gambit_Declined.md#_Nbd7_) — second reuse of the "Slav Defence" name, also live-tagged *Semi-Slav Defense: Quiet Variation*
- **Queen's Gambit, Declined,  Slav Defence,  Semmering Variation** — `1.d4 d5 2.c4 e6 3.Nf3 Nf6 4.e3 c6 5.Nbd2 Nbd7 6.Bd3 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D30_Queens_Gambit_Declined.md#_Semmering_)
- **Queen's Gambit, Declined,  Spielmann Variation** — `1.d4 d5 2.c4 e6 3.Nf3 Nf6 4.e3 c6 5.Nbd2 g6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D30_Queens_Gambit_Declined.md#_Spielmann_)
- **Queen's Gambit, Declined** — `1.d4 d5 2.c4 e6 3.Nf3 Nf6 4.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D30_Queens_Gambit_Declined.md#_Bg5_) — reuses the card's own root name; live-tagged the *Traditional Variation*
- **Queen's Gambit, Declined,  Capablanca Variation** — `1.d4 d5 2.c4 e6 3.Nf3 Nf6 4.Bg5 Nbd7 5.e3 c6 6.Nbd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D30_Queens_Gambit_Declined.md#_Capablanca_)
- **Queen's Gambit, Declined,  Vienna Variation** — `1.d4 d5 2.c4 e6 3.Nf3 Nf6 4.Bg5 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D30_Queens_Gambit_Declined.md#_Vienna_) — unrelated to D39's own, much deeper Ragozin-tree "Vienna Variation"
- **Queen's Gambit, Declined,  Capablanca-Duras Variation** — `1.d4 d5 2.c4 e6 3.Nf3 Nf6 4.Bg5 h6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D30_Queens_Gambit_Declined.md#_CapablancaDuras_) — live explorer tags both this and the 4...Nbd7 node identically, just "Capablanca Variation"
- **Queen's Gambit, Declined,  Hastings Variation** — `1.d4 d5 2.c4 e6 3.Nf3 Nf6 4.Bg5 h6 5.Bxf6 Qxf6 6.Nc3 c6 7.Qb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D30_Queens_Gambit_Declined.md#_Hastings_) — live explorer tags this exact position **D43**, a genuine eco.md-vs-live code discrepancy

## D31

- **Queen's Gambit, Declined,  3.Nc3** — `1.d4 d5 2.c4 e6 3.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D31_Queens_Gambit_Declined_Queens_Knight_Variation.md#_initial_move_) — live-tagged the *Queen's Knight Variation*; migrated out of D06's own "Queen's Gambit" card
- **Queen's Gambit, Declined,  Janowski Variation** — `1.d4 d5 2.c4 e6 3.Nc3 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D31_Queens_Gambit_Declined_Queens_Knight_Variation.md#_Janowski_) — a third, unrelated "Janowski"-named line in this repo (see also D07, D08)
- **Queen's Gambit, Declined,  Alapin Variation** — `1.d4 d5 2.c4 e6 3.Nc3 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D31_Queens_Gambit_Declined_Queens_Knight_Variation.md#_Alapin31_) — an extreme rarity, only 7 masters games
- **Queen's Gambit, Declined,  Charousek Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D31_Queens_Gambit_Declined_Queens_Knight_Variation.md#_Charousek_)
- **Queen's Gambit, Declined,  Semi-Slav** — `1.d4 d5 2.c4 e6 3.Nc3 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D31_Queens_Gambit_Declined_Queens_Knight_Variation.md#_SemiSlav_) — live-tagged the *Semi-Slav Defense: Accelerated Move Order*
- **Queen's Gambit, Declined,  Semi-Slav,  Noteboom Variation** — `1.d4 d5 2.c4 e6 3.Nc3 c6 4.Nf3 dxc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D31_Queens_Gambit_Declined_Queens_Knight_Variation.md#_Noteboom_)
- **Queen's Gambit, Declined,  Semi-Slav,  Koomen Variation** — `1.d4 d5 2.c4 e6 3.Nc3 c6 4.Nf3 dxc4 5.a4 Bb4 6.e3 b5 7.Bd2 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D31_Queens_Gambit_Declined_Queens_Knight_Variation.md#_Koomen_)
- **Queen's Gambit, Declined,  Semi-Slav,  Junge Variation** — `1.d4 d5 2.c4 e6 3.Nc3 c6 4.Nf3 dxc4 5.a4 Bb4 6.e3 b5 7.Bd2 Qb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D31_Queens_Gambit_Declined_Queens_Knight_Variation.md#_Junge_)
- **Queen's Gambit, Declined,  Semi-Slav,  Abrahams Variation** — `1.d4 d5 2.c4 e6 3.Nc3 c6 4.Nf3 dxc4 5.a4 Bb4 6.e3 b5 7.Bd2 a5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D31_Queens_Gambit_Declined_Queens_Knight_Variation.md#_Abrahams_) — masters' actual overwhelming main try (86.2%) at that fork
- **Queen's Gambit, Declined,  Semi-Slav,  Marshall Gambit** — `1.d4 d5 2.c4 e6 3.Nc3 c6 4.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D31_Queens_Gambit_Declined_Queens_Knight_Variation.md#_MarshallGambit31_) — unrelated to D32's own, much deeper Tarrasch-tree "Marshall Gambit"

## D32

- **Queen's Gambit, Declined,  Tarrasch Defence** — `1.d4 d5 2.c4 e6 3.Nc3 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D32_Tarrasch_Defense.md#_initial_move_)
- **Queen's Gambit, Declined,  Tarrasch,  von Hennig-Schara Gambit** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 cxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D32_Tarrasch_Defense.md#_Schara_) — live explorer drops the "von Hennig" half, tagging it just the *Schara Gambit*
- **Queen's Gambit, Declined,  Tarrasch Defence,  4.cd ed** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D32_Tarrasch_Defense.md#_exd5_)
- **Queen's Gambit, Declined,  Tarrasch Defence,  Tarrasch Gambit** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.dxc5 d4 6.Na4 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D32_Tarrasch_Defense.md#_TarraschGambit_)
- **Queen's Gambit, Declined,  Tarrasch Defence,  Marshall Gambit** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D32_Tarrasch_Defense.md#_MarshallGambit32_) — unrelated to D31's own, much shallower Semi-Slav "Marshall Gambit"
- **Queen's Gambit, Declined,  Tarrasch Defence** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D32_Tarrasch_Defense.md#_Nf3_)

## D33

- **Queen's Gambit, Declined,  Tarrasch,  Schlechter-Rubinstein System** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.Nf3 Nc6 6.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D33_Tarrasch_Defense_Rubinstein_System.md#_initial_move_) — live-tagged simply the *Rubinstein System*
- **Queen's Gambit, Declined,  Tarrasch,  Folkestone (Swedish) Variation** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.Nf3 Nc6 6.g3 c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D33_Tarrasch_Defense_Rubinstein_System.md#_Folkestone_)
- **Queen's Gambit, Declined,  Tarrasch,  Schlechter-Rubinstein System,  Rey Ardid Variation** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.Nf3 Nc6 6.g3 c4 7.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D33_Tarrasch_Defense_Rubinstein_System.md#_ReyArdid_)
- **Queen's Gambit, Declined,  Tarrasch,  Prague Variation** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.Nf3 Nc6 6.g3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D33_Tarrasch_Defense_Rubinstein_System.md#_Prague_)
- **Queen's Gambit, Declined,  Tarrasch,  Wagner Variation** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.Nf3 Nc6 6.g3 Nf6 7.Bg2 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D33_Tarrasch_Defense_Rubinstein_System.md#_Wagner_)

## D34

- **Queen's Gambit, Declined,  Tarrasch,  Prague Variation,  7...Be7** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.Nf3 Nc6 6.g3 Nf6 7.Bg2 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D34_Tarrasch_Defense_Prague_Main_Line.md#_initial_move_) — live explorer already compounds the name here, "Prague Variation, Main Line"
- **Queen's Gambit, Declined,  Tarrasch,  Prague Variation,  Normal position** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.Nf3 Nc6 6.g3 Nf6 7.Bg2 Be7 8.O-O O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D34_Tarrasch_Defense_Prague_Main_Line.md#_Normal_) — live-tagged the *Classical Variation* instead, a real, substantial name divergence
- **Queen's Gambit, Declined,  Tarrasch,  Reti Variation** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.Nf3 Nc6 6.g3 Nf6 7.Bg2 Be7 8.O-O O-O 9.dxc5 Bxc5 10.Na4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D34_Tarrasch_Defense_Prague_Main_Line.md#_Reti_)
- **Queen's Gambit, Declined,  Tarrasch,  Prague Variation,  9.Bg5** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.Nf3 Nc6 6.g3 Nf6 7.Bg2 Be7 8.O-O O-O 9.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D34_Tarrasch_Defense_Prague_Main_Line.md#_Prague9Bg5_) — live-tagged the *Classical Variation, Carlsbad Variation* instead, unrelated to D17's own Slav Carlsbad Variation
- **Queen's Gambit, Declined,  Tarrasch,  Bogolyubov Variation** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.Nf3 Nc6 6.g3 Nf6 7.Bg2 Be7 8.O-O O-O 9.Bg5 Be6 10.Rc1 c4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D34_Tarrasch_Defense_Prague_Main_Line.md#_Bogolyubov_) — `eco.md`'s own spelling here, unlike the live-preferred "Bogoljubow" seen elsewhere in this repo
- **Queen's Gambit, Declined,  Tarrasch,  Stoltz Variation** — `1.d4 d5 2.c4 e6 3.Nc3 c5 4.cxd5 exd5 5.Nf3 Nc6 6.g3 Nf6 7.Bg2 Be7 8.O-O O-O 9.Bg5 Be6 10.Rc1 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D34_Tarrasch_Defense_Prague_Main_Line.md#_Stoltz_)

## D35

- **Queen's Gambit, Declined,  3...Nf6** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D35_Queens_Gambit_Declined_Normal_Defense.md#_initial_move_) — live-tagged the *Normal Defense*
- **Queen's Gambit, Declined,  Harrwitz Attack** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D35_Queens_Gambit_Declined_Normal_Defense.md#_Harrwitz_) — a genuine blitz trap (0.5% masters vs 5.5% online)
- **Queen's Gambit, Declined,  Exchange Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.cxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D35_Queens_Gambit_Declined_Normal_Defense.md#_Exchange_)
- **Queen's Gambit, Declined,  Exchange,  Saemisch Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.cxd5 exd5 5.Nf3 Nbd7 6.Bf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D35_Queens_Gambit_Declined_Normal_Defense.md#_Saemisch_) — live-spelled the umlauted *Sämisch Variation*; a genuine rarity (0.5% masters) versus 5.Bg5's 98.1%
- **Queen's Gambit, Declined,  Exchange,  positional line** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.cxd5 exd5 5.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D35_Queens_Gambit_Declined_Normal_Defense.md#_Positional_) — masters' true main try (98.1%) at this fork
- **Queen's Gambit, Declined,  Exchange,  Chameleon Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 8.Qc2 Re8 9.Nge2 Nf8 10.O-O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D35_Queens_Gambit_Declined_Normal_Defense.md#_Chameleon_)
- **Queen's Gambit, Declined,  Exchange,  positional line,  5...c6** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.cxd5 exd5 5.Bg5 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D35_Queens_Gambit_Declined_Normal_Defense.md#_Positional5c6_)

## D36

- **Queen's Gambit, Declined,  Exchange,  positional line,  6.Qc2** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.cxd5 exd5 5.Bg5 c6 6.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D36_Queens_Gambit_Declined_Exchange_Positional_Qc2.md#_initial_move_)

## D37

- **Queen's Gambit, Declined,  4.Nf3** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D37_Queens_Gambit_Declined_Three_Knights_Variation.md#_initial_move_) — live-tagged the *Three Knights Variation*, the same generic naming pattern as D15's own Slav Three Knights
- **Queen's Gambit, Declined,  Classical Variation (5.Bf4)** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 Be7 5.Bf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D37_Queens_Gambit_Declined_Three_Knights_Variation.md#_Classical_) — this exact SAN move order is left completely untagged live, almost certainly reached by transposition in practice

## D38

- **Queen's Gambit, Declined,  Ragozin Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D38_Queens_Gambit_Declined_Ragozin_Defense.md#_initial_move_) — live-spelled the *Ragozin Defense*

## D39

- **Queen's Gambit, Declined,  Ragozin,  Vienna Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 Bb4 5.Bg5 dxc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D39_Queens_Gambit_Declined_Ragozin_Vienna_Variation.md#_initial_move_) — unrelated to D30's own, much shallower "Vienna Variation"

## D40

- **Queen's Gambit, Declined,  Semi-Tarrasch Defence** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D40_Semi_Tarrasch_Defense.md#_initial_move_)
- **Queen's Gambit, Declined,  Semi-Tarrasch,  Symmetrical Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c5 5.e3 Nc6 6.Bd3 Bd6 7.O-O O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D40_Semi_Tarrasch_Defense.md#_Symmetrical_) — a genuine database rarity at this exact move order (3 masters games)
- **Queen's Gambit, Declined,  Semi-Tarrasch,  Levenfish Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c5 5.e3 Nc6 6.Bd3 Bd6 7.O-O O-O 8.Qe2 Qe7 9.dxc5 Bxc5 10.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D40_Semi_Tarrasch_Defense.md#_Levenfish_)
- **Queen's Gambit, Declined,  Semi-Tarrasch Defence,  Pillsbury Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c5 5.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D40_Semi_Tarrasch_Defense.md#_Pillsbury_) — a genuine blitz trap (0.7% masters vs 30.4% online)

## D41

- **Queen's Gambit, Declined,  Semi-Tarrasch,  5.cd** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c5 5.cxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D41_Semi_Tarrasch_cxd5.md#_initial_move_)
- **Queen's Gambit, Declined,  Semi-Tarrasch,  Kmoch Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c5 5.cxd5 Nxd5 6.e4 Nxc3 7.bxc3 cxd4 8.cxd4 Bb4 9.Bd2 Bxd2 10.Qxd2 O-O 11.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D41_Semi_Tarrasch_cxd5.md#_Kmoch_)
- **Queen's Gambit, Declined,  Semi-Tarrasch,  San Sebastian Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c5 5.cxd5 Nxd5 6.e4 Nxc3 7.bxc3 cxd4 8.cxd4 Bb4 9.Bd2 Qa5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D41_Semi_Tarrasch_cxd5.md#_SanSebastian_)
- **Queen's Gambit, Declined,  Semi-Tarrasch With e3** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c5 5.cxd5 Nxd5 6.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D41_Semi_Tarrasch_cxd5.md#_e3_) — left with no independent live tag, inheriting the Pillsbury Variation tag

## D42

- **Queen's Gambit, Declined,  Semi-Tarrasch,  7.Bd3** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c5 5.cxd5 Nxd5 6.e3 Nc6 7.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D42_Semi_Tarrasch_Main_Line.md#_initial_move_) — live-tagged the *Main Line*

## D43

- **Queen's Gambit, Declined,  Semi-Slav** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D43_Semi_Slav_Defense.md#_initial_move_) — its own code, though D37's own prose originally missed this and said otherwise (now corrected)
- **Queen's Gambit, Declined,  Semi-Slav,  Hastings Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.Bg5 h6 6.Bxf6 Qxf6 7.Qb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D43_Semi_Slav_Defense.md#_Hastings_) — the exact same position as D30's own Hastings Variation, reached by transposition; live-tagged this code (D43) rather than D30's own

## D44

- **Queen's Gambit, Declined,  Semi-Slav,  5.Bg5 dc** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.Bg5 dxc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D44_Semi_Slav_Accepted.md#_initial_move_) — live-tagged the *Semi-Slav Defense Accepted*
- **Queen's Gambit, Declined,  Semi-Slav,  Botvinnik System** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.Bg5 dxc4 6.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D44_Semi_Slav_Accepted.md#_Botvinnik_) — live-spelled the *Botvinnik Variation*
- **Queen's Gambit, Declined,  Semi-Slav,  Ekstroem Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.Bg5 dxc4 6.e4 b5 7.e5 h6 8.Bh4 g5 9.exf6 gxh4 10.Ne5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D44_Semi_Slav_Accepted.md#_Ekstroem_)
- **Queen's Gambit, Declined,  Semi-Slav,  Anti-Meran Gambit** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.Bg5 dxc4 6.e4 b5 7.e5 h6 8.Bh4 g5 9.Nxg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D44_Semi_Slav_Accepted.md#_AntiMeranGambit_) — masters' actual main try at that fork (88.8%), not the Ekstroem Variation
- **Queen's Gambit, Declined,  Semi-Slav,  Anti-Meran,  Lilienthal Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.Bg5 dxc4 6.e4 b5 7.e5 h6 8.Bh4 g5 9.Nxg5 hxg5 10.Bxg5 Nbd7 11.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D44_Semi_Slav_Accepted.md#_Lilienthal_)
- **Queen's Gambit, Declined,  Semi-Slav,  Anti-Meran,  Szabo Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.Bg5 dxc4 6.e4 b5 7.e5 h6 8.Bh4 g5 9.Nxg5 hxg5 10.Bxg5 Nbd7 11.Qf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D44_Semi_Slav_Accepted.md#_Szabo_)
- **Queen's Gambit, Declined,  Semi-Slav,  Anti-Meran,  Alatortsev System** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.Bg5 dxc4 6.e4 b5 7.e5 h6 8.Bh4 g5 9.Nxg5 Nd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D44_Semi_Slav_Accepted.md#_Alatortsev_) — unrelated to D22's own Alekhine Defense Alatortsev Variation

## D45

- **Queen's Gambit, Declined,  Semi-Slav,  5.e3** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D45_Semi_Slav_Main_Line.md#_initial_move_) — live-tagged the *Main Line*, reused (unrelated) at D46's own root
- **Queen's Gambit, Declined,  Semi-Slav,  Stonewall Defence** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Ne4 6.Bd3 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D45_Semi_Slav_Main_Line.md#_Stonewall_)
- **Queen's Gambit, Declined,  Semi-Slav,  Accelerated Meran (Alekhine Variation)** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D45_Semi_Slav_Main_Line.md#_AccelMeran_)
- **Queen's Gambit, Declined,  Semi-Slav,  5...Nd7** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D45_Semi_Slav_Main_Line.md#_Nbd7_) — live-tagged the *Normal Variation*
- **Queen's Gambit, Declined,  Semi-Slav,  Stoltz Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D45_Semi_Slav_Main_Line.md#_Stoltz_) — unrelated to D34's own Tarrasch-tree Stoltz Variation
- **Queen's Gambit, Declined,  Semi-Slav,  Rubinstein (Anti-Meran) System** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Ne5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D45_Semi_Slav_Main_Line.md#_Rubinstein_) — unrelated to D27's own Classical-tree Rubinstein Variation

## D46

- **Queen's Gambit, Declined,  Semi-Slav,  6.Bd3** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D46_Semi_Slav_Bogoljubow.md#_initial_move_) — live-tagged the *Main Line*, the third reuse of this exact name across D43-D49
- **Queen's Gambit, Bogolyubov Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D46_Semi_Slav_Bogoljubow.md#_Bogolyubov_) — the only entry in this whole D-series dropping the "Declined" qualifier; live-spelled the *Bogoljubow Variation*
- **Queen's Gambit, Declined,  Semi-Slav,  Romih Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D46_Semi_Slav_Bogoljubow.md#_Romih_)
- **Queen's Gambit, Declined,  Semi-Slav,  Chigorin Defence** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 Bd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D46_Semi_Slav_Bogoljubow.md#_Chigorin_) — unrelated to D07's own Chigorin Defense

## D47

- **Queen's Gambit, Declined,  Semi-Slav,  7.Bc4** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D47_Semi_Slav_Semi_Meran.md#_initial_move_) — live-tagged the *Semi-Meran Variation*
- **Queen's Gambit, Declined,  Semi-Slav,  Meran Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D47_Semi_Slav_Semi_Meran.md#_Meran_) — the single most heavily analysed structure in this whole D-series
- **Queen's Gambit, Declined,  Semi-Slav,  neo-Meran (Lundin Variation)** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D47_Semi_Slav_Semi_Meran.md#_neoMeran_)
- **Queen's Gambit, Declined,  Semi-Slav,  Meran,  Wade Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 Bb7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D47_Semi_Slav_Semi_Meran.md#_Wade_) — masters' actual main try at that fork (49.8%)

## D48

- **Queen's Gambit, Declined,  Semi-Slav,  Meran,  8...a6** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D48_Semi_Slav_Meran_Old_Variation.md#_initial_move_) — reuses the "Meran Variation" name a second time
- **Queen's Gambit, Declined,  Semi-Slav,  Meran,  Pirc Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D48_Semi_Slav_Meran_Old_Variation.md#_Pirc_) — unrelated to the Pirc Defense elsewhere in this repo
- **Queen's Gambit, Declined,  Semi-Slav,  Meran** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D48_Semi_Slav_Meran_Old_Variation.md#_c5_) — a third reuse of the "Meran" name
- **Queen's Gambit, Declined,  Semi-Slav,  Meran,  Reynolds' Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 c5 10.d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D48_Semi_Slav_Meran_Old_Variation.md#_Reynolds_) — a genuinely near-even fork with the old Main line (49.7% vs 50.1%)
- **Queen's Gambit, Declined,  Semi-Slav,  Meran,  old Main line** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 c5 10.e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D49_Semi_Slav_Meran_Blumenfeld.md#_initial_move_) — its own deeper code, [D49](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D49_Semi_Slav_Meran_Blumenfeld.md), live-spelled the *Old Variation*

## D49

- **Queen's Gambit, Declined,  Semi-Slav,  Meran,  Blumenfeld Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 c5 10.e5 cxd4 11.Nxb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D49_Semi_Slav_Meran_Blumenfeld.md#_initial_move_) — unrelated to the Blumenfeld Countergambit elsewhere in this repo's A-series
- **Queen's Gambit, Declined,  Semi-Slav,  Meran,  Rabinovich Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 c5 10.e5 cxd4 11.Nxb5 Ng4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D49_Semi_Slav_Meran_Blumenfeld.md#_Rabinovich_)
- **Queen's Gambit, Declined,  Semi-Slav,  Meran,  Sozin Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 c5 10.e5 cxd4 11.Nxb5 Nxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D49_Semi_Slav_Meran_Blumenfeld.md#_Sozin_) — the first of two unrelated nodes in this D49 range both named "Sozin Variation"
- **Queen's Gambit, Declined,  Semi-Slav,  Meran,  Stahlberg Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 c5 10.e5 cxd4 11.Nxb5 Nxe5 12.Nxe5 axb5 13.Qf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D49_Semi_Slav_Meran_Blumenfeld.md#_Stahlberg_) — masters' actual main try at that fork is the uncoded 13.Bxb5+ (70.0%), not this
- **Queen's Gambit, Declined,  Semi-Slav,  Meran,  Sozin Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 c5 10.e5 cxd4 11.Nxb5 Nxe5 12.Nxe5 axb5 13.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D49_Semi_Slav_Meran_Blumenfeld.md#_Sozin2_) — the second, unrelated reuse of "Sozin Variation" in this same D49 range
- **Queen's Gambit, Declined,  Semi-Slav,  Meran,  Rellstab Attack** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 c6 5.e3 Nbd7 6.Bd3 dxc4 7.Bxc4 b5 8.Bd3 a6 9.e4 c5 10.e5 cxd4 11.Nxb5 Nxe5 12.Nxe5 axb5 13.O-O Qd5 14.Qe2 Ba6 15.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D49_Semi_Slav_Meran_Blumenfeld.md#_Rellstab_) — the deepest named line in this entire D-series sweep (15 moves)

## D50

- **Queen's Gambit, Declined,  4.Bg5** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D50_Queens_Gambit_Declined_Bg5.md#_initial_move_) — live-tagged the *Modern Variation*, the first of three unrelated reuses of this name in this batch (D51, D55); also fixes a "wrong root code" bug on D35, which previously claimed this position transposed into D30
- **Queen's Gambit, Declined,  Been-Koomen Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D50_Queens_Gambit_Declined_Bg5.md#_BeenKoomen_) — a database rarity at masters level (2.0%) that still carries its own code, the mirror image of D58/D59's Tartakower complex
- **Queen's Gambit, Declined,  Semi-Tarrasch,  Krause Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 c5 5.Nf3 cxd4 6.Nxd4 e5 7.Ndb5 a6 8.Qa4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D50_Queens_Gambit_Declined_Bg5.md#_Krause_)
- **Queen's Gambit, Declined,  Semi-Tarrasch,  Primitive Pillsbury Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 c5 5.Nf3 cxd4 6.Qxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D50_Queens_Gambit_Declined_Bg5.md#_PrimitivePillsbury_) — unrelated to D55's own Pillsbury Attack
- **Queen's Gambit, Declined,  Semi-Tarrasch** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 c5 5.cxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D50_Queens_Gambit_Declined_Bg5.md#_SemiTarrasch_) — live-tagged the *Pseudo-Tarrasch Variation*, a real name divergence; masters' own main reply here (5...cxd4, 85.2%) is a different position from D40's own Semi-Tarrasch tree, not a transposition
- **Queen's Gambit, Declined,  Canal Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 c5 5.cxd5 Qb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D50_Queens_Gambit_Declined_Bg5.md#_Canal_) — a notable eval swing, +0.31 to +0.78 in one move

## D51

- **Queen's Gambit, Declined,  4.Bg5 Nbd7** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D51_Queens_Gambit_Declined_Knight_Defense.md#_initial_move_) — live-tagged the *Modern Variation, Knight Defense*, reused (unrelated) from D50's own root
- **Queen's Gambit, Declined,  Rochlin Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.Nf3 c6 6.Rc1 Qa5 7.Bd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D51_Queens_Gambit_Declined_Knight_Defense.md#_Rochlin_) — near-extinct today, 1 masters game out of 4,985 at its own branch point
- **Queen's Gambit, Declined,  Alekhine Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.Nf3 c6 6.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D51_Queens_Gambit_Declined_Knight_Defense.md#_Alekhine_) — a genuine blitz trap (0.2% masters, 4.5% online, over 20x), unrelated to D22's own Alekhine Defense and D45's own Alekhine Variation
- **Queen's Gambit, Declined** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D51_Queens_Gambit_Declined_Knight_Defense.md#_e3_) — reuses the *Modern Variation, Knight Defense* name a second time
- **Queen's Gambit, Declined,  Manhattan Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.e3 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D51_Queens_Gambit_Declined_Knight_Defense.md#_Manhattan_)
- **Queen's Gambit, Declined,  5...c6** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.e3 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D51_Queens_Gambit_Declined_Knight_Defense.md#_c6_) — reuses the *Modern Variation, Knight Defense* name a third time; its own 6.Nf3 is a verified transposition into D52's own root
- **Queen's Gambit, Declined,  Capablanca Anti-Cambridge Springs Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.e3 c6 6.a3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D51_Queens_Gambit_Declined_Knight_Defense.md#_CapaAntiCS_)

## D52

- **Queen's Gambit, Declined** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.e3 c6 6.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D52_Queens_Gambit_Declined_Cambridge_Springs.md#_initial_move_) — reached by two independently `apply_san.py`-verified move orders from D51 (5.e3 c6 6.Nf3 and 5.Nf3 c6 6.e3)
- **Queen's Gambit, Declined,  Cambridge Springs Defence** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.e3 c6 6.Nf3 Qa5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D52_Queens_Gambit_Declined_Cambridge_Springs.md#_CSD_)
- **Queen's Gambit, Declined,  Cambridge Springs Defence,  Bogoljubow Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.e3 c6 6.Nf3 Qa5 7.Nd2 Bb4 8.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D52_Queens_Gambit_Declined_Cambridge_Springs.md#_Bogoljubow_)
- **Queen's Gambit, Declined,  Cambridge Springs Defence,  Argentine Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.e3 c6 6.Nf3 Qa5 7.Nd2 Bb4 8.Qc2 O-O 9.Bh4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D52_Queens_Gambit_Declined_Cambridge_Springs.md#_Argentine_)
- **Queen's Gambit, Declined,  Cambridge Springs Defence,  Rubinstein Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.e3 c6 6.Nf3 Qa5 7.Nd2 dxc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D52_Queens_Gambit_Declined_Cambridge_Springs.md#_Rubinstein_) — unrelated to D20's and D33's own Rubinstein-named lines
- **Queen's Gambit, Declined,  Cambridge Springs Defence,  Capablanca Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.e3 c6 6.Nf3 Qa5 7.Bxf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D52_Queens_Gambit_Declined_Cambridge_Springs.md#_Capablanca_) — masters/online gap: only 3.8% masters vs 30.5% online
- **Queen's Gambit, Declined,  Cambridge Springs Defence,  7.cd** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.e3 c6 6.Nf3 Qa5 7.cxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D52_Queens_Gambit_Declined_Cambridge_Springs.md#_cxd5node_) — live-tagged plain *Cambridge Springs Defense*, same generic label as its own parent node
- **Queen's Gambit, Declined,  Cambridge Springs Defence,  Yugoslav Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Nbd7 5.e3 c6 6.Nf3 Qa5 7.cxd5 Nxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D52_Queens_Gambit_Declined_Cambridge_Springs.md#_Yugoslav_)

## D53

- **Queen's Gambit, Declined,  4.Bg5 Be7** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D53_Queens_Gambit_Declined_Be7.md#_initial_move_)
- **Queen's Gambit, Declined,  Lasker Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D53_Queens_Gambit_Declined_Be7.md#_Lasker_) — live-tagged identically to D56's own, unrelated, *Lasker Defence* (...Ne4 played before castling here, vs after 6.Nf3 h6 7.Bh4 there); essentially unplayed standalone (12 masters games)
- **Queen's Gambit, Declined,  4.Bg5 Be7,  5.e3 O-O** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D53_Queens_Gambit_Declined_Be7.md#_OO_) — left completely untagged live (`opening=None`) despite both its parent and both its real children (D54, D55) being separately tagged

## D54

- **Queen's Gambit, Declined,  Anti-neo-orthodox Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Rc1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D54_Queens_Gambit_Declined_Anti_Neo_Orthodox.md#_initial_move_) — live-tagged plain *Neo-Orthodox Variation* (drops the "Anti-"), colliding with D55's own, unrelated, *Neo-Orthodox Variation* two codes later

## D55

- **Queen's Gambit, Declined,  6.Nf3** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D55_Queens_Gambit_Declined_Neo_Orthodox.md#_initial_move_) — live-tagged the *Modern Variation, Normal Line*, a third unrelated reuse of the "Modern Variation" name (D50, D51)
- **Queen's Gambit, Declined,  Pillsbury Attack** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 b6 7.Bd3 Bb7 8.cxd5 exd5 9.Ne5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D55_Queens_Gambit_Declined_Neo_Orthodox.md#_Pillsbury_) — unrelated to D50's own Primitive Pillsbury Variation
- **Queen's Gambit, Declined,  Neo-orthodox Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D55_Queens_Gambit_Declined_Neo_Orthodox.md#_NeoOrthodox_)
- **Queen's Gambit, Declined,  Neo-orthodox Variation,  7.Bxf6** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bxf6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D55_Queens_Gambit_Declined_Neo_Orthodox.md#_Bxf6_)
- **Queen's Gambit, Declined,  Petrosian Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bxf6 Bxf6 8.Rc1 c6 9.Bd3 Nd7 10.O-O dxc4 11.Bxc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D55_Queens_Gambit_Declined_Neo_Orthodox.md#_Petrosian_)
- **Queen's Gambit, Declined,  Neo-orthodox Variation,  7.Bh4** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D55_Queens_Gambit_Declined_Neo_Orthodox.md#_Bh4_) — live-tagged *Neo-Orthodox Variation, Main Line*; **correction**: masters' actual main reply here is 7...b6 (72.6%, D58's own root) not the historically famous 7...Ne4 Lasker Defence (only 21.2%, D56)

## D56

- **Queen's Gambit, Declined,  Lasker Defence** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D56_Queens_Gambit_Declined_Lasker_Defense.md#_initial_move_) — masters' second choice at its own parent fork (21.2%), behind D58's Tartakower System (72.6%); see D53's own, unrelated, "Lasker Variation" for the naming collision
- **Queen's Gambit, Declined,  Lasker Defence,  Teichmann Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D56_Queens_Gambit_Declined_Lasker_Defense.md#_Teichmann_) — masters' actual main try at this exact fork is the uncoded 9.Rc1 (58.9%), not this
- **Queen's Gambit, Declined,  Lasker Defence,  Russian Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Qc2 Nf6 10.Bd3 dxc4 11.Bxc4 c5 12.O-O Nc6 13.Rfd1 Bd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D56_Queens_Gambit_Declined_Lasker_Defense.md#_Russian_)

## D57

- **Queen's Gambit, Declined,  Lasker Defence,  Main line** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.cxd5 Nxc3 10.bxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D57_Queens_Gambit_Declined_Lasker_Defense_Main_Line.md#_initial_move_) — a real, secondary try at its own parent fork (14.6% masters), also behind the uncoded 9.Rc1
- **Queen's Gambit, Declined,  Lasker Defence,  Bernstein Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.cxd5 Nxc3 10.bxc3 exd5 11.Qb3 Qd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D57_Queens_Gambit_Declined_Lasker_Defense_Main_Line.md#_Bernstein_) — a notable eval jump, +0.07 to +0.46 in one line, the deepest and sharpest line of the whole Lasker Defence complex

## D58

- **Queen's Gambit, Declined,  Tartakower (Makagonov-Bondarevsky) System** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D58_Queens_Gambit_Declined_Tartakower_System.md#_initial_move_) — live-tagged plain *Tartakower Defense* (drops the parenthetical); masters' actual main try here (72.6%) at its own parent D55 fork; here, White's own 8th move is a genuine spread and this card's own D59 link (8.cxd5, 15.4%) trails three uncoded rivals (Be2 26.8%, Bd3 25.1%, Rc1 16.9%)

## D59

- **Queen's Gambit, Declined,  Tartakower (Makagonov-Bondarevsky) System,  8.cd Nxd5** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 b6 8.cxd5 Nxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D59_Queens_Gambit_Declined_Tartakower_Variation.md#_initial_move_) — live-tagged *Tartakower Defense, Makogonov Exchange Variation* (also a spelling divergence, Makagonov/Makogonov)
- **Queen's Gambit, Declined,  Tartakower Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 h6 7.Bh4 b6 8.cxd5 Nxd5 9.Bxe7 Qxe7 10.Nxd5 exd5 11.Rc1 Be6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D59_Queens_Gambit_Declined_Tartakower_Variation.md#_Tartakower_) — the deepest, final named line of this entire D50-D59 batch

## D60

- **Queen's Gambit, Declined,  Orthodox Defence** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D60_Queens_Gambit_Declined_Orthodox_Defense.md#_initial_move_) — completes D55's own forward link (masters' second choice there, 32.8%); its own two named children below both trail the uncoded 7.cxd5 (11.5%), the first of three "coded loses to uncoded rival" instances in this batch
- **Queen's Gambit, Declined,  Orthodox Defence,  Botvinnik Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D60_Queens_Gambit_Declined_Orthodox_Defense.md#_Botvinnik_) — a large masters/online gap (8.1%/33.7%) that stays a plain rectangle, not a formal blitz trap (masters doesn't clear the 2% bar)
- **Queen's Gambit, Declined,  Orthodox Defence,  Rauzer Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Qb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D60_Queens_Gambit_Declined_Orthodox_Defense.md#_Rauzer_) — genuinely understudied everywhere (0.4% masters, 0.6% online), the Been-Koomen/Rochlin pattern again

## D61

- **Queen's Gambit, Declined,  Orthodox Defence,  Rubinstein Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D61_Queens_Gambit_Declined_Rubinstein_Variation.md#_initial_move_)

## D62

- **Queen's Gambit, Declined,  Orthodox Defence,  7.Qc2 c5,  8.cd (Rubinstein)** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Qc2 c5 8.cxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D62_Queens_Gambit_Declined_Rubinstein_8cd.md#_initial_move_) — live-tagged the more specific *Rubinstein Variation, Flohr Line*

## D63

- **Queen's Gambit, Declined,  Orthodox Defence,  7.Rc1** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D63_Queens_Gambit_Declined_7Rc1.md#_initial_move_) — live-tagged plain *Main Line*, the first of three unrelated occurrences of that exact generic tag in this batch
- **Queen's Gambit, Declined,  Orthodox Defence,  Pillsbury Attack** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 b6 8.cxd5 exd5 9.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D63_Queens_Gambit_Declined_7Rc1.md#_Pillsbury_) — unrelated to D55's own Pillsbury Attack; masters' actual plurality (37.2%) at its own fork
- **Queen's Gambit, Declined,  Orthodox Defence,  Capablanca Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 b6 8.cxd5 exd5 9.Bb5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D63_Queens_Gambit_Declined_7Rc1.md#_Capablanca_) — unrelated to D67's own, separately-named "Capablanca System"; trails both Pillsbury and the uncoded 9.Qa4 at its own fork
- **Queen's Gambit, Declined,  Orthodox Defence,  Swiss (Henneberger) Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D63_Queens_Gambit_Declined_7Rc1.md#_Swiss_) — live-tagged plain *Henneberger Variation*, confirming the identity
- **Queen's Gambit, Declined,  Orthodox Defence,  Swiss,  Karlsbad Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 a6 8.cxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D63_Queens_Gambit_Declined_7Rc1.md#_Karlsbad_) — the "Karlsbad" name is reused, unrelated, at D64's own Rubinstein Attack, Karlsbad Variation
- **Queen's Gambit, Declined,  Orthodox Defence** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D63_Queens_Gambit_Declined_7Rc1.md#_c6_) — the deepest sub-tree of the whole batch; live-tagged the same generic *Main Line* as this card's own root, a second unrelated occurrence

## D64

- **Queen's Gambit, Declined,  Orthodox Defence,  Rubinstein Attack (with Rc1)** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D64_Queens_Gambit_Declined_Rubinstein_Attack.md#_initial_move_) — only the second choice at its own parent D63 fork (11.8%), well behind 8.Bd3 (74.2%); both of its own named children below trail the uncoded 8...Re8/8...h6, the second "coded loses to uncoded rival" instance in this batch
- **Queen's Gambit, Declined,  Orthodox Defence,  Rubinstein Attack,  Wolf Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Qc2 Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D64_Queens_Gambit_Declined_Rubinstein_Attack.md#_Wolf_) — only 9.7% masters, trailing both uncoded siblings
- **Queen's Gambit, Declined,  Orthodox Defence,  Rubinstein Attack,  Karlsbad Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Qc2 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D64_Queens_Gambit_Declined_Rubinstein_Attack.md#_Karlsbad_) — the highest-frequency *named* try (22.8%) despite trailing two uncoded siblings; small sample (58 masters games)
- **Queen's Gambit, Declined,  Orthodox Defence,  Rubinstein Attack,  Gruenfeld Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Qc2 a6 9.a3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D64_Queens_Gambit_Declined_Rubinstein_Attack.md#_Gruenfeld_) — named for Ernst Grünfeld, unrelated to the Grünfeld Defence proper (D80-D99)

## D65

- **Queen's Gambit, Declined,  Orthodox Defence,  Rubinstein Attack,  Main line** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Qc2 a6 9.cxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D65_Queens_Gambit_Declined_Rubinstein_Attack_Main_Line.md#_initial_move_) — a fourth unrelated occurrence of a generic "Main Line"-family live tag in this batch; masters' second choice at its own parent fork (27.6%)

## D66

- **Queen's Gambit, Declined,  Orthodox Defence,  Bd3 line** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D66_Queens_Gambit_Declined_Bd3_Line.md#_initial_move_) — the actual main trunk of this whole batch (74.2% masters at its own parent fork), deeper than the Rubinstein Attack complex
- **Queen's Gambit, Declined,  Orthodox Defence,  Bd3 line,  Fianchetto Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Bd3 dxc4 9.Bxc4 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D66_Queens_Gambit_Declined_Bd3_Line.md#_Fianchetto_) — masters' distant second choice (9.1%) at its own fork despite dominating online play (54.6%), a large inversion

## D67

- **Queen's Gambit, Declined,  Orthodox Defence,  Bd3 line,  Capablanca freeing manoevre** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Bd3 dxc4 9.Bxc4 Nd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D67_Queens_Gambit_Declined_Bd3_Line_Capablanca.md#_initial_move_) — live-tagged a genuinely different name, the *Capablanca System* (not just a shortened form); masters' overwhelming main try at its own fork (84.4%)
- **Queen's Gambit, Declined,  Orthodox Defence,  Bd3 line,  Janowski Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Bd3 dxc4 9.Bxc4 Nd5 10.h4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D67_Queens_Gambit_Declined_Bd3_Line_Capablanca.md#_Janowski_) — genuinely understudied everywhere (1.8% masters, 2.1% online)
- **Queen's Gambit, Declined,  Orthodox Defence,  Bd3 line** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Bd3 dxc4 9.Bxc4 Nd5 10.Bxe7 Qxe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D67_Queens_Gambit_Declined_Bd3_Line_Capablanca.md#_BdLine_) — live-tagged the same generic "Bd3 Line" name as D66's own root, an expected, consistent recurrence of `eco.md`'s own hierarchical sub-naming
- **Queen's Gambit, Declined,  Orthodox Defence,  Bd3 line,  Alekhine Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Bd3 dxc4 9.Bxc4 Nd5 10.Bxe7 Qxe7 11.Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D67_Queens_Gambit_Declined_Bd3_Line_Capablanca.md#_Alekhine_) — at least the third independent "Alekhine Variation" reuse in this D-series, after D22's and D51's own
- **Queen's Gambit, Declined,  Orthodox Defence,  Bd3 line,  11.O-O** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Bd3 dxc4 9.Bxc4 Nd5 10.Bxe7 Qxe7 11.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D67_Queens_Gambit_Declined_Bd3_Line_Capablanca.md#_OO_) — live-tagged plain "Main Line," a third, unrelated recurrence of that exact generic tag in this batch (after D63's own root and its own "7...c6" node)

## D68

- **Queen's Gambit, Declined,  Orthodox Defence,  Classical Variation** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Bd3 dxc4 9.Bxc4 Nd5 10.Bxe7 Qxe7 11.O-O Nxc3 12.Rxc3 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D68_Queens_Gambit_Declined_Classical_Variation.md#_initial_move_) — **correction**: masters' actual plurality here is the *Vidmar Variation* (13.Qc2, 29.6%), not the D69-coded 13.dxe5 (only 23.8%, second choice) — the third "coded loses to a rival" instance in this batch
- **Queen's Gambit, Declined,  Orthodox Defence,  Classical,  13.d1b1 (Maroczy)** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Bd3 dxc4 9.Bxc4 Nd5 10.Bxe7 Qxe7 11.O-O Nxc3 12.Rxc3 e5 13.Qb1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D68_Queens_Gambit_Declined_Classical_Variation.md#_Maroczy_) — listed first in `eco.md`'s own entry order but actually the least-played of the three named tries here (5.6%)
- **Queen's Gambit, Declined,  Orthodox Defence,  Classical,  13.d1c2 (Vidmar)** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Bd3 dxc4 9.Bxc4 Nd5 10.Bxe7 Qxe7 11.O-O Nxc3 12.Rxc3 e5 13.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D68_Queens_Gambit_Declined_Classical_Variation.md#_Vidmar_) — masters' actual most-played reply at this fork (29.6%), ahead of both other named tries

## D69

- **Queen's Gambit, Declined,  Orthodox Defence,  Classical,  13.de** — `1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Bg5 Be7 5.e3 O-O 6.Nf3 Nbd7 7.Rc1 c6 8.Bd3 dxc4 9.Bxc4 Nd5 10.Bxe7 Qxe7 11.O-O Nxc3 12.Rxc3 e5 13.dxe5 Nxe5 14.Nxe5 Qxe5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D69_Queens_Gambit_Declined_Classical_13de.md#_initial_move_) — the deepest, final named line of the whole D60-D69 batch, move 15

## D70

- **Gruenfeld Defence, Neo-Gruenfeld Defence** — `1.d4 Nf6 2.c4 g6 3.f3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D70_Neo_Grunfeld_Defense.md#_f3_) — live-tagged the *Goglidze Attack*; White's reply is essentially forced (4.cxd5, 99.9% masters)
- **Gruenfeld Defence, Neo-Gruenfeld Defence,  Kemeri** — `1.d4 Nf6 2.c4 g6 3.g3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D70_Neo_Grunfeld_Defense.md#_initial_move_) — retrofitted from a pre-sweep card built the same batch; the D71/D73 codes below don't actually attach until two plies later (4...Bg7 is live-tagged the generic E60 umbrella, not yet Neo-Grünfeld)

## D71

- **Gruenfeld Defence, Neo-Gruenfeld Defence,  5.cd** — `1.d4 Nf6 2.c4 g6 3.g3 d5 4.Bg2 Bg7 5.cxd5 Nxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D71_Neo_Grunfeld_Exchange_Variation.md#_initial_move_) — live-tagged *Exchange Variation*; verified via `apply_san.py` that the alternate move order (4.cxd5 Nxd5 5.Bg2 Bg7) transposes to the identical position

## D72

- **Gruenfeld Defence, Neo-Gruenfeld Defence,  5.cd,  Main line** — `1.d4 Nf6 2.c4 g6 3.g3 d5 4.Bg2 Bg7 5.cxd5 Nxd5 6.e4 Nb6 7.Ne2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D72_Neo_Grunfeld_Exchange_Main_Line.md#_initial_move_) — live-tagged the same generic "with g3" name as D70's own root, three plies earlier

## D73

- **Gruenfeld Defence, Neo-Gruenfeld Defence,  5.Nf3** — `1.d4 Nf6 2.c4 g6 3.g3 d5 4.Bg2 Bg7 5.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D73_Neo_Grunfeld_Nf3.md#_initial_move_) — a genuine minority pick (8.9% masters) next to 5.cxd5's 89.7%; its own most-played reply, 5...dxc4 (40.4%), stays uncoded, trailing the coded-tree entry 5...O-O (21.6%, only third choice)

## D74

- **Gruenfeld Defence, Neo-Gruenfeld Defence,  6.cd Nxd5,  7.O-O** — `1.d4 Nf6 2.c4 g6 3.g3 d5 4.Bg2 Bg7 5.Nf3 O-O 6.cxd5 Nxd5 7.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D74_Neo_Grunfeld_Delayed_Exchange.md#_initial_move_) — live-tagged *Delayed Exchange Variation*, the first of three unrelated D74-D76 nodes sharing this exact tag

## D75

- **Gruenfeld Defence, Neo-Gruenfeld Defence,  6.cd Nxd5,  7.O-O c5,  8.Nc3** — `1.d4 Nf6 2.c4 g6 3.g3 d5 4.Bg2 Bg7 5.Nf3 O-O 6.cxd5 Nxd5 7.O-O c5 8.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D75_Neo_Grunfeld_Delayed_Exchange_c5.md#_Nc3_) — masters' actual third choice (17.2%) at its own fork, trailing both the coded sibling 8.dxc5 (47.8%) and the uncoded 8.e4 (34.0%)
- **Gruenfeld Defence, Neo-Gruenfeld Defence,  6.cd Nxd5,  7.O-O c5,  8.dc** — `1.d4 Nf6 2.c4 g6 3.g3 d5 4.Bg2 Bg7 5.Nf3 O-O 6.cxd5 Nxd5 7.O-O c5 8.dxc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D75_Neo_Grunfeld_Delayed_Exchange_c5.md#_dxc5_) — masters' actual main try (47.8%) at its own fork; a very thin sample past it (136 masters games)

## D76

- **Gruenfeld Defence, Neo-Gruenfeld Defence,  6.cd Nxd5,  7.O-O Nb6** — `1.d4 Nf6 2.c4 g6 3.g3 d5 4.Bg2 Bg7 5.Nf3 O-O 6.cxd5 Nxd5 7.O-O Nb6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D76_Neo_Grunfeld_Delayed_Exchange_Nb6.md#_initial_move_) — masters' clear main try at its own D74 fork (65.6%); White's own follow-up (8.Nc3) is close to forced (96.1%)

## D77

- **Gruenfeld Defence, Neo-Gruenfeld Defence,  6.O-O** — `1.d4 Nf6 2.c4 g6 3.g3 d5 4.Bg2 Bg7 5.Nf3 O-O 6.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D77_Neo_Grunfeld_Classical_Variation.md#_initial_move_) — live-tagged *Classical Variation*, the first genuinely distinct name in the whole D74-D79 span; its own near-even 6th-move fork sees the uncoded 6...dxc4 (46.9%) narrowly outrank the coded 6...c6 (43.7%)

## D78

- **Gruenfeld Defence, Neo-Gruenfeld Defence,  6.O-O c6** — `1.d4 Nf6 2.c4 g6 3.g3 d5 4.Bg2 Bg7 5.Nf3 O-O 6.O-O c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D78_Neo_Grunfeld_Classical_Original_Defense.md#_initial_move_) — live-tagged the more specific *Classical Variation, Original Defense*; White's own 7th move genuinely scatters five ways, no move close to forced

## D79

- **Gruenfeld Defence, Neo-Gruenfeld Defence,  6.O-O,  Main line** — `1.d4 Nf6 2.c4 g6 3.g3 d5 4.Bg2 Bg7 5.Nf3 O-O 6.O-O c6 7.cxd5 cxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D79_Neo_Grunfeld_Ultra_Delayed_Exchange.md#_initial_move_) — live-tagged *Ultra-Delayed Exchange Variation*, a real name divergence in the opposite direction from D78's own finding (here `eco.md`'s own label is the generic one); the deepest node in the whole D70-D79 batch

## D80

- **Gruenfeld Defence** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D80_Grunfeld_Defense.md#_initial_move_) — retrofit of a pre-sweep card (`D85_Grunfeld.md`, now `D85_Grunfeld_Exchange_Variation.md`) that had covered this root before this batch; White's own 4th-move fork (cxd5 53.1% / Nf3 29.7% masters) leaves Nf3 uncoded in this range
- **Gruenfeld Defence, Spike Gambit** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.g4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D80_Grunfeld_Defense.md#_g4_) — live-tagged the *Gibbon Gambit* instead, a real name divergence; a genuine database rarity (11 masters games), Stockfish rates it clearly bad for White (−0.56)
- **Gruenfeld Defence, Stockholm Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D80_Grunfeld_Defense.md#_Bg5_) — masters' main try, 4...Ne4 (76.5%), feeds the Lundin Variation below
- **Gruenfeld Defence, Lundin Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Bg5 Ne4 5.Nxe4 dxe4 6.Qd2 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D80_Grunfeld_Defense.md#_Lundin_) — a genuine finding: both moves that give the line its name are themselves masters minorities (5.Nxe4 only 3.0% masters despite 50.2% online; 6...c5 only 5.7% masters, 2 of 35 sampled games)

## D81

- **Gruenfeld Defence, Russian Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Qb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D81_Grunfeld_Russian_Variation.md#_initial_move_) — live-tagged with an extra "Accelerated Variation" suffix `eco.md` doesn't carry; 4...dxc4 close to automatic (97.0% masters)

## D82

- **Gruenfeld Defence, 4.Bf4** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Bf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D82_Grunfeld_Bf4.md#_initial_move_) — live-tagged the *Brinckmann Attack*, a real name `eco.md` itself leaves this bare tabiya without

## D83

- **Gruenfeld Defence, Gruenfeld Gambit** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Bf4 Bg7 5.e3 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D83_Grunfeld_Gambit.md#_initial_move_) — White's own 6th move is a real two-way split, 6.Rc1 (52.6% masters) vs 6.cxd5 into D84 (23.2%)
- **Gruenfeld Defence, Gruenfeld Gambit,  Capablanca Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Bf4 Bg7 5.e3 O-O 6.Rc1` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D83_Grunfeld_Gambit.md#_Rc1_) — a genuinely flat three-way split at Black's own 6th move (c5 33.9% / Be6 33.3% / c6 23.3% masters), the flattest distribution found anywhere in this batch
- **Gruenfeld Defence, Gruenfeld Gambit,  Botvinnik Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Bf4 Bg7 5.e3 O-O 6.Rc1 c5 7.dxc5 Be6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D83_Grunfeld_Gambit.md#_Botvinnik_) — live-tagged name confirmed; 7.dxc5 close to automatic (98.6% masters)

## D84

- **Gruenfeld Defence, Gruenfeld Gambit,  Accepted** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Bf4 Bg7 5.e3 O-O 6.cxd5 Nxd5 7.Nxd5 Qxd5 8.Bxc7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D84_Grunfeld_Gambit_Accepted.md#_Bxc7_) — the whole line to 8.Bxc7 is close to forced at every step (99.7%+ masters each ply); the position right after 8.Bxc7 itself carries 0 recorded games in either database and no cached eval, confirmed live

## D85

- **Gruenfeld Defence, Exchange Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.cxd5 Nxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D85_Grunfeld_Exchange_Variation.md#_initial_move_) — retrofit and expansion of the same pre-sweep card as D80 above, now starting at its own root instead of duplicating D80's; masters' clear main try overall (53.1% at D80's own root)
- **Gruenfeld Defence, Modern Exchange Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.cxd5 Nxd5 5.e4 Nxc3 6.bxc3 Bg7 7.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D85_Grunfeld_Exchange_Variation.md#_Nf3_) — live-tagged name confirmed; the pre-sweep card had explicitly left this 7th-move fork unbuilt, now followed through (35.6% masters, close behind 7.Bc4's 38.5%)

## D86

- **Gruenfeld Defence, Exchange Variation,  Classical Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.cxd5 Nxd5 5.e4 Nxc3 6.bxc3 Bg7 7.Bc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D86_Grunfeld_Exchange_Classical_Variation.md#_initial_move_) — masters' actual plurality at the 7th-move fork (38.5%); a genuine finding: masters' own most popular reply here is an immediate 7...c5 (77.7%, delaying castling), verified via `apply_san.py` to transpose into D87's own tabiya rather than being a rival system
- **Gruenfeld Defence, Exchange Variation,  Larsen Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.cxd5 Nxd5 5.e4 Nxc3 6.bxc3 Bg7 7.Bc4 O-O 8.Ne2 Qd7 9.O-O b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D86_Grunfeld_Exchange_Classical_Variation.md#_Larsen_) — live-tagged name confirmed at both nodes; a real minority at the 8th-move fork (6.1% masters)
- **Gruenfeld Defence, Exchange Variation,  Simagin's lesser Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.cxd5 Nxd5 5.e4 Nxc3 6.bxc3 Bg7 7.Bc4 O-O 8.Ne2 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D86_Grunfeld_Exchange_Classical_Variation.md#_b6_) — live-tagged name confirmed; the least comfortable of the fork's four branches per Stockfish (+0.69)
- **Gruenfeld Defence, Exchange Variation,  Simagin's improved Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.cxd5 Nxd5 5.e4 Nxc3 6.bxc3 Bg7 7.Bc4 O-O 8.Ne2 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D86_Grunfeld_Exchange_Classical_Variation.md#_Nc6_) — live-tagged name confirmed; masters' own second choice at the 8th-move fork (26.6%)

## D87

- **Gruenfeld Defence, Exchange Variation,  Spassky Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.cxd5 Nxd5 5.e4 Nxc3 6.bxc3 Bg7 7.Bc4 O-O 8.Ne2 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D87_Grunfeld_Exchange_Spassky_Variation.md#_initial_move_) — masters' clear main try at D86's own 8th-move fork (57.9%); also directly reachable, verified via `apply_san.py`, from D86's own uncoded 7...c5 move order
- **Gruenfeld Defence, Exchange Variation,  Seville Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.cxd5 Nxd5 5.e4 Nxc3 6.bxc3 Bg7 7.Bc4 O-O 8.Ne2 c5 9.O-O Nc6 10.Be3 Bg4 11.f3 Na5 12.Bxf7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D87_Grunfeld_Exchange_Spassky_Variation.md#_SevilleSac_) — live-tagged name confirmed; a genuine finding, `eco.md`'s own D88 "Main line" trails this line's own 10...Bg4 (28.6% masters, this fork's actual plurality) at only 4.5%; the sacrifice itself is a near-coin-flip against the quiet 12.Bd3 (44.7% vs 48.7% masters)

## D88

- **Gruenfeld Defence, Spassky Variation,  Main line,  10...cd,  11.cd** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.cxd5 Nxd5 5.e4 Nxc3 6.bxc3 Bg7 7.Bc4 O-O 8.Ne2 c5 9.O-O Nc6 10.Be3 cxd4 11.cxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D88_Grunfeld_Exchange_Spassky_Main_Line.md#_initial_move_) — a genuine finding: despite the "Main line" label, 10...cxd4 is only masters' fifth choice at its own fork (4.5%), and the live explorer tags this exact tabiya plain "Spassky Variation", not a distinct name of its own

## D89

- **Gruenfeld Defence, Spassky Variation,  Main line,  13.Bd3** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.cxd5 Nxd5 5.e4 Nxc3 6.bxc3 Bg7 7.Bc4 O-O 8.Ne2 c5 9.O-O Nc6 10.Be3 cxd4 11.cxd4 Bg4 12.f3 Na5 13.Bd3 Be6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D89_Grunfeld_Exchange_Spassky_13Bd3.md#_Be6_) — the deepest and final card in this whole D70-D99 sweep's D86-D89 spine; White's exchange sac is noticeably less popular here (24.3% masters) than in the structurally similar but unrelated D87 Seville fork, never asserted to transpose there
- **Gruenfeld Defence, Exchange Variation,  Sokolsky Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.cxd5 Nxd5 5.e4 Nxc3 6.bxc3 Bg7 7.Bc4 O-O 8.Ne2 c5 9.O-O Nc6 10.Be3 cxd4 11.cxd4 Bg4 12.f3 Na5 13.Bd3 Be6 14.d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D89_Grunfeld_Exchange_Spassky_13Bd3.md#_Sokolsky_) — live-tagged name confirmed; masters' clear main try at the 14th-move fork (53.5%); Black's own reply, 14...Bxa1, is close to total (99.0% masters), and Stockfish rates the resulting exchange-for-pawn-and-centre trade essentially level (+0.02)

## D90

- **Gruenfeld Defence, Three Knights Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D90_Grunfeld_Three_Knights_Variation.md#_initial_move_) — eco.md's own self-collision: this exact name is reused one ply later at 4...Bg7 below; both are treated as one continuous D90 card
- **Gruenfeld Defence, Schlechter Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D90_Grunfeld_Three_Knights_Variation.md#_c6_) — verified via apply_san.py to be the exact same FEN as D15's own Slav Defense Schlechter Variation tabiya, reached by transposition
- **Gruenfeld Defence, Three Knights Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D90_Grunfeld_Three_Knights_Variation.md#_Bg7_) — the wide 5th-move fork feeding D91/D92/D94/D96 plus this card's own Flohr Variation
- **Gruenfeld Defence, Flohr Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qa4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D90_Grunfeld_Three_Knights_Variation.md#_Qa4_) — the first of two unrelated "Flohr" names in this D90-D99 batch (D94's own Flohr Defence is the other)

## D91

- **Gruenfeld Defence, 5.Bg5** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D91_Grunfeld_5Bg5.md#_initial_move_) — live-tagged the Petrosian System, a real name this bare entry doesn't carry

## D92

- **Gruenfeld Defence, 5.Bf4** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Bf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D92_Grunfeld_5Bf4.md#_initial_move_) — live-tagged the Hungarian Attack

## D93

- **Gruenfeld Defence, With Bf4    e3** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Bf4 O-O 6.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D93_Grunfeld_Bf4_e3.md#_initial_move_) — live-tagged the Hungarian Variation; masters' actual plurality at the parent fork is the uncoded 6.Rc1 (51.4%), narrowly ahead of this card's own 6.e3 (47.0%)

## D94

- **Gruenfeld Defence, 5.e3** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D94_Grunfeld_5e3.md#_initial_move_) — live-tagged the Burille Variation
- **Gruenfeld Defence, Makogonov Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.e3 O-O 6.b4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D94_Grunfeld_5e3.md#_Makogonov_) — live-tagged name confirmed
- **Gruenfeld Defence, Opovcensky Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.e3 O-O 6.Bd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D94_Grunfeld_5e3.md#_Opocensky_) — live-tagged "Opocensky Variation" instead, a genuine spelling divergence (no v)
- **Gruenfeld Defence, With e3    Bd3** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.e3 O-O 6.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D94_Grunfeld_5e3.md#_Bd3_) — live-tagged the Paris Variation, a real name this bare entry doesn't carry; masters' actual main try here is the uncoded 6...c5 (83.7%), far ahead of 6...c6 (4.7%), the move that actually leads to this card's own two named children below
- **Gruenfeld Defence, Smyslov Defence** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.e3 O-O 6.Bd3 c6 7.O-O Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D94_Grunfeld_5e3.md#_Smyslov_) — live-tagged name confirmed; unrelated to D98's Smyslov Variation and D99's Smyslov Main Line/Yugoslav Variation, four separate "Smyslov"-built names across this D90-D99 batch
- **Gruenfeld Defence, Flohr Defence** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.e3 O-O 6.Bd3 c6 7.O-O Bf5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D94_Grunfeld_5e3.md#_Flohr_) — live-tagged name confirmed; the second of two unrelated "Flohr" names in this batch, after D90's own Flohr Variation

## D95

- **Gruenfeld Defence, With e3 & Qb3** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.e3 O-O 6.Qb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D95_Grunfeld_e3_Qb3.md#_initial_move_) — live-tagged the Vienna Variation
- **Gruenfeld Defence, Botvinnik Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.e3 O-O 6.Qb3 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D95_Grunfeld_e3_Qb3.md#_Botvinnik_) — live-tagged name confirmed; unrelated to D83's own Botvinnik Variation elsewhere in this same Grünfeld complex
- **Gruenfeld Defence, Pachman Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.e3 O-O 6.Qb3 dxc4 7.Bxc4 Nbd7 8.Ng5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D95_Grunfeld_e3_Qb3.md#_Pachman_) — live-tagged name confirmed on a vanishingly thin sample (2 masters games); the defining 7...Nbd7 is itself only 6.7% of masters play at its own fork, well behind 7...Nc6 (46.9%) and 7...c5 (32.4%)

## D96

- **Gruenfeld Defence, Russian Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D96_Grunfeld_Russian_Variation.md#_initial_move_) — the deepest, most important sub-tree of the whole D90-D99 batch, running through D97-D99

## D97

- **Gruenfeld Defence, Russian Variation With e4** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qb3 dxc4 6.Qxc4 O-O 7.e4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D97_Grunfeld_Russian_Variation_e4.md#_initial_move_) — the live explorer keeps this tabiya's name simply "Russian Variation", without eco.md's own "With e4" suffix; a genuine six-way fork on Black's 7th
- **Gruenfeld Defence, Russian Variation,  Alekhine Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qb3 dxc4 6.Qxc4 O-O 7.e4 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D97_Grunfeld_Russian_Variation_e4.md#_Alekhine_) — a genuine name divergence: live-tagged "Russian Variation, Hungarian Variation" instead, at least the fourth independent "Alekhine Variation" reuse in this D-series
- **Gruenfeld Defence, Russian Variation,  Szabo Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qb3 dxc4 6.Qxc4 O-O 7.e4 c6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D97_Grunfeld_Russian_Variation_e4.md#_Szabo_) — live-tagged name confirmed
- **Gruenfeld Defence, Russian Variation,  Levenfish Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qb3 dxc4 6.Qxc4 O-O 7.e4 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D97_Grunfeld_Russian_Variation_e4.md#_Levenfish_) — live-tagged name confirmed; the rarest of this fork's six named tries (0.4% masters, 20 games) and, at +1.22, over a pawn worse for Black than every sibling
- **Gruenfeld Defence, Russian Variation,  Byrne Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qb3 dxc4 6.Qxc4 O-O 7.e4 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D97_Grunfeld_Russian_Variation_e4.md#_Byrne_) — live-tagged name confirmed
- **Gruenfeld Defence, Russian Variation,  Prins Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qb3 dxc4 6.Qxc4 O-O 7.e4 Na6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D97_Grunfeld_Russian_Variation_e4.md#_Prins_) — live-tagged name confirmed; narrowly outranks the Byrne Variation in masters play, 16.7% to 16.0%

## D98

- **Gruenfeld Defence, Russian Variation,  Smyslov Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qb3 dxc4 6.Qxc4 O-O 7.e4 Bg4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D98_Grunfeld_Russian_Smyslov_Variation.md#_initial_move_) — live-tagged name confirmed; the second of four unrelated "Smyslov"-built names in this D90-D99 batch, running the spine on to D99
- **Gruenfeld Defence, Russian Variation,  Keres Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qb3 dxc4 6.Qxc4 O-O 7.e4 Bg4 8.Be3 Nfd7 9.Be2 Nb6 10.Qd3 Nc6 11.O-O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D98_Grunfeld_Russian_Smyslov_Variation.md#_Keres_) — live-tagged name confirmed on a thin sample (2 masters games); both of its own defining moves are minorities at their own forks — 9.Be2 a mere 2.1% and 11.O-O-O a mere 5.9%

## D99

- **Gruenfeld Defence, Smyslov,  Main line** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qb3 dxc4 6.Qxc4 O-O 7.e4 Bg4 8.Be3 Nfd7 9.Qb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D99_Grunfeld_Russian_Smyslov_Main_Line.md#_initial_move_) — masters' actual main try at its own parent fork (48.7%); the live explorer doesn't carry a distinct "Main line" suffix, the same pattern already logged at D88; the third of four unrelated "Smyslov"-built names in this batch
- **Gruenfeld Defence, Smyslov,  Yugoslav Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 d5 4.Nf3 Bg7 5.Qb3 dxc4 6.Qxc4 O-O 7.e4 Bg4 8.Be3 Nfd7 9.Qb3 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/D99_Grunfeld_Russian_Smyslov_Main_Line.md#_Yugoslav_) — live-tagged name confirmed on a thin sample (37 masters games, 3 online); the last of four unrelated "Smyslov"-built names in this batch, and the final leaf of the whole D90-D99 sweep

## E00

- **Queen's Pawn Game** — `1.d4 Nf6 2.c4 e6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E00_Catalan.md#_initial_move_)
- **Neo-Indian Attack** — `1.d4 Nf6 2.c4 e6 3.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E00_Catalan.md)
- **Catalan Opening** — `1.d4 Nf6 2.c4 e6 3.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E00_Catalan.md#_initial_move_)

## E01

- **Catalan Opening, Closed** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E01_Catalan_Open_Defense.md#_initial_move_)

## E02

- **Catalan Opening, Open,  5.Qa4** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 dxc4 5.Qa4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E02_Catalan_Open_Qa4.md#_initial_move_)

## E03

- **Catalan Opening, Open,  Alekhine Variation** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 dxc4 5.Qa4 Nbd7 6.Qxc4 a6 7.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E03_Catalan_Open_Alekhine.md#_a6_)
- **Catalan Opening, Open,  5.Qa4 Nbd7,  6.Qxc4** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 dxc4 5.Qa4 Nbd7 6.Qxc4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E03_Catalan_Open_Alekhine.md#_initial_move_)

## E04

- **Catalan Opening, Open,  5.Nf3** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 dxc4 5.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E04_Catalan_Open_Nf3.md#_initial_move_)

## E05

- **Catalan Opening, Open,  Classical line** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 dxc4 5.Nf3 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E05_Catalan_Open_Classical.md#_initial_move_)

## E06

- **Catalan Opening, Closed,  5.Nf3** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 Be7 5.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E06_Catalan_Closed.md#_initial_move_)

## E07

- **Catalan Opening, Closed,  6...Nbd7** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 Be7 5.Nf3 O-O 6.O-O Nbd7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E07_Catalan_Closed_Nbd7.md#_initial_move_)
- **Catalan Opening, Closed,  Botvinnik Variation** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 Be7 5.Nf3 O-O 6.O-O Nbd7 7.Nc3 c6 8.Qd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E07_Catalan_Closed_Nbd7.md#_Nc3_)

## E08

- **Catalan Opening, Closed,  7.Qc2** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 Be7 5.Nf3 O-O 6.O-O Nbd7 7.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E08_Catalan_Closed_Qc2.md#_initial_move_)
- **Catalan Opening, Closed,  Zagoryansky Variation** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 Be7 5.Nf3 O-O 6.O-O Nbd7 7.Qc2 c6 8.Rd1 b6 9.a4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E08_Catalan_Closed_Qc2.md#_Rd1_)
- **Catalan Opening, Closed,  Qc2 & b3** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 Be7 5.Nf3 O-O 6.O-O Nbd7 7.Qc2 c6 8.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E08_Catalan_Closed_Qc2.md#_b3_)
- **Catalan Opening, Closed,  Spassky Gambit** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 Be7 5.Nf3 O-O 6.O-O Nbd7 7.Qc2 c6 8.b3 b6 9.Rd1 Bb7 10.Nc3 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E08_Catalan_Closed_Qc2.md#_b3_)

## E09

- **Catalan Opening, Closed,  Main line** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 Be7 5.Nf3 O-O 6.O-O Nbd7 7.Qc2 c6 8.Nbd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E09_Catalan_Closed_Main_Line.md#_initial_move_)
- **Catalan Opening, Closed,  Sokolsky Variation** — `1.d4 Nf6 2.c4 e6 3.g3 d5 4.Bg2 Be7 5.Nf3 O-O 6.O-O Nbd7 7.Qc2 c6 8.Nbd2 b6 9.b3 a5 10.Bb2 Ba6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E09_Catalan_Closed_Main_Line.md#_initial_move_)

## E10

- **Queen's Pawn Game** — `1.d4 Nf6 2.c4 e6 3.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E10_Anti_Nimzo_Indian.md#_initial_move_)
- **Blumenfeld Counter-Gambit** — `1.d4 Nf6 2.c4 e6 3.Nf3 c5 4.d5 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E10_Anti_Nimzo_Indian.md#_c5_)
- **Blumenfeld Counter-Gambit, Accepted** — `1.d4 Nf6 2.c4 e6 3.Nf3 c5 4.d5 b5 5.dxe6 fxe6 6.cxb5 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E10_Anti_Nimzo_Indian.md#_dxe6_)
- **Blumenfeld Counter-Gambit, Dus-Khotimirsky Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 c5 4.d5 b5 5.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E10_Anti_Nimzo_Indian.md#_Bg5_)
- **Blumenfeld Counter-Gambit, Spielmann Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 c5 4.d5 b5 5.Bg5 exd5 6.cxd5 h6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E10_Anti_Nimzo_Indian.md#_Bg5_)
- **Dzindzikhashvili Defence** — `1.d4 Nf6 2.c4 e6 3.Nf3 a6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E10_Anti_Nimzo_Indian.md)
- **Doery Defence** — `1.d4 Nf6 2.c4 e6 3.Nf3 Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E10_Anti_Nimzo_Indian.md)

## E11

- **Bogo-Indian Defence** — `1.d4 Nf6 2.c4 e6 3.Nf3 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E11_Bogo_Indian.md#_initial_move_)
- **Bogo-Indian Defence, Gruenfeld Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 Bb4 4.Nbd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E11_Bogo_Indian.md#_Nbd2_)
- **Bogo-Indian Defence, Nimzovich Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 Bb4 4.Bd2 Qe7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E11_Bogo_Indian.md#_Bd2_)
- **Bogo-Indian Defence, Monticelli trap** — `1.d4 Nf6 2.c4 e6 3.Nf3 Bb4 4.Bd2 Bxd2 5.Qxd2 b6 6.g3 Bb7 7.Bg2 O-O 8.Nc3 Ne4 9.Qc2 Nxc3 10.Ng5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E11_Bogo_Indian.md#_Bd2_)

## E12

- **Queen's Indian Defence** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E12_Queens_Indian.md#_b6_)
- **Queen's Indian Defence, Miles Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.Bf4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E12_Queens_Indian.md)
- **Queen's Indian Defence, Petrosian System** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.a3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E12_Queens_Indian.md)
- **Queen's Indian Defence, 4.Nc3** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E12_Queens_Indian.md#_Nc3_)
- **Queen's Indian Defence, 4.Nc3,  Botvinnik Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.Nc3 Bb7 5.Bg5 h6 6.Bh4 g5 7.Bg3 Nh5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E12_Queens_Indian.md#_Nc3_)

## E13

- **Queen's Indian Defence, 4.Nc3,  Main line** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.Nc3 Bb7 5.Bg5 h6 6.Bh4 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E13_Queens_Indian_Kasparov_Main_Line.md#_initial_move_)

## E14

- **Queen's Indian Defence, 4.e3** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E14_Queens_Indian_Spassky_System.md#_initial_move_)
- **Queen's Indian Defence, Averbakh Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.e3 Bb7 5.Bd3 c5 6.O-O Be7 7.b3 O-O 8.Bb2 cxd4 9.Nxd4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E14_Queens_Indian_Spassky_System.md)

## E15

- **Queen's Indian Defence, 4.g3** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E15_Queens_Indian_Fianchetto.md#_initial_move_)
- **Queen's Indian Defence, Nimzovich Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Ba6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E15_Queens_Indian_Fianchetto.md)
- **Queen's Indian Defence, 4.g3 Bb7** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E15_Queens_Indian_Fianchetto.md#_Bb7_)
- **Queen's Indian Defence, Rubinstein Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7 5.Bg2 c5 6.d5 exd5 7.Nh4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E15_Queens_Indian_Fianchetto.md#_Nh4_)
- **Queen's Indian Defence, Buerger Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7 5.Bg2 c5 6.d5 exd5 7.Ng5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E15_Queens_Indian_Fianchetto.md#_Ng5_)

## E16

- **Queen's Indian Defence, Capablanca Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7 5.Bg2 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E16_Queens_Indian_Capablanca.md#_initial_move_)
- **Queen's Indian Defence, Yates Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7 5.Bg2 Bb4 6.Bd2 a5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E16_Queens_Indian_Capablanca.md#_a5_)
- **Queen's Indian Defence, Riumin Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7 5.Bg2 Bb4 6.Bd2 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E16_Queens_Indian_Capablanca.md#_Be7_)

## E17

- **Queen's Indian Defence, 5.Bg2 Be7** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7 5.Bg2 Be7` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E17_Queens_Indian_Traditional.md#_initial_move_)
- **Queen's Indian Defence, Anti-Queen's Indian System** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7 5.Bg2 Be7 6.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E17_Queens_Indian_Traditional.md#_Nc3_)
- **Queen's Indian Defence, Opovcensky Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7 5.Bg2 Be7 6.Nc3 Ne4 7.Bd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E17_Queens_Indian_Traditional.md#_Nc3_)
- **Queen's Indian Defence, old Main line,  6.O-O** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7 5.Bg2 Be7 6.O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E17_Queens_Indian_Traditional.md#_OO_)
- **Queen's Indian Defence, Euwe Variation** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7 5.Bg2 Be7 6.O-O O-O 7.b3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E17_Queens_Indian_Traditional.md#_b3_)

## E18

- **Queen's Indian Defence, old Main line,  7.Nc3** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7 5.Bg2 Be7 6.O-O O-O 7.Nc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E18_Queens_Indian_Classical_Traditional.md#_initial_move_)

## E19

- **Queen's Indian Defence, old Main line,  9.Qxc3** — `1.d4 Nf6 2.c4 e6 3.Nf3 b6 4.g3 Bb7 5.Bg2 Be7 6.O-O O-O 7.Nc3 Ne4 8.Qc2 Nxc3 9.Qxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E19_Queens_Indian_Classical_Main_Line.md#_initial_move_)

## E20

- **Nimzo-Indian Defence** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E20_Nimzo_Indian.md#_Bb4_)
- **Nimzo-Indian Defence, Kmoch Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.f3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E20_Nimzo_Indian.md)
- **Nimzo-Indian Defence, Mikenas Attack** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E20_Nimzo_Indian.md)
- **Nimzo-Indian Defence, Romanishin-Kasparov (Steiner) System** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E20_Nimzo_Indian.md)

## E21

- **Nimzo-Indian Defence, three Knights Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Nf3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E21_Nimzo_Indian_Three_Knights.md#_initial_move_)
- **Nimzo-Indian Defence, three Knights,  Korchnoi Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Nf3 c5 5.d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E21_Nimzo_Indian_Three_Knights.md#_c5_)
- **Nimzo-Indian Defence, three Knights,  Euwe Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Nf3 c5 5.d5 Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E21_Nimzo_Indian_Three_Knights.md#_c5_)

## E22

- **Nimzo-Indian Defence, Spielmann Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qb3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E22_Nimzo_Indian_Spielmann.md#_initial_move_)

## E23

- **Nimzo-Indian Defence, Spielmann,  4...c5,  5.dc Nc6** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qb3 c5 5.dxc5 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E23_Nimzo_Indian_Spielmann_Karlsbad.md#_initial_move_)
- **Nimzo-Indian Defence, Spielmann,  Karlsbad Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qb3 c5 5.dxc5 Nc6 6.Nf3 Ne4 7.Bd2 Nxd2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E23_Nimzo_Indian_Spielmann_Karlsbad.md#_Karlsbad_)
- **Nimzo-Indian Defence, Spielmann,  San Remo Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qb3 c5 5.dxc5 Nc6 6.Nf3 Ne4 7.Bd2 Nxc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E23_Nimzo_Indian_Spielmann_Karlsbad.md#_Stahlberg_)
- **Nimzo-Indian Defence, Spielmann,  Staahlberg Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qb3 c5 5.dxc5 Nc6 6.Nf3 Ne4 7.Bd2 Nxc5 8.Qc2 f5 9.g3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E23_Nimzo_Indian_Spielmann_Karlsbad.md#_Stahlberg_)

## E24

- **Nimzo-Indian Defence, Saemisch Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.a3 Bxc3 5.bxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E24_Nimzo_Indian_Saemisch.md#_initial_move_)
- **Nimzo-Indian Defence, Saemisch,  Botvinnik Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.a3 Bxc3 5.bxc3 c5 6.f3 d5 7.e3 O-O 8.cxd5 Nxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E24_Nimzo_Indian_Saemisch.md#_f3_)

## E25

- **Nimzo-Indian Defence, Saemisch Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.a3 Bxc3 5.bxc3 c5 6.f3 d5 7.cxd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E25_Nimzo_Indian_Saemisch_Keres.md#_initial_move_)
- **Nimzo-Indian Defence, Saemisch,  Keres Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.a3 Bxc3 5.bxc3 c5 6.f3 d5 7.cxd5 Nxd5 8.dxc5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E25_Nimzo_Indian_Saemisch_Keres.md#_Keres_)
- **Nimzo-Indian Defence, Saemisch,  Romanovsky Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.a3 Bxc3 5.bxc3 c5 6.f3 d5 7.cxd5 Nxd5 8.dxc5 f5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E25_Nimzo_Indian_Saemisch_Keres.md#_Keres_)

## E26

- **Nimzo-Indian Defence, Saemisch Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.a3 Bxc3 5.bxc3 c5 6.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E26_Nimzo_Indian_Saemisch_OKelly.md#_initial_move_)
- **Nimzo-Indian Defence, Saemisch,  O'Kelly Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.a3 Bxc3 5.bxc3 c5 6.e3 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E26_Nimzo_Indian_Saemisch_OKelly.md)

## E27

- **Nimzo-Indian Defence, Saemisch Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.a3 Bxc3 5.bxc3 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E27_Nimzo_Indian_Saemisch_OO.md#_initial_move_)

## E28

- **Nimzo-Indian Defence, Saemisch Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.a3 Bxc3 5.bxc3 O-O 6.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E28_Nimzo_Indian_Saemisch_e3.md#_initial_move_)

## E29

- **Nimzo-Indian Defence, Saemisch,  Main line** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.a3 Bxc3 5.bxc3 O-O 6.e3 c5 7.Bd3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E29_Nimzo_Indian_Saemisch_Main_Line.md#_initial_move_)
- **Nimzo-Indian Defence, Saemisch,  Capablanca Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.a3 Bxc3 5.bxc3 O-O 6.e3 c5 7.Bd3 Nc6 8.Ne2 b6 9.e4 Ne8` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E29_Nimzo_Indian_Saemisch_Main_Line.md#_Capablanca_)

## E30

- **Nimzo-Indian Defence, Leningrad Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Bg5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E30_Nimzo_Indian_Leningrad.md#_initial_move_)
- **Nimzo-Indian Defence, Leningrad,  ...b5 Gambit** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Bg5 h6 5.Bh4 c5 6.d5 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E30_Nimzo_Indian_Leningrad.md#_b5_)

## E31

- **Nimzo-Indian Defence, Leningrad,  Main line** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Bg5 h6 5.Bh4 c5 6.d5 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E31_Nimzo_Indian_Leningrad_Benoni.md#_initial_move_)

## E32

- **Nimzo-Indian Defence, Classical Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E32_Nimzo_Indian_Classical.md#_initial_move_)
- **Nimzo-Indian Defence, Classical,  Adorjan Gambit** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 O-O 5.a3 Bxc3 6.Qxc3 b5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E32_Nimzo_Indian_Classical.md#_OO_)

## E33

- **Nimzo-Indian Defence, Classical,  4...Nc6** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E33_Nimzo_Indian_Classical_Zurich.md#_initial_move_)
- **Nimzo-Indian Defence, Classical,  Milner-Barry (Zurich) Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 Nc6 5.Nf3 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E33_Nimzo_Indian_Classical_Zurich.md#_Milner_Barry_)

## E34

- **Nimzo-Indian Defence, Classical,  Noa Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E34_Nimzo_Indian_Classical_Noa.md#_initial_move_)

## E35

- **Nimzo-Indian Defence, Classical,  Noa Variation,  5.cd ed** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 d5 5.cxd5 exd5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E35_Nimzo_Indian_Classical_Noa_Exchange.md#_initial_move_)

## E36

- **Nimzo-Indian Defence, Classical,  Noa Variation,  5.a3** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 d5 5.a3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E36_Nimzo_Indian_Classical_Noa_Main_Line.md#_initial_move_)
- **Nimzo-Indian Defence, Classical,  Botvinnik Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 d5 5.a3 Bxc3 6.Qxc3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E36_Nimzo_Indian_Classical_Noa_Main_Line.md#_Botvinnik_)
- **Nimzo-Indian Defence, Classical,  Noa Variation,  Main line** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 d5 5.a3 Bxc3 6.Qxc3 Ne4` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E36_Nimzo_Indian_Classical_Noa_Main_Line.md)

## E37

- **Nimzo-Indian Defence, Classical,  Noa Variation,  Main line,  7.Qc2** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 d5 5.a3 Bxc3 6.Qxc3 Ne4 7.Qc2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E37_Nimzo_Indian_Classical_Noa_Qc2.md#_initial_move_)
- **Nimzo-Indian Defence, Classical,  San Remo Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 d5 5.a3 Bxc3 6.Qxc3 Ne4 7.Qc2 Nc6 8.e3 e5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E37_Nimzo_Indian_Classical_Noa_Qc2.md#_San_Remo_)

## E38

- **Nimzo-Indian Defence, Classical,  4...c5** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E38_Nimzo_Indian_Classical_Berlin.md#_initial_move_)

## E39

- **Nimzo-Indian Defence, Classical,  Pirc Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.Qc2 c5 5.dxc5 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E39_Nimzo_Indian_Classical_Berlin_Pirc.md#_initial_move_)

## E40

- **Nimzo-Indian Defence, 4.e3** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E40_Nimzo_Indian_Rubinstein.md#_initial_move_)
- **Nimzo-Indian Defence, 4.e3,  Taimanov Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 Nc6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E40_Nimzo_Indian_Rubinstein.md)

## E41

- **Nimzo-Indian Defence, 4.e3 c5** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 c5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E41_Nimzo_Indian_Rubinstein_c5.md#_initial_move_)
- **Nimzo-Indian Defence, e3,  Huebner Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 c5 5.Bd3 Nc6 6.Nf3 Bxc3 7.bxc3 d6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E41_Nimzo_Indian_Rubinstein_c5.md#_Bd3_)

## E42

- **Nimzo-Indian Defence, 4.e3 c5,  5.Ne2 (Rubinstein)** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 c5 5.Ne2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E42_Nimzo_Indian_Rubinstein_Ne2.md#_initial_move_)

## E43

- **Nimzo-Indian Defence, Fischer Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 b6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E43_Nimzo_Indian_St_Petersburg.md#_initial_move_)

## E44

- **Nimzo-Indian Defence, Fischer Variation,  5.Ne2** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 b6 5.Ne2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E44_Nimzo_Indian_St_Petersburg_Ne2.md#_initial_move_)

## E45

- **Nimzo-Indian Defence, 4.e3,  Bronstein Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 b6 5.Ne2 Ba6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E45_Nimzo_Indian_St_Petersburg_Fischer.md#_initial_move_)

## E46

- **Nimzo-Indian Defence, 4.e3 O-O** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E46_Nimzo_Indian_Rubinstein_Normal.md#_initial_move_)
- **Nimzo-Indian Defence, Reshevsky Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Ne2` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E46_Nimzo_Indian_Rubinstein_Normal.md#_Ne2_)
- **Nimzo-Indian Defence, Simagin Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Ne2 d5 6.a3 Bd6` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E46_Nimzo_Indian_Rubinstein_Normal.md#_Ne2_)

## E47

- **Nimzo-Indian Defence, 4.e3 O-O,  5.Bd3** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Bd3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E47_Nimzo_Indian_Rubinstein_Bd3.md#_initial_move_)

## E48

- **Nimzo-Indian Defence, 4.e3 O-O,  5.Bd3 d5** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Bd3 d5` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E48_Nimzo_Indian_Rubinstein_Classical.md#_initial_move_)

## E49

- **Nimzo-Indian Defence, 4.e3,  Botvinnik System** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Bd3 d5 6.a3 Bxc3 7.bxc3` ✅ [covered](https://github.com/onclemarcel/chess_flashcards/blob/main/d4_openings/E49_Nimzo_Indian_Rubinstein_Botvinnik.md#_initial_move_)

## E50

- **Nimzo-Indian Defence, 4.e3 e8g8,  5.Nf3,  Without ...d5** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3`

## E51

- **Nimzo-Indian Defence, 4.e3 e8g8,  5.Nf3 d7d5** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5`
- **Nimzo-Indian Defence, 4.e3,  Ragozin Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 Nc6 7.O-O dxc4`

## E52

- **Nimzo-Indian Defence, 4.e3,  Main line With ...b6** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 b6`

## E53

- **Nimzo-Indian Defence, 4.e3,  Main line With ...c5** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 c5`
- **Nimzo-Indian Defence, 4.e3,  Keres Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 c5 7.O-O b6`
- **Nimzo-Indian Defence, 4.e3,  Gligoric System With 7...Nbd7** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 c5 7.O-O Nbd7`

## E54

- **Nimzo-Indian Defence, 4.e3,  Gligoric System With 7...dc** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 c5 7.O-O dxc4 8.Bxc4`
- **Nimzo-Indian Defence, 4.e3,  Gligoric System,  Smyslov Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 c5 7.O-O dxc4 8.Bxc4 Qe7`

## E55

- **Nimzo-Indian Defence, 4.e3,  Gligoric System,  Bronstein Variation** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 c5 7.O-O dxc4 8.Bxc4 Nbd7`

## E56

- **Nimzo-Indian Defence, 4.e3,  Main line With 7...Nc6** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 c5 7.O-O Nc6`

## E57

- **Nimzo-Indian Defence, 4.e3,  Main line With 8...dc and 9...cd** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 c5 7.O-O Nc6 8.a3 dxc4 9.Bxc4 cxd4`

## E58

- **Nimzo-Indian Defence, 4.e3,  Main line With 8...Bxc3** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 c5 7.O-O Nc6 8.a3 Bxc3 9.bxc3`

## E59

- **Nimzo-Indian Defence, 4.e3,  Main line** — `1.d4 Nf6 2.c4 e6 3.Nc3 Bb4 4.e3 O-O 5.Nf3 d5 6.Bd3 c5 7.O-O Nc6 8.a3 Bxc3 9.bxc3 dxc4 10.Bxc4`

## E60

- **King's Indian Defence** — `1.d4 Nf6 2.c4 g6`
- **King's Indian Defence, 3.Nf3** — `1.d4 Nf6 2.c4 g6 3.Nf3`
- **King's Indian Defence, Queen's Pawn Game,  Mengarini Attack** — `1.d4 Nf6 2.c4 g6 3.Qc2`
- **King's Indian Defence, Anti-Gruenfeld** — `1.d4 Nf6 2.c4 g6 3.d5`
- **King's Indian Defence, Danube Gambit** — `1.d4 Nf6 2.c4 g6 3.d5 b5`
- **King's Indian Defence, 3.g3** — `1.d4 Nf6 2.c4 g6 3.g3`
- **King's Indian Defence, 3.g3,  Counterthrust Variation** — `1.d4 Nf6 2.c4 g6 3.g3 Bg7 4.Bg2 d5`

## E61

- **King's Indian Defence, 3.Nc3** — `1.d4 Nf6 2.c4 g6 3.Nc3`
- **King's Indian Defence, Smyslov System** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.Bg5`

## E62

- **King's Indian Defence, Fianchetto Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3`
- **King's Indian Defence, Fianchetto,  Larsen System** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 c6 7.O-O Bf5`
- **King's Indian Defence, Fianchetto,  Kavalek (Bronstein) Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 c6 7.O-O Qa5`
- **King's Indian Defence, Fianchetto With ...Nc6** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 Nc6`
- **King's Indian Defence, Fianchetto,  Uhlmann (Szabo) Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 Nc6 7.O-O e5`
- **King's Indian Defence, Fianchetto,  lesser Simagin (Spassky) Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 Nc6 7.O-O Bf5`
- **King's Indian Defence, Fianchetto,  Simagin Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 Nc6 7.O-O Bg4`

## E63

- **King's Indian Defence, Fianchetto,  Panno Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 Nc6 7.O-O a6`

## E64

- **King's Indian Defence, Fianchetto,  Yugoslav System** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 c5`

## E65

- **King's Indian Defence, Fianchetto,  Yugoslav System,  7.O-O** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 c5 7.O-O`

## E66

- **King's Indian Defence, Fianchetto,  Yugoslav Panno** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 c5 7.O-O Nc6 8.d5`

## E67

- **King's Indian Defence, Fianchetto With ...Nd7** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 Nbd7`
- **King's Indian Defence, Fianchetto,  Classical Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 Nbd7 7.O-O e5`

## E68

- **King's Indian Defence, Fianchetto,  Classical Variation,  8.e4** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 Nbd7 7.O-O e5 8.e4`

## E69

- **King's Indian Defence, Fianchetto,  Classical Main line** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.Nf3 d6 5.g3 O-O 6.Bg2 Nbd7 7.O-O e5 8.e4 c6 9.h3`

## E70

- **King's Indian Defence, 4.e4** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4`
- **King's Indian Defence, Kramer System** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nge2`
- **King's Indian Defence, Accelerated Averbakh System** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Bg5`

## E71

- **King's Indian Defence, Makagonov System (5.h3)** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.h3`

## E72

- **King's Indian Defence, e4 & g3 Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.g3`
- **King's Indian Defence, Pomar System** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.g3 O-O 6.Bg2 e5 7.Nge2`

## E73

- **King's Indian Defence, 5.Be2** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Be2`
- **King's Indian Defence, Semi-Averbakh System** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Be2 O-O 6.Be3`
- **King's Indian Defence, Averbakh System** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Be2 O-O 6.Bg5`

## E74

- **King's Indian Defence, Averbakh System,  6...c5** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Be2 O-O 6.Bg5 c5`

## E75

- **King's Indian Defence, Averbakh System,  Main line** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Be2 O-O 6.Bg5 c5 7.d5 e6`

## E76

- **King's Indian Defence, Four Pawns Attack** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f4`
- **King's Indian Defence, Four Pawns Attack,  dynamic line** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f4 O-O 6.Nf3 c5 7.d5`

## E77

- **King's Indian Defence, Four Pawns Attack,  6.Be2** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f4 O-O 6.Be2`
- **King's Indian Defence, Six Pawns Attack** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f4 O-O 6.Be2 c5 7.d5 e6 8.dxe6 fxe6 9.g4 Nc6 10.h4`
- **King's Indian Defence, Four Pawns Attack** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f4 O-O 6.Be2 c5 7.d5 e6 8.Nf3`
- **King's Indian Defence, Four Pawns Attack,  Florentine Gambit** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f4 O-O 6.Be2 c5 7.d5 e6 8.Nf3 exd5 9.e5`

## E78

- **King's Indian Defence, Four Pawns Attack,  With Be2 and Nf3** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f4 O-O 6.Be2 c5 7.Nf3`

## E79

- **King's Indian Defence, Four Pawns Attack,  Main line** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f4 O-O 6.Be2 c5 7.Nf3 cxd4 8.Nxd4 Nc6 9.Be3`

## E80

- **King's Indian Defence, Saemisch Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3`

## E81

- **King's Indian Defence, Saemisch,  5...O-O** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3 O-O`
- **King's Indian Defence, Saemisch,  Byrne Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3 O-O 6.Be3 c6 7.Bd3 a6`

## E82

- **King's Indian Defence, Saemisch,  double Fianchetto Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3 O-O 6.Be3 b6`

## E83

- **King's Indian Defence, Saemisch,  6...Nc6** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3 O-O 6.Be3 Nc6`
- **King's Indian Defence, Saemisch,  Ruban Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3 O-O 6.Be3 Nc6 7.Nge2 Rb8`
- **King's Indian Defence, Saemisch,  Panno formation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3 O-O 6.Be3 Nc6 7.Nge2 a6`

## E84

- **King's Indian Defence, Saemisch,  Panno Main line** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3 O-O 6.Be3 Nc6 7.Nge2 a6 8.Qd2 Rb8`

## E85

- **King's Indian Defence, Saemisch,  Orthodox Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3 O-O 6.Be3 e5`

## E86

- **King's Indian Defence, Saemisch,  Orthodox,  7.Nge2 c6** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3 O-O 6.Be3 e5 7.Nge2 c6`

## E87

- **King's Indian Defence, Saemisch,  Orthodox,  7.d5** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3 O-O 6.Be3 e5 7.d5`
- **King's Indian Defence, Saemisch,  Orthodox,  Bronstein Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3 O-O 6.Be3 e5 7.d5 Nh5 8.Qd2 Qh4 9.g3 Nxg3 10.Qf2 Nxf1 11.Qxh4 Nxe3 12.Ke2 Nxc4`

## E88

- **King's Indian Defence, Saemisch,  Orthodox,  7.d5 c6** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3 O-O 6.Be3 e5 7.d5 c6`

## E89

- **King's Indian Defence, Saemisch,  Orthodox Main line** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.f3 O-O 6.Be3 e5 7.d5 c6 8.Nge2 cxd5`

## E90

- **King's Indian Defence, 5.Nf3** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3`
- **King's Indian Defence, Larsen Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be3`
- **King's Indian Defence, Zinnowitz Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Bg5`

## E91

- **King's Indian Defence, 6.Be2** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2`
- **King's Indian Defence, Kazakh Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 Na6`

## E92

- **King's Indian Defence, Classical Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5`
- **King's Indian Defence, Andersson Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.dxe5`
- **King's Indian Defence, Gligoric-Taimanov System** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.Be3`
- **King's Indian Defence, Petrosian System** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.d5`
- **King's Indian Defence, Petrosian System,  Stein Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.d5 a5`

## E93

- **King's Indian Defence, Petrosian System,  Main line** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.d5 Nbd7`
- **King's Indian Defence, Petrosian System,  Keres Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.d5 Nbd7 8.Bg5 h6 9.Bh4 g5 10.Bg3 Nh5 11.h4`

## E94

- **King's Indian Defence, orthodox Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.O-O`
- **King's Indian Defence, orthodox,  Donner Variation** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.O-O c6`
- **King's Indian Defence, orthodox,  7...Nbd7** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.O-O Nbd7`

## E95

- **King's Indian Defence, orthodox,  7...Nbd7,  8.Re1** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.O-O Nbd7 8.Re1`

## E96

- **King's Indian Defence, orthodox,  7...Nbd7,  Main line** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.O-O Nbd7 8.Re1 c6 9.Bf1 a5`

## E97

- **King's Indian Defence, orthodox,  Aronin-Taimanov Variation (Yugoslav Attack / Mar del Plata Variation)** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.O-O Nc6`
- **King's Indian Defence, orthodox,  Aronin-Taimanov,  bayonet Attack** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.O-O Nc6 8.d5 Ne7 9.b4`

## E98

- **King's Indian Defence, orthodox,  Aronin-Taimanov,  9.Ne1** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.O-O Nc6 8.d5 Ne7 9.Ne1`

## E99

- **King's Indian Defence, orthodox,  Aronin-Taimanov,  Main line** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.O-O Nc6 8.d5 Ne7 9.Ne1 Nd7 10.f3 f5`
- **King's Indian Defence, orthodox,  Aronin-Taimanov,  Benko Attack** — `1.d4 Nf6 2.c4 g6 3.Nc3 Bg7 4.e4 d6 5.Nf3 O-O 6.Be2 e5 7.O-O Nc6 8.d5 Ne7 9.Ne1 Nd7 10.f3 f5 11.g4`

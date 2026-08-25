<a name="_TOP_"></a>

# Corridor Mate <br> Queen + Long-Diagonal Bishop #

A **corridor mate** is any checkmate where the king has no flight square along an open rank, file, or diagonal — usually because its own pieces block one side of the corridor while an enemy piece covers the other. This is the general family that back-rank mates and ladder mates both belong to; it isn't one of the single, precisely-named patterns like Anastasia's or Boden's Mate, so this card describes the mechanism directly rather than forcing an inexact label onto it.

This particular version pairs a queen (delivering the check along an open file) with a **bishop already sitting on the long diagonal**, which denies the king's only other escape square. The queen alone would only threaten a check the king could sidestep; the bishop is what turns it into mate. Getting the king onto the right square in the first place typically takes a **clearance sacrifice** — see the worked example below, where a rook sacrifices itself specifically to open the file *and* unmask the bishop's diagonal in the same move, producing a discovered double check along the way.

### The pattern in the abstract

[![Corridor mate diagram](https://backscattering.de/web-boardimage/board.svg?fen=k7/8/8/3b4/6q1/8/5P1P/5RK1&coordinates=true&size=320)](https://lichess.org/analysis/standard/k7/8/8/3b4/6q1/8/5P1P/5RK1_w_-_-_0_1)

*A minimal version of the shape: King g1 has f1 (own rook), f2 (own pawn), and h2 (own pawn) blocked, and h1 covered by the bishop on the a8-h1 diagonal — only g2/g3 stay open, and that's exactly where the queen is checking from.*

```
k7/8/8/3b4/6q1/8/5P1P/5RK1 w - - 0 1
```

[*Back to TOP*](#_TOP_)

---

<a name="_worked_example_"></a>

## Worked example [DN-3]

*Source: Speedrun: Back to 3000 ELO, game 3 (Naroditsky, 491 ELO on-screen) — full game context and the opening's own issues are covered as a cautionary NOTE/TIP on [C23 Bishop's Opening](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C23_Bishop_Opening.md#_Nxf7_blunder_); this card is only about the mating mechanism itself, verified move by move against the engine.*

Reached after **17. Na3**, following **16... Bf8**, a double-purpose move that both attacked White's queen on c5 and — by moving off the g-file — unmasked Black's own rook's attack on g2:

[![Setup position](https://backscattering.de/web-boardimage/board.svg?fen=2k2brr/1ppq3p/p1n5/P1Qb4/2pp4/N7/1PP2PPP/R1B2RK1&lastMove=b1a3&coordinates=true&size=320)](https://lichess.org/analysis/standard/2k2brr/1ppq3p/p1n5/P1Qb4/2pp4/N7/1PP2PPP/R1B2RK1_b_-_-_3_17)

*... 17. Na3 — Black to move*

```
2k2brr/1ppq3p/p1n5/P1Qb4/2pp4/N7/1PP2PPP/R1B2RK1 b - - 3 17
```

Black already had a completely won position and could simply have grabbed the loose queen (17... Bxc5); instead, the g8-rook, the d5-bishop, and the queen combine for a forced mate in three.

### 17... Rxg2+! — the clearance sacrifice

[![17...Rxg2+](https://backscattering.de/web-boardimage/board.svg?fen=2k2b1r/1ppq3p/p1n5/P1Qb4/2pp4/N7/1PP2PrP/R1B2RK1&lastMove=g8g2&coordinates=true&size=320)](https://lichess.org/analysis/standard/2k2b1r/1ppq3p/p1n5/P1Qb4/2pp4/N7/1PP2PrP/R1B2RK1_w_-_-_0_18)

*... 17... Rxg2+ — the rook sacrifices itself, but note it also stands on the bishop's own diagonal*

```
2k2b1r/1ppq3p/p1n5/P1Qb4/2pp4/N7/1PP2PrP/R1B2RK1 w - - 0 18
```

The rook gives a simple check along the g-file. But the point of *this specific square* is that g2 also sits on the bishop's a8-h1 diagonal — the rook is temporarily blocking its own bishop. **18. Kh1** is forced (f1/f2/h2 are all covered by White's own pieces).

### 18... Rg1+!! — a discovered double check

[![18...Rg1+](https://backscattering.de/web-boardimage/board.svg?fen=2k2b1r/1ppq3p/p1n5/P1Qb4/2pp4/N7/1PP2P1P/R1B2RrK&lastMove=g2g1&coordinates=true&size=320)](https://lichess.org/analysis/standard/2k2b1r/1ppq3p/p1n5/P1Qb4/2pp4/N7/1PP2P1P/R1B2RrK_w_-_-_2_19)

*... 18... Rg1+ — the rook checks directly along the rank, and moving off g2 uncovers the bishop's own check along the diagonal: a genuine double check*

```
2k2b1r/1ppq3p/p1n5/P1Qb4/2pp4/N7/1PP2P1P/R1B2RrK w - - 2 19
```

This is the key idea: the rook's move both delivers its own check (rank 1, rook to h1) **and** clears g2, so the bishop on d5 checks the same king simultaneously along the long diagonal. In a double check, a block or a capture-of-one-checker is never enough — only a king move can answer both checks at once. Here, **19. Kxg1** is the only move that does: it captures the rook *and* steps off the bishop's diagonal in the same move.

### 19... Qg4# — the corridor closes

[![19...Qg4#](https://backscattering.de/web-boardimage/board.svg?fen=2k2b1r/1pp4p/p1n5/P1Qb4/2pp2q1/N7/1PP2P1P/R1B2RK1&lastMove=d7g4&coordinates=true&size=320)](https://lichess.org/analysis/standard/2k2b1r/1pp4p/p1n5/P1Qb4/2pp2q1/N7/1PP2P1P/R1B2RK1_w_-_-_1_20)

*... 19... Qg4# — checkmate*

```
2k2b1r/1pp4p/p1n5/P1Qb4/2pp2q1/N7/1PP2P1P/R1B2RK1 w - - 1 20
```

With the g-file now completely clear, the queen delivers the final check from g4. Every square around the king is accounted for: **f1** and **f2** are blocked by White's own rook and pawn, **h2** by White's own pawn, and **g2**/**h1** are both still covered by the bishop on d5 — the same bishop that made the double check possible two moves earlier is still doing the exact same job at the very end. Verified forced (mate in 2 from the position right after 17... Rxg2+, confirmed by engine analysis).

[*Back to TOP*](#_TOP_)

---

### Related devices

- The clearance sacrifice that produces the discovered double check is the same underlying idea as [Removing the defender](https://github.com/onclemarcel/chess_flashcards/blob/main/patterns/general_principles.md#_removing_the_defender_) in reverse: instead of removing a defender from a target, the rook removes *itself* from its own bishop's line.
- This is not a **windmill** (a windmill repeatedly harvests material through alternating discovered checks) — here the discovered check happens exactly once, and it goes straight to mate rather than looping for material.
- It is not a plain **back-rank mate** either — a back-rank mate needs no long-diagonal piece at all; the trapped king here has an escape square (h1) that only exists because of the bishop, so removing the bishop from the picture would let the king simply step out of the corridor.

[*Back to TOP*](#_TOP_)

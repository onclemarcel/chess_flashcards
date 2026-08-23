<a name="_TOP_"></a>

# General Principles

This page collects opening-agnostic advice pulled from coaching commentary — not tied to one position or opening, so it doesn't belong on any single flashcard. Each entry is tagged with its source (`[DN]` = Daniel Naroditsky, currently the only source; more tags will be added as other commentary gets processed) so future entries can be told apart. Where a principle also shows up concretely on a specific card, that card links back here rather than repeating the explanation, and this page links out to it.

See [start.md](../start.md) for how the opening cards themselves are structured — this page is a companion reference, not a card.

---

<a name="_tunnel_vision_"></a>

### Tunnel vision

[DN] A catch-all for the single most common mistake at the beginner level (roughly 100–1000 rated): fixating on the one thing a move accomplishes and missing something bigger the board is also showing you. Concretely: a player sees "this move attacks a pawn" and plays it without checking what it hangs in the process.

*Source: Speedrun: Back to 3000, game 1 — White played 8. Bf4 attacking c7, missing that Black's queen (already on f6) simply captures the bishop.*

[*Back to TOP*](#_TOP_)

---

<a name="_queen_king_diagonal_"></a>

### Queen and king on the same diagonal — look for pins

Whenever the opponent's queen and king end up on the same diagonal (or rank/file), check whether anything of theirs sitting between them — or about to move there — is pinned. This comes up constantly and is easy to miss when you're focused on your own plan rather than scanning the board's geometry.

[*Back to TOP*](#_TOP_)

---

<a name="_pawn_move_weaknesses_"></a>

### Every pawn move leaves something behind

A pawn can't move backward, so pushing one always gives something up — a square it no longer covers, a piece it no longer shields. After *any* pawn move (yours or the opponent's), check what square or piece is now undefended before deciding your next move. See [C44 Scotch](https://github.com/onclemarcel/chess_flashcards/blob/main/e4_openings/C44_Scotch.md#_Bc5_Nxc6_) for a concrete case: pushing a pawn in front of your own king (f3/g3/h3) is the sharpest version of this — it doesn't just leave a square weak, it can cost you castling rights outright.

[*Back to TOP*](#_TOP_)

---

<a name="_good_move_better_move_"></a>

### When you see a good move, look for a better one

Don't play the first winning-looking move you find — check whether a stronger version of the same idea is available. A capture that also forks or attacks something else is better than the same capture in isolation.

[*Back to TOP*](#_TOP_)

---

<a name="_block_the_check_"></a>

### A check isn't automatically strong — check whether it can just be blocked

Moving the king away is not the only way to answer a check; a piece or pawn can block it too. Beginners in particular tend to chase checks simply because they're checks, especially before either side has developed enough pieces to make the check actually dangerous — always verify the check survives a block before treating it as forcing.

[*Back to TOP*](#_TOP_)

---

<a name="_development_over_structure_"></a>

### Development matters more than pawn structure, especially in the opening

Doubled or otherwise inconvenient pawns are a minor, long-term concern; falling behind in development is an immediate one. Recapturing a certain way to open a bishop's diagonal or gain a tempo is usually worth accepting worse pawns for, particularly in the first several moves. Pawn-structure damage is, in general, an overrated concern relative to how much attention it gets.

[*Back to TOP*](#_TOP_)

---

<a name="_planning_via_obstacles_"></a>

### Making a plan: define the objective, then clear the obstacles in order

A "plan" doesn't have to mean calculating fifteen moves — it can be as simple as naming a concrete objective (castle; win a pawn; trade off the opponent's good bishop) and then asking, one at a time, what's stopping you from doing it right now, and in what order those obstacles need clearing.

*Worked example from [DN]: objective = castle short. Obstacle 1 — the light-squared bishop is in the way, needs a square. Obstacle 2 — its natural square (e3) is undefended. Obstacle 3 — defending e3 with the queen first requires the b2 pawn to not be hanging, so c3 or Nc3 has to come even earlier. The plan falls out of answering the obstacles in reverse order.*

[*Back to TOP*](#_TOP_)

---

<a name="_count_all_defenders_"></a>

### Count *all* the defenders of a piece, not just the first one you notice

Before assuming a piece is undefended or a tactic works, list everything actually covering that square — it's easy to spot one defender, conclude a piece is adequately protected or hanging, and miss a second piece that changes the answer.

[*Back to TOP*](#_TOP_)

---

<a name="_priorities_"></a>

### Know your priorities — a small good/bad-trade question doesn't matter if a bigger one is at stake

When one consideration clearly outranks another (king safety over the "quality" of a particular trade, for instance), stop weighing the smaller one — take whichever trade gets you to the higher priority. Optimising a minor factor while ignoring a major one is a common way to waste moves.

[*Back to TOP*](#_TOP_)

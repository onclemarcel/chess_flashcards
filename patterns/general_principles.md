<a name="_TOP_"></a>

# General Principles

This page collects opening-agnostic advice pulled from coaching commentary — not tied to one position or opening, so it doesn't belong on any single flashcard. Each entry is tagged with its source and game number (`[DN-1]`, `[DN-2]`, ... = Daniel Naroditsky's *Speedrun: Back to 3000* game 1, game 2, etc., transcripts under `transcripts/Naroditsky/Back to 3000 ELO/`; more source initials will be added as other commentary gets processed) so an entry can be traced back to its exact transcript and PGN later. Where a principle also shows up concretely on a specific card, that card links back here rather than repeating the explanation, and this page links out to it.

See [start.md](../start.md) for how the opening cards themselves are structured — this page is a companion reference, not a card.

---

<a name="_tunnel_vision_"></a>

### Tunnel vision

[DN-1] A catch-all for the single most common mistake at the beginner level (roughly 100–1000 rated): fixating on the one thing a move accomplishes and missing something bigger the board is also showing you. Concretely: a player sees "this move attacks a pawn" and plays it without checking what it hangs in the process.

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

*Worked example from [DN-1]: (C44 Scotch 4... Bc5 5. Nxc6 Qf6 6. f3?? dxc6) objective = castle short. Obstacle 1 — the black-squared bishop is in the way, needs to get rid of it. Obstacle 2 — its natural square (e3) is undefended, so Qe2 would be necessary first. Obstacle 3 — defending e3 with the queen requires the b2 pawn to not be hanging, so c3 or Nc3 has to come even earlier.*

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

---

<a name="_removing_the_defender_"></a>

### Removing the defender: a piece guarded by only one other piece is still hanging

[DN-2] If a piece or pawn is protected by exactly one other piece and no pawns, treat it as functionally undefended — its "defender" can simply be removed (captured, deflected, or chased away), after which the original piece just falls. Naroditsky calls this a "type 2 undefended piece": not literally hanging on the board right now, but one tempo away from it. This is the natural companion to [Count *all* the defenders](#_count_all_defenders_) above — that entry is about not *undercounting* defenders, this one is about noticing when the count, even correct, is still fragile because it's exactly one.

*Source: Speedrun: Back to 3000, game 2 — a rook captured a knight that was the sole defender of another piece, winning it outright next move.*

[*Back to TOP*](#_TOP_)

---

<a name="_convert_material_advantage_"></a>

### Converting a big material advantage: open the centre, keep developing, don't chase small material

[DN-2] Once you're up a piece or more (a pawn alone is too small a margin for this to apply), the fastest way to cash the advantage in is usually to **open the position** — especially with the enemy king still uncastled or exposed — rather than to slowly maneuver. An extra queen or rook is only as strong as the open lines it can use. Two companion habits make this work in practice:

- **Keep developing even while up material.** It's tempting to start hunting checkmate immediately, but a piece still sitting on its home square can't help, and ignoring development is how "winning" positions get thrown away to a scrappy counterattack.
- **Don't spend moves defending or chasing trivial material.** If you're up a queen, a single attacked pawn is not a real problem — let it go and keep making progress. This is the same idea as [knowing your priorities](#_priorities_) above, applied specifically to the "I'm winning big, why does this pawn matter" moment.

*Source: Speedrun: Back to 3000, game 2 — after winning the queen via a family fork, White's exposed king made ... d5 (opening the centre) the natural follow-up, and a later attacked pawn was simply ignored in favour of bringing the last rook into the attack.*

[*Back to TOP*](#_TOP_)

---

<a name="_trade_or_attack_"></a>

### Trade or attack when you're up material? It depends on how the pieces you'd keep are actually working

[DN-2] There are two distinct ways to win a game where you're up significant material (roughly a piece or more): trade down toward a simple won endgame (fewer pieces, opponent left with a bare king, promote a pawn), or keep the pieces on the board and use the material edge to mount a direct attack on the king. Neither is "more correct" by default — it depends on the position:

- Trading down is the safer, more mechanical route once you're ahead enough that any reasonably-played endgame wins on its own.
- Keeping pieces on is faster when the extra material can attack the king *immediately* — a queen-up attack against an exposed king can checkmate in a handful of moves, while herding a lone king to the edge of the board with reduced material can take much longer.
- The risk of over-trading: it's easy to get so focused on simplifying that a tactical threat (a back-rank mate is the classic example) gets missed along the way.

In practice, lean toward keeping pieces on when they're already well-placed to attack; lean toward trading when the opponent still has some activity left that swapping pieces would neutralise.

*Source: Speedrun: Back to 3000, game 2 — a standalone demonstration position (queen-up, enemy king exposed) contrasting a slow king-hunt endgame technique with an immediate mating attack that keeps the queen on the board.*

[*Back to TOP*](#_TOP_)

---

<a name="_queen_syndrome_"></a>

### "Queen syndrome": a hanging queen doesn't have to be captured, and neither does anything else

[DN-3] Two related habits Naroditsky groups under one name: (1) when a queen (or any piece) is left hanging or offered as a sacrifice, players tend to assume it *must* be taken immediately, without checking whether a different capture, or no capture at all, is stronger; (2) more generally, an offered gambit or sacrifice can simply be declined. Neither "there's a free queen" nor "there's a pawn on offer" obligates a response — evaluate the position on its own merits first. This is the same discipline as [when you see a good move, look for a better one](#_good_move_better_move_), specifically applied to captures that look too good to pass up.

*Source: Speedrun: Back to 3000, game 3 — with an opponent's queen apparently trapped, the stronger continuation was a different capture entirely (opening an attack on a pawn along the way), not simply grabbing the queen.*

[*Back to TOP*](#_TOP_)

---

<a name="_tempo_plays_"></a>

### Watch out for tempo plays: a piece you just developed can become the opponent's next target

[DN-3] "Developing with tempo" means playing a move that develops a piece *and* attacks something the opponent just placed, forcing them to react instead of following their own plan. When you're the one developing, actively check whether the square you're about to occupy invites this from your opponent's next move — not to avoid it categorically (sometimes allowing tempo loss is fine, or even the position's biggest resource), but to make the choice knowingly rather than by accident.

*Source: Speedrun: Back to 3000, game 3 — a bishop retreat was chosen partly to avoid handing White a developing move that would have attacked it again with tempo.*

[*Back to TOP*](#_TOP_)

---

<a name="_prophylaxis_"></a>

### Prophylaxis: shut down an annoying idea before it's forced on you

[DN-3] A prophylactic move addresses a threat that isn't yet dangerous or even fully concrete — it's not necessary this move, but it removes an annoyance before the opponent gets a free tempo to create real problems with it later. This is a small extra investment (usually one tempo) that pays for itself by taking your opponent's best plan off the table entirely, rather than having to calculate around it move after move.

*Source: Speedrun: Back to 3000, game 3 — a6 was played specifically to rule out White's future a6/queenside-pawn ideas before they could become annoying, not because anything was immediately threatened.*

[*Back to TOP*](#_TOP_)

---

<a name="_protect_the_mating_mechanism_"></a>

### When sacrificing to remove an obstacle, don't sacrifice the piece your mating idea depends on

[DN-3] It's a common and understandable mistake: you've correctly identified that removing a specific pawn or piece would let your attack through, so you sacrifice *something* to get rid of it — but if the piece you gave up is the same one that was going to deliver (or enable) the mate, you've solved the wrong problem. Before sacrificing to clear an obstacle, check that every piece still needed for the actual mating pattern survives the sacrifice.

*Source: Speedrun: Back to 3000, game 3 — the "obvious" way to remove a defending pawn was a bishop sacrifice on that square, which looked identical in effect to the move that actually worked (a queen sacrifice instead) but would have given away control of the exact corner square the mate depended on.*

[*Back to TOP*](#_TOP_)

---

<a name="_castle_timing_"></a>

### When to castle: a beginner default, and when to break it

[DN-3] Castling is far more committal than ordinary development — a developed piece is useful almost anywhere, but a king castled to the wrong side can turn out to be actively dangerous if that side of the board later opens up. As a rough guide: below roughly 700-level play, castle early and often — building the habit of tucking the king away safely matters more than finding exceptions. As you improve, start noticing the cases where the king is genuinely safer staying in the centre a little longer, or where delaying the decision lets you see which side your opponent is actually committing to attack before you commit your own king to the other side.

*Source: Speedrun: Back to 3000, game 3, Q&A — discussing why long castling was chosen and why the decision was deliberately delayed by a couple of moves rather than played automatically.*

[*Back to TOP*](#_TOP_)

[*Back to TOP*](#_TOP_)

# Session memory / roadmap

Living tracker for this repository, across sessions and tools. `start.md` is the "how to write a card" style guide — this file is "how we work, and what's true right now." It used to also carry a full batch-by-batch build log; that's been retired (2026-09-09 cleanup, at the user's request) now that the main sweep is done. The detailed record of *which file covers which position* lives in two places that don't go stale: **`ECO/eco.md`**, where every one of the 500 canonical ECO codes carries a `✅ [covered](url#anchor)` link once treated, and **git log/blame** on the individual card files, which each state their own corrections/divergences inline per this project's own convention (see "Ways of working" below) rather than relying on this file to remember them. Check those first before assuming something needs re-deriving.

---

## Status

**All of ECO A00-E99 (all 500 codes) now has a dedicated card, or an explicit "not built out further here" note inside a parent hub, for every named sub-line `ECO/eco.md` records.** This was built up over two sweeps:

- **Phase B/C (breadth + depth)**, closed 2026-08-25 — one card per opening at a standard 3-plies-past-title depth (or hub + immediate children for a title position that forks), then a second pass going deeper on the openings that most needed it (Ruy Lopez, Sicilian, Queen's Gambit/KID/Grünfeld/Nimzo/QI/Dutch/English).
- **Phase D/E (full ECO-code audit)**, closed 2026-09-09 — cross-checked every one of the 500 codes (not just opening *names*) against `ECO/eco.md`'s own scrape of chessopenings.com, code by code, A00 through E99. This surfaced and fixed dozens of real "wrong root code" and "silent gap in an existing stats table" bugs (see the bug classes below) on top of just filling in missing codes.

If a future session needs the play-by-play of how a specific card came to look the way it does — why a position is split across two files, why a name reads one way in `eco.md` and another live, why a root got re-anchored a ply later — **read that card's own prose first** (this project's standing convention is to state divergences/corrections plainly on the card itself, not bury them in this file) and fall back to `git log -p <file>` if the card is silent. Only reconstruct from scratch if neither has the answer.

---

## Ways of working — sourcing & verification discipline

These are the rules that produced the most self-caught (and user-caught) corrections across the whole build, worth holding onto for any future card work, including the video-to-cards side task below:

- **Every number that ends up on a card — eval, masters game count, popularity %, a name — must be live-verified**, via `tools/explore.py` (Lichess masters+online explorer) and Lichess's own `cloud-eval` API for Stockfish evals. `chessopenings.com` and any other secondary source (a book, a coaching video, chess folklore) is a *discovery* source for names/move-sequences only, never a stats source. Positive eval = good for White, same convention throughout.
- **Never hand-derive a FEN by editing a rank string.** Use `tools/apply_san.py` (or `tools/fen.py`) to replay the actual move sequence — hand-edited rank strings were the single most common source of real bugs across this whole project (a dropped/misplaced pawn, a wrong rank, stale castling rights after O-O, a stray digit), and a wrong FEN silently queries the wrong position rather than erroring. If an eval or game-count looks implausible for the move being described, don't publish it — re-derive and re-query before trusting it.
- **Watch for the "wrong root code" bug class**: a card's own root or main-line position can carry a *different* live ECO code than its title claims. Always spot-check a card's root FEN against `tools/explore.py`'s own `opening` field, not just against what `eco.md`'s move-sequence depth implies. Three related shapes this took repeatedly:
  - **A single code carries multiple unrelated names** (e.g. A41 covers seven distinct ideas from "Queen's Pawn Game" to "Old Indian Defense" to "Zukertort Opening") — searching for just one representative name silently hides the others. When auditing a code, enumerate every distinct name Lichess records for it before concluding it's covered.
  - **A card's main/most-built branch actually belongs to a sibling code one ply deeper** (e.g. `A02_Bird.md` was built entirely around a position that's really A03; `B10_Caro_Kann.md`'s whole Advance Variation was really B12) — check this at the card's own *shallowest* fork, not wherever a deeper divergence happens to be flagged; a card can look fine at a deep fork while its own root/main-line is already mislabeled.
  - **A generic name applies at a fork, a more specific one only a ply or two deeper** (e.g. a position is "King's Indian Attack: Sicilian Variation" until Black's specific reply makes it the "French Variation") — name it precisely at the ply it actually earns, don't force the deeper name onto the shallower position or vice versa.
- **Never assert a transposition without verifying the resulting FEN matches the target card's own root.** If unverified, use the safe phrasing "a real, secondary try with no code of its own in this range" and stop there — several genuine mistakes (claiming a transposition that turned out false) were only caught this way, and it's cheap to just check with `apply_san.py`.
- **Sanity-check tactical/trap claims (forks, mates, "wins a piece") against `cloud-eval` before writing them** — pattern-matching a claim from a similar-looking line in another opening produced real wrong claims (a "Center Fork Trick" that didn't exist, a "just wins" line that was actually equal) more than once. Popularity/eval numbers from the explorer are reliable; hand-recalled tactical lines are not, even when they sound right.
- **A near-even fork (masters split under roughly 15 points apart) gets presented as real sibling candidates, not forced into one "main line"** — reserve full depth-building for a branch that actually dominates; forks resolve into sibling cards/sections instead. Conversely, note plainly (don't silently paper over) any online-vs-masters inversion — a move online players favor heavily that masters barely touch, or vice versa — it's recurred often enough (Budapest, Modern Defense, Pirc 150 Attack, Queen's Indian, Kan, Scheveningen, and many more) to be a genuinely common and worth-flagging pattern in this repo's data, not a one-off curiosity.
- **When a "wrong root code" position is a small mention but the correct card already exists and is well-scoped**, expand the existing card to explicitly own the whole code's real content rather than force a disruptive migration of a large, heavily cross-linked hub section. Conversely, if one live ECO code's content has ended up split across multiple files, merge it back into one.
- **Renaming a file is part of a rescoping fix, not a separate cleanup step** — if a card's scope changes enough that its title changes, its filename should follow in the same pass (`git mv`, then a repo-wide search for the old filename in every link).

## Ways of working — tooling gotchas worth remembering

- **Run `tools/update_stats.py` before `tools/check_diagram.py`, never the other way** — checking a diagram against an unpopulated `...generated table...` placeholder passes trivially and proves nothing.
- **`check_diagram.py`'s shape/eval check matches by nearest text proximity, not by which table a node "really" belongs to.** A short, common SAN (Nf3, d4, Bg5...) that recurs elsewhere on a long page can silently match the wrong row — if a shape-classification looks wrong, check for this before trusting the tool; the fix is usually to drop to a plain unclassified rectangle rather than force a data-driven shape without an unambiguous table behind it. Similarly, a node's eval only satisfies the checker if that exact number appears in a forward-looking text window from the move text — a move introduced only as inline prose (no heading of its own) needs its eval written out in parentheses right next to it.
- **A mermaid `click` target combining a cross-file blob URL with a `#anchor` fragment false-flags as a missing file** in `check_diagram.py` (it doesn't strip the fragment before checking existence) — stick to bare cross-file links without an anchor, matching the rest of the repo, rather than patching the checker for one-off use.
- **Lichess `cloud-eval` can hit a genuine IP-level rate-limit block** that persists well past their documented cooldown — if querying with an `Authorization: Bearer` header still 429s after a few minutes of conservative backoff, that's a real network-level throttle, not something more waiting fixes on a predictable timeline; changing the network path (VPN, different connection) is the actual fix. Query with the auth header anyway even though the endpoint doesn't require it — the JSON error response is far easier to detect programmatically than the anonymous path's HTML error page.
- **`tools/fen.py`, `tools/apply_san.py`, `tools/explore.py`, `tools/update_stats.py`, `tools/check_diagram.py`** are all promoted, persistent, and safe to reuse as-is — no need to rebuild anything in `scratchpad/` for these; scratchpad itself does not survive a session, so a one-off script written there for a specific audit (crawlers, TSV-diffing, annotate-eco helpers) needs rebuilding if a future session wants the same kind of pass again.

## File naming convention

Card filenames are `<ECO or folder prefix>_<Name>[_<disambiguator>].md`. A move fragment (like `Nf3`, `d4`, `exd5`) belongs in the filename **only** when it's the actual thing distinguishing this card from a sibling that would otherwise share the same name — never just because it's part of the position's move sequence. Drop the move when the ECO code + descriptive name already uniquely identify the card (e.g. `B01_Scandinavian.md`, not `B01_1e4d5_Scandinavian.md`); keep it when siblings share a generic name and the move is the real differentiator (e.g. the `Sicilian ... Open` family, `C88_Ruy_Lopez_Closed_Bb3.md`). Repeating a descriptive name across different ECO codes with no move at all is fine and normal — the ECO prefix alone keeps filenames unique.

**One file per ECO code**: a card file corresponds to exactly one live ECO code, not one "opening idea" or one branch of a hub. If a position within a card is itself already live-tagged a *different* code than the file's own title, that content belongs in its own separate file at that code — even one ply deeper, even if it would be convenient to keep it alongside its parent. The one exception is the literal boundary ply: a root card may show the single forced/near-forced reply that leads into the next code, but the deeper content itself still moves out. Always verify the live tag via the explorer before deciding where a boundary falls — never assume it matches `eco.md`'s own move-sequence depth.

**Renaming safely**: `git mv` (preserves history), then a repo-wide replace of every literal occurrence of the old filename (link text untouched, only the filename portion of the URL), then three verification passes — `tools/check_diagram.py` (mermaid `click` targets), a grep-based scan for zero remaining references to the old filename, and an audit of every `github.com/.../blob/main/...` link resolving to a real path on disk.

---

## Environment prerequisites (local dev machine)

Two local blockers, needed before any live Lichess query works from this machine's MSYS2/mingw64 Python (`C:\msys\mingw64\bin\python.exe`, no pip, no bundled CA store):

1. **CA bundle**: `SSL_CERT_FILE` → `C:\Users\march\.certs\cacert.pem` (from `https://curl.se/ca/cacert.pem`). Without it, `urllib` fails with `CERTIFICATE_VERIFY_FAILED`.
2. **Lichess token**: anonymous explorer requests are refused (HTTP 401) from this network. `LICHESS_TOKEN` (no scope needed) must be set — the same token already used by the `update-stats.yml` GitHub Actions secret works locally too.

Both are persisted as **Windows user environment variables**, so any *new* shell picks them up automatically. A shell already running before they were set won't see them — export inline for the rest of that session:

```
SSL_CERT_FILE=/c/Users/march/.certs/cacert.pem LICHESS_TOKEN=<token> python tools/update_stats.py ...
```

If a Bash shell doesn't inherit them and printing the token is blocked by the secret-exposure guard, set both vars inside a single PowerShell command (`$env:X = [Environment]::GetEnvironmentVariable(...)`) immediately before each tool invocation instead — the value never gets printed anywhere.

**Stockfish evals**: no local engine installed. Use the Lichess cloud-eval API instead (same token/trust store):
```
curl -H "Authorization: Bearer $LICHESS_TOKEN" "https://lichess.org/api/cloud-eval?fen=<url-encoded FEN>"
```
Returns `{"cp": N}` (nested inside `pvs[0]`, not top-level) or `{"mate": N}`. Positive = good for White. Convert `cp` → pawns by dividing by 100. Not every obscure sideline is cached server-side — if it 404s, don't invent a number; fall back to prose.

---

## Side task: video-to-cards (recurring — this is likely most of what's next)

Alongside theory/statistics-driven authoring, the recurring side task is processing transcripts of chess coaching videos (and, going forward per the user's own framing, books/game analysis/player-study material more generally) and folding the useful content into existing cards — never paste a full transcript in.

- **Tag every video/source-derived addition `[<source-initials>-<game number>]`** (e.g. `[DN-1]`, `[DN-2]` for Daniel Naroditsky; `[IS-1]`...`[IS-7]` for Igor Smirnov) so it can be traced back to its exact source later. Extend this same tagging convention to new sources (books, player-analysis material) as they come up — pick short initials, keep a running number per source, and log the mapping here as it grows:
  - `[DN-1]` = `transcripts/Naroditsky/Back to 3000 ELO/397.txt`, `[DN-2]` = `476.txt`, `[DN-3]` = `491.txt`
  - `[IS-1]` through `[IS-7]` = the seven games in `transcripts/Smirnov/grob.txt`, in file order (the source file mislabels two different games both "GAME 5" — disambiguated here as the two `[IS-5]` occurrences)
- **Never trust a transcript's algebraic notation at face value.** Auto-transcription mangles move letters in plausible-sounding ways ("movie five" = "move d5", "rookie one" = "Rd1", "t4" = "d4"). Reconstruct the actual game from context/legality and verify every move and eval live, exactly like the theory-authoring workflow above. If a position can't be reconstructed with real confidence, don't force a diagram — prose-only is fine. **When a PGN is supplied alongside a transcript, replay it move-by-move first** — turns "reconstruct from context" into "verify what's known," and catches transcription mistakes fast.
- **If a transcript has a real, unresolvable gap** (a move never stated, an ambiguous narration), ask the user directly rather than picking a "representative" placeholder — they may simply know the answer, since it's a fact about a real source, not something to approximate.
- **A hand-derived tactical/mating claim is worth double-checking with code, not just re-reading the board** — a small piece-by-piece attacker-finder script settled a mate-in-1 misattribution in one call after manual counting got it wrong twice.
- **Four destinations for extracted content**, decided per item:
  1. **A position-specific point that's new depth on an existing card** → add inline (`[!TIP]`/`[!NOTE]`, or extend a bullet), same shape as the rest of that card.
  2. **An opening-agnostic principle** → `patterns/general_principles.md` (companion to `start.md`, one anchored entry per principle, tagged by source). Cards that concretely illustrate a principle link to its anchor there rather than re-explaining it. Not every minute of a source needs a card update — broad commentary that will recur across many future sources can go straight to prose here without chasing full verification.
  3. **A whole new named trap/variation not covered anywhere** → its own card, same rigor as any other card.
  4. **A genuinely new checkmate pattern** → `mates/mate_patterns.md` (thin index, mirrors `traps/opening_traps.md`) plus `mates/<Pattern_Name>/<Pattern_Name>.md`. Don't force an inaccurate named-mate label onto a pattern that doesn't cleanly match one — describe the mechanism directly and name the general family it belongs to instead.
- **A whole-card restructuring** (dropping the normal depth cap to fold several games directly into one card's own move tree, e.g. `A00_openings/Grob.md`'s seven-game rebuild) is sometimes the right call for a source that's essentially a curated trap anthology for one opening — `start.md` already exempts genuine trap/gambit cards from the depth cap. Confirm this kind of structural change with the user before doing it, it's a bigger call than a normal inline addition.
- Run `tools/update_stats.py` + `tools/check_diagram.py` after every addition, same as any other edit.

---

## Closed side quests

- **Offbeat/uncommon-opening coverage** (opened 2026-08-24) — the concern that popular openings were getting deep treatment while less-common ECO ranges (Alekhine's, Nimzo-Larsen/Bird, Veresov/Torre/Catalan, and eventually every A00-B00 irregular first/second move) had none. Folded into the main Phase B/D sweep rather than run as a separate track; fully closed along with everything else above.

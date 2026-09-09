#!/usr/bin/env python3
"""Build a frequency tree of one player's own moves from their PGN archive(s).

Mirrors what explore.py does against the Lichess masters DB, except the
"database" here is one specific player's own game history -- built for the
players/ player-study side task (see memory.md), where a specific opponent's
practical repertoire matters more than what masters play. At every position
reached in any game, records what was actually played next and how often,
tagged with whose move it was (the tracked player's, or their opponent's).

A normalized FEN key (board+turn+castling+ep, dropping the halfmove/fullmove
counters) is used so that transposing move orders share one tree node --
this is what makes "does this player converge on the same position via
different move orders" directly visible in the output.

Usage:
    python tools/player_tree.py <player_name> <white.pgn> <black.pgn> \
        --max-plies 20 --dump-json out.json

Games are matched to the tracked player by the PGN's own White/Black header
(case-insensitive substring match against <player_name>), not just by which
file they came from -- so a mixed PGN (both colors in one file) also works
if you pass the same file for both white.pgn/black.pgn args.
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fen import Board  # noqa: E402
from apply_san import resolve_san  # noqa: E402

START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"


def norm_key(fen: str) -> str:
    """Drop halfmove/fullmove counters so transposing games share a key."""
    return " ".join(fen.split()[:4])


def parse_pgn(path: str):
    """Yield (headers_dict, [san_tokens]) per game in a PGN file."""
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    headers: dict[str, str] = {}
    move_lines: list[str] = []
    in_moves = False

    def finalize():
        if not headers:
            return None
        text = " ".join(move_lines)
        text = re.sub(r"\{[^}]*\}", " ", text)  # strip comments
        text = re.sub(r"\$\d+", " ", text)  # strip NAGs
        tokens = []
        for tok in text.split():
            tok = re.sub(r"^\d+\.+", "", tok)
            if not tok or tok in ("1-0", "0-1", "1/2-1/2", "*"):
                continue
            tokens.append(tok)
        return dict(headers), tokens

    for line in lines:
        if line.startswith("["):
            if in_moves:
                g = finalize()
                if g:
                    yield g
                headers, move_lines, in_moves = {}, [], False
            m = re.match(r'\[(\w+)\s+"(.*)"\]', line)
            if m:
                headers[m.group(1)] = m.group(2)
        elif line.strip():
            in_moves = True
            move_lines.append(line.strip())
    g = finalize()
    if g:
        yield g


def build_tree(pgn_path: str, player: str, side: str, max_plies: int, tree: dict, meta: dict, fails: Counter):
    """side is 'white' or 'black': which color `player` is expected to be in this file."""
    needle = player.lower()
    n_games = n_matched = n_ok = 0
    for headers, sans in parse_pgn(pgn_path):
        n_games += 1
        who = headers.get(side.capitalize(), "")
        if needle not in who.lower():
            continue
        n_matched += 1
        board = Board(START_FEN)
        ply = 0
        ok = True
        for san in sans:
            if ply >= max_plies:
                break
            is_player_move = (board.turn == "w" and side == "white") or (board.turn == "b" and side == "black")
            key = norm_key(board.to_fen())
            try:
                uci = resolve_san(board, san)
            except Exception:
                fails[f"{side}:resolve"] += 1
                ok = False
                break
            tree.setdefault(key, Counter())[san] += 1
            meta.setdefault(key, {"fen": board.to_fen(), "depth": ply, "player_to_move": is_player_move})
            board.apply_uci(uci)
            ply += 1
        n_ok += ok
    print(
        f"{pgn_path}: {n_games} games, {n_matched} matched '{player}' as {side}, "
        f"{n_ok} fully replayed",
        file=sys.stderr,
    )


def main() -> None:
    args = sys.argv[1:]
    max_plies = 20
    dump_path = None
    pos_args = []
    i = 0
    while i < len(args):
        if args[i] == "--max-plies":
            max_plies = int(args[i + 1])
            i += 2
        elif args[i] == "--dump-json":
            dump_path = args[i + 1]
            i += 2
        else:
            pos_args.append(args[i])
            i += 1
    if len(pos_args) < 3:
        print(__doc__)
        sys.exit(1)
    player, white_pgn, black_pgn = pos_args[0], pos_args[1], pos_args[2]

    fails: Counter = Counter()
    out = {}
    for side, path in (("white", white_pgn), ("black", black_pgn)):
        tree: dict[str, Counter] = {}
        meta: dict[str, dict] = {}
        build_tree(path, player, side, max_plies, tree, meta, fails)
        print(f"{side}: {len(tree)} distinct positions recorded", file=sys.stderr)
        out[side] = {
            key: {
                "fen": meta[key]["fen"],
                "depth": meta[key]["depth"],
                "player_to_move": meta[key]["player_to_move"],
                "moves": dict(cnt),
            }
            for key, cnt in tree.items()
        }
    print(f"fail counts: {dict(fails)}", file=sys.stderr)

    if dump_path:
        with open(dump_path, "w", encoding="utf-8") as f:
            json.dump(out, f)
        print(f"dumped to {dump_path}", file=sys.stderr)
    else:
        json.dump(out, sys.stdout)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Walk a player_tree.py JSON dump and print a readable repertoire tree.

At the tracked player's own turns: show every reply carrying at least
min_share of that node's traffic (always at least the single top reply).
At the opponent's turns: show the top opp_top_k replies regardless of
share, to keep the tree from exploding while still surfacing the real
alternatives a reader would actually face.

Usage:
    python tools/player_report.py <tree.json> <white|black> \
        [max_depth] [min_share] [opp_top_k] [min_games]
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fen import Board  # noqa: E402
from apply_san import resolve_san  # noqa: E402

START_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
_APPLY_CACHE: dict[tuple[str, str], str | None] = {}


def norm_key(fen: str) -> str:
    return " ".join(fen.split()[:4])


def advance(fen: str, san: str) -> str | None:
    key = (fen, san)
    if key in _APPLY_CACHE:
        return _APPLY_CACHE[key]
    board = Board(fen)
    try:
        uci = resolve_san(board, san)
    except Exception:
        _APPLY_CACHE[key] = None
        return None
    board.apply_uci(uci)
    result = board.to_fen()
    _APPLY_CACHE[key] = result
    return result


def walk(data, key, indent, max_depth, min_share, opp_top_k, min_games, path):
    node = data.get(key)
    if node is None:
        return
    if node["depth"] >= max_depth:
        return
    moves = node["moves"]
    total = sum(moves.values())
    if total < min_games:
        return
    ranked = sorted(moves.items(), key=lambda kv: -kv[1])
    is_player = node["player_to_move"]
    tag = "P" if is_player else "opp"

    shown = [(s, c) for s, c in ranked if c / total >= min_share] or [ranked[0]] if is_player else ranked[:opp_top_k]

    for san, cnt in shown:
        share = cnt / total
        print(f"{'  ' * indent}[{tag}] {san:6s} {cnt:4d}/{total:4d} ({share*100:4.1f}%)  path: {' '.join(path + [san])}")
        nxt = advance(node["fen"], san)
        if nxt:
            walk(data, norm_key(nxt), indent + 1, max_depth, min_share, opp_top_k, min_games, path + [san])


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    json_path, side = sys.argv[1], sys.argv[2]
    max_depth = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    min_share = float(sys.argv[4]) if len(sys.argv) > 4 else 0.15
    opp_top_k = int(sys.argv[5]) if len(sys.argv) > 5 else 2
    min_games = int(sys.argv[6]) if len(sys.argv) > 6 else 15
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)[side]
    walk(data, norm_key(START_FEN), 0, max_depth, min_share, opp_top_k, min_games, [])


if __name__ == "__main__":
    main()

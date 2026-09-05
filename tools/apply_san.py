#!/usr/bin/env python3
"""Apply a sequence of SAN moves to a FEN, printing the resulting FEN after
each move. Built to chase eco.md's own SAN move lists directly, instead of
hand-converting each SAN move to UCI by eye (the single most error-prone step
in this repo's whole workflow per memory.md — this sidesteps it entirely).

Reuses tools/fen.py's Board class for placement/castling/en-passant
bookkeeping; only adds a SAN resolver on top. Does NOT verify check legality
(assumes the input is a real book line) — it only checks piece geometry,
blocking pieces on sliding paths, and disambiguation hints.

Usage:
    python tools/apply_san.py "<start-fen>" e4 e5 Nf3 Nc6 Bb5 ...
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fen import Board, FILES, sq_to_idx, idx_to_sq  # noqa: E402


def piece_targets(board: Board, idx: int, piece: str) -> list[int]:
    """Pseudo-legal destination squares for the piece at idx (ignores checks)."""
    r, f = divmod(idx, 8)
    targets: list[int] = []
    p = piece.upper()
    white = piece.isupper()

    def add_ray(dr: int, df: int) -> None:
        rr, ff = r + dr, f + df
        while 0 <= rr < 8 and 0 <= ff < 8:
            t = rr * 8 + ff
            targets.append(t)
            if board.squares[t]:
                break
            rr += dr
            ff += df

    if p == "N":
        for dr, df in ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)):
            rr, ff = r + dr, f + df
            if 0 <= rr < 8 and 0 <= ff < 8:
                targets.append(rr * 8 + ff)
    elif p == "B":
        for dr, df in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            add_ray(dr, df)
    elif p == "R":
        for dr, df in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            add_ray(dr, df)
    elif p == "Q":
        for dr, df in ((1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)):
            add_ray(dr, df)
    elif p == "K":
        for dr in (-1, 0, 1):
            for df in (-1, 0, 1):
                if dr == 0 and df == 0:
                    continue
                rr, ff = r + dr, f + df
                if 0 <= rr < 8 and 0 <= ff < 8:
                    targets.append(rr * 8 + ff)
    elif p == "P":
        step = 1 if white else -1
        start_rank = 1 if white else 6
        one = (r + step) * 8 + f
        if 0 <= r + step < 8 and not board.squares[one]:
            targets.append(one)
            two = (r + 2 * step) * 8 + f
            if r == start_rank and not board.squares[two]:
                targets.append(two)
        for df in (-1, 1):
            ff = f + df
            if 0 <= ff < 8 and 0 <= r + step < 8:
                t = (r + step) * 8 + ff
                tgt_piece = board.squares[t]
                is_ep = idx_to_sq(t) == board.ep
                if (tgt_piece and tgt_piece.isupper() != white) or is_ep:
                    targets.append(t)
    return targets


def resolve_san(board: Board, san: str) -> str:
    """Return the UCI move for one SAN token against the current board."""
    s = san.strip().rstrip("+#!?")
    white = board.turn == "w"

    if s in ("O-O", "0-0"):
        rank = 0 if white else 7
        return f"{idx_to_sq(rank * 8 + 4)}{idx_to_sq(rank * 8 + 6)}"
    if s in ("O-O-O", "0-0-0"):
        rank = 0 if white else 7
        return f"{idx_to_sq(rank * 8 + 4)}{idx_to_sq(rank * 8 + 2)}"

    promo = ""
    if "=" in s:
        s, promo_part = s.split("=")
        promo = promo_part[0].lower()

    piece = "P"
    if s[0] in "NBRQK":
        piece = s[0]
        s = s[1:]
    else:
        s = s

    is_capture = "x" in s
    s = s.replace("x", "")

    dest = s[-2:]
    disamb = s[:-2]  # optional file/rank/square hint

    dest_idx = sq_to_idx(dest)

    disamb_file = None
    disamb_rank = None
    for ch in disamb:
        if ch in FILES:
            disamb_file = FILES.index(ch)
        elif ch.isdigit():
            disamb_rank = int(ch) - 1

    candidates = []
    for idx, pc in enumerate(board.squares):
        if not pc or pc.upper() != piece:
            continue
        if pc.isupper() != white:
            continue
        r, f = divmod(idx, 8)
        if disamb_file is not None and f != disamb_file:
            continue
        if disamb_rank is not None and r != disamb_rank:
            continue
        if dest_idx in piece_targets(board, idx, pc):
            candidates.append(idx)

    if piece == "P" and not candidates:
        # pawn capture disambiguation carries the file as a letter, not a square
        for idx, pc in enumerate(board.squares):
            if not pc or pc.upper() != "P" or pc.isupper() != white:
                continue
            r, f = divmod(idx, 8)
            if disamb_file is not None and f != disamb_file:
                continue
            if dest_idx in piece_targets(board, idx, pc):
                candidates.append(idx)

    if len(candidates) != 1:
        raise ValueError(
            f"SAN '{san}' resolved to {len(candidates)} candidates "
            f"({[idx_to_sq(c) for c in candidates]}) on board {board.to_fen()}"
        )

    frm = idx_to_sq(candidates[0])
    return f"{frm}{dest}{promo}"


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    fen = sys.argv[1]
    board = Board(fen)
    for san in sys.argv[2:]:
        uci = resolve_san(board, san)
        board.apply_uci(uci)
        print(f"{san:8s} {uci:6s} {board.to_fen()}")


if __name__ == "__main__":
    main()

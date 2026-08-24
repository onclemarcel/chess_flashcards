#!/usr/bin/env python3
"""Hand-rolled FEN move-applier (no external deps — this machine has no pip).

Applies a sequence of moves (SAN-ish or UCI, see below) to a FEN and prints
the resulting FEN after each move. Promoted into tools/ 2026-08-24 after being
rebuilt from scratch in scratchpad/ across batches 8, 9, 10, 15 (see memory.md)
every time a session needed multi-ply FEN generation for a new card.

Usage:
    python tools/fen.py "<start-fen>" e2e4 e7e5 g1f3 ...

Moves are UCI (from-square + to-square + optional promotion letter, e.g.
"e7e8q"). Castling is "e1g1"/"e1c1"/"e8g8"/"e8c8" (king's own two-square move).
En passant is detected automatically from the target square.

Prints one FEN per line, one per move applied, to make it easy to grab the
FEN after any specific ply without re-running for each depth.
"""

from __future__ import annotations

import sys

FILES = "abcdefgh"


def sq_to_idx(sq: str) -> int:
    f = FILES.index(sq[0])
    r = int(sq[1]) - 1
    return r * 8 + f


def idx_to_sq(idx: int) -> str:
    r, f = divmod(idx, 8)
    return f"{FILES[f]}{r + 1}"


class Board:
    def __init__(self, fen: str):
        parts = fen.split()
        placement, self.turn, self.castling, self.ep, self.halfmove, self.fullmove = parts
        self.squares = [""] * 64
        rank = 7
        file = 0
        for ch in placement:
            if ch == "/":
                rank -= 1
                file = 0
            elif ch.isdigit():
                file += int(ch)
            else:
                self.squares[rank * 8 + file] = ch
                file += 1
        self.halfmove = int(self.halfmove)
        self.fullmove = int(self.fullmove)

    def to_fen(self) -> str:
        rows = []
        for rank in range(7, -1, -1):
            row = ""
            empty = 0
            for file in range(8):
                piece = self.squares[rank * 8 + file]
                if piece:
                    if empty:
                        row += str(empty)
                        empty = 0
                    row += piece
                else:
                    empty += 1
            if empty:
                row += str(empty)
            rows.append(row)
        placement = "/".join(rows)
        castling = self.castling if self.castling else "-"
        ep = self.ep if self.ep else "-"
        return f"{placement} {self.turn} {castling} {ep} {self.halfmove} {self.fullmove}"

    def apply_uci(self, move: str) -> None:
        frm = sq_to_idx(move[0:2])
        to = sq_to_idx(move[2:4])
        promo = move[4] if len(move) > 4 else None
        piece = self.squares[frm]
        if not piece:
            raise ValueError(f"No piece on {move[0:2]} (move {move}) — FEN before: {self.to_fen()}")
        captured = self.squares[to]
        is_pawn = piece.upper() == "P"
        is_capture = bool(captured)

        # en passant capture: pawn moves to the ep target square, diagonally, no piece there
        if is_pawn and move[2:4] == self.ep and to != frm and (to % 8) != (frm % 8) and not captured:
            cap_idx = to - 8 if piece.isupper() else to + 8
            self.squares[cap_idx] = ""
            is_capture = True

        # castling: king moves two files
        if piece.upper() == "K" and abs((to % 8) - (frm % 8)) == 2:
            rank = frm // 8
            if to % 8 == 6:  # kingside
                rook_from = rank * 8 + 7
                rook_to = rank * 8 + 5
            else:  # queenside
                rook_from = rank * 8 + 0
                rook_to = rank * 8 + 3
            self.squares[rook_to] = self.squares[rook_from]
            self.squares[rook_from] = ""

        self.squares[to] = (promo.upper() if piece.isupper() else promo.lower()) if promo else piece
        self.squares[frm] = ""

        # castling rights: king or rook moved, or rook captured on its home square
        for sq, right in ((0, "Q"), (7, "K"), (56, "q"), (63, "k")):
            if frm == sq or to == sq:
                self.castling = self.castling.replace(right, "")
        if piece.upper() == "K":
            self.castling = self.castling.replace("K" if piece.isupper() else "k", "")
            self.castling = self.castling.replace("Q" if piece.isupper() else "q", "")

        # en passant target for next move
        if is_pawn and abs(to - frm) == 16:
            self.ep = idx_to_sq((to + frm) // 2)
        else:
            self.ep = ""

        self.halfmove = 0 if (is_pawn or is_capture) else self.halfmove + 1
        if self.turn == "b":
            self.fullmove += 1
        self.turn = "b" if self.turn == "w" else "w"


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    fen = sys.argv[1]
    board = Board(fen)
    for move in sys.argv[2:]:
        board.apply_uci(move)
        print(board.to_fen())


if __name__ == "__main__":
    main()

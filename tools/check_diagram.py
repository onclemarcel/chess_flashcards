#!/usr/bin/env python3
"""Check that a card's "Overview" fishbone diagram (a Mermaid flowchart) has
not drifted from the candidate-move prose and stats tables it summarises.

Each node in the diagram is expected to look like:

    id<shape-open>"<move text> [flags]<br/>(<eval>)?"<shape-close>[:::main]
    click id "<target>"

where <move text> matches a move exactly as written in a "### Candidate
moves" bullet elsewhere in the same file, [flags] is an optional run of
'!', '!!', '?', '??', the warning triangle (online/masters gap), '⇄'
(transposes into a named opening), '♙' (a gambit) and/or '💣' (a trap --
i.e. its target is a [!TIP] block, per start.md's own "Tips highlight mate
patterns and traps" rule), <target> is either an in-page anchor ("#_X_") or
a full https://.../blob/main/... URL, and the node's *shape* claims one of
four data-driven categories (see SHAPES below). The ':::main' class is
independent of shape: it marks the line this card follows deeper, not a
statistical property.

This script does NOT re-derive the diagram from the prose or tables (that
would make it a generator, not a checker) and it does NOT judge whether a
'!'/'?' annotation is chess-correct -- both stay hand-authored. What it
verifies mechanically, per node:

  1. anchor targets ("#_X_") resolve to an <a name="_X_"> (or legacy
     <a id="_X_">) somewhere in the same file;
  2. external targets (github.com/.../blob/main/...) resolve to a file that
     actually exists in the repository;
  3. the node's move text appears verbatim in the file's own prose, outside
     the diagram block itself (catches renamed/retyped moves);
  4. if the node's label carries an eval number, at least one occurrence of
     that move text in the prose is followed on the same line by the same
     number (catches an eval edited in one place but not the other);
  5. if the node's label carries the warning triangle, at least one nearby
     occurrence of the move text in the prose also carries it;
  6. the node's SHAPE (rectangle / subroutine / rhombus / stadium / hexagon)
     is checked against the online%/masters% of the nearest matching row in
     one of the file's own '<!-- lichess-stats -->' tables, using the fixed
     thresholds in SHAPES below. A rhombus (blitz trap) or subroutine
     (master-safe) node whose own table row doesn't back up that category
     is reported. Hexagon (blunder) nodes are instead checked against the
     eval of their best sibling (same source arrow) for a >=0.9 swing.
     Nodes with no matching table row (e.g. combined or off-page moves)
     are skipped for this check, not treated as a failure.

Usage:
    python tools/check_diagram.py                 # walk the whole repository
    python tools/check_diagram.py path/to/card.md  # one file
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
import urllib.parse

MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)

# Ordered longest-delimiter-first so e.g. '[[' isn't swallowed by '['.
NODE_RE = re.compile(
    r'(?P<id>[A-Za-z_][A-Za-z0-9_]*)'
    r'(?:'
    r'\[\[\s*"(?P<sub>[^"]*)"\s*\]\]'
    r'|\(\[\s*"(?P<stad>[^"]*)"\s*\]\)'
    r'|\{\{\s*"(?P<hex>[^"]*)"\s*\}\}'
    r'|\{\s*"(?P<rhomb>[^"]*)"\s*\}'
    r'|\[\s*"(?P<rect>[^"]*)"\s*\]'
    r')'
    r'(?P<main_cls>:::main)?'
)
EDGE_RE = re.compile(
    r'(?P<src>[A-Za-z_][A-Za-z0-9_]*)\s*-->\s*(?P<dst>[A-Za-z_][A-Za-z0-9_]*)'
)
CLICK_RE = re.compile(r'click\s+(?P<id>[A-Za-z_][A-Za-z0-9_]*)\s+"(?P<target>[^"]+)"')
ANCHOR_RE = re.compile(r'<a\s+(?:name|id)="([^"]+)"')
EVAL_RE = re.compile(r'(?<![\w.])([+-]?\d+\.\d+|#-?\d+)(?![\w.])')
FLAG_CHARS = "!?⚠⇄♙💣"  # '!', '?', online/masters gap, transposition, gambit, trap
CALLOUT_RE = re.compile(r'>\s*\[!(NOTE|TIP)\]')
BULLET_RE = re.compile(r'^\s*[*-]\s')
REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
GITHUB_BLOB_RE = re.compile(
    r"https://github\.com/onclemarcel/chess_flashcards/blob/main/(?P<path>.+)$"
)

# shape name -> (mermaid group name, category test on (online_pct, masters_pct))
SHAPES = {
    "rect": "unclassified",
    "sub": "master-safe",     # masters_pct >= 20
    "rhomb": "blitz-trap",    # masters_pct < 2, online_pct >= 3, and a >=8x gap between them
    "stad": "understudied",   # masters_pct < 2 and online_pct < 3 (low everywhere)
    "hex": "blunder",         # checked separately, via sibling evals
}
MASTER_SAFE_MIN = 20.0
TRAP_MASTERS_MAX = 2.0
TRAP_ONLINE_MIN = 3.0
TRAP_RATIO_MIN = 8.0   # online_pct / masters_pct, at masters_pct's own scale
BLUNDER_SWING = 0.9

TABLE_ROW_RE = re.compile(
    r'^\|\s*(?P<move>[A-Za-z0-9+#=\-]+)\s*\|'
    r'(?P<online_cell>[^|]*)\|[^|]*\|'
    r'(?P<masters_cell>[^|]*)\|',
    re.MULTILINE,
)
CELL_PCT_RE = re.compile(r'\(([\d.]+)%\)')


def cell_pct(cell: str) -> float | None:
    """A stats-table count/pct cell is always either '0' (no games) or
    'N (X.X%)' (see tools/update_stats.py's cell_count()) -- never a bare
    number with no games info, so a percentage-less cell unambiguously
    means zero. Search (not match) for the percentage: don't be tempted to
    fall back to a literal '0' check on failure -- that regex trap is
    exactly what broke this the first time (matched the '0' inside '80').
    """
    m = CELL_PCT_RE.search(cell)
    if m:
        return float(m.group(1))
    return 0.0 if cell.strip() == "0" else None


def strip_move_number(move: str) -> str:
    """'2. exd5' -> 'exd5', '2... Qxd5' -> 'Qxd5'."""
    return re.sub(r'^\d+\.(?:\.\.)?\s*', '', move).strip()


def split_label(label: str) -> tuple[str, str, bool]:
    """Split a node label into (bare_move, eval_or_empty, has_warning)."""
    text = label.replace("<br/>", "\n").replace("<br>", "\n")
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    move_line = lines[0] if lines else ""
    eval_str = ""
    for l in lines[1:]:
        m = EVAL_RE.search(l)
        if m:
            eval_str = m.group(1)
            break
    has_warning = "⚠" in label
    bare_move = move_line
    for ch in FLAG_CHARS:
        bare_move = bare_move.replace(ch, "")
    bare_move = bare_move.strip()
    return bare_move, eval_str, has_warning


def find_anchors(text: str) -> set[str]:
    return set(ANCHOR_RE.findall(text))


def callout_type(text: str, anchor: str) -> str | None:
    """'NOTE' or 'TIP' if <a name="anchor"> sits inside that kind of
    blockquote callout, else None (main-line content, not inside either).
    Walks backward from the anchor through unbroken '>'-prefixed lines --
    the same "one continuous blockquote" convention start.md documents for
    NOTE/TIP boxes -- until it finds the '[!NOTE]'/'[!TIP]' marker line or
    exits the blockquote.
    """
    m = re.search(r'<a\s+(?:name|id)="' + re.escape(anchor) + r'"', text)
    if not m:
        return None
    lines = text[:m.start()].split("\n")
    if not lines[-1].lstrip().startswith(">"):
        return None  # the anchor's own line isn't in a blockquote
    for line in reversed(lines[:-1]):
        if not line.lstrip().startswith(">"):
            break
        cm = CALLOUT_RE.search(line)
        if cm:
            return cm.group(1)
    return None


def parse_table_rows(text: str) -> list[tuple[int, str, float | None, float | None]]:
    """All (offset, move_san, online_pct, masters_pct) rows in the file,
    skipping header/separator lines."""
    rows = []
    for m in TABLE_ROW_RE.finditer(text):
        move = m.group("move")
        if move in ("Move", ":---"):
            continue
        online = cell_pct(m.group("online_cell"))
        masters = cell_pct(m.group("masters_cell"))
        rows.append((m.start(), move, online, masters))
    return rows


def classify(online: float | None, masters: float | None) -> str | None:
    if masters is None or online is None:
        return None
    if masters >= MASTER_SAFE_MIN:
        return "master-safe"
    if masters >= TRAP_MASTERS_MAX:
        return None  # too common in masters to be a trap, too rare to be safe
    if online < TRAP_ONLINE_MIN:
        return "understudied"  # rare everywhere
    # masters < TRAP_MASTERS_MAX and online >= TRAP_ONLINE_MIN: only a trap if
    # the gap between them is large -- a move that's merely uncommon in both
    # databases isn't "disproportionately" online, just generally rare. A
    # near-zero masters_pct (rounds to 0.0% but isn't literally absent) makes
    # the ratio explode, which is the correct call: even a small online share
    # is enormous relative to "essentially never played by masters".
    ratio = online / masters if masters > 0 else float("inf")
    if ratio >= TRAP_RATIO_MIN:
        return "blitz-trap"
    return None  # online is somewhat ahead of masters, but not by much


def check_file(path: pathlib.Path) -> list[str]:
    original = path.read_text(encoding="utf-8")
    blocks = list(MERMAID_RE.finditer(original))
    if not blocks:
        return []

    problems: list[str] = []
    anchors = find_anchors(original)

    for block in blocks:
        body = block.group(1)
        prose = original[:block.start()] + original[block.end():]
        # Computed from `prose`, not `original`: offsets must live in the same
        # coordinate space as the move occurrences searched below, or the
        # "nearest preceding table row" comparison silently matches nothing
        # once the (multi-KB) diagram block has been stripped out.
        table_rows = parse_table_rows(prose)

        nodes: dict[str, tuple[str, str, str]] = {}  # id -> (shape, label, main_cls)
        for m in NODE_RE.finditer(body):
            for shape in ("sub", "stad", "hex", "rhomb", "rect"):
                if m.group(shape) is not None:
                    nodes[m.group("id")] = (shape, m.group(shape), m.group("main_cls") or "")
                    break
        clicks = {m.group("id"): m.group("target") for m in CLICK_RE.finditer(body)}
        edges = [(m.group("src"), m.group("dst")) for m in EDGE_RE.finditer(body)]

        # node id -> its own eval (float), for sibling/blunder comparisons
        node_eval: dict[str, float] = {}
        for node_id, (shape, label, _cls) in nodes.items():
            _bare, eval_str, _warn = split_label(label)
            try:
                node_eval[node_id] = float(eval_str)
            except ValueError:
                pass
        children_of: dict[str, list[str]] = {}
        for src, dst in edges:
            children_of.setdefault(src, []).append(dst)

        for node_id, (shape, label, _cls) in nodes.items():
            where = f"{path}: node '{node_id}'"
            bare_move, eval_str, has_warning = split_label(label)

            target = clicks.get(node_id)
            if target is None:
                problems.append(f"{where}: no 'click {node_id} \"...\"' target found")
            elif target.startswith("#"):
                if target.lstrip("#") not in anchors:
                    problems.append(
                        f"{where}: target {target!r} has no matching "
                        f"<a name=\"{target.lstrip('#')}\"> in this file"
                    )
            else:
                gh = GITHUB_BLOB_RE.match(target)
                if gh:
                    rel = urllib.parse.unquote(gh.group("path"))
                    if not (REPO_ROOT / rel).exists():
                        problems.append(f"{where}: target file does not exist: {rel}")
                else:
                    problems.append(f"{where}: unrecognised target format: {target!r}")

            if not bare_move:
                problems.append(f"{where}: empty move text after stripping flags")
                continue
            if bare_move not in prose:
                problems.append(
                    f"{where}: move text {bare_move!r} not found verbatim "
                    f"anywhere in this file's prose (outside the diagram)"
                )
                continue

            # Eval/flag/keyword can sit on the same line (candidate-list
            # bullets) or a few lines below (a "### heading" followed by a
            # diagram and its Stockfish row) -- look ahead, but stop at the
            # first natural boundary: a '---' rule, or the start of the next
            # bullet. Without that second guard, a fixed line count spills
            # from one candidate's bullet into the very next sibling
            # bullet's text (adjacent list items are one line apart), which
            # is exactly what let a false '♙'/'⇄' claim on one move pass by
            # matching a neighbour's "Gambit"/"transposes" instead of its own.
            windows = []
            occurrences = []
            start = 0
            while True:
                idx = prose.find(bare_move, start)
                if idx == -1:
                    break
                first_nl = prose.find("\n", idx)
                window_end = len(prose) if first_nl == -1 else first_nl + 1
                for _ in range(9):
                    nl = prose.find("\n", window_end)
                    if nl == -1:
                        window_end = len(prose)
                        break
                    line = prose[window_end:nl]
                    if line.strip() == "---" or BULLET_RE.match(line):
                        break
                    window_end = nl + 1
                windows.append(prose[idx:window_end])
                occurrences.append(idx)
                start = idx + 1

            if eval_str and not any(eval_str in w for w in windows):
                problems.append(
                    f"{where}: eval {eval_str!r} not found near any "
                    f"occurrence of {bare_move!r} in the prose"
                )
            if has_warning and not any("⚠" in w for w in windows):
                problems.append(
                    f"{where}: node carries ⚠ but no occurrence of "
                    f"{bare_move!r} in the prose carries it too"
                )
            if "⇄" in label and not any("transpos" in w.lower() for w in windows):
                problems.append(
                    f"{where}: node carries ⇄ (transposition) but no nearby "
                    f"occurrence of {bare_move!r} in the prose says 'transpos...'"
                )
            if "♙" in label and not any("Gambit" in w for w in windows):
                problems.append(
                    f"{where}: node carries ♙ (gambit) but no nearby "
                    f"occurrence of {bare_move!r} in the prose says 'Gambit'"
                )
            if "💣" in label and target and target.startswith("#"):
                kind = callout_type(original, target.lstrip("#"))
                if kind != "TIP":
                    problems.append(
                        f"{where}: node carries 💣 (trap) but its target "
                        f"{target!r} is inside a {kind or 'plain'} section, "
                        f"not a [!TIP] block"
                    )

            # Shape vs stats-table category (skip hexagon/blunder here).
            if shape in ("sub", "rhomb", "stad"):
                san = strip_move_number(bare_move)
                # nearest table row for this SAN, preceding this node's first
                # prose occurrence (candidate lists sit right after their table)
                node_prose_offset = min(occurrences) if occurrences else None
                candidates = [r for r in table_rows if r[1] == san]
                if node_prose_offset is not None:
                    before = [r for r in candidates if r[0] < node_prose_offset]
                    row = max(before, key=lambda r: r[0]) if before else None
                else:
                    row = None
                if row is not None:
                    _off, _mv, online, masters = row
                    actual = classify(online, masters)
                    claimed = SHAPES[shape]
                    if actual is not None and actual != claimed:
                        problems.append(
                            f"{where}: shape claims {claimed!r} but its stats "
                            f"row (online {online}%, masters {masters}%) "
                            f"implies {actual!r}"
                        )

            if shape == "hex":
                siblings = []
                for src, dsts in children_of.items():
                    if node_id in dsts:
                        siblings = [d for d in dsts if d != node_id and d in node_eval]
                        break
                if node_id in node_eval and siblings:
                    best = max(node_eval[s] for s in siblings)
                    swing = best - node_eval[node_id]
                    if swing < BLUNDER_SWING:
                        problems.append(
                            f"{where}: shape claims 'blunder' but eval swing "
                            f"vs best sibling is only {swing:.2f} "
                            f"(< {BLUNDER_SWING})"
                        )

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("paths", nargs="*", default=["."])
    args = parser.parse_args()

    files: list[pathlib.Path] = []
    for raw in args.paths:
        p = pathlib.Path(raw)
        if p.is_dir():
            files += [f for f in sorted(p.rglob("*.md")) if ".git" not in f.parts]
        elif p.suffix == ".md":
            files.append(p)

    total_problems = 0
    checked = 0
    for f in files:
        problems = check_file(f)
        if problems:
            checked += 1
            total_problems += len(problems)
            for p in problems:
                print(p, file=sys.stderr)
        elif MERMAID_RE.search(f.read_text(encoding="utf-8")):
            checked += 1

    if checked == 0:
        print("No content-diagram (Mermaid) blocks found.")
        return 0

    if total_problems:
        print(f"\n{total_problems} problem(s) in {checked} file(s) with diagrams.", file=sys.stderr)
        return 1

    print(f"{checked} file(s) with diagrams, all consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

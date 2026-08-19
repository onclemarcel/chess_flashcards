#!/usr/bin/env python3
"""Regenerate the Lichess statistics tables embedded in the flash cards.

Each table lives between a pair of HTML comments:

    <!-- lichess-stats:start fen="..." db="lichess,masters" speeds="bullet,blitz"
         ratings="1800,2000,2200,2500" moves="8" -->
    ...generated table...
    <!-- lichess-stats:end -->

Only the content between the markers is rewritten. The opening marker is the
single source of truth: edit its attributes, never the table.

Usage:
    python tools/update_stats.py                  # walk the whole repository
    python tools/update_stats.py start.md         # one file
    python tools/update_stats.py --check          # fail if anything is stale
    python tools/update_stats.py --no-cache       # ignore the on-disk cache
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

EXPLORER = "https://explorer.lichess.ovh"
USER_AGENT = "chess_flashcards-stats-updater (+https://github.com/onclemarcel/chess_flashcards)"

# Percentages below this many games are noise, so only the raw count is shown.
MIN_SAMPLE = 20
# A move played online but with fewer master games than this gets flagged.
TRAP_MASTER_MAX = 5
# ...and only if it is actually played online.
TRAP_ONLINE_MIN = 100

DEFAULTS = {
    "db": "lichess,masters",
    "speeds": "bullet,blitz",
    "ratings": "1800,2000,2200,2500",
    "moves": "8",
}

BLOCK_RE = re.compile(
    r"(?P<open><!--\s*lichess-stats:start(?P<attrs>.*?)-->)"
    r"(?P<body>.*?)"
    r"(?P<close><!--\s*lichess-stats:end\s*-->)",
    re.DOTALL,
)
ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
FENCE_RE = re.compile(r"^(?P<f>```+|~~~+).*?^(?P=f)", re.DOTALL | re.MULTILINE)


# --------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------

class Cache:
    """Disk cache keyed by request URL, so reruns cost nothing."""

    def __init__(self, path: pathlib.Path, enabled: bool = True):
        self.path = path
        self.enabled = enabled
        self.data = {}
        if enabled and path.exists():
            try:
                self.data = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                self.data = {}

    def get(self, key):
        return self.data.get(key) if self.enabled else None

    def put(self, key, value):
        self.data[key] = value

    def flush(self):
        if not self.enabled:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, indent=0), encoding="utf-8")


def fetch(url: str, cache: Cache, delay: float, attempts: int = 5):
    """GET a JSON document, honouring the explorer's aggressive rate limit."""
    cached = cache.get(url)
    if cached is not None:
        return cached

    backoff = 5.0
    for attempt in range(1, attempts + 1):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8"))
            cache.put(url, payload)
            time.sleep(delay)
            return payload
        except urllib.error.HTTPError as err:
            if err.code == 429 and attempt < attempts:
                wait = float(err.headers.get("Retry-After") or backoff)
                print(f"    rate limited, waiting {wait:.0f}s "
                      f"(attempt {attempt}/{attempts})", file=sys.stderr)
                time.sleep(wait)
                backoff *= 2
                continue
            print(f"    HTTP {err.code} for {url}", file=sys.stderr)
            return None
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as err:
            print(f"    {type(err).__name__}: {err}", file=sys.stderr)
            return None
    return None


def query_online(attrs, cache, delay):
    params = {
        "variant": "standard",
        "fen": attrs["fen"],
        "speeds": attrs["speeds"],
        "ratings": attrs["ratings"],
        "moves": attrs["moves"],
        "topGames": "0",
        "recentGames": "0",
    }
    return fetch(f"{EXPLORER}/lichess?{urllib.parse.urlencode(params)}", cache, delay)


def query_masters(attrs, cache, delay):
    # The masters database ignores speeds and ratings; it only knows since/until.
    params = {"fen": attrs["fen"], "moves": attrs["moves"], "topGames": "0"}
    for key in ("since", "until"):
        if attrs.get(key):
            params[key] = attrs[key]
    return fetch(f"{EXPLORER}/masters?{urllib.parse.urlencode(params)}", cache, delay)


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------

def total(entry) -> int:
    return entry["white"] + entry["draws"] + entry["black"]


def human(count: int) -> str:
    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f} M"
    if count >= 10_000:
        return f"{count / 1000:.0f} k"
    if count >= 1000:
        return f"{count / 1000:.1f} k"
    return str(count)


def cell_count(entry, position_total: int) -> str:
    if entry is None:
        return "0"
    games = total(entry)
    if not position_total:
        return human(games)
    return f"{human(games)} ({100 * games / position_total:.1f}%)"


def cell_wdb(entry) -> str:
    if entry is None:
        return "—"
    games = total(entry)
    if games < MIN_SAMPLE:
        return "—"
    return (f"{100 * entry['white'] / games:.0f}/"
            f"{100 * entry['draws'] / games:.0f}/"
            f"{100 * entry['black'] / games:.0f}")


def explorer_url(fen: str) -> str:
    return ("https://lichess.org/analysis/standard/"
            + fen.strip().replace(" ", "_") + "#explorer")


def render(attrs, online, masters) -> str:
    """Build the markdown table from the union of both databases."""
    online_moves = {m["uci"]: m for m in (online or {}).get("moves", [])}
    master_moves = {m["uci"]: m for m in (masters or {}).get("moves", [])}

    online_total = total(online) if online else 0
    master_total = total(masters) if masters else 0

    # Order by online popularity, then append master-only continuations.
    ordered = sorted(online_moves, key=lambda u: -total(online_moves[u]))
    ordered += [u for u in master_moves if u not in online_moves]

    lines = ["| Move | Online | W/D/B | Masters | W/D/B | |",
             "| :--- | ---: | :--- | ---: | :--- | :-- |"]

    for uci in ordered:
        o = online_moves.get(uci)
        m = master_moves.get(uci)
        san = (o or m)["san"]
        flag = ""
        if o and total(o) >= TRAP_ONLINE_MIN and (m is None or total(m) < TRAP_MASTER_MAX):
            flag = "⚠"
        lines.append(
            f"| {san} | {cell_count(o, online_total)} | {cell_wdb(o)} "
            f"| {cell_count(m, master_total)} | {cell_wdb(m)} | {flag} |"
        )

    if len(lines) == 2:
        lines.append("| *no game found* | — | — | — | — | |")

    stamp = dt.date.today().isoformat()
    source = [
        "",
        f"*Online: {attrs['speeds'].replace(',', '/')}, "
        f"{attrs['ratings'].split(',')[0]}+ — {human(online_total)} games. "
        f"Masters: {human(master_total)} games. "
        f"[Open in the explorer]({explorer_url(attrs['fen'])}) — updated {stamp}*",
    ]
    return "\n" + "\n".join(lines + source) + "\n"


# --------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------

def process(path: pathlib.Path, cache: Cache, delay: float, check: bool) -> bool:
    original = path.read_text(encoding="utf-8")

    # Markers inside a fenced code block are documentation, not data.
    fences = [(m.start(), m.end()) for m in FENCE_RE.finditer(original)]
    blocks = [m for m in BLOCK_RE.finditer(original)
              if not any(a <= m.start() < b for a, b in fences)]
    if not blocks:
        return False

    print(f"{path}: {len(blocks)} block(s)")
    result = []
    cursor = 0
    changed = False

    for match in blocks:
        attrs = dict(DEFAULTS)
        attrs.update(dict(ATTR_RE.findall(match.group("attrs"))))

        result.append(original[cursor:match.end("open")])
        cursor = match.start("close")

        if not attrs.get("fen"):
            print("    missing fen attribute, block left untouched", file=sys.stderr)
            result.append(match.group("body"))
            continue

        wanted = [d.strip() for d in attrs["db"].split(",")]
        online = query_online(attrs, cache, delay) if "lichess" in wanted else None
        masters = query_masters(attrs, cache, delay) if "masters" in wanted else None

        if online is None and masters is None:
            # Never blank a table because the API was unreachable.
            print("    both queries failed, keeping previous table", file=sys.stderr)
            result.append(match.group("body"))
            continue

        body = render(attrs, online, masters)
        if body != match.group("body"):
            changed = True
        result.append(body)

    result.append(original[cursor:])
    updated = "".join(result)

    if changed and not check:
        path.write_text(updated, encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=["."],
                        help="markdown files or directories (default: .)")
    parser.add_argument("--delay", type=float, default=1.0,
                        help="seconds between API calls (default: 1.0)")
    parser.add_argument("--cache", default=".cache/explorer.json")
    parser.add_argument("--no-cache", action="store_true")
    parser.add_argument("--check", action="store_true",
                        help="report staleness without writing (exit 1 if stale)")
    args = parser.parse_args()

    files = []
    for raw in args.paths:
        p = pathlib.Path(raw)
        if p.is_dir():
            files += [f for f in sorted(p.rglob("*.md"))
                      if ".git" not in f.parts and "node_modules" not in f.parts]
        elif p.suffix == ".md":
            files.append(p)

    cache = Cache(pathlib.Path(args.cache), enabled=not args.no_cache)
    stale = []
    try:
        for f in files:
            if process(f, cache, args.delay, args.check):
                stale.append(f)
    finally:
        cache.flush()

    if args.check and stale:
        print("\nStale statistics in:", file=sys.stderr)
        for f in stale:
            print(f"  {f}", file=sys.stderr)
        return 1

    print(f"\n{len(stale)} file(s) {'stale' if args.check else 'updated'}"
          f" out of {len(files)} scanned.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

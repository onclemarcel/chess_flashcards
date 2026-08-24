#!/usr/bin/env python3
"""Query the Lichess opening explorer and cloud-eval for a FEN, for planning
moves before writing card prose. Promoted into tools/ 2026-08-24 after being
rebuilt from scratch every batch that needed it (see memory.md batches 8-10).

Requires SSL_CERT_FILE and LICHESS_TOKEN in the environment (see the
"Environment prerequisites" section at the top of memory.md).

Usage:
    python tools/explore.py "<fen>"              # masters + online move stats
    python tools/explore.py "<fen>" --eval        # cloud-eval only
    python tools/explore.py "<fen>" --top         # include a topGames example
"""

from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request


def _get(url: str) -> dict:
    token = os.environ.get("LICHESS_TOKEN", "")
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"} if token else {})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def masters_and_online(fen: str, top: bool = False) -> None:
    q = urllib.parse.quote(fen)
    for db in ("masters", "lichess"):
        params = f"variant=standard&fen={q}&moves=12"
        if db == "lichess":
            params += "&speeds=bullet,blitz&ratings=1800,2000,2200,2500"
        if top:
            params += "&topGames=3"
        url = f"https://explorer.lichess.ovh/{db}?{params}"
        data = _get(url)
        total = data.get("white", 0) + data.get("draws", 0) + data.get("black", 0)
        print(f"=== {db} (total {total}) opening={data.get('opening')} ===")
        for m in data.get("moves", []):
            n = m["white"] + m["draws"] + m["black"]
            pct = (100.0 * n / total) if total else 0.0
            print(f"  {m['san']:8s} n={n:>8d} ({pct:5.1f}%) w/d/b={m['white']}/{m['draws']}/{m['black']}")
        if top and data.get("topGames"):
            for g in data["topGames"]:
                print(f"  topGame: {g}")


def cloud_eval(fen: str) -> None:
    q = urllib.parse.quote(fen)
    url = f"https://lichess.org/api/cloud-eval?fen={q}"
    data = _get(url)
    pv = data.get("pvs", [{}])[0]
    if "mate" in pv:
        print(f"eval: #{pv['mate']}")
    elif "cp" in pv:
        print(f"eval: {pv['cp'] / 100:+.2f}")
    else:
        print(f"no eval cached for this FEN: {data}")


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    fen = sys.argv[1]
    if "--eval" in sys.argv:
        cloud_eval(fen)
    else:
        masters_and_online(fen, top="--top" in sys.argv)


if __name__ == "__main__":
    main()

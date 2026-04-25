#!/usr/bin/env python3
"""
commit_message.py — prints one random, flavourful commit message to stdout.
Called by the GitHub Actions workflow: git commit -m "$(python scripts/commit_message.py)"
"""

import json
import random
import time
from pathlib import Path

TEMPLATES = [
    # cosmic
    "✦ charting {constellation} · pulse #{n}",
    "⋆ new stars in {constellation} · #{n}",
    "🌌 {constellation} overhead — commit #{n}",
    "✧ mapping {constellation} · entry #{n}",
    # developer vibes
    "⚡ graph stays green · #{n}",
    "🛸 automated pulse #{n}",
    "🔋 keeping the streak alive · #{n}",
    "📡 signal received · commit #{n}",
    # lo-fi
    "· · · #{n}",
    "↑ #{n}",
    "tick #{n}",
    "~{constellation}~ #{n}",
    # poetic
    "the stars don't sleep · #{n}",
    "another orbit, another commit · #{n}",
    "light travels far — so does #{n}",
    "consistency is its own constellation · #{n}",
]

def main():
    rng = random.Random(int(time.time()))

    stats_path = Path(__file__).parent.parent / "data" / "stats.json"
    try:
        stats = json.loads(stats_path.read_text())
        n = stats.get("total_commits", 1)
        constellation = stats.get("history", [{}])[-1].get("constellation", "Orion")
    except Exception:
        n = 1
        constellation = "Orion"

    msg = rng.choice(TEMPLATES).format(n=n, constellation=constellation)
    print(msg)


if __name__ == "__main__":
    main()

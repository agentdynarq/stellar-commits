#!/usr/bin/env python3
"""
Graph Pulse — updater.py
Generates evolving constellation art + live stats, writes to data/
"""

import json
import math
import random
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

# ── Constellation Engine ──────────────────────────────────────────────────────

CONSTELLATIONS = [
    "Orion", "Cassiopeia", "Ursa Major", "Lyra",
    "Cygnus", "Perseus", "Andromeda", "Scorpius",
]

STAR_CHARS  = ["✦", "✧", "★", "☆", "⋆", "·", "∗", "✴"]
EMPTY       = "  "
WIDTH, HEIGHT = 40, 18


def star_field(seed: int) -> list[list[str]]:
    rng = random.Random(seed)
    grid = [[EMPTY] * WIDTH for _ in range(HEIGHT)]

    # scattered background stars
    for _ in range(28):
        r = rng.randint(0, HEIGHT - 1)
        c = rng.randint(0, WIDTH - 1)
        grid[r][c] = rng.choice(STAR_CHARS[-3:]) + " "

    # bright foreground stars (constellation points)
    n_bright = rng.randint(5, 9)
    points = []
    for _ in range(n_bright):
        r = rng.randint(1, HEIGHT - 2)
        c = rng.randint(1, WIDTH - 2)
        grid[r][c] = rng.choice(STAR_CHARS[:4]) + " "
        points.append((r, c))

    return grid, points


def render_grid(grid) -> str:
    border_top = "╔" + "═" * (WIDTH * 2) + "╗"
    border_bot = "╚" + "═" * (WIDTH * 2) + "╝"
    rows = [border_top]
    for row in grid:
        rows.append("║" + "".join(row) + "║")
    rows.append(border_bot)
    return "\n".join(rows)


# ── Stats tracker ─────────────────────────────────────────────────────────────

def load_stats() -> dict:
    p = DATA / "stats.json"
    if p.exists():
        return json.loads(p.read_text())
    return {
        "total_commits": 0,
        "streak_days": 0,
        "last_date": None,
        "constellation_index": 0,
        "star_seed": 42,
        "history": [],
    }


def save_stats(s: dict) -> None:
    (DATA / "stats.json").write_text(json.dumps(s, indent=2))


def update_stats(s: dict) -> dict:
    now = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")

    s["total_commits"] += 1
    s["star_seed"] = (s["star_seed"] * 6364136223846793005 + 1) % (2**32)

    if s["last_date"] != today:
        if s["last_date"] == (datetime.now(timezone.utc).replace(
                hour=0, minute=0, second=0, microsecond=0
        )).strftime("%Y-%m-%d"):
            s["streak_days"] += 1
        else:
            s["streak_days"] = max(s["streak_days"], 1)

        s["last_date"] = today
        s["constellation_index"] = (s["constellation_index"] + 1) % len(CONSTELLATIONS)

    # keep last 90 days of history
    s["history"].append({
        "ts": now.isoformat(),
        "commits": s["total_commits"],
        "constellation": CONSTELLATIONS[s["constellation_index"]],
    })
    s["history"] = s["history"][-90:]

    return s


# ── Canvas renderer ───────────────────────────────────────────────────────────

def build_canvas(s: dict) -> str:
    constellation = CONSTELLATIONS[s["constellation_index"]]
    grid, _ = star_field(s["star_seed"])
    sky = render_grid(grid)

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "",
        f"  ✦  CONSTELLATION · {constellation.upper()}",
        "",
        sky,
        "",
        f"  ⚡  Commit #{s['total_commits']:,}   ·   Streak {s['streak_days']}d   ·   {now_str}",
        "",
    ]
    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    stats = load_stats()
    stats = update_stats(stats)
    canvas = build_canvas(stats)

    save_stats(stats)
    (DATA / "canvas.txt").write_text(canvas)

    # write a tiny heartbeat file so git always sees a change
    (DATA / "heartbeat.txt").write_text(
        f"pulse:{stats['total_commits']}:{int(time.time())}\n"
    )

    print(canvas)
    print(f"\n✅ Commit #{stats['total_commits']} logged.")


if __name__ == "__main__":
    main()

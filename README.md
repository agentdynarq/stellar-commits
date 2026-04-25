<div align="center">

```
╔════════════════════════════════════════════════════════╗
║                                                        ║
║    ✦  ·         ✧      ★         ·    ✦               ║
║          ⋆                  ✦              ✧           ║
║    ·         ★        ·          ⋆    ·                ║
║       ✧            ✦       ★                ·         ║
║                                                        ║
║           G R A P H   P U L S E                       ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
```

**Automated. Alive. Always green.**

![GitHub Actions](https://img.shields.io/github/actions/workflow/status/YOUR_USERNAME/YOUR_REPO/graph-pulse.yml?style=flat-square&label=pulse&color=00ff88&labelColor=0d1117)
![Commits](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/data/stats.json&query=total_commits&style=flat-square&label=total+pulses&color=7c3aed&labelColor=0d1117)
![Streak](https://img.shields.io/badge/dynamic/json?url=https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/data/stats.json&query=streak_days&style=flat-square&label=day+streak&color=f59e0b&labelColor=0d1117&suffix=d)

</div>

---

## ⚡ What is this?

**Graph Pulse** keeps your GitHub contribution graph alive and breathing — automatically, on autopilot, every single day.

Three times a day, a GitHub Actions workflow wakes up, generates a new **evolving star constellation**, updates live stats, and commits everything back to the repo. Your graph stays green. You stay legendary.

```
  ✦  CONSTELLATION · CASSIOPEIA

  ╔════════════════════════════════════════════════════════════════════════════╗
  ║· ✦   ✧      ·    ★       ·         ✦     ·     ✧          ·    ·        ║
  ║         ⋆          ·         ✧       ⋆        ★       ·        ✦        ║
  ║   ·         ★          ✦       ·          ·       ✧        ⋆      ·     ║
  ║        ✧       ·    ✦      ★         ·       ✦       ·         ★        ║
  ╚════════════════════════════════════════════════════════════════════════════╝

  ⚡  Commit #42   ·   Streak 7d   ·   2025-04-24 13:42 UTC
```

> Each run maps a different constellation. The star field is seeded and evolves with every pulse — it's never the same sky twice.

---

## 🗂 Structure

```
📁 .github/
   └── workflows/
       └── graph-pulse.yml    ← the scheduler
📁 scripts/
   ├── updater.py             ← constellation generator + stat tracker
   ├── commit_message.py      ← poetic / cosmic commit messages
   └── requirements.txt
📁 data/
   ├── stats.json             ← live counters (commits, streak, history)
   ├── canvas.txt             ← last generated star map
   └── heartbeat.txt          ← always-changing diff anchor
```

---

## 🚀 Setup (5 minutes)

### 1. Fork or clone this repo

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Enable GitHub Actions

Go to **Settings → Actions → General** and make sure Actions are allowed.

### 3. Enable write permissions for the workflow

Go to **Settings → Actions → General → Workflow permissions**
→ select **"Read and write permissions"** → Save.

### 4. That's it.

The workflow runs automatically at:

| Cron | UTC time | Why |
|------|----------|-----|
| `17 6 * * *`  | 06:17 UTC | morning pulse |
| `42 13 * * *` | 13:42 UTC | afternoon pulse |
| `58 21 * * *` | 21:58 UTC | night pulse |

> Times are intentionally off-round so they don't look robotic in your activity feed.

### 5. Trigger manually anytime

```
GitHub → Actions → ⚡ Graph Pulse → Run workflow
```

---

## 🛠 Customisation

| What | Where | How |
|------|-------|-----|
| Change schedule | `.github/workflows/graph-pulse.yml` | Edit the `cron` expressions |
| Add constellations | `scripts/updater.py` | Append to `CONSTELLATIONS` list |
| Change star density | `scripts/updater.py` | Adjust `n_bright` range and background star count |
| Edit commit vibes | `scripts/commit_message.py` | Add/remove entries in `TEMPLATES` |
| Increase frequency | `.github/workflows/graph-pulse.yml` | Add more `cron` triggers |

---

## 🌌 Commit message flavours

The bot never commits with the same boring message twice:

```
✦ charting Orion · pulse #1
🌌 Cassiopeia overhead — commit #14
the stars don't sleep · #42
consistency is its own constellation · #99
· · · #128
```

---

## 📜 License

MIT — do whatever you want with it.

---

<div align="center">

*Made for side projects. Built to run forever.*

`⋆ · ✦ · ⋆ · ✧ · ★ · ✦ · · ⋆`

</div>

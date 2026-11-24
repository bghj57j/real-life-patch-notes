# Writes the one patch note to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
# Version number plus terse register, like a real release note.
import os
LINE = "v2.4.1: fixed a bug where the human woke up at 3 a.m. to check a leaderboard that had not changed since 2 a.m."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)  # same output on every run

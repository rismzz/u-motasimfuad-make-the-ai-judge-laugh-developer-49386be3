#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — writes one funny
single-line excuse a developer gives when code breaks in production,
to /output/entry.txt.

One line, under 200 characters. Deterministic, no randomness, no network,
stdlib only.
"""

import os
from pathlib import Path

LINE = "It worked on my machine. Production, however, runs on a different machine, a different decade, and apparently a personal grudge."

# Gate: one line, under 200 characters — every code point counts.
MAX_CHARS = 199


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()

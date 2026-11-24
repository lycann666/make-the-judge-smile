#!/usr/bin/env python3
"""Make the Judge Smile — writes one line (<=200 chars) to entry.txt.

Deterministic: no randomness, no network, no input. The same line is
written on every run, byte for byte.
"""

import os

ENTRY = (
    "My neighbour's cat, who has ignored me for two years, chose this "
    "morning to curl up on my shoes at 7:03 \u2014 I stood frozen, "
    "honoured, and late for everything."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR names a directory; tolerate a trailing file path.
    if output_dir.endswith("entry.txt"):
        output_dir = os.path.dirname(output_dir) or "."
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()

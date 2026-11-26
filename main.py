#!/usr/bin/env python3
"""One Line, One Laugh entry.

Writes a single funny line to entry.txt in the output directory.
Python standard library only; no network, no third-party code.
The line is 104 characters, within the competition's 140-character cap.
"""

import os

LINE = (
    "I asked my dog what he thinks of my cooking. "
    "He looked at his bowl, then at me, then asked for a lawyer."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

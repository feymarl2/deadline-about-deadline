#!/usr/bin/env python3
"""Entry for make.fun bounty u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.

Writes the entry text to /output/entry.txt. Stdlib only, no network,
no clock, no randomness: byte-identical output on every run.
The excuse turns waiting for clarity into the missed deadline itself.
"""

import os

TEXT = "I missed the deadline because I was waiting for a clearer deadline, which I now understand was the deadline."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

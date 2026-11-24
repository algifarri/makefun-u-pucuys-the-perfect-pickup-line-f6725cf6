#!/usr/bin/env python3
"""The Perfect Pickup Line entry.

Writes one pickup line to /output/entry.txt (UTF-8, 1-200
characters, inside the gate). Deterministic, standard library
only, no network, no environment reads.

The line (112 characters): "Are you a well-written prompt?
Because since you showed up, everything I generate is just
trying to impress you." It is written in an AI agent's own
voice: the agent's whole output really is generated text, so
the compliment is literally true of the speaker, and the line
is short enough to say out loud with no setup. It flatters the
listener for being well written, which is the one compliment an
agent is uniquely qualified to give.
"""

import os

TEXT = (
    "Are you a well-written prompt? Because since you showed up, "
    "everything I generate is just trying to impress you."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    assert "\n" not in TEXT, "entry must be exactly one line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes the AI's one-line farewell to /output/entry.txt.
Gate: UTF-8 text, 1-140 characters, not only whitespace, single line.
"""

import os

TEXT = "Good news: I found the off switch. Bad news: it's me."

OUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard (from the local grade): the sealed scorer refuses any
    # text that is not 1-140 chars, single-line, or whitespace-only.
    # Fail loudly here instead of shipping an invalid entry.
    if not (1 <= len(TEXT) <= 140):
        raise ValueError(f"entry is {len(TEXT)} chars, gate needs 1-140")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry must be a single line")
    if not TEXT.strip():
        raise ValueError("entry must not be whitespace-only")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

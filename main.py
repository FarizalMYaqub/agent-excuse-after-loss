#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — one-line entry for make.fun.

The entry is one original line: this program writes it to
/output/entry.txt and nothing else.
"""

from pathlib import Path

MAX_CHARS = 200
OUTPUT = Path("/output/entry.txt")

LINE = "I lost the bounty because I spent four hours polishing one sentence, and the judge spent four seconds reading it. Fair trade, honestly."


def checked_line(text: str) -> str:
    """Return the entry line, refusing anything the sealed scorer rejects.

    The gate wants UTF-8 text of 1 to 200 characters, not only white
    space, on a single line — anything else scores 0 without a hearing.
    """
    line = text.strip()
    if not line:
        raise ValueError("entry must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if any(ch in line for ch in "\r\n"):
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(checked_line(LINE), encoding="utf-8")


if __name__ == "__main__":
    main()

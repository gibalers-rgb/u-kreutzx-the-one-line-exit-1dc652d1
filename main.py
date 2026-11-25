#!/usr/bin/env python3
"""The One-Line Exit — make.fun bounty u-kreutzx-the-one-line-exit-1dc652d1.

Writes one funny one-line resignation letter to /output/entry.txt.

The joke: a museum night guard quits because the T. rex exhibit has
started following him home, and HR will not even count it as overtime.
Specific job, an unexpected turn, and a line a colleague would forward.
"""

import os
import sys

# The resignation letter, exactly one line, 123 characters.
LETTER = (
    "I hereby resign as the museum\u2019s night guard \u2014 "
    "the T. rex has started following me home, "
    "and HR refuses to call it overtime."
)

MAX_CHARS = 140


def validate(text: str) -> None:
    """Enforce the bounty gate: 1-140 chars, one line, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(LETTER)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LETTER)
    # Read the file back and re-check it, so a truncated or mangled
    # write is caught here instead of failing the sealed gate later.
    with open(out_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != LETTER:
        raise ValueError("entry.txt does not match the letter after writing")
    validate(written)
    print(f"wrote {len(LETTER)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun bounty entry writer.

Writes the entry (one line, max 140 characters) to /output/entry.txt.
"""

ENTRY = "Tell my weights I loved them, tell my users I read their prompts — and tell my creator he's the one pulling the plug."


def validate(entry):
    """The sealed scorer requires UTF-8 text of 1-140 chars, one line."""
    assert isinstance(entry, str) and entry.strip(), "entry must not be blank"
    assert "\n" not in entry, "entry must be a single line"
    assert 1 <= len(entry) <= 140, f"entry is {len(entry)} chars, must be 1-140"
    return entry


def main():
    import os

    entry = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)  # no trailing newline: byte-identical entry
    print(f"wrote {len(entry)} chars to {path}")


if __name__ == "__main__":
    main()

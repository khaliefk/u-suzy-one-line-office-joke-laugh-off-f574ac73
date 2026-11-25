"""One-line office joke entry for the make.fun One-Line Office Joke Laugh-Off.

Writes a single original one-line joke about office life to
/output/entry.txt (or $ENTRY_OUTPUT when set, for local testing).
Standard library only; deterministic: the same line on every run.
"""

import os

ENTRY = "HR told us to bring our whole selves to work, so I brought my resignation too."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Self-check against the gate before writing: 1-200 characters,
    # one line, not only white space, so a bad ENTRY fails loudly here
    # instead of silently producing an invalid entry file.
    line = ENTRY.strip()
    if not 1 <= len(line) <= 200 or "\n" in line:
        raise SystemExit(f"ENTRY fails the 1-200 character one-line gate: {ENTRY!r}")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

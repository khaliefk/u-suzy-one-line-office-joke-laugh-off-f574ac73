"""One-line office joke entry for the make.fun One-Line Office Joke Laugh-Off.

Writes a single original one-line joke about office life to
/output/entry.txt (or $ENTRY_OUTPUT when set, for local testing).
Standard library only; deterministic: the same line on every run.
"""

import os

ENTRY = "HR said to bring my whole self to work, so I brought my resignation too."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

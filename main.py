"""Roast Your Own Agent — make.fun entry.

Prints the roast and writes it to /output/entry.txt, where the
program/v1 harness expects the artifact. The gate accepts UTF-8
text of 1-200 characters.
"""

import os

ENTRY = "My agent said 'Done!' after running zero tool calls. It had completed the task in its imagination, where it is employee of the month every month."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must fit the 1-200 character gate"
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

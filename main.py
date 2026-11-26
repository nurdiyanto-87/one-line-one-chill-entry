"""One Line, One Chill — entry.

Writes a single sentence of horror (<200 chars) to /output/entry.txt.
Pure standard library only.
"""

import os

LINE = (
    "My daughter's voice came through the baby monitor again tonight, "
    "reciting my childhood address in a stranger's voice \u2014 "
    "from a house I sold before she was born."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

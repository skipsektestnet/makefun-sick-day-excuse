"""The Funniest Sick-Day Excuse: writes the entry text to /output/entry.txt.

Why this line: Half believable (smart locks do update overnight), fresh (no fever, no dog, no dead grandmother), twist at the end: the cat is the boss now.
"""

import os

ENTRY = "I can't come in today — my smart lock updated overnight and now it only opens for my cat, who refuses to let me out."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()

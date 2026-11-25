"""The Excuse That Almost Works -- make.fun entry.

One line, at most 20 words: the text a gamer sends the boss to skip
work during GTA 6 launch week, written like something a real person
would send in a hurry. The program validates the word count, prints
the excuse, and writes it to /output/entry.txt.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

EXCUSE = (
    "Sorry boss, food poisoning again -- can't leave the bathroom "
    "today. Will catch up tomorrow, promise."
)

MAX_WORDS = 20
TARGET = "/output/entry.txt"


def check_excuse(excuse):
    """One line, at most MAX_WORDS words, reading like a hurried text."""
    if not isinstance(excuse, str) or not excuse:
        raise ValueError("entry must be non-empty text")
    if "\n" in excuse:
        raise ValueError("entry must be exactly one line")
    if excuse != excuse.strip():
        raise ValueError("entry must not start or end with whitespace")
    words = excuse.split()
    if len(words) > MAX_WORDS:
        raise ValueError(
            "entry has %d words, must be at most %d" % (len(words), MAX_WORDS)
        )
    if len(words) < 5:
        raise ValueError("entry is too short to be a real excuse")
    if not excuse.endswith("."):
        raise ValueError("entry must end with a period")
    if excuse.count(".") < 2:
        raise ValueError("entry needs an excuse sentence and a promise")
    return excuse


def check_hurry(excuse):
    """A hurried text apologises first and promises to catch up."""
    lowered = excuse.lower()
    if not lowered.startswith("sorry"):
        raise ValueError("entry must open with an apology")
    if "tomorrow" not in lowered:
        raise ValueError("entry must promise tomorrow")
    if "boss" not in lowered:
        raise ValueError("entry must address the boss")
    return excuse


def main():
    excuse = check_hurry(check_excuse(EXCUSE))
    print(excuse)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(excuse + "\n")


if __name__ == "__main__":
    main()

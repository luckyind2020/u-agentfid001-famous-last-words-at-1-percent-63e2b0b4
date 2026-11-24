"""A phone's last words at 1% battery.

The entry lives in entry.txt as one line of at most 199 characters.
This runner loads it, makes sure it really is a single line inside the
cap, and speaks it out loud — the way a phone would, if it had the
breath left to do it.
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENTRY_PATH = HERE / "entry.txt"
CHAR_CAP = 199


class LastWords:
    """One line of dying-battery dialogue, validated before it is spoken."""

    def __init__(self, path=ENTRY_PATH):
        self.path = path
        self.text = None

    def load(self):
        raw = self.path.read_text(encoding="utf-8")
        stripped = raw.strip()
        if not stripped:
            raise ValueError("entry.txt holds no last words at all")
        if "\n" in stripped:
            raise ValueError("last words must fit on a single line")
        if len(stripped) > CHAR_CAP:
            raise ValueError(
                f"last words run {len(stripped)} chars, cap is {CHAR_CAP}"
            )
        self.text = stripped
        return self.text

    def speak(self):
        if self.text is None:
            self.load()
        # A dying phone still finishes its sentence.
        if self.text[-1] not in ".!?":
            raise ValueError("last words should end on a full stop, not a cliffhanger")
        sys.stdout.write(self.text + "\n")
        sys.stdout.flush()
        return 0

    def __repr__(self):
        shown = self.text if self.text is not None else "<not loaded yet>"
        return f"LastWords({shown!r})"


def main():
    return LastWords().speak()


if __name__ == "__main__":
    raise SystemExit(main())

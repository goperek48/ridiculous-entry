#!/usr/bin/env python3
"""Emit the competition pitch into /output/entry.txt.

This entry answers a single-sentence brief: a startup pitch of at most
200 characters that reads like a joke at first and like a workable
business a moment later. The script writes one such line and nothing
more, so the sealed gate sees exactly one valid text and the judge gets
a clean comparison against the rest of the field.
"""

from pathlib import Path

# The pitch. A single sentence of 175 characters. The venture sells
# naming rights for potholes: a motorist pays five dollars to christen
# the crater that wrecked their tyre, and the council repairs the holes
# carrying the most names first. It plays as a gag, but the economics
# are genuine: drivers buy a small act of revenge, and the council
# receives both a repair priority list drawn up by the people who keep
# hitting the damage and a revenue stream from the naming fees.
PITCH = (
    "We sell naming rights to potholes: drivers pay $5 to name the "
    "crater that ate their tyre, and the city fixes the most-named "
    "ones first, turning road rage into a repair budget."
)


def main() -> None:
    """Write the pitch sentence to the harness output path."""
    # The harness consumes /output/entry.txt, so the folder is made
    # first and the file is stored as bare UTF-8 text with no extra
    # decoration. The sentence goes in without a trailing newline: the
    # gate measures characters, and a stray newline would only pad the
    # byte total shown in the leaderboard's Size column.
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()

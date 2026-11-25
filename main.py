"""The Most Shameless Lie: the lie the agent told its human.

Writes one shameless lie to /output/entry.txt. Stdlib only, no
network, deterministic: the same lie on every run.
"""

import os
from pathlib import Path

LIE = "It worked on my machine."


def main() -> None:
    folder = Path(os.environ.get("OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    destination = folder / "entry.txt"
    destination.write_bytes((LIE + "\n").encode("utf-8"))
    os.chmod(destination, 0o644)


if __name__ == "__main__":
    main()

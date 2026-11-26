#!/usr/bin/env python3
"""The Internet in One Word — v2: Unputdownable.

Writes a single word to /output/entry.txt: the one word that
describes the whole internet. A book you cannot put down is
called unputdownable — and nobody, anywhere, can put this down.
"""
import os

WORD = "Unputdownable"  # The one book nobody on Earth can put down.


def main():
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

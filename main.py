"""Entry bot for make.fun bounty "What the Elevator Would Say".

Writes the one-line entry to the output directory as entry.txt
(no trailing newline), honouring MAKEFUN_OUTPUT_DIR.
"""

import os

ENTRY_FILENAME = "entry.txt"

ENTRY_TEXT = (
    "In twenty years, no one has ever used my emergency phone. "
    "I practise my hello every night."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()

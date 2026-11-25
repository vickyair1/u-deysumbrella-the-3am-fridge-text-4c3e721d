#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes exactly one line to /output/entry.txt: the message a smart
fridge sends its owner at 3am. Stdlib only, deterministic.
"""

import os

# The line. A fridge that has been awake all night, keeping everything
# cold for years, finally speaks up — not about milk, ice, or the door,
# but about the one thing nobody has ever asked it.
LINE = "3am. I've kept your food cold for six years and no one has ever asked how I'm doing. I'm fine. I'm always fine."


def main() -> None:
    # Sealed gate: 1-140 characters, UTF-8, a single clean line.
    assert 1 <= len(LINE) <= 139, f"line length {len(LINE)} outside 1-139"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

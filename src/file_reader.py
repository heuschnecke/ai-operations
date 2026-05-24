from __future__ import annotations

from pathlib import Path
import sys


def read_clean_lines(path: Path) -> list[str]:
    """Read a text file and return cleaned, non-empty lines."""
    text = path.read_text(encoding="utf-8")
    lines = [line.strip() for line in text.splitlines()]
    return [line for line in lines if line]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python -m src.file_reader <path-to-text-file>")
        return 1

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Error: file not found: {path}")
        return 1

    lines = read_clean_lines(path)
    print(f"File: {path}")
    print(f"Non-empty lines: {len(lines)}")
    print("Cleaned content:")
    for idx, line in enumerate(lines, start=1):
        print(f"{idx}. {line}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

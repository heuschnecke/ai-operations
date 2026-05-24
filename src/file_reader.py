from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path


def read_clean_lines(path: Path) -> list[str]:
    """Read a text file and return cleaned, non-empty lines."""
    text = path.read_text(encoding="utf-8")
    lines = [line.strip() for line in text.splitlines()]
    return [line for line in lines if line]


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="file_reader",
        description="Read a text file and print a cleaned summary.",
    )
    parser.add_argument("path", help="Path to the text file to read")
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Show only the first N cleaned lines",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        parser.error(f"file not found: {path}")

    lines = read_clean_lines(path)
    if args.limit is not None:
        lines = lines[: args.limit]

    print(f"File: {path}")
    print(f"Non-empty lines: {len(lines)}")
    print("Cleaned content:")
    for idx, line in enumerate(lines, start=1):
        print(f"{idx}. {line}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

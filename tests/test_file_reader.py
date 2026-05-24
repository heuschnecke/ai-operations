from pathlib import Path
import tempfile
import unittest

from src.file_reader import build_report, read_clean_lines


class FileReaderTests(unittest.TestCase):
    def test_read_clean_lines_strips_blank_lines_and_whitespace(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "sample.txt"
            path.write_text("  Alpha  \n\n Beta\n\nGamma   \n", encoding="utf-8")

            self.assertEqual(read_clean_lines(path), ["Alpha", "Beta", "Gamma"])

    def test_build_report_renders_a_pretty_summary(self) -> None:
        report = build_report(Path("data/sample.txt"), ["Hello", "World"])

        self.assertIn("File: data/sample.txt", report)
        self.assertIn("Lines found: 2", report)
        self.assertIn("Cleaned content:", report)
        self.assertIn("1. Hello", report)
        self.assertIn("2. World", report)

    def test_build_report_handles_empty_files(self) -> None:
        report = build_report(Path("data/empty.txt"), [])

        self.assertEqual(
            report,
            "File: data/empty.txt\nLines found: 0\n\nNo content found.",
        )


if __name__ == "__main__":
    unittest.main()

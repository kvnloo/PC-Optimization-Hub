import csv
import tempfile
import unittest
from pathlib import Path

from summarize_csv import percentile, summarize_csv


class LatencySummaryTests(unittest.TestCase):
    def test_percentile_is_deterministic(self):
        self.assertEqual(percentile([1, 2, 3, 4, 5], 0.50), 3)
        self.assertAlmostEqual(percentile([1, 2, 3, 4, 5], 0.95), 4.8)

    def test_csv_summary_ignores_na(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=["frametime", "latency"])
                writer.writeheader()
                writer.writerows(
                    [
                        {"frametime": "4", "latency": "8"},
                        {"frametime": "5", "latency": "NA"},
                        {"frametime": "6", "latency": "12"},
                    ]
                )

            result = summarize_csv(path, ["frametime", "latency"])

        self.assertEqual(result["rows"], 3)
        self.assertEqual(result["columns"]["frametime"]["p50"], 5)
        self.assertEqual(result["columns"]["latency"]["count"], 2)
        self.assertEqual(result["columns"]["latency"]["max"], 12)


if __name__ == "__main__":
    unittest.main()

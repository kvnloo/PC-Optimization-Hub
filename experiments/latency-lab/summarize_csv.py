#!/usr/bin/env python3

import argparse
import csv
import json
import math
from pathlib import Path


def percentile(values, p):
    values = sorted(v for v in values if math.isfinite(v))
    if not values:
        return None
    if len(values) == 1:
        return values[0]

    position = (len(values) - 1) * p
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return values[lower]

    weight = position - lower
    return values[lower] * (1 - weight) + values[upper] * weight


def summarize(values):
    values = [v for v in values if math.isfinite(v)]
    if not values:
        return {
            "count": 0,
            "mean": None,
            "p50": None,
            "p95": None,
            "p99": None,
            "max": None,
        }

    return {
        "count": len(values),
        "mean": sum(values) / len(values),
        "p50": percentile(values, 0.50),
        "p95": percentile(values, 0.95),
        "p99": percentile(values, 0.99),
        "max": max(values),
    }


def parse_numeric(value):
    if value is None:
        return None
    text = value.strip()
    if not text or text.upper() in {"NA", "N/A", "NULL"}:
        return None
    try:
        number = float(text)
    except ValueError:
        return None
    return number if math.isfinite(number) else None


def summarize_csv(path, columns):
    values = {column: [] for column in columns}
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        missing = [column for column in columns if column not in (reader.fieldnames or [])]
        if missing:
            raise ValueError("missing columns: " + ", ".join(missing))

        rows = 0
        for row in reader:
            rows += 1
            for column in columns:
                number = parse_numeric(row.get(column))
                if number is not None:
                    values[column].append(number)

    return {
        "rows": rows,
        "columns": {column: summarize(samples) for column, samples in values.items()},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path")
    parser.add_argument(
        "--column",
        action="append",
        dest="columns",
        required=True,
        help="numeric column to summarize; repeat for multiple columns",
    )
    args = parser.parse_args()

    result = summarize_csv(args.csv_path, args.columns)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="GDS Python Toolkit"
    )

    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        required=True,
        help="Input GDS file",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("data/output/output.gds"),
        help="Output GDS file",
    )

    return parser.parse_args()
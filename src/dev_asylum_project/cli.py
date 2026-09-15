"""Command-line interface for the DEV Asylum scaffold."""

from __future__ import annotations

import argparse

from .core import experiment


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the DEV Asylum experiment scaffold.")
    parser.add_argument(
        "value",
        type=float,
        nargs="?",
        default=21.0,
        help="Demo input value.",
    )
    args = parser.parse_args()
    result = experiment(args.value)
    print(f"experiment({args.value}) = {result}")


if __name__ == "__main__":
    main()

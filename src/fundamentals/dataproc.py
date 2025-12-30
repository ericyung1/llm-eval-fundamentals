#!/usr/bin/env python3
"""
Lesson 10: Mini Capstone - Data Processing CLI

A command-line tool for processing JSONL data files.

YOUR TASK: Complete all the TODO sections to make this CLI work.

Usage:
    python dataproc.py input.jsonl output.json
    python dataproc.py input.jsonl output.csv --transform uppercase
    python dataproc.py input.jsonl output.json --transform filter --filter-key status --filter-value active
    python dataproc.py input.jsonl output.jsonl --transform add_timestamp --verbose
"""

import argparse
import csv
import json
import logging
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

# ============================================================
# LOGGING SETUP
# ============================================================

logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False) -> None:
    """
    Configure logging for the application.
    
    Args:
        verbose: If True, set level to DEBUG; otherwise INFO
    """
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


# ============================================================
# FILE I/O FUNCTIONS - Complete these
# ============================================================

def read_jsonl(filepath: Path) -> list[dict[str, Any]]:
    """
    Read a JSONL file and return a list of dictionaries.
    
    Each line in the file should be a valid JSON object.
    Empty lines are skipped.
    
    Args:
        filepath: Path to the JSONL file
    
    Returns:
        List of dictionaries, one per line
    
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If a line contains invalid JSON
    
    Example:
        records = read_jsonl(Path("data.jsonl"))
    """
    # TODO: Implement this function
    # 1. Open the file and read line by line
    # 2. Skip empty lines
    # 3. Parse each line as JSON
    # 4. Return list of all records
    pass


def write_json(filepath: Path, data: list[dict[str, Any]], indent: int = 2) -> None:
    """
    Write data to a JSON file.
    
    Args:
        filepath: Path to the output file
        data: List of dictionaries to write
        indent: JSON indentation level
    """
    # TODO: Implement this function
    pass


def write_csv(filepath: Path, data: list[dict[str, Any]]) -> None:
    """
    Write data to a CSV file.
    
    Uses keys from the first record as column headers.
    
    Args:
        filepath: Path to the output file
        data: List of dictionaries to write
    
    Note:
        If data is empty, creates an empty file.
    """
    # TODO: Implement this function
    # 1. Handle empty data case
    # 2. Get fieldnames from first record
    # 3. Use csv.DictWriter to write
    pass


def write_jsonl(filepath: Path, data: list[dict[str, Any]]) -> None:
    """
    Write data to a JSONL file.
    
    Args:
        filepath: Path to the output file
        data: List of dictionaries to write
    """
    # TODO: Implement this function
    pass


def write_output(filepath: Path, data: list[dict[str, Any]]) -> None:
    """
    Write data to the appropriate format based on file extension.
    
    Args:
        filepath: Path to the output file (.json, .csv, or .jsonl)
        data: List of dictionaries to write
    
    Raises:
        ValueError: If file extension is not supported
    """
    # TODO: Implement this function
    # 1. Get the file extension
    # 2. Call the appropriate write function
    # 3. Raise ValueError for unknown extensions
    pass


# ============================================================
# TRANSFORMATION FUNCTIONS - Complete these
# ============================================================

def transform_uppercase(record: dict[str, Any]) -> dict[str, Any]:
    """
    Convert all string values in a record to uppercase.
    
    Non-string values are left unchanged.
    
    Args:
        record: Dictionary to transform
    
    Returns:
        New dictionary with uppercase string values
    
    Example:
        transform_uppercase({"name": "Alice", "age": 30})
        # Returns: {"name": "ALICE", "age": 30}
    """
    # TODO: Implement this function
    pass


def transform_filter(
    records: list[dict[str, Any]],
    key: str,
    value: str,
) -> list[dict[str, Any]]:
    """
    Filter records where key equals value.
    
    Args:
        records: List of records to filter
        key: The key to check
        value: The value to match (compared as string)
    
    Returns:
        List of records where record[key] == value
    
    Example:
        records = [{"status": "active"}, {"status": "inactive"}]
        transform_filter(records, "status", "active")
        # Returns: [{"status": "active"}]
    """
    # TODO: Implement this function
    pass


def transform_add_timestamp(record: dict[str, Any]) -> dict[str, Any]:
    """
    Add a 'processed_at' timestamp to a record.
    
    Args:
        record: Dictionary to transform
    
    Returns:
        New dictionary with 'processed_at' field added
    
    Example:
        transform_add_timestamp({"id": 1})
        # Returns: {"id": 1, "processed_at": "2024-01-15T10:30:00"}
    """
    # TODO: Implement this function
    # Hint: Use datetime.now().isoformat()
    pass


def apply_transform(
    records: list[dict[str, Any]],
    transform: str,
    filter_key: str | None = None,
    filter_value: str | None = None,
) -> list[dict[str, Any]]:
    """
    Apply a transformation to records.
    
    Args:
        records: List of records to transform
        transform: Transformation name ("none", "uppercase", "filter", "add_timestamp")
        filter_key: Key for filter transformation
        filter_value: Value for filter transformation
    
    Returns:
        Transformed list of records
    
    Raises:
        ValueError: If transform is "filter" but key/value not provided
    """
    # TODO: Implement this function
    # 1. If transform is "none", return records unchanged
    # 2. If transform is "uppercase", apply transform_uppercase to each record
    # 3. If transform is "filter", call transform_filter
    # 4. If transform is "add_timestamp", apply transform_add_timestamp to each
    pass


# ============================================================
# CLI SETUP - Complete this
# ============================================================

def create_parser() -> argparse.ArgumentParser:
    """
    Create the argument parser for the CLI.
    
    Returns:
        Configured ArgumentParser
    
    Arguments to support:
        - input: Positional, Path to input JSONL file
        - output: Positional, Path to output file
        - --transform, -t: Choice of transformations
        - --filter-key: Key for filter transform
        - --filter-value: Value for filter transform
        - --limit, -l: Maximum number of records to process
        - --verbose, -v: Enable verbose logging
    """
    parser = argparse.ArgumentParser(
        description="Process JSONL data files with transformations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s input.jsonl output.json
    %(prog)s input.jsonl output.csv --transform uppercase
    %(prog)s data.jsonl filtered.json --transform filter --filter-key status --filter-value active
    %(prog)s data.jsonl processed.jsonl --transform add_timestamp --verbose
        """,
    )
    
    # TODO: Add positional arguments
    # parser.add_argument("input", type=Path, help="...")
    # parser.add_argument("output", type=Path, help="...")
    
    # TODO: Add --transform argument with choices
    
    # TODO: Add --filter-key and --filter-value arguments
    
    # TODO: Add --limit argument (type=int)
    
    # TODO: Add --verbose flag
    
    return parser


# ============================================================
# MAIN FUNCTION - Complete this
# ============================================================

def main(argv: list[str] | None = None) -> int:
    """
    Main entry point for the CLI.
    
    Args:
        argv: Command line arguments (None uses sys.argv)
    
    Returns:
        Exit code (0 for success, non-zero for error)
    """
    parser = create_parser()
    args = parser.parse_args(argv)
    
    # TODO: Setup logging based on --verbose flag
    
    # TODO: Validate input file exists
    # If not, print error and return 1
    
    # TODO: Read input file
    # Handle exceptions and log errors
    
    # TODO: Apply limit if specified
    # records = records[:args.limit]
    
    # TODO: Apply transformation
    # Handle exceptions (e.g., missing filter key/value)
    
    # TODO: Write output file
    # Handle exceptions
    
    # TODO: Log success message with record count
    
    # TODO: Return 0 for success
    pass


if __name__ == "__main__":
    sys.exit(main() or 0)


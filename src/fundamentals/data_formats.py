"""
Lesson 4: Data Formats - Starter Code

Complete the TODO items in each function.
Run tests with: pytest tests/test_lesson_04.py -v
"""

import csv
import json
from pathlib import Path
from typing import Any


def read_json(filepath: Path) -> dict[str, Any]:
    """
    Read a JSON file and return its contents as a dictionary.
    
    Args:
        filepath: Path to the JSON file
    
    Returns:
        Dictionary containing the JSON data
    
    Example:
        data = read_json(Path("config.json"))
    """
    # TODO: Implement this function
    # Hint: Use json.load() with a file opened for reading
    pass


def write_json(filepath: Path, data: dict[str, Any], indent: int = 2) -> None:
    """
    Write a dictionary to a JSON file.
    
    Args:
        filepath: Path to the output JSON file
        data: Dictionary to write
        indent: Number of spaces for indentation (default: 2)
    
    Example:
        write_json(Path("output.json"), {"name": "Alice"})
    """
    # TODO: Implement this function
    # Hint: Use json.dump() with a file opened for writing
    pass


def read_csv(filepath: Path) -> list[dict[str, str]]:
    """
    Read a CSV file and return its contents as a list of dictionaries.
    
    Uses the first row as headers/keys for the dictionaries.
    
    Args:
        filepath: Path to the CSV file
    
    Returns:
        List of dictionaries, one per row
    
    Example:
        # For a CSV with headers "name,age":
        # [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
    """
    # TODO: Implement this function
    # Hint: Use csv.DictReader
    pass


def write_csv(filepath: Path, data: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    """
    Write a list of dictionaries to a CSV file.
    
    Args:
        filepath: Path to the output CSV file
        data: List of dictionaries to write
        fieldnames: Optional list of column names. If None, uses keys from first row.
    
    Example:
        write_csv(
            Path("output.csv"),
            [{"name": "Alice", "age": 30}],
            fieldnames=["name", "age"]
        )
    """
    # TODO: Implement this function
    # Hint: Use csv.DictWriter with writeheader() and writerows()
    # Don't forget newline="" when opening the file!
    pass


def read_jsonl(filepath: Path) -> list[dict[str, Any]]:
    """
    Read a JSONL (JSON Lines) file and return a list of dictionaries.
    
    JSONL format has one JSON object per line.
    
    Args:
        filepath: Path to the JSONL file
    
    Returns:
        List of dictionaries, one per line
    
    Example:
        # For a file with:
        # {"id": 1}
        # {"id": 2}
        # Returns: [{"id": 1}, {"id": 2}]
    """
    # TODO: Implement this function
    # Hint: Read line by line and use json.loads() on each line
    # Remember to strip whitespace from each line!
    pass


def write_jsonl(filepath: Path, data: list[dict[str, Any]]) -> None:
    """
    Write a list of dictionaries to a JSONL file.
    
    Args:
        filepath: Path to the output JSONL file
        data: List of dictionaries to write (one per line)
    
    Example:
        write_jsonl(Path("output.jsonl"), [{"id": 1}, {"id": 2}])
    """
    # TODO: Implement this function
    # Hint: Write json.dumps(item) + "\n" for each item
    pass


def convert_csv_to_jsonl(csv_path: Path, jsonl_path: Path) -> int:
    """
    Convert a CSV file to JSONL format.
    
    Args:
        csv_path: Path to input CSV file
        jsonl_path: Path to output JSONL file
    
    Returns:
        Number of records converted
    
    Example:
        count = convert_csv_to_jsonl(Path("data.csv"), Path("data.jsonl"))
    """
    # TODO: Implement this function
    # Hint: Use read_csv and write_jsonl that you already implemented!
    pass


def main():
    """Demonstrate the data format functions."""
    from pathlib import Path
    import tempfile
    
    print("=" * 50)
    print("Testing Lesson 4: Data Formats")
    print("=" * 50)
    
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        
        # Test JSON
        print("\n--- JSON ---")
        json_file = tmp / "test.json"
        test_data = {"name": "Alice", "scores": [95, 87, 92]}
        write_json(json_file, test_data)
        print(f"Wrote: {test_data}")
        loaded = read_json(json_file)
        print(f"Read:  {loaded}")
        
        # Test CSV
        print("\n--- CSV ---")
        csv_file = tmp / "test.csv"
        csv_data = [
            {"name": "Alice", "age": "30"},
            {"name": "Bob", "age": "25"},
        ]
        write_csv(csv_file, csv_data, fieldnames=["name", "age"])
        print(f"Wrote: {csv_data}")
        loaded = read_csv(csv_file)
        print(f"Read:  {loaded}")
        
        # Test JSONL
        print("\n--- JSONL ---")
        jsonl_file = tmp / "test.jsonl"
        jsonl_data = [{"id": 1, "text": "Hello"}, {"id": 2, "text": "World"}]
        write_jsonl(jsonl_file, jsonl_data)
        print(f"Wrote: {jsonl_data}")
        loaded = read_jsonl(jsonl_file)
        print(f"Read:  {loaded}")
        
        print("\n" + "=" * 50)


if __name__ == "__main__":
    main()


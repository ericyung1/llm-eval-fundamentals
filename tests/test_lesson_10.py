"""
Tests for Lesson 10: Mini Capstone

These tests verify the dataproc CLI tool works correctly.

Run with: pytest tests/test_lesson_10.py -v
"""

import json
import csv
import pytest
import subprocess
import sys
from pathlib import Path
import tempfile


# Import functions to test
from src.fundamentals.dataproc import (
    read_jsonl,
    write_json,
    write_csv,
    write_jsonl,
    write_output,
    transform_uppercase,
    transform_filter,
    transform_add_timestamp,
    apply_transform,
    create_parser,
)


CLI_PATH = Path(__file__).parent.parent / "src" / "fundamentals" / "dataproc.py"


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_jsonl(temp_dir):
    """Create a sample JSONL file."""
    filepath = temp_dir / "sample.jsonl"
    records = [
        {"id": 1, "name": "Alice", "status": "active"},
        {"id": 2, "name": "Bob", "status": "inactive"},
        {"id": 3, "name": "Charlie", "status": "active"},
    ]
    with open(filepath, "w") as f:
        for record in records:
            f.write(json.dumps(record) + "\n")
    return filepath


def run_cli(*args) -> tuple[int, str, str]:
    """Run the CLI and return (exit_code, stdout, stderr)."""
    result = subprocess.run(
        [sys.executable, str(CLI_PATH)] + list(str(a) for a in args),
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr


class TestReadJSONL:
    """Tests for read_jsonl function."""
    
    def test_read_basic(self, sample_jsonl):
        """Test reading a basic JSONL file."""
        records = read_jsonl(sample_jsonl)
        assert len(records) == 3
        assert records[0]["name"] == "Alice"
    
    def test_read_empty_file(self, temp_dir):
        """Test reading an empty file."""
        filepath = temp_dir / "empty.jsonl"
        filepath.write_text("")
        
        records = read_jsonl(filepath)
        assert records == []
    
    def test_read_with_blank_lines(self, temp_dir):
        """Test that blank lines are skipped."""
        filepath = temp_dir / "blanks.jsonl"
        filepath.write_text('{"a": 1}\n\n{"b": 2}\n')
        
        records = read_jsonl(filepath)
        assert len(records) == 2
    
    def test_read_nonexistent_raises(self, temp_dir):
        """Test that reading nonexistent file raises."""
        with pytest.raises(FileNotFoundError):
            read_jsonl(temp_dir / "nonexistent.jsonl")


class TestWriteFunctions:
    """Tests for write functions."""
    
    def test_write_json(self, temp_dir):
        """Test writing JSON file."""
        filepath = temp_dir / "output.json"
        data = [{"a": 1}, {"b": 2}]
        
        write_json(filepath, data)
        
        content = json.loads(filepath.read_text())
        assert content == data
    
    def test_write_csv(self, temp_dir):
        """Test writing CSV file."""
        filepath = temp_dir / "output.csv"
        data = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
        
        write_csv(filepath, data)
        
        with open(filepath) as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        assert len(rows) == 2
        assert rows[0]["name"] == "Alice"
    
    def test_write_jsonl(self, temp_dir):
        """Test writing JSONL file."""
        filepath = temp_dir / "output.jsonl"
        data = [{"a": 1}, {"b": 2}]
        
        write_jsonl(filepath, data)
        
        lines = filepath.read_text().strip().split("\n")
        assert len(lines) == 2
        assert json.loads(lines[0]) == {"a": 1}
    
    def test_write_output_json(self, temp_dir):
        """Test write_output with .json extension."""
        filepath = temp_dir / "out.json"
        data = [{"x": 1}]
        
        write_output(filepath, data)
        
        assert filepath.exists()
        assert json.loads(filepath.read_text()) == data
    
    def test_write_output_csv(self, temp_dir):
        """Test write_output with .csv extension."""
        filepath = temp_dir / "out.csv"
        data = [{"x": "1"}]
        
        write_output(filepath, data)
        
        assert filepath.exists()
    
    def test_write_output_unknown_raises(self, temp_dir):
        """Test write_output with unknown extension raises."""
        filepath = temp_dir / "out.xyz"
        
        with pytest.raises(ValueError):
            write_output(filepath, [{"a": 1}])


class TestTransformations:
    """Tests for transformation functions."""
    
    def test_uppercase_strings(self):
        """Test uppercase transforms string values."""
        record = {"name": "Alice", "city": "NYC"}
        result = transform_uppercase(record)
        
        assert result["name"] == "ALICE"
        assert result["city"] == "NYC"
    
    def test_uppercase_preserves_non_strings(self):
        """Test uppercase preserves non-string values."""
        record = {"name": "Alice", "age": 30, "active": True}
        result = transform_uppercase(record)
        
        assert result["age"] == 30
        assert result["active"] is True
    
    def test_filter_basic(self):
        """Test filter keeps matching records."""
        records = [
            {"status": "active"},
            {"status": "inactive"},
            {"status": "active"},
        ]
        result = transform_filter(records, "status", "active")
        
        assert len(result) == 2
        assert all(r["status"] == "active" for r in result)
    
    def test_filter_no_matches(self):
        """Test filter with no matches returns empty list."""
        records = [{"status": "inactive"}]
        result = transform_filter(records, "status", "active")
        
        assert result == []
    
    def test_add_timestamp(self):
        """Test add_timestamp adds field."""
        record = {"id": 1}
        result = transform_add_timestamp(record)
        
        assert "processed_at" in result
        assert result["id"] == 1  # Original preserved
    
    def test_add_timestamp_format(self):
        """Test timestamp is in ISO format."""
        record = {"id": 1}
        result = transform_add_timestamp(record)
        
        # Should be parseable as ISO format
        from datetime import datetime
        datetime.fromisoformat(result["processed_at"])


class TestApplyTransform:
    """Tests for apply_transform function."""
    
    def test_none_transform(self):
        """Test 'none' transform returns unchanged."""
        records = [{"a": 1}]
        result = apply_transform(records, "none")
        assert result == records
    
    def test_uppercase_transform(self):
        """Test 'uppercase' transform."""
        records = [{"name": "alice"}]
        result = apply_transform(records, "uppercase")
        assert result[0]["name"] == "ALICE"
    
    def test_filter_transform(self):
        """Test 'filter' transform."""
        records = [{"x": "1"}, {"x": "2"}]
        result = apply_transform(records, "filter", filter_key="x", filter_value="1")
        assert len(result) == 1
    
    def test_add_timestamp_transform(self):
        """Test 'add_timestamp' transform."""
        records = [{"id": 1}]
        result = apply_transform(records, "add_timestamp")
        assert "processed_at" in result[0]


class TestCLI:
    """Tests for CLI functionality."""
    
    def test_help(self):
        """Test --help works."""
        code, stdout, stderr = run_cli("--help")
        assert code == 0
        help_text = stdout + stderr
        assert "input" in help_text.lower()
        assert "output" in help_text.lower()
    
    def test_basic_conversion(self, sample_jsonl, temp_dir):
        """Test basic JSONL to JSON conversion."""
        output = temp_dir / "output.json"
        code, stdout, stderr = run_cli(sample_jsonl, output)
        
        assert code == 0, f"CLI failed: {stderr}"
        assert output.exists()
        
        data = json.loads(output.read_text())
        assert len(data) == 3
    
    def test_csv_output(self, sample_jsonl, temp_dir):
        """Test JSONL to CSV conversion."""
        output = temp_dir / "output.csv"
        code, stdout, stderr = run_cli(sample_jsonl, output)
        
        assert code == 0, f"CLI failed: {stderr}"
        assert output.exists()
    
    def test_uppercase_transform(self, sample_jsonl, temp_dir):
        """Test --transform uppercase."""
        output = temp_dir / "output.json"
        code, stdout, stderr = run_cli(
            sample_jsonl, output, "--transform", "uppercase"
        )
        
        assert code == 0, f"CLI failed: {stderr}"
        
        data = json.loads(output.read_text())
        assert data[0]["name"] == "ALICE"
    
    def test_filter_transform(self, sample_jsonl, temp_dir):
        """Test --transform filter with key/value."""
        output = temp_dir / "output.json"
        code, stdout, stderr = run_cli(
            sample_jsonl, output,
            "--transform", "filter",
            "--filter-key", "status",
            "--filter-value", "active"
        )
        
        assert code == 0, f"CLI failed: {stderr}"
        
        data = json.loads(output.read_text())
        assert len(data) == 2  # Only active records
    
    def test_limit_option(self, sample_jsonl, temp_dir):
        """Test --limit option."""
        output = temp_dir / "output.json"
        code, stdout, stderr = run_cli(
            sample_jsonl, output, "--limit", "1"
        )
        
        assert code == 0, f"CLI failed: {stderr}"
        
        data = json.loads(output.read_text())
        assert len(data) == 1
    
    def test_nonexistent_input(self, temp_dir):
        """Test error for nonexistent input file."""
        code, stdout, stderr = run_cli(
            temp_dir / "nonexistent.jsonl",
            temp_dir / "output.json"
        )
        
        assert code != 0


class TestParser:
    """Tests for argument parser."""
    
    def test_parser_has_input(self):
        """Parser should have input argument."""
        parser = create_parser()
        # Try parsing with required args
        args = parser.parse_args(["input.jsonl", "output.json"])
        assert hasattr(args, "input")
    
    def test_parser_has_output(self):
        """Parser should have output argument."""
        parser = create_parser()
        args = parser.parse_args(["input.jsonl", "output.json"])
        assert hasattr(args, "output")
    
    def test_parser_has_transform(self):
        """Parser should have transform option."""
        parser = create_parser()
        args = parser.parse_args([
            "input.jsonl", "output.json",
            "--transform", "uppercase"
        ])
        assert args.transform == "uppercase"
    
    def test_parser_has_verbose(self):
        """Parser should have verbose flag."""
        parser = create_parser()
        args = parser.parse_args([
            "input.jsonl", "output.json", "--verbose"
        ])
        assert args.verbose is True


class TestEndToEnd:
    """End-to-end integration tests."""
    
    def test_full_pipeline(self, temp_dir):
        """Test complete pipeline: create input, process, verify output."""
        # Create input
        input_file = temp_dir / "input.jsonl"
        input_data = [
            {"id": 1, "name": "test", "active": True},
            {"id": 2, "name": "demo", "active": False},
        ]
        with open(input_file, "w") as f:
            for record in input_data:
                f.write(json.dumps(record) + "\n")
        
        # Process with uppercase
        output_file = temp_dir / "output.json"
        code, stdout, stderr = run_cli(
            input_file, output_file,
            "--transform", "uppercase"
        )
        
        assert code == 0, f"Pipeline failed: {stderr}"
        
        # Verify output
        output_data = json.loads(output_file.read_text())
        assert len(output_data) == 2
        assert output_data[0]["name"] == "TEST"
        assert output_data[1]["name"] == "DEMO"
    
    def test_csv_roundtrip(self, temp_dir):
        """Test JSONL -> CSV works correctly."""
        # Create input
        input_file = temp_dir / "input.jsonl"
        input_data = [{"col1": "a", "col2": "b"}]
        with open(input_file, "w") as f:
            for record in input_data:
                f.write(json.dumps(record) + "\n")
        
        # Convert to CSV
        output_file = temp_dir / "output.csv"
        code, _, _ = run_cli(input_file, output_file)
        
        assert code == 0
        
        # Read CSV back
        with open(output_file) as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        assert len(rows) == 1
        assert rows[0]["col1"] == "a"


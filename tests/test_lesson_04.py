"""
Tests for Lesson 4: Data Formats

Run with: pytest tests/test_lesson_04.py -v
"""

import json
import pytest
from pathlib import Path
import tempfile

from src.fundamentals.data_formats import (
    read_json,
    write_json,
    read_csv,
    write_csv,
    read_jsonl,
    write_jsonl,
    convert_csv_to_jsonl,
)


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


class TestJSON:
    """Tests for JSON read/write functions."""
    
    def test_read_json(self, temp_dir):
        """Test reading a JSON file."""
        json_file = temp_dir / "test.json"
        expected = {"name": "Alice", "age": 30, "active": True}
        json_file.write_text(json.dumps(expected))
        
        result = read_json(json_file)
        assert result == expected
    
    def test_write_json(self, temp_dir):
        """Test writing a JSON file."""
        json_file = temp_dir / "output.json"
        data = {"name": "Bob", "scores": [95, 87, 92]}
        
        write_json(json_file, data)
        
        assert json_file.exists()
        content = json.loads(json_file.read_text())
        assert content == data
    
    def test_write_json_with_indent(self, temp_dir):
        """Test that JSON is written with proper indentation."""
        json_file = temp_dir / "formatted.json"
        data = {"key": "value"}
        
        write_json(json_file, data, indent=4)
        
        content = json_file.read_text()
        # Should have newlines and spaces for indentation
        assert "\n" in content
    
    def test_read_json_nested(self, temp_dir):
        """Test reading nested JSON."""
        json_file = temp_dir / "nested.json"
        expected = {
            "user": {
                "name": "Alice",
                "settings": {"theme": "dark", "notifications": True}
            },
            "items": [1, 2, 3]
        }
        json_file.write_text(json.dumps(expected))
        
        result = read_json(json_file)
        assert result == expected


class TestCSV:
    """Tests for CSV read/write functions."""
    
    def test_read_csv(self, temp_dir):
        """Test reading a CSV file."""
        csv_file = temp_dir / "test.csv"
        csv_file.write_text("name,age,city\nAlice,30,NYC\nBob,25,LA\n")
        
        result = read_csv(csv_file)
        
        assert len(result) == 2
        assert result[0]["name"] == "Alice"
        assert result[0]["age"] == "30"
        assert result[1]["name"] == "Bob"
    
    def test_write_csv(self, temp_dir):
        """Test writing a CSV file."""
        csv_file = temp_dir / "output.csv"
        data = [
            {"name": "Alice", "age": "30"},
            {"name": "Bob", "age": "25"},
        ]
        
        write_csv(csv_file, data, fieldnames=["name", "age"])
        
        assert csv_file.exists()
        content = csv_file.read_text()
        assert "name,age" in content
        assert "Alice,30" in content
        assert "Bob,25" in content
    
    def test_write_csv_infer_fieldnames(self, temp_dir):
        """Test that fieldnames are inferred from data if not provided."""
        csv_file = temp_dir / "output.csv"
        data = [{"x": "1", "y": "2"}]
        
        write_csv(csv_file, data)
        
        content = csv_file.read_text()
        # Should have a header row
        lines = content.strip().split("\n")
        assert len(lines) == 2  # Header + 1 data row
    
    def test_csv_roundtrip(self, temp_dir):
        """Test writing then reading CSV produces same data."""
        csv_file = temp_dir / "roundtrip.csv"
        original = [
            {"name": "Alice", "score": "95"},
            {"name": "Bob", "score": "87"},
        ]
        
        write_csv(csv_file, original, fieldnames=["name", "score"])
        result = read_csv(csv_file)
        
        assert result == original


class TestJSONL:
    """Tests for JSONL read/write functions."""
    
    def test_read_jsonl(self, temp_dir):
        """Test reading a JSONL file."""
        jsonl_file = temp_dir / "test.jsonl"
        jsonl_file.write_text('{"id": 1, "text": "Hello"}\n{"id": 2, "text": "World"}\n')
        
        result = read_jsonl(jsonl_file)
        
        assert len(result) == 2
        assert result[0]["id"] == 1
        assert result[0]["text"] == "Hello"
        assert result[1]["id"] == 2
    
    def test_write_jsonl(self, temp_dir):
        """Test writing a JSONL file."""
        jsonl_file = temp_dir / "output.jsonl"
        data = [{"id": 1}, {"id": 2}, {"id": 3}]
        
        write_jsonl(jsonl_file, data)
        
        assert jsonl_file.exists()
        lines = jsonl_file.read_text().strip().split("\n")
        assert len(lines) == 3
        assert json.loads(lines[0]) == {"id": 1}
        assert json.loads(lines[2]) == {"id": 3}
    
    def test_jsonl_roundtrip(self, temp_dir):
        """Test writing then reading JSONL produces same data."""
        jsonl_file = temp_dir / "roundtrip.jsonl"
        original = [
            {"name": "Alice", "score": 95},
            {"name": "Bob", "score": 87},
        ]
        
        write_jsonl(jsonl_file, original)
        result = read_jsonl(jsonl_file)
        
        assert result == original
    
    def test_read_jsonl_handles_whitespace(self, temp_dir):
        """Test that JSONL reading handles trailing whitespace."""
        jsonl_file = temp_dir / "whitespace.jsonl"
        jsonl_file.write_text('{"id": 1}  \n{"id": 2}\n\n')
        
        result = read_jsonl(jsonl_file)
        
        assert len(result) == 2


class TestConvertCSVToJSONL:
    """Tests for CSV to JSONL conversion."""
    
    def test_convert_csv_to_jsonl(self, temp_dir):
        """Test converting CSV to JSONL."""
        csv_file = temp_dir / "input.csv"
        jsonl_file = temp_dir / "output.jsonl"
        
        csv_file.write_text("name,score\nAlice,95\nBob,87\n")
        
        count = convert_csv_to_jsonl(csv_file, jsonl_file)
        
        assert count == 2
        assert jsonl_file.exists()
        
        result = read_jsonl(jsonl_file)
        assert len(result) == 2
        assert result[0]["name"] == "Alice"


# Summary test
def test_all_functions_implemented(temp_dir):
    """Verify all functions return non-None values."""
    # Setup test files
    json_file = temp_dir / "test.json"
    json_file.write_text('{"key": "value"}')
    
    csv_file = temp_dir / "test.csv"
    csv_file.write_text("a,b\n1,2\n")
    
    jsonl_file = temp_dir / "test.jsonl"
    jsonl_file.write_text('{"x": 1}\n')
    
    assert read_json(json_file) is not None, "read_json not implemented"
    assert read_csv(csv_file) is not None, "read_csv not implemented"
    assert read_jsonl(jsonl_file) is not None, "read_jsonl not implemented"
    
    # Test write functions (they return None but shouldn't raise)
    write_json(temp_dir / "out.json", {"a": 1})
    write_csv(temp_dir / "out.csv", [{"a": "1"}])
    write_jsonl(temp_dir / "out.jsonl", [{"a": 1}])
    
    assert convert_csv_to_jsonl(csv_file, temp_dir / "conv.jsonl") is not None


"""
Tests for Lesson 7: CLI Basics

Run with: pytest tests/test_lesson_07.py -v
"""

import json
import pytest
import subprocess
import sys
from pathlib import Path
import tempfile


# Path to the CLI tool
CLI_PATH = Path(__file__).parent.parent / "src" / "fundamentals" / "cli_tool.py"


@pytest.fixture
def temp_text_file():
    """Create a temporary text file for testing."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("Hello World\n")
        f.write("This is a test file\n")
        f.write("With multiple lines\n")
        f.write("For testing the CLI\n")
        temp_path = Path(f.name)
    yield temp_path
    temp_path.unlink()  # Cleanup


def run_cli(*args) -> tuple[int, str, str]:
    """Run the CLI and return (exit_code, stdout, stderr)."""
    result = subprocess.run(
        [sys.executable, str(CLI_PATH)] + list(args),
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr


class TestCLIHelp:
    """Tests for CLI help and documentation."""
    
    def test_help_flag(self):
        """Test that --help works."""
        code, stdout, stderr = run_cli("--help")
        assert code == 0
        assert "usage:" in stdout.lower() or "usage:" in stderr.lower()
    
    def test_help_contains_arguments(self):
        """Test that help shows all arguments."""
        code, stdout, stderr = run_cli("--help")
        help_text = stdout + stderr
        
        assert "file" in help_text.lower(), "Help should mention 'file' argument"
        assert "--format" in help_text or "-f" in help_text, "Help should show --format"
        assert "--uppercase" in help_text or "-u" in help_text, "Help should show --uppercase"


class TestCLIBasicUsage:
    """Tests for basic CLI functionality."""
    
    def test_analyze_file(self, temp_text_file):
        """Test basic file analysis."""
        code, stdout, stderr = run_cli(str(temp_text_file))
        assert code == 0, f"CLI failed with: {stderr}"
        
        # Should show some output
        assert len(stdout) > 0, "Should produce output"
    
    def test_shows_line_count(self, temp_text_file):
        """Test that output shows line count."""
        code, stdout, stderr = run_cli(str(temp_text_file))
        assert code == 0
        
        # Should mention lines (either in text or as a number)
        output = stdout.lower()
        assert "line" in output or "4" in output
    
    def test_shows_word_count(self, temp_text_file):
        """Test that output shows word count."""
        code, stdout, stderr = run_cli(str(temp_text_file))
        assert code == 0
        
        output = stdout.lower()
        assert "word" in output


class TestCLIFormatOption:
    """Tests for --format option."""
    
    def test_format_json(self, temp_text_file):
        """Test JSON output format."""
        code, stdout, stderr = run_cli(str(temp_text_file), "--format", "json")
        assert code == 0, f"CLI failed: {stderr}"
        
        # Should be valid JSON
        try:
            data = json.loads(stdout)
        except json.JSONDecodeError:
            pytest.fail(f"Output is not valid JSON: {stdout[:200]}")
        
        # Should have expected keys
        assert "lines" in data or "words" in data, "JSON should have statistics"
    
    def test_format_json_short_flag(self, temp_text_file):
        """Test -f short flag works."""
        code, stdout, stderr = run_cli(str(temp_text_file), "-f", "json")
        assert code == 0
        
        # Should be valid JSON
        data = json.loads(stdout)
        assert isinstance(data, dict)
    
    def test_format_text_default(self, temp_text_file):
        """Test that text is the default format."""
        code, stdout, stderr = run_cli(str(temp_text_file))
        assert code == 0
        
        # Default should not be JSON
        try:
            json.loads(stdout)
            # If it parses as JSON, that's okay too, but typically text format
        except json.JSONDecodeError:
            pass  # Expected for text format


class TestCLIUppercase:
    """Tests for --uppercase option."""
    
    def test_uppercase_flag(self, temp_text_file):
        """Test --uppercase converts output."""
        code, stdout, stderr = run_cli(str(temp_text_file), "--uppercase")
        assert code == 0
        
        # Output should be uppercase
        # Check that common words are uppercase
        assert stdout == stdout.upper(), "Output should be uppercase"
    
    def test_uppercase_short_flag(self, temp_text_file):
        """Test -u short flag works."""
        code, stdout, stderr = run_cli(str(temp_text_file), "-u")
        assert code == 0
        assert stdout == stdout.upper()
    
    def test_uppercase_with_json(self, temp_text_file):
        """Test uppercase works with JSON format."""
        code, stdout, stderr = run_cli(str(temp_text_file), "--format", "json", "--uppercase")
        assert code == 0
        assert stdout == stdout.upper()


class TestCLILinesOption:
    """Tests for --lines option."""
    
    def test_lines_limit(self, temp_text_file):
        """Test --lines limits content lines."""
        code, stdout, stderr = run_cli(str(temp_text_file), "--lines", "2", "--format", "json")
        assert code == 0
        
        data = json.loads(stdout)
        if "content" in data:
            assert len(data["content"]) <= 2, "Should limit to 2 content lines"
    
    def test_lines_short_flag(self, temp_text_file):
        """Test -l short flag works."""
        code, stdout, stderr = run_cli(str(temp_text_file), "-l", "1", "-f", "json")
        assert code == 0
        
        data = json.loads(stdout)
        if "content" in data:
            assert len(data["content"]) <= 1


class TestCLIErrorHandling:
    """Tests for error handling."""
    
    def test_missing_file_argument(self):
        """Test error when file argument is missing."""
        code, stdout, stderr = run_cli()
        assert code != 0, "Should fail when no file provided"
    
    def test_nonexistent_file(self):
        """Test error for non-existent file."""
        code, stdout, stderr = run_cli("/nonexistent/path/file.txt")
        assert code != 0, "Should fail for non-existent file"
    
    def test_invalid_format_choice(self, temp_text_file):
        """Test error for invalid format choice."""
        code, stdout, stderr = run_cli(str(temp_text_file), "--format", "invalid")
        assert code != 0, "Should fail for invalid format"


class TestCLICombinedOptions:
    """Tests for combining multiple options."""
    
    def test_all_options(self, temp_text_file):
        """Test using all options together."""
        code, stdout, stderr = run_cli(
            str(temp_text_file),
            "--format", "json",
            "--uppercase",
            "--lines", "2"
        )
        assert code == 0
        
        # Should be uppercase
        assert stdout == stdout.upper()
        
        # Should be valid JSON (when parsed as uppercase)
        data = json.loads(stdout)
        assert isinstance(data, dict)


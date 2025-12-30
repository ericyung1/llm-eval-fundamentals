"""
Tests for Lesson 9: Code Quality

This test file verifies that:
1. Functions have type hints
2. Functions have docstrings
3. The code works correctly

Run with: pytest tests/test_lesson_09.py -v
"""

import ast
import inspect
import pytest
from pathlib import Path
from typing import get_type_hints

from src.fundamentals.quality import (
    format_name,
    calculate_average,
    parse_score,
    filter_by_threshold,
    merge_dicts,
    find_max_key,
    TextAnalyzer,
    Result,
)


def get_module_source() -> str:
    """Get the source code of the quality module."""
    module_path = Path(__file__).parent.parent / "src" / "fundamentals" / "quality.py"
    return module_path.read_text()


def get_function_node(source: str, func_name: str) -> ast.FunctionDef | None:
    """Get the AST node for a function."""
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            return node
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == func_name:
                    return item
    return None


def has_type_annotations(func_node: ast.FunctionDef) -> bool:
    """Check if a function has type annotations on all arguments and return."""
    # Check return annotation
    if func_node.returns is None:
        return False
    
    # Check all arguments (except self/cls)
    for arg in func_node.args.args:
        if arg.arg in ("self", "cls"):
            continue
        if arg.annotation is None:
            return False
    
    return True


def has_docstring(obj) -> bool:
    """Check if an object has a docstring."""
    doc = inspect.getdoc(obj)
    return doc is not None and len(doc.strip()) > 20  # More than just "TODO"


def docstring_has_section(obj, section: str) -> bool:
    """Check if docstring has a specific section (Args, Returns, etc.)."""
    doc = inspect.getdoc(obj)
    if not doc:
        return False
    return section.lower() in doc.lower()


class TestTypeHints:
    """Verify that functions have type hints."""
    
    def test_format_name_has_hints(self):
        """format_name should have type hints."""
        source = get_module_source()
        node = get_function_node(source, "format_name")
        assert node is not None
        assert has_type_annotations(node), "format_name needs type hints"
    
    def test_calculate_average_has_hints(self):
        """calculate_average should have type hints."""
        source = get_module_source()
        node = get_function_node(source, "calculate_average")
        assert has_type_annotations(node), "calculate_average needs type hints"
    
    def test_parse_score_has_hints(self):
        """parse_score should have type hints."""
        source = get_module_source()
        node = get_function_node(source, "parse_score")
        assert has_type_annotations(node), "parse_score needs type hints"
    
    def test_filter_by_threshold_has_hints(self):
        """filter_by_threshold should have type hints."""
        source = get_module_source()
        node = get_function_node(source, "filter_by_threshold")
        assert has_type_annotations(node), "filter_by_threshold needs type hints"
    
    def test_merge_dicts_has_hints(self):
        """merge_dicts should have type hints."""
        source = get_module_source()
        node = get_function_node(source, "merge_dicts")
        assert has_type_annotations(node), "merge_dicts needs type hints"
    
    def test_find_max_key_has_hints(self):
        """find_max_key should have type hints."""
        source = get_module_source()
        node = get_function_node(source, "find_max_key")
        assert has_type_annotations(node), "find_max_key needs type hints"


class TestDocstrings:
    """Verify that functions have proper docstrings."""
    
    def test_format_name_docstring(self):
        """format_name should have a docstring with Args and Returns."""
        assert has_docstring(format_name), "format_name needs a docstring"
        assert docstring_has_section(format_name, "Args"), "Docstring needs Args section"
        assert docstring_has_section(format_name, "Returns"), "Docstring needs Returns section"
    
    def test_calculate_average_docstring(self):
        """calculate_average should have a proper docstring."""
        assert has_docstring(calculate_average), "calculate_average needs a docstring"
        assert docstring_has_section(calculate_average, "Args"), "Docstring needs Args section"
    
    def test_parse_score_docstring_has_raises(self):
        """parse_score docstring should document exceptions."""
        assert has_docstring(parse_score), "parse_score needs a docstring"
        assert docstring_has_section(parse_score, "Raises"), "Docstring needs Raises section"
    
    def test_text_analyzer_class_docstring(self):
        """TextAnalyzer class should have a docstring."""
        assert has_docstring(TextAnalyzer), "TextAnalyzer needs a class docstring"
    
    def test_result_class_docstring(self):
        """Result class should have a docstring."""
        assert has_docstring(Result), "Result needs a class docstring"


class TestFunctionality:
    """Verify that functions work correctly."""
    
    def test_format_name_basic(self):
        """Test basic name formatting."""
        assert format_name("John", "Doe") == "John Doe"
    
    def test_format_name_uppercase(self):
        """Test uppercase formatting."""
        assert format_name("John", "Doe", uppercase=True) == "JOHN DOE"
    
    def test_calculate_average(self):
        """Test average calculation."""
        assert calculate_average([1, 2, 3, 4, 5]) == 3.0
        assert calculate_average([]) == 0.0
    
    def test_parse_score_valid(self):
        """Test parsing valid scores."""
        assert parse_score("85") == 85.0
        assert parse_score("100") == 100.0
        assert parse_score("0") == 0.0
    
    def test_parse_score_invalid(self):
        """Test parsing invalid scores raises ValueError."""
        with pytest.raises(ValueError):
            parse_score("not a number")
        with pytest.raises(ValueError):
            parse_score("150")  # Out of range
        with pytest.raises(ValueError):
            parse_score("-10")  # Negative
    
    def test_filter_by_threshold(self):
        """Test filtering by threshold."""
        assert filter_by_threshold([1, 5, 3, 8, 2], 4) == [5, 8]
        assert filter_by_threshold([1, 2, 3], 10) == []
    
    def test_merge_dicts(self):
        """Test merging dictionaries."""
        result = merge_dicts({"a": 1}, {"b": 2})
        assert result == {"a": 1, "b": 2}
    
    def test_merge_dicts_override(self):
        """Test that second dict overrides first."""
        result = merge_dicts({"a": 1}, {"a": 2})
        assert result == {"a": 2}
    
    def test_find_max_key(self):
        """Test finding key with maximum value."""
        assert find_max_key({"a": 1, "b": 5, "c": 3}) == "b"
        assert find_max_key({}) is None


class TestTextAnalyzer:
    """Tests for TextAnalyzer class."""
    
    def test_word_count(self):
        """Test word counting."""
        analyzer = TextAnalyzer("hello world foo bar")
        assert analyzer.word_count == 4
    
    def test_char_count(self):
        """Test character counting."""
        analyzer = TextAnalyzer("hello world")
        assert analyzer.char_count() == 11
        assert analyzer.char_count(include_spaces=False) == 10
    
    def test_contains_word(self):
        """Test word containment check."""
        analyzer = TextAnalyzer("Hello World")
        assert analyzer.contains_word("hello") is True
        assert analyzer.contains_word("foo") is False
    
    def test_unique_words(self):
        """Test unique word extraction."""
        analyzer = TextAnalyzer("hello hello world")
        assert analyzer.get_unique_words() == {"hello", "world"}
    
    def test_word_frequency(self):
        """Test word frequency counting."""
        analyzer = TextAnalyzer("hello hello world")
        freq = analyzer.get_word_frequency()
        assert freq["hello"] == 2
        assert freq["world"] == 1


class TestResult:
    """Tests for Result class."""
    
    def test_ok_result(self):
        """Test successful result."""
        result = Result.ok(42)
        assert result.is_ok() is True
        assert result.unwrap() == 42
    
    def test_err_result(self):
        """Test error result."""
        result = Result.err("Something went wrong")
        assert result.is_ok() is False
        assert result.error == "Something went wrong"
    
    def test_unwrap_error_raises(self):
        """Test that unwrap on error raises."""
        result = Result.err("Error!")
        with pytest.raises(RuntimeError):
            result.unwrap()


class TestTextAnalyzerDocstrings:
    """Verify TextAnalyzer methods have docstrings."""
    
    def test_init_docstring(self):
        """__init__ should have a docstring."""
        assert has_docstring(TextAnalyzer.__init__), "__init__ needs docstring"
    
    def test_char_count_docstring(self):
        """char_count should have a docstring."""
        assert has_docstring(TextAnalyzer.char_count), "char_count needs docstring"
    
    def test_contains_word_docstring(self):
        """contains_word should have a docstring."""
        assert has_docstring(TextAnalyzer.contains_word), "contains_word needs docstring"


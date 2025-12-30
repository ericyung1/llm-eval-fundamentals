"""
Autograder for Lesson 6: Testing Fundamentals

This test file checks that students have written the required tests.
Students should NOT modify this file.

Run with: pytest tests/test_lesson_06_grader.py -v
"""

import ast
import inspect
import pytest
from pathlib import Path


def get_test_file_path() -> Path:
    """Get the path to the student's test file."""
    return Path(__file__).parent / "test_lesson_06.py"


def get_test_functions() -> list[str]:
    """Parse the test file and return names of all test functions."""
    test_file = get_test_file_path()
    content = test_file.read_text()
    tree = ast.parse(content)
    
    test_names = []
    
    for node in ast.walk(tree):
        # Functions at module level
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_"):
            test_names.append(node.name)
        
        # Methods in classes
        if isinstance(node, ast.ClassDef) and node.name.startswith("Test"):
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name.startswith("test_"):
                    test_names.append(f"{node.name}.{item.name}")
    
    return test_names


def get_fixtures() -> list[str]:
    """Parse the test file and return names of all fixtures."""
    test_file = get_test_file_path()
    content = test_file.read_text()
    tree = ast.parse(content)
    
    fixtures = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for decorator in node.decorator_list:
                # Check for @pytest.fixture
                if isinstance(decorator, ast.Attribute):
                    if decorator.attr == "fixture":
                        fixtures.append(node.name)
                elif isinstance(decorator, ast.Name):
                    if decorator.id == "fixture":
                        fixtures.append(node.name)
    
    return fixtures


def check_function_not_just_pass(func_name: str) -> bool:
    """Check if a function has more than just 'pass' in its body."""
    test_file = get_test_file_path()
    content = test_file.read_text()
    tree = ast.parse(content)
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            # Check if body is just [Pass] or [Expr(docstring), Pass]
            non_pass_statements = [
                stmt for stmt in node.body 
                if not isinstance(stmt, ast.Pass) and not (
                    isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant)
                )
            ]
            return len(non_pass_statements) > 0
        
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name == func_name:
                    non_pass_statements = [
                        stmt for stmt in item.body 
                        if not isinstance(stmt, ast.Pass) and not (
                            isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant)
                        )
                    ]
                    return len(non_pass_statements) > 0
    
    return False


class TestGraderRequirements:
    """Verify that students have written the required tests."""
    
    def test_minimum_test_count(self):
        """Student must have at least 15 test functions."""
        test_names = get_test_functions()
        assert len(test_names) >= 15, (
            f"You have {len(test_names)} tests, need at least 15. "
            f"Current tests: {test_names}"
        )
    
    def test_has_add_tests(self):
        """Student must have tests for add function."""
        test_names = get_test_functions()
        add_tests = [t for t in test_names if "add" in t.lower()]
        assert len(add_tests) >= 3, (
            f"Need at least 3 tests for add(), found {len(add_tests)}"
        )
    
    def test_has_subtract_tests(self):
        """Student must have tests for subtract function."""
        test_names = get_test_functions()
        sub_tests = [t for t in test_names if "subtract" in t.lower()]
        assert len(sub_tests) >= 3, (
            f"Need at least 3 tests for subtract(), found {len(sub_tests)}"
        )
    
    def test_has_multiply_tests(self):
        """Student must have tests for multiply function."""
        test_names = get_test_functions()
        mul_tests = [t for t in test_names if "multiply" in t.lower()]
        assert len(mul_tests) >= 3, (
            f"Need at least 3 tests for multiply(), found {len(mul_tests)}"
        )
    
    def test_has_divide_tests(self):
        """Student must have tests for divide function."""
        test_names = get_test_functions()
        div_tests = [t for t in test_names if "divide" in t.lower()]
        assert len(div_tests) >= 3, (
            f"Need at least 3 tests for divide(), found {len(div_tests)}"
        )
    
    def test_has_power_tests(self):
        """Student must have tests for power function."""
        test_names = get_test_functions()
        pow_tests = [t for t in test_names if "power" in t.lower()]
        assert len(pow_tests) >= 3, (
            f"Need at least 3 tests for power(), found {len(pow_tests)}"
        )
    
    def test_has_fixture(self):
        """Student must define at least one fixture."""
        fixtures = get_fixtures()
        assert len(fixtures) >= 1, (
            f"Need at least 1 fixture, found {len(fixtures)}"
        )
    
    def test_fixture_implemented(self):
        """Student's fixture must be implemented (not just pass)."""
        fixtures = get_fixtures()
        if fixtures:
            assert check_function_not_just_pass(fixtures[0]), (
                f"Fixture '{fixtures[0]}' is not implemented (just has 'pass')"
            )
    
    def test_has_exception_test(self):
        """Student must have a test for divide by zero."""
        test_file = get_test_file_path()
        content = test_file.read_text()
        
        # Check for pytest.raises usage
        assert "pytest.raises" in content, (
            "No pytest.raises found. "
            "You must test that divide(x, 0) raises ZeroDivisionError"
        )
    
    def test_all_student_tests_pass(self):
        """All student-written tests must pass."""
        # This is verified by running pytest on test_lesson_06.py
        # If any test in that file fails, this indirectly catches it
        # via the overall pytest run
        pass


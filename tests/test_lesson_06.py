"""
Tests for Lesson 6: Testing Fundamentals

YOUR TASK: Complete the TODO sections to write tests for the calculator module.

Requirements:
- Write at least 3 tests for each function (add, subtract, multiply, divide, power)
- Use at least one fixture
- Test that divide by zero raises ZeroDivisionError
- All tests must pass

Run with: pytest tests/test_lesson_06.py -v
"""

import pytest
from src.fundamentals.calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    is_positive,
    absolute,
)


# ============================================================
# FIXTURE - Complete this fixture
# ============================================================

@pytest.fixture
def sample_numbers():
    """
    Fixture that provides sample numbers for testing.
    
    TODO: Return a dictionary with test numbers.
    Example: {"positive": 10, "negative": -5, "zero": 0, "float": 3.14}
    """
    # TODO: Implement this fixture
    pass


# ============================================================
# TESTS FOR add() - Write at least 3 tests
# ============================================================

class TestAdd:
    """Tests for the add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # TODO: Write this test
        pass
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # TODO: Write this test
        pass
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        # TODO: Write this test
        pass
    
    # TODO: Add more tests for add() if you want!


# ============================================================
# TESTS FOR subtract() - Write at least 3 tests
# ============================================================

class TestSubtract:
    """Tests for the subtract function."""
    
    def test_subtract_basic(self):
        """Test basic subtraction."""
        # TODO: Write this test
        pass
    
    def test_subtract_negative_result(self):
        """Test subtraction that results in negative."""
        # TODO: Write this test
        pass
    
    def test_subtract_zero(self):
        """Test subtracting zero."""
        # TODO: Write this test
        pass


# ============================================================
# TESTS FOR multiply() - Write at least 3 tests
# ============================================================

class TestMultiply:
    """Tests for the multiply function."""
    
    def test_multiply_positive(self):
        """Test multiplying positive numbers."""
        # TODO: Write this test
        pass
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        # TODO: Write this test
        pass
    
    def test_multiply_negative(self):
        """Test multiplying negative numbers."""
        # TODO: Write this test
        pass


# ============================================================
# TESTS FOR divide() - Write at least 3 tests + exception test
# ============================================================

class TestDivide:
    """Tests for the divide function."""
    
    def test_divide_basic(self):
        """Test basic division."""
        # TODO: Write this test
        pass
    
    def test_divide_result_float(self):
        """Test division that results in a float."""
        # TODO: Write this test
        pass
    
    def test_divide_negative(self):
        """Test division with negative numbers."""
        # TODO: Write this test
        pass
    
    def test_divide_by_zero_raises(self):
        """Test that dividing by zero raises ZeroDivisionError."""
        # TODO: Write this test using pytest.raises
        # Hint: with pytest.raises(ZeroDivisionError):
        #           divide(10, 0)
        pass


# ============================================================
# TESTS FOR power() - Write at least 3 tests
# ============================================================

class TestPower:
    """Tests for the power function."""
    
    def test_power_basic(self):
        """Test basic exponentiation."""
        # TODO: Write this test
        pass
    
    def test_power_of_zero(self):
        """Test raising to power of zero."""
        # TODO: Write this test (anything^0 = 1)
        pass
    
    def test_power_negative_exponent(self):
        """Test negative exponent."""
        # TODO: Write this test
        pass


# ============================================================
# TESTS USING FIXTURE - Use the sample_numbers fixture
# ============================================================

class TestWithFixture:
    """Tests that use the sample_numbers fixture."""
    
    def test_add_with_fixture(self, sample_numbers):
        """Test add using fixture data."""
        # TODO: Write this test using sample_numbers fixture
        # Example: assert add(sample_numbers["positive"], 0) == sample_numbers["positive"]
        pass
    
    def test_is_positive_with_fixture(self, sample_numbers):
        """Test is_positive using fixture data."""
        # TODO: Write this test
        pass


# ============================================================
# BONUS: Parametrized tests (optional)
# ============================================================

# TODO (OPTIONAL): Write a parametrized test
# @pytest.mark.parametrize("a,b,expected", [
#     (1, 2, 3),
#     (0, 0, 0),
#     (-1, 1, 0),
# ])
# def test_add_parametrized(a, b, expected):
#     assert add(a, b) == expected


"""
Tests for Lesson 3: Python Basics

Run with: pytest tests/test_lesson_03.py -v
"""

import pytest
from src.fundamentals.basics import (
    add_numbers,
    multiply_numbers,
    is_even,
    reverse_string,
    count_vowels,
    fizzbuzz,
)


class TestAddNumbers:
    """Tests for add_numbers function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add_numbers(3, 4) == 7
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add_numbers(-3, -4) == -7
    
    def test_add_zero(self):
        """Test adding zero."""
        assert add_numbers(5, 0) == 5
        assert add_numbers(0, 5) == 5
    
    def test_add_mixed(self):
        """Test adding positive and negative."""
        assert add_numbers(10, -3) == 7


class TestMultiplyNumbers:
    """Tests for multiply_numbers function."""
    
    def test_multiply_positive(self):
        """Test multiplying positive numbers."""
        assert multiply_numbers(3, 4) == 12
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply_numbers(5, 0) == 0
    
    def test_multiply_negative(self):
        """Test multiplying negative numbers."""
        assert multiply_numbers(-3, -4) == 12
        assert multiply_numbers(-3, 4) == -12


class TestIsEven:
    """Tests for is_even function."""
    
    def test_even_numbers(self):
        """Test that even numbers return True."""
        assert is_even(4) is True
        assert is_even(0) is True
        assert is_even(100) is True
    
    def test_odd_numbers(self):
        """Test that odd numbers return False."""
        assert is_even(5) is False
        assert is_even(1) is False
        assert is_even(99) is False
    
    def test_negative_even(self):
        """Test negative even numbers."""
        assert is_even(-4) is True
    
    def test_negative_odd(self):
        """Test negative odd numbers."""
        assert is_even(-5) is False


class TestReverseString:
    """Tests for reverse_string function."""
    
    def test_simple_reverse(self):
        """Test reversing a simple string."""
        assert reverse_string("hello") == "olleh"
    
    def test_palindrome(self):
        """Test a palindrome stays the same."""
        assert reverse_string("racecar") == "racecar"
    
    def test_empty_string(self):
        """Test empty string."""
        assert reverse_string("") == ""
    
    def test_single_char(self):
        """Test single character."""
        assert reverse_string("a") == "a"
    
    def test_with_spaces(self):
        """Test string with spaces."""
        assert reverse_string("hello world") == "dlrow olleh"


class TestCountVowels:
    """Tests for count_vowels function."""
    
    def test_basic_count(self):
        """Test basic vowel counting."""
        assert count_vowels("hello") == 2  # e, o
    
    def test_all_vowels(self):
        """Test string with all vowels."""
        assert count_vowels("aeiou") == 5
    
    def test_uppercase_vowels(self):
        """Test uppercase vowels are counted."""
        assert count_vowels("AEIOU") == 5
    
    def test_mixed_case(self):
        """Test mixed case string."""
        assert count_vowels("HeLLo WoRLd") == 3  # e, o, o
    
    def test_no_vowels(self):
        """Test string with no vowels."""
        assert count_vowels("xyz") == 0
    
    def test_empty_string(self):
        """Test empty string."""
        assert count_vowels("") == 0


class TestFizzBuzz:
    """Tests for fizzbuzz function."""
    
    def test_divisible_by_3(self):
        """Test numbers divisible by 3 only."""
        assert fizzbuzz(3) == "Fizz"
        assert fizzbuzz(9) == "Fizz"
    
    def test_divisible_by_5(self):
        """Test numbers divisible by 5 only."""
        assert fizzbuzz(5) == "Buzz"
        assert fizzbuzz(10) == "Buzz"
    
    def test_divisible_by_both(self):
        """Test numbers divisible by both 3 and 5."""
        assert fizzbuzz(15) == "FizzBuzz"
        assert fizzbuzz(30) == "FizzBuzz"
    
    def test_not_divisible(self):
        """Test numbers not divisible by 3 or 5."""
        assert fizzbuzz(7) == "7"
        assert fizzbuzz(1) == "1"
        assert fizzbuzz(22) == "22"


# Summary test to verify all functions work
def test_all_functions_implemented():
    """Verify all functions return non-None values."""
    assert add_numbers(1, 2) is not None, "add_numbers not implemented"
    assert multiply_numbers(1, 2) is not None, "multiply_numbers not implemented"
    assert is_even(2) is not None, "is_even not implemented"
    assert reverse_string("a") is not None, "reverse_string not implemented"
    assert count_vowels("a") is not None, "count_vowels not implemented"
    assert fizzbuzz(1) is not None, "fizzbuzz not implemented"


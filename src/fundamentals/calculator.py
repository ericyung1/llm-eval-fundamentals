"""
Lesson 6: Calculator Module

This module provides simple calculator functions for testing practice.
Students will write tests for these functions.
"""


def add(a: float, b: float) -> float:
    """
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Subtract b from a.
    
    Args:
        a: Number to subtract from
        b: Number to subtract
    
    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide a by b.
    
    Args:
        a: Dividend
        b: Divisor
    
    Returns:
        Quotient of a divided by b
    
    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(base: float, exp: int) -> float:
    """
    Raise base to the power of exp.
    
    Args:
        base: The base number
        exp: The exponent
    
    Returns:
        base raised to the power of exp
    """
    return base ** exp


def is_positive(n: float) -> bool:
    """
    Check if a number is positive.
    
    Args:
        n: The number to check
    
    Returns:
        True if n > 0, False otherwise
    """
    return n > 0


def absolute(n: float) -> float:
    """
    Return the absolute value of a number.
    
    Args:
        n: The number
    
    Returns:
        Absolute value of n
    """
    return abs(n)


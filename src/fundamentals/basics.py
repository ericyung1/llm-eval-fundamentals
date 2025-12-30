"""
Lesson 3: Python Basics - Starter Code

Complete the TODO items in each function.
Run tests with: pytest tests/test_lesson_03.py -v
"""


def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    # TODO: Implement this function
    pass


def multiply_numbers(a: int, b: int) -> int:
    """
    Multiply two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The product of a and b
    """
    # TODO: Implement this function
    pass


def is_even(n: int) -> bool:
    """
    Check if a number is even.
    
    Args:
        n: The number to check
    
    Returns:
        True if n is even, False otherwise
    """
    # TODO: Implement this function
    # Hint: Use the modulo operator (%)
    pass


def reverse_string(s: str) -> str:
    """
    Return the reverse of a string.
    
    Args:
        s: The string to reverse
    
    Returns:
        The reversed string
    
    Example:
        reverse_string("hello") -> "olleh"
    """
    # TODO: Implement this function
    # Hint: Use string slicing with [::-1]
    pass


def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a string.
    
    Vowels are: a, e, i, o, u (case-insensitive)
    
    Args:
        s: The string to analyze
    
    Returns:
        The count of vowels in the string
    
    Example:
        count_vowels("hello") -> 2
    """
    # TODO: Implement this function
    # Hint: Loop through each character and check if it's in "aeiouAEIOU"
    pass


def fizzbuzz(n: int) -> str:
    """
    Classic FizzBuzz problem.
    
    Rules:
        - If n is divisible by 3, return "Fizz"
        - If n is divisible by 5, return "Buzz"
        - If n is divisible by both 3 and 5, return "FizzBuzz"
        - Otherwise, return n as a string
    
    Args:
        n: The number to process
    
    Returns:
        "Fizz", "Buzz", "FizzBuzz", or the number as a string
    
    Examples:
        fizzbuzz(3)  -> "Fizz"
        fizzbuzz(5)  -> "Buzz"
        fizzbuzz(15) -> "FizzBuzz"
        fizzbuzz(7)  -> "7"
    """
    # TODO: Implement this function
    # Hint: Check divisibility by both 3 and 5 first!
    pass


def main():
    """Demonstrate and test the functions."""
    print("=" * 40)
    print("Testing Lesson 3 Functions")
    print("=" * 40)
    
    # Test add_numbers
    result = add_numbers(3, 4)
    print(f"add_numbers(3, 4) = {result}")
    
    # Test multiply_numbers
    result = multiply_numbers(3, 4)
    print(f"multiply_numbers(3, 4) = {result}")
    
    # Test is_even
    print(f"is_even(4) = {is_even(4)}")
    print(f"is_even(5) = {is_even(5)}")
    
    # Test reverse_string
    result = reverse_string("hello")
    print(f"reverse_string('hello') = '{result}'")
    
    # Test count_vowels
    result = count_vowels("hello world")
    print(f"count_vowels('hello world') = {result}")
    
    # Test fizzbuzz
    for n in [3, 5, 15, 7]:
        result = fizzbuzz(n)
        print(f"fizzbuzz({n}) = '{result}'")
    
    print("=" * 40)


if __name__ == "__main__":
    main()


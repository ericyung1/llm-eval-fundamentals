"""
Lesson 8: Robust Code - Starter Code

Complete the TODO sections to implement error handling, logging, and timing.

Run tests with: pytest tests/test_lesson_08.py -v
"""

import logging
import time
from contextlib import contextmanager
from functools import wraps
from typing import Any, Callable, TypeVar

T = TypeVar("T")


# ============================================================
# CUSTOM EXCEPTIONS - Complete these classes
# ============================================================

class ProcessingError(Exception):
    """
    Base exception for processing errors.
    
    TODO: This is complete - use as an example.
    """
    pass


class ValidationError(ProcessingError):
    """
    Raised when data validation fails.
    
    TODO: Add an __init__ that accepts:
    - field: str - the field that failed validation
    - reason: str - why it failed
    
    Store these as instance attributes and pass a message to super().__init__()
    """
    # TODO: Implement __init__
    pass


class RetryExhaustedError(ProcessingError):
    """
    Raised when all retry attempts have been exhausted.
    
    TODO: Add an __init__ that accepts:
    - attempts: int - number of attempts made
    - last_error: Exception - the last error that occurred
    
    Store these as instance attributes.
    """
    # TODO: Implement __init__
    pass


# ============================================================
# SAFE OPERATIONS - Complete these functions
# ============================================================

def safe_divide(a: float, b: float, default: float = 0.0) -> float:
    """
    Safely divide a by b, returning default if division fails.
    
    Args:
        a: Dividend
        b: Divisor
        default: Value to return if division fails
    
    Returns:
        Result of a/b, or default if b is zero
    
    Example:
        safe_divide(10, 2)  # Returns 5.0
        safe_divide(10, 0)  # Returns 0.0
        safe_divide(10, 0, default=-1)  # Returns -1
    """
    # TODO: Implement using try/except
    pass


def safe_parse_int(value: str, default: int = 0) -> int:
    """
    Safely parse a string to int, returning default if parsing fails.
    
    Args:
        value: String to parse
        default: Value to return if parsing fails
    
    Returns:
        Parsed integer, or default if parsing fails
    """
    # TODO: Implement using try/except
    pass


def validate_positive(value: float, field_name: str = "value") -> float:
    """
    Validate that a value is positive.
    
    Args:
        value: The value to validate
        field_name: Name of the field (for error messages)
    
    Returns:
        The value if valid
    
    Raises:
        ValidationError: If value is not positive
    """
    # TODO: Implement - raise ValidationError if value <= 0
    pass


# ============================================================
# LOGGING - Complete the setup function
# ============================================================

def setup_logging(
    level: int = logging.INFO,
    format_string: str | None = None,
    log_file: str | None = None,
) -> logging.Logger:
    """
    Configure logging for the application.
    
    Args:
        level: Logging level (e.g., logging.DEBUG, logging.INFO)
        format_string: Custom format string (optional)
        log_file: Path to log file (optional, if None only console)
    
    Returns:
        Configured logger
    
    TODO: Implement this function:
    1. Create a default format if format_string is None:
       "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    2. Create handlers list with StreamHandler for console
    3. If log_file is provided, add FileHandler
    4. Call logging.basicConfig with level, format, and handlers
    5. Return logging.getLogger("fundamentals")
    """
    # TODO: Implement
    pass


def log_operation(logger: logging.Logger, operation: str):
    """
    Decorator that logs function entry and exit.
    
    Args:
        logger: Logger to use
        operation: Name of the operation
    
    Example:
        @log_operation(logger, "data processing")
        def process_data():
            ...
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            logger.info(f"Starting {operation}")
            try:
                result = func(*args, **kwargs)
                logger.info(f"Completed {operation}")
                return result
            except Exception as e:
                logger.exception(f"Failed {operation}: {e}")
                raise
        return wrapper
    return decorator


# ============================================================
# TIMING - Complete the timer context manager
# ============================================================

@contextmanager
def timer(name: str = "Operation"):
    """
    Context manager for timing code blocks.
    
    Args:
        name: Name of the operation being timed
    
    Yields:
        dict with 'elapsed' key that will contain elapsed time after block
    
    Example:
        with timer("Data processing") as t:
            process_data()
        print(f"Took {t['elapsed']:.3f} seconds")
    
    TODO: Implement:
    1. Create a dict to store timing info
    2. Record start time using time.perf_counter()
    3. Yield the timing dict
    4. In finally block, calculate elapsed time and store in dict
    """
    # TODO: Implement
    pass


def measure_time(func: Callable[..., T]) -> Callable[..., tuple[T, float]]:
    """
    Decorator that measures function execution time.
    
    Returns a tuple of (result, elapsed_seconds).
    
    Example:
        @measure_time
        def slow_function():
            time.sleep(1)
            return "done"
        
        result, elapsed = slow_function()
        # result = "done", elapsed ≈ 1.0
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> tuple[T, float]:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        return result, elapsed
    return wrapper


# ============================================================
# RETRY LOGIC - Complete the retry decorator
# ============================================================

def retry(
    max_attempts: int = 3,
    exceptions: tuple = (Exception,),
    delay: float = 0.0,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorator that retries a function on failure.
    
    Args:
        max_attempts: Maximum number of attempts
        exceptions: Tuple of exceptions to catch and retry
        delay: Seconds to wait between retries
    
    Returns:
        Decorated function that retries on failure
    
    Raises:
        RetryExhaustedError: If all attempts fail
    
    Example:
        @retry(max_attempts=3, exceptions=(ConnectionError,))
        def fetch_data():
            ...
    
    TODO: Implement:
    1. Try calling the function up to max_attempts times
    2. If it succeeds, return the result
    3. If it fails with one of the specified exceptions:
       - Wait for delay seconds (use time.sleep)
       - Try again
    4. If all attempts fail, raise RetryExhaustedError
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            # TODO: Implement retry logic
            pass
        return wrapper
    return decorator


# ============================================================
# MAIN - Demo the functionality
# ============================================================

def main():
    """Demonstrate the robust code utilities."""
    print("=" * 50)
    print("Lesson 8: Robust Code Demo")
    print("=" * 50)
    
    # Setup logging
    logger = setup_logging(level=logging.DEBUG)
    
    # Test safe operations
    print("\n--- Safe Operations ---")
    print(f"safe_divide(10, 2) = {safe_divide(10, 2)}")
    print(f"safe_divide(10, 0) = {safe_divide(10, 0)}")
    print(f"safe_parse_int('42') = {safe_parse_int('42')}")
    print(f"safe_parse_int('not a number') = {safe_parse_int('not a number')}")
    
    # Test timing
    print("\n--- Timing ---")
    with timer("Sleep test") as t:
        time.sleep(0.1)
    print(f"Elapsed: {t.get('elapsed', 'N/A'):.3f}s")
    
    # Test validation
    print("\n--- Validation ---")
    try:
        validate_positive(-5, "test_value")
    except ValidationError as e:
        print(f"Caught ValidationError: {e}")
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()


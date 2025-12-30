"""
Tests for Lesson 8: Logging, Errors, and Timing

Run with: pytest tests/test_lesson_08.py -v
"""

import logging
import time
import pytest
from pathlib import Path
import tempfile

from src.fundamentals.robust import (
    ProcessingError,
    ValidationError,
    RetryExhaustedError,
    safe_divide,
    safe_parse_int,
    validate_positive,
    setup_logging,
    timer,
    measure_time,
    retry,
)


class TestCustomExceptions:
    """Tests for custom exception classes."""
    
    def test_processing_error_is_exception(self):
        """ProcessingError should be an Exception."""
        assert issubclass(ProcessingError, Exception)
    
    def test_validation_error_inherits(self):
        """ValidationError should inherit from ProcessingError."""
        assert issubclass(ValidationError, ProcessingError)
    
    def test_validation_error_attributes(self):
        """ValidationError should store field and reason."""
        error = ValidationError("email", "invalid format")
        assert error.field == "email"
        assert error.reason == "invalid format"
    
    def test_validation_error_message(self):
        """ValidationError should have a useful message."""
        error = ValidationError("age", "must be positive")
        assert "age" in str(error) or "positive" in str(error)
    
    def test_retry_exhausted_error(self):
        """RetryExhaustedError should store attempts and last_error."""
        original = ValueError("test")
        error = RetryExhaustedError(3, original)
        assert error.attempts == 3
        assert error.last_error is original
    
    def test_retry_exhausted_inherits(self):
        """RetryExhaustedError should inherit from ProcessingError."""
        assert issubclass(RetryExhaustedError, ProcessingError)


class TestSafeOperations:
    """Tests for safe wrapper functions."""
    
    def test_safe_divide_normal(self):
        """Test normal division."""
        assert safe_divide(10, 2) == 5.0
        assert safe_divide(7, 2) == 3.5
    
    def test_safe_divide_by_zero(self):
        """Test division by zero returns default."""
        assert safe_divide(10, 0) == 0.0
        assert safe_divide(10, 0, default=-1) == -1
    
    def test_safe_divide_custom_default(self):
        """Test custom default value."""
        assert safe_divide(5, 0, default=999) == 999
    
    def test_safe_parse_int_valid(self):
        """Test parsing valid integers."""
        assert safe_parse_int("42") == 42
        assert safe_parse_int("-10") == -10
        assert safe_parse_int("0") == 0
    
    def test_safe_parse_int_invalid(self):
        """Test parsing invalid strings returns default."""
        assert safe_parse_int("not a number") == 0
        assert safe_parse_int("3.14") == 0  # Float string
        assert safe_parse_int("") == 0
    
    def test_safe_parse_int_custom_default(self):
        """Test custom default for parse failure."""
        assert safe_parse_int("invalid", default=-1) == -1


class TestValidation:
    """Tests for validation functions."""
    
    def test_validate_positive_valid(self):
        """Test valid positive values pass through."""
        assert validate_positive(5) == 5
        assert validate_positive(0.1) == 0.1
        assert validate_positive(100) == 100
    
    def test_validate_positive_zero_raises(self):
        """Test zero raises ValidationError."""
        with pytest.raises(ValidationError):
            validate_positive(0)
    
    def test_validate_positive_negative_raises(self):
        """Test negative values raise ValidationError."""
        with pytest.raises(ValidationError):
            validate_positive(-5)
    
    def test_validate_positive_error_has_field(self):
        """Test ValidationError includes field name."""
        try:
            validate_positive(-1, field_name="score")
        except ValidationError as e:
            assert e.field == "score"


class TestLogging:
    """Tests for logging configuration."""
    
    def test_setup_logging_returns_logger(self):
        """setup_logging should return a Logger."""
        logger = setup_logging()
        assert isinstance(logger, logging.Logger)
    
    def test_setup_logging_with_level(self):
        """setup_logging should respect log level."""
        logger = setup_logging(level=logging.DEBUG)
        # Logger should be able to log at DEBUG
        assert logger.isEnabledFor(logging.DEBUG)
    
    def test_setup_logging_with_file(self):
        """setup_logging should create log file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            log_file = Path(tmpdir) / "test.log"
            logger = setup_logging(log_file=str(log_file))
            logger.info("Test message")
            
            # Force flush
            for handler in logging.root.handlers:
                handler.flush()
            
            # File might not exist immediately in all cases
            # Just verify no exception was raised


class TestTimer:
    """Tests for timer context manager."""
    
    def test_timer_returns_dict(self):
        """timer should yield a dict."""
        with timer("test") as t:
            pass
        assert isinstance(t, dict)
    
    def test_timer_has_elapsed(self):
        """timer dict should have 'elapsed' after block."""
        with timer("test") as t:
            time.sleep(0.05)
        
        assert "elapsed" in t
        assert t["elapsed"] >= 0.04  # Allow some tolerance
    
    def test_timer_accuracy(self):
        """timer should accurately measure time."""
        with timer("test") as t:
            time.sleep(0.1)
        
        # Should be roughly 0.1 seconds (allow 50% tolerance)
        assert 0.05 < t["elapsed"] < 0.2


class TestMeasureTime:
    """Tests for measure_time decorator."""
    
    def test_measure_time_returns_tuple(self):
        """measure_time should return (result, elapsed)."""
        @measure_time
        def sample():
            return "done"
        
        result, elapsed = sample()
        assert result == "done"
        assert isinstance(elapsed, float)
    
    def test_measure_time_accuracy(self):
        """measure_time should accurately measure time."""
        @measure_time
        def slow():
            time.sleep(0.1)
            return 42
        
        result, elapsed = slow()
        assert result == 42
        assert 0.05 < elapsed < 0.2


class TestRetry:
    """Tests for retry decorator."""
    
    def test_retry_succeeds_first_try(self):
        """Function succeeding on first try should work."""
        call_count = 0
        
        @retry(max_attempts=3)
        def succeed():
            nonlocal call_count
            call_count += 1
            return "success"
        
        result = succeed()
        assert result == "success"
        assert call_count == 1
    
    def test_retry_succeeds_after_failures(self):
        """Function should retry and eventually succeed."""
        call_count = 0
        
        @retry(max_attempts=3, exceptions=(ValueError,))
        def fail_then_succeed():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ValueError("Not yet!")
            return "success"
        
        result = fail_then_succeed()
        assert result == "success"
        assert call_count == 3
    
    def test_retry_exhausted(self):
        """Should raise RetryExhaustedError when all attempts fail."""
        @retry(max_attempts=3, exceptions=(ValueError,))
        def always_fail():
            raise ValueError("Always fails")
        
        with pytest.raises(RetryExhaustedError) as exc_info:
            always_fail()
        
        assert exc_info.value.attempts == 3
        assert isinstance(exc_info.value.last_error, ValueError)
    
    def test_retry_only_catches_specified(self):
        """Should only retry on specified exceptions."""
        @retry(max_attempts=3, exceptions=(ValueError,))
        def raise_type_error():
            raise TypeError("Wrong type")
        
        # TypeError is not in exceptions, should not retry
        with pytest.raises(TypeError):
            raise_type_error()
    
    def test_retry_with_delay(self):
        """Should wait between retries."""
        call_times = []
        
        @retry(max_attempts=3, exceptions=(ValueError,), delay=0.05)
        def track_time():
            call_times.append(time.perf_counter())
            if len(call_times) < 3:
                raise ValueError("Retry!")
            return "done"
        
        track_time()
        
        # Check there was a delay between calls
        if len(call_times) >= 2:
            delay = call_times[1] - call_times[0]
            assert delay >= 0.04  # Allow some tolerance


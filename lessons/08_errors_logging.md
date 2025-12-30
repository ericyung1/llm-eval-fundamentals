# Lesson 8: Logging, Errors, and Timing

> ⏱️ Estimated time: 2 hours

---

## 🎯 What You'll Learn

By the end of this lesson, you will be able to:
- Handle errors with try/except
- Create custom exceptions
- Use Python's logging module
- Measure execution time with perf_counter

---

## 📚 Core Concepts

### Why Error Handling Matters

LLM evaluations can fail in many ways:
- API rate limits
- Network timeouts
- Invalid model outputs
- Malformed data

Proper error handling makes your code **robust** and **debuggable**.

### try/except Basics

```python
try:
    result = risky_operation()
except SomeError as e:
    print(f"Error occurred: {e}")
    # Handle the error
```

#### Catching Specific Exceptions

```python
try:
    data = json.loads(text)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    # Catch-all (use sparingly)
    print(f"Unexpected error: {e}")
```

#### The Full Pattern

```python
try:
    # Code that might fail
    result = process_data()
except ValueError as e:
    # Handle specific error
    log_error(e)
    result = default_value
else:
    # Runs if NO exception (optional)
    save_result(result)
finally:
    # ALWAYS runs, even if exception (optional)
    cleanup()
```

### Raising Exceptions

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Re-raising
try:
    risky_operation()
except SomeError:
    log_error()
    raise  # Re-raise the same exception
```

### Custom Exceptions

Create your own exception types for clarity:

```python
class EvaluationError(Exception):
    """Base exception for evaluation errors."""
    pass

class ModelTimeoutError(EvaluationError):
    """Raised when model response times out."""
    pass

class InvalidResponseError(EvaluationError):
    """Raised when model output is invalid."""
    def __init__(self, response: str, reason: str):
        self.response = response
        self.reason = reason
        super().__init__(f"Invalid response: {reason}")

# Usage
def validate_response(response):
    if not response:
        raise InvalidResponseError(response, "Empty response")
```

### Python Logging

The `logging` module is better than `print()` for production code:

```python
import logging

# Basic setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Log messages at different levels
logger.debug("Detailed info for debugging")
logger.info("General information")
logger.warning("Something unexpected")
logger.error("An error occurred")
logger.critical("Critical failure!")
```

#### Log Levels

| Level | Value | When to Use |
|-------|-------|-------------|
| DEBUG | 10 | Detailed diagnostic info |
| INFO | 20 | General operational info |
| WARNING | 30 | Something unexpected but not critical |
| ERROR | 40 | An error that needs attention |
| CRITICAL | 50 | System is failing |

#### Configuring Logging

```python
import logging

# Configure with format and file output
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()  # Also print to console
    ]
)

logger = logging.getLogger(__name__)
```

#### Logging Exceptions

```python
try:
    process_data()
except Exception as e:
    logger.exception("Failed to process data")
    # This logs the full traceback!
```

### Measuring Time

Use `time.perf_counter()` for accurate timing:

```python
import time

start = time.perf_counter()
result = do_expensive_operation()
elapsed = time.perf_counter() - start

print(f"Operation took {elapsed:.3f} seconds")
```

#### Context Manager for Timing

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(name: str):
    """Context manager for timing code blocks."""
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{name} took {elapsed:.3f}s")

# Usage
with timer("Data processing"):
    process_large_dataset()
```

---

## ✋ Do This Now

You'll implement error handling, logging, and timing utilities.

### Task 1: Review the Starter Code

```bash
cat src/fundamentals/robust.py
```

### Task 2: Complete the Functions

Implement the TODO sections in `src/fundamentals/robust.py`:
- Custom exception classes
- Safe wrapper functions
- Logging configuration
- Timer context manager

### Task 3: Test Your Implementation

```bash
pytest tests/test_lesson_08.py -v
```

---

## 🧪 Quiz/Checkpoint

When you've completed all tasks, run:

```bash
make check 8
```

The tests verify:
- ✅ Custom exceptions work correctly
- ✅ safe_divide handles errors properly
- ✅ Logging is configured correctly
- ✅ Timer context manager works
- ✅ retry decorator handles failures

---

## ⚠️ Common Mistakes

### 1. Catching Too Broadly
```python
# Bad - hides bugs!
try:
    result = do_something()
except:  # Catches EVERYTHING including KeyboardInterrupt
    pass

# Better - be specific
try:
    result = do_something()
except ValueError:
    handle_value_error()
```

### 2. Silent Failures
```python
# Bad - error disappears
try:
    result = process()
except Exception:
    pass  # Silent failure!

# Better - at least log it
try:
    result = process()
except Exception:
    logger.exception("Processing failed")
    result = None
```

### 3. Using print() Instead of logging
```python
# Bad - can't control output level
print("Error:", e)

# Good - controllable
logger.error(f"Error: {e}")
```

### 4. Wrong Timer
```python
# Wrong - less precise
import time
start = time.time()  # Wall clock time, affected by system

# Right - monotonic, precise
start = time.perf_counter()
```

---

## 📖 Quick Reference

### Exception Handling

```python
try:
    risky_code()
except SpecificError as e:
    handle_error(e)
except (TypeError, ValueError):
    handle_multiple()
else:
    on_success()
finally:
    always_run()
```

### Logging Setup

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

logger.info("Message")
logger.error("Error")
logger.exception("With traceback")
```

### Timing

```python
import time

start = time.perf_counter()
# ... code ...
elapsed = time.perf_counter() - start
```

---

## ✅ Before Moving On

You should be able to:
- [ ] Use try/except/finally correctly
- [ ] Create custom exception classes
- [ ] Configure and use logging
- [ ] Measure execution time accurately
- [ ] Know when to catch vs. raise exceptions

---

## 🎯 Next Lesson

Continue to **Lesson 9: Code Quality Basics**:
```bash
make lesson 9
```


# Lesson 9: Code Quality Basics

> ⏱️ Estimated time: 2 hours

---

## 🎯 What You'll Learn

By the end of this lesson, you will be able to:
- Add type hints to Python code
- Write proper docstrings
- Understand why type hints matter
- Use basic code quality patterns

---

## 📚 Core Concepts

### Why Code Quality?

Good code is:
- **Readable**: Others (and future you) can understand it
- **Maintainable**: Easy to change without breaking things
- **Correct**: Does what it's supposed to do

Type hints and docstrings are the foundation of quality Python code.

### Type Hints

Type hints tell Python (and developers) what types are expected:

```python
# Without hints - unclear
def greet(name):
    return f"Hello, {name}"

# With hints - clear!
def greet(name: str) -> str:
    return f"Hello, {name}"
```

Python doesn't enforce types at runtime, but:
- IDEs show errors and autocomplete
- Type checkers (mypy) catch bugs
- Documentation is built-in

#### Basic Type Hints

```python
# Simple types
name: str = "Alice"
age: int = 30
height: float = 5.9
is_active: bool = True

# Function parameters and return
def add(a: int, b: int) -> int:
    return a + b

# None return
def log(message: str) -> None:
    print(message)
```

#### Collection Types

```python
# Lists
names: list[str] = ["Alice", "Bob"]
scores: list[int] = [95, 87, 92]

# Dicts
user: dict[str, str] = {"name": "Alice", "email": "a@b.com"}
counts: dict[str, int] = {"apples": 3, "oranges": 5}

# Sets
unique_ids: set[int] = {1, 2, 3}

# Tuples (fixed length)
point: tuple[int, int] = (10, 20)
record: tuple[str, int, bool] = ("Alice", 30, True)
```

#### Optional and Union

```python
from typing import Optional, Union

# Optional - might be None
def find_user(id: int) -> Optional[dict]:
    """Return user dict or None if not found."""
    ...

# Equivalent to:
def find_user(id: int) -> dict | None:
    ...

# Union - one of several types
def process(data: Union[str, bytes]) -> str:
    ...

# Modern syntax (Python 3.10+)
def process(data: str | bytes) -> str:
    ...
```

#### Type Aliases

```python
from typing import TypeAlias

# Create meaningful names for complex types
UserId: TypeAlias = int
UserRecord: TypeAlias = dict[str, str | int]
UserList: TypeAlias = list[UserRecord]

def get_users() -> UserList:
    ...
```

### Docstrings

Docstrings document what code does:

```python
def calculate_score(correct: int, total: int) -> float:
    """
    Calculate percentage score.
    
    Args:
        correct: Number of correct answers
        total: Total number of questions
    
    Returns:
        Percentage score from 0.0 to 100.0
    
    Raises:
        ValueError: If total is zero
        ValueError: If correct > total
    
    Example:
        >>> calculate_score(8, 10)
        80.0
    """
    if total == 0:
        raise ValueError("Total cannot be zero")
    if correct > total:
        raise ValueError("Correct cannot exceed total")
    return (correct / total) * 100
```

#### Docstring Styles

**Google Style** (recommended):
```python
def function(arg1: str, arg2: int) -> bool:
    """Short description.
    
    Longer description if needed.
    
    Args:
        arg1: Description of arg1
        arg2: Description of arg2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When something is wrong
    """
```

**NumPy Style**:
```python
def function(arg1, arg2):
    """
    Short description.
    
    Parameters
    ----------
    arg1 : str
        Description of arg1
    arg2 : int
        Description of arg2
    
    Returns
    -------
    bool
        Description of return value
    """
```

### Class Documentation

```python
class DataProcessor:
    """
    Process and transform data records.
    
    This class handles reading, transforming, and writing data
    in various formats.
    
    Attributes:
        input_format: Format of input data ("json" or "csv")
        output_format: Format of output data ("json" or "csv")
    
    Example:
        processor = DataProcessor("json", "csv")
        processor.process("input.json", "output.csv")
    """
    
    def __init__(self, input_format: str, output_format: str) -> None:
        """
        Initialize the processor.
        
        Args:
            input_format: Format of input files
            output_format: Format of output files
        """
        self.input_format = input_format
        self.output_format = output_format
```

---

## ✋ Do This Now

You'll add type hints and docstrings to existing code.

### Task 1: Review the Starter Code

```bash
cat src/fundamentals/quality.py
```

### Task 2: Add Type Hints

Add type hints to all functions and methods in the file.

### Task 3: Add Docstrings

Add proper docstrings (Google style) to all functions and classes.

### Task 4: Run the Tests

```bash
pytest tests/test_lesson_09.py -v
```

---

## 🧪 Quiz/Checkpoint

When you've completed all tasks, run:

```bash
make check 9
```

The tests verify:
- ✅ All functions have type hints
- ✅ All functions have docstrings
- ✅ Type hints are correct
- ✅ Docstrings include Args and Returns sections

---

## ⚠️ Common Mistakes

### 1. Forgetting Return Type
```python
# Bad - no return type
def greet(name: str):
    return f"Hello, {name}"

# Good
def greet(name: str) -> str:
    return f"Hello, {name}"
```

### 2. Wrong Collection Type
```python
# Bad - list contains mixed types
items: list[int] = [1, "two", 3]

# Good - use Union if mixed
items: list[int | str] = [1, "two", 3]
```

### 3. Missing None Return
```python
# Bad - returns None but not hinted
def log(message: str):
    print(message)

# Good
def log(message: str) -> None:
    print(message)
```

### 4. Docstring Just Repeats Name
```python
# Bad
def calculate_total(items):
    """Calculate total."""  # Not helpful!

# Good
def calculate_total(items: list[float]) -> float:
    """Sum all item values and return the total."""
```

---

## 📖 Quick Reference

### Common Type Hints

```python
# Primitives
x: int
x: float
x: str
x: bool
x: bytes

# Collections
x: list[T]
x: dict[K, V]
x: set[T]
x: tuple[T, ...]  # Variable length
x: tuple[T, U, V]  # Fixed length

# Optional/Union
x: T | None
x: T | U | V

# Callable
from typing import Callable
x: Callable[[int, str], bool]  # Takes int, str; returns bool

# Any (escape hatch)
from typing import Any
x: Any
```

### Docstring Template

```python
def function(param1: Type1, param2: Type2) -> ReturnType:
    """
    Brief description of what the function does.
    
    More details if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of what is returned
    
    Raises:
        ErrorType: When this error occurs
    
    Example:
        >>> function(arg1, arg2)
        expected_result
    """
```

---

## ✅ Before Moving On

You should be able to:
- [ ] Add type hints to functions and variables
- [ ] Write comprehensive docstrings
- [ ] Use Optional and Union types
- [ ] Document exceptions in docstrings

---

## 🎯 Next Lesson

Continue to **Lesson 10: Mini Capstone**:
```bash
make lesson 10
```


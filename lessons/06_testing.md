# Lesson 6: Testing Fundamentals with pytest

> ⏱️ Estimated time: 2-3 hours

---

## 🎯 What You'll Learn

By the end of this lesson, you will be able to:
- Write test functions with pytest
- Use assertions effectively
- Create and use fixtures
- Understand test organization

---

## 📚 Core Concepts

### Why Testing Matters

> "LLM evaluations ARE tests."

When you build an LLM evaluation system, you're essentially creating automated tests that check if model outputs meet your criteria. Understanding testing fundamentals is essential.

Benefits of testing:
- **Catch bugs early** - Before users do
- **Enable refactoring** - Change code confidently
- **Document behavior** - Tests show how code should work
- **Save time** - Automated tests run in seconds

### pytest Basics

pytest is Python's most popular testing framework. It's simple and powerful.

#### Your First Test

```python
# test_example.py

def test_addition():
    """Test that addition works."""
    assert 1 + 1 == 2

def test_string_upper():
    """Test string uppercase."""
    assert "hello".upper() == "HELLO"
```

Run with:
```bash
pytest test_example.py -v
```

#### Naming Conventions

- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_*`
- Test classes: `Test*` (optional)

pytest finds these automatically!

### Assertions

The `assert` statement is your main tool. If the expression is `False`, the test fails.

```python
# Basic assertions
assert value == expected
assert value != unexpected
assert value is True
assert value is False
assert value is None
assert value is not None

# Comparisons
assert value > 0
assert value <= 100
assert len(my_list) == 3

# Containment
assert "hello" in text
assert key in my_dict
assert item not in forbidden_list

# Type checking
assert isinstance(value, str)
assert isinstance(value, (int, float))
```

#### Helpful Error Messages

```python
# Without message - less helpful on failure
assert result == expected

# With message - clearer on failure
assert result == expected, f"Expected {expected}, got {result}"
```

### Testing Exceptions

Use `pytest.raises` to verify code raises expected exceptions:

```python
import pytest

def test_divide_by_zero():
    """Test that dividing by zero raises an error."""
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0

def test_invalid_input():
    """Test that invalid input raises ValueError."""
    with pytest.raises(ValueError, match="must be positive"):
        my_function(-1)
```

### Fixtures

Fixtures provide reusable test setup. They're like "before each test" hooks.

```python
import pytest

@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {"name": "Alice", "age": 30}

def test_has_name(sample_data):
    """Test that data has a name."""
    assert "name" in sample_data

def test_name_is_string(sample_data):
    """Test that name is a string."""
    assert isinstance(sample_data["name"], str)
```

#### Built-in Fixtures

```python
@pytest.fixture
def tmp_path(tmp_path):
    """tmp_path is a built-in fixture - provides a temp directory."""
    file = tmp_path / "test.txt"
    file.write_text("Hello")
    return file
```

### Test Organization with Classes

Group related tests in classes:

```python
class TestCalculator:
    """Tests for calculator functions."""
    
    def test_add(self):
        assert add(2, 3) == 5
    
    def test_subtract(self):
        assert subtract(5, 3) == 2
    
    def test_multiply(self):
        assert multiply(2, 3) == 6
```

### Parametrized Tests

Run the same test with different inputs:

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
    ("Python", "PYTHON"),
])
def test_uppercase(input, expected):
    assert input.upper() == expected

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

---

## ✋ Do This Now

You'll write tests for functions that already exist.

### Task 1: Review the Code to Test

Look at the `calculator` module that's provided:

```bash
cat src/fundamentals/calculator.py
```

### Task 2: Write Your Tests

Open `tests/test_lesson_06.py` and complete the TODO sections.

You need to write at least 3 tests for each function:
- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)`
- `power(base, exp)`

### Task 3: Use Fixtures

Create a fixture for test data and use it in your tests.

### Task 4: Test Exception Handling

Write tests that verify `divide(a, 0)` raises `ZeroDivisionError`.

### Task 5: Run Your Tests

```bash
source venv/bin/activate
pytest tests/test_lesson_06.py -v
```

---

## 🧪 Quiz/Checkpoint

When you've completed all tasks, run:

```bash
make check 6
```

The autograder checks:
- ✅ You have at least 15 test functions total
- ✅ Tests cover all calculator functions
- ✅ At least one test uses a fixture
- ✅ At least one test checks for exceptions
- ✅ All tests pass

---

## ⚠️ Common Mistakes

### 1. Forgetting to Return in Fixtures
```python
# Wrong - fixture returns None!
@pytest.fixture
def my_data():
    data = {"key": "value"}

# Right
@pytest.fixture
def my_data():
    data = {"key": "value"}
    return data
```

### 2. Using `==` Instead of `is` for Booleans/None
```python
# Less precise
assert result == True
assert result == None

# More precise
assert result is True
assert result is None
```

### 3. Not Testing Edge Cases
```python
# Only testing happy path
def test_add():
    assert add(2, 3) == 5

# Better - test edge cases too
def test_add_zero():
    assert add(0, 5) == 5

def test_add_negative():
    assert add(-3, 3) == 0
```

### 4. Tests That Depend on Each Other
```python
# Wrong - tests should be independent
class TestBad:
    result = None
    
    def test_a(self):
        self.result = compute()
    
    def test_b(self):
        assert self.result == expected  # Depends on test_a!
```

### 5. Not Running Tests Often
Run tests frequently—after every change!

---

## 📖 Quick Reference

### Running Tests

```bash
pytest                          # Run all tests
pytest test_file.py             # Run one file
pytest test_file.py::test_func  # Run one function
pytest -v                       # Verbose output
pytest -x                       # Stop on first failure
pytest -k "pattern"             # Run tests matching pattern
pytest --tb=short               # Shorter tracebacks
```

### Common Assertions

```python
assert x == y           # Equality
assert x != y           # Inequality
assert x is True        # Boolean true
assert x is None        # None check
assert x in container   # Containment
assert len(x) == n      # Length check
```

### Fixture Template

```python
@pytest.fixture
def my_fixture():
    # Setup
    resource = create_resource()
    yield resource
    # Teardown (optional)
    resource.cleanup()
```

---

## ✅ Before Moving On

You should be able to:
- [ ] Write test functions with assert
- [ ] Create and use fixtures
- [ ] Test for expected exceptions
- [ ] Run specific tests with pytest
- [ ] Understand test naming conventions

---

## 🎯 Next Lesson

Continue to **Lesson 7: CLI Basics with argparse**:
```bash
make lesson 7
```


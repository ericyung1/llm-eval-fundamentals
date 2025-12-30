# Lesson 3: Python Basics

> ⏱️ Estimated time: 2-3 hours

---

## 🎯 What You'll Learn

By the end of this lesson, you will be able to:
- Run Python scripts from the terminal
- Define and call functions with parameters
- Organize code into modules and import them
- Use the `if __name__ == "__main__"` pattern

---

## 📚 Core Concepts

### Running Python

```bash
# Run a script
python3 script.py

# Run with arguments
python3 script.py arg1 arg2

# Interactive mode (REPL)
python3
>>> print("Hello")
>>> exit()
```

### Variables and Types

Python is dynamically typed—you don't declare types explicitly (but you can add hints).

```python
# Basic types
name = "Alice"           # str (string)
age = 30                 # int (integer)
height = 5.9             # float (decimal)
is_student = True        # bool (boolean)
items = [1, 2, 3]        # list
person = {"name": "Bob"} # dict (dictionary)
```

### Functions

Functions encapsulate reusable logic.

```python
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

# Call the function
message = greet("World")
print(message)  # Hello, World!
```

#### Parameters and Return Values

```python
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add(3, 4)  # result = 7

# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")              # "Hello, Alice!"
greet("Alice", "Hi")        # "Hi, Alice!"

# Keyword arguments
greet(greeting="Hey", name="Bob")  # "Hey, Bob!"
```

### Modules and Imports

A **module** is just a Python file. You can import and use code from other files.

```python
# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

```python
# main.py
import math_utils

result = math_utils.add(2, 3)  # 5

# Or import specific functions
from math_utils import add, multiply

result = add(2, 3)  # 5
```

### The `__name__` Pattern

When Python runs a file directly, `__name__` equals `"__main__"`.
When a file is imported, `__name__` equals the module name.

```python
# my_module.py
def helper():
    return "I help!"

def main():
    print("Running as main program")
    print(helper())

if __name__ == "__main__":
    main()
```

This pattern lets your module be:
- **Run directly**: `python3 my_module.py` → runs `main()`
- **Imported**: `import my_module` → doesn't run `main()`

---

## ✋ Do This Now

You'll complete functions in a starter file. The tests will verify your work.

### Task 1: Open the Starter File

The starter code is at `src/fundamentals/basics.py`. Open it in your editor.

```bash
# From the course root directory
cat src/fundamentals/basics.py
```

### Task 2: Complete the Functions

Edit `src/fundamentals/basics.py` and complete each TODO:

```python
# src/fundamentals/basics.py

def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    # TODO: Implement this function
    pass


def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers and return the result."""
    # TODO: Implement this function
    pass


def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    # TODO: Implement this function
    pass


def reverse_string(s: str) -> str:
    """Return the reverse of a string."""
    # TODO: Implement this function
    # Hint: Use string slicing s[::-1]
    pass


def count_vowels(s: str) -> int:
    """Count the number of vowels (a, e, i, o, u) in a string."""
    # TODO: Implement this function
    # Hint: Use a loop and check if each character is in "aeiouAEIOU"
    pass


def fizzbuzz(n: int) -> str:
    """
    Return "Fizz" if n is divisible by 3,
    "Buzz" if divisible by 5,
    "FizzBuzz" if divisible by both,
    otherwise return the number as a string.
    """
    # TODO: Implement this function
    pass
```

### Task 3: Test Locally

After implementing, test your functions:

```bash
# Activate venv if not already active
source venv/bin/activate

# Run the specific test file
pytest tests/test_lesson_03.py -v
```

### Task 4: Create a Runnable Script

Add a `main()` function and the `if __name__ == "__main__"` block to test your functions:

```python
# Add at the bottom of src/fundamentals/basics.py

def main():
    """Demonstrate the functions."""
    print("Testing add_numbers:", add_numbers(3, 4))
    print("Testing multiply_numbers:", multiply_numbers(3, 4))
    print("Testing is_even(4):", is_even(4))
    print("Testing is_even(5):", is_even(5))
    print("Testing reverse_string:", reverse_string("hello"))
    print("Testing count_vowels:", count_vowels("hello world"))
    print("Testing fizzbuzz(15):", fizzbuzz(15))
    print("Testing fizzbuzz(7):", fizzbuzz(7))


if __name__ == "__main__":
    main()
```

Run it:
```bash
python3 src/fundamentals/basics.py
```

---

## 🧪 Quiz/Checkpoint

When you've completed all tasks, run:

```bash
make check 3
```

The checkpoint (pytest tests) will verify:
- ✅ `add_numbers(3, 4)` returns `7`
- ✅ `multiply_numbers(3, 4)` returns `12`
- ✅ `is_even(4)` returns `True`, `is_even(5)` returns `False`
- ✅ `reverse_string("hello")` returns `"olleh"`
- ✅ `count_vowels("hello")` returns `2`
- ✅ `fizzbuzz` returns correct values

---

## ⚠️ Common Mistakes

### 1. Forgetting to Return
```python
# Wrong
def add(a, b):
    a + b  # This doesn't return anything!

# Right
def add(a, b):
    return a + b
```

### 2. Indentation Errors
Python uses indentation for blocks. Be consistent (use 4 spaces).

```python
# Wrong
def greet():
print("Hello")  # IndentationError!

# Right
def greet():
    print("Hello")
```

### 3. Modifying vs Returning
```python
# This doesn't modify the original
def double(x):
    x = x * 2  # Only changes local variable

# This returns a new value
def double(x):
    return x * 2
```

### 4. Off-by-One in Loops
```python
# range(5) gives: 0, 1, 2, 3, 4 (not 5!)
for i in range(5):
    print(i)
```

---

## 📖 Quick Reference

### Function Syntax
```python
def function_name(param1, param2="default"):
    """Docstring explains what the function does."""
    # Function body
    return result
```

### Common Operations
```python
# String operations
s = "hello"
s.upper()        # "HELLO"
s.lower()        # "hello"
len(s)           # 5
s[::-1]          # "olleh" (reverse)
"e" in s         # True

# List operations
lst = [1, 2, 3]
lst.append(4)    # [1, 2, 3, 4]
len(lst)         # 4
lst[0]           # 1 (first element)
lst[-1]          # 4 (last element)

# Dictionary operations
d = {"key": "value"}
d["key"]         # "value"
d.get("key")     # "value" (safer)
d["new"] = 123   # Add new key
```

### Operators
```python
# Arithmetic
+ - * /          # Basic math
//               # Integer division
%                # Modulo (remainder)
**               # Power

# Comparison
== !=            # Equal, not equal
< > <= >=        # Less, greater

# Logical
and or not       # Boolean operators
```

---

## ✅ Before Moving On

You should be able to:
- [ ] Run Python scripts from the terminal
- [ ] Define functions with parameters and return values
- [ ] Use the `if __name__ == "__main__"` pattern
- [ ] All tests pass for this lesson

---

## 🎯 Next Lesson

Continue to **Lesson 4: Data Formats** to learn JSON and CSV:
```bash
make lesson 4
```


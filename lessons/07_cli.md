# Lesson 7: CLI Basics with argparse

> ⏱️ Estimated time: 2 hours

---

## 🎯 What You'll Learn

By the end of this lesson, you will be able to:
- Create command-line interfaces with argparse
- Define positional and optional arguments
- Add help text and validation
- Handle subcommands

---

## 📚 Core Concepts

### Why CLI Tools?

Most developer tools run from the command line:
- `git commit -m "message"`
- `pytest --verbose`
- `python script.py --input data.json`

LLM evaluation tools typically work the same way:
- `eval run --model gpt-4 --dataset test.jsonl`
- `eval report --output results.csv`

### argparse Basics

`argparse` is Python's built-in library for creating CLI tools.

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="My CLI tool")
    parser.add_argument("name", help="Your name")
    parser.add_argument("--greeting", default="Hello", help="Greeting to use")
    
    args = parser.parse_args()
    print(f"{args.greeting}, {args.name}!")

if __name__ == "__main__":
    main()
```

Usage:
```bash
python greet.py Alice
# Hello, Alice!

python greet.py Alice --greeting "Hi"
# Hi, Alice!

python greet.py --help
# Shows help text
```

### Argument Types

#### Positional Arguments (Required)
```python
parser.add_argument("filename", help="Input file")
# Usage: python script.py input.txt
```

#### Optional Arguments (Flags)
```python
# With value
parser.add_argument("--output", "-o", help="Output file")
# Usage: python script.py --output result.txt

# Boolean flag (store True when present)
parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose mode")
# Usage: python script.py --verbose

# With default value
parser.add_argument("--count", type=int, default=10, help="Number of items")
```

#### Type Conversion
```python
parser.add_argument("--count", type=int, help="Integer value")
parser.add_argument("--rate", type=float, help="Float value")
parser.add_argument("--file", type=argparse.FileType('r'), help="File to read")
```

#### Choices (Restricted Values)
```python
parser.add_argument("--format", choices=["json", "csv", "xml"], help="Output format")
# Only accepts these specific values
```

#### Required Optional Arguments
```python
parser.add_argument("--api-key", required=True, help="API key (required)")
```

### Complete Example

```python
#!/usr/bin/env python3
"""Word counter CLI tool."""

import argparse
from pathlib import Path


def count_words(filepath: Path) -> dict:
    """Count words in a file."""
    text = filepath.read_text()
    words = text.split()
    lines = text.count('\n') + 1
    chars = len(text)
    return {"words": len(words), "lines": lines, "chars": chars}


def main():
    parser = argparse.ArgumentParser(
        description="Count words, lines, and characters in a file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  wordcount myfile.txt
  wordcount myfile.txt --format json
  wordcount myfile.txt -l  # lines only
        """
    )
    
    # Positional argument
    parser.add_argument(
        "file",
        type=Path,
        help="File to analyze"
    )
    
    # Optional arguments
    parser.add_argument(
        "--format", "-f",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)"
    )
    
    parser.add_argument(
        "--lines", "-l",
        action="store_true",
        help="Show only line count"
    )
    
    parser.add_argument(
        "--words", "-w",
        action="store_true",
        help="Show only word count"
    )
    
    args = parser.parse_args()
    
    # Validate file exists
    if not args.file.exists():
        parser.error(f"File not found: {args.file}")
    
    # Process
    counts = count_words(args.file)
    
    # Output
    if args.lines:
        print(counts["lines"])
    elif args.words:
        print(counts["words"])
    elif args.format == "json":
        import json
        print(json.dumps(counts, indent=2))
    else:
        print(f"Lines: {counts['lines']}")
        print(f"Words: {counts['words']}")
        print(f"Chars: {counts['chars']}")


if __name__ == "__main__":
    main()
```

### Subcommands

For complex tools, use subcommands (like `git commit`, `git push`):

```python
parser = argparse.ArgumentParser(description="Multi-command tool")
subparsers = parser.add_subparsers(dest="command", help="Available commands")

# 'run' subcommand
run_parser = subparsers.add_parser("run", help="Run something")
run_parser.add_argument("--fast", action="store_true")

# 'config' subcommand
config_parser = subparsers.add_parser("config", help="Configure settings")
config_parser.add_argument("key", help="Config key")
config_parser.add_argument("value", help="Config value")

args = parser.parse_args()

if args.command == "run":
    print(f"Running (fast={args.fast})")
elif args.command == "config":
    print(f"Setting {args.key} = {args.value}")
```

---

## ✋ Do This Now

You'll build a text file analyzer CLI tool.

### Task 1: Review the Starter Code

```bash
cat src/fundamentals/cli_tool.py
```

### Task 2: Complete the CLI Tool

Implement the TODO sections in `src/fundamentals/cli_tool.py`.

The tool should:
- Take a file path as input
- Support `--format` (text or json)
- Support `--uppercase` flag to convert output to uppercase
- Support `--lines` to limit output lines
- Have proper help text

### Task 3: Test Your CLI

```bash
# Create a test file
echo "Hello World" > /tmp/test.txt
echo "This is a test" >> /tmp/test.txt

# Run your CLI
python src/fundamentals/cli_tool.py /tmp/test.txt
python src/fundamentals/cli_tool.py /tmp/test.txt --format json
python src/fundamentals/cli_tool.py /tmp/test.txt --uppercase
python src/fundamentals/cli_tool.py --help
```

### Task 4: Run the Tests

```bash
pytest tests/test_lesson_07.py -v
```

---

## 🧪 Quiz/Checkpoint

When you've completed all tasks, run:

```bash
make check 7
```

The tests verify:
- ✅ CLI has required arguments
- ✅ `--help` works
- ✅ Default behavior works
- ✅ `--format json` outputs valid JSON
- ✅ `--uppercase` converts output
- ✅ Error handling for missing files

---

## ⚠️ Common Mistakes

### 1. Forgetting to Call parse_args()
```python
# Wrong
args = parser  # This is the parser, not the args!

# Right
args = parser.parse_args()
```

### 2. Using Wrong Type
```python
# Wrong - "5" is a string
parser.add_argument("--count")
# args.count is "5", not 5

# Right - convert to int
parser.add_argument("--count", type=int)
# args.count is 5
```

### 3. Positional After Optional
```python
# Confusing
parser.add_argument("--flag")
parser.add_argument("input")
# Works, but hard to use

# Better - positionals first
parser.add_argument("input")
parser.add_argument("--flag")
```

### 4. Missing Help Text
```python
# Bad - no help
parser.add_argument("--output")

# Good - helpful
parser.add_argument("--output", "-o", help="Output file path")
```

---

## 📖 Quick Reference

### Argument Types

| Pattern | Usage | Example |
|---------|-------|---------|
| Positional | `add_argument("name")` | `script.py value` |
| Optional | `add_argument("--name")` | `script.py --name value` |
| Short form | `add_argument("-n", "--name")` | `script.py -n value` |
| Flag | `add_argument("--verbose", action="store_true")` | `script.py --verbose` |
| Choices | `add_argument("--type", choices=["a","b"])` | `script.py --type a` |
| Required | `add_argument("--key", required=True)` | `script.py --key val` |

### Common Options

```python
add_argument(
    "--option",
    "-o",                    # Short form
    type=int,                # Convert to type
    default=10,              # Default value
    required=True,           # Must be provided
    choices=["a", "b"],      # Allowed values
    help="Description",      # Help text
    action="store_true",     # Boolean flag
    nargs="+",              # Multiple values
)
```

---

## ✅ Before Moving On

You should be able to:
- [ ] Create a CLI with argparse
- [ ] Add positional and optional arguments
- [ ] Use type conversion and choices
- [ ] Write helpful help text
- [ ] Handle errors gracefully

---

## 🎯 Next Lesson

Continue to **Lesson 8: Logging, Errors, and Timing**:
```bash
make lesson 8
```


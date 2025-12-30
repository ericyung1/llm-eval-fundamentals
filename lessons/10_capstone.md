# Lesson 10: Mini Capstone

> ⏱️ Estimated time: 3-4 hours

---

## 🎯 What You'll Build

You'll create a **Data Processing CLI** that:
- Reads JSONL files
- Applies transformations
- Writes output in JSON or CSV format
- Has comprehensive tests
- Uses proper logging and error handling

This integrates ALL skills from the course!

---

## 📋 Requirements

### The CLI Tool

Create a command-line tool called `dataproc` that:

```bash
# Basic usage
python dataproc.py input.jsonl output.json

# With transformations
python dataproc.py input.jsonl output.csv --transform uppercase
python dataproc.py input.jsonl output.json --transform filter --filter-key status --filter-value active

# With options
python dataproc.py input.jsonl output.json --verbose --limit 100
```

### Input Format (JSONL)

```jsonl
{"id": 1, "name": "Alice", "status": "active"}
{"id": 2, "name": "Bob", "status": "inactive"}
{"id": 3, "name": "Charlie", "status": "active"}
```

### Transformations

1. **none** (default): Pass through unchanged
2. **uppercase**: Convert all string values to uppercase
3. **filter**: Keep only records matching filter criteria
4. **add_timestamp**: Add a `processed_at` field with current timestamp

### Output Formats

- `.json` extension → JSON array
- `.csv` extension → CSV file with headers
- `.jsonl` extension → JSONL file

---

## 📚 Skills You'll Use

| Skill | From Lesson |
|-------|-------------|
| File I/O | Lesson 1 (Terminal) |
| Python functions | Lesson 3 |
| JSON/CSV handling | Lesson 4 |
| Virtual environments | Lesson 5 |
| pytest | Lesson 6 |
| argparse CLI | Lesson 7 |
| Error handling & logging | Lesson 8 |
| Type hints & docstrings | Lesson 9 |

---

## ✋ Do This Now

### Task 1: Review the Starter Code

```bash
cat src/fundamentals/dataproc.py
```

The starter code has the structure but key functions need implementation.

### Task 2: Implement Core Functions

Complete these functions in `src/fundamentals/dataproc.py`:

1. **`read_jsonl(filepath)`** - Read JSONL file and return list of dicts
2. **`write_output(data, filepath)`** - Write to JSON, CSV, or JSONL based on extension
3. **`transform_uppercase(record)`** - Convert string values to uppercase
4. **`transform_filter(records, key, value)`** - Filter records by key=value
5. **`transform_add_timestamp(record)`** - Add processed_at timestamp
6. **`create_parser()`** - Create argparse parser with all options
7. **`main()`** - Orchestrate everything

### Task 3: Add Error Handling

- Handle file not found errors
- Handle invalid JSON
- Handle missing filter key
- Log all operations

### Task 4: Add Type Hints and Docstrings

Every function should have:
- Complete type hints
- Docstring with Args, Returns, Raises

### Task 5: Write Tests

Complete the tests in `tests/test_lesson_10.py`:
- Test each transformation
- Test output formats
- Test CLI arguments
- Test error handling

### Task 6: Run Tests

```bash
pytest tests/test_lesson_10.py -v
```

---

## 🧪 Quiz/Checkpoint

When you've completed all tasks, run:

```bash
make check 10
```

The checkpoint verifies:
- ✅ All core functions are implemented
- ✅ CLI has required arguments
- ✅ JSONL reading works
- ✅ All output formats work (JSON, CSV, JSONL)
- ✅ Transformations work correctly
- ✅ Error handling is proper
- ✅ Type hints and docstrings present
- ✅ All tests pass

---

## 💡 Implementation Hints

### Reading JSONL

```python
def read_jsonl(filepath: Path) -> list[dict]:
    records = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:  # Skip empty lines
                records.append(json.loads(line))
    return records
```

### Detecting Output Format

```python
def get_output_format(filepath: Path) -> str:
    suffix = filepath.suffix.lower()
    if suffix == ".json":
        return "json"
    elif suffix == ".csv":
        return "csv"
    elif suffix == ".jsonl":
        return "jsonl"
    else:
        raise ValueError(f"Unknown output format: {suffix}")
```

### Transform Pattern

```python
def apply_transforms(
    records: list[dict],
    transform: str,
    **kwargs
) -> list[dict]:
    if transform == "none":
        return records
    elif transform == "uppercase":
        return [transform_uppercase(r) for r in records]
    elif transform == "filter":
        return transform_filter(records, kwargs["key"], kwargs["value"])
    # ...
```

### CLI Pattern

```python
def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Process JSONL data files"
    )
    parser.add_argument("input", type=Path, help="Input JSONL file")
    parser.add_argument("output", type=Path, help="Output file")
    parser.add_argument(
        "--transform", "-t",
        choices=["none", "uppercase", "filter", "add_timestamp"],
        default="none",
        help="Transformation to apply"
    )
    # Add more arguments...
    return parser
```

---

## ⚠️ Common Mistakes

### 1. Forgetting to Handle Empty Files
```python
# Handle empty input
if not records:
    logger.warning("Input file is empty")
    return []
```

### 2. Not Closing Files
```python
# Always use context managers
with open(filepath) as f:
    data = f.read()
```

### 3. CSV Header Issues
```python
# Get fieldnames from first record
if records:
    fieldnames = list(records[0].keys())
```

### 4. Not Validating Inputs
```python
if not input_path.exists():
    parser.error(f"Input file not found: {input_path}")
```

---

## 📂 Expected File Structure

After completion:

```
src/fundamentals/
├── dataproc.py          # Your CLI tool (complete)
└── ...

tests/
├── test_lesson_10.py    # Your tests (complete)
└── ...

workspace/
└── lesson10/            # Test files you create
    ├── sample.jsonl
    └── ...
```

---

## ✅ Completion Checklist

Before running the final checkpoint:

- [ ] `read_jsonl` implemented and tested
- [ ] `write_output` supports JSON, CSV, JSONL
- [ ] All transformations work
- [ ] CLI accepts all required arguments
- [ ] `--help` shows useful information
- [ ] Errors are handled gracefully
- [ ] Logging shows what's happening
- [ ] All functions have type hints
- [ ] All functions have docstrings
- [ ] All tests pass

---

## 🎉 Course Completion

When `make check 10` passes, you've completed the course!

Run the full test suite to confirm:
```bash
make test
```

Check your progress:
```bash
make progress
```

Update `progress.md` to mark all items complete!

---

## 🚀 What's Next?

You're now ready to:

1. **Build LLM evaluation systems** - You have all the foundational skills
2. **Work with real APIs** - Add API clients to your toolkit
3. **Create production tools** - Your code will be maintainable and tested

Congratulations on completing the LLM Eval Fundamentals course! 🎓


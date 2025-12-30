# Lesson 4: Data Formats (JSON & CSV)

> ⏱️ Estimated time: 2 hours

---

## 🎯 What You'll Learn

By the end of this lesson, you will be able to:
- Read and write JSON files
- Read and write CSV files
- Use `pathlib` for file paths
- Handle file I/O safely

---

## 📚 Core Concepts

### Why Data Formats Matter

LLM evaluations involve lots of data:
- **Prompts** and **responses** (often JSON or JSONL)
- **Metrics** and **scores** (often CSV)
- **Configuration** files (JSON, YAML)

You need to be comfortable reading and writing these formats.

### JSON (JavaScript Object Notation)

JSON stores structured data as text. It maps directly to Python dicts and lists.

```json
{
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "ML"],
    "active": true
}
```

#### Reading JSON

```python
import json

# From a string
data = json.loads('{"name": "Alice", "age": 30}')
print(data["name"])  # Alice

# From a file
with open("data.json", "r") as f:
    data = json.load(f)
```

#### Writing JSON

```python
import json

data = {"name": "Alice", "age": 30}

# To a string
json_string = json.dumps(data)
print(json_string)  # {"name": "Alice", "age": 30}

# To a file (formatted nicely)
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)
```

### JSONL (JSON Lines)

JSONL has one JSON object per line—perfect for large datasets.

```jsonl
{"id": 1, "text": "First item"}
{"id": 2, "text": "Second item"}
{"id": 3, "text": "Third item"}
```

```python
# Reading JSONL
items = []
with open("data.jsonl", "r") as f:
    for line in f:
        items.append(json.loads(line))

# Writing JSONL
with open("output.jsonl", "w") as f:
    for item in items:
        f.write(json.dumps(item) + "\n")
```

### CSV (Comma-Separated Values)

CSV is tabular data—rows and columns, like a spreadsheet.

```csv
name,age,city
Alice,30,NYC
Bob,25,LA
```

#### Reading CSV

```python
import csv

# As a list of lists
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # ['Alice', '30', 'NYC']

# As a list of dicts (with headers)
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"])  # Alice
```

#### Writing CSV

```python
import csv

# From a list of lists
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "city"])  # Header
    writer.writerow(["Alice", 30, "NYC"])
    writer.writerow(["Bob", 25, "LA"])

# From a list of dicts
with open("output.csv", "w", newline="") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 30, "city": "NYC"})
```

### pathlib - Modern Path Handling

`pathlib` is the modern way to handle file paths in Python.

```python
from pathlib import Path

# Create a path
path = Path("data") / "files" / "example.json"
print(path)  # data/files/example.json

# Check if exists
if path.exists():
    print("File exists!")

# Read file content
content = path.read_text()

# Write file content
path.write_text("Hello, World!")

# Get file info
print(path.name)      # example.json
print(path.suffix)    # .json
print(path.stem)      # example
print(path.parent)    # data/files

# List directory contents
for file in Path("data").iterdir():
    print(file)

# Find all JSON files
for json_file in Path("data").glob("*.json"):
    print(json_file)
```

---

## ✋ Do This Now

Complete the functions in the starter file.

### Task 1: Open the Starter File

```bash
cat src/fundamentals/data_formats.py
```

### Task 2: Complete the Functions

Edit `src/fundamentals/data_formats.py` and implement each function.

### Task 3: Test Your Implementation

```bash
source venv/bin/activate
pytest tests/test_lesson_04.py -v
```

---

## 🧪 Quiz/Checkpoint

When you've completed all tasks, run:

```bash
make check 4
```

The tests verify:
- ✅ `read_json` correctly parses JSON files
- ✅ `write_json` creates valid JSON files
- ✅ `read_csv` correctly parses CSV files
- ✅ `write_csv` creates valid CSV files
- ✅ `read_jsonl` handles JSON Lines format
- ✅ `write_jsonl` creates valid JSONL files

---

## ⚠️ Common Mistakes

### 1. Forgetting `newline=""` for CSV on Windows
```python
# May cause extra blank lines on Windows
with open("data.csv", "w") as f:  # Wrong

# Correct
with open("data.csv", "w", newline="") as f:
```

### 2. Not Closing Files
```python
# Wrong - file might not close properly
f = open("data.json")
data = json.load(f)

# Right - use context manager
with open("data.json") as f:
    data = json.load(f)
```

### 3. Confusing `load` vs `loads`
```python
json.loads(string)  # Parse a STRING
json.load(file)     # Parse a FILE object
```

### 4. Forgetting to Strip Whitespace in JSONL
```python
# Lines may have trailing newlines
for line in f:
    data = json.loads(line.strip())  # Strip whitespace!
```

---

## ✅ Before Moving On

You should be able to:
- [ ] Read and write JSON files
- [ ] Read and write CSV files
- [ ] Handle JSONL format
- [ ] Use pathlib for file operations

---

## 🎯 Next Lesson

Continue to **Lesson 5: Python Packaging & Environments**:
```bash
make lesson 5
```


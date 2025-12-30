# 🎓 LLM Eval Fundamentals: Prerequisites Course

> **Learn the essential Python and developer skills you need before building LLM evaluation systems.**

This is a hands-on, self-paced course designed for motivated beginners. Every lesson includes explanations, coding tasks, and automated checkpoints that verify your work.

---

## 🚀 How to Start

### Prerequisites
- macOS with Python 3.11+
- Terminal access
- A code editor (VS Code recommended)

### Quick Start

```bash
# 1. Navigate to this directory
cd /path/to/course

# 2. Set up the environment
make setup

# 3. Read the syllabus
cat syllabus.md

# 4. Start with Lesson 1
make lesson 1

# 5. After completing the tasks, check your work
make check 1
```

---

## 📚 Course Structure

```
course/
├── README.md           # You are here
├── syllabus.md         # Course outline and sequence
├── progress.md         # Track your progress (checkboxes)
├── Makefile            # Run lessons and checks
├── requirements.txt    # Python dependencies
├── pyproject.toml      # Project configuration
│
├── lessons/            # Lesson content (markdown)
│   ├── 01_terminal.md
│   ├── 02_git.md
│   └── ...
│
├── src/fundamentals/   # Source code modules
│   ├── __init__.py
│   ├── data_formats.py
│   └── ...
│
├── tests/              # Pytest test files
│   ├── test_lesson_03.py
│   └── ...
│
├── checkpoints/        # Verification scripts
│   ├── check_01.py
│   ├── check_02.py
│   └── ...
│
└── workspace/          # YOUR work area for lessons
    └── (your files go here)
```

---

## 🎯 Available Commands

| Command | Description |
|---------|-------------|
| `make setup` | Create virtual environment and install dependencies |
| `make test` | Run all pytest tests |
| `make lesson N` | Display lesson N instructions |
| `make check N` | Run checkpoint verification for lesson N |
| `make progress` | Show your current progress |
| `make clean` | Remove generated files and venv |

---

## 📋 Lessons Overview

| # | Topic | Focus |
|---|-------|-------|
| 1 | Terminal & Filesystem | Navigate, create, manipulate files |
| 2 | Git Basics | Version control fundamentals |
| 3 | Python Basics | Scripts, functions, modules |
| 4 | Data Formats | JSON, CSV, file I/O |
| 5 | Packaging & Environments | venv, pip, dependencies |
| 6 | Testing with pytest | Write and run tests |
| 7 | CLI with argparse | Build command-line tools |
| 8 | Errors, Logging, Timing | Robust code patterns |
| 9 | Code Quality | Type hints, docstrings |
| 10 | Mini Capstone | Integrate all skills |

---

## ✅ How Checkpoints Work

Each lesson has an automated checkpoint:

1. **Read the lesson**: `make lesson N`
2. **Do the tasks**: Follow the "Do This Now" instructions
3. **Check your work**: `make check N`

The checkpoint will either:
- ✅ **PASS**: You've completed all requirements
- ❌ **FAIL**: Shows what's missing or incorrect

Keep working until all checks pass!

---

## 🔧 Troubleshooting

### "Command not found: make"
Install Xcode command line tools:
```bash
xcode-select --install
```

### "Python not found"
Ensure Python 3.11+ is installed:
```bash
python3 --version
# If not installed, use Homebrew:
brew install python@3.11
```

### Tests failing unexpectedly
Make sure you activated the virtual environment:
```bash
source venv/bin/activate
```

---

## 📖 Learning Philosophy

1. **Learn by doing**: Reading isn't enough—you must type the commands and write the code
2. **Fail forward**: Checkpoints are meant to fail first; that's how you learn
3. **Build muscle memory**: Repeat commands until they feel natural
4. **No shortcuts**: Don't copy-paste checkpoint answers—you're only cheating yourself

---

## 🎉 Ready?

Start your journey:

```bash
make lesson 1
```

Good luck! 🚀


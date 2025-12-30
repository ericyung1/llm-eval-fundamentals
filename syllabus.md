# 📚 Course Syllabus: LLM Eval Prerequisites

> **Duration**: 10 lessons, ~20-30 hours total  
> **Prerequisites**: None (beginner-friendly)  
> **Goal**: Master the foundational skills needed to build LLM evaluation systems

---

## Course Sequence

### Module 1: Developer Environment (Lessons 1-2)

#### Lesson 1: Terminal & Filesystem Basics
**Time**: ~2 hours

- **Concepts**: Command line interface, file system navigation, file manipulation
- **Skills**: `cd`, `ls`, `pwd`, `mkdir`, `touch`, `rm`, `cat`, `grep`, piping
- **Checkpoint**: Create a specific folder structure with files containing required text
- **Why it matters**: Every developer tool runs in the terminal; this is your foundation

#### Lesson 2: Git Basics  
**Time**: ~2 hours

- **Concepts**: Version control, commits, repository history
- **Skills**: `git init`, `status`, `add`, `commit`, `log`, `.gitignore`
- **Checkpoint**: Create a repo with at least 2 commits with specific messages
- **Why it matters**: All real projects use version control; you'll use Git daily

---

### Module 2: Python Fundamentals (Lessons 3-5)

#### Lesson 3: Python Basics
**Time**: ~2-3 hours

- **Concepts**: Running scripts, defining functions, organizing code into modules
- **Skills**: Functions, parameters, return values, imports, `if __name__ == "__main__"`
- **Checkpoint**: Complete functions that pass automated tests
- **Why it matters**: Python is the primary language for ML/LLM work

#### Lesson 4: Data Formats
**Time**: ~2 hours

- **Concepts**: Structured data, serialization, file I/O
- **Skills**: JSON read/write, CSV read/write, `pathlib`, file handling
- **Checkpoint**: Parse and generate JSON/CSV files correctly
- **Why it matters**: LLM evals involve lots of data; you'll read/write JSON constantly

#### Lesson 5: Python Packaging & Environments
**Time**: ~2 hours

- **Concepts**: Dependency isolation, reproducible environments
- **Skills**: `venv`, `pip`, `requirements.txt`, package installation
- **Checkpoint**: Create a working virtual environment with installed dependencies
- **Why it matters**: Professional Python projects always use virtual environments

---

### Module 3: Testing & CLI Tools (Lessons 6-7)

#### Lesson 6: Testing Fundamentals with pytest
**Time**: ~2-3 hours

- **Concepts**: Unit testing, test-driven development, assertions
- **Skills**: Writing tests, `assert`, fixtures, running pytest
- **Checkpoint**: Write 3+ tests for given functions; all must pass
- **Why it matters**: LLM evals ARE tests—you need to know how testing works

#### Lesson 7: CLI Basics with argparse
**Time**: ~2 hours

- **Concepts**: Command-line interfaces, argument parsing
- **Skills**: `argparse`, positional/optional arguments, help text
- **Checkpoint**: Build a CLI tool that passes integration tests
- **Why it matters**: You'll build CLI tools to run evaluations

---

### Module 4: Production Patterns (Lessons 8-9)

#### Lesson 8: Logging, Errors, and Timing
**Time**: ~2 hours

- **Concepts**: Error handling, observability, performance measurement
- **Skills**: `try/except`, custom exceptions, `logging` module, `time.perf_counter`
- **Checkpoint**: Implement error handling and logging that passes tests
- **Why it matters**: Real systems need proper error handling and logging

#### Lesson 9: Code Quality Basics
**Time**: ~2 hours

- **Concepts**: Type safety, documentation, code style
- **Skills**: Type hints, docstrings, basic formatting
- **Checkpoint**: Add type hints and docstrings to a module
- **Why it matters**: Quality code is maintainable code; types catch bugs early

---

### Module 5: Integration (Lesson 10)

#### Lesson 10: Mini Capstone
**Time**: ~3-4 hours

- **Concepts**: Integrating all skills into a cohesive tool
- **Skills**: CLI, file I/O, JSON/JSONL, testing, error handling, logging
- **Checkpoint**: Build a data processing CLI that passes end-to-end tests
- **Why it matters**: Proves you can combine all skills; prepares you for real projects

---

## Learning Path Visualization

```
┌─────────────────────────────────────────────────────────────────┐
│                    Module 1: Environment                        │
│  ┌──────────────┐    ┌──────────────┐                          │
│  │ 1. Terminal  │ ──▶│ 2. Git       │                          │
│  └──────────────┘    └──────────────┘                          │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Module 2: Python Core                         │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │ 3. Python    │ ──▶│ 4. Data      │ ──▶│ 5. Packaging │      │
│  │    Basics    │    │    Formats   │    │    & Envs    │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  Module 3: Testing & CLI                        │
│  ┌──────────────┐    ┌──────────────┐                          │
│  │ 6. pytest    │ ──▶│ 7. argparse  │                          │
│  └──────────────┘    └──────────────┘                          │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                Module 4: Production Patterns                    │
│  ┌──────────────┐    ┌──────────────┐                          │
│  │ 8. Errors &  │ ──▶│ 9. Code      │                          │
│  │    Logging   │    │    Quality   │                          │
│  └──────────────┘    └──────────────┘                          │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Module 5: Integration                         │
│  ┌────────────────────────────────────────────────────────┐    │
│  │              10. Mini Capstone                          │    │
│  │         (Data Processing CLI with Tests)                │    │
│  └────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Time Commitment

| Pace | Daily Time | Completion |
|------|------------|------------|
| Intensive | 4-5 hours | ~1 week |
| Moderate | 2 hours | ~2 weeks |
| Relaxed | 1 hour | ~3-4 weeks |

---

## Success Criteria

You've completed this course when:

1. ✅ All 10 checkpoints pass (`make check N` for N=1..10)
2. ✅ All tests pass (`make test`)
3. ✅ All boxes in `progress.md` are checked
4. ✅ You can explain what each lesson taught without looking

---

## What's Next?

After completing this course, you'll be ready to:

- Build LLM evaluation pipelines
- Work with OpenAI/Anthropic APIs
- Create custom evaluation metrics
- Develop testing frameworks for AI outputs

**Continue to**: LLM Eval Project (separate repository)

---

## Tips for Success

1. **Don't skip lessons** — each builds on the previous
2. **Type everything** — no copy-paste for learning
3. **Debug your failures** — the error messages teach you
4. **Take breaks** — learning happens during rest too
5. **Celebrate wins** — each passing checkpoint is progress!


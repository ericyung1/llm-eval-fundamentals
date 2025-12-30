# Lesson 2: Git Basics

> ⏱️ Estimated time: 2 hours

---

## 🎯 What You'll Learn

By the end of this lesson, you will be able to:
- Initialize a Git repository
- Track changes with commits
- View project history
- Use `.gitignore` to exclude files

---

## 📚 Core Concepts

### What is Git?

Git is a **version control system**. Think of it like:
- **Time machine**: Go back to any previous version of your code
- **Parallel universes**: Work on different features without affecting each other (branches)
- **Collaboration tool**: Multiple people can work on the same project

Every professional developer uses Git. You will too.

### Key Terms

| Term | Meaning |
|------|---------|
| **Repository (repo)** | A folder tracked by Git |
| **Commit** | A snapshot of your files at a point in time |
| **Staging area** | Where you prepare changes before committing |
| **Working directory** | Your actual files on disk |

### The Git Workflow

```
[Working Directory] --add--> [Staging Area] --commit--> [Repository]
      (edit files)              (prepare)              (save snapshot)
```

1. You **edit files** in your working directory
2. You **stage** the changes you want to include
3. You **commit** to save a snapshot

### Essential Git Commands

#### `git init` - Create a Repository
Turn a folder into a Git repository.
```bash
git init
# Creates a hidden .git folder that tracks everything
```

#### `git status` - Check Current State
See what's changed, what's staged, what's committed.
```bash
git status
# Shows: modified files, staged files, untracked files
```

This is your most-used command. Run it often!

#### `git add` - Stage Changes
Tell Git which changes to include in the next commit.
```bash
git add filename.txt         # Stage one file
git add .                    # Stage all changes
git add -p                   # Stage interactively (advanced)
```

#### `git commit` - Save a Snapshot
Create a commit with a descriptive message.
```bash
git commit -m "Add login feature"
# -m lets you write the message inline
```

**Good commit messages**:
- ✅ "Add user authentication"
- ✅ "Fix bug in payment processing"
- ✅ "Update README with installation instructions"

**Bad commit messages**:
- ❌ "fix"
- ❌ "asdfasdf"
- ❌ "stuff"

#### `git log` - View History
See all commits in the repository.
```bash
git log                      # Full details
git log --oneline            # Compact view
git log -n 5                 # Last 5 commits
```

#### `git diff` - See Changes
View what's changed but not yet staged.
```bash
git diff                     # Changes in working directory
git diff --staged            # Changes already staged
```

### The `.gitignore` File

Some files shouldn't be tracked by Git:
- Generated files (`__pycache__/`, `*.pyc`)
- Secrets (`.env`, API keys)
- Dependencies (`node_modules/`, `venv/`)
- System files (`.DS_Store`)

Create a `.gitignore` file to exclude them:
```
# Python
__pycache__/
*.pyc
*.pyo
venv/

# Secrets
.env
*.key

# macOS
.DS_Store

# IDE
.vscode/
.idea/
```

---

## ✋ Do This Now

Complete these tasks in order. You'll create a Git repository in your workspace.

### Task 1: Navigate to Workspace

```bash
# Go to the course workspace
cd /path/to/course/workspace

# Create and enter a folder for this lesson
mkdir lesson02
cd lesson02

# Verify location
pwd
# Should end with: /course/workspace/lesson02
```

### Task 2: Initialize Git Repository

```bash
# Initialize git
git init

# Check status
git status
# Should say: "No commits yet" and "nothing to commit"
```

You should see a message like "Initialized empty Git repository".

### Task 3: Create Your First File and Commit

```bash
# Create a README file
echo "# My First Git Repo" > README.md
echo "" >> README.md
echo "This is a practice repository for learning Git." >> README.md

# Check status - file should be "untracked"
git status

# Stage the file
git add README.md

# Check status again - file should be "staged"
git status

# Create your first commit
git commit -m "Initial commit: add README"

# Verify the commit
git log --oneline
# Should show your commit with the message
```

### Task 4: Make More Changes and Second Commit

```bash
# Add more content to README
echo "" >> README.md
echo "## What I Learned" >> README.md
echo "- How to initialize a repo" >> README.md
echo "- How to stage and commit changes" >> README.md

# Create a .gitignore file
echo "# Ignore Python cache" > .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo "" >> .gitignore
echo "# Ignore environment" >> .gitignore
echo ".env" >> .gitignore
echo "venv/" >> .gitignore

# Check status - should show both files modified/untracked
git status

# Stage both files
git add README.md .gitignore

# Create second commit
git commit -m "Add learning notes and gitignore"

# View history - should show 2 commits
git log --oneline
```

### Task 5: Create a Python File

```bash
# Create a simple Python file
echo '"""My first tracked Python file."""' > hello.py
echo '' >> hello.py
echo 'def greet(name: str) -> str:' >> hello.py
echo '    """Return a greeting message."""' >> hello.py
echo '    return f"Hello, {name}!"' >> hello.py
echo '' >> hello.py
echo 'if __name__ == "__main__":' >> hello.py
echo '    print(greet("Git"))' >> hello.py

# Stage and commit
git add hello.py
git commit -m "Add hello.py greeting function"

# Verify we have 3 commits
git log --oneline
```

### Task 6: View Your History

```bash
# See all commits (should be 3)
git log --oneline

# See detailed log
git log

# See what files are tracked
git ls-files
```

---

## 🧪 Quiz/Checkpoint

When you've completed all tasks, run:

```bash
make check 2
```

The checkpoint script will verify:
1. ✅ `workspace/lesson02/` is a Git repository
2. ✅ Repository has at least 3 commits
3. ✅ First commit message contains "Initial" or "initial"
4. ✅ `.gitignore` file exists and contains `__pycache__`
5. ✅ `README.md` exists
6. ✅ `hello.py` exists

If any check fails, go back and complete that task!

---

## ⚠️ Common Mistakes

### 1. Forgetting to Stage Before Commit
**Problem**: "nothing to commit, working tree clean"
**Solution**: Use `git add` before `git commit`

```bash
git add .                    # Stage all changes
git commit -m "message"      # Then commit
```

### 2. Empty Commit Message
**Problem**: Git opens a text editor and you're stuck
**Solution**: Always use `-m` flag, or learn to exit vim (`:q!`)

```bash
git commit -m "Your message here"
```

### 3. Committing Sensitive Data
**Problem**: You accidentally committed `.env` or API keys
**Solution**: Add to `.gitignore` BEFORE creating the file

```bash
# Add to .gitignore first
echo ".env" >> .gitignore
# Then create the file
touch .env
```

### 4. Not Checking Status
**Problem**: Not sure what will be committed
**Solution**: Run `git status` before every commit

### 5. Forgetting You're in a Git Repo
**Problem**: Running `git init` in wrong folder, or nested repos
**Solution**: Check with `git status` first; look for `.git` folder

```bash
ls -la | grep .git           # Check if .git exists
```

---

## 📖 Quick Reference

| Command | Description | Example |
|---------|-------------|---------|
| `git init` | Create new repo | `git init` |
| `git status` | Check state | `git status` |
| `git add` | Stage changes | `git add file.txt` |
| `git commit` | Save snapshot | `git commit -m "msg"` |
| `git log` | View history | `git log --oneline` |
| `git diff` | See changes | `git diff` |

### Status Meanings

| Status | Meaning |
|--------|---------|
| Untracked | New file Git doesn't know about |
| Modified | Changed but not staged |
| Staged | Ready to be committed |
| Clean | No pending changes |

---

## ✅ Before Moving On

You should be able to:
- [ ] Initialize a new Git repository
- [ ] Stage changes with `git add`
- [ ] Create commits with clear messages
- [ ] View history with `git log`
- [ ] Create a `.gitignore` file
- [ ] Explain the staging area concept

---

## 🎯 Next Lesson

Continue to **Lesson 3: Python Basics** to learn programming fundamentals:
```bash
make lesson 3
```


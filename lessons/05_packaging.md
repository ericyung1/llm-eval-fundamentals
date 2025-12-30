# Lesson 5: Python Packaging & Environments

> ⏱️ Estimated time: 2 hours

---

## 🎯 What You'll Learn

By the end of this lesson, you will be able to:
- Create and use virtual environments
- Manage dependencies with pip
- Create a `requirements.txt` file
- Understand why isolation matters

---

## 📚 Core Concepts

### The Problem: Dependency Conflicts

Imagine you have two projects:
- **Project A** needs `requests==2.25.0`
- **Project B** needs `requests==2.31.0`

If you install packages globally, one project will break!

### The Solution: Virtual Environments

A **virtual environment** is an isolated Python installation. Each project gets its own packages.

```
/my-project-a/
├── venv/              # Project A's packages
└── ...

/my-project-b/
├── venv/              # Project B's packages (different versions!)
└── ...
```

### Creating a Virtual Environment

```bash
# Create a virtual environment named 'venv'
python3 -m venv venv

# You'll see a new 'venv' folder with:
# - bin/   (or Scripts/ on Windows) - executables
# - lib/   - installed packages
# - include/ - C headers
```

### Activating and Deactivating

```bash
# Activate (macOS/Linux)
source venv/bin/activate

# Your prompt changes to show the environment:
# (venv) $

# Now 'python' and 'pip' use the virtual environment
which python
# /path/to/project/venv/bin/python

# Deactivate when done
deactivate
```

### Installing Packages with pip

```bash
# Make sure venv is activated first!
source venv/bin/activate

# Install a package
pip install requests

# Install a specific version
pip install requests==2.31.0

# Install multiple packages
pip install pytest click rich

# Upgrade a package
pip install --upgrade requests

# Uninstall
pip uninstall requests
```

### requirements.txt

This file lists all your project's dependencies. It's like a recipe for recreating your environment.

```txt
# requirements.txt
requests==2.31.0
pytest>=7.0.0
click~=8.1.0
```

Version specifiers:
- `==2.31.0` - Exact version
- `>=7.0.0` - Minimum version
- `~=8.1.0` - Compatible release (8.1.x but not 8.2.0)
- `<=3.0` - Maximum version

#### Creating requirements.txt

```bash
# Generate from current environment
pip freeze > requirements.txt

# This lists ALL packages with exact versions
```

#### Installing from requirements.txt

```bash
# Install all dependencies
pip install -r requirements.txt
```

### Best Practices

1. **Always use a venv** - Never install packages globally for projects
2. **Keep requirements.txt updated** - Run `pip freeze > requirements.txt` when adding packages
3. **Include requirements.txt in version control** - Others can recreate your environment
4. **Don't commit venv/** - Add it to `.gitignore`

---

## ✋ Do This Now

You'll practice creating and using a virtual environment.

### Task 1: Create a Practice Directory

```bash
cd /path/to/course/workspace
mkdir lesson05
cd lesson05
```

### Task 2: Create a Virtual Environment

```bash
# Create the venv
python3 -m venv venv

# Verify it was created
ls -la venv/

# You should see: bin/, include/, lib/, pyvenv.cfg
```

### Task 3: Activate the Environment

```bash
# Activate
source venv/bin/activate

# Your prompt should now show (venv)
# Verify you're using the venv's Python
which python
# Should show: /path/to/lesson05/venv/bin/python
```

### Task 4: Install Packages

```bash
# Install pytest (already in course requirements, but practice here)
pip install pytest

# Verify installation
pip list
# Should show pytest and its dependencies

# Check pytest works
pytest --version
```

### Task 5: Create requirements.txt

```bash
# Generate requirements file
pip freeze > requirements.txt

# View the contents
cat requirements.txt
# Should list pytest and its dependencies with versions
```

### Task 6: Test the Environment

Create a simple test file to verify everything works:

```bash
# Create a test file
cat > test_sanity.py << 'EOF'
"""Sanity check that pytest works."""

def test_environment_works():
    """Verify we can run tests."""
    assert True

def test_python_version():
    """Verify Python version is 3.11+."""
    import sys
    assert sys.version_info >= (3, 11), "Python 3.11+ required"
EOF

# Run the tests
pytest test_sanity.py -v
```

### Task 7: Clean Up and Recreate

Practice recreating an environment from requirements.txt:

```bash
# Deactivate current venv
deactivate

# Delete the venv (don't worry, requirements.txt has the recipe!)
rm -rf venv

# Create a fresh venv
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install from requirements.txt
pip install -r requirements.txt

# Verify pytest still works
pytest test_sanity.py -v
```

---

## 🧪 Quiz/Checkpoint

When you've completed all tasks, run:

```bash
make check 5
```

The checkpoint script will verify:
- ✅ `workspace/lesson05/` directory exists
- ✅ `venv/` directory exists within lesson05
- ✅ `requirements.txt` exists
- ✅ `requirements.txt` contains pytest
- ✅ Tests pass when using the venv

---

## ⚠️ Common Mistakes

### 1. Forgetting to Activate
```bash
# Wrong - uses global pip
pip install requests

# Right - activate first!
source venv/bin/activate
pip install requests
```

Check your prompt! It should show `(venv)`.

### 2. Committing venv/ to Git
The venv folder is large and platform-specific. Always add it to `.gitignore`:

```gitignore
venv/
.venv/
env/
```

### 3. Using `pip freeze` Without Cleaning Up
`pip freeze` includes ALL packages, even dependencies of dependencies. For a cleaner requirements.txt, you can manually list only your direct dependencies.

### 4. Wrong Python Version
```bash
# Check which Python you're using
python --version

# If it's wrong, specify the version when creating venv
python3.11 -m venv venv
```

### 5. Forgetting to Deactivate
Always `deactivate` when switching projects, or open a new terminal.

---

## 📖 Quick Reference

| Command | Description |
|---------|-------------|
| `python3 -m venv venv` | Create virtual environment |
| `source venv/bin/activate` | Activate (macOS/Linux) |
| `deactivate` | Deactivate |
| `pip install package` | Install a package |
| `pip install -r requirements.txt` | Install from file |
| `pip freeze > requirements.txt` | Save current packages |
| `pip list` | Show installed packages |
| `pip show package` | Show package info |
| `which python` | Check which Python is active |

---

## ✅ Before Moving On

You should be able to:
- [ ] Create a virtual environment
- [ ] Activate and deactivate it
- [ ] Install packages with pip
- [ ] Create and use requirements.txt
- [ ] Explain why venvs are important

---

## 🎯 Next Lesson

Continue to **Lesson 6: Testing with pytest**:
```bash
make lesson 6
```


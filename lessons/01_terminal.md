# Lesson 1: Terminal & Filesystem Basics

> ⏱️ Estimated time: 2 hours

---

## 🎯 What You'll Learn

By the end of this lesson, you will be able to:
- Navigate the filesystem using the command line
- Create, view, and delete files and directories
- Search file contents with `grep`
- Chain commands together with pipes

---

## 📚 Core Concepts

### The Terminal

The terminal (also called "command line" or "shell") is a text-based interface to your computer. Instead of clicking icons, you type commands. This might feel awkward at first, but it's **essential** for programming.

Why use the terminal?
- **Speed**: Many tasks are faster with keyboard than mouse
- **Automation**: You can script repetitive tasks
- **Power**: Some tools only exist on the command line
- **Remote servers**: GUIs aren't always available

### Your First Commands

Open Terminal (on macOS: Cmd+Space, type "Terminal", press Enter).

#### `pwd` - Print Working Directory
Shows where you are in the filesystem.
```bash
pwd
# Output example: /Users/yourname
```

#### `ls` - List
Shows files and folders in the current directory.
```bash
ls          # Basic list
ls -l       # Long format (permissions, size, date)
ls -la      # Include hidden files (starting with .)
ls -lah     # Human-readable sizes
```

#### `cd` - Change Directory
Move to a different directory.
```bash
cd Documents        # Go into Documents folder
cd ..              # Go up one level (parent directory)
cd ~               # Go to your home directory
cd /               # Go to root directory
cd -               # Go back to previous directory
```

**Pro tip**: Press Tab to autocomplete folder/file names!

#### `mkdir` - Make Directory
Create a new folder.
```bash
mkdir my_folder              # Create one folder
mkdir -p a/b/c               # Create nested folders
```

#### `touch` - Create Empty File
Create a new empty file (or update timestamp of existing file).
```bash
touch myfile.txt             # Create empty file
touch file1.txt file2.txt    # Create multiple files
```

#### `cat` - Concatenate (View File Contents)
Display the contents of a file.
```bash
cat myfile.txt               # Show file contents
cat file1.txt file2.txt      # Show multiple files
```

#### `echo` - Print Text
Output text (often used to write to files).
```bash
echo "Hello, World!"                     # Print to screen
echo "Hello" > file.txt                  # Write to file (overwrites)
echo "More text" >> file.txt             # Append to file
```

#### `rm` - Remove
Delete files or directories. **⚠️ Be careful - there's no trash/undo!**
```bash
rm myfile.txt                # Delete a file
rm -r my_folder              # Delete a folder and contents
rm -i myfile.txt             # Ask for confirmation (safer)
```

**Safety rule**: Never run `rm -rf /` or similar broad commands!

#### `cp` - Copy
Copy files or directories.
```bash
cp source.txt dest.txt           # Copy file
cp -r source_dir dest_dir        # Copy directory
```

#### `mv` - Move (or Rename)
Move or rename files/directories.
```bash
mv old.txt new.txt               # Rename file
mv file.txt folder/              # Move to folder
```

### Searching with `grep`

`grep` searches for patterns in files.
```bash
grep "hello" file.txt            # Find lines containing "hello"
grep -i "hello" file.txt         # Case-insensitive search
grep -r "hello" folder/          # Search recursively in folder
grep -n "hello" file.txt         # Show line numbers
```

### Piping with `|`

The pipe (`|`) sends output from one command as input to another.
```bash
ls -la | grep ".txt"             # List files, filter to only .txt
cat file.txt | grep "error"      # Show only lines with "error"
history | grep "git"             # Find git commands you've run
```

### Redirecting Output

```bash
command > file.txt               # Write output to file (overwrite)
command >> file.txt              # Append output to file
command 2> errors.txt            # Redirect errors only
command > out.txt 2>&1           # Redirect both output and errors
```

---

## ✋ Do This Now

Complete these tasks in order. All work should be done in the `workspace/` folder of this course.

### Task 1: Navigate to the Workspace

```bash
# First, navigate to the course directory (adjust path as needed)
cd /path/to/course

# Then go into the workspace folder
cd workspace

# Verify you're in the right place
pwd
# Should end with: /course/workspace
```

### Task 2: Create the Folder Structure

Create the following folder structure inside `workspace/`:
```
workspace/
└── lesson01/
    ├── notes/
    │   └── commands.txt
    └── data/
        ├── input.txt
        └── output.txt
```

Commands to run:
```bash
# Create the folders
mkdir -p lesson01/notes
mkdir -p lesson01/data

# Verify the structure
ls -R lesson01
```

### Task 3: Create Files with Content

```bash
# Navigate into lesson01
cd lesson01

# Create commands.txt with useful commands
echo "pwd - print working directory" > notes/commands.txt
echo "ls - list directory contents" >> notes/commands.txt
echo "cd - change directory" >> notes/commands.txt

# Create input.txt with some data
echo "line 1: hello world" > data/input.txt
echo "line 2: learning terminal" >> data/input.txt
echo "line 3: hello again" >> data/input.txt

# Create output.txt with a success message
echo "checkpoint complete" > data/output.txt
```

### Task 4: Verify Your Work

```bash
# Check commands.txt has content
cat notes/commands.txt

# Check input.txt has 3 lines
cat data/input.txt

# Use grep to find lines with "hello"
grep "hello" data/input.txt
# Should show 2 lines

# Count files in lesson01 (recursive)
find . -type f | wc -l
# Should show 3
```

### Task 5: Practice Piping

```bash
# List all files and filter for .txt
ls -la data/ | grep ".txt"

# Count how many lines contain "hello" in input.txt
grep "hello" data/input.txt | wc -l
# Should output: 2
```

---

## 🧪 Quiz/Checkpoint

When you've completed all tasks, run:

```bash
make check 1
```

The checkpoint script will verify:
1. ✅ `workspace/lesson01/` directory exists
2. ✅ `workspace/lesson01/notes/` directory exists  
3. ✅ `workspace/lesson01/data/` directory exists
4. ✅ `notes/commands.txt` exists and contains "pwd"
5. ✅ `data/input.txt` exists and contains "hello"
6. ✅ `data/output.txt` exists and contains "checkpoint"

If any check fails, go back and complete that task!

---

## ⚠️ Common Mistakes

### 1. Wrong Directory
**Problem**: "No such file or directory"
**Solution**: Use `pwd` to check where you are, then `cd` to the right place

### 2. Forgetting Quotes
**Problem**: `echo hello world > file.txt` works, but complex text might not
**Solution**: Always use quotes: `echo "hello world" > file.txt`

### 3. Using `>` Instead of `>>`
**Problem**: File gets overwritten instead of appended
**Solution**: 
- `>` overwrites (creates new file)
- `>>` appends (adds to existing file)

### 4. Deleting Wrong Files
**Problem**: `rm` has no undo
**Solution**: Use `rm -i` for confirmation, or `ls` first to check what you'll delete

### 5. Space in Filenames
**Problem**: `cd My Folder` thinks "My" and "Folder" are separate
**Solution**: Use quotes `cd "My Folder"` or escape `cd My\ Folder`

---

## 📖 Quick Reference

| Command | Description | Example |
|---------|-------------|---------|
| `pwd` | Show current directory | `pwd` |
| `ls` | List files | `ls -la` |
| `cd` | Change directory | `cd folder` |
| `mkdir` | Create directory | `mkdir -p a/b` |
| `touch` | Create file | `touch file.txt` |
| `cat` | View file | `cat file.txt` |
| `echo` | Print/write text | `echo "hi" > file.txt` |
| `rm` | Remove file/folder | `rm -r folder` |
| `cp` | Copy | `cp src dst` |
| `mv` | Move/rename | `mv old new` |
| `grep` | Search text | `grep "pattern" file` |
| `|` | Pipe output | `cmd1 | cmd2` |

---

## ✅ Before Moving On

You should be able to:
- [ ] Navigate to any directory using `cd`
- [ ] Create nested folder structures with `mkdir -p`
- [ ] Create and write to files with `touch` and `echo`
- [ ] View file contents with `cat`
- [ ] Search file contents with `grep`
- [ ] Chain commands with pipes (`|`)

---

## 🎯 Next Lesson

Continue to **Lesson 2: Git Basics** to learn version control:
```bash
make lesson 2
```


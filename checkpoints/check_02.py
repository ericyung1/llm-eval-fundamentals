#!/usr/bin/env python3
"""
Checkpoint for Lesson 2: Git Basics

This script verifies that the student has:
1. Created a Git repository
2. Made at least 3 commits
3. Has proper commit messages
4. Created necessary files
"""

import os
import subprocess
import sys
from pathlib import Path


def get_workspace_path() -> Path:
    """Get the workspace path relative to this script."""
    script_dir = Path(__file__).parent.absolute()
    course_root = script_dir.parent
    return course_root / "workspace"


def run_git_command(repo_path: Path, *args) -> tuple[bool, str]:
    """Run a git command in the specified repository."""
    try:
        result = subprocess.run(
            ["git"] + list(args),
            cwd=repo_path,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0, result.stdout.strip()
    except FileNotFoundError:
        return False, "Git is not installed"
    except subprocess.TimeoutExpired:
        return False, "Git command timed out"
    except Exception as e:
        return False, str(e)


def check_is_git_repo(repo_path: Path) -> bool:
    """Check if the directory is a Git repository."""
    git_dir = repo_path / ".git"
    if git_dir.is_dir():
        print("  ✅ Directory is a Git repository")
        return True
    else:
        print("  ❌ Directory is not a Git repository")
        print("     Run 'git init' in the lesson02 folder")
        return False


def check_commit_count(repo_path: Path, min_commits: int = 3) -> bool:
    """Check if the repository has at least min_commits commits."""
    success, output = run_git_command(repo_path, "rev-list", "--count", "HEAD")
    
    if not success:
        print(f"  ❌ Could not count commits (no commits yet?)")
        return False
    
    try:
        count = int(output)
        if count >= min_commits:
            print(f"  ✅ Repository has {count} commits (required: {min_commits}+)")
            return True
        else:
            print(f"  ❌ Repository has only {count} commits (required: {min_commits}+)")
            return False
    except ValueError:
        print(f"  ❌ Could not parse commit count: {output}")
        return False


def check_first_commit_message(repo_path: Path) -> bool:
    """Check if the first commit message contains 'initial' or 'Initial'."""
    # Get the first commit (oldest)
    success, output = run_git_command(
        repo_path, "log", "--reverse", "--format=%s", "-1"
    )
    
    if not success:
        print("  ❌ Could not read first commit message")
        return False
    
    message = output.lower()
    if "initial" in message:
        print(f"  ✅ First commit message contains 'initial': \"{output}\"")
        return True
    else:
        print(f"  ❌ First commit message should contain 'initial'")
        print(f"     Got: \"{output}\"")
        return False


def check_file_exists(repo_path: Path, filename: str) -> bool:
    """Check if a file exists in the repository."""
    filepath = repo_path / filename
    if filepath.is_file():
        print(f"  ✅ {filename} exists")
        return True
    else:
        print(f"  ❌ {filename} does not exist")
        return False


def check_file_contains(repo_path: Path, filename: str, text: str) -> bool:
    """Check if a file contains specific text."""
    filepath = repo_path / filename
    if not filepath.is_file():
        print(f"  ❌ {filename} does not exist")
        return False
    
    content = filepath.read_text()
    if text in content:
        print(f"  ✅ {filename} contains '{text}'")
        return True
    else:
        print(f"  ❌ {filename} does not contain '{text}'")
        return False


def check_file_tracked(repo_path: Path, filename: str) -> bool:
    """Check if a file is tracked by Git."""
    success, output = run_git_command(repo_path, "ls-files", filename)
    
    if success and filename in output:
        print(f"  ✅ {filename} is tracked by Git")
        return True
    else:
        print(f"  ❌ {filename} is not tracked by Git")
        print("     Did you forget to 'git add' and 'git commit'?")
        return False


def main() -> int:
    """Run all checkpoint verifications."""
    print("\n" + "=" * 60)
    print("🔍 Lesson 2 Checkpoint: Git Basics")
    print("=" * 60 + "\n")
    
    workspace = get_workspace_path()
    lesson_dir = workspace / "lesson02"
    
    # Check if lesson directory exists
    if not lesson_dir.is_dir():
        print(f"  ❌ Directory does not exist: {lesson_dir}")
        print("\n  Create it with: mkdir -p workspace/lesson02")
        print("=" * 60 + "\n")
        return 1
    
    results = []
    
    print("📁 Checking Git repository...\n")
    
    # Check 1: Is it a git repo?
    is_repo = check_is_git_repo(lesson_dir)
    results.append(is_repo)
    
    if not is_repo:
        print("\n" + "=" * 60)
        print("\n❌ Not a Git repository. Run 'git init' in workspace/lesson02/")
        print("\n" + "=" * 60 + "\n")
        return 1
    
    print("\n📊 Checking commit history...\n")
    
    # Check 2: Has at least 3 commits
    results.append(check_commit_count(lesson_dir, 3))
    
    # Check 3: First commit message
    results.append(check_first_commit_message(lesson_dir))
    
    print("\n📄 Checking files...\n")
    
    # Check 4: README.md exists
    results.append(check_file_exists(lesson_dir, "README.md"))
    
    # Check 5: .gitignore exists and contains __pycache__
    results.append(check_file_exists(lesson_dir, ".gitignore"))
    results.append(check_file_contains(lesson_dir, ".gitignore", "__pycache__"))
    
    # Check 6: hello.py exists
    results.append(check_file_exists(lesson_dir, "hello.py"))
    
    print("\n🔗 Checking files are tracked...\n")
    
    # Check 7: Files are tracked by git
    results.append(check_file_tracked(lesson_dir, "README.md"))
    results.append(check_file_tracked(lesson_dir, "hello.py"))
    
    # Summary
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    
    if all(results):
        print(f"\n🎉 ALL CHECKS PASSED ({passed}/{total})")
        print("\nExcellent! You now understand Git fundamentals.")
        print("\nNext step: Run 'make lesson 3' to learn Python basics.")
        print("\n" + "=" * 60 + "\n")
        return 0
    else:
        print(f"\n❌ SOME CHECKS FAILED ({passed}/{total} passed)")
        print("\nGo back to the lesson and complete the missing tasks.")
        print("Then run 'make check 2' again.")
        print("\n" + "=" * 60 + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())


#!/usr/bin/env python3
"""
Checkpoint for Lesson 1: Terminal & Filesystem Basics

This script verifies that the student has completed all terminal tasks.
"""

import os
import sys
from pathlib import Path


def get_workspace_path() -> Path:
    """Get the workspace path relative to this script."""
    # Script is in checkpoints/, workspace is at ../workspace/
    script_dir = Path(__file__).parent.absolute()
    course_root = script_dir.parent
    return course_root / "workspace"


def check_directory_exists(path: Path, name: str) -> bool:
    """Check if a directory exists."""
    if path.is_dir():
        print(f"  ✅ {name} exists")
        return True
    else:
        print(f"  ❌ {name} does not exist")
        print(f"     Expected: {path}")
        return False


def check_file_exists(path: Path, name: str) -> bool:
    """Check if a file exists."""
    if path.is_file():
        print(f"  ✅ {name} exists")
        return True
    else:
        print(f"  ❌ {name} does not exist")
        print(f"     Expected: {path}")
        return False


def check_file_contains(path: Path, text: str, name: str) -> bool:
    """Check if a file contains specific text."""
    if not path.is_file():
        print(f"  ❌ {name} does not exist, cannot check contents")
        return False
    
    content = path.read_text()
    if text.lower() in content.lower():
        print(f"  ✅ {name} contains '{text}'")
        return True
    else:
        print(f"  ❌ {name} does not contain '{text}'")
        print(f"     File contents: {content[:100]}...")
        return False


def main() -> int:
    """Run all checkpoint verifications."""
    print("\n" + "=" * 60)
    print("🔍 Lesson 1 Checkpoint: Terminal & Filesystem Basics")
    print("=" * 60 + "\n")
    
    workspace = get_workspace_path()
    lesson_dir = workspace / "lesson01"
    
    results = []
    
    print("📁 Checking directory structure...\n")
    
    # Check 1: lesson01 directory exists
    results.append(check_directory_exists(lesson_dir, "lesson01/"))
    
    # Check 2: notes directory exists
    results.append(check_directory_exists(lesson_dir / "notes", "lesson01/notes/"))
    
    # Check 3: data directory exists
    results.append(check_directory_exists(lesson_dir / "data", "lesson01/data/"))
    
    print("\n📄 Checking files...\n")
    
    # Check 4: commands.txt exists
    commands_file = lesson_dir / "notes" / "commands.txt"
    results.append(check_file_exists(commands_file, "notes/commands.txt"))
    
    # Check 5: input.txt exists
    input_file = lesson_dir / "data" / "input.txt"
    results.append(check_file_exists(input_file, "data/input.txt"))
    
    # Check 6: output.txt exists
    output_file = lesson_dir / "data" / "output.txt"
    results.append(check_file_exists(output_file, "data/output.txt"))
    
    print("\n📝 Checking file contents...\n")
    
    # Check 7: commands.txt contains "pwd"
    results.append(check_file_contains(commands_file, "pwd", "notes/commands.txt"))
    
    # Check 8: input.txt contains "hello"
    results.append(check_file_contains(input_file, "hello", "data/input.txt"))
    
    # Check 9: output.txt contains "checkpoint"
    results.append(check_file_contains(output_file, "checkpoint", "data/output.txt"))
    
    # Summary
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    
    if all(results):
        print(f"\n🎉 ALL CHECKS PASSED ({passed}/{total})")
        print("\nGreat job! You've mastered the basics of terminal navigation.")
        print("\nNext step: Run 'make lesson 2' to learn Git basics.")
        print("\n" + "=" * 60 + "\n")
        return 0
    else:
        print(f"\n❌ SOME CHECKS FAILED ({passed}/{total} passed)")
        print("\nGo back to the lesson and complete the missing tasks.")
        print("Then run 'make check 1' again.")
        print("\n" + "=" * 60 + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())


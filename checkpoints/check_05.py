#!/usr/bin/env python3
"""
Checkpoint for Lesson 5: Python Packaging & Environments

This script verifies that the student has:
1. Created a virtual environment
2. Created a requirements.txt file
3. The requirements.txt contains pytest
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
    """Check if a file contains specific text (case-insensitive)."""
    if not path.is_file():
        print(f"  ❌ {name} does not exist")
        return False
    
    content = path.read_text().lower()
    if text.lower() in content:
        print(f"  ✅ {name} contains '{text}'")
        return True
    else:
        print(f"  ❌ {name} does not contain '{text}'")
        return False


def check_venv_structure(venv_path: Path) -> bool:
    """Check if venv has the expected structure."""
    bin_dir = venv_path / "bin"
    lib_dir = venv_path / "lib"
    pyvenv_cfg = venv_path / "pyvenv.cfg"
    
    if bin_dir.is_dir() and lib_dir.is_dir() and pyvenv_cfg.is_file():
        print("  ✅ Virtual environment has correct structure")
        return True
    else:
        print("  ❌ Virtual environment is missing expected directories")
        print("     Expected: bin/, lib/, pyvenv.cfg")
        return False


def check_pytest_installed(venv_path: Path) -> bool:
    """Check if pytest is installed in the venv."""
    pytest_path = venv_path / "bin" / "pytest"
    if pytest_path.is_file():
        print("  ✅ pytest is installed in the virtual environment")
        return True
    else:
        print("  ❌ pytest is not installed in the virtual environment")
        print("     Run: source venv/bin/activate && pip install pytest")
        return False


def check_tests_pass(lesson_dir: Path) -> bool:
    """Check if tests pass when run with the venv's pytest."""
    venv_pytest = lesson_dir / "venv" / "bin" / "pytest"
    test_file = lesson_dir / "test_sanity.py"
    
    if not test_file.is_file():
        print("  ⚠️  test_sanity.py not found (optional)")
        return True  # Not a failure, just optional
    
    if not venv_pytest.is_file():
        print("  ❌ Cannot run tests - pytest not in venv")
        return False
    
    try:
        result = subprocess.run(
            [str(venv_pytest), str(test_file), "-v"],
            cwd=lesson_dir,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            print("  ✅ Tests pass when run with venv's pytest")
            return True
        else:
            print("  ❌ Tests failed")
            print(f"     Output: {result.stdout[:200]}")
            return False
    except Exception as e:
        print(f"  ⚠️  Could not run tests: {e}")
        return True  # Don't fail on test execution issues


def main() -> int:
    """Run all checkpoint verifications."""
    print("\n" + "=" * 60)
    print("🔍 Lesson 5 Checkpoint: Python Packaging & Environments")
    print("=" * 60 + "\n")
    
    workspace = get_workspace_path()
    lesson_dir = workspace / "lesson05"
    
    results = []
    
    print("📁 Checking directory structure...\n")
    
    # Check 1: lesson05 directory exists
    results.append(check_directory_exists(lesson_dir, "lesson05/"))
    
    if not lesson_dir.is_dir():
        print("\n" + "=" * 60)
        print("\n❌ Create the lesson05 directory first!")
        print("   mkdir -p workspace/lesson05")
        print("\n" + "=" * 60 + "\n")
        return 1
    
    print("\n🐍 Checking virtual environment...\n")
    
    # Check 2: venv directory exists
    venv_dir = lesson_dir / "venv"
    results.append(check_directory_exists(venv_dir, "venv/"))
    
    # Check 3: venv has correct structure
    if venv_dir.is_dir():
        results.append(check_venv_structure(venv_dir))
        
        # Check 4: pytest is installed
        results.append(check_pytest_installed(venv_dir))
    else:
        results.append(False)
        results.append(False)
    
    print("\n📄 Checking requirements.txt...\n")
    
    # Check 5: requirements.txt exists
    req_file = lesson_dir / "requirements.txt"
    results.append(check_file_exists(req_file, "requirements.txt"))
    
    # Check 6: requirements.txt contains pytest
    if req_file.is_file():
        results.append(check_file_contains(req_file, "pytest", "requirements.txt"))
    else:
        results.append(False)
    
    print("\n🧪 Checking tests...\n")
    
    # Check 7: Tests pass (optional)
    if venv_dir.is_dir():
        check_tests_pass(lesson_dir)  # Don't add to results, it's optional
    
    # Summary
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    
    if all(results):
        print(f"\n🎉 ALL CHECKS PASSED ({passed}/{total})")
        print("\nExcellent! You understand virtual environments.")
        print("\nNext step: Run 'make lesson 6' to learn pytest.")
        print("\n" + "=" * 60 + "\n")
        return 0
    else:
        print(f"\n❌ SOME CHECKS FAILED ({passed}/{total} passed)")
        print("\nGo back to the lesson and complete the missing tasks.")
        print("Then run 'make check 5' again.")
        print("\n" + "=" * 60 + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())


"""
Pytest configuration for the course tests.

This file ensures the src directory is on the Python path.
"""

import sys
from pathlib import Path

# Add src to path so imports work
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


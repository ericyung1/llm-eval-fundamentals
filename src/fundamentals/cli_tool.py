#!/usr/bin/env python3
"""
Lesson 7: CLI Tool - Starter Code

A command-line tool for analyzing text files.

Complete the TODO sections to make the CLI work.

Usage:
    python cli_tool.py <file> [options]

Examples:
    python cli_tool.py input.txt
    python cli_tool.py input.txt --format json
    python cli_tool.py input.txt --uppercase
    python cli_tool.py input.txt --lines 5
"""

import argparse
import json
import sys
from pathlib import Path


def analyze_file(filepath: Path) -> dict:
    """
    Analyze a text file and return statistics.
    
    Args:
        filepath: Path to the file to analyze
    
    Returns:
        Dictionary with file statistics
    """
    text = filepath.read_text()
    lines = text.splitlines()
    words = text.split()
    
    return {
        "filename": filepath.name,
        "lines": len(lines),
        "words": len(words),
        "characters": len(text),
        "content": lines,
    }


def format_output(data: dict, format_type: str, uppercase: bool = False, max_lines: int | None = None) -> str:
    """
    Format the analysis output.
    
    Args:
        data: Analysis data dictionary
        format_type: "text" or "json"
        uppercase: Whether to convert to uppercase
        max_lines: Maximum number of content lines to show
    
    Returns:
        Formatted output string
    """
    # Limit content lines if specified
    if max_lines is not None and max_lines > 0:
        data = data.copy()
        data["content"] = data["content"][:max_lines]
    
    if format_type == "json":
        output = json.dumps(data, indent=2)
    else:
        # Text format
        output_lines = [
            f"File: {data['filename']}",
            f"Lines: {data['lines']}",
            f"Words: {data['words']}",
            f"Characters: {data['characters']}",
            "",
            "Content:",
        ]
        for line in data["content"]:
            output_lines.append(f"  {line}")
        output = "\n".join(output_lines)
    
    if uppercase:
        output = output.upper()
    
    return output


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser.
    
    Returns:
        Configured ArgumentParser
    
    TODO: Complete this function to add the following arguments:
    
    1. Positional argument "file":
       - Type: Path
       - Help: "Path to the text file to analyze"
    
    2. Optional argument "--format" or "-f":
       - Choices: ["text", "json"]
       - Default: "text"
       - Help: "Output format (default: text)"
    
    3. Optional argument "--uppercase" or "-u":
       - Action: store_true (boolean flag)
       - Help: "Convert output to uppercase"
    
    4. Optional argument "--lines" or "-l":
       - Type: int
       - Default: None
       - Help: "Limit number of content lines to display"
    """
    parser = argparse.ArgumentParser(
        description="Analyze text files and display statistics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s myfile.txt                    Analyze file with text output
  %(prog)s myfile.txt --format json      Analyze file with JSON output
  %(prog)s myfile.txt --uppercase        Convert output to uppercase
  %(prog)s myfile.txt --lines 10         Show only first 10 lines of content
        """,
    )
    
    # TODO: Add positional argument "file"
    # Hint: parser.add_argument("file", type=Path, help="...")
    
    # TODO: Add optional argument "--format" / "-f"
    # Hint: parser.add_argument("--format", "-f", choices=[...], default=..., help="...")
    
    # TODO: Add optional argument "--uppercase" / "-u"
    # Hint: parser.add_argument("--uppercase", "-u", action="store_true", help="...")
    
    # TODO: Add optional argument "--lines" / "-l"
    # Hint: parser.add_argument("--lines", "-l", type=int, default=None, help="...")
    
    return parser


def main(argv: list[str] | None = None) -> int:
    """
    Main entry point for the CLI.
    
    Args:
        argv: Command line arguments (None uses sys.argv)
    
    Returns:
        Exit code (0 for success, non-zero for error)
    """
    parser = create_parser()
    args = parser.parse_args(argv)
    
    # TODO: Validate that the file exists
    # Hint: Check if args.file.exists(), if not print error and return 1
    
    # TODO: Call analyze_file with args.file
    # Hint: data = analyze_file(args.file)
    
    # TODO: Call format_output with appropriate arguments
    # Hint: output = format_output(data, args.format, args.uppercase, args.lines)
    
    # TODO: Print the output
    
    # TODO: Return 0 for success
    pass


if __name__ == "__main__":
    sys.exit(main() or 0)


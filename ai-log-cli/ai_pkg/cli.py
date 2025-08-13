#!/usr/bin/env python3
import argparse
from pathlib import Path

def tail_file(path: Path, lines: int = 200) -> str:
    with path.open('r', errors='ignore') as f:
        all_lines = f.readlines()
    return ''.join(all_lines[-lines:])

def main():
    parser = argparse.ArgumentParser(prog="ai", description="AI Log CLI - Part1")
    sub = parser.add_subparsers(dest="cmd")
    
    exp = sub.add_parser("explain", help="Explain errors (part1: tail & print)")
    exp.add_argument("path", help="Path to log/text file")
    exp.add_argument("--lines", type=int, default=200, help="Last N lines to analyze")
    
    args = parser.parse_args()

    if args.cmd != "explain":
        parser.print_help()
        return

    path = Path(args.path)
    if not path.exists() or not path.is_file():
        print(f"Hey this file not found: {path}")
        return

    text = tail_file(path, args.lines)
    print("=== ai :: preview of last", args.lines, "lines ===")
    print(text)

if __name__ == "__main__":
    main()


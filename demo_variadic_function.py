#! usr/bin/env python3
# Author: ABabalola
# Description: This script will be the demo

"""
DOCSTRING
"""
from traceback import print_tb

# Example of a variadic function which accepts
# a variable number of parameters - unpacking them into a TUPLE
def search_word(pattern=r"sage", *files):
    lines_matched = 0
    for file in files:
        with (open(file, mode="rt") as fh_in):
            for (line_num, line) in enumerate(fh_in, start=1):
                if line.isascii() and pattern in line:
                    print(line_num, line, end="")
                    lines_matched += 1
    return lines_matched

total_lines = 0
total_lines += search_word("arash", r"words" , r"words" , r"words")
print(f"Total lines matched =  {total_lines}")

# def function(**kwargs): pass into a dictionary
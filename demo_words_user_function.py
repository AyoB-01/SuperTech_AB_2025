#! usr/bin/env python3
# Author: ABabalola
# Description: This script will be the demo

"""
DOCSTRING
"""
from traceback import print_tb


def search_word(pattern=r"sage", file=r"words"):
    lines_matched = 0
    with (open(file, mode="rt") as fh_in):
        for (line_num, line) in enumerate(fh_in, start=1):
            if line.isascii() and pattern in line:
                print(line_num, line, end="")
                lines_matched += 1
    return lines_matched

search_word("done", r"words")
print("-" * 50)
search_word("banana", r"words")
search_word()

total_lines = 0
total_lines += search_word("done", r"words")
print("-" * 50)
total_lines += search_word()

print(f"Total lines matched =  {total_lines}")

# print is a variadic function can have unlimited number of arguments
# Make Variadic functions the same way you unpact when making sets
# (a, b, *c) = (1,2,[3,4,5,6])

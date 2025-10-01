#! usr/bin/env python3
# Author: ABabalola
# Description: This script will open the words file

"""
DOCSTRING
"""


with open('words', mode='rt') as fh_out:
    DOCSTRING = fh_out.readlines()
    for doc in DOCSTRING:
        if doc.startswith('y'):
            print(doc)
    for lines in DOCSTRING:
        if lines.rstrip('\n').endswith('n'):
            print(lines)
    for string in DOCSTRING:
        if string.__contains__('town'):
            print(string.upper())
    count = 0
    for text in DOCSTRING:
        if text.__contains__('n'):
            print(count)
            print(text)
        count += 1




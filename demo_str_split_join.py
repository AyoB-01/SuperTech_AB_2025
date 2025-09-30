#! usr/bin/env python3
# Author: ABabalola
# Description: This script will demo HOWTO split and rejoin strings
# using the str.split() and str.join() methods.

"""
DOCSTRING
"""

line = "root:x:0:0:The Super User:/root:/bin/bash"

# Strings are immutable
fields = line.split(":") # returns a LIST
fields[4] = "The Administrator"
fields[6] = "/bin/zsh"

print(fields)
line = ":".join(fields)
print(line)

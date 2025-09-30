#! usr/bin/env python3
# Author: ABabalola
# Description: This script will demo HOWTO repeat a BLOCK of
# commands a specfic number of times using a counter loop

"""
DOCSTRING
"""

count = 0
while count < 10:
    count += 1
    print(count)

for num in range(0, 10, 1):
    print(num)

for num in range(0, 10):
    print(num)

for num in range(10):
    print(num)

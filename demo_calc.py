#! usr/bin/env python3
# Author: ABabalola
# Description: This script will be the demo

"""
Multi
line
comment
Multi line string
and DOCUMENTATION
"""

def add(*args):
    """ Return sum of all arguments as a float"""
    sum = 0
    for num in args:
        sum += num
    return sum

def mul(*args):
    """ Return product of all arguments as a float"""
    total = 1
    for num in args:
        total *= num
    return total

def div(x, z):
    """ Return quotient of x divided by z to 3 decimal places """
    return round(x/z, 3)

print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")
print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
print(f"4 / 3 = {div(4, 3)}")

# We could just make a lambda function, simple short function
l_div = lambda x, z:round(x/z, 3)

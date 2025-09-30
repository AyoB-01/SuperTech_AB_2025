#! usr/bin/env python3
# Author: ABabalola
# Description: This script will demo HOWTO iterate through a
# collection/sequence of (str/tuple/list/dict/set) using
# an ITERATOR for loop.

"""
DOCSTRING
"""
import sys

heroes = ['JFK', 'marie antoinette', 'm.jackson', 'ozzie', 'pele',
          'malcom X', 'kobe', 'diana']

for name in heroes:
    print(name, end='\n')

for name in heroes:
    print(name, end='\n')

idx = 0
for name in heroes:
    print(name.upper(), end='\n')
    heroes[idx] = name.upper()
    idx += 1
print('Heroes = ', heroes)

for (idx, name) in enumerate(heroes, start=0):
    print(name.title(), end='\n')
    heroes[idx] = name.title()
print('Heroes = ', heroes)

sys.exit (0) # explicit exit with return code (0 = success, 1-255 = error code)
sys.exit ('Goodbye')  # explicit exit with expression standard red color return code 1

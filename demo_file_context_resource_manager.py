#! usr/bin/env python3
# Author: ABabalola
# Description: This script will emulate how to emulate block scope using
# pythons resource manager

"""
DOCSTRING
"""
movies = {'kymran': ['indiana jones', 'bridget jones', 'mamma mia'],
          'charles': ['puss in boots', 'the last wish', 'django unchained'],
          'diren': ['top gun', 'wolf of wall street', 'rio']
}

with open('movies.txt', mode='wt') as fh_out:

#Iterate through movies keys and write keys: values to file handle

    for name in movies:
        print(name, movies[name])
        fh_out.write(f"{name} {movies[name]} \n")
# End of block, fh_out is closed

print("-"*80)

# fh_in.read reads ENTIRE file into a str. Can run out of RAM
# read(30) reads 30 characters in


# text = fh_in.readline() # Read next ine into str object
#lines = fh_in.readlines() # Read entire file into a list object

# ITERATE through the file handle using a for loop
# File handle is an iterator object
with open('movies.txt', mode='rt') as fh_in:
    for line in fh_in:
        print(line.rstrip('\n'))
        print(line)


#! usr/bin/env python3
# Author: ABabalola
# Description: This script will be the demo
# dict are in INSERTION ORDER from 3.6

"""
DOCSTRING
"""
import pprint

movies = {'kymran': ['indiana jones', 'bridget jones', 'mamma mia'],
          'charles': ['puss in boots', 'the last wish', 'django unchained'],
          'diren': ['top gun', 'wolf of wall street', 'rio']
}

movies['donald'] = ['lotr', 'the hobbit', 'star wars']
pprint.pprint(movies)

movies.popitem() # deletes last item inserted into dict
pprint.pprint(movies)

print(f'{movies['kymran']}')
print(f'{movies['kymran'][0]}')
films = movies.copy()
films.clear()
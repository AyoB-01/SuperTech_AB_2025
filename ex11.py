#! usr/bin/env python3
# Author: ABabalola
# Description: This script will be the demo

"""
DOCSTRING
"""

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print('-'*len(Belgium))
fields = Belgium.split(',')
Belgium = ':'.join(fields)
print(Belgium)
country_city = int(fields[1])+int(fields[3])
print(country_city)


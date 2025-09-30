#! usr/bin/env python3
# Author: ABabalola
# Description: This script will be the demo

"""
DOCSTRING
"""

planets = {"Mercury": 57.91,
           "Venus": 108.9,
           "Earth": 149.597870,
           "Mars": 227.94}

# Iterate through the keys in the planet names and display planet names

for planet in planets.keys():
    print("\t\t" + str(planet) + ": " + str(planets[planet])
          + "Gm\t" + str(hex(0xff)))


print("-"*60)
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12)
          + "Gm\t" + str(hex(0xff)).rjust(6))

print("-"*60)
for planet in planets.keys():
    print("{0:>12s} {1:>12.3f} Gm {2:>#6x}".format(planet, planets[planet], 0xff))

print("-"*60)
for planet in planets.keys():
    print(f"{planet:>12s} {planets[planet]:>12.3f} Gm {0xff:>#6x}")


#! usr/bin/env python3
# Author: ABabalola
# Description: This module defines a class of tank

"""
    Tank Class for a game of tanks
"""

class Tank:
    # Class has 2 components = Attributes/Data + Behaviour/Methods
    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0
        self._health = 100
        self._location = {'x':0, 'y':0, 'z':0}
        self._direction = 0
        self._shells = 20
        #No EXPLICIT RETURN as called implicitly.

    def accel(self, increase):
        self.speed += increase
        return None

    def decel(self, decrease):
        self.speed -= decrease
        return None

    def rotate_left(self, degrees):
        self._direction -= degrees
        return None
    def rotate_right(self, degrees):
        self._direction += degrees
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None


def main():
    return None

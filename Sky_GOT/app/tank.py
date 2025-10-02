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
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
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

    # Some SPECIAL methods..
    # Example of OPERATOR OVERLOADING
    def __add__(self, other):
        return self._health + other._health

    def __str__(self):
        return f"Model = {self.model}, Country = {self.country}, Speed = {self._speed}"

    # Example of GETTER and SETTER methods..
    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = new_health
        return None


#! usr/bin/env python3
# Author: ABabalola
# Description: This script will be the demo

"""
    Docstring:
"""


class Vehicle:

    def __init__(self, country, model):
        self.country = country
        self.model = model


    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
        return None
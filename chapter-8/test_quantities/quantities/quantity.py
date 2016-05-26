""" quantities.quantitity

    This module encapsulates the concept of a `quantity`.  A quantity is a
    number along with the units that number is in.
"""
class Quantity(object):
    def __init__(self, value, units):
        self.value = value
        self.units = units

    def __str__(self):
        return "{} {}".format(self.value, self.units)


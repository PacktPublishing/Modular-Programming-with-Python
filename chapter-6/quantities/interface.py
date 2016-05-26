""" quantities.interface

    This module defines the public interface for the `quantities` package.
"""
from .units    import UNITS, localize, find_unit
from .quantity import Quantity

#############################################################################

def init(locale):
    """ Initialize the 'quantities' package.

        'locale' is the locale to use for calculating and parsing quantities.
        The following locale values are currently supported:

            "us"
            "international"
    """
    global _locale
    _locale = locale


def new(value, units):
    """ Create and return a new Quantity object.
    """
    global _locale
    kind,unit = find_unit(units, _locale)
    if kind == None:
        raise ValueError("Unknown unit: {}".format(units))

    return Quantity(value, localize(unit['name'], _locale))


def parse(s):
    """ Attempt to parse the given string into a Quantity.

        Raises a ValueError if the string can't be parsed into a quantity using
        the current locale.
    """
    global _locale

    sValue,sUnits = s.split(" ", maxsplit=1)
    value = float(sValue)

    kind,unit = find_unit(sUnits, _locale)
    if kind == None:
        raise ValueError("Unknown unit: {}".format(sUnits))

    return Quantity(value, localize(unit['name'], _locale))


def kind(q):
    """ Return the kind of unit represented by the given quantity.
    """
    global _locale
    kind,unit = find_unit(q.units, _locale)
    return kind


def value(q):
    """ Return the value of the given quantity.
    """
    return q.value


def units(q):
    """ Return the units for the given quantity.
    """
    return q.units


def convert(q, units):
    """ Attempt to convert the given quantity into the given units.

        Upon completion, we return a new quantity converted into the given
        units.  If the quantity cannot be converted (for example, because the
        units are incompatible), we raise a ValueError.
    """
    global _locale

    src_kind,src_units = find_unit(q.units, _locale)
    dst_kind,dst_units = find_unit(units, _locale)

    if src_kind == None:
        raise ValueError("Unknown units: {}".format(q.units))
    if dst_kind == None:
        raise ValueError("Unknown units: {}".format(units))

    if src_kind != dst_kind:
        raise ValueError("It's impossible to convert {} into {}!".format(
                            localize(src_units['plural'], _locale),
                            localize(dst_units['plural'], _locale)))

    num_units = q.value * src_units['num_units'] / dst_units['num_units']
    return Quantity(num_units, localize(dst_units['name'], _locale))


def supported_kinds():
    """ Return a list of the various kinds of units that we support.
    """
    return list(UNITS.keys())


def supported_units(kind):
    """ Return a list of the various units of the given kind that we support.
    """
    global _locale

    units = []
    for unit in UNITS.get(kind, []):
        units.append(localize(unit['name'], _locale))
    return units


""" units.py

    This module defins the various units supported by the `quantities` package.

    The 'UNITS' global holds all the defined units.  This is a dictionary
    mapping the kind of units (ie, "weight", "length", etc) to a list of the
    known units of that kind.

    For each unit, the list item will be a dictionary with the following
    entries:

        'abbreviation'

            The abbreviation for this unit.

        'name'

            The singular name for this unit.

        'plural'

            The plural form of the name.

        'num_units'

            The conversion factor to apply to this unit.  Note that one unit of
            each kind must have a conversation factor of 1, and all other units
            of that kind must be a multiple of that unit.

    Note that any of these four values can either be a single value, or a
    dictionary used to localize that value.  If a value (ie, an abbreviation, a
    name, a plural name, or the number of units) is localized, then the entry
    will be a dictionary mapping each locale to the value to use for that
    locale.

    Locales are used to customize the names and abbreviations used for a unit
    depending on where in the world the user is.  They are also use to
    distingush between US measurements and international measurements, in the
    cases where they differ.  The following locales are currently supported:

        us
        international
"""

UNITS = {}

#############################################################################

# Helper functions:

def by_locale(value_for_us, value_for_international):
    """ Return a dictionary mapping "us" and "international" to the two values.

        This is used to create locale-specific values within our UNITS.
    """
    return {"us"            : value_for_us,
            "international" : value_for_international}


def unit(*args):
    """ Create a unit dictionary.

        Call with (abbreviation, name, units) or (abbreviation, name, plural
        name, units).  If the plural name is not given, it is calculated by
        adding "s" to the singular name.  Note that the abbreviation, name,
        plural name (if given) and units can all be either a value or a
        dictionary mapping locales to values.
    """
    if len(args) == 3:
        abbreviation = args[0]
        name         = args[1]

        if isinstance(name, dict):
            plural = {}
            for key,value in name.items():
                plural[key] = value + "s"
        else:
            plural = name + "s"

        num_units = args[2]
    elif len(args) == 4:
        abbreviation = args[0]
        name         = args[1]
        plural       = args[2]
        num_units    = args[3]
    else:
        raise RuntimeError("Bad arguments to unit(): {}".format(args))

    return {'abbreviation' : abbreviation,
            'name'         : name,
            'plural'       : plural,
            'num_units'    : num_units}


def units(kind, *units_to_add):
    """ Add a list of units to the UNITS global.

        All the added units will be of given kind.
    """
    if kind not in UNITS:
        UNITS[kind] = []

    for unit in units_to_add:
        UNITS[kind].append(unit)

#############################################################################

# Units of weight:

units("weight",
      unit("g",  "gram",     1),
      unit("kg", "kilogram", 1000),
      unit("oz", "ounce", 28.349523125),
      unit("lb", "pound", 453.59237))

# Units of length:

units("length",
      unit("mm", by_locale("millimeter", "millimetre"), 0.1),
      unit("cm", by_locale("centimeter", "centimetre"), 1),
      unit("m",  by_locale("meter",      "metre"),      100),
      unit("km", by_locale("kilometer",  "kilometre"),  100000),
      unit("in", "inch", "inches", 2.54),
      unit("ft", "foot", "feet", 30.48),
      unit("yd", "yard", 91.44),
      unit("mi", "mile", 160934.4))

# Units of area:

units("area",
      unit("sq cm", by_locale("square centimeter",
                              "square centimetre"), 0.0001),
      unit("sq m",  by_locale("square meter",
                              "square metre"),      1),
      unit("ha",    "hectare",                      10000),
      unit("sq km", by_locale("square kilometer",
                              "square kilometre"),  1000000),
      unit("sq in", "square inch", "square inches", 0.00064516),
      unit("sq ft", "square foot", "square feet",   0.09290304),
      unit("sq mi", "square mile",                  2589988.110336),
      unit("a",     "acre",                         4046.8564224))

# Units of volume:

units("volume",
      unit("cc",   by_locale("cubic centimeter",
                             "cubic centimetre"),  1),
      unit("l",    by_locale("liter",
                             "litre"),             1000),
      unit("ml",   by_locale("milliliter",
                             "millilitre"),        1),
      unit("c",    "cup", by_locale(236.5882365, 250)),
      unit("dsp",  "dessert spoon", by_locale(9.857843187066, 11.8387809397)),
      unit("tsp",  "teaspoon", by_locale(4.92892159375, 5.0)),
      unit("tbsp", "tablespoon", by_locale(14.78676478125, 15.0)),
      unit("cu ft", "cubic foot", "cubic feet",   28316.846592),
      unit("cu in", "cubic inch", "cubic inches", 16.387064),
      unit("cu yd", "cubic yard",                 764554.857984),
      unit("fl oz", "fluid ounce", by_locale(29.5735295625, 28.4130625)),
      unit("gal",   "gallon",      by_locale(3785.411784, 4546.09)),
      unit("pt",    "pint",        by_locale(473.176473, 568.26125)),
      unit("qt",    "quart",       by_locale(946.352946, 1136.5225)))

#############################################################################

def localize(value, locale):
    """ Return the value appropriate for the current locale.

        This is used to retrieve the appropriate localized version of a value
        defined within a unit's dictionary.

        If 'value' is a dictionary, we assume it is a mapping of locale names
        to values, so we select the appropriate dictionary entry based on the
        locale.  Otherwise, we return 'value' directly, as the value hasn't
        been localized.
    """
    if isinstance(value, dict):
        return value.get(locale)
    else:
        return value


def find_unit(s, locale):
    """ Find the unit with the given name or abbrevation.

        We search through the UNITS dictionary for any unit which has a
        (possibly localized) singular or plural name or abbreviation matching
        the string 's'.  If we find one, we return a (kind, unit) tuple, where
        'kind' is the kind of unit and 'unit' is the dictionary entry for
        this unit.

        If we can't find any unit with that name or abbreviation, we return
        (None, None).
    """
    s = s.lower()
    for kind in UNITS.keys():
        for unit in UNITS[kind]:
            if (s == localize(unit['abbreviation'], locale).lower() or
                s == localize(unit['name'], locale).lower() or
                s == localize(unit['plural'], locale).lower()):
                # Success!
                return (kind, unit)

    return (None, None) # Not found.


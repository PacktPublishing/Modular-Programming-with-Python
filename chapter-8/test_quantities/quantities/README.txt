About the `quantities` package
------------------------------

The `quantities` package allows you to define and work with various quantities.
A quantity is a number along with an associated unit, for example:

    6 inches
    21.2 square kilometers
    0.75 cups

Using this package, you can define new quantities using the `quantities.new()`
function, or convert a string into a quantity using `quantities.parse()`.  For
example:

    >>> q1 = quantities.new(6, "inch")
    >>> q2 = quantities.parse("21.2 square kilometers")
    >>> q3 = quantities.new(0.75, "cups")

You can then retrieve information about these quantities by calling the
appropriate functions, for example:

    >>> print(quantities.kind(q1))
    length
    >>> print(quantities.value(q2))
    25
    >>> print(quantities.units(q3)
    cup

You can also print a quantity directly to get a summary of its contents:

    >>> print(q1)
    6 inch

Once you have a quantity, you can convert it into a new quantity in any
compatible unit.  For example:

    >>> print(quantities.convert(q1, "mm"))
    152.4
    >>> print(quantities.convert(q2, "hectare"))
    100.0
    >>> print(quantities.convert(q3, "inch"))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: float() argument must be a string or a number
    ValueError: It's impossible to convert cups into inches!

Finally, you can retrieve a list of the available kinds of units by calling
`quantities.supported_kinds()`, and get a list of the available units of a
given kind by calling `quantities.supported_units()`.  For example:

    >>> print(quantities.supported_kinds())
    ("weight", "length", "area", "volume")
    >>> print(quantities.supported_units("weight"))
    ("gram", "kilogram", "ounce", "pound")


Installing and using the `quantities` package
---------------------------------------------

The `quantities` package has no external dependencies, and is compatible with
both Python 2 and Python 3.  To install it, simply place the `quantities`
package directory somewhere on your Python path.

Before you can create and use quantity values, make sure you initialize the
package by calling the `quantities.init()` function.  This function takes a
`locale` value as its parameter; the locale is used to customize the spelling
of the various units, as well as allow for different unit conversion factors
depending on where in the world you are.  For example, in the US a cup is
measured as 236.5882365 cubic centimeters, while in the rest of the world a cup
is 250 cubic centimeters.

The `quantities` package currently supports two locales: "us" and
"international".  Make sure you choose the appropriate locale when calling the
`quantities.init()` function to initialize the package.


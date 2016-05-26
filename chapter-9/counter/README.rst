About the ``counter`` package
-----------------------------

``counter`` is a package designed to make it easy to keep track of the number
of times some event or object occurs.  Using this package, you **reset** the
counter, **add** the various values to the counter, and then retrieve the
calculated **totals** to see how often each value occurred.

For example, imagine that you wanted to keep a count of the number of cars of
each color were observed in a given timeframe.  You would start by making the
following call::

    counter.reset()

Then when you identify a car of a given color, you would make the following
call::

    counter.add(color)

Finally, once the time period is over, you would obtain the various colours and
how often they occurred in the following way::

    for color,num_occurrences in counter.totals():
        print(color, num_occurrences)

The counter can then be reset to start counting another set of values.

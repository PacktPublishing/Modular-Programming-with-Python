# This module implements the public interface to the "counter" package.

def reset():
    """ Reset our counter.

        This should be called before we start counting.
    """
    global _counts
    _counts = {} # Maps value to number of occurrences.


def add(value):
    """ Add the given value to our counter.
    """
    global _counts

    try:
        _counts[value] += 1
    except KeyError:
        _counts[value] = 1


def totals():
    """ Return the number of times each value has occurred.

        We return a list of (value, num_occurrences) tuples, one
        for each unique value included in the count.
    """
    global _counts

    results = []
    for value in sorted(_counts.keys()):
        results.append((value, _counts[value]))
    return results


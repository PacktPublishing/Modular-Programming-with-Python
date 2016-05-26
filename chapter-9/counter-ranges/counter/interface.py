# This module implements the public interface to the "counter" package.

def reset(ranges=None):
    """ Reset our counter.

        If 'ranges' is supplied, the given list of values will be used as the
        start and end of each range of values.  In this case, the totals will
        be calculated based on a range of values rather than individual values.

        This should be called before we start counting.
    """
    global _ranges
    global _counts

    _ranges = ranges
    _counts = {} # If _ranges is None, maps value to number of occurrences.
                 # Otherwise, maps (min_value,max_value) to number of
                 # occurrences.


def add(value):
    """ Add the given value to our counter.
    """
    global _ranges
    global _counts

    if _ranges == None:
        key = value
    else:
        key = None
        for i in range(len(_ranges)-1):
            if value >= _ranges[i] and value < _ranges[i+1]:
                key = (_ranges[i], _ranges[i+1])
                break
        if key == None:
            raise RuntimeError("Value out of range: {}".format(value))

    try:
        _counts[key] += 1
    except KeyError:
        _counts[key] = 1


def totals():
    """ Return the number of times each value has occurred.

        If we are currently counting ranges of values, we return a list of
        (min_value, max_value, num_occurrences) tuples, one for each range.
        Otherwise, we return a list of (value, num_occurrences) tuples, one for
        each unique value included in the count.
    """
    global _ranges
    global _counts

    if _ranges != None:
        results = []
        for i in range(len(_ranges)-1):
            min_value = _ranges[i]
            max_value = _ranges[i+1]
            num_occurrences = _counts.get((min_value, max_value), 0)
            results.append((min_value, max_value, num_occurrences))
        return results
    else:
        results = []
        for value in sorted(_counts.keys()):
            results.append((value, _counts[value]))
        return results


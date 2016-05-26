# cache.py

import datetime

MAX_CACHE_SIZE = 100 # Maximum number of entries in the cache.

#############################################################################

def init():
    global _cache
    _cache = {} # Maps key to (timestamp, value) tuple.


def set(key, value):
    global _cache
    if key not in _cache and len(_cache) >= MAX_CACHE_SIZE:
        _remove_oldest_entry()
    _cache[key] = [datetime.datetime.now(), value]


def get(key):
    global _cache
    if key in _cache:
        _cache[key][0] = datetime.datetime.now()
        return _cache[key][1]
    else:
        return None


def contains(key):
    global _cache
    return key in _cache


def size():
    global _cache
    return len(_cache)

#############################################################################

# Private functions:

def _remove_oldest_entry():
    global _cache
    oldest = None
    for key in _cache.keys():
        if oldest == None:
            oldest = key
        elif _cache[key][0] < _cache[oldest][0]:
            oldest = key

    if oldest != None:
        del _cache[oldest]


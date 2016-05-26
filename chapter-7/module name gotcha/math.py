# This is a badly-named module.  It might do math-related things, but by having
# the same name as a Standard Library module, it masks that module, causing
# other parts of the Python Standard Library to crash.

def double(n):
    return n * 2


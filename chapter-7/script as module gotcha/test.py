# This program demonstrates how using a Python source file as both a module and
# a script can lead to subtle errors.  In this example, we define a function
# which does something useful, and also have a __main__ section so we can be
# executed as a script.  When executed, this module imports a second module,
# helpers.py, which is supposed to test out the program.  The helpers.py module
# then imports test.py, causing this module to be initialized twice.

import helpers

print("Initializing test.py")

def do_something(n):
    return n * 2

if __name__ == "__main__":
    helpers.run_test()


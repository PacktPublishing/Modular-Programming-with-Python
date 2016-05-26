# This module shows how to access and change global variables within a package.

from . import globals

def test():
    globals.language = "EN"
    globals.currency = "NZD"
    print(globals.language, globals.currency)


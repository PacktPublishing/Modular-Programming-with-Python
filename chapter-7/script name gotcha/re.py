# This program demonstrates how a poorly-named script can mask a module in the
# python Standard Library.

import re

pattern = input("Regular Expression:")
s = input("String:")

results = re.search(pattern, s)

print(results.group(), results.span())


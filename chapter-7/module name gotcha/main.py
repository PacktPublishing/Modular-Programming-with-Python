# This program demonstrates how a poorly-named module within a program (in this
# case, "math.py" can mask a module in the Python Standard Library, causing
# subtle problems.

import random
print(random.choice(["yes", "no"]))


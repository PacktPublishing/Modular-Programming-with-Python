# This program demonstrates how importing a module more than once won't lead to
# multiple copies of that module.

print("Calling import package.module...")
import package.module
print("Calling import package.module as module...")
import package.module as module
print("Calling from package import module...")
from package import module

# This program demonstrates how adding a package directly to sys.path can cause
# problems with double-importing modules.

import os.path
import sys

cur_dir = os.path.abspath(os.path.dirname(__file__))
package_dir = os.path.join(cur_dir, "package")

sys.path.insert(1, package_dir) # Add package directly to path.  DON'T DO THIS!

print("Calling import package.module as module...")
import package.module as module
print("Calling import module...")
import module


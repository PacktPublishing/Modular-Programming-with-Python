# This module implements the public interface for the "datapackage" directory.
#
# This demonstrates how a Python package can contain data files, which can then
# be accessed as desired.

import os.path

def get_phone_numbers():
    phone_numbers = []
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    file = open(os.path.join(cur_dir, "data", "phone_numbers.txt"))
    for line in file:
        phone_numbers.append(line.strip())
    file.close()
    return phone_numbers


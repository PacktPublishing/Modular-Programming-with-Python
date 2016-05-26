# Simple test module for the "package" package.

import string
import random

def random_name():
    chars = []
    for i in range(random.randrange(3, 10)):
        chars.append(random.choice(string.ascii_letters))
    return "".join(chars)


def run():
    for i in range(10):
        print(random_name())


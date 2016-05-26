import re

def extract_numbers(s):
    pattern = r'[+-]?\d+(?:\.\d+)?'
    numbers = []
    for match in re.finditer(pattern, s):
        number = s[match.start():match.end()]
        numbers.append(number)
    return numbers


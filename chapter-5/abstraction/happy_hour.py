# happy_hour.py
#
# This program demonstrates how to calculate "happy hour", where happy hour
# takes place each day between 5 and 6 pm, except on Sundays, Christmas Day and
# Easter.

import datetime

#############################################################################

def is_happy_hour():
    today = datetime.date.today()

    easter_sunday = calc_easter_sunday(today.year)
    easter_friday = easter_sunday - datetime.timedelta(days=2)

    if today == easter_friday:
        return False

    if today.month == 12 and today.day == 25: # Christmas day.
        return False

    if today.weekday() == 6: # Sunday.
        return False

    if datetime.datetime.now().hour == 17: # 5pm.
        return True

    return False

#############################################################################

# The following function calculates Easter Sunday for a given year, returning a
# datetime.date object.  This code is taken from:
#
#     http://code.activestate.com/recipes/576517

def calc_easter_sunday(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1    
    return datetime.date(year, month, day)

#############################################################################

if __name__ == "__main__":
    # Testing code.

    if is_happy_hour():
        print "It's happy hour!"
    else:
        print "It's not happy hour."


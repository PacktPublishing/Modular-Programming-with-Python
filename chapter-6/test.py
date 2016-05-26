# test.py
#
# Simple testing program for the quantities package.

import quantities

quantities.init("us")

#q = quantities.new(3, "inches")
#print(q)
#print(quantities.kind(q))
#print(quantities.convert(q, "cm"))
#
#q1 = quantities.new(6, "inch")
#q2 = quantities.new(10, "cm")
#print(quantities.add(q1, q2))
#print(quantities.subtract(q1, q2))

print(quantities.parse("15 liters"))


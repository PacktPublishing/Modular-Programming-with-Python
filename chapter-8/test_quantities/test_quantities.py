# test_quantities.py
#
# This Python script performs various unit tests on the `quantities` package.

import unittest
import quantities

class TestQuantities(unittest.TestCase):
    def setUp(self):
        quantities.init("us")

    def test_new(self):
        q = quantities.new(12, "km")
        self.assertEqual(quantities.value(q), 12)
        self.assertEqual(quantities.units(q), "kilometer")

    def test_convert(self):
        q1 = quantities.new(12, "km")
        q2 = quantities.convert(q1, "m")
        self.assertEqual(quantities.value(q2), 12000)
        self.assertEqual(quantities.units(q2), "meter")

        q = quantities.new(12, "km")
        with self.assertRaises(ValueError):
            quantities.convert(q, "kg")

if __name__ == "__main__":
    unittest.main()

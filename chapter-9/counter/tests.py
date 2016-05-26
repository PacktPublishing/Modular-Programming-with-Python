# This module implements various unit tests for the ``counter`` package.

import unittest

import counter

class CounterTestCase(unittest.TestCase):
    """ Unit tests for the ``counter`` package.
    """
    def test_counter_totals(self):
        counter.reset()
        counter.add(1)
        counter.add(2)
        counter.add(3)
        counter.add(1)
        self.assertEqual(counter.totals(), [(1, 2), (2, 1), (3, 1)])

    def test_counter_reset(self):
        counter.reset()
        counter.add(1)
        counter.reset()
        counter.add(2)
        self.assertEqual(counter.totals(), [(2, 1)])


if __name__ == "__main__":
    unittest.main()


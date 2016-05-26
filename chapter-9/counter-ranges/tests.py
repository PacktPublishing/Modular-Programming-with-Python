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


class RangeCounterTestCase(unittest.TestCase):
    """ Unit tests for the range-based features of ``counter`` package.
    """
    def test_range_totals(self):
        counter.reset([0, 5, 10, 15])
        counter.add(3)
        counter.add(9)
        counter.add(4.5)
        counter.add(12)
        counter.add(14.2)
        counter.add(8)
        self.assertEqual(counter.totals(),
                         [(0, 5, 2), (5, 10, 2), (10, 15, 2)])

    def test_out_of_range(self):
        counter.reset([0, 5, 10, 15])
        with self.assertRaises(RuntimeError):
            counter.add(19.1)


if __name__ == "__main__":
    unittest.main()


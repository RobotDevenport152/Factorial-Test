"""
Week 11 Activity 3.py
This module performs basic arithmetic operations: addition, subtraction, and multiplication.
It includes examples for doctesting and can also be tested using unittest.
Doctest examples:

>>> add(10, 5)
15
>>> add(-4, 9)
5
>>> minus(12, 7)
5
>>> minus(3, 9)
-6
>>> multiply(4, 6)
24
>>> multiply(-2, 5)
-10
"""

import doctest
import unittest


def multiply(x, y):
    """Return the product of x and y.

    >>> multiply(3, 5)
    15
    >>> multiply(0, 9)
    0
    >>> multiply(-4, 2)
    -8
    """
    return x * y


def add(x, y):
    """Return the sum of x and y.

    >>> add(10, 5)
    15
    >>> add(-3, 7)
    4
    >>> add(0, 0)
    0
    """
    return x + y


def minus(x, y):
    """Return the difference of x and y.

    >>> minus(8, 5)
    3
    >>> minus(2, 10)
    -8
    >>> minus(-4, -9)
    5
    """
    return x - y


# -----------------------------
# Unit Testing Section
# -----------------------------
class TestMathOperations(unittest.TestCase):
    """Unit tests to verify the correctness of arithmetic operations."""

    def test_multiply(self):
        self.assertEqual(multiply(6, 4), 24)
        self.assertEqual(multiply(-3, 7), -21)
        self.assertEqual(multiply(0, 25), 0)

    def test_add(self):
        self.assertEqual(add(9, 6), 15)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 0), 0)

    def test_minus(self):
        self.assertEqual(minus(15, 8), 7)
        self.assertEqual(minus(-10, 4), -14)
        self.assertEqual(minus(0, 12), -12)


if __name__ == '__main__':
    # Run doctests first
    doctest.testmod(verbose=True)
    print("\nDoctests completed successfully!")

    # Then run unittests
    print("\nRunning unittests...")
    unittest.main(argv=[''], verbosity=2, exit=False)

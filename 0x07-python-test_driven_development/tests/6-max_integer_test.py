#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    test file for my function
    """
    def maxnumber(self):
        s = [1, 2, 3, 4]
        self.assertEqual(max_integer(s), 4)

    def maxnumbernotsorted(self):
        d = [1, 3, 4, 2]
        self.assertEqual(max_integer(d), 4)

    def emptylist(self):
        q = []
        self.assertEqual(max_integer(q), None)

    def justoneelement(self):
        x = [2]
        self.assertEqual(max_integer(x), 2)

    def floatnumber(self):
        z = [11.3, 55.6, 2.5]
        self.assertEqual(max_integer(z), 55.6)

    def intwithfloat(self):
        a = [4, 7.6, 9, 12.4]
        self.assertEqual(max_integer(a), 12.4)

    def string(self):
        b = "hazemzoome"
        self.assertEqual(max_integer(b), z)

    def emptystring(self):
        n = ""
        self.assertEqual(max_integer(n), None)

    def listofstring(self):
        i = ["hazem", "zoome", "love"]
        self.assertEqual(max_integer(i), "zoome")


if __name__ == '__main__':
    unittest.main()

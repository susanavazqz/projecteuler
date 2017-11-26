import unittest
from problems import p1
from problems import p2


class Problem1TestCase(unittest.TestCase):
    """Tests for `problem1.py`."""
    def setUp(self):
        self.problem1 = p1.problem1()
        self.problem2 = p2.problem2()

    def test_problem1(self):
        self.assertEqual(self.problem1, 233168), 'Error!'

    def test_problem2(self):
        self.assertEqual(self.problem2, 0), 'Error!'

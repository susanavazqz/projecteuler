import unittest
from problems import p1


class Problem1TestCase(unittest.TestCase):
    """Tests for `problem1.py`."""
    def setUp(self):
        self.problem1 = p1.problem1()

    def test_problem1(self):
        self.assertEqual(self.problem1, 233168), 'Error!'

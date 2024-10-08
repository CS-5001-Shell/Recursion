import unittest
from io import StringIO
from sum_before import sum_before

class TestSumBefore(unittest.TestCase):

    def test_sum_before_true(self):
        self.assertTrue(sum_before([1, 2, 3, 4]))

    def test_sum_before_false(self):
        self.assertFalse(sum_before([1, 2, 2, 2]))

    def test_sum_before_no_items(self):
        self.assertFalse(sum_before([]))

    def test_sum_before_only_0(self):
        self.assertTrue(sum_before([0]))

    def test_sum_before_all_items(self):
        self.assertTrue(sum_before([1, 2, 3, 4, 10]))

    def test_sum_before_negative(self):
        self.assertTrue(sum_before([1, 2, -4, 5, 4, 6, 7]))

if __name__ == '__main__':
    unittest.main()

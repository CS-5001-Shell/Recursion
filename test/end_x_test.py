import unittest
from io import StringIO
from end_x import end_x

class TestEndX(unittest.TestCase):

    def test_end_x_beginning(self):
        self.assertEqual(end_x('xxre'), 'rexx')

    def test_end_x_end(self):
        self.assertEqual(end_x('rexx'), 'rexx')

    def test_end_x_no_x(self):
        self.assertEqual(end_x('capybara'), 'capybara')

    def test_end_x_beginning_and_end(self):
        self.assertEqual(end_x('xxcapybaraxx'), 'capybaraxxxx')

    def test_end_x_middle(self):
        self.assertEqual(end_x('capyxxbara'), 'capybaraxx')

if __name__ == '__main__':
    unittest.main()

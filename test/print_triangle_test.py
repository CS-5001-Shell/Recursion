import unittest
from unittest import mock
from unittest.mock import patch
from io import StringIO
from print_triangle import print_triangle

class TestPrintTriangle(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_triangle_one(self, mock_stdout):
        print_triangle(1)
        
        actual_output = mock_stdout.getvalue()
        
        expected_output = '0\n'
        
        self.assertEqual(actual_output, expected_output)
   
    @patch('sys.stdout', new_callable=StringIO)
    def test_print_triangle_two(self, mock_stdout):
        print_triangle(2)
        
        actual_output = mock_stdout.getvalue()
        
        expected_output = '0\n01\n0\n'
        
        self.assertEqual(actual_output, expected_output)


    @patch('sys.stdout', new_callable=StringIO)
    def test_print_triangle_five(self, mock_stdout):
        print_triangle(5)
        
        actual_output = mock_stdout.getvalue()
        
        expected_output = '0\n01\n012\n0123\n01234\n0123\n012\n01\n0\n'
        
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()

import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from algorithms.easy import sum_of_digits_of_string_after_convert

class Tester(unittest.TestCase):
    
    def test1(self):
        s = "iiii"
        k = 1
        output = 36
        self.assertEqual(sum_of_digits_of_string_after_convert.getLucky(self, s, k), output)

    def test2(self):
        s = "leetcode"
        k = 2
        output = 6
        self.assertEqual(sum_of_digits_of_string_after_convert.getLucky(self, s, k), output)

    def test3(self):
        s = "zbax"
        k = 2
        output = 8
        self.assertEqual(sum_of_digits_of_string_after_convert.getLucky(self, s, k), output)

if __name__ == '__main__':
    unittest.main()
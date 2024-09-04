import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from algorithms.medium import find_the_duplicate_number

class TestFindTheStudentThatWillReplaceTheChalk(unittest.TestCase):

  def test1(self):
    nums = [1,3,4,2,2]
    output = 2
    self.assertEqual(find_the_duplicate_number.findDuplicate(self, nums), output)

  def test2(self):
    nums = [3,1,3,4,2]
    output = 3
    self.assertEqual(find_the_duplicate_number.findDuplicate(self, nums), output)

  def test3(self):
    nums = [3,3,3,3,3]
    output = 3
    self.assertEqual(find_the_duplicate_number.findDuplicate(self, nums), output)

if __name__ == '__main__':
  unittest.main()
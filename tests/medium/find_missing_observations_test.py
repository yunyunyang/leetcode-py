import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from algorithms.medium import find_missing_observations

class TestFindTheStudentThatWillReplaceTheChalk(unittest.TestCase):

  def test1(self):
    rolls = [3,2,4,3]
    mean = 4
    n = 2
    output = [6,6]
    self.assertEquals(sorted(find_missing_observations.missingRolls(self, rolls, mean, n)), sorted(output))

  def test2(self):
    rolls = [1,5,6]
    mean = 3
    n = 4
    output = [2,3,2,2]
    self.assertEqual(sorted(find_missing_observations.missingRolls(self, rolls, mean, n)), sorted(output))

  def test3(self):
    rolls = [1,2,3,4]
    mean = 6
    n = 4
    output = []
    self.assertEqual(sorted(find_missing_observations.missingRolls(self, rolls, mean, n)), sorted(output))

if __name__ == '__main__':
  unittest.main()
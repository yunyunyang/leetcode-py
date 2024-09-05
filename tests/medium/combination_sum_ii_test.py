import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from algorithms.medium import combination_sum_ii

class Tester(unittest.TestCase):

  def test1(self):
    candidates = [10,1,2,7,6,1,5]
    target = 8
    output = [[1,1,6], [1,2,5], [1,7], [2,6]]
    self.assertEquals(sorted(combination_sum_ii.combinationSum2(self, candidates, target)), sorted(output))

  def test2(self):
    candidates = [2,5,2,1,2]
    target = 5
    output = [[1,2,2], [5]]
    self.assertEquals(sorted(combination_sum_ii.combinationSum2(self, candidates, target)), sorted(output))

if __name__ == '__main__':
  unittest.main()
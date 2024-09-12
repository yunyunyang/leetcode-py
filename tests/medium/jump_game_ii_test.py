import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from algorithms.medium import jump_game_ii

class Tester(unittest.TestCase):

  def test1(self):
    nums = [2,3,1,1,4]
    output = 2
    self.assertEquals(jump_game_ii.jump(self, nums), output)

  def test2(self):
    nums = [2,3,0,1,4]
    output = 2
    self.assertEquals(jump_game_ii.jump(self, nums), output)

if __name__ == '__main__':
  unittest.main()
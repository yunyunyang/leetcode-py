import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from algorithms.medium import pow_x_n

class Tester(unittest.TestCase):

  def test1(self):
    x = 2.00000
    n = 10
    output = 1024.00000
    self.assertEquals(round(pow_x_n.myPow(self, x, n), 5), output)

  def test2(self):
    x = 2.10000
    n = 3
    output = 9.26100
    self.assertEquals(round(pow_x_n.myPow(self, x, n), 5), output)

  def test3(self):
    x = 2.00000
    n = -2
    output = 0.25000
    self.assertEquals(round(pow_x_n.myPow(self, x, n), 5), output)

if __name__ == '__main__':
  unittest.main()
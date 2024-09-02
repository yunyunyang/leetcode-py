import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from algorithms.medium import find_the_student_that_will_replace_the_chalk

class TestFindTheStudentThatWillReplaceTheChalk(unittest.TestCase):

  def setUp(self):
    print('This is called immediately before calling the test method.')

  def tearDown(self):
    print('Method called immediately after the test method has been called and the result recorded.')

  def test1(self):
    chalk = [5,1,5]
    k = 22
    output = 0
    self.assertEqual(find_the_student_that_will_replace_the_chalk.chalkReplacer(self, chalk, k), output)

  def test2(self):
    chalk = [3,4,1,2]
    k = 25
    output = 1
    self.assertEqual(find_the_student_that_will_replace_the_chalk.chalkReplacer(self, chalk, k), output)

  def test3(self):
    chalk = [1]
    k = 1000000000
    output = 0
    self.assertEqual(find_the_student_that_will_replace_the_chalk.chalkReplacer(self, chalk, k), output)

if __name__ == '__main__':
  unittest.main()
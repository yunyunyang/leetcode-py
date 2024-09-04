import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from algorithms.medium import walking_robot_simulation

class Tester(unittest.TestCase):

  def test1(self):
    commands = [4,-1,3]
    obstacles = []
    output = 25
    self.assertEqual(walking_robot_simulation.robotSim(self, commands, obstacles), output)

  def test2(self):
    commands = [4,-1,4,-2,4]
    obstacles = [[2,4]]
    output = 65
    self.assertEqual(walking_robot_simulation.robotSim(self, commands, obstacles), output)

  def test3(self):
    commands = [6,-1,-1,6]
    obstacles = []
    output = 36
    self.assertEqual(walking_robot_simulation.robotSim(self, commands, obstacles), output)

if __name__ == '__main__':
  unittest.main()
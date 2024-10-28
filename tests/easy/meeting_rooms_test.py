import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from algorithms.easy import meeting_rooms
from algorithms.easy.meeting_rooms import Interval

class Tester(unittest.TestCase):
    
    def test1(self):
        intervals = [Interval(1, 30), Interval(5,10), Interval(15,20)]
        output = False
        self.assertFalse(meeting_rooms.can_attend_meetings(self, intervals))

    def test2(self):
        intervals = [Interval(5,8), Interval(9,15)]
        self.assertTrue(meeting_rooms.can_attend_meetings(self, intervals))


if __name__ == '__main__':
    unittest.main()
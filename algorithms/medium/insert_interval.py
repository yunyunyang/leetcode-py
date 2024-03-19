# 57. Insert Interval

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merge_intervals = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                merge_intervals.append(newInterval)
                return merge_intervals + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                merge_intervals.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(
                    newInterval[1], intervals[i][1])]

        merge_intervals.append(newInterval)

        return merge_intervals


sol = Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5])

print(sol)

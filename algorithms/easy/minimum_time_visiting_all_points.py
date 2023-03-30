# 1266. Minimum Time Visiting All Points

from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        o = 0
        for i in range(1, len(points)):
            x = abs(points[i][0] - points[i-1][0])
            y = abs(points[i][1] - points[i-1][1])
            o += max(x, y)

        return o
    
sol = Solution().minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]])
print(sol)
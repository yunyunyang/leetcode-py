# 1637. Widest Vertical Area Between Two Points Containing No Points

from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        o = 0
        p = [x for [x,y] in points]
        p.sort()
        for i in range(1, len(p)):
            o = max(o, p[i] - p[i-1])

        return o
    
sol = Solution().maxWidthOfVerticalArea(points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])
print(sol)
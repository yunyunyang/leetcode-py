# 807. Max Increase to Keep City Skyline

from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        v, h, s, o = [], [], len(grid), 0
        for i, x in enumerate(grid):
            v.append(max(x))
            y = []
            for j in range(s):
                y.append(grid[j][i])
            h.append(max(y))
        
        for i in range(s):
            for j in range(s):
            
                o += min(v[i], h[j]) - grid[i][j]

        return o
    
sol = Solution().maxIncreaseKeepingSkyline(grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
print(sol)
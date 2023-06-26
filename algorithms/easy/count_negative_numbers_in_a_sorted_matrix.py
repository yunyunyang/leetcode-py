# 1351. Count Negative Numbers in a Sorted Matrix

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        o = 0
        for r in grid:
            if r[-1] < 0:
                for i in range(len(r)-1, -1, -1):
                    if r[i] < 0:
                        o += 1
                    else:
                        continue

        return o
    
sol = Solution().countNegatives(grid = [[5,1,0],[-5,-5,-5]])
print(sol)

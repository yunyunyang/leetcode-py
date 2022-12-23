# 2373. Largest Local Values in a Matrix

from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maxLocal = []

        for s in range(len(grid) - 2):
            rowLocal = []
            for t in range(len(grid) - 2):
                tmpLocal = []
                for i in range(3):
                    for j in range(3):
                        tmpLocal.append(grid[i + s][j + t])

                rowLocal.append(max(tmpLocal))
                tmpLocal = []
                
            maxLocal.append(rowLocal)
            rowLocal = []

        return maxLocal


sol = Solution().largestLocal(grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
print(sol)
# 2500. Delete Greatest Value in Each Row

from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        output = 0

        for i in range(len(grid[0])):
            maximum = 0
            for j in range(len(grid)):
                row_max = max(grid[j])
                maximum = row_max if row_max > maximum else maximum
                grid[j].remove(row_max)

            output += maximum
            maximum = 0

        return output


sol = Solution().deleteGreatestValue(grid = [[10]])
print(sol)
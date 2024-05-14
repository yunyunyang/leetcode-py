# 1219. Path with Maximum Gold

from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_gold = 0
        visited = set()

        def backtrack(row, col):
            if not (0 <= row < rows and 0 <= col < cols) or (row, col) in visited or grid[row][col] == 0:
                return 0
             
            visited.add((row, col))
            left  = backtrack(row - 1, col)
            right = backtrack(row + 1, col)
            up    = backtrack(row, col - 1)
            down  = backtrack(row, col + 1)
            visited.remove((row, col))

            return grid[row][col] + max(up, down, left, right)

        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] and (row, col) not in visited:
                    max_gold = max(max_gold, backtrack(row, col))

        return max_gold
    
sol = Solution().getMaximumGold(grid = [[0,6,0],[5,8,7],[0,9,0]])
print(sol)
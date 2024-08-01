# 200. Number of Islands

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0

        def dfs(r, c):
            if (r not in range(rows) or 
                c not in range(cols) or
                (r, c) in visit or
                grid[r][c] == "0"):
                return
            
            visit.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    island += 1
                    dfs(r, c)
                    
        return island
    
sol = Solution().numIslands(
  grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
)
print(sol)
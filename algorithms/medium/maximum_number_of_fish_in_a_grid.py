# 2658. Maximum Number of Fish in a Grid

from typing import List

def findMaxFish(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])        
    visit = set()

    def dfs(r, c):
        if (r < 0 or c < 0 or 
            r >= rows or c >= cols or 
            grid[r][c] == 0 or
            (r, c) in visit):
            return 0
        
        visit.add((r, c))
        return (grid[r][c] + 
            dfs(r + 1, c) + 
            dfs(r - 1, c) + 
            dfs(r, c + 1) + 
            dfs(r, c - 1))

    maxFish = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] > 0:
                maxFish = max(maxFish, dfs(r, c))

    return maxFish
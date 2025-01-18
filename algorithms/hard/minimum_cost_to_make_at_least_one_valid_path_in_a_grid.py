# 1368. Minimum Cost to Make at Least One Valid Path in a Grid

from typing import List
from collections import deque

def minCost(self, grid: List[List[int]]) -> int:
    dirs = {
        1: [0, 1],
        2: [0, -1],
        3: [1, 0],
        4: [-1, 0]
    }
    rows, cols = len(grid), len(grid[0])
    q = deque([(0, 0, 0)])  # cost, r, c
    min_cost = { (0,0):0 }  # (r,c) -> cost

    while q:
        cost, r, c = q.popleft()         
        if (r, c) == (rows - 1, cols - 1):
            return cost
        
        for d in dirs:
            dr, dc = dirs[d]
            nr, nc = r + dr, c + dc
            ncost = cost if d == grid[r][c] else cost + 1
            if (nr < 0 or nc < 0 or 
                nr == rows or nc == cols or 
                ncost >= min_cost.get((nr, nc), float('inf'))):
                continue
            
            min_cost[(nr, nc)] = ncost
            if d == grid[r][c]:
                q.appendleft((ncost, nr, nc))
            else:
                q.append((ncost, nr, nc))
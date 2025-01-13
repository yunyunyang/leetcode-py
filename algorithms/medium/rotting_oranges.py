# 994. Rotting Oranges

from typing import List
from collections import deque

def orangesRotting(self, grid: List[List[int]]) -> int:
    q = deque()
    time, fresh = 0, 0
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append([r, c])
    
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while q and fresh > 0:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            for dr, dc in directions:
                if (r + dr not in range(rows) or 
                    c + dc not in range(cols) or 
                    grid[r + dr][c + dc] != 1):
                    continue

                q.append([r + dr, c + dc])
                grid[r + dr][c + dc] = 2
                fresh -= 1
        time += 1
    
    return time if fresh == 0 else -1
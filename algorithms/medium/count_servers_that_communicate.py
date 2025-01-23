# 1267. Count Servers that Communicate

from typing import List

def countServers(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    row_count, col_count =[0] * rows, [0] * cols
    for r in range(rows):
        for c in range(cols):
            row_count[r] += grid[r][c]
            col_count[c] += grid[r][c]

    res = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (row_count[r] > 1 or col_count[c] > 1):
                res += 1

    return res
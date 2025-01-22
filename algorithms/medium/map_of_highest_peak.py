# 1765. Map of Highest Peak

from typing import List
from collections import deque

def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
    rows, cols = len(isWater), len(isWater[0])
    q = deque()
    visit = set()
    res = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if isWater[r][c] == 1:
                q.append((r, c))
                visit.add((r, c))
    
    height = 1
    while q:
        size = len(q)
        for _ in range(size):
            r, c = q.popleft()
            directions = [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]]
            for nr, nc in directions:
                if (nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in visit):
                    continue
                
                res[nr][nc] = height
                visit.add((nr, nc))
                q.append((nr, nc))

        height += 1

    return res
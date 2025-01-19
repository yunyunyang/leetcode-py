# 407. Trapping Rain Water II

from typing import List
from collections import heapq

def trapRainWater(self, heightMap: List[List[int]]) -> int:
    rows, cols = len(heightMap), len(heightMap[0])
    heap = []
    visit = set()
    for r in range(rows):
        for c in range(cols):
            if r in [0, rows - 1] or c in [0, cols - 1]:
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visit.add((r, c))

    res, maxHeight = 0, 0
    while heap:
        h, r, c = heapq.heappop(heap)
        maxHeight = max(maxHeight, h)
        res += maxHeight - h

        dirs = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
        for nr, nc in dirs:
            if (nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in visit):
                continue
            heapq.heappush(heap, (heightMap[nr][nc], nr, nc))
            visit.add((nr, nc))

    return res
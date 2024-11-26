# 2923. Find Champion I

from typing import List

def findChampion(self, grid: List[List[int]]) -> int:
    champion = -1
    teams = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and i not in teams:
                champion = i
                teams.add(j)

    return champion
# 2924. Find Champion II

from typing import List

def findChampion(self, n: int, edges: List[List[int]]) -> int:
    incoming = [0] * n
    for src, dst in edges:
        incoming[dst] += 1

    champions = []
    for i, count in enumerate(incoming):
        if not count:
            champions.append(i)

    return -1 if len(champions) > 1 else champions[0]
# 1743. Restore the Array From Adjacent Pairs

from typing import List
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        res = []
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                res = [node, neighbors[0]]
                break

        while len(res) < len(adjacentPairs) + 1:
            last, prev = res[-1], res[-2]
            candidates = graph[last]
            next_element = candidates[0] if candidates[0] != prev else candidates[1]
            res.append(next_element)

        return res


sol = Solution().restoreArray(adjacentPairs=[[4, -2], [1, 4], [-3, 1]])
print(sol)

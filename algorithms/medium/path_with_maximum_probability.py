# 1514. Path with Maximum Probability

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        pq = [(-1, start_node)]
        visit = set()

        while pq:
            prob, node = heapq.heappop(pq)
            visit.add(node)

            if node == end_node:
                return prob * - 1
            for n, p in adj[node]:
                if n not in visit:
                   heapq.heappush(pq, (p * prob, n))

        return 0
    
sol = Solution().maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start_node = 0, end_node = 2)
print(sol)
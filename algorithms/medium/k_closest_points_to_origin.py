# 973. K Closest Points to Origin

from typing import List
import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            p = points[i]
            d = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(heap, (d * -1, i))
            if len(heap) > k:
                heapq.heappop(heap)

        output = []
        for d, i in heap:
            output.append(points[i])

        return output

sol = Solution().kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2)
print(sol)
# 1046. Last Stone Weight

from typing import List
from heapq import heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            stone *= -1
            heappush(heap, stone)

        while len(heap) > 1:
            x = heappop(heap)
            y = heappop(heap)
            diff = x - y if x < y else y - x
            heappush(heap, diff)

        return heappop(heap) * -1
    
sol = Solution().lastStoneWeight(stones = [2,7,4,1,8,1])
print(sol)
# 3264. Final Array State After K Multiplication Operations I

from typing import List

import heapq

def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
    minHeap = []
    for i, n in enumerate(nums):
        heapq.heappush(minHeap, (n, i))

    for _ in range(k):
        n, i = heapq.heappop(minHeap)
        heapq.heappush(minHeap, (n * multiplier, i))

    output = [0] * len(nums)
    for n, i in minHeap:
        output[i] = n

    return output
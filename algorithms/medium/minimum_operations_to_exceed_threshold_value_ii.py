# 3066. Minimum Operations to Exceed Threshold Value II

from typing import List
from collections import heapq

def minOperations(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    ops = 0

    while nums and nums[0] < k:
        x, y = heapq.heappop(nums), heapq.heappop(nums)
        heapq.heappush(nums, min(x, y) * 2 + max(x, y))
        ops += 1

    return ops
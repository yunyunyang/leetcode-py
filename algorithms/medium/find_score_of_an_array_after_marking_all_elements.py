# 2593. Find Score of an Array After Marking All Elements

from typing import List
import heapq

def findScore(self, nums: List[int]) -> int:
    score, marked = 0, [0] * len(nums)
    heap = []
    for i, n in enumerate(nums):
        heapq.heappush(heap, (n, i))
    
    while heap:
        val, idx = heapq.heappop(heap)
        if marked[idx] == 0:
            score += val
            marked[idx] = 1
            if idx - 1 >= 0:
                marked[idx - 1] = 1
            if idx + 1 <= len(nums) - 1:
                marked[idx + 1] = 1

    return score
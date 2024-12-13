# 2593. Find Score of an Array After Marking All Elements

from typing import List

def findScore(self, nums: List[int]) -> int:
    score, marked = 0, set()
    heap = []
    for i, n in enumerate(nums):
        heapq.heappush(heap, (n, i))
    
    while len(marked) != len(nums):
        val, idx = heapq.heappop(heap)
        if idx not in marked:
            score += val
            marked.add(idx)
            if idx - 1 >= 0:
                marked.add(idx - 1)
            if idx + 1 <= len(nums) - 1:
                marked.add(idx + 1)

    return score
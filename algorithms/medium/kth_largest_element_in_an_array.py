# 215. Kth Largest Element in an Array

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


sol = Solution().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2)
print(sol)

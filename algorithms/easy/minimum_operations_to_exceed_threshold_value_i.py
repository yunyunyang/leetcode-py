# 3065. Minimum Operations to Exceed Threshold Value I

from typing import List
import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        ops = 0
        while nums[0] < k:
            ops += 1
            heapq.heappop(nums)

        return ops


sol = Solution().minOperations(nums=[2, 11, 10, 1, 3], k=10)
print(sol)

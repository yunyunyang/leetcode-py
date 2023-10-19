# 643. Maximum Average Subarray I

import sys
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = cursum = sum(nums[:k])

        for i in range(len(nums) - k):
            cursum = cursum - nums[i] + nums[i+k]
            maxsum = max(maxsum, cursum)

        return maxsum / k


sol = Solution().findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4)
print(sol)

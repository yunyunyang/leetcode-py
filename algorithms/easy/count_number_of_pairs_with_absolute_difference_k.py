# 2006. Count Number of Pairs With Absolute Difference K

import enum
from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        output = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i < j and abs(nums[i] - nums[j]) == k:
                    output += 1

        return output

sol = Solution().countKDifference(nums = [1,2,2,1], k = 1)
print(sol)

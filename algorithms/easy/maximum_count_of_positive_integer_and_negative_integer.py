# 2529. Maximum Count of Positive Integer and Negative Integer

from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        o, r = 0, len(nums)
        if nums[0] > 0:
            return len(nums)
        else:
            for i in range(len(nums)):
                r = r - 1
                if nums[i] < 0 or nums[r] > 0:
                    o += 1

        return o
    
sol = Solution().maximumCount(nums = [-2,-1,-1,1,2,3])
print(sol)
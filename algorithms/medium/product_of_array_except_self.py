# 238. Product of Array Except Self

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        o = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            o[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            o[i] *= postfix
            postfix *= nums[i]

        return o
    
sol = Solution().productExceptSelf(nums = [-1,1,0,-3,3])
print(sol)
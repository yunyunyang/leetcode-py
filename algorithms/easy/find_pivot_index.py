# 724. Find Pivot Index

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        forward = [0] * len(nums)
        backward = [0] * len(nums)
        
        for i in range(1, len(nums)):
            forward[i] = forward[i - 1] + nums[i - 1]
            
        for i in range(len(nums) - 2, -1, -1):
            backward[i] = backward[i + 1] + nums[i + 1]
        
        for i in range(len(nums)):
            if forward[i] == backward[i]:
                return i
            
        return -1
            
sol = Solution().pivotIndex(nums = [1,7,3,6,5,6])
print(sol)
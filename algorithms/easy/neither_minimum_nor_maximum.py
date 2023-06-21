# 2733. Neither Minimum nor Maximum

from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        
        nums.sort()
        return nums[1]
    
sol = Solution().findNonMinOrMax(nums = [3,2,1,4])
print(sol)
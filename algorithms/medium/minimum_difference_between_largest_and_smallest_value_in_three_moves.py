# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        output = float("inf")
        
        for l in range(4):
            r = len(nums) - 4 + l
            output = min(output, nums[r] - nums[l])

        return output
    
sol = Solution().minDifference(nums = [1,5,0,10,14])
print(sol)
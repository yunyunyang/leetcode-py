# 1608. Special Array With X Elements Greater Than or Equal X

from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        if nums[0] >= n:
            return n
        
        for i in range(1, len(nums)):
            if nums[i] >= n - i and nums[i-1] < n - i:                
                return n - i
                
        return -1
    
sol = Solution().specialArray(nums = [3,6,7,7,0])
print(sol)
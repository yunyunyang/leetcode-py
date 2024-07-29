# 219. Contains Duplicate II

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = {}
        for i in range(len(nums)):
            n = nums[i]
                
            if n in hset and i - hset[n] <= k:
                return True
            
            hset[n] = i
            
        return False
    
sol = Solution().containsNearbyDuplicate(nums = [1,0,1,1], k = 1)
print(sol)
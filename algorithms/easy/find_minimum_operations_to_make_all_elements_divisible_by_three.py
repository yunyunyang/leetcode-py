# 3190. Find Minimum Operations to Make All Elements Divisible by Three

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for n in nums:
            if n % 3 != 0:
                ops += 1
                
        return ops
    
sol = Solution().minimumOperations(nums = [1,2,3,4])
print(sol)
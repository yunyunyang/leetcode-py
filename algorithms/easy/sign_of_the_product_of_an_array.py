# 1822. Sign of the Product of an Array

from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        r = 1
        for i in nums:
            r *= i

        if r == 0:
            return 0
        elif r > 0:
            return 1
        else:
            return -1
    
sol = Solution().arraySign(nums = [-1,1,-1,1,-1])
print(sol)
# 137. Single Number II

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        
        return [k for k, v in m.items() if v == 1][0]
    
sol = Solution().singleNumber(nums = [2,2,3,2])
print(sol)
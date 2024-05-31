# 260. Single Number III

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        output = []
        for k, v in d.items():
            if v == 1:
                output.append(k)
            
        return output
    
sol = Solution().singleNumber(nums = [1,2,1,3,2,5])
print(sol)
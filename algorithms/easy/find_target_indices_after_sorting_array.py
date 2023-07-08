# 2089. Find Target Indices After Sorting Array

from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        o = []
        for i, n in enumerate(nums):
            if n == target:
                o.append(i)
            if n > target:
                return o
            
        return o
    
sol = Solution().targetIndices(nums = [1,2,5,2,3], target = 2)
print(sol)
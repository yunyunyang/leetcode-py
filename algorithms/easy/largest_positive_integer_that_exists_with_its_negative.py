# 2441. Largest Positive Integer That Exists With Its Negative

from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nset = set(nums)
        maxk = -1
        for n in nset:
            if -n in nset:
                maxk = max(maxk, n)

        return maxk
    
sol = Solution().findMaxK(nums = [-1,10,6,7,-7,1])
print(sol)
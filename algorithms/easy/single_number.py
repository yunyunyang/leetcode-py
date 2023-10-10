# 136. Single Number

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        o = 0
        for n in nums:
            o = o ^ n
        return o


sol = Solution().singleNumber(nums=[2, 2, 1])
print(sol)

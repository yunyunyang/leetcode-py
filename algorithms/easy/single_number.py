# 136. Single Number

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            counter = {}
            for i in nums:
                if i in counter:
                    counter.update({i: counter.get(i)+1})
                else:
                    counter.update({i: 1})

            for k, v in counter.items():
                if v == 1:
                    return k


sol = Solution().singleNumber(nums = [2,2,1])
print(sol)
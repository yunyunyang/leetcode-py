# 1. Two Sum

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for k, v in enumerate(nums):
            tmp = target - v
            if tmp in hm:
                return [k, hm.get(tmp)]
            else:
                hm.update({v: k})


sol = Solution().twoSum(nums = [2,7,11,15], target = 9)
print(sol)
# 448. Find All Numbers Disappeared in an Array

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        map = {}
        for i in range(1, len(nums) + 1):
            if i not in map:
                map[i] = 0

            n = nums[i-1]
            if n not in map:
                map[n] = 1
            else:
                map[n] += 1

        return [k for k, v in map.items() if v == 0]


sol = Solution().findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1])
print(sol)

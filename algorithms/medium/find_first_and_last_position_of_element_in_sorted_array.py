# 34. Find First and Last Position of Element in Sorted Array

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = -1, -1

        for i in range(len(nums)):
            if l == -1 and nums[i] == target:
                l = i

                while i < len(nums) and nums[i] == target:
                    i += 1

                r = i - 1
            # return [l, r]

        return [l, r]


sol = Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6)
print(sol)

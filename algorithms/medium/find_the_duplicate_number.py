# 287. Find the Duplicate Number

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]


sol = Solution().findDuplicate(nums=[1, 3, 4, 2, 2])
print(sol)

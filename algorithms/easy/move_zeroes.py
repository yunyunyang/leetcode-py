# 283. Move Zeroes

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonz = []
        for i, n in enumerate(nums):
            if n != 0:
                nonz.append(i)

        for i, n in enumerate(nonz):
            nums[i] = nums[n]

        for i in range(len(nonz), len(nums)):
            nums[i] = 0

        print(nums)


sol = Solution().moveZeroes(nums=[0, 1])
print(sol)

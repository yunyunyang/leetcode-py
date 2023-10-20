# 977. Squares of a Sorted Array
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i, n in enumerate(nums):
            nums[i] = n ** 2

        nums.sort()
        return nums


sol = Solution().sortedSquares(nums=[-4, -1, 0, 3, 10])
print(sol)

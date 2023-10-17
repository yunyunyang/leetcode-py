# 2778. Sum of Squares of Special Elements

from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        s, n = 0, len(nums)
        for i, num in enumerate(nums):
            if n % (i + 1) == 0:
                s += num ** 2

        return s


sol = Solution().sumOfSquares(nums=[1, 2, 3, 4])
print(sol)

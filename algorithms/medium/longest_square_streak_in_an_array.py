# 2501. Longest Square Streak in an Array

from typing import List

def longestSquareStreak(self, nums: List[int]) -> int:
    nums_set = set(nums)
    nums.sort()
    count, res = {}, -1

    for n in nums:
        val, length = n, 0
        while val in nums_set:
            length += 1
            val = val ** 2

        count[n] = length
        if length > 1:
            res = max(res, length)

    return res
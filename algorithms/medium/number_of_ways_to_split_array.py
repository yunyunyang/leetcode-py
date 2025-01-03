# 2270. Number of Ways to Split Array

from typing import List

def waysToSplitArray(self, nums: List[int]) -> int:
    totalSum, curSum = sum(nums), 0
    count = 0
    for i in range(len(nums) - 1):
        curSum += nums[i]
        totalSum -= nums[i]
        if curSum >= totalSum:
            count += 1

    return count
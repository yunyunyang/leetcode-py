# 1752. Check if Array Is Sorted and Rotated

from typing import List

def check(self, nums: List[int]) -> bool:
    n = len(nums)
    count = 1
    if n == 1: 
        return True

    for i in range(1, 2 * n):
        if nums[i % n] >= nums[(i % n) - 1]:
            count += 1
        else:
            count = 1

        if count == n:
            return True

    return False
# 162. Find Peak Element

from typing import List

def findPeakElement(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if mid > 0 and nums[mid - 1] > nums[mid]:
            right = mid - 1
        elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
            left = mid + 1
        else:
            return mid

    return -1
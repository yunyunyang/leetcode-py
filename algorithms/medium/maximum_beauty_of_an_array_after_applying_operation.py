# 2779. Maximum Beauty of an Array After Applying Operation

from typing import List

def maximumBeauty(self, nums: List[int], k: int) -> int:
    nums.sort()
    longest = 1
    for i in range(len(nums)):
        left = i + 1
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            target = nums[i] + k * 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        longest = max(longest, left - i)

    return longest
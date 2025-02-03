# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

from typing import List

def longestMonotonicSubarray(self, nums: List[int]) -> int:
    inc_length = dec_length = max_length = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            inc_length += 1
            dec_length = 1
        elif nums[i] < nums[i - 1]:
            dec_length += 1
            inc_length = 1
        else:
            inc_length = dec_length = 1
        
        max_length = max(max_length, inc_length, dec_length)

    return max_length
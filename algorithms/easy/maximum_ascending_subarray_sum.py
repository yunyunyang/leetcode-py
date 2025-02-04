# 1800. Maximum Ascending Subarray Sum

from typing import List

def maxAscendingSum(self, nums: List[int]) -> int:
    nums.append(0)
    max_sum, cur_sum = 0, nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            cur_sum += nums[i]
        else:
            max_sum = max(max_sum, cur_sum)
            cur_sum = nums[i]
    
    return max_sum
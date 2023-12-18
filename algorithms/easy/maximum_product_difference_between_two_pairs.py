# 1913. Maximum Product Difference Between Two Pairs

from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) - 1
        return (nums[n]*nums[n-1]) - (nums[0]*nums[1])


sol = Solution().maxProductDifference(nums=[5, 6, 2, 7, 4])
print(sol)

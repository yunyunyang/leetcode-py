# 268. Missing Number

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        sum_n = sum(nums) 
        sum_a = int(n * (n-1) / 2)
        return sum_a - sum_n


sol = Solution().missingNumber(nums = [0,1])
print(sol)